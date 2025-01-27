.. _Interpret the Grade Report:

########################################
Interpreting the Grade Report
########################################

.. tags:: educator, reference

A grade report for your course is a time-stamped .csv file that identifies each
learner by ID, email address, and username, and provides a snapshot of their
cumulative course scores.

Scores in the grade report are presented by assignment. There is a column for
every assignment that is included in your grading configuration: each
homework, lab, midterm, final, and any other assignment type you added to your
course.

.. note:: The grade report does not include information about individual
   problems within assignments or include learner answer distributions. For a
   report that shows problem-level information, see :ref:`problem_report`.

The report indicates the enrollment track for each learner. For professional
and verified track learners it also shows whether they have verified their
identity. The report shows whether each learner is eligible to receive a
certificate (determined by whether he has earned a passing grade at the time
the report was requested), whether a certificate has been generated, and the
type of certificate earned.

If your course includes :ref:`cohorts<Cohorts Overview>`, :ref:`content
experiments<Overview of Content Experiments>`, or
:ref:`teams<CA_Teams_Overview>`, the grade report includes additional columns
indicating the name of the cohort, experiment group, or team that each learner
belongs to.

.. image:: /_images/educator_references/Grade-Report-with-enroll-status.png
  :alt: A course grade report, opened in Excel, showing the grades achieved by
        learners on several homework assignments and the midterm.

The grade report .csv file contains one row of data for each learner, and
columns that provide the following information.

* Learner identifiers, including an internal **Student ID**, **Email** address,
  and **Username**.

* The overall **Grade**, with the total score a learner has currently attained
  in the course. This value is expressed as a decimal: a learner with a grade
  of 0.65 has earned 65% of the credit in the course, and a learner with a
  grade of 1 has earned 100%.

* Each **{assignment type} {number}** is defined in your grading configuration,
  with the score that the learner attained for that specific assignment. For
  example, column Homework 3 shows the scores for the third homework
  assignment. If the learner did not attempt the assignment, the value is "Not
  Attempted". If the assignment was not available for the learner, the value
  is "Not Available".

* An **{assignment type} (Avg)** with each learner's current average score for
  that assignment type: for example, "Homework (Avg)". This column is not
  included if a particular assignment type has only one assignment.

  This assignment type average takes both dropped assignments and the
  assignment weight into account. For example, if the course includes five
  homework assignments and the course grading policy allows one homework
  assignment with the lowest score to be dropped, the homework assignment
  average in this grade report is calculated over four homework assignments
  rather than five. This average is then multiplied by the assignment weight to
  calculate the assignment type average.

* If :ref:`cohorts<Cohorts Overview>` are used in the course, a **Cohort Name**
  column indicates the name of the cohort that each learner belongs to,
  including the default cohort. The column is empty for learners who are not
  yet assigned to a cohort.

* If :ref:`content experiments<Overview of Content Experiments>` are used in
  the course, an **Experiment Group** column indicates the name of the
  experiment group that each learner belongs to within a group configuration.
  The column heading includes the name of the group configuration. The column
  is empty for learners who are not assigned to an experiment group. If you
  have more than one experiment group configuration in your course, you see one
  column for each group configuration.

* If :ref:`teams<CA_Teams_Overview>` are enabled in the course, a **Team Name**
  column indicates the name of the team that each learner belongs to. The
  column is empty for learners who have not joined a team.

* The **Enrollment Track** column indicates whether each learner is enrolled in
  the course in the honor code, verified, or professional education track.

* The **Verification Status** column indicates whether learners who are
  enrolled in course tracks that require ID verification have successfully
  verified their identities to your instance by submitting an official photo ID via webcam. The value in this column is "N/A" for learners enrolled in course
  tracks that do not require ID verification, such as "Audit".

  A value of "Not ID Verified" in this column indicates that the learner is
  enrolled in a course mode that requires ID verification, such as "Verified",
  but she has not attempted ID verification, or her ID verification has failed
  or expired. A value of "ID Verified" indicates that the learner is enrolled
  in a course mode that requires ID verification, and her ID verification is
  current and valid.

* The **Certificate Eligible** column indicates whether a learner is eligible
  for a certificate for your course.

  The value in this column is "Y" for the following learners.

  * Verified learners who attained a passing grade before this report was
    requested. For example, the learner could have earned a passing grade in an
    earlier session, or run, of the course.

  * All whitelisted learners, regardless of grade or enrollment track.

  The value is "N" for the following learners.

  * Learners who did not attain a passing grade.

  * Learners who are in the audit track.

  * Learners who live in embargoed countries.

* For learners who are eligible to receive a certificate, the **Certificate
  Delivered** column has a value of "Y" when the certificates for a course have
  been generated. The value is "N" for learners who are not eligible to
  receive a certificate.

* The **Certificate Type** column indicates the type of certificate that the
  learner is eligible for, such as "honor" or "verified". If a learner is not
  eligible for a certificate, or if the certificates for a course have not yet
  been generated, the value in this column is "N/A".

* The **Enrollment Status** column indicates whether the learner is currently
  enrolled or unenrolled in the course.

.. seealso::
  

  :ref:`Learner Data` (concept)
  
  :ref:`Interpret the Problem Grade Report` (reference)

  :ref:`Understanding the Progress Page` (reference

  :ref:`Manage Learner Grades <Grades>` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
