.. _Run Open edX Without Tutor:

How to Run Open edX (edx-platform) Without Tutor
################################################

.. tags:: site operator, how-to

This guide provides a checklist for running the Open edX platform (edx-platform)
directly on Ubuntu without using Tutor. This approach requires manual setup of
all dependent services and is intended for system administrators who need
fine-grained control over their deployment or development environment.

.. warning::

   Running Open edX without Tutor is significantly more complex than using the
   officially supported Tutor installation method. This approach requires
   extensive system administration knowledge and is not recommended for production
   deployments unless you have specific requirements that prevent using Tutor.

Prerequisites
*************

* Ubuntu 24.04 LTS
* Root or sudo access
* Minimum 8GB RAM (16GB+ recommended for production)
* Basic familiarity with Django applications
* Understanding of service management (systemd)

Required Services Overview
**************************

The Open edX platform requires the following services to be running:

* **MySQL 8.0** - Primary relational database
* **MongoDB 7.0** - Document storage for modulestore (course content)
* **Redis 7.x** - Caching and Celery broker
* **Memcached** - Application caching layer
* **Elasticsearch 7.x** - Course search functionality

Installation Steps
******************

1. Install System Dependencies
==============================

Install required packages:

.. code-block:: bash

   sudo apt-get update
   sudo apt-get install -y \
       build-essential \
       git \
       libffi-dev \
       libmysqlclient-dev \
       libssl-dev \
       libxml2-dev \
       libxslt1-dev \
       libjpeg-dev \
       libpng-dev \
       python3.11 \
       python3.11-dev \
       python3-pip \
       python3-venv

**Test this step:**

.. code-block:: bash

   python3.11 --version
   git --version

2. Install and Configure MySQL
==============================

Install MySQL 8.0:

.. code-block:: bash

   sudo apt-get install -y mysql-server mysql-client
   sudo systemctl start mysql
   sudo systemctl enable mysql

**Test this step:**

.. code-block:: bash

   sudo systemctl status mysql
   mysql --version

Create required databases and users:

.. code-block:: bash

   sudo mysql -e "CREATE DATABASE edxapp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
   sudo mysql -e "CREATE DATABASE edxapp_csmh CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
   sudo mysql -e "CREATE USER 'edxapp'@'localhost' IDENTIFIED BY 'your_password';"
   sudo mysql -e "GRANT ALL PRIVILEGES ON edxapp.* TO 'edxapp'@'localhost';"
   sudo mysql -e "GRANT ALL PRIVILEGES ON edxapp_csmh.* TO 'edxapp'@'localhost';"
   sudo mysql -e "FLUSH PRIVILEGES;"

.. note::

   Replace ``your_password`` with a strong password. Store it securely for use in Django settings.

**Test database creation:**

.. code-block:: bash

   mysql -u edxapp -p -e "SHOW DATABASES;"
   # Should list edxapp and edxapp_csmh databases

3. Install and Configure MongoDB
================================

Install MongoDB 7.0:

.. code-block:: bash

   wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | sudo apt-key add -
   echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | \
       sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
   sudo apt-get update
   sudo apt-get install -y mongodb-org
   sudo systemctl start mongod
   sudo systemctl enable mongod

**Test this step:**

.. code-block:: bash

   sudo systemctl status mongod
   mongosh --eval "db.version()"

Create MongoDB database and user:

.. code-block:: bash

   mongosh <<EOF
   use edxapp
   db.createUser({
       user: "edxapp",
       pwd: "your_mongodb_password",
       roles: [{role: "readWrite", db: "edxapp"}]
   })
   EOF

**Test MongoDB access:**

.. code-block:: bash

   mongosh -u edxapp -p your_mongodb_password --authenticationDatabase edxapp --eval "db.getName()"
   # Should return: edxapp

4. Install and Configure Redis
==============================

Install Redis:

.. code-block:: bash

   sudo apt-get install -y redis-server
   sudo systemctl start redis-server
   sudo systemctl enable redis-server

**Test this step:**

.. code-block:: bash

   sudo systemctl status redis-server
   redis-cli ping
   # Should return: PONG

5. Install and Configure Memcached
==================================

Install Memcached:

.. code-block:: bash

   sudo apt-get install -y memcached
   sudo systemctl start memcached
   sudo systemctl enable memcached

**Test this step:**

