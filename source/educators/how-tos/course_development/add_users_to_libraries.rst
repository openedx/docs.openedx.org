.. _Add users to Libraries:

Manage Library User Access
##########################

.. tags:: educator, how-to

Access to a library team starts from the library home page in Studio and is
managed in the Roles and Permissions console. This article explains the
library roles and how to add and manage members of a library team.

Any change made in the Roles and Permissions console applies to this library
only. It does not change what that user can do in other libraries or in
courses.

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

Access the Roles and Permissions Console
*****************************************

#. From the home page of the library in Studio, select the :guilabel:`ⓘ Library Info` button on
   the top right of the page to open the right sidebar.

   .. image:: /_images/educator_how_tos/library_info_button.png
      :alt: The Library Info button appears below the header, on the top-right of the page.

#. In the right sidebar, select :guilabel:`Manage Access`. This opens the Roles and
   Permissions console in a new browser tab, filtered to this library's team.

   .. image:: /_images/educator_how_tos/library_manage_access_button.png
      :alt: The "Manage Access" button appears in the right sidebar, below the Published status and Organization information.
      :scale: 40
      :align: center

For a full description of the console's tabs, filters, and audit view, see
:ref:`Use Roles and Permissions Console`.

Find and Audit Team Members
****************************

Use search or filters to find a team member. Select the option in the
**Actions** column to open their audit view, which shows their current
role and the permissions it grants for this library.

   .. image:: /_images/educator_how_tos/library_team_roles_edit_user_screen.png
      :alt: The audit view for one team member, showing their role (Library Admin) and a table of which permissions that role grants them.

Assign a Role
**************

Only Library Admins and global site admins can assign roles.

#. In the Roles and Permissions console, select **Assign Role**.

   This opens the Assign Role wizard. Use it both to add a new team member
   and to give an existing team member an additional role.

#. In **Step 1: Who and Role**, enter one or more usernames or email
   addresses, separated by commas, and select the role to assign: Library
   Admin, Library Author, Library Contributor, or Library User.

   .. image:: /_images/educator_how_tos/library_team_roles_assign.png
      :alt: The Assign Role wizard's first step, with a text box for entering users by username or email and a dropdown for the role to assign.

   Users must have an existing account. If any entry does not match a user,
   the input shows an error for that entry and blocks the flow until
   corrected.

#. Select **Next**.

#. In **Step 2: Where It Applies**, select this library to apply the role to.

#. Select **Save**. After saving, the new role assignments appear in the team
   table.

   .. image:: /_images/educator_how_tos/library_team_roles_assign_save.png
      :alt: The "Save" button in the Assign Role wizard.

Remove a Role
**************

Library Admins and global site admins can remove role assignments.

#. In the team members list, find the user whose role you want to remove and
   select the option to open their audit view.

#. In the audit view, find the role to remove and select the option to
   remove that role.

   .. image:: /_images/educator_how_tos/library_team_roles_delete.png
      :alt: The remove-role control on a role card in the audit view.

#. Review the confirmation message and select **Remove** to confirm, or
   **Cancel** to keep the current assignment.

   .. image:: /_images/educator_how_tos/library_team_roles_remove_role_popup.png
      :alt: The confirmation dialog, explaining that removing the role also removes all library access if it is the user's only role.

.. note::

    After a role is removed, if the user has no roles left for this library,
    they will no longer have access and will stop appearing in the team list.
    Their roles in other libraries or courses are not affected.

.. note::
    With Verawood, this same Roles and Permissions console can also manage
    course team roles, if your site has enabled Course Authoring. See
    :ref:`Manage Course Authoring Roles` for the equivalent course workflow. This
    doesn't change how library access works — everything above applies the
    same way whether or not Course Authoring is enabled.

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

    :ref:`Use Roles and Permissions Console` (how-to)

    :ref:`Manage Course Authoring Roles` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-12-11   | Product WG                    | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
| 07/02/2025   | Leira (Curricu.me)            | Sumac          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
| [DATE]       | [REVIEWER]                    |   Verawood     | [PASS/FAIL]                    |
+--------------+-------------------------------+----------------+--------------------------------+
