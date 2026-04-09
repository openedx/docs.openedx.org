.. _Create a Custom Course CCX:

Create a Custom Course (CCX)
############################

.. tags:: educator, how-to

A custom course (CCX) lets you reuse existing course content for a new group
of learners on a different schedule. As a CCX coach, you select the content to
include, enroll learners, set the schedule, and manage grading.

.. note::

   Your site operations team will need to first :ref:`Enable CCX` on your
   Open edX instance before you can use this feature. Once enabled, a course
   admin must also enable CCX for the specific course in Studio Advanced
   Settings and assign you as the CCX coach.

.. contents:: Steps
   :local:
   :depth: 1

.. note::
   A CCX can contain only content from an existing course. You cannot author
   new content within a CCX.


Enable CCX for Your Course
***************************

A course admin must enable CCX in Studio for the specific course before a CCX
coach can be assigned. CCX is disabled at the course level by default.

#. In Studio, open the course and select :guilabel:`Advanced Settings` from the
   **Settings** menu.
#. Locate the ``Enable CCX`` key and set its value to ``true``.
#. Select :guilabel:`Save Changes`.


Add a CCX Coach
****************

A CCX requires exactly one CCX coach. Before assigning a coach, confirm that
the person has registered an account in the LMS and enrolled in the course.

#. In the LMS, select :guilabel:`Instructor`, then select
   :guilabel:`Membership`.
#. In the **Course Team Management** section, open the **Select a course team
   role** dropdown and select **CCX Coaches**.
#. Enter the coach's username or email address, then select
   :guilabel:`Add CCX Coach`.

When the CCX coach next logs in, the :guilabel:`CCX Coach` tab will appear in
the course navigation.

.. note::
   The CCX Coach dashboard is not accessible to team members with the Admin or
   Staff roles.


Create the Custom Course
*************************

Once assigned as CCX coach, you can create a CCX from inside the original
course.

#. In the LMS, open the course and select the :guilabel:`CCX Coach` tab.
#. Enter a name for your CCX.

   .. tip::
      Choose a name that distinguishes this CCX from others based on the same
      course.

#. Select :guilabel:`Coach a new Custom Course for edX`.

You are redirected to the full CCX Coach Dashboard. To return to the CCX
later, open the original course and select the :guilabel:`CCX Coach` tab.


Configure the CCX Schedule
***************************

The **Schedule** tab is where you select source course content to include in
the CCX and set start and due dates for each unit.

#. In the CCX Coach Dashboard, select the :guilabel:`Schedule` tab.
#. Use the dropdown menus to browse the course content hierarchy and select
   items to include.

   - To include all source course content, select :guilabel:`Add All Units`.

#. For each unit, set a start date and due date as needed. To edit dates after
   adding a unit, hover over the unit row in the content hierarchy.
#. Select :guilabel:`Save Changes`.


Enroll Learners
****************

#. In the CCX Coach Dashboard, select the :guilabel:`Enrollment` tab.
#. Select :guilabel:`Student List Management` to add individual learners who
   already have platform accounts.
#. To send email invitations to learners added through Batch Enrollment, select
   **Notify users by email**. Learners are automatically enrolled when they
   access the invitation link.


View and Download Grades
*************************

#. In the CCX Coach Dashboard, select the :guilabel:`Student Admin` tab.
#. From this tab, you can view the gradebook or download learner grades.


Modify the Grading Policy
**************************

A CCX coach can adjust the grading policy inherited from the original course.

.. warning::
   Modifying the grading policy incorrectly can make your CCX unusable. Only
   attempt this if you are confident you understand how your changes affect
   grading.

#. In the CCX Coach Dashboard, select the :guilabel:`Grading Policy` tab.
#. Edit the grading policy, which is in JSON format.
#. Verify that the JSON is well-formed before selecting
   :guilabel:`Save Grading Policy`.


.. seealso::

   :ref:`Enable CCX` (site operators how-to)

   :ref:`Guide to Course Team Roles` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|2026-04-09    |  sarina                       | Ulmo           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+