.. _Enable Custom Course Settings:

####################################
Enabling Custom Course Settings
####################################

.. tags:: site operator

Tutor Instructions
******************

To enable course developers to add custom fields to a course on your instance 
of Open edX,, the ``ENABLE_OTHER_COURSE_SETTINGS``
flag must be enabled by making a `Tutor plugin <https://docs.tutor.edly.io/tutorials/plugin.html#modifying-existing-files-with-patches>`_.

.. code-block::

  from tutor import hooks

  hooks.Filters.ENV_PATCHES.add_item(
      (
          "openedx-cms-common-settings",
          "ENABLE_OTHER_COURSE_SETTINGS = True"
      )
  )

Legacy (non-Tutor) installations
********************************


To enable course developers to add custom fields to a course on your Open edX
instance, you must configure the ``studio.yml`` file.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

#. Stop the LMS server.

#. Create or update the file ``studio.yml`` to include the custom course 
   settings feature flag.

   .. code-block:: yaml

     'ENABLE_OTHER_COURSE_SETTINGS': true,

#. Restart the LMS server.

.. include:: /links.txt


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