.. code-block:: bash

   sudo systemctl status memcached
   echo "stats" | nc localhost 11211
   # Should return memcached statistics

6. Install and Configure Elasticsearch
======================================

Install Elasticsearch 7.x:

.. code-block:: bash

   wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
   echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | \
       sudo tee /etc/apt/sources.list.d/elastic-7.x.list
   sudo apt-get update
   sudo apt-get install -y elasticsearch
   sudo systemctl start elasticsearch
   sudo systemctl enable elasticsearch

**Test this step:**

.. code-block:: bash

   # Wait 30 seconds for Elasticsearch to fully start
   sleep 30
   curl -X GET "localhost:9200/"
   # Should return JSON with cluster information

7. Install Node.js and Build Tools
==================================

Install Node.js 18.x:

.. code-block:: bash

   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs

**Test this step:**

.. code-block:: bash

   node --version
   # Should return: v18.x.x
   npm --version
   # Should return: 9.x.x or higher

8. Clone edx-platform Repository
================================

Choose your installation directory and clone the repository:

.. code-block:: bash

   cd /opt
   sudo git clone https://github.com/openedx/edx-platform.git
   cd edx-platform

   # Checkout a specific release (recommended for stability)
   sudo git checkout open-release/sumac.master
   # OR stay on master for latest development code
   # sudo git checkout master

**Test this step:**

.. code-block:: bash

   ls -la /opt/edx-platform
   git log -1
   # Should show the latest commit

9. Create Python Virtual Environment
====================================

Create and activate a virtual environment:

.. code-block:: bash

   cd /opt/edx-platform
   sudo python3.11 -m venv venv
   sudo chown -R $USER:$USER venv
   source venv/bin/activate

**Test this step:**

.. code-block:: bash

   which python
   # Should return: /opt/edx-platform/venv/bin/python
   python --version
   # Should return: Python 3.11.x

10. Install Python Requirements
===============================

Install edx-platform Python dependencies:

.. code-block:: bash

   pip install --upgrade pip setuptools wheel
   pip install -r requirements/edx/base.txt

.. note::

   This step may take 15-30 minutes depending on your system. If you encounter
   errors, you may need to install additional system libraries.

**Test this step:**

.. code-block:: bash

   pip list | grep -i django
   # Should show Django and related packages
   pip list | grep -i celery
   # Should show Celery

11. Install Node.js Dependencies and Build Assets
=================================================

Install JavaScript dependencies and build static assets:

.. code-block:: bash

   npm clean-install
   npm run build

.. note::

   This step may take 10-20 minutes and requires significant memory.

**Test this step:**

.. code-block:: bash

   ls node_modules/ | wc -l
   # Should show hundreds of packages
   ls -la lms/static/
   # Should show compiled assets

12. Create Configuration Files
==============================

Create the configuration directory:

.. code-block:: bash

   sudo mkdir -p /edx/etc
   sudo chown -R $USER:$USER /edx

Create LMS configuration file at ``/edx/etc/lms.yml``:

.. code-block:: yaml

   PLATFORM_NAME: "Your Open edX Site"
   LMS_BASE: "localhost:8000"
   LMS_ROOT_URL: "http://localhost:8000"
   CMS_BASE: "localhost:8001"

   DATABASES:
     default:
       ENGINE: django.db.backends.mysql
       NAME: edxapp
       USER: edxapp
       PASSWORD: your_password
       HOST: localhost
       PORT: 3306

   MODULESTORE:
     default:
       ENGINE: xmodule.modulestore.mongo.MongoModuleStore
       OPTIONS:
         host: localhost
         port: 27017
         user: edxapp
         password: your_mongodb_password
         db: edxapp

   CACHES:
     default:
       BACKEND: django.core.cache.backends.memcached.PyMemcacheCache
       LOCATION: 127.0.0.1:11211

   CELERY_BROKER_URL: redis://localhost:6379/0

   ELASTIC_SEARCH_CONFIG:
     - host: localhost
       port: 9200

   # MFE Configuration
   MFE_CONFIG:
     LEARNING_BASE_URL: http://localhost:2000
     ACCOUNT_SETTINGS_URL: http://localhost:1997
     ACCOUNT_PROFILE_URL: http://localhost:1995
     DISCUSSIONS_MFE_BASE_URL: http://localhost:2002
     GRADEBOOK_BASE_URL: http://localhost:1994
     AUTHN_BASE_URL: http://localhost:1999

   # CORS Configuration for MFEs
   CORS_ORIGIN_WHITELIST:
     - http://localhost:1999
     - http://localhost:1995
     - http://localhost:1997
     - http://localhost:2000
     - http://localhost:2002
     - http://localhost:1994
     - http://localhost:2001

   CORS_ALLOW_CREDENTIALS: true
   CORS_ALLOW_HEADERS:
     - '*'

   # Login redirect whitelist
   LOGIN_REDIRECT_WHITELIST:
     - localhost:1999
     - localhost:1995
     - localhost:1997
     - localhost:2000
     - localhost:2002
     - localhost:1994
     - localhost:2001

   # Enable MFE features
   FEATURES:
     ENABLE_AUTHN_MICROFRONTEND: true
     ENABLE_DISCUSSION_HOME_PANEL: true
     ENABLE_DISCUSSIONS_MFE: true

   # Session cookie settings
   SESSION_COOKIE_DOMAIN: localhost
   SESSION_COOKIE_SAMESITE: Lax

