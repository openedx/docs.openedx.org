.. _Run Open edX Without Tutor:

How to Run Open edX (edx-platform) Without Tutor
#################################################

.. tags:: site operator, how-to

This guide provides a checklist for running the Open edX platform (edx-platform)
directly on Ubuntu without using Tutor. This approach requires manual setup of all
dependent services and is intended for system administrators who need fine-grained
control over their deployment or development environment.

.. warning::

   Running Open edX without Tutor is significantly more complex than using the
   officially supported Tutor installation method. This approach requires extensive
   system administration knowledge and is not recommended for production deployments
   unless you have experience running complicated infrastructure.


Prerequisites
*************

* Ubuntu 24.04 LTS
* Root or sudo access
* Minimum 8GB RAM (16GB+ recommended for production)
* Basic familiarity with Django applications
* Understanding of service management (systemd)

Required Services Overview
***************************

TODO: Do we actually need Memcached or Elasticsearch?

The Open edX platform requires the following services to be running:

* **MySQL 8.0** - Primary relational database
* **MongoDB 7.0** - Document storage for modulestore (course content)
* **Redis 7.x** - Caching and Celery broker
* **Memcached** - Application caching layer
* **Elasticsearch 7.x** - Course search functionality

Installation Steps
******************

1. Install System Dependencies
===============================

Install required packages:

TODO: Figure out exactly which of these we actually need for this install

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

       -- Things Tutor installs for minimal
       build-essential \
       curl \
       git \
       language-pack-en \

       -- Things Tutor installs python
       libssl-dev \
       zlib1g-dev \
       libbz2-dev \
       libreadline-dev \
       libsqlite3-dev \
       wget \
       curl \
       llvm \
       libncurses5-dev \
       libncursesw5-dev \
       xz-utils \
       tk-dev \
       libffi-dev \
       liblzma-dev \
       python3-openssl \
       git \

       -- Things Tutor installs for the virtualenv
       software-properties-common \
       libmysqlclient-dev \
       libxmlsec1-dev \
       libgeos-dev \
       # Install xmlsec dependencies
       libxml2-dev \
       libxmlsec1-openssl \

       -- Things Tutor installs for "production"
       gettext \
       gfortran \
       graphviz \
       graphviz-dev \
       libffi-dev \
       libfreetype6-dev \
       libgeos-dev \
       libjpeg8-dev \
       liblapack-dev \
       libmysqlclient-dev \
       libpng-dev \
       libsqlite3-dev \
       libxmlsec1-dev \
       lynx \
       mysql-client \
       ntp \
       pkg-config \
       rdfind \

       -- Things Tutor installs for development
       vim \
       iputils-ping \
       dnsutils \
       telnet \



2. Install and Configure MySQL
===============================

Install MySQL 8.0:

.. code-block:: bash

   sudo apt-get install -y mysql-server mysql-client
   sudo systemctl start mysql
   sudo systemctl enable mysql

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

3. Install and Configure MongoDB
=================================

Install MongoDB 7.0:

.. code-block:: bash

   wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | sudo apt-key add -
   echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | \
       sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
   sudo apt-get update
   sudo apt-get install -y mongodb-org
   sudo systemctl start mongod
   sudo systemctl enable mongod

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

.. note::

    Replace ``your_mongodb_password`` with a strong password. Store it securely for use in Django settings.

4. Install and Configure Redis
===============================

Install Redis:

.. code-block:: bash

   sudo apt-get install -y redis-server
   sudo systemctl start redis-server
   sudo systemctl enable redis-server

Verify Redis is running:

.. code-block:: bash

   redis-cli ping
   # Should return: PONG

5. Install and Configure Memcached
===================================

Install Memcached:

.. code-block:: bash

   sudo apt-get install -y memcached
   sudo systemctl start memcached
   sudo systemctl enable memcached

6. Install and Configure Elasticsearch
=======================================

Install Elasticsearch 7.x:

.. code-block:: bash

   wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
   echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | \
       sudo tee /etc/apt/sources.list.d/elastic-7.x.list
   sudo apt-get update
   sudo apt-get install -y elasticsearch
   sudo systemctl start elasticsearch
   sudo systemctl enable elasticsearch

Wait for Elasticsearch to start and verify:

.. code-block:: bash

   curl -X GET "localhost:9200/"

7. Install Node.js and Build Tools
===================================

Install Node.js 18.x:

.. code-block:: bash

   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs

8. Clone edx-platform Repository
=================================

Choose your Open edX release:

Releases are tagged with the release name and a version such as ``ulmo.1``. The most
current information on recent releases can be found at :ref:`Named Release Branches and Tags`.

In the code block below, replace {your-chosen-release}.{most-recent-release-version}
below with the most recent version tag for your chosen release.

Choose your installation directory and clone the repository:

.. code-block:: bash

   cd /opt
   git clone https://github.com/openedx/edx-platform.git
   cd edx-platform

   # Checkout a specific release (recommended for stability)
   git checkout release/{your-chosen-release}.{most-recent-release-version}
   # OR stay on master for latest development code
   # sudo git checkout master

9. Create Python Virtual Environment
=====================================

Create and activate a virtual environment:

.. code-block:: bash

   cd /opt/edx-platform
   python3.11 -m venv venv
   source venv/bin/activate

10. Install Python Requirements
================================

Install edx-platform Python dependencies:

.. code-block:: bash

   # Get the expected versions of pip etc.
   pip install -r requirements/pip-tools.txt

   # Uses the version of pip installed above to further install our
   # Python dependencies
   pip install -r requirements/edx/base.txt

.. note::

   This step may take 15-30 minutes depending on your system. If you encounter errors, you may need to install additional system libraries.

