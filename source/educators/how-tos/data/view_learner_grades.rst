.. _View Learner Grades:

#####################
View Learner Grades
#####################

.. tags:: educator, how-to

You can access learner grades at any time after you create the course. 

.. contents::
 :local:
 :depth: 1

.. _Access_grades:

****************************************************
Generate a Grade Report for All Learners in a Course
****************************************************

For any course, you can generate grades and then download a file with the
results for all learners in the course, including unenrolled learners. Best practice is to generate a grade report as soon as certificates have been issued for your course.

When you initiate calculations to grade learner work, a process starts on the
Open edX servers. The complexity of your grading configuration and the number of
learners in your course affect how long this process takes. You can download a
report of the calculated grades in a comma-separated values (.csv) file when
the grading process is complete.

You also have the option to review learner grades on the instructor dashboard.
For more information, see :ref:`gradebook`.

To generate and download the grade report for the learners in your course,
follow these steps.

.. important::
   Because the grade report file contains confidential, personally identifiable
   data, be sure to follow your institution's data stewardship policies when
   you open or save this file.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. To start the grading process, select **Generate Grade Report**.

   A status message indicates that the grading process is in progress. This
   process can take some time to complete, but you can navigate away from this
   page and do other work while it runs.

#. To check the progress of the grading process, reload the page in your
   browser and scroll down to the **Pending Tasks** section. The
   status of active tasks is shown in the table.

   When the report is complete, a linked .csv file name becomes available above
   the **Pending Tasks** section. File names are in the format
   ``{course_id}_grade_report_{datetime}.csv``. The most recently generated
   reports appear at the top of the list.

#. To open or save a grade report file, locate and select the link for the
   grade report you requested.

   You can open .csv files in a spreadsheet application to sort, graph, and
   compare data.

.. note::
   To prevent the accidental distribution of learner data, you can download
   grade report files only by selecting the links on this page. Do not copy
   these links for reuse elsewhere, as they expire within 5 minutes. The links
   on this page also expire if the page is open for more than 5 minutes. If
   necessary, refresh the page to generate new links.

.. seealso::
 

 :ref:`Guide to the Grade Report` (reference)


.. _problem_report:

************************************************************
Generate a Problem Grade Report for All Learners in a Course
************************************************************

For any course, you can calculate grades for problems and generate a report
that can be downloaded. The problem grade report for a course shows the number
of points that each learner has earned for each problem, and the number of
possible points for every problem in the course. In addition, the
report shows the final grade score for each learner.

To generate and download the problem grade report for all learners who have
ever enrolled in your course, follow these steps.

.. important:: Because the problem grade report file contains confidential,
   personally identifiable data, be sure to follow your institution's data
   stewardship policies when you open or save this file.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. To start the problem grading process, select **Generate Problem Grade
   Report**.

   A status message indicates that the problem grading process is in progress.
   This process can take some time to complete, but you can navigate away from
   this page and do other work while it runs.

#. To check the progress of the problem grading process, reload the page in
   your browser and scroll down to the **Pending Tasks** section. The status of
   active tasks is shown in the table.

   When the report is complete, a linked .csv file name becomes available above
   the **Pending Tasks** section. File names are in the format
   ``{course_id}_problem_grade_report_{datetime}.csv``. The most recently
   generated reports appear at the top of the list.

#. To open or save a problem grade report file, locate and select the link for
   the problem grade report you requested.

   You can open .csv files in a spreadsheet application to sort, graph, and
   compare data.

.. note:: To prevent the accidental distribution of learner data, you can
   download problem grade report files only by selecting the links on this
   page. Do not copy these links for reuse elsewhere, as they expire within 5
   minutes. The links on this page also expire if the page is open for more
   than 5 minutes. If necessary, refresh the page to generate new links.

.. seealso::
 

 :ref:`Guide to the Problem Grade Report` (reference)


.. _gradebook:

*************************************************
Review Learner Grades on the Instructor Dashboard
*************************************************

You can review a gradebook for a course on the instructor dashboard. To
review grades for a course, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Student Admin**.

#. Select **View Gradebook**. Grades are calculated and the Gradebook displays.

   .. image:: /_images/educator_how_tos/Learner_Gradebook.png
     :alt: Course gradebook with rows for learners and columns for assignments.

The gradebook displays a table, with a row for each learner (\*see note) enrolled in the
course, listed by user name, and a column for each assignment in the course.

