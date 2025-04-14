.. _Modifying a Released Problem:

Modifying a Released Problem
#############################

.. tags:: educator, reference

.. warning::
 Be careful when you modify problems after they have been
 released. Changes that you make to published problems can affect the learner
 experience in the course and analysis of course data.

After a learner submits a response to a problem, the LMS stores that response,
the score that the learner received, and the maximum score for the problem. For
problems with a **Maximum Attempts** setting greater than 1, the LMS updates
these values each time the learner submits a new response to a problem.
However, if you change a problem or its attributes, existing learner
information for that problem is not automatically updated.

For example, you release a problem and specify that its answer is 3.
After some learners have submitted responses, you notice that the answer
should be 2 instead of 3. When you update the problem with the correct
answer, the LMS does not update scores for learners who originally answered
2 for the problem and received the wrong score.

For another example, you change the number of response fields to
three. Learners who submitted answers before the change have a score of
0, 1, or 2 out of 2.0 for that problem. Learners who submitted answers
after the change have scores of 0, 1, 2, or 3 out of 3.0 for the same
problem.

If you change the points setting for the problem in Studio, however, existing
scores update when the learner's **Progress** page is refreshed. In a live
section, learners will see the effect of these changes.


Workarounds
************

If you have to modify a released problem in a way that affects grading, you
have two options to ensure that every learner has the opportunity
to submit a new response and be regraded. Note that both options require you to
ask your learners to go back and resubmit answers to a problem.

*  In the problem component that you changed, increase the number of attempts
   for the problem, and then ask all of your learners to redo the problem.

*  Delete the entire problem component in Studio and replace it with a new
   problem component that has the content and settings that you want. Then ask
   all of your learners to complete the new problem. (If the revisions you must
   make are minor, you might want to duplicate the problem component before you
   delete it, and then revise the copy.)

For information about how to review and adjust learner grades in the LMS, see
:ref:`Adjust_grades`.

.. seealso::
 
   :ref:`About Problems Exercises and Tools` (concept)

   :ref:`Core Problem Types` (reference)

   :ref:`Working with Problem Components` (reference)

   :ref:`Guide to Problem Settings` (reference)

   :ref:`Gradebook Assignment Types` (reference)

   :ref:`Feedback Best Practices` (concept)

   :ref:`Adding Feedback and Hints to a Problem` (reference)

   :ref:`Configure Hint` (how-to)

   :ref:`Partial Credit` (reference)

   :ref:`Set the Assignment Type and Due Date for a Subsection` (how-to)

   :ref:`Adding Tooltips` (reference)

   :ref:`Learner View of Problems` (reference)

   :ref:`Advanced Editor` (reference)

   :ref:`Add Hints via the Advanced Editor` (how-to)

   :ref:`Add Unsupported Exercises Problems` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
