.. _Run Open edX Without Tutor:

How to Run Open edX (edx-platform) Without Tutor
################################################

.. tags:: site operator, how-to

This guide provides a checklist for running the Open edX platform (edx-platform)
directly on Ubuntu without using Tutor. This approach requires manual setup of
all dependent services and is intended for system administrators who need
fine-grained control over their deployment or development environment.

The focus of this guide is on getting a development environment up and running,
but it touches on some of the key steps involved in setting up a production
environment as well.

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

.. warning::

   **Python Version Requirements by Branch:**

   * **Teak and Ulmo named releases**: Require Python 3.11
   * **Master branch**: Compatible with Python 3.12

   If you need to use Teak or Ulmo, you must install Python 3.11 from the deadsnakes PPA.

   For the latest features, and development use Python 3.12 and the master branches.

   This guide assumes you are using the master branch with Python 3.12.


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
       python3.12 \
       python3.12-dev \
       python3-pip \
       python3-venv \
       pkg-config

**Test this step:**

.. code-block:: bash

   python3.12 --version
   git --version


2. Install and Configure MySQL
==============================

Install MySQL 8.0:

.. code-block:: bash

   sudo apt-get install -y mysql-server mysql-client
   sudo systemctl start mysql
   sudo systemctl enable mysql

.. note::

   **Container environments:** If running in a Docker container without systemd, use
   ``sudo service mysql start`` instead of systemctl commands.

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

   wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | \
       gpg --dearmor | sudo tee /usr/share/keyrings/mongodb-server-7.0.gpg > /dev/null
   echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | \
       sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
   sudo apt-get update
   sudo apt-get install -y mongodb-org
   sudo systemctl start mongod
   sudo systemctl enable mongod

.. note::

   **Container environments:** If systemctl is not available, start MongoDB manually:
   ``sudo mkdir -p /var/lib/mongodb /var/log/mongodb && sudo chown -R mongodb:mongodb /var/lib/mongodb /var/log/mongodb && sudo mongod --fork --logpath /var/log/mongodb/mongod.log --dbpath /var/lib/mongodb``

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

.. note::

   **Container environments:** Use ``sudo service redis-server start`` if systemctl is unavailable.

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

.. note::

   **Container environments:** Use ``memcached -d -u root`` to start in daemon mode if systemctl is unavailable.

**Test this step:**

.. code-block:: bash

   sudo systemctl status memcached
   # Install netcat if not present
   sudo apt-get install -y netcat-openbsd
   echo "stats" | nc localhost 11211
   # Should return memcached statistics

6. Install and Configure Elasticsearch
======================================

Install Elasticsearch 7.x:

.. code-block:: bash

   wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | \
       gpg --dearmor | sudo tee /usr/share/keyrings/elasticsearch-keyring.gpg > /dev/null
   echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | \
       sudo tee /etc/apt/sources.list.d/elastic-7.x.list
   sudo apt-get update
   sudo apt-get install -y elasticsearch
   sudo systemctl start elasticsearch
   sudo systemctl enable elasticsearch

.. note::

   **Container environments:** Use ``sudo /etc/init.d/elasticsearch start`` if systemctl is unavailable.

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
   # Use shallow clone to save time and disk space
   # Clone master branch (compatible with Python 3.12)
   sudo git clone --depth 1 --branch master https://github.com/openedx/edx-platform.git
   cd edx-platform

.. note::

   **Branch Selection:**

   * **master branch** (recommended): Latest development version, Python 3.12 compatible
   * **release/ulmo.1**: Named release, requires Python 3.11
   * **release/teak.1**: Named release, requires Python 3.11

   For named releases with Python 3.11, use:
   ``sudo git clone --depth 1 --branch release/ulmo.1 https://github.com/openedx/edx-platform.git``


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
   sudo python3.12 -m venv venv
   sudo chown -R $USER:$USER venv
   source venv/bin/activate

**Test this step:**

.. code-block:: bash

   which python
   # Should return: /opt/edx-platform/venv/bin/python
   python --version
   # Should return: Python 3.12.x

10. Install Python Requirements
===============================

Install edx-platform Python dependencies:

