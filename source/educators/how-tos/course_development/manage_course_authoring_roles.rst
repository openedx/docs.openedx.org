.. _Manage Course Authoring Roles:

Manage Course Authoring Roles
##############################################################

.. tags:: educator, how-to

This article covers the course authoring roles introduced in the Verawood
release. Whether these roles or the ones described in
:ref:`Add Course Team Members` apply to your course team depends on whether
Course Authoring is enabled for your site.

.. note::
    This feature is not enabled by default. See the operator release notes:
    :ref:`Enabling RBAC in Verawood`
    for instructions on how to enable it. For more on what's included in this
    release, see :ref:`Verawood Course Authoring Roles`.

.. contents::
  :local:
  :depth: 2

Course Roles
*************

Courses use roles to control what each team member can do. See
:ref:`Course Authoring Roles Under the New Roles and Permissions System <New System Course Authoring Roles>`
for more detail on the following course roles:

* Course Admin
* Course Staff

Access the Roles and Permissions Console
*****************************************

The Roles and Permissions console can be opened from the Studio home page.
A filtered view, scoped to a specific course, can be accessed from the
course Settings menu.

To open the console for a specific course:

#. In Studio, open the **Settings** menu for your course.

#. Select **Roles and Permissions**. The console opens in a new browser tab,
   filtered to show only this course's team.

   .. image:: /_images/educator_how_tos/course_settings_roles_and_perms.png
      :alt: The Settings menu in Studio, showing the Roles and Permissions option

Find and Audit Team Members
****************************

Once you open the console, your course team is shown in the **Team Members**
tab. The tab lists all users with a role assignment on this course. Use the
search bar and filters to find a specific user.

Select the option in the **Actions** column to open a user's audit view,
which lists all of their role assignments.

For a detailed description of the console and its filters, see
:ref:`Use Roles and Permissions Console`.

Assign a Role
**************

Only Course Admins and global site admins can assign roles.

#. In the Roles and Permissions console, select **Assign Role**.

   .. image:: /_images/educator_how_tos/assign_role_button.png
      :alt: The Assign Role button in the Roles and Permissions console

   This opens the Assign Role wizard.

#. In **Step 1: Who and Role**, enter one or more usernames or email addresses,
   separated by commas. Select the role to assign.

   .. image:: /_images/educator_how_tos/assign_role_step1_manage_roles.png
      :alt: Step 1 of the Assign Role wizard, showing a text input for users and a role selector

   Users must have an existing account. If any entry does not match a user,
   the input shows an error for that entry and blocks the flow until corrected.

#. Select **Next**. If all users are valid, the wizard moves to Step 2.

#. In **Step 2: Where It Applies**, select one or more courses to apply the
   role to. Use the search bar or Organization filter to find a specific course.

   .. image:: /_images/educator_how_tos/assign_role_step2_manage_roles.png
      :alt: Step 2 of the Assign Role wizard, showing a list of courses with checkboxes

   .. note::
       The courses and organizations available here reflect where the Course
       Authoring feature is actually enabled. If a role assignment doesn't
       seem to take effect right away, check with your site operator — this
       can happen briefly during a flag change.

#. Select **Save**. After saving, the new role assignments appear in the Team
   Members table and a confirmation message is shown.

Remove a Role
**************

Course Admins and global site admins can remove role assignments.

#. In the Team Members tab, find the user whose role you want to remove and
   select the option to open their audit view.

#. In the user audit view, find the role assignment to remove and select
   the option to remove the role assignment in the **Actions** column.

   .. image:: /_images/educator_how_tos/remove_role_icon.png
      :alt: The remove-role control in the Actions column of the user audit view

#. Review the confirmation message and select **Remove** to confirm, or
   **Cancel** to keep the current assignment.

.. note::
    A role assignment tied to a course where the Course Authoring flag is
    disabled still appears in the Team Members table and the user audit
    view. The option to remove it is unavailable, with a message explaining
    why.

.. note::

    You cannot remove your own admin role. If you need to revoke your own
    access, another user with the required permissions must do it.

    Super Admin and Global Staff roles are managed at the platform level and
    cannot be removed from the Roles and Permissions console.

.. seealso::

    :ref:`Use Roles and Permissions Console` (how-to)

    :ref:`Guide to Course Team Roles` (reference)

    :ref:`Add Course Team Members` (how-to)

    :ref:`Add users to Libraries` (how-to)

    :ref:`Manage Course Beta Testing` (how-to)

    :ref:`Assign discussion roles <Assign discussion roles>` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| [DATE]       | [REVIEWER]                    |   Verawood     | [PASS/FAIL]                    |
+--------------+-------------------------------+----------------+--------------------------------+
