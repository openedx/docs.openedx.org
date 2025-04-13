.. _Manage_Course_Enrollments:

#########################
Manage Course Enrollments
#########################

.. tags:: educator, how-to

You can enroll and unenroll learners from the instructor dashboard. See :ref:`Enrollment_Requirements` for more information.

***************************
Enroll Learners in a Course
***************************

To enroll learners or course team members, follow these steps. Note that this will
enroll learners/team members even if the **Enrollment Start Date** has not yet passed.

#. :ref:`View the live version of your course<View Published Content>`

#. Select **Instructor**, and then select **Membership**.

#. In the **Batch Enrollment** section of the page, enter the username or email
   address of the learner, or enter multiple names or addresses separated by
   commas or new lines.

    .. image:: /_images/educator_how_tos/batch_enrollment_instructor_dash.png
     :width: 500

   You can copy and paste data from a CSV file of email addresses. However,
   note that this feature is better suited to courses with smaller enrollments,
   rather than courses with massive enrollments.

#. To streamline the course enrollment process, leave **Auto Enroll** selected.

#. To send learners an email message, leave **Notify students by email**
   selected.

#. Select **Enroll**.

You can view or download a list of the people who are enrolled in the course.
For more information, see :ref:`Learner Data`.

.. note::
 When you enroll learners in a course, all learners are automatically enrolled
 in the audit enrollment track. For more information about course enrollment
 tracks, see :term:`Enrollment Track`.

Enroll Beta Testers in a Course
*******************************

To enroll :ref:`beta testers <About Course Beta Testing>` in the course, follow
the above instructions, but utilize the **Batch Beta Tester Addition** box below
the **Batch Enrollment** box on the Membership page of the instructor dashboard.

.. image:: /_images/educator_how_tos/batch_beta_enrollment_instructor_dash.png

.. _unenroll_student:

*******************************
Unenroll Learners from a Course
*******************************

You can remove learners from a course by unenrolling them. To prevent learners
from re-enrolling, course enrollment must also be closed. You use Studio to set
the **Enrollment End Date** for the course to a date in the past. For more
information, see :ref:`Course Schedule` and :ref:`Set Course Schedule`.

.. note:: Unenrollment does not delete data for a learner. An unenrolled
   learner's state remains in the database and is reinstated if the learner
   does re-enroll.

To unenroll learners, you supply the email addresses of enrolled learners.

#. View the live version of your course.

#. Select **Membership**.

#. In the **Batch Enrollment** section of the page, enter a username or an
   email address, or multiple names or addresses separated by commas or new
   lines.

#. In the **Enter the reason why the students are to be manually enrolled or
   unenrolled** field, enter a specific, detailed reason why you want to
   unenroll these learners.

#. To send learners an email message, leave **Notify students by email**
   selected.

   .. note:: The **Auto Enroll** option has no effect when you select
     **Unenroll**.

#. Select **Unenroll**. The course is no longer listed on the learners'
   **Current Courses** dashboards, and the learners can no longer access the
   course content or contribute to discussions or the wiki.


.. seealso::

 :ref:`Enrollment_Requirements` (reference)

 :ref:`View Course Enrollments` (how-to)

 :ref:`View Learners Not Yet Enrolled` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+-----------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                   |
+--------------+-------------------------------+----------------+-----------------------------------------------------------------+
| 2025-04-13   | sarina                        | Sumac          | Pass                                                            |
+--------------+-------------------------------+----------------+-----------------------------------------------------------------+
| 2025-03-07   | Docs WG                       | Sumac          | `Fail <https://github.com/openedx/docs.openedx.org/issues/957>`_|
+--------------+-------------------------------+----------------+-----------------------------------------------------------------+