.. code-block:: bash

   pip install --upgrade pip setuptools wheel
   pip install -r requirements/edx/base.txt
   pip install -r requirements/edx/assets.txt

.. note::

   This step may take 15-30 minutes depending on your system. If you encounter
   errors, you may need to install additional system libraries. The assets.txt
   file includes libsass which is required for SASS compilation in the next step.

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
   npm run webpack

   # SASS compilation must run with virtual environment activated
   source venv/bin/activate
   PATH="$PATH:/opt/edx-platform/node_modules/.bin" python scripts/compile_sass.py --env=production

.. note::

   This step may take 10-20 minutes and requires significant memory. The webpack
   build and SASS compilation are separate steps because the SASS compilation
   script requires access to Python packages in the virtual environment. Running
   ``npm run build`` directly will fail because it doesn't activate the venv before
   running the SASS compilation script.

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

.. note::

   Before running migrations on the **master branch**, you must add required apps to INSTALLED_APPS.
   See the "Master Branch Testing: February 2026" section for the complete list of apps to add.

Apply Django migrations:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate

   # Set environment variables
   export LMS_CFG=/edx/etc/lms.yml
   export CMS_CFG=/edx/etc/cms.yml

   # Run migrations for LMS
   ./manage.py lms migrate --settings=production

   # Run migrations for CMS
   ./manage.py cms migrate --settings=production

**Test this step:**

.. code-block:: bash

   mysql -u edxapp -p -e "USE edxapp; SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'edxapp';"
   # Should show 567 tables (master branch, February 2026)

14. Create Django Superuser
===========================

Create an administrative user:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate
   export LMS_CFG=/edx/etc/lms.yml

   # Create superuser with --noinput (non-interactive)
   ./manage.py lms createsuperuser --username admin --email admin@example.com --noinput --settings=production

   # Set the password using Python
   python -c "
   import os
   import django
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.envs.production')
   django.setup()
   from django.contrib.auth import get_user_model
   User = get_user_model()
   user = User.objects.get(username='admin')
   user.set_password('your-secure-password')
   user.save()
   print('Password set successfully')
   "

.. warning::

   Replace ``your-secure-password`` with a strong password of your choice.

**Test this step:**

.. code-block:: bash

   mysql -u edxapp -p -e "USE edxapp; SELECT username, email, is_superuser, is_staff FROM auth_user WHERE is_superuser=1;"
   # Should show your superuser with is_superuser=1 and is_staff=1

15. Collect Static Assets
=========================

Collect Django static files:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate
   export LMS_CFG=/edx/etc/lms.yml
   export CMS_CFG=/edx/etc/cms.yml

   # Collect LMS static files
   ./manage.py lms collectstatic --noinput --settings=production

   # Collect CMS static files
   ./manage.py cms collectstatic --noinput --settings=production

**Test this step:**

.. code-block:: bash

   ls -la /opt/staticfiles/
   # Should show LMS static files (6,600+ files)

   ls -la /opt/staticfiles/studio/
   # Should show CMS/Studio static files (3,000+ files)

16. Clone and Set Up MFEs
=========================

Open edX uses React-based Micro-Frontends (MFEs) for key user-facing features.
Set these up before starting the servers.

.. important::

   **MFE Branch Selection:**

   MFE branches should match your edx-platform branch:

   * If using **edx-platform master branch**: Use MFE **master** or **main** branches
   * If using **edx-platform named releases** (e.g., release/ulmo.1): Use corresponding MFE release branches (e.g., open-release/sumac.master)

   This guide uses the **master branch** for both edx-platform and MFEs.

Essential MFEs
--------------

.. note::

   **npm install vs npm clean-install:**

   Use ``npm install`` rather than ``npm clean-install`` for MFE setup. The clean-install command
   requires package-lock.json to be perfectly synchronized and may fail with "Missing from lock file"
   errors. Regular ``npm install`` is more forgiving and will work even if the lock file is slightly
   out of sync with package.json.

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
   # Uses default branch (master/main) - matches edx-platform master
   sudo chown -R $USER:$USER /opt/frontend-app-authn
   npm install

Create ``.env.development`` file:

.. code-block:: bash

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:1999
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Test Open edX Site
   LOGO_URL=http://localhost:8000/static/images/logo.png
   FAVICON_URL=http://localhost:8000/static/images/favicon.ico
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   PORT=1999
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
   # Uses default branch (master/main) - matches edx-platform master
   sudo chown -R $USER:$USER /opt/frontend-app-learning
   npm install

Create ``.env.development`` file:

.. code-block:: bash

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:2000
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Test Open edX Site
   LOGO_URL=http://localhost:8000/static/images/logo.png
   FAVICON_URL=http://localhost:8000/static/images/favicon.ico
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   PORT=2000
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
   # Uses default branch (master/main) - matches edx-platform master
   sudo chown -R $USER:$USER /opt/frontend-app-account
   npm install

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:1997
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Test Open edX Site
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   PORT=1997
   EOF

**Test:** ``npm run build && ls dist/``

Clone and Configure frontend-app-profile
----------------------------------------

.. code-block:: bash

   cd /opt
   sudo git clone https://github.com/openedx/frontend-app-profile.git
   cd frontend-app-profile
   # Uses default branch (master/main) - matches edx-platform master
   sudo chown -R $USER:$USER /opt/frontend-app-profile
   npm install

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:1995
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Test Open edX Site
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   PORT=1995
   EOF

**Test:** ``npm run build && ls dist/``

Clone and Configure frontend-app-discussions
--------------------------------------------

.. code-block:: bash

   cd /opt
   sudo git clone https://github.com/openedx/frontend-app-discussions.git
   cd frontend-app-discussions
   # Uses default branch (master/main) - matches edx-platform master
   sudo chown -R $USER:$USER /opt/frontend-app-discussions
   npm install

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:2002
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Test Open edX Site
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   PORT=2002
   EOF

**Test:** ``npm run build && ls dist/``

Clone and Configure frontend-app-gradebook
------------------------------------------

.. code-block:: bash

   cd /opt
   sudo git clone https://github.com/openedx/frontend-app-gradebook.git
   cd frontend-app-gradebook
   # Uses default branch (master/main) - matches edx-platform master
   sudo chown -R $USER:$USER /opt/frontend-app-gradebook
   npm install

   cat > .env.development << 'EOF'
   LMS_BASE_URL=http://localhost:8000
   BASE_URL=http://localhost:1994
   LOGIN_URL=http://localhost:1999/login
   LOGOUT_URL=http://localhost:1999/logout
   REFRESH_ACCESS_TOKEN_ENDPOINT=http://localhost:8000/login_refresh
   ACCESS_TOKEN_COOKIE_NAME=edx-jwt-cookie-header-payload
   SITE_NAME=Test Open edX Site
   STUDIO_BASE_URL=http://localhost:8001
   LANGUAGE_PREFERENCE_COOKIE_NAME=openedx-language-preference
   USER_INFO_COOKIE_NAME=edx-user-info
   CSRF_TOKEN_API_PATH=/csrf/api/v1/token
   PORT=1994
   EOF

**Test:** ``npm run build && ls dist/``

.. note::

   **Shared Components**: MFEs use shared header and footer components (``frontend-component-header`` and ``frontend-component-footer``). These are automatically installed as npm dependencies and do not need separate setup.

17. Start LMS and CMS Servers
=============================

Before starting the servers, build the frontend webpack assets.

Build Webpack Assets
--------------------

.. code-block:: bash

   cd /opt/edx-platform
   npm run build

This will compile webpack bundles and SASS files. The build generates ``webpack-stats.json`` files that need to be copied to the production staticfiles directory:

.. code-block:: bash

   # Copy webpack stats files to production location
   cp /opt/edx-platform/test_root/staticfiles/webpack-stats.json /opt/staticfiles/
   cp /opt/edx-platform/test_root/staticfiles/studio/webpack-stats.json /opt/staticfiles/studio/

Start Development Servers
--------------------------

Open separate terminal windows for each service. In each terminal, activate the virtual environment first:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate

Terminal 1 - Start LMS:

.. code-block:: bash

   export LMS_CFG=/edx/etc/lms.yml
   ./manage.py lms runserver 0.0.0.0:8000 --settings=production

.. note::

   The manage.py script automatically prepends ``lms.envs.`` to the settings module, so use ``--settings=production`` not ``--settings=lms.envs.production``.

