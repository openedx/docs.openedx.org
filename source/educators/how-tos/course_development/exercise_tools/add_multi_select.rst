.. _Add a Multi Select Problem:

Add a Multi-select (Checkbox) Problem
######################################

.. tags:: educator, how-to

.. youtube:: 6VYKcMeZrxg

.. START ADD MULTIPLE CHOICE PROBLEM

You add multi-select problems in Studio by selecting the **Problem** component.
In the problem editor, select **the Multi-select** option. Fill in the fields
on this screen to create your problem.

.. image:: /_images/educator_how_tos/problem_editor_multi_select.png
 :alt: An example multi-select problem in the problem editor with number
    indicators labeling the various features.
 :width: 800

Creating a multi-select problem is as simple as:

#. Editing the **Display Name**. Click the pen icon to edit.
#. Filling in the **Question** field.
#. Filling in the **Explanation** field. When this is shown to learners is
   based on the selection in the **Show answer** panel on the right.
#. Filling in the **Answer** fields. Select the correct answer(s) by ticking
   off the checkbox(es). Additional answers can be added by clicking the
   **Add answer** button. Answers can be deleted by clicking the trash can
   icon. Feedback can be provided for each answer. More information on feedback
   can be found in the following section.
#. Selecting and filling in any desired settings on the right.

.. END ADD MULTIPLE CHOICE PROBLEM

If you have any questions on the specifics of using the simple editor, please check
out :ref:`Simple Editor` and :ref:`Guide to Problem Settings`.

.. _Adding Feedback for Multi select Problems:

Adding Feedback
***************

For an overview of feedback in problems, see :ref:`Adding Feedback and Hints to
a Problem`. For multi-select problems, you can add feedback for each of the answer
options you provide in the problem. You can also identify different
combinations of answer options that learners are likely to select, and add
group feedback for those combinations.

Adding Feedback for Individual Answers
======================================

In multi-select problems, you can provide feedback for each answer that a learner
can select, with distinct feedback depending on whether or not the learner
selects that answer. This means that there are several possible types of
feedback.

* The learner selects a correct answer. This type of feedback
  should indicate why the answer is correct.

* The learner does not select a correct answer. This type of feedback should
  indicate that the learner missed checking this answer and why it is correct.

* The learner selects an incorrect answer. This type of feedback should
  indicate that the learner incorrectly checked this answer and why it is
  incorrect.

* The learner does not select an incorrect answer. This type of feedback should
  reinforce why the learner correctly left this answer unselected.

You can access the feedback panel shown below by clicking the button to the
right of the answer text.

.. image:: /_images/educator_how_tos/problem_editor_multi_feedback_box.png
 :alt: An example of an expanded feedback section for multi-select problems showing
    the 'is selected' and 'is not selected' feedback fields.
 :width: 600

Adding Group Feedback
=====================

You can configure the multi-select problem to provide group feedback.
Group feedback is feedback given for a specific combination of answers. For
example, if you have three possible answers in the problem, you can define
specific feedback for when a learner selects each combination of possible
options.

* A
* B
* C
* A, B
* B, C
* A, C
* A, B, C

For problems with more than three answers, providing specific feedback for each
combination can become difficult. For such problems, you might choose to define
group feedback for more likely combinations of answers or for combinations of
answers that reflect common learner misunderstandings. If you do not define
feedback for a combination that a learner selects, the learner receives
feedback for the individual selections.

Group feedback can be entered in the Group Feedback panel on the right of the
editor. The example below shows feedback for combinations of (A, B), (B, C)
and (A, C) respectively.

.. image:: /_images/educator_how_tos/problem_editor_group_feedback_example.png
 :alt: An example of group feedback.
 :width: 200

.. note:: If you configure individual option feedback for every answer, and
  you also provide group feedback, when learners select the exact
  combination of answer choices defined, they only see the compound feedback.
  In this example, learners who select apple (A), pumpkin (B), and tomato (D)
  see the message "An apple, pumpkin, and tomato are all fruits as they are all
  the fertilized ovaries of a plant and contain seeds." They do not also see
  the individual feedback for selecting A, B, and D, and for leaving C
  unselected.

.. _Use Hints in a Multi select Problem:

Adding Hints
============

You can add hints to a multi-select problem. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. seealso::
 

 :ref:`Multi select` (reference)

 :ref:`Edit Multi select Problems using the Advanced Editor` (how-to)

 :ref:`Adding Feedback and Hints to a Problem` (how-to)

 :ref:`Multi select Problem XML` (reference)

 :ref:`Awarding Partial Credit in a Multi select Problem` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
