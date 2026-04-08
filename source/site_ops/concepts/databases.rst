.. _Open edX Databases:

Open edX Platform Database and Search Technologies
##################################################

.. tags:: site operator, concept

The Open edX platform uses several databases and search backends, each
serving different purposes.

Relational (SQL)
****************

**MySQL**
  The long-standing primary relational database for most services (LMS,
  CMS/Studio), storing users, courses, enrollments, and grades.

**PostgreSQL**
  Newly supported as of the Verawood release, with migrations updated to
  make the Open edX platform compatible across both MySQL and PostgreSQL.
  Changes include dynamic SQL generation based on the database engine,
  cross-database field type handling, and custom psycopg2 adapter
  registration for Open edX's OpaqueKey types like ``CourseLocator``. A
  community-developed Tutor plugin (`tutor-contrib-postgresql <https://github.com/qasimgulzar/tutor-contrib-postgresql>`_)
  supports PostgreSQL-based Tutor deployments. See :ref:`use postgresql`.

**SQLite**
  Used in local development and testing environments.

NoSQL / Document
****************

**MongoDB**
  Used to store course content structure in Studio. There is ongoing work to
  migrate away from MongoDB toward MySQL via the Learning Core
  (`openedx-learning <https://github.com/openedx/openedx-core>`_) initiative.

Caching / In-Memory
*******************

**Redis**
  Used for caching, session storage, and Celery task queuing. Superseded
  Memcached in modern deployments.

**Memcached**
  Legacy caching layer, largely replaced by Redis.

Search
******

**Meilisearch**
  The current primary search engine for content library and course
  authoring search (introduced in Quince), used by the Authoring MFE for
  course and library content discovery, as well as the Catalog MFE for course searching.

**Typesense**
  A supported alternative search backend for site operators, attractive in
  part because it supports raft-based clustering for high availability — a
  limitation that has been noted with Meilisearch. See :ref:`Use Typesense search backend`.

  .. note:: Typesense is currently (as of Verawood) only supported for LMS searching, _not_ Studio/libraries.

**Elasticsearch / OpenSearch**
  Used for older LMS-level search (course catalog, user search). OpenSearch
  is the current preferred variant, with ongoing community discussion about
  whether to deprecate it in favor of lighter-weight alternatives.

Message Broker
**************

**Redis** (also serves this role) **or RabbitMQ**
  Used as a Celery broker for background task processing.

.. seealso::

   :ref:`Use Typesense search backend`

   :ref:`use postgresql`

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-04-10   | sarina                        |  Verawood      |   Pass                         |
+--------------+-------------------------------+----------------+--------------------------------+