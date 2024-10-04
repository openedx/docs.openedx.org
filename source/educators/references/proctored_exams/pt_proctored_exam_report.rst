.. _PT Proctored Session Results File:

********************************************
Interpret the Proctored Exam Results Report
********************************************

The Proctored Exam Results report contains the following fields.

.. list-table::
   :widths: 30 55
   :header-rows: 1

   * - Column
     - Description
   * - course_id
     - The ID of the course.
   * - exam_name
     - The name of the proctored exam in the body of the course.
   * - username
     - The username that identifies the learner taking the proctored exam.
   * - email
     - The email address that identifies the learner taking the proctored exam.
   * - attempt_code
     - An identifier for the exam attempt. The attempt code is an
       internal identifier and is included in the report for use in
       troubleshooting.
   * - allowed_time_limit_mins
     - The amount of time in minutes that this learner was allotted for
       completing the exam.
   * - is_sample_attempt
     - Indicates whether this exam attempt was for a practice exam.
   * - started_at
     - The date and time that the learner started to take the proctored exam.
   * - completed_at
     - The date and time that the learner submitted the proctored exam.
   * - status
     - The current status of the proctoring session as a whole. The proctoring
       session encompasses the time from when the learner chooses to take the
       proctored exam until the proctored exam review is complete. If the
       proctored exam review is complete, the value in the ``review_status``
       column affects the value in this column.

       For possible values in the status column and an explanation of each
       value, see :ref:`Proctoring Results Status Column`.

   * - review_status
     - The current status of the proctoring exam review by
       Proctortrack/the course team. If the proctored exam review is
       complete, the value in this column affects the value in the
       ``status`` column.

       For possible values and an explanation of each value, see
       :ref:`Proctoring Results Review Status Column PT`.

   * - Suspicious Count
     - Number of incidents during the exam that Proctortrack marked as
       "Suspicious".
   * - Suspicious Comments
     - The comments that Proctortrack entered for each "Suspicious"
       incident, separated by semicolons (;).
   * - Rules Violation Count
     - Number of incidents during the exam that Proctortrack marked as
       "Rules Violation".
   * - Rules Violation Comments
     - The comments that Proctortrack entered for each "Rules Violation"
       incident, separated by semicolons (;).

.. _Proctoring Results Status Column:

===============================
Values in the ``status`` Column
===============================

The following table describes the possible values in the ``status`` column.

.. list-table::
   :widths: 30 55
   :header-rows: 1

   * - Value
     - Description
   * - completed
     - The learner has completed the proctored exam.
   * - created
     - The exam attempt record has been created, but the exam has not yet been
       started.
   * - declined
     - The learner declined to take the exam as a proctored exam.
   * - error
     - An error has occurred with the exam.
   * - expired
     - The course end date passed before the learner completed the proctored
       exam.
   * - ready_to_start
     - The exam attempt record has been created. The learner still needs to
       start the exam.
   * - ready_to_submit
     - The learner has completed but not yet submitted the proctored exam.
   * - rejected
     - The proctoring session review has been completed, and the learner has
       not passed the review. The learner receives a value of "Unsatisfactory"
       on the learner exam page and in a notification email message.
       Additionally, the learner automatically receives a score of 0 for the
       exam. For most courses, the learner is no longer eligible for academic
       credit.

       This value results from a value of "Suspicious" in the
       :ref:`review_status<Proctoring Results Review Status Column PT>`
       column after a member of the course team marks the exam session
       a failure in the Proctortrack dashboard.

   * - second_review_required
     - The exam attempt has been reviewed and the review team has determined
       that the exam requires additional evaluation. Course teams
       should perform this second round of review, as described
       :ref:`above<Review PT Proctored Session Results>`

       This status results from a value of "Suspicious" in the
       :ref:`review_status<Proctoring Results Review Status Column PT>` column.

   * - started
     - The learner has started the proctored exam.
   * - submitted
     - The learner has completed the proctored exam and results have been
       submitted for review.
   * - timed_out
     - The proctored exam has timed out.
   * - verified
     - The proctoring session review has been completed, and the learner has
       passed the review. The learner receives a value of "Satisfactory" on the
       learner exam page and in a notification email message.

       This value results from a value of "Clean" or "Rules Violation" in the
       :ref:`review_status<Proctoring Results Review Status Column PT>` column.


.. _Proctoring Results Review Status Column PT:

======================================
Values in the ``review_status`` Column
======================================

After learners complete a proctored exam, a reviewer from the proctoring
service provider reviews the exam according to specific criteria, including the
:ref:`Online Proctoring Rules <CA Online Proctoring Rules>`. The value in the
``review_status`` column shows the outcome of the proctored exam review.

Additionally, the value in the ``review_status`` column affects the following
information for the course team and for the learner.

* The values in the ``status`` column.
* The proctoring result that is visible on the learner exam page and in the
  email notification that the learner receives.

For example, if the ``review_status`` column has a value of "Clean", the value
in the ``status`` column is "verified". On the learner exam page and in the
email notification, the status of the exam is "Satisfactory".

If the ``review_status`` column has a value of "Suspicious", the value
in the ``status`` column is "second_review_required" or "rejected". If
the ``status`` is "rejected", then on the learner exam page and in the email
notification, the status of the exam is "Unsatisfactory".

The following table describes the possible values in the ``review_status``
column.

.. list-table::
   :widths: 30 20 55
   :header-rows: 1

   * - Value
     - Exam Result
     - Description
   * - Clean
     - Pass
     - No rules violations or suspicious incidents occurred. The learner has
       passed the proctoring review.

       This value causes a value of "verified" in the ``status`` column. The
       learner receives a result of "Satisfactory" for the proctored exam.

   * - Not Reviewed
     - n/a
     - The proctoring review is not yet complete.
   * - Rules Violation
     - Pass
     - An incident occurred that violates proctored exam rules, but the
       incident does not compromise exam integrity. For example, music may be
       playing. The learner has passed the proctoring review.

       This value causes a value of "verified" in the ``status`` column. The
       learner receives a result of "Satisfactory" for the proctored exam.

   * - Suspicious
     - Fail
     - An incident has occurred that directly compromises exam integrity. For
       example, cheating might have occurred. The learner has failed the
       proctoring review.

       This value causes a value of "second_review_required" or
       "rejected" in the ``status`` column. The learner receives a
       result of "Unsatisfactory" for the proctored exam in the latter
       case.  The learner also receives a score of 0 on the exam. In
       most courses, the learner is no longer eligible for academic
       credit.

.. seealso::
 :class: dropdown

  :ref:`ProctoredExams_Overview` (concept)
  :ref:`Enable Proctored Exams` (how-to)
  :ref:`Preparing Learners for Proctored Exams` (concept)
  :ref:`Online Proctoring Rules` (reference)
  :ref:`Manage Proctored Exams` (how-to)
  :ref:`Allow Opting Out of Proctored Exams` (how-to)
  :ref:`Create a Proctored Exam with Proctortrack` (how-to)
  :ref:`Review PT Proctored Session Results` (how-to)
  :ref:`Create a Proctored Exam with RPNow` (how-to)
  :ref:`RPNow Proctored Session Results File` (reference)
  :ref:`Review RP Proctored Session Results` (how-to)


