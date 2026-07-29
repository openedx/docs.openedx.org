.. _Add Course Team Members:

###########################
Add Course Team Members
###########################

.. tags:: educator, how-to

You can add course staff members from Studio. You can add course staff members, limited staff, admins, beta testers, and discussion moderators from the LMS Instructor Dashboard.

*****************************
Add Course Staff from Studio
*****************************

.. youtube:: IwuGccK49m8

Course team members are users who help you build your course. To add someone
to the course team, you must meet these prerequisites.

* You must have the Admin role in the course. When you create a new course in Studio, you are automatically an Admin in the course, meaning you can create and add course creators, in addition to being able to create and manage course content.

* The team member that you want to add must register a user account and
  activate the account.

* You need the same, registered email address for the team member you want to add.

Other course team members can edit the course and perform all tasks except
adding and removing other team members and granting Admin access.

.. note::
 Any course team member can delete content created by other team members.

To add a course team member, follow these steps.

#. Ensure you have Admin access.
#. Ensure that the new team member has registered and activated an account.
#. In Studio, from the **Settings** menu, select **Course Team**.
#. Select **Add a New Team Member**.
#. Enter the new team member's email address, then select **ADD USER**.
#. You can optionally upgrade the user to an Admin role. Admins can add other users to the course team.

The new team member can now work on the course in Studio.

* To preview the course in the LMS, the team member must enroll in the course.

* To moderate course discussions, the team member must also have one of the
  discussion roles. For more information, see
  :ref:`Assign discussion roles <Assign discussion roles>`.



.. _Assign Course Team Roles:

***********************************************************
Assign Course Team Roles from the LMS Instructor Dashboard
***********************************************************

You can also assign privileged roles to users when you work in the LMS by
selecting **Instructor** and then **Membership**.

Assigning a course team role to a user both adds the user to the course team
and assigns the role to that user.

To assign the Staff or Admin role to a team member, you must meet these prerequisites.

* You must have the Admin role in the course.

* You need the email address or username of each team member you want to add.

* Each of those team members must register a user account for that email
  address or username, activate the account, and enroll in your course.

To assign a privileged role to a course team member, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Membership**.

#. In the **Course Team Management** section, select **Staff** or **Admin**.

#. Under the list of users who currently have that role, enter an email
   address or username, and then select **Add** for the role type.

To remove an assigned role, view the list of users and then select **Revoke
access**.

.. note::
    For installations using the Roles and Permissions console: course team
    management is available from :guilabel:`Settings` > :guilabel:`Roles and
    Permissions` in Studio. See :ref:`Manage Course Authoring Roles` for the
    Course Admin and Course Staff roles available there.

    The Roles and Permissions console (called the Administrative Console in
    earlier releases) is not enabled by default. See the operator release
    notes:
    https://openedx.atlassian.net/wiki/spaces/OEPM/pages/6331662350/RBAC+AuthZ+for+Course+Authoring+-+Operator+Release+Notes#Enabling-the-Feature-Flag
    for instructions on how to enable it.

.. seealso::

  :ref:`Guide to Course Team Roles` (reference)

  :ref:`Manage Course Beta Testing` (how-to)

  :ref:`Manage Course Authoring Roles` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                 |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| 03/19/2025   | John (Curricu.me)             | Sumac          | Pass                                                          |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| 03/07/2025   | Leira (Curricu.me)            | Sumac          | Fail (https://github.com/openedx/docs.openedx.org/issues/881) |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| [DATE]       | [REVIEWER]                    | Verawood       | [PASS/FAIL]                                                   |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
