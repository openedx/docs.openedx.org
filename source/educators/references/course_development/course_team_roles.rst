.. _Guide to Course Team Roles:

###########################
Guide to Course Team Roles
###########################

.. tags:: educator, reference

To give team members access to Studio, and the instructor dashboard in the LMS
you assign one of these course team roles to them.

* Staff

* Limited Staff

* Admin

* Course Data Researcher

You can assign these privileged roles when you work in either the LMS or
Studio. The people who have these roles can work on your course in Studio and
the LMS. For more information about assigning roles to team members in Studio,
see :ref:`Add Course Team Members`.

You can also designate teams of people to beta test your course or to moderate
and manage its discussions by assigning other roles in the LMS. Beta testers
and discussion team members must be enrolled in your course, but they do not
need to have the Staff or Admin role. For more information, see
:ref:`Manage Course Beta Testing` and :ref:`Assign discussion roles <Assign discussion roles>`.

For more information about how to add course team members, see
:ref:`Add Course Team Members`.

.. _Administrative Team Roles:

*************************
Administrative Team Roles
*************************

To provide access to features on the instructor dashboard in the LMS, you
can assign the Staff role or the Admin role to course team members.

Team members who have either of these roles can work on your course in Studio
immediately, and can also use the LMS. For more information about
assigning roles while you run your course, see :ref:`Add Course Team Members`.

You can also designate teams of people to beta test your course and to
moderate and manage its discussions by assigning other LMS roles. The beta
testers and discussion administrators must be enrolled in your course, but
they do not need to have Staff or Admin access. For more information, see
:ref:`Manage Course Beta Testing` and :ref:`Assign discussion roles <Assign discussion roles>`.

For more information about how to add course team members, see
:ref:`Add Course Team Members`.


==================
The Staff Role
==================

Course team members who have the Staff role can complete the following tasks.

* View the course before the course start date.

* Enroll and unenroll learners.

* Access and modify grades for individual learners. For example, users with the
  Staff role can reset an individual learner's attempt to answer a question.

* See course HTML errors.

* Send email messages to course participants.

* Activate course certificates.

======================
The Limited Staff Role
======================

Course team members who have the Limited Staff role can do all of the Staff tasks
but without content editing permissions. This role has no access to Studio.

==============
The Admin Role
==============

Course team members who have the Admin role can complete all the tasks that
team members who have the Staff role can complete. In addition, they can
complete the following tasks.

* Access and modify grades for all learners in a course. For example, users
  with the Admin role can reset all learners' attempts to answer a question.

* Add team members to, and remove them from, the Staff role.

* Add team members to, and remove them from, the Admin role.

* Add and remove team members as beta testers.

* Add team members to, and remove them from, the Discussion Admin or
  Discussion Moderator role.

* Add enrolled learners to, and remove them from, the Community TA or Group
  Community TA role.

  .. note:: To moderate course discussions, team members must explicitly be
     added to a discussion moderation role in addition to having the course
     team Staff or Admin role. For more information, see
     :ref:`Assign discussion roles <Assign discussion roles>`.


.. _Course Data Researcher Role:

The Course Data Researcher Role
================================

Course data researchers can access the Data Download tab on the instructor dashboard.

Course data researchers can:

* :ref:`View and download learner data <View Learner Data>`
* :ref:`View Anonymized Learner IDs`
* :ref:`View Certificate Data`
* :ref:`View Learners Not Yet Enrolled`

.. _New System Course Authoring Roles:

***********************************************************************
Course Authoring Roles Under the New Roles and Permissions System
***********************************************************************

.. note::
    These roles are available when your platform has enabled Course
    Authoring — an opt-in feature disabled by default.
    This must be enabled by your site administrator. See :ref:`Enabling RBAC in Verawood`
    for instructions on how to enable it. The legacy Staff and Admin roles
    remain available on platforms that have not yet enabled this feature.

Course Admin and Course Staff are the new system's equivalents of the legacy
Admin and Staff roles for Studio authoring: same responsibilities, new
assignment mechanism. The day-to-day experience in Studio is unchanged —
these roles carry the same capabilities, just under new names and managed
through the Roles and Permissions console.

Existing role assignments require migration to take effect in the new system.
New role assignments share the behavior of their legacy counterparts across the
full platform, not only in Studio.

=============
Course Admin
=============

Course Admins have full authoring access and can manage the course team.
They can do everything a Course Staff member can do, and can also add,
remove, and change roles for team members in the Roles and Permissions console.

=============
Course Staff
=============

Course Staff members can operate the full course lifecycle in Studio, including
publishing content, editing schedules, managing advanced settings, and importing
and exporting course content.

.. seealso::

  :ref:`Add Course Team Members` (how-to)

  :ref:`Manage Course Beta Testing` (how-to)

  :ref:`Manage Course Authoring Roles` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+------------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                    |
+--------------+-------------------------------+----------------+------------------------------------------------------------------+
| 2025-07-30   | eduNEXT                       | Verawood       | Pass                                                             |
+--------------+-------------------------------+----------------+------------------------------------------------------------------+
| 2025-04-13   | sarina                        | Sumac          | Pass                                                             |
+--------------+-------------------------------+----------------+------------------------------------------------------------------+
| 2025-03-07   | Docs WG                       |  Sumac         | `Fail <https://github.com/openedx/docs.openedx.org/issues/958>`_ |
+--------------+-------------------------------+----------------+------------------------------------------------------------------+
