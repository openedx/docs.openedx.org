.. _Enable CCX:

####################################
Enabling Custom Courses
####################################

.. tags:: site operator

To enable designated users to create custom courses (CCX) on your instance of
Open edX, you must configure the ``server-vars.yml`` file in the edX platform.

Tutor Instructions
******************

To enable Custom Courses (CCX), the `CUSTOM_COURSES_EDX <https://docs.openedx.org/projects/edx-platform/en/latest/references/featuretoggles.html#featuretoggle-CUSTOM_COURSES_EDX>`_
flag must be enabled by making a `Tutor plugin <https://docs.tutor.edly.io/tutorials/plugin.html#modifying-existing-files-with-patches>`_.

.. code-block::

  from tutor import hooks

  hooks.Filters.ENV_PATCHES.add_item(
      (
          "openedx-common-settings",
          "CUSTOM_COURSES_EDX = True"
      )
  )


Legacy (non-Tutor) installations
********************************

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

#. Stop the LMS server.

#. Create or update the file ``/edx/app/edx_ansible/server-vars.yml`` to
   include the CCX feature flag.

   .. code-block:: yaml

     EDXAPP_FEATURES:
       CUSTOM_COURSES_EDX: true

#. Run the command ``/edx/bin/update``.

   .. code-block:: bash

      sudo /edx/bin/update edx-platform <your-branch-name>

#. Restart the LMS server.

.. include:: /links.txt


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
