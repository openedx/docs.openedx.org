.. _Partial Credit:

Awarding Partial Credit for a Problem
#####################################

.. tags:: educator, reference

You can configure the following problem types so that learners can receive
partial credit for a problem if they submit a partly correct answer.

* :ref:`Single Select <Awarding Partial Credit in a Multiple Choice Problem>`
* :ref:`Multi-select <Awarding Partial Credit in a Multi select Problem>`
* :ref:`Numerical Input <Awarding Partial Credit in a Numerical Input Problem>`
* :ref:`Custom Python-evaluated Input Problem (Write-Your-Own Grader) <Award Half Credit>`

By awarding partial credit for problems, you can motivate learners who have
mastered some of the course content and provided a score that accurately
demonstrates their progress.

For more information about configuring partial credit, see the topic for each
problem type.


How Learners Receive Partial Credit
************************************

Learners receive partial credit when they submit an answer in the LMS.

In the following example, the course team configured a single select problem
to award 25% of the possible points (instead of 0) for one of the
incorrect answer options. The learner selected this incorrect option and
received 25% of the possible points.

.. image:: /_images/educator_references/partial_credit_multiple_choice.png
 :alt: A single select problem with partial credit for an incorrect
     answer.
 :width: 500



Partial Credit and Reporting on Learner Performance
***************************************************

When a learner receives partial credit for a problem, the LMS only adds the
points earned to the grade. However, the LMS reports any
problem for which a learner receives credit, in full or in part, as correct in
the following ways.

* Events that the system generates when learners receive partial credit for a
  problem indicate that the answer was correct. Specifically, the
  ``correctness`` field has a value of ``correct``.

  For more information about events, see :ref:`problem` in the *EdX Research Guide*.

* The **AnswerValue** in the :ref:`Student_Answer_Distribution` report is
  **1**, for correct.

Course teams can see that a learner received partial credit for a problem in
the learner's submission history. The submission history shows the score that
the learner received out of the total available score and the value in the
``correctness`` field is ``partially-correct``.  For more information, see
:ref:`Student_Answer_Submission`.

.. seealso::

 :ref:`Awarding Partial Credit in a Multiple Choice Problem` (how-to)
 
 :ref:`Awarding Partial Credit in a Multi select Problem` (how-to)

 :ref:`Awarding Partial Credit in a Numerical Input Problem` (how-to)

 :ref:`Award Partial Credit` (how-to)
