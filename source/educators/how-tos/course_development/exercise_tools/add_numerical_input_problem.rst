.. :diataxis-type: how-to
.. _Adding Numerical Input Problem: 

***********************************
Adding a Numerical Input Problem
***********************************

.. youtube:: fkoF8ZDPMoQ

You add numerical input problems in Studio by selecting the **Problem**
component. In the problem editor, select the **Numerical Input** option. Fill in
the fields on this screen to create your problem.

.. image:: /_images/educator_how_tos/problem_editor_numerical_input.png
 :alt: An example numerical input problem in the problem editor with number
    indicators labeling the various features.
 :width: 800

Creating a numerical input problem is as simple as:

#. Editing the **Display Name**. Click the pen symbol to edit.
#. Filling in the **Question** field.
#. Filling in the **Explanation** field. When this is shown to learners is
   based on the selection in the **Show answer** panel on the right.
#. Filling in the **Answer** fields. For numerical input problems, only correct
   answers can be added here. Additional answers can be added by clicking the
   **Add answer** button. Answers can be deleted by clicking the trash can icon.
   Feedback can be provided for each answer. More information on feedback can be
   found in the following section.
#. Selecting and filling in any desired settings on the right.

.. note:: Only correct answers can be added to a numerical input problem.

If you have any questions on the specifics of using the simple editor, please check
out :ref:`Simple Editor` and :ref:`Problem Settings`.

============================================================
Adding a Tolerance or a Range
============================================================

To give learners the option to receive full credit for a close approximation of
the correct answer, and to support a wide range of possible correct numerical
answers, you can specify a tolerance for the correct answer or a range of values
to mark as correct for the numerical input problem type.

.. contents::
  :local:
  :depth: 1

.. note:: You can either have a **tolerance** or an **answer range** for a
  numerical input problem. You cannot add both.

-------------------
Adding a Tolerance
-------------------

You can specify a margin of error or tolerance for learner responses. You
can specify a percentage or number. The tolerance settings panel can be
found to the right of the editor.

.. image:: /_images/educator_how_tos/problem_editor_tolerance_box.png
 :alt: An example tolerance setting set to 5%.
 :width: 200

--------------------------------------
Specifying an Answer Range
--------------------------------------

You can specify an answer range so that any learner response within that range
is marked correct.

Add an answer range by selecting the **Add answer range** button from the
**Add answer** dropdown. This option can only be selected if you only have one
answer. This will replace your answer field with an answer range field.

.. image:: /_images/educator_how_tos/problem_editor_answer_range_box.png
 :alt: An example answer range set from 1 to 10. This includes 1 but not 10.
 :width: 200

To format an answer range, you provide the starting and
ending values and then separate them with a comma character (``,``). You then
surround the range with bracket (``[ ]``) or parentheses characters (``( )``),
or a combination of one bracket and one parenthesis.

* Use a bracket to include the number next to it in the range, as in a less
  than or equal to, or greater than or equal to, inequality.

* Use a parenthesis to exclude the number from the range, as in a less than or
  greater than inequality.

For example, to identify the correct answers as 5, 6, or 7, but not 8, specify
``[5,8)``. To identify the correct answers as 6, 7, and 8, but not 5, specify
``(5,8]``.
.. :diataxis-type: how-to
.. _Use Feedback in a Numerical Input Problems:

=================
Adding Feedback
=================

For an overview of feedback in problems, see :ref:`Adding Feedback and Hints to
a Problem`. In numerical input problems, you can provide feedback for correct
responses. If you define multiple correct responses, you can define feedback
for each response. In numerical input problems, use feedback to reinforce the
process used to arrive at the correct answer.

You can add answer-specific feedback for each answer in a numerical input problem.
You can access the feedback panel shown below by clicking the button to the right
of the answer text.

.. image:: /_images/educator_how_tos/problem_editor_feedback_box_2.png
 :alt: An example of an expanded feedback section for dropdown problems showing
    the 'is selected' feedback field.
 :width: 600

Simply enter your feedback message in this text field. It will display when the
learner submits this answer.

.. note:: You cannot add feedback for an incorrect answer in numerical input
  problems. Add hints to guide the learners in the correct direction instead.

.. _Use Hints in a Numerical Input Problem:

=================
Adding Hints
=================

You can add hints to a numerical input problem using the simple editor or the
advanced editor. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. seealso::
 :class: dropdown

 :ref:`Numerical Input` (reference)

 :ref:`Use Feedback in a Numerical Input Problems` (how to)

 :ref:`Numerical Input Problem XML` (reference)

 :ref:`Awarding Partial Credit in a Numerical Input Problem` (how to)