Terminal 2 - Start CMS:

.. code-block:: bash

   export CMS_CFG=/edx/etc/cms.yml
   ./manage.py cms runserver 0.0.0.0:8001 --settings=production

**Test this step:**

.. code-block:: bash

   # In a new terminal
   curl -I http://localhost:8000
   # Should return HTTP 200 OK

   curl -I http://localhost:8001
   # Should return HTTP 302 Found

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

Open edX uses Celery for asynchronous task processing.

Configure Celery Broker Settings
---------------------------------

The production settings construct the broker URL from component settings. Ensure these are in your configuration files (``/edx/etc/lms.yml`` and ``/edx/etc/cms.yml``):

.. code-block:: yaml

   CELERY_BROKER_TRANSPORT: redis
   CELERY_BROKER_HOSTNAME: localhost:6379
   CELERY_BROKER_VHOST: 0
   CELERY_BROKER_USER: ''
   CELERY_BROKER_PASSWORD: ''

Start Celery Workers
--------------------

Open separate terminal windows for each worker:

Terminal 3 - LMS Celery worker:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate
   export LMS_CFG=/edx/etc/lms.yml
   export DJANGO_SETTINGS_MODULE=lms.envs.production
   celery -A lms.celery worker --loglevel=info

Terminal 4 - CMS Celery worker:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate
   export CMS_CFG=/edx/etc/cms.yml
   export DJANGO_SETTINGS_MODULE=cms.envs.production
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
   export LMS_CFG=/edx/etc/lms.yml
   ./manage.py lms runserver 0.0.0.0:8000 --settings=production

   # Window 1: CMS (Ctrl-b c)
   cd /opt/edx-platform && source venv/bin/activate
   export CMS_CFG=/edx/etc/cms.yml
   ./manage.py cms runserver 0.0.0.0:8001 --settings=production

   # Window 2: LMS Celery worker
   cd /opt/edx-platform && source venv/bin/activate
   export LMS_CFG=/edx/etc/lms.yml
   export DJANGO_SETTINGS_MODULE=lms.envs.production
   celery -A lms.celery worker --loglevel=info

   # Window 3: CMS Celery worker
   cd /opt/edx-platform && source venv/bin/activate
   export CMS_CFG=/edx/etc/cms.yml
   export DJANGO_SETTINGS_MODULE=cms.envs.production
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
   command=/opt/edx-platform/venv/bin/python /opt/edx-platform/manage.py lms runserver 0.0.0.0:8000 --settings=production
   directory=/opt/edx-platform
   environment=LMS_CFG="/edx/etc/lms.yml"
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

* Install and configure Nginx or Caddy as a reverse proxy
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

* Configure appropriate worker counts for Gunicorn - note that multiple threads per process is known to have issues at the time of writing
* Tune MySQL, MongoDB, and Elasticsearch for your workload
* Set up CDN for static assets
* Configure Redis persistence appropriately
* Enable Django caching layers

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

* Make sure that all required apps are added to the ``INSTALLED_APPS`` setting in Django settings
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

If Celery workers fail with "No such transport: ''" error:

This indicates the BROKER_URL is not being constructed properly. The production.py settings build
BROKER_URL from component settings, not from CELERY_BROKER_URL directly.

**Solution:** Ensure your configuration files (lms.yml, cms.yml) include these component settings:

.. code-block:: yaml

   CELERY_BROKER_TRANSPORT: redis
   CELERY_BROKER_HOSTNAME: localhost:6379
   CELERY_BROKER_VHOST: 0
   CELERY_BROKER_USER: ''
   CELERY_BROKER_PASSWORD: ''

Other Celery troubleshooting steps:

* Verify Redis is running and accessible
* Check Celery logs for errors
* Ensure DJANGO_SETTINGS_MODULE and LMS_CFG/CMS_CFG environment variables are set
* Verify worker processes are actually running: ``ps aux | grep celery``

LMS/CMS Server Startup Issues
==============================

**Error: "Cannot resolve bundle commons" or webpack-stats.json errors:**

The production settings require webpack assets to be built before starting servers.

**Solution:**

