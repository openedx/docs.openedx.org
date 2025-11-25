.. _Partial Credit:

Awarding Partial Credit for a Problem
#####################################

.. tags:: educator, reference

.. START PARTIAL CREDIT

.. warning::

  Partial credit is only available in multipart problems, which can currently
  only be authored directly in OLX. Multipart problems cannot be authored in
  Studio. See :ref:`Multipart Components OLX`.
  
  Studio and LMS support of partial credit is not guaranteed to work.

You can configure the following problem types so that learners can receive
partial credit for a problem if they submit a partially correct answer.

* :ref:`Single Select <Awarding Partial Credit in a Multiple Choice Problem>`
* :ref:`Multi-select <Awarding Partial Credit in a Multi select Problem>`
* :ref:`Numerical Input <Award Partial Credit in a Numerical Input Problem>`
* :ref:`Custom Python-evaluated Input Problem (Write-Your-Own Grader) <Award Half Credit>`

By awarding partial credit for problems, you can motivate learners who have
mastered some of the course content and provided a score that accurately
demonstrates their progress.

For more information about configuring partial credit, see the topic for each
problem type.

************************************
How Learners Receive Partial Credit
************************************

Learners receive partial credit when they submit an answer in the LMS.

The LMS will distribute the total number of points available for the problem
evenly across all problems. So in the following screenshot, with a two-part
problem worth 2 points, if a learner answers one part correctly and the second
incorrectly, they will be awarded 1/2 points.

.. image:: /_images/educator_references/partial_credit_multiple_choice.png
 :alt: A multipart problem with partial credit for an incorrect
     answer.
 :width: 500


***************************************************
Partial Credit and Reporting on Learner Performance
***************************************************

When a learner receives partial credit for a problem, the LMS only adds the
points earned to the grade. However, the LMS reports any
problem for which a learner receives credit, in full or in part, as correct in
the following ways.

* Events that the system generates when learners receive partial credit for a
  problem indicate that the answer was correct. Specifically, the
  ``correctness`` field has a value of ``correct``.

  For more information about events, see :ref:`problem`.

* The **AnswerValue** in the :ref:`Student_Answer_Distribution` report is
  **1**, for correct.

Course teams can see that a learner received partial credit for a problem in
the learner's submission history. The submission history shows the score that
the learner received out of the total available score and the value in the
``correctness`` field is ``partially-correct``.  For more information, see
:ref:`Student_Answer_Submission`.

.. END PARTIAL CREDIT

.. seealso::

  :ref:`About Problems Exercises and Tools` (concept)

  :ref:`Core Problem Types` (reference)

  :ref:`Working with Problem Components` (reference)

  :ref:`Guide to Problem Settings` (reference)

  :ref:`Gradebook Assignment Types` (reference)

  :ref:`Feedback Best Practices` (concept)

  :ref:`Adding Feedback and Hints to a Problem` (reference)

  :ref:`Configure Hint` (how-to)

  :ref:`Set the Assignment Type and Due Date for a Subsection` (how-to)

  :ref:`Adding Tooltips` (reference)

  :ref:`Learner View of Problems` (reference)

  :ref:`Advanced Editor` (reference)

  :ref:`Add Hints via the Advanced Editor` (how-to)

  :ref:`Modifying a Released Problem` (reference)

  :ref:`Add Unsupported Exercises Problems` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