Create CMS (Studio) configuration file at ``/edx/etc/cms.yml``:

.. code-block:: yaml

   PLATFORM_NAME: "Your Open edX Site"
   CMS_BASE: "localhost:8001"
   LMS_BASE: "localhost:8000"
   LMS_ROOT_URL: "http://localhost:8000"

   DATABASES:
     default:
       ENGINE: django.db.backends.mysql
       NAME: edxapp
       USER: edxapp
       PASSWORD: your_password
       HOST: localhost
       PORT: 3306

   MODULESTORE:
     default:
       ENGINE: xmodule.modulestore.mongo.MongoModuleStore
       OPTIONS:
         host: localhost
         port: 27017
         user: edxapp
         password: your_mongodb_password
         db: edxapp

   CACHES:
     default:
       BACKEND: django.core.cache.backends.memcached.PyMemcacheCache
       LOCATION: 127.0.0.1:11211

   CELERY_BROKER_URL: redis://localhost:6379/0

Create authentication file at ``/edx/etc/lms.auth.json``:

.. code-block:: json

   {
     "SECRET_KEY": "your-secret-key-change-this",
     "MYSQL_PASSWORD": "your_password",
     "MONGO_PASSWORD": "your_mongodb_password"
   }

Create ``/edx/etc/cms.auth.json`` with the same structure.

.. warning::

   Generate a strong SECRET_KEY using:
   ``python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"``

**Test this step:**

.. code-block:: bash

   ls -la /edx/etc/
   # Should show lms.yml, cms.yml, lms.auth.json, cms.auth.json
   cat /edx/etc/lms.yml | grep PLATFORM_NAME
   # Should show your platform name

13. Run Database Migrations
===========================

Apply Django migrations:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate

   # Run migrations for LMS
   ./manage.py lms migrate --settings=lms.envs.production

   # Run migrations for CMS
   ./manage.py cms migrate --settings=cms.envs.production

**Test this step:**

.. code-block:: bash

   mysql -u edxapp -p -e "USE edxapp; SHOW TABLES;" | wc -l
   # Should show 200+ tables

14. Create Django Superuser
===========================

Create an administrative user:

.. code-block:: bash

   ./manage.py lms createsuperuser --settings=lms.envs.production

**Test this step:**

.. code-block:: bash

   mysql -u edxapp -p -e "USE edxapp; SELECT username, email FROM auth_user WHERE is_superuser=1;"
   # Should show your superuser

15. Collect Static Assets
=========================

Collect Django static files:

.. code-block:: bash

   ./manage.py lms collectstatic --noinput --settings=lms.envs.production
   ./manage.py cms collectstatic --noinput --settings=cms.envs.production

**Test this step:**

.. code-block:: bash

   ls -la /opt/edx-platform/staticfiles/
   # Should show collected static files

16. Clone and Set Up MFEs
=========================

Open edX uses React-based Micro-Frontends (MFEs) for key user-facing features.
Set these up before starting the servers.

Essential MFEs
--------------

The following MFEs are required for basic functionality:

* **frontend-app-authn** (port 1999) - Login and registration pages
* **frontend-app-learning** (port 2000) - Course experience
* **frontend-app-account** (port 1997) - User account settings
* **frontend-app-profile** (port 1995) - User profile pages
* **frontend-app-discussions** (port 2002) - Course discussions/forums
* **frontend-app-gradebook** (port 1994) - Instructor gradebook