1. Build webpack assets: ``cd /opt/edx-platform && npm run build``
2. Copy webpack-stats.json files to production location:

   .. code-block:: bash

      cp /opt/edx-platform/test_root/staticfiles/webpack-stats.json /opt/staticfiles/
      cp /opt/edx-platform/test_root/staticfiles/studio/webpack-stats.json /opt/staticfiles/studio/

**Error: "No module named 'lms.envs.lms'" when using --settings:**

The manage.py script automatically prepends the environment prefix to the settings argument.

**Solution:** Use ``--settings=production`` not ``--settings=lms.envs.production``

.. code-block:: bash

   # Correct:
   ./manage.py lms runserver --settings=production

   # Incorrect:
   ./manage.py lms runserver --settings=lms.envs.production

Alternative: Using Docker Compose Without Tutor
************************************************

If you want containerization benefits without Tutor's abstractions, you can create a custom Docker Compose setup:

#. Create separate containers for each service
#. Mount edx-platform code as volumes
#. Configure networking between containers
#. Use custom entrypoint scripts for initialization

This approach provides isolation while maintaining direct control over the configuration. Ongoing experiments in adopting this configuration are happening at `Minimal edX Platform <https://github.com/feanil/minimal-edx-platform>`_.

Testing Results and Validation
*******************************

Latest Testing: February 2026
==============================

**Environment:**
- Ubuntu 24.04.3 LTS (Docker container)
- edx-platform branch: release/ulmo.1 (commit ea91c4c)
- Python 3.12.3
- Node.js 18.20.8
- MySQL 8.0.45, MongoDB 7.0.29, Redis 7.0.15, Elasticsearch 7.17.29, Memcached 1.6.24

**Results:** Steps 1-12 completed successfully with all corrections applied to the main installation
instructions. All services started correctly, Python packages installed (600+ packages), Node.js
dependencies installed (1019 packages), webpack build completed, and SASS compilation succeeded.

**Key Corrections Made:**
- Updated to Python 3.12 (Ubuntu 24.04 default)
- Added pkg-config to system dependencies
- Updated MongoDB and Elasticsearch to use modern GPG key method (not apt-key)
- Added netcat-openbsd for Memcached testing
- Changed to shallow git clone with --depth 1
- Fixed npm build process to run SASS compilation with venv activated
- Added container environment notes for service management

**Additional Findings:**

1. **Installation Time:** Steps 1-12 took approximately 45-60 minutes total:

   - Python packages (Step 10): ~15 minutes
   - Node packages (Step 11): ~5 minutes
   - Webpack build: ~1 minute
   - SASS compilation: ~30 seconds

2. **Disk Space:** After completing Step 12:

   - edx-platform directory (shallow clone): ~2.5 GB
   - Virtual environment with packages: ~3 GB
   - node_modules: ~1 GB
   - Total: ~6.5 GB (vs ~10+ GB for full clone)

3. **Memory Usage:** Peak memory during npm build was ~4 GB. Minimum 8 GB RAM recommended.

4. **Node.js Deprecation:** Node.js 18.x shows deprecation warning. Future testing should
   evaluate Node.js 20.x compatibility.

5. **Service Versions:** All services installed correctly with latest stable versions from
   repositories. Version drift from guide specifications is normal and expected.

Master Branch Testing: February 2026
=====================================

**Environment:**
- Ubuntu 24.04.3 LTS (Docker container)
- edx-platform branch: master (February 2026)
- Python 3.12.3
- Node.js 18.20.8
- MySQL 8.0.45, MongoDB 7.0.29, Redis 7.0.15, Elasticsearch 7.17.29, Memcached 1.6.24

**Results:** Steps 1-19 completed successfully with all services operational. All migrations ran without Python 3.11 compatibility issues.

**Why Master Branch:**

The release/ulmo.1 branch has a dependency on boto 2.49.0 which is incompatible with Python 3.12. There are likely other compatibility issues with Python 3.12. The master branch uses only boto3, making it compatible with Python 3.12 on Ubuntu 24.04.

**Required INSTALLED_APPS Changes:**

The master branch requires the following apps to be added to INSTALLED_APPS:

**For LMS** (``lms/envs/common.py``):

Add these apps near the end of the INSTALLED_APPS list (around line 2025, before the closing bracket):

