.. _Access_anonymized:

#############################
Access Anonymized Learner IDs
#############################

.. tags:: educator, how-to

Some of the tools that are available for use with the Open edX platform, including
external graders and surveys, work with anonymized learner data. If it becomes
necessary for you to deanonymize previously anonymized data, you can download a
CSV file to use for that purpose.

To download a file of assigned user IDs and anonymized user IDs, follow these
steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. Select **Get Student Anonymized IDs CSV**.

You are prompted to open or save the {course-id}-anon-id.csv file for your
course. This file contains the user ID that is assigned to each learner at
registration and its corresponding Open edX-wide anonymized user ID and course
specific anonymized user ID. Values are included for every learner who ever
enrolled for your course.

To research and deanonymize learner data, you can use this file together with
the ``{course_id}_student_profile_info_{date}.csv`` file of learner data or the
``{course_id}_grade_report_{date}.csv`` file of grades.

.. seealso::
 

 :ref:`Learner Data` (concept)

 :ref:`Columns in the Student Profile Report` (reference)

 :ref:`View and download student data` (how-to)
