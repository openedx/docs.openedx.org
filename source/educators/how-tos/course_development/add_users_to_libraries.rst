.. _Add users to Libraries:

Manage Library User Access
##########################

.. tags:: educator, how-to

Access to a library team starts from the library home page in Studio and is
managed in the library team manager in the :ref:`Administrative Console <Ulmo
console>`. This article explains the library roles and how to add and manage
members of a library team.

Any change made in the library team manager applies to this library only. It
does not change what that user can do in other libraries or in courses.

.. contents::
  :local:
  :depth: 2

Library Roles
*************

Libraries use roles to control what each team member can do. See
:ref:`authz:Library Roles` for more detail on the following library roles:

* Library User
* Library Contributor
* Library Author
* Library Admin

Library Team Management
***********************

On the Team Management panel, there are three tabs at the top of the page:

* Team Members
* Roles
* Permissions

Any user who has any of the above Library Roles can view these tabs.

Team Members Tab
================

On the Team Members tab, users can see who has access to the Library and which
roles they have. The list of team members is searchable by username or email,
and can be filtered by role, making it easy to understand who else can edit,
publish or manage access.

.. image:: /_images/educator_how_tos/library_team_member_tab.png
    :alt: The Team Members tab of the Admin Console, showing two team members in a table with the columns Name, Email, Role, and Actions
    :width: 800
    :align: center

Roles Tab
=========

The :ref:`authz:Library Roles` tab has a description of each Library role and
the set of permissions each role includes, helping users understand at a glance what
each role covers when granting permissions.

.. image:: /_images/educator_how_tos/library_team_roles_tab.png
    :alt: The Roles tab shows all 4 Library roles and what permissions each role grants
    :align: center

Permissions Tab
===============

The Permissions tab has a :ref:`authz:Library RP Summary Table` that describes
which permissions are assigned to each role. Every permission in the table
includes a short explanation, enabling users to see what role allows which
actions, and compare roles side by side before they change a user's access.

.. image:: /_images/educator_how_tos/library_permissions_tab.png
    :alt: The Permissions tab shows a table of permissions, with a ✅ for permissions a given role allows and a ❌ for permissions not available for that role.
    :align: center


Manage Access for Library Team Members
**************************************

Only Library Admins and global site admins can add or remove team members or change
their roles. All actions in this section affect access to one library only.

To begin, follow these steps to open the Team Management panel:

#. From the home page of the library in Studio, click the :guilabel:`ⓘ Library Info` button on
   the top right of the page to open the right sidebar.

   .. image:: /_images/educator_how_tos/library_info_button.png
      :alt: The Library Info button appears below the header, on the top-right of the page.

#. In the right sidebar, click the :guilabel:`Manage Access` button. This opens the team
   management panel in a new browser tab in the Administrative Console, on the
   Team Members tab.

   .. image:: /_images/educator_how_tos/library_manage_access_button.png
      :alt: The "Manage Access" button appears in the right sidebar, below the Published status and Organization information.
      :scale: 40
      :align: center

View Team Members
=================

Library administrators can audit a user's access to that library via the Team Management panel:

#. Use search or filters to find a user to update and select Edit in the Action
   column to open the user detail view.

   .. image:: /_images/educator_how_tos/library_team_roles_edit.png
      :alt: The "Edit" link appears in the rightmost column of the User table for each row that contains a user.

#. Once "Edit" has been clicked, a new screen is shown that allows admins to
   view what roles a user holds and edit their access to the library.

   .. image:: /_images/educator_how_tos/library_team_roles_edit_user_screen.png
      :alt: The screen for one single user, showing their role (Library Admin) and a table of which permissions that role grants them.


Add a New Team Member
========================

Library administrators can add a new team member via the Team Management panel:

#. In the team management panel, click the :guilabel:`+ Add New Team Member` button in the
   upper right corner to open the Add User pop-up.

   .. image:: /_images/educator_how_tos/library_add_team_member_button.png
      :alt: The Add New Team Member button appears at the top-right of the Library Team Management page