.. code-block:: python

   # Learning Core Apps, used by v2 content libraries (content_libraries app)
   'openedx.core.djangoapps.content_libraries',
   "openedx_learning.apps.authoring.collections",
   "openedx_learning.apps.authoring.components",
   "openedx_learning.apps.authoring.contents",
   "openedx_learning.apps.authoring.publishing",
   "openedx_learning.apps.authoring.units",
   "openedx_learning.apps.authoring.subsections",
   "openedx_learning.apps.authoring.sections",

   # Additional required apps
   "openedx.core.djangoapps.bookmarks",
   "openedx.core.djangoapps.discussions",
   "openedx.core.djangoapps.theming",

Also add ``lms.djangoapps.program_enrollments`` after programs config (around line 1895):

.. code-block:: python

   # programs support
   'openedx.core.djangoapps.programs.apps.ProgramsConfig',
   'lms.djangoapps.program_enrollments',

**For CMS** (``cms/envs/common.py``):

Add these apps near the end of the INSTALLED_APPS list (around line 900, before the closing bracket):

.. code-block:: python

   # Learning Core Apps, used by v2 content libraries (content_libraries app)
   'openedx.core.djangoapps.content_libraries',
   "openedx_learning.apps.authoring.collections",
   "openedx_learning.apps.authoring.components",
   "openedx_learning.apps.authoring.contents",
   "openedx_learning.apps.authoring.publishing",
   "openedx_learning.apps.authoring.units",
   "openedx_learning.apps.authoring.subsections",
   "openedx_learning.apps.authoring.sections",

   # Additional required apps
   "openedx.core.djangoapps.bookmarks",
   "openedx.core.djangoapps.discussions",
   "openedx.core.djangoapps.theming",
   "openedx.core.djangoapps.content_staging",

**Note:** ``lms.djangoapps.bulk_email`` is already uncommented in the master branch.

**Migration Results:**

- LMS migrations: 567 tables created successfully
- CMS migrations: Completed successfully
- No boto2-related errors
- All apps initialized properly

**Static Assets:**

- LMS: 6,604 files copied, 6,686 post-processed
- CMS: 3,087 files copied, 3,115 post-processed

**Webpack Assets (Step 17):**

The production settings require webpack bundles to be built before starting servers:

1. Run ``npm run build`` in the edx-platform directory to compile webpack bundles and SASS files
2. Copy webpack-stats.json files from build output to production location:

   .. code-block:: bash

      cp /opt/edx-platform/test_root/staticfiles/webpack-stats.json /opt/staticfiles/
      cp /opt/edx-platform/test_root/staticfiles/studio/webpack-stats.json /opt/staticfiles/studio/

3. Important: The manage.py script automatically prepends ``lms.envs.`` or ``cms.envs.`` to settings arguments,
   so use ``--settings=production`` not ``--settings=lms.envs.production``

**Celery Configuration (Step 18):**

The production.py settings construct BROKER_URL from component settings rather than using CELERY_BROKER_URL directly.
Required settings in both lms.yml and cms.yml:

.. code-block:: yaml

   CELERY_BROKER_TRANSPORT: redis
   CELERY_BROKER_HOSTNAME: localhost:6379
   CELERY_BROKER_VHOST: 0
   CELERY_BROKER_USER: ''
   CELERY_BROKER_PASSWORD: ''

Both Celery workers started successfully and connected to Redis.

**MFE Setup (Step 19):**

All 6 essential MFEs were set up using their master/main branches (not release branches) to match edx-platform master:

- frontend-app-authn (port 1999): Started successfully
- frontend-app-learning (port 2000): Started successfully
- frontend-app-account (port 1997): Started successfully
- frontend-app-profile (port 1995): Started successfully
- frontend-app-discussions (port 2002): Started successfully
- frontend-app-gradebook (port 1994): Started successfully

All MFE development servers responded with HTTP 200.

**Complete System Status:**

All services operational and tested:
- ✓ MySQL, MongoDB, Redis, Memcached, Elasticsearch
- ✓ LMS server (HTTP 200 on port 8000)
- ✓ CMS server (HTTP 302 on port 8001)
- ✓ LMS and CMS Celery workers connected to Redis
- ✓ All 6 MFE development servers responding

