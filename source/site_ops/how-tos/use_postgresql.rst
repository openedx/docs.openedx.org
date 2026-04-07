.. _use postgresql:

Use PostgreSQL as the Relational Database Backend
#################################################

.. note::

   PostgreSQL support was introduced in the Verawood release. The Tutor plugin
   that enables this feature (`tutor-contrib-postgresql <https://github.com/qasimgulzar/tutor-contrib-postgresql>`_)
   is under active development. Migration from an existing MySQL installation is
   not yet supported. See `Current PostgreSQL Limitations`_ for details.

PostgreSQL is a powerful open source relational database system with a strong
reputation for reliability, standards compliance, and extensibility. It is a
common choice for production web applications and is widely supported by
managed cloud database services such as Amazon RDS, Google Cloud SQL, and
Azure Database for PostgreSQL.

Historically, the Open edX platform used MySQL as its only supported relational
database. As of the Verawood release, PostgreSQL is also supported as a
relational database backend for the Open edX platform, thanks to community
contributions that updated the platform's Django migrations and field adapters
to work correctly across both database engines.

Prerequisites
*************

- A Tutor-based Open edX deployment (local or Kubernetes)
- Tutor Verawood or later
- A fresh Open edX installation (see `Current PostgreSQL Limitations`_)

Installation
************

PostgreSQL support is provided via the community-maintained Tutor plugin
``tutor-contrib-postgresql``, authored by `@qasimgulzar
<https://github.com/qasimgulzar>`_.

.. warning::

   This plugin is under active development and has not yet reached a stable
   release. Use in production environments is at your own risk. Review the
   `plugin repository <https://github.com/qasimgulzar/tutor-contrib-postgresql>`_
   for the latest status before proceeding.

Step 1: Install the plugin
==========================

.. code-block:: bash

   pip install git+https://github.com/qasimgulzar/tutor-contrib-postgresql

Step 2: Enable the plugin
=========================

.. code-block:: bash

   tutor plugins enable postgresql

Step 3: Build the Open edX image
=================================

The Open edX image must be rebuilt to include the necessary PostgreSQL client
libraries and Python packages (``psycopg2``).

.. code-block:: bash

   tutor images build openedx

Step 4: Launch the platform
============================

.. code-block:: bash

   tutor local launch

This will initialize a fresh Open edX database in PostgreSQL and run all
Django migrations against it.

.. _Current PostgreSQL Limitations:

Current Limitations
*******************

Fresh installations only
========================

At this time, PostgreSQL support is available for fresh Open edX installations
only. There is no supported or documented migration path from an existing MySQL
database to PostgreSQL. Operators with an existing MySQL-backed deployment who
wish to switch to PostgreSQL will need to wait for migration tooling and
documentation to be developed.

If you are interested in contributing to or tracking the development of
MySQL-to-PostgreSQL migration support, see the `tutor-contrib-postgresql
repository <https://github.com/qasimgulzar/tutor-contrib-postgresql>`_ and the
`original platform pull request
<https://github.com/openedx/openedx-platform/pull/35762>`_.

Known rough edges
=================

PostgreSQL support was introduced with the following known limitations that may
be addressed in subsequent releases.

- Opaque key adapter coverage for v2 content libraries (beta libraries in
  Studio) may be incomplete. Runtime errors related to ``LearningContextKey``
  or ``UsageKey`` serialization, if encountered, should be reported to the
  plugin maintainer.
- The ``tutor-contrib-postgresql`` plugin does not yet have a stable release.
  Install directly from the GitHub repository as shown above.

Getting Help
************

PostgreSQL support for the Open edX platform is a community-driven effort. If
you encounter issues or have questions:

- Open an issue on the `tutor-contrib-postgresql repository
  <https://github.com/qasimgulzar/tutor-contrib-postgresql/issues>`_
- Post on the `Open edX discussion forum <https://discuss.openedx.org>`_


.. seealso::

   :ref:`Open edX Databases`

   `Tutor PostgreSQL plugin <https://github.com/qasimgulzar/tutor-contrib-postgresql>`_


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-04-10   | sarina                        |  Verawood      |   Pass                         |
+--------------+-------------------------------+----------------+--------------------------------+