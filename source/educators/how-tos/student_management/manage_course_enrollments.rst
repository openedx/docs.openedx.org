.. :diataxis-type: how-to

.. _Manage_Course_Enrollments:

##############################
Manage Course Enrollments
##############################

.. _view_enrollment_count:

=========================
View an Enrollment Count
=========================

After you create a course, you can access the total number of people who are
enrolled in it. Note the following information about how this count is
computed.

* In addition to learners, the enrollment count includes all course team
  members, including Admins and Staff. (To work with a course in Studio or the
  LMS you must be enrolled in that course.)

* The enrollment count displays the number of currently enrolled learners and
  course team members. It is not a historical count of everyone who has ever
  enrolled in the course.

  .. note:: Learners can unenroll from courses, and course Admins and Staff
   can unenroll learners when necessary.

The total number of current enrollees is shown as the sum of the number of
people who selected each of the certification tracks (verified, professional,
or honor) that is available for your course.

To view the enrollment count for a course, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Course Info** if necessary.

   The **Enrollment Information** section of the page that opens shows the
   number of people who are currently enrolled in your course and in each of
   the certification tracks.


*********************************
Enroll Learners in a Course
*********************************

To enroll learners or course team members, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Membership**.

#. In the **Batch Enrollment** section of the page, enter the username or email
   address of the learner, or enter multiple names or addresses separated by
   commas or new lines.

   You can copy and paste data from a CSV file of email addresses. However,
   note that this feature is better suited to courses with smaller enrollments,
   rather than courses with massive enrollments.

#. For **Role of the users being enrolled**, select the role of the learner.

   * If the learner is a member of the course staff, select **Partner**.
   * If the learner is not a member of the course staff, select **Learner**.

   .. note::
    All of the users that you enroll at one time must have the same role. If
    you have some users who are partners and others who are learners, you must
    complete two batch enrollments.

#. In the **Enter the reason why the students are to be manually enrolled or
   unenrolled** field, enter a specific, detailed reason why you want to
   enroll these learners.

#. To streamline the course enrollment process, leave **Auto Enroll** selected.

#. To send learners an email message, leave **Notify students by email**
   selected.

#. Select **Enroll**.

You can view or download a list of the people who are enrolled in the course.
For more information, see :ref:`Student Data`.

.. note::
 When you enroll learners in a course, all learners are automatically enrolled
 in the audit enrollment track. For more information about course enrollment
 tracks, see :ref:`enrollment track<enrollment_track_g>`.



.. note:: If your course has a fee, and an organization wants to purchase
   enrollment for multiple seats in your course at one time, you can create
   enrollment codes for the organization. The organization then distributes
   these enrollment codes to its learners to simplify the enrollment process.
   You can also create coupon codes to give learners a discount when they
   enroll in your course. For more information, see :ref:`Enable
   and Create Enrollment Codes`.

.. _Report Learners Not Yet Enrolled:

********************************
Report Learners Not Yet Enrolled
********************************

After you enroll learners in a course using the **Auto Enroll** option, any
learner who does not yet have a user account must register and activate an
account to complete the enrollment process. In addition, the learner must
register the account using the same email address that was used for auto
enrollment. You can download a report of auto enrolled email addresses that do
not yet correspond to an enrolled learner.

To download this report, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. In the **Reports** section of the page, select **Download a CSV of learners
   who can enroll**.

  A status message indicates that report generation is in progress. This
  process can take some time to complete, but you can navigate away from this
  page and do other work while it runs.

  To track the progress of the report process, reload the page in your browser
  and scroll down to the **Pending Tasks** section.

4. To open or save the report, select the
   ``{org}_{course_id}_may_enroll_info_{date}.csv`` file name at the bottom of
   the page.


.. _unenroll_student:

*********************************
Unenroll Learners from a Course
*********************************

You can remove learners from a course by unenrolling them. To prevent learners
from re-enrolling, course enrollment must also be closed. You use Studio to set
the **Enrollment End Date** for the course to a date in the past. For more
information, see :ref:`Scheduling Your Course`.

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
 :class: dropdown

  :ref:`Enrollment_Requirements` (reference)