Known Issues and Corrections (Historical - January 2026)
*********************************************************

The following issues were discovered during initial testing. Most have been corrected in the
main installation steps above:

System Dependencies (Step 1)
=============================

**Issue 1: Python Version** ✅ FIXED IN MAIN STEPS

The document originally specified Python 3.11, but Ubuntu 24.04 ships with Python 3.12 by default.

**Resolution:** Main installation steps now use Python 3.12. If you specifically need Python 3.11,
add the deadsnakes PPA as shown below, but Python 3.12 works correctly with release/ulmo.1.

.. code-block:: bash

   sudo apt-get install -y software-properties-common
   sudo add-apt-repository -y ppa:deadsnakes/ppa
   sudo apt-get update
   sudo apt-get install -y python3.11 python3.11-dev python3.11-venv

**Issue 2: Missing pkg-config** ✅ FIXED IN MAIN STEPS

The ``pkg-config`` package is required for building Python packages (especially mysqlclient).

**Resolution:** Added to Step 1 system dependencies list.

**Issue 3: Python symlink** ⚠️ OPTIONAL

Some build scripts expect ``/usr/bin/python`` to exist but it doesn't by default in Ubuntu 24.04.

**Resolution:** Not required for the installation process. If needed for other tools:

.. code-block:: bash

   sudo ln -s /usr/bin/python3.12 /usr/bin/python

MongoDB and Elasticsearch Setup (Steps 3 & 6)
==============================================

**Issue 4: Deprecated apt-key** ✅ FIXED IN MAIN STEPS

The instructions originally used ``apt-key add -`` which is deprecated in Ubuntu 24.04.

**Resolution:** Steps 3 and 6 now use the modern GPG keyring method with ``signed-by``.

Repository Checkout (Step 8)
=============================

**Issue 5: Branch naming convention** ✅ FIXED IN MAIN STEPS

Newer releases use ``release/<name>.<number>`` format instead of ``open-release/<name>.master``.

**Resolution:** Step 8 now uses the correct branch format and includes shallow clone
with ``--depth 1`` to save time and disk space.

Python Requirements (Step 10)
==============================

**Issue 6: Missing assets requirements** ✅ FIXED IN MAIN STEPS

The ``requirements/edx/assets.txt`` file (which includes libsass for SASS compilation) was not
originally included in the installation steps.

**Resolution:** Step 10 now includes installing ``requirements/edx/assets.txt`` after base.txt.

Node.js Assets (Step 11)
=========================

**Issue 7: npm run build fails** ✅ FIXED IN MAIN STEPS

Running ``npm run build`` fails because the SASS compilation script (a Python script) is executed
outside the virtual environment, causing ``ModuleNotFoundError: No module named 'click'``.

**Resolution:** Step 11 now separates the build into two parts:

1. Run ``npm run webpack`` (does not need venv)
2. Run SASS compilation with venv activated: ``source venv/bin/activate && PATH="$PATH:/opt/edx-platform/node_modules/.bin" python scripts/compile_sass.py --env=production``

The PATH addition ensures ``rtlcss`` from node_modules/.bin is available for RTL CSS generation.

Database Migrations (Step 13)
==============================

**Issue 8: Settings syntax and environment variables** ✅ TESTED AND FIXED

The correct settings flag format is ``--settings=production``, not ``--settings=lms.envs.production``,
and the ``LMS_CFG`` environment variable must be set to point to the configuration file.

**Issue 9: Missing apps in INSTALLED_APPS (release/ulmo.1)** ✅ TESTED AND FIXED

The release/ulmo.1 branch is missing several apps from INSTALLED_APPS in ``lms/envs/common.py``,
which causes KeyError exceptions during migrations.

**Required fixes for lms/envs/common.py:**

1. Uncomment bulk_email app (around line 2130):

.. code-block:: python

   'lms.djangoapps.certificates.apps.CertificatesConfig',
   'lms.djangoapps.instructor_task',
   'openedx.core.djangoapps.course_groups',
   'lms.djangoapps.bulk_email',  # Uncomment this line
   'lms.djangoapps.branding',

2. Add program_enrollments app after programs config (around line 2253):