Clone and Configure frontend-app-authn
--------------------------------------

.. code-block:: bash

   cd /opt
   sudo git clone https://github.com/openedx/frontend-app-authn.git
   cd frontend-app-authn
   sudo git checkout open-release/sumac.master
   sudo chown -R $USER:$USER /opt/frontend-app-authn
   npm clean-install

Create ``.env.development`` file:

.. code-block:: bash

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:1999
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Your Open edX Site
   LOGO_URL=http://localhost:8000/static/images/logo.png
   FAVICON_URL=http://localhost:8000/static/images/favicon.ico
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   EOF

**Test this step:**

.. code-block:: bash

   npm run build
   ls dist/
   # Should show built files

Clone and Configure frontend-app-learning
------------------------------------------

.. code-block:: bash

   cd /opt
   sudo git clone https://github.com/openedx/frontend-app-learning.git
   cd frontend-app-learning
   sudo git checkout open-release/sumac.master
   sudo chown -R $USER:$USER /opt/frontend-app-learning
   npm clean-install

Create ``.env.development`` file:

.. code-block:: bash

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:2000
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Your Open edX Site
   LOGO_URL=http://localhost:8000/static/images/logo.png
   FAVICON_URL=http://localhost:8000/static/images/favicon.ico
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   EOF

**Test this step:**

.. code-block:: bash

   npm run build
   ls dist/
   # Should show built files

Clone and Configure frontend-app-account
----------------------------------------

.. code-block:: bash

   cd /opt
   sudo git clone https://github.com/openedx/frontend-app-account.git
   cd frontend-app-account
   sudo git checkout open-release/sumac.master
   sudo chown -R $USER:$USER /opt/frontend-app-account
   npm clean-install

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:1997
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Your Open edX Site
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   EOF

**Test:** ``npm run build && ls dist/``

Clone and Configure frontend-app-profile
----------------------------------------

.. code-block:: bash

   cd /opt
   sudo git clone https://github.com/openedx/frontend-app-profile.git
   cd frontend-app-profile
   sudo git checkout open-release/sumac.master
   sudo chown -R $USER:$USER /opt/frontend-app-profile
   npm clean-install

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:1995
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Your Open edX Site
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   EOF

**Test:** ``npm run build && ls dist/``

Clone and Configure frontend-app-discussions
--------------------------------------------

.. code-block:: bash

   cd /opt
   sudo git clone https://github.com/openedx/frontend-app-discussions.git
   cd frontend-app-discussions
   sudo git checkout open-release/sumac.master
   sudo chown -R $USER:$USER /opt/frontend-app-discussions
   npm clean-install

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:2002
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Your Open edX Site
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   EOF

**Test:** ``npm run build && ls dist/``

Clone and Configure frontend-app-gradebook
------------------------------------------

.. code-block:: bash

   cd /opt
   sudo git clone https://github.com/openedx/frontend-app-gradebook.git
   cd frontend-app-gradebook
   sudo git checkout open-release/sumac.master
   sudo chown -R $USER:$USER /opt/frontend-app-gradebook
   npm clean-install

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:1994
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Your Open edX Site
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   EOF

**Test:** ``npm run build && ls dist/``

.. note::

   **Shared Components**: MFEs use shared header and footer components (``frontend-component-header`` and ``frontend-component-footer``). These are automatically installed as npm dependencies and do not need separate setup.

17. Start LMS and CMS Servers
=============================

Now that all configuration is complete, start the backend servers.

In Development
--------------

Open separate terminal windows for each service. In each terminal, activate the virtual environment first:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate

Terminal 1 - Start LMS:

.. code-block:: bash

   ./manage.py lms runserver 0.0.0.0:8000 --settings=lms.envs.production

Terminal 2 - Start CMS:

.. code-block:: bash

   ./manage.py cms runserver 0.0.0.0:8001 --settings=cms.envs.production

**Test this step:**

.. code-block:: bash

   # In a new terminal
   curl -I http://localhost:8000
   # Should return HTTP 200 or 302
   curl -I http://localhost:8001
   # Should return HTTP 200 or 302

For Production
--------------

Use Gunicorn as the WSGI server:

.. code-block:: bash

   pip install gunicorn

   # Start LMS
   gunicorn -c /opt/edx-platform/lms/envs/gunicorn.py lms.wsgi:application

   # Start CMS (in separate terminal)
   gunicorn -c /opt/edx-platform/cms/envs/gunicorn.py cms.wsgi:application

18. Start Celery Workers
========================

Open edX uses Celery for asynchronous task processing. Start workers in separate terminals:

Terminal 3 - LMS Celery worker:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate
   celery -A lms.celery worker --loglevel=info

Terminal 4 - CMS Celery worker:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate
   celery -A cms.celery worker --loglevel=info

**Test this step:**

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate
   celery -A lms.celery inspect active
   # Should connect and show active tasks (may be empty)

19. Start MFE Development Servers
=================================

Start each MFE in a separate terminal:

Terminal 5 - frontend-app-authn:

.. code-block:: bash

   cd /opt/frontend-app-authn
   npm run start

Terminal 6 - frontend-app-learning:

.. code-block:: bash

   cd /opt/frontend-app-learning
   npm run start

Terminal 7 - frontend-app-account:

.. code-block:: bash

   cd /opt/frontend-app-account
   npm run start

Terminal 8 - frontend-app-profile:

.. code-block:: bash

   cd /opt/frontend-app-profile
   npm run start

Terminal 9 - frontend-app-discussions:

.. code-block:: bash

   cd /opt/frontend-app-discussions
   npm run start

Terminal 10 - frontend-app-gradebook:

.. code-block:: bash

   cd /opt/frontend-app-gradebook
   npm run start

**Test each MFE:**

.. code-block:: bash

   curl -I http://localhost:1999  # authn
   curl -I http://localhost:2000  # learning
   curl -I http://localhost:1997  # account
   curl -I http://localhost:1995  # profile
   curl -I http://localhost:2002  # discussions
   curl -I http://localhost:1994  # gradebook
   # Each should return HTTP 200

20. Full Integration Verification
=================================

Test the complete system:

1. **Verify all services are running:**

   .. code-block:: bash

      sudo systemctl status mysql
      sudo systemctl status mongod
      sudo systemctl status redis-server
      sudo systemctl status memcached
      sudo systemctl status elasticsearch

2. **Access the LMS:**

   Open a browser and navigate to ``http://localhost:8000``

   You should see the LMS home page with the login button linking to the authn MFE.

3. **Access CMS (Studio):**

   Navigate to ``http://localhost:8001``

   You should see the Studio login page.

4. **Test authentication:**

   Click the login button. You should be redirected to ``http://localhost:1999/login``

   Log in with your superuser credentials.