.. note:: By default, the gradebook will not include any user enrolled in the course who also has a
   "Course Access Role". This includes course staff, course administrators, course data researchers,
   and beta testers. To see a listing of users who fall into this category, navigate to the Insurector
   Dashboard and refer to the Course Team Management section of the Membership tab.

The gradebook includes the following features:

* **Filtering:** There are several options for filtering the data shown on the gradebook.

  * *Assignment Type:* only show grades for a certain Assignment Type.

  * *Assignment:* only show grades for a single Assignment.

  * *Assignemnt Grade:* when filtering by *Assignment*, only show users with a grade for that
    assignment within a certain range.

  * *Overall Grade:* only show learners whose total course grade is within a certain range.

  * *Track:* only show learners of a certain enrollment mode (e.g. verified, audit, masters).

  * *Cohort:* only show learners in a certain cohort.

  * *Include Course Team Members:* By default, users with certain course roles
    (Staff, Admin, Beta Tester, Course Data Researcher) will be excluded from gradebook results.
    To include those users, you can select this option, which will include those excluded users
    in the gradebook.

* **Searching:** You can search for individual learners by their username, using the search field. Searches are case-insensitive.

* **Grade Override:** You can override the grade that a learner has received for a
  specific graded subsection. For information about how to do this, see
  :ref:`Override in Gradebook`.

.. _Interventions Report:

********************************
Per-Learner Interventions Report
********************************

.. note:: Master’s-only feature

This feature is available in courses with a Master’s track, to support manual learning interventions. It allows you to export per-learner progress and grade information for Master’s track learners, and enables you to identify and reach out to learners who may need additional help.

To download and view the interventions report, follow these steps:

#. View the live version of your course.

#. Select **Instructor**, and then select **Student Admin**.

#. Select **View Gradebook**.

#. Set up the filters to identify the segment of learners you want to view

#. Click the **Download Interventions** button to download a CSV report of progress and grades information for these learners.


The report file contains per-learner information for learners in the Master’s track, including:

* User ID

* Username

* Student Key

* Email

* Full Name

* Course ID

* Cohort

* Activity in this course -- number of videos, problems, and discussion forum posts submitted over the last week and overall in this course

* Assignment grades

* Letter Course Grade

* Numeric Course Grade to-date

Learner data is updated every day to include activity through the end of the previous day (23:59 UTC).


.. _check_student_progress:

****************************************
Check the Progress of a Specific Learner
****************************************

To check a single learner's progress in your course, you can review the data
in the :ref:`grade report<Access_grades>` or :ref:`problem grade
report<problem_report>`, or review the learner's **Progress** page.

The **Progress** page includes a variety of features which allow learners to gauge
their performance in a course. The main features of the **Progress** page are:

* the :ref:`Course Completion<course_completion>` chart, which represents all course content completed, both graded and ungraded,

* the :ref:`Grades<grades_chart>` chart, which compares the current weighted grade compared to the grade required to pass the course and receive a certificate,

* the :ref:`Grade Summary<grade_summary>` table, which lists all assignment types and their weights,

* the :ref:`Detailed Grades<detailed_grades>` display, which lists each graded assignment in the course and the score earned,

* and the :ref:`Certificate Status<certificate_status>` display, which describes whether the learner has earned a certificate.


.. contents::
 :local:
 :depth: 1

.. _View a Specific Learners Progress Page:

=======================================
View a Specific Learner's Progress Page
=======================================

To view a specific learner's **Progress** page, you need their email
address or username. You can check the progress for learners who are either
enrolled in, or who have unenrolled from, the course.

Learners can view their own progress chart and assignment scores when they are
logged in to the course.

To view the **Progress** page for a specific learner, follow these steps.

#. View the live version of your course.

#. Next to **View this course as**, select **Specific student**.

#. In the **Username or email** field that appears, enter the learner's
   username or email address, and then press the Enter key on your keyboard.

#. Select the **Progress** page.

It is important to keep in mind that some of the performance displays may be
impacted by content or grade visibility settings in Studio. The implications of
these settings will be discussed in the following section.

.. seealso::
 
 :ref:`Manage Learner Grades <Grades>` (how-to)

 :ref:`Guide to the Progress Page` (reference)

 :ref:`Guide to the Grade Report` (reference)

 :ref:`Guide to the Problem Grade Report` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+-------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                               |
+--------------+-------------------------------+----------------+-------------------------------------------------------------+
| 03/12/2025   |Leira (Curricu.me)             | Sumac          |Fail (https://github.com/openedx/docs.openedx.org/issues/902)|
+--------------+-------------------------------+----------------+-------------------------------------------------------------+