.. code-block:: python

   # programs support
   'openedx.core.djangoapps.programs.apps.ProgramsConfig',
   'lms.djangoapps.program_enrollments',  # Add this line

3. Add missing openedx.core.djangoapps apps (locations vary, add where appropriate):

.. code-block:: python

   'openedx.core.djangoapps.bookmarks',
   'openedx.core.djangoapps.content_libraries',
   'openedx.core.djangoapps.discussions',
   'openedx.core.djangoapps.theming',

**Issue 10: MODULESTORE configuration incomplete** ✅ TESTED AND FIXED

The minimal MODULESTORE configuration in ``/edx/etc/lms.yml`` causes ``TypeError: MongoModuleStore.__init__()
missing 2 required positional arguments: 'fs_root' and 'render_template'``.

**Resolution:** The MODULESTORE must use MixedModuleStore with complete configuration. Replace the minimal
MODULESTORE section in ``/edx/etc/lms.yml`` with:

.. code-block:: yaml

   DOC_STORE_CONFIG:
     db: edxapp
     host: localhost
     port: 27017
     user: edxapp
     password: your_mongodb_password
     collection: modulestore
     ssl: false
     socketTimeoutMS: 6000
     connectTimeoutMS: 2000
     auth_source: null
     read_preference: SECONDARY_PREFERRED

   CONTENTSTORE:
     ENGINE: xmodule.contentstore.mongo.MongoContentStore
     DOC_STORE_CONFIG:
       db: edxapp
       host: localhost
       port: 27017
       user: edxapp
       password: your_mongodb_password
       ssl: false
       auth_source: null
     OPTIONS:
       db: edxapp
       host: localhost
       port: 27017
       user: edxapp
       password: your_mongodb_password
       ssl: false
       auth_source: null

   MODULESTORE:
     default:
       ENGINE: xmodule.modulestore.mixed.MixedModuleStore
       OPTIONS:
         mappings: {}
         stores:
           - NAME: split
             ENGINE: xmodule.modulestore.split_mongo.split_draft.DraftVersioningModuleStore
             DOC_STORE_CONFIG:
               db: edxapp
               host: localhost
               port: 27017
               user: edxapp
               password: your_mongodb_password
               collection: modulestore
               ssl: false
               socketTimeoutMS: 6000
               connectTimeoutMS: 2000
               auth_source: null
               read_preference: SECONDARY_PREFERRED
             OPTIONS:
               default_class: xmodule.hidden_block.HiddenBlock
               fs_root: /edx/var/edxapp/data
               render_template: common.djangoapps.edxmako.shortcuts.render_to_string
           - NAME: draft
             ENGINE: xmodule.modulestore.mongo.DraftMongoModuleStore
             DOC_STORE_CONFIG:
               db: edxapp
               host: localhost
               port: 27017
               user: edxapp
               password: your_mongodb_password
               collection: modulestore
               ssl: false
               socketTimeoutMS: 6000
               connectTimeoutMS: 2000
               auth_source: null
               read_preference: SECONDARY_PREFERRED
             OPTIONS:
               default_class: xmodule.hidden_block.HiddenBlock
               fs_root: /edx/var/edxapp/data
               render_template: common.djangoapps.edxmako.shortcuts.render_to_string

   DATA_DIR: /edx/var/edxapp/data

Create the required data directory:

.. code-block:: bash

   sudo mkdir -p /edx/var/edxapp/data

**Final working approach (tested February 2026):**

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate
   export LMS_CFG=/edx/etc/lms.yml
   ./manage.py lms migrate --settings=production

**Test result:**

.. code-block:: bash

   mysql -u edxapp -p -e "USE edxapp; SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'edxapp';"
   # Should show 566 tables (February 2026 test result)

**Status:** Migrations complete successfully with all fixes applied. The issues were not circular imports
as initially suspected, but rather missing app registrations and incomplete MODULESTORE configuration.

Environment Notes
=================

**Issue 11: Container/non-systemd environments** ✅ FIXED IN MAIN STEPS

Container environments without systemd require different service management commands.

**Resolution:** Notes have been added throughout Steps 2-6 explaining how to start services
in container environments using ``service`` commands or direct daemon invocation.

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