11. Install Node.js Dependencies
=================================

TODO: Is this right, can it even work without everything being configured? Should it go after collectstatic?

Install JavaScript dependencies and build static assets:

.. code-block:: bash

   npm clean-install
   npm run build

.. note::

    This step may take 15-30 minutes depending on your system.


12. Create Configuration Files
===============================

Create the configuration directory:

.. code-block:: bash

   sudo mkdir -p /edx/etc
   sudo chown $USER:$USER /edx/etc

TODO: Redis isn't configured as a cache here, and I doubt this is all of the necessary config

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

Create CMS (Studio) configuration file at ``/edx/etc/cms.yml`` with similar content, adjusting URLs as needed.

Create authentication file at ``/edx/etc/lms.auth.json``:

TODO: Is this really all that's needed here?

.. code-block:: json

   {
     "SECRET_KEY": "your-secret-key-change-this",
     "MYSQL_PASSWORD": "your_password",
     "MONGO_PASSWORD": "your_mongodb_password"
   }

Create ``/edx/etc/cms.auth.json`` with the same structure.

.. warning::

   Generate a strong SECRET_KEY using: ``python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"``

13. Run Database Migrations
============================

Apply Django migrations:

.. code-block:: bash

   cd /opt/edx-platform
   source venv/bin/activate

   # Run migrations for LMS
   ./manage.py lms migrate --settings=lms.envs.production

   # Run migrations for CMS
   ./manage.py cms migrate --settings=cms.envs.production

14. Create Django Superuser
============================

Create an administrative user:

.. code-block:: bash

   ./manage.py lms createsuperuser --settings=lms.envs.production

15. Collect Static Assets
==========================

Collect Django static files:

.. code-block:: bash

   ./manage.py lms collectstatic --noinput --settings=lms.envs.production
   ./manage.py cms collectstatic --noinput --settings=cms.envs.production

16. Start Celery Workers
=========================

Open edX uses Celery for asynchronous task processing. Start workers in separate terminal sessions or as systemd services:

.. code-block:: bash

   # LMS Celery worker
   celery -A lms.celery worker --loglevel=info

   # CMS Celery worker
   celery -A cms.celery worker --loglevel=info

17. Start the LMS and CMS Servers
==================================

In development, you can use Django's runserver:

.. code-block:: bash

   # Start LMS (in one terminal)
   ./manage.py lms runserver 0.0.0.0:8000 --settings=lms.envs.production

   # Start CMS (in another terminal)
   ./manage.py cms runserver 0.0.0.0:8001 --settings=cms.envs.production

For production, use a WSGI server like Gunicorn:

.. code-block:: bash

   # Install Gunicorn
   pip install gunicorn

   # Start LMS
   gunicorn -c /opt/edx-platform/lms/envs/gunicorn.py lms.wsgi:application

   # Start CMS
   gunicorn -c /opt/edx-platform/cms/envs/gunicorn.py cms.wsgi:application


TODO: The whole frontend

Verification Steps
******************

After starting the services, verify the installation:

1. Access the LMS at ``http://localhost:8000``
2. Access CMS (Studio) at ``http://localhost:8001``
3. Log in with the superuser credentials you created
4. Check that all services are running:

   .. code-block:: bash

      sudo systemctl status mysql
      sudo systemctl status mongod
      sudo systemctl status redis-server
      sudo systemctl status memcached
      sudo systemctl status elasticsearch

Production Considerations
*************************

For production deployments, additional configuration is required:

Move Services
=============

In this simple setup all services compete for server resources. It
is better to run MySQL, redis, Memcached, Elasticsearch, and MongoDB
on their own dedicated servers or hosted services.

Web Server Configuration
========================

* Install and configure Nginx or Apache as a reverse proxy
* Configure SSL/TLS certificates
* Set up proper logging and log rotation
* Configure static and media file serving

Service Management
==================

* Create systemd service files for LMS, CMS, and Celery workers
* Set up automatic restart on failure
* Configure resource limits and monitoring

Security Hardening
==================

* Use strong passwords for all database users
* Configure firewall rules (ufw or iptables)
* Keep all services updated with security patches
* Use separate database users with minimal required privileges
* Configure ALLOWED_HOSTS in Django settings
* Disable DEBUG mode in production settings

Performance Optimization
========================

* Configure appropriate worker counts for Gunicorn
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

Common Issues
*************

Port Conflicts
==============

If ports 8000 or 8001 are in use, modify the runserver commands to use different ports.

Memory Issues
=============

Ensure sufficient RAM is available. Consider adding swap space if running on limited hardware.

Migration Failures
==================

If migrations fail, check database connectivity and permissions. Review migration logs for specific errors.

Static Asset 404 Errors
=======================

Ensure ``collectstatic`` completed successfully and your web server is configured to serve static files from the correct directory.

Service Connection Errors
=========================

Verify all required services (MySQL, MongoDB, Redis, Elasticsearch) are running and accessible on the configured hosts and ports.

Alternative: Using Docker Compose Without Tutor
***********************************************

If you want containerization benefits without Tutor's abstractions, you can create a custom Docker Compose setup:

#. Create separate containers for each service
#. Mount edx-platform code as volumes
#. Configure networking between containers
#. Use custom entrypoint scripts for initialization

This approach provides isolation while maintaining direct control over the configuration.
Ongoing expeirments in adopting this configuration are happening at `Minimal edX Platform <https://github.com/feanil/minimal-edx-platform>`_.


See Also
********

* :ref:`Installing and Starting the Open edX Platform`
* `Open edX Developer Documentation <https://docs.openedx.org/en/latest/developers/>`_
* `edx-platform Repository <https://github.com/openedx/edx-platform>`_


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