#. In the pop-up window, enter one or more email addresses or usernames of the
   people you want to grant access to, separated by commas. Select the desired
   role to assign, for example Library Admin, Library Author, Library
   Contributor, or Library User.

   .. image:: /_images/educator_how_tos/library_team_roles_assign.png
      :alt: The pop-up modal has a text box for entering users by username or email, and a dropdown menu that shows the available roles to be assigned.

#. Save the changes. After saving, the new user(s) are listed in the team table with their new role.

   .. image:: /_images/educator_how_tos/library_team_roles_assign_save.png
      :alt: The "Save" button appears in the bottom right of the pop-up modal.

Edit User Roles
===============

Library Admins and global site admins can update roles for users who are already
on the library team. To begin, follow these steps to open the Team Management
panel:

#. From the home page of the library in Studio, click the :guilabel:`ⓘ Library Info` button on
   the top right of the page to open the right sidebar.

   .. image:: /_images/educator_how_tos/library_info_button.png
      :alt: The Library Info button appears below the header, on the top-right of the page.

#. In the right sidebar, click the :guilabel:`Manage Access` button. This opens the team
   management panel in a new browser tab in the Administrative Console, on the
   Team Members tab.

   .. image:: /_images/educator_how_tos/library_manage_access_button.png
      :alt: The "Manage Access" button appears in the right sidebar, below the Published status and Organization information.
      :scale: 40
      :align: center

Add a Role to a Team Member
----------------------------

#. Navigate to the "Team Members" tab of the Team Management panel. Use search
   or filters to find the user to update and select "Edit" in the Action column
   to open the user detail view for the user.

   .. image:: /_images/educator_how_tos/library_team_roles_edit.png
      :alt: The "Edit" link appears in the rightmost column of the User table for each row that contains a user.

#. In the user detail view, select :guilabel:`Add New Role` in the upper right corner.

   .. image:: /_images/educator_how_tos/library_team_add_new_role.png
      :alt: The "Add New Role" button appears in the top right corner.


#. In the Add New Role pop-up, open the Roles dropdown and select the new role to add.

   .. image:: /_images/educator_how_tos/library_team_roles_new_role_popup.png
      :alt: The pop-up dialog has a dropdown for selecting a role, and both a Cancel and a Save button in the bottom right.

#. Select Save.

The new role is added for this user in this library and appears in their list of roles.

Remove a Role from a Team Member
--------------------------------

#. Navigate to the "Team Members" tab of the Team Management panel. Use search
   or filters to find the user to update and select "Edit" in the Action column
   to open the user detail view for the user.

   .. image:: /_images/educator_how_tos/library_team_roles_edit.png
      :alt: The "Edit" link appears in the rightmost column of the User table for each row that contains a user.

#. In the user detail view, find the role to remove and select the delete icon for that role.

   .. image:: /_images/educator_how_tos/library_team_roles_delete.png
      :alt: The delete (trash can) icon appears on the top right of each "card", where a card represents one role a user holds.


#. In the Remove role confirmation pop-up, review the message and select Remove
   to confirm, or Cancel to retain the user's current level of access.

   .. image:: /_images/educator_how_tos/library_team_roles_remove_role_popup.png
      :alt: The pop-up dialog, in this example, explains that removing the role for the user will also remove all their Library access as it is the only role the user has.

.. note::

    After "Remove" is selected, that role is removed for this user in this library. If the
    user has no roles left for this library, they will no longer have access and
    will stop appearing in the team list. Their roles in other libraries or courses
    are not affected.


.. seealso::

    :ref:`Navigate the Library Homepage`

    :ref:`Create and edit content in a Library`

    :ref:`Create and edit units in a Library`

    :ref:`Build a Collection in a Library`

    :ref:`Publish Library content`

    :ref:`Search for content in a Library`

    :ref:`Use content sidebars to manage content`

    :ref:`Add and Delete tags in Library content`

    :ref:`Add Library content to a course`

    :ref:`Sync a Library update to your course`

    :ref:`Add a Problem Bank to your course for randomization`

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-12-11   | Product WG                    | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
| 07/02/2025   | Leira (Curricu.me)            | Sumac          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
