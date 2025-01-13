.. _Review PT Proctored Session Results:

View Proctored Session Results with Proctortrack
################################################

.. tags:: educator, how-to

To review individual violation videos and screenshots, follow these steps:

#. In the LMS, open the Proctortrack Review Dashboard by navigating to the **Instructor Dashboard**
   > **Special Exams** tab > **Review Dashboard**.

#. The Verificient **Proctortrack Review Dashboard** will load inline in the LMS.

#. Navigate to the **Quiz List** tab and locate the exam you want to review.

#. Click on **View Sessions** to open the list of learners who took the exam

#. Review all learners who are flagged as “Require Attention” as follows.

#. To review an individual learner's session, click on the learner's name to pop out
   their detailed exam results in a new tab. Here you can review their exam data, including Video
   Monitoring, Online Violations, Verification scans, and Onboarding tabs to understand what infractions
   (if any) were flagged as suspicious

#. If the suspicious behavior is deemed to be in violation of proctoring rules of your course,
   select **Fail** to fail the learner and set their grade to 0. Learners will get an email informing them that they did not pass proctoring review, and their grade was set to 0.

#. If needed, you can later revert this decision by clicking **Pass** to pass the learner and
   restore their original exam grade.

#. If needed, you can download the violation screenshot and data by clicking the **Export Data arrow**.

To see a summary of proctored exam results, you use the Proctored Exam Results
report. This report is a .csv file that you can download from the instructor
dashboard. You can use this report to view proctoring results for all learners,
or :ref:`determine whether a specific learner has passed the proctoring
review<Determine if Learner Passed Proctoring Review>`.

.. note::
 The Proctored Exam Results report contains information about the proctoring
 review. The report does not include information about the learner's score on
 the exam. A learner might pass the proctoring review but not earn a high
 enough score to pass the exam itself.

For more information about the Proctored Exam Results report, see the following
sections.

.. contents::
  :local:
  :depth: 1

.. _Viewing PT Proctored Session Results:

Download the Proctored Exam Results Report
******************************************

At any time after learners have taken the proctored exam in your course, you
can download a .csv file that displays the current status of the proctoring
session for participating learners.

To generate and download the Proctored Exam Results report, follow these
steps.

.. important::
   This report contains confidential, personally identifiable data. Be sure to
   follow your institution's data stewardship policies when you open or save
   this report.

#. View the live version of your course.

#. In the LMS, select **Instructor**, then select **Data Download**.

#. In the **Reports** section, select **Generate Proctored Exam Results
   Report**.

   A status message indicates that the report generation process is in
   progress. This process can take some time to complete. You can navigate away
   from this page while the process runs.

#. To check the progress of the report generation, reload the page in your
   browser and scroll to the **Pending Tasks** section. The table shows the
   status of active tasks.

   When the report is complete, a linked .csv file name becomes available in
   the **Reports Available for Download** section. The most recently generated
   reports appear at the top of the list.

   File names are in the following format.

   ``{course_id}_proctored_exam_results_report_{datetime}.csv``

#. To download a report file, select the link for the report you requested.
   The .csv file begins downloading automatically.

.. note::
   To prevent the accidental distribution of learner data, you can download
   exam result report files only by clicking the links on this page. These
   links expire after 5 minutes. If necessary, refresh the page to generate new
   links.

#. When the download is complete, open the .csv files in a spreadsheet
   application to sort, graph, and compare data.

.. _Determine if Learner Passed Proctoring Review:

Determine if a Learner Passed the Proctored Exam Review
*******************************************************

To determine whether a specific learner passed the proctored exam review, you
can either view the Proctored Session Results report or view the course as the
learner.

View the Proctored Session Results Report
=========================================

#. Download and open the Proctored Session Results report.
#. In the row for the learner, check the ``status`` column.

   * If the value in the column is "verified", the learner passed the review.
   * If the value is "rejected", the learner did not pass the review. The
     learner automatically receives a score of 0 on the exam. Additionally, for
     most courses, the learner is no longer eligible for academic credit.

View the Course as the Learner
==============================

#. :ref:`View the course as the learner that you want<Roles for Viewing Course
   Content>`.
#. Open the page for the proctored exam.

On the page, the learner's status is visible as "Pending", "Satisfactory", or
"Unsatisfactory".

.. seealso::
 :class: dropdown

 :ref:`ProctoredExams_Overview` (concept)

 :ref:`Enable Proctored Exams` (how-to)

 :ref:`Preparing Learners for Proctored Exams` (concept)

 :ref:`Online Proctoring Rules` (reference)

 :ref:`Manage Proctored Exams` (how-to)

 :ref:`Allow Opting Out of Proctored Exams` (how-to)

 :ref:`Create a Proctored Exam with Proctortrack` (how-to)

 :ref:`PT Proctored Session Results File` (reference)

 :ref:`Create a Proctored Exam with RPNow` (how-to)

 :ref:`RPNow Proctored Session Results File` (reference)

 :ref:`Review RP Proctored Session Results` (how-to)
