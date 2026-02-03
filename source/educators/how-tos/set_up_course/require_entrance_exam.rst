.. _Require an Entrance Exam:

########################
Require an Entrance Exam
########################

.. tags:: educator, how-to

.. admonition:: Turn on the Entrance Exam feature

   In order for the Entrance Exam feature to work, it must be enabled on your Open edX instance. It is not enabled by default.

   Please contact your site administrator to enable the `FEATURES['ENTRANCE_EXAMS'] <https://docs.openedx.org/projects/edx-platform/en/latest/references/featuretoggles.html#featuretoggle-FEATURES['ENTRANCE_EXAMS']>`_ flag.

To require an entrance exam, follow these steps.

#. In Studio, open your course.
#. On the **Settings** menu, select **Schedule & Details**.
#. On the **Schedule & Details** page, locate the **Requirements** section.
#. Select the **Require students to pass an exam before accessing course
   materials** option.

   .. image:: /_images/educator_how_tos/require_entrance_exam.png
      :alt: The "Require students to pass an exam before accessing course materials" checkbox appears at the bottom of the "Requirements" section.

#. In the **Grade Requirements** section, set the percentage score required to
   pass the exam (default is 50%).
#. Select **Save Changes**.

After changes are saved, Studio automatically creates an **Entrance Exam**
section in the course outline. To add content to the entrance exam, go to the
course outline.

***********************
Create an Entrance Exam
***********************

Adding as Entrance Exam automatically places a new section called "Entrance
Exam" at the top of the course outline.

.. image:: /_images/educator_how_tos/entrance_exam_in_outline.png
   :alt: The "Entrance Exam" appears as a section at the top of the course outline, above all other course sections


Creating entrance exam content is just like creating other course content. For
more information, see the section on :ref:`Content Creation and Management <Content Creation and Management TOC>`.

**********************************
Adjust Scores in the Entrance Exam
**********************************

If the exam is changed or corrected after learners take the exam, there are
several options to rescore the exam for individual learners. These options are
available on the instructor dashboard.

In the LMS, select **Instructor** to access the instructor dashboard, and then
select **Student Admin**. In the **Entrance Exam Grade Adjustment** section,
the following options are available.

.. image:: /_images/educator_how_tos/entrance_exam_inst_dash.png
   :alt: The Entrance Exam Grade Adjust section of the Instructor Dashboard

* **Attempts**: Reset the value for one particular learner's
  attempts back to zero so that the learner can begin work over again. For more
  information, see :ref:`reset_attempts`.

* **Allow Skip**: Waive the requirement for the learner to take the exam.

* **Rescore**: Rescore any responses that have been submitted. The 'Rescore All
  Problems Only If Score Improves' option updates the learner's scores only if
  it improves in the learner's favor. For more information, see :ref:`rescore`.

* **Delete Learner's State**: Delete a learner's entire history for the exam
  from the database. For more information, see :ref:`delete_state`.

Another option on the instructor dashboard is **Task Status**. If one of the
above options are selected, the operation runs in the background. If you want to
see a record of all the operations that have run for the entrance exam, select
**Show Task Status**.

.. seealso::

  :ref:`Set Course Prerequisites` (reference)

  :ref:`Require a Prerequisite Course` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                 |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| 2025-11-16   | sarina                        |  Ulmo          | Pass                                                          |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| 03/11/2025   | Leira (Curricu.me)            | Sumac          | Fail (https://github.com/openedx/docs.openedx.org/issues/891) |
|              |                               |                | (this simply hasn't been tested with the flag on)             |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
