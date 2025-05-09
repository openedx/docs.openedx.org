.. _Enable Course Prerequisites:

#############################
Enabling Course Prerequisites
#############################

.. tags:: site operator

This topic describes how to enable course prerequisites in your instance of
Open edX.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

Course teams can set prerequisites for a course. Learners must complete the
prerequisite courses before participating in the course.

To use this feature on your instance of Open edX, you must configure the
Milestones application, then enable prerequisites in Studio and the Learning
Management System.

For information about prerequisites, see the *Building and Running an
Open edX Course* and *Open edX Learner's* guides.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

.. include:: configure_milestone_app.rst

*************************************************************************
Enable Prerequisite Courses in Studio and the Learning Management System
*************************************************************************

To enable prerequisite courses, you modify the ``lms.yml`` and
``studio.yml`` files, which are located one level above the ``edx-platform``
directory.

#. Set the value of ``ENABLE_PREREQUISITE_COURSES`` in the
   ``lms.yml`` and ``studio.yml`` files to ``true``.

   .. code-block:: none

       # Prerequisite courses feature flag
       'ENABLE_PREREQUISITE_COURSES': true,

#. Save the ``lms.yml`` and ``studio.yml`` files.

.. include:: /links.txt


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
