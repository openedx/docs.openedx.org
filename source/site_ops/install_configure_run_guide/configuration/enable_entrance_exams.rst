.. _Enable Entrance Exams:

########################
Enabling Entrance Exams
########################

.. tags:: site operator

This topic describes how to enable entrance exams in your instance of Open
edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

Course teams can create an entrance exam for the course. Learners must pass the
entrance exam before participating in the course.

To enable this feature on your instance of Open edX, you must enable
entrance exams in Studio and the Learning Management System.

For information about entrance exams, see the *Building and Running an
Open edX Course* and *Open edX Learner's* guides.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

.. include:: configure_milestone_app.rst

*************************************************************************
Enable Entrance Exams in Studio and the Learning Management System
*************************************************************************

In Tutor, entrance exams can be enabled by utilizing the following `Tutor plugin <https://docs.tutor.edly.io/tutorials/plugin.html#modifying-existing-files-with-patches>`_:

.. code-block::

  from tutor import hooks

  hooks.Filters.ENV_PATCHES.add_item(
      (
          "openedx-lms-common-settings",
          "FEATURES['ENTRANCE_EXAMS'] = True"
      )
  )

  hooks.Filters.ENV_PATCHES.add_item(
      (
          "openedx-cms-common-settings",
          "FEATURES['ENTRANCE_EXAMS'] = True"
      )
  )


To enable entrance exams in a non-Tutor environment, you modify the ``lms.yml`` and ``studio.yml``
files, which are located one level above the ``edx-platform`` directory.

#. Set the value of ``ENTRANCE_EXAMS`` in the ``lms.yml`` and
   ``studio.yml`` files to ``True``.

   .. code-block:: none

     # Entrance exams feature flag
     'ENTRANCE_EXAMS': True,

#. Save the ``lms.yml`` and ``studio.yml`` files.

.. include:: /links.txt


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
