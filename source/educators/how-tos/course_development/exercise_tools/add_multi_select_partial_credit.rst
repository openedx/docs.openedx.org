.. _Awarding Partial Credit in a Multi select Problem:

Awarding Partial Credit
#######################

.. tags:: educator, how-to

You can configure a multi-select problem to award partial credit to learners
who submit an answer that is partly correct.

For an overview of partial credit in problems, see :ref:`Partial Credit`.

In the following example, the learner selected two of the three correct
choices, and did not select any incorrect choices. The learner therefore had
four out of five correct answers. Because the course team set this problem up
to award partial credit for every correct answer selected and every incorrect
answer left unselected (known as :ref:`every decision counts`), the learner earned
80% of the points for this problem.

.. image:: /_images/educator_how_tos/checkbox_partial_credit.png
 :alt: A checkbox choice problem with partial credit for two out of
     three answers.
 :width: 600

You can use the following methods to award partial credit in a multi-select
problem.

.. contents::
  :local:
  :depth: 1

.. _Every Decision Counts:

Using the Every Decision Counts Method
**************************************

You can configure a multi-select problem so that every selection a learner makes for
the multi-select problem is evaluated and scored. This method is known as every
decision counts (EDC).

With EDC, if "n" is the number of possible answers, learners earn 1/n of the
total possible score for each correct answer they select. Learners receive
partial credit for every correct answer selected and every incorrect answer left
unselected.

For example, if there are four answers, every answer that a learner matches is
worth 25% of the total score. A learner also gains 25% for each incorrect answer
that a learner does NOT select.

The following table shows how the different combinations of learner selections
would score for one EDC problem whose answers are as follows.

* Correct answers: A, B, D
* Incorrect answers: C

.. list-table::
     :widths: 20 20 20
     :header-rows: 1

     * - Learner's Selections
       - Score
       - Explanation
     * - A, B, D
       - 100%
       - The learner matched each of the 3 correct answers for 75%, and also
         gained 25% for not selecting the incorrect answer.
     * - A, B
       - 75%
       - The learner matched 2 of the correct answers for 50%, and also gained
         25% for not selecting the incorrect answer.
     * - A, B, C
       - 50%
       - The learner matched 2 of the correct answers for 50%, but selected the
         incorrect answer.
     * - A, C
       - 25%
       - The learner matched 1 of the correct answers for 25%, but selected the
         incorrect answer.

Configure an EDC Multi-select Problem
=====================================

To configure an EDC multi-select problem, you add the ``partial_credit="EDC"``
attribute to the ``<choiceresponse>`` element in the problem OLX.

For example, the following OLX shows the multi-select problem template after it is
updated to provide partial credit.

.. code-block:: xml

  <problem>
    <choiceresponse partial_credit="EDC">
      <label>Which of the following is a fruit?</label>
      <description>Select all that apply.</description>
      <checkboxgroup>
        <choice correct="true">apple</choice>
        <choice correct="true">pumpkin</choice>
        <choice correct="false">potato</choice>
        <choice correct="true">tomato</choice>
      </checkboxgroup>
    </choiceresponse>
  </problem>

Using the By Halves Method
**************************

You can configure a multi-select problem so that for every answer that a learner
gets wrong, either by not selecting a correct answer or by selecting an
incorrect answer, half of the remaining points are deducted from the learner's
score. This method is known as scoring by halves.

.. note:: By design, partial credit by halves requires the number of answer
   options to be more than twice the number of incorrect answers. In addition,
   partial credit is not given for more than two wrong answers, regardless of
   the total number of answer options. In other words, two wrong answers is
   scored at 25% only if there are at least 5 answer options. Three or more
   wrong answers is always scored at 0%, regardless of the number of total
   answer options.

Partial credit using the by halves method is calculated as follows.

* If a learner makes no errors, she receives full credit for the problem.

* If a learner makes one error, she receives 50% of the possible points, as
  long as there are three or more choices in the problem. If a learner makes
  one error and there are only two choices in the problem, no credit is given.

* If a learner makes two errors, she receives 25% of the possible points, as
  long as there are five or more choices in the problem. If a learner makes two
  errors and there are only three choices or four choices in the problem, no
  credit is given.

* If a learner makes three errors, she receives no credit for the problem,
  regardless of how many answer options there are.

The following tables illustrate partial credit score using the halves method,
for problems with an increasing number of total answer options.

.. list-table::
     :widths: 30 30 30
     :header-rows: 1

     * - Number of Incorrect Answers
       - Number of Answer Options
       - Credit Given (%)
     * - 0
       - 2
       - 100
     * - 1
       - 2
       - 0
     * - 2
       - 2
       - 0

.. list-table::
     :widths: 30 30 30
     :header-rows: 1

     * - Number of Incorrect Answers
       - Number of Answer Options
       - Credit Given (%)
     * - 0
       - 3
       - 100
     * - 1
       - 3
       - 0
     * - 2
       - 3
       - 0
     * - 3
       - 3
       - 0

.. list-table::
     :widths: 30 30 30
     :header-rows: 1

     * - Number of Incorrect Answers
       - Number of Answer Options
       - Credit Given (%)
     * - 0
       - 4
       - 100
     * - 1
       - 4
       - 50
     * - 2
       - 4
       - 0
     * - 3
       - 4
       - 0
     * - 4
       - 4
       - 0

.. list-table::
     :widths: 30 30 30
     :header-rows: 1

     * - Number of Incorrect Answers
       - Number of Answer Options
       - Credit Given (%)
     * - 0
       - 5
       - 100
     * - 1
       - 5
       - 50
     * - 2
       - 5
       - 25
     * - 3
       - 5
       - 0
     * - 4
       - 5
       - 0
     * - 5
       - 5
       - 0

.. list-table::
     :widths: 30 30 30
     :header-rows: 1

     * - Number of Incorrect Answers
       - Number of Answer Options
       - Credit Given (%)
     * - 0
       - 7
       - 100
     * - 1
       - 7
       - 50
     * - 2
       - 7
       - 25
     * - 3
       - 7
       - 0
     * - 4
       - 7
       - 0
     * - 5
       - 7
       - 0

Configure a By Halves Multi-select Problem
==========================================

To configure a by halves multi-select problem, you add the
``partial_credit="halves"`` attribute to the ``<choiceresponse>`` element in
the problem OLX.

The following example shows a multi-select problem that provides partial credit by
halves.

.. code-block:: xml

  <problem>
    <choiceresponse partial_credit="halves">
      <label>Which of the following is a fruit?</label>
      <description>Select all that apply.</description>
      <checkboxgroup>
        <choice correct="true">apple</choice>
        <choice correct="true">pumpkin</choice>
        <choice correct="false">potato</choice>
        <choice correct="true">tomato</choice>
      </checkboxgroup>
    </choiceresponse>
  </problem>


.. seealso::
 :class: dropdown

 :ref:`Multi select` (reference)

 :ref:`Add a Multi Select Problem` (how-to)

 :ref:`Adding Feedback and Hints to a Problem` (how-to)

 :ref:`Multi select Problem XML` (reference)