5. **Test course experience:**

   Create a test course in Studio (``http://localhost:8001``)

   Navigate to the course from the LMS. The course content should load in the Learning MFE (``http://localhost:2000``)

6. **Test profile:**

   Click on your username in the LMS header

   Select "Profile" - should navigate to ``http://localhost:1995``

7. **Test account settings:**

   From the user menu, select "Account" - should navigate to ``http://localhost:1997``

8. **Verify all MFE ports respond:**

   .. code-block:: bash

      for port in 1994 1995 1997 1999 2000 2002; do
          echo -n "Port $port: "
          curl -s -o /dev/null -w "%{http_code}" http://localhost:$port
          echo
      done
      # All should return 200

Development Workflow Tips
*************************

Managing Multiple Processes
===========================

Running Open edX without Tutor means managing many processes simultaneously. Here are strategies to help:

Using Terminal Multiplexer (tmux)
---------------------------------

Use tmux to manage multiple terminal sessions:

.. code-block:: bash

   # Install tmux
   sudo apt-get install -y tmux

   # Start a new tmux session
   tmux new -s openedx

   # Create windows for each service (Ctrl-b c to create new window)
   # Window 0: LMS
   cd /opt/edx-platform && source venv/bin/activate
   ./manage.py lms runserver 0.0.0.0:8000 --settings=lms.envs.production

   # Window 1: CMS (Ctrl-b c)
   cd /opt/edx-platform && source venv/bin/activate
   ./manage.py cms runserver 0.0.0.0:8001 --settings=cms.envs.production

   # Window 2: LMS Celery worker
   cd /opt/edx-platform && source venv/bin/activate
   celery -A lms.celery worker --loglevel=info

   # Window 3: CMS Celery worker
   cd /opt/edx-platform && source venv/bin/activate
   celery -A cms.celery worker --loglevel=info

   # Windows 4-9: Individual MFEs
   # Navigate between windows with Ctrl-b <number>
   # Detach from session: Ctrl-b d
   # Reattach to session: tmux attach -t openedx

Using Process Managers
----------------------

For a more robust solution, use supervisord for managing services:

.. code-block:: bash

   sudo apt-get install -y supervisor

Create supervisor configuration files in ``/etc/supervisor/conf.d/`` for each service.

Example for LMS (``/etc/supervisor/conf.d/edxapp-lms.conf``):

.. code-block:: ini

   [program:edxapp-lms]
   command=/opt/edx-platform/venv/bin/python /opt/edx-platform/manage.py lms runserver 0.0.0.0:8000 --settings=lms.envs.production
   directory=/opt/edx-platform
   user=www-data
   autostart=true
   autorestart=true
   stdout_logfile=/var/log/supervisor/edxapp-lms.log
   stderr_logfile=/var/log/supervisor/edxapp-lms-error.log

Reload supervisor after adding configuration:

.. code-block:: bash

   sudo supervisorctl reread
   sudo supervisorctl update
   sudo supervisorctl start all

Using Shell Scripts
-------------------

Create helper scripts to start/stop all services:

.. code-block:: bash

   mkdir -p /opt/scripts
   cat > /opt/scripts/start-all.sh << 'EOF'
   #!/bin/bash
   # Start backend services
   cd /opt/edx-platform
   source venv/bin/activate
   ./manage.py lms runserver 0.0.0.0:8000 --settings=lms.envs.production &
   ./manage.py cms runserver 0.0.0.0:8001 --settings=cms.envs.production &
   celery -A lms.celery worker --loglevel=info &
   celery -A cms.celery worker --loglevel=info &

   # Start MFEs
   cd /opt/frontend-app-authn && npm run start &
   cd /opt/frontend-app-learning && npm run start &
   cd /opt/frontend-app-account && npm run start &
   cd /opt/frontend-app-profile && npm run start &
   cd /opt/frontend-app-discussions && npm run start &
   cd /opt/frontend-app-gradebook && npm run start &

   echo "All services started"
   wait
   EOF

Make the script executable:

.. code-block:: bash

   chmod +x /opt/scripts/start-all.sh

Production Considerations
*************************

For production deployments, additional configuration is required:

Separate Services
=================

In this development setup, all services run on a single server. For production:

* Run MySQL, MongoDB, Redis, Memcached, and Elasticsearch on dedicated servers or use managed services
* Distribute load across multiple LMS/CMS application servers
* Use a load balancer to distribute traffic

Web Server Configuration
========================

* Install and configure Nginx or Apache as a reverse proxy
* Configure SSL/TLS certificates for all domains
* Set up proper logging and log rotation
* Configure static and media file serving
* Enable HTTP/2 and compression

Service Management
==================

* Create systemd service files for LMS, CMS, and Celery workers
* Set up automatic restart on failure
* Configure resource limits and monitoring
* Use supervisord or systemd for process management

Security Hardening
==================

* Use strong passwords for all database users
* Configure firewall rules (ufw or iptables)
* Keep all services updated with security patches
* Use separate database users with minimal required privileges
* Configure ALLOWED_HOSTS in Django settings
* Disable DEBUG mode in production settings
* Set secure cookie flags (Secure, HttpOnly, SameSite)
* Implement rate limiting

Performance Optimization
========================

* Configure appropriate worker counts for Gunicorn
* Tune MySQL, MongoDB, and Elasticsearch for your workload
* Set up CDN for static assets
* Configure Redis persistence appropriately
* Enable Django caching layers
* Optimize database indexes
* Enable query caching

Monitoring and Logging
======================

* Set up application monitoring (e.g., New Relic, Datadog)
* Configure centralized logging (e.g., ELK stack)
* Monitor service health and resource usage
* Set up alerting for critical issues
* Track application performance metrics
* Monitor error rates and response times

MFE Production Deployment
=========================

For production, MFEs should be built and served as static files rather than using the development server.

Build MFEs for Production
-------------------------

For each MFE, create a ``.env.production`` file with production URLs:

.. code-block:: bash

   cd /opt/frontend-app-learning

   # Create production environment file
   cat > .env.production << 'EOF'
   LMS_BASE_URL=https://lms.yoursite.org
   BASE_URL=https://learning.yoursite.org
   LOGIN_URL=https://authn.yoursite.org/login
   LOGOUT_URL=https://authn.yoursite.org/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=https://lms.yoursite.org/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Your Open edX Site
   STUDIO_BASE_URL=https://studio.yoursite.org
   EOF

   # Build for production
   NODE_ENV=production npm run build

Serve MFEs with Nginx
---------------------

Configure Nginx to serve the built MFE static files:

.. code-block:: nginx

   server {
       listen 443 ssl http2;
       server_name learning.yoursite.org;

       ssl_certificate /etc/ssl/certs/yoursite.crt;
       ssl_certificate_key /etc/ssl/private/yoursite.key;

       root /opt/frontend-app-learning/dist;
       index index.html;

       location / {
           try_files $uri $uri/ /index.html;
       }

       # Cache static assets
       location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
           expires 1y;
           add_header Cache-Control "public, immutable";
       }
   }

Repeat this configuration for each MFE with appropriate server names and root directories.

Additional Production Considerations
------------------------------------

* Use a CDN to serve MFE static assets globally
* Configure proper cache headers for optimal performance
* Set up proper DNS and SSL certificates for all MFE subdomains
* Use environment-specific configuration files
* Implement automated deployment pipelines for MFE updates
* Monitor MFE performance and error rates
* Consider using a build cache to speed up subsequent builds
* Enable gzip compression for text assets

Common Issues
*************

Port Conflicts
==============

If ports 8000, 8001, or any MFE ports are in use, modify the configuration to use different ports. Update both the server startup commands and the configuration files.

Memory Issues
=============

Ensure sufficient RAM is available. Consider adding swap space if running on limited hardware. MFE builds are particularly memory-intensive.

Migration Failures
==================

If migrations fail:

* Check database connectivity and permissions
* Review migration logs for specific errors
* Ensure all required services are running
* Verify database user has sufficient privileges

Static Asset 404 Errors
========================

Ensure ``collectstatic`` completed successfully and your web server is configured to serve static files from the correct directory.

Service Connection Errors
==========================

Verify all required services (MySQL, MongoDB, Redis, Elasticsearch, Memcached) are running and accessible on the configured hosts and ports.

MFE CORS Errors
===============

If you see CORS errors in the browser console, verify:

* ``CORS_ORIGIN_WHITELIST`` in LMS configuration includes all MFE URLs
* ``CORS_ALLOW_CREDENTIALS`` is set to ``true``
* LMS has been restarted after configuration changes
* Cookie domains are configured correctly

MFE Authentication Issues
=========================

If MFEs cannot authenticate:

* Verify all MFEs have the correct ``LMS_BASE_URL`` in their ``.env`` files
* Check that cookie domains are configured correctly
* Ensure ``ACCESS_TOKEN_COOKIE_NAME`` matches across all MFEs
* Verify ``LOGIN_REDIRECT_WHITELIST`` includes all MFE domains
* Check browser console for specific error messages

MFE Build Failures
==================

If ``npm run build`` fails:

* Ensure you have sufficient memory (Node.js builds can be memory-intensive)
* Check Node.js version compatibility with the MFE
* Clear npm cache: ``npm cache clean --force``
* Delete ``node_modules`` and reinstall: ``rm -rf node_modules && npm clean-install``
* Check for disk space issues

Celery Worker Issues
====================

If Celery workers are not processing tasks:

* Verify Redis is running and accessible
* Check Celery logs for errors
* Ensure the correct broker URL is configured
* Verify worker processes are actually running

Alternative: Using Docker Compose Without Tutor
************************************************

If you want containerization benefits without Tutor's abstractions, you can create a custom Docker Compose setup:

#. Create separate containers for each service
#. Mount edx-platform code as volumes
#. Configure networking between containers
#. Use custom entrypoint scripts for initialization

This approach provides isolation while maintaining direct control over the configuration. Ongoing experiments in adopting this configuration are happening at `Minimal edX Platform <https://github.com/feanil/minimal-edx-platform>`_.

See Also
********

* :ref:`Installing and Starting the Open edX Platform`
* `Open edX Developer Documentation <https://docs.openedx.org/en/latest/developers/>`_
* `edx-platform Repository <https://github.com/openedx/edx-platform>`_
* `Open edX Configuration Repository <https://github.com/openedx/configuration>`_

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
