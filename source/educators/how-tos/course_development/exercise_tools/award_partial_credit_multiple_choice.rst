.. :diataxis-type: how-to
.. _Awarding Partial Credit in a Multiple Choice Problem:

=======================
Awarding Partial Credit
=======================

You can configure a single select problem so that specific incorrect answers
award learners partial credit for the problem.


In the following example, the learner selected a wrong answer and received
partial credit.

.. image:: /_images/educator_how_tos/partial_credit_multiple_choice.png
 :alt: A single select problem with partial credit for an incorrect answer.
 :width: 400

You can specify what percentage of the points for the problem a learner
receives for an incorrect answer. If you do not specify the percentage, the
system uses the default of 50%.

For an overview of partial credit in problems, see :ref:`Partial Credit`.

To configure a single select problem to award partial credit for a specific
answer, you add the following attributes to the problem OLX.

* Add the ``partial_credit="points"`` attribute to the
  ``<multiplechoiceresponse>`` element.

* For each answer that you intend to award partial credit, in the ``<choice>``
  element set the value of the ``correct`` attribute to ``"partial"``.

* Optionally, define the percentage of the problem score to award for each
  answer. Add the ``point_value`` attribute to the ``<choice>`` element, and
  enter its value as a decimal. For example, add ``point_value="0.25"`` to
  award 25% of the points to learners who select that answer. The percentage
  awarded should reflect how close the learner has gotten to a full
  understanding of the concept. If you do not add the ``point_value``
  attribute, the system uses the default of 50%.

For example, the following OLX shows a single select problem that
provides partial credit of 25% for an answer option.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse partial_credit="points">
      <label>Which of the following is a vegetable?</label>
      <choicegroup type="MultipleChoice">
        .
        .
        .
        <choice correct="partial" point_value="0.25">tomato </choice>
      </choicegroup>
    </multiplechoiceresponse>
  </problem>

.. _Shuffle Answers in a Single Select Problem:

===============
Shuffle Answers
===============

Optionally, you can configure a single select problem so that it shuffles
the order of possible answers.

For example, one view of a problem could be as follows.

.. image:: /_images/educator_how_tos/problem_editor_shuffle_answer_1.png
 :alt: One view of a shuffled single select problem.
 :width: 600

Another view of the same problem, for a different learner or for the same
learner on a subsequent view of the unit, could be as follows.

.. image:: /_images/educator_how_tos/problem_editor_shuffle_answer_2.png
 :alt: Another view of a shuffled single select problem.
 :width: 600

You can also shuffle some answers, but not others. For example, you might
want to include the answer "All of the above" and have it always appear at the
end of the list, but shuffle the other answers.

You can configure the problem to shuffle answers using the advanced editor.
To add shuffling to a single select problem, you add ``shuffle="true"`` to the
``<choicegroup>`` element.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>What Apple device competed with the portable CD player?</label>
      <choicegroup type="MultipleChoice" shuffle="true">
        <choice correct="false">The iPad</choice>
        <choice correct="false">Napster</choice>
        <choice correct="true">The iPod</choice>
        <choice correct="false">The vegetable peeler</choice>
      </choicegroup>
    </multiplechoiceresponse>
  </problem>

To make the location of an answer fixed in a shuffled list, add
``fixed="true"`` to the ``choice`` element for the answer.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>What Apple device competed with the portable CD player?</label>
      <choicegroup type="MultipleChoice" shuffle="true">
        .
        .
        .
        <choice correct="false" fixed="true">All of the above</choice>
      </choicegroup>
    </multiplechoiceresponse>
  </problem>

Then, you select **Settings** to specify an option other than **Never** for the
**Randomization** setting.

.. _Answer Pools in a Single Select Problem:

============
Answer Pools
============

You can configure a single select problem so that a random subset of choices
are shown to each learner. For example, you can add 10 possible choices to the
problem, and each learner views a set of five choices.

The answer pool must have at least one correct answer. It can have more than
one correct answer. In each set of choices shown to a learner, one correct
answer is included. For example, you can configure two correct answers in the
set of choices. One of the two correct answers is included in each set that a
learner views.

You configure the problem to provide answer pools by editing the OLX for the
problem in the :ref:`advanced editor<Advanced Editor>`.

* In the ``<choicegroup>`` element, add the ``answer-pool`` attribute, with the
  numerical value indicating the number of answer options to show to learners.
  For example, ``<choicegroup answer-pool="4">``.

* If you include more than one correct answer among the options, for each
  correct answer add an ``explanation-id`` attribute with a unique value to the
  ``<choice>`` element: ``<choice correct="false" explanation-id="correct1">``.

* If you include more than one correct answer among the options, for each
  ``<solution>`` element, add an ``explanation-id`` attribute and a value that
  maps back to a specific correct answer. For example, ``<solution
  explanation-id="correct1">``.

* Place the ``<solution>`` elements within a ``<solutionset>`` element.

.. note:: If the choices include only one correct answer, you do not have to
 use the ``explanation-id`` in either the ``<choice>`` or ``<solution>``
 element. You do still use the ``<solutionset>`` element to wrap the
 ``<solution>`` element.

For example, for the following single select problem, a learner will see
four choices. In each set, one of the choices will be one of the two correct
choices. The explanation shown for the correct answer is the one with the same
explanation ID.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>What Apple devices let you carry your digital music library in your pocket?</label>
      <description>You can select only one option.</description>
      <choicegroup type="MultipleChoice" answer-pool="4">
        <choice correct="false">The iPad</choice>
        <choice correct="false">Napster</choice>
        <choice correct="true" explanation-id="iPod">The iPod</choice>
        <choice correct="false">The vegetable peeler</choice>
        <choice correct="false">The iMac</choice>
        <choice correct="true" explanation-id="iPhone">The iPhone</choice>
      </choicegroup>
      <solutionset>
        <solution explanation-id="iPod">
          <div class="detailed-solution">
            <p>Explanation</p>
            <p>The iPod is Apple's portable digital music player.</p>
          </div>
        </solution>
        <solution explanation-id="iPhone">
          <div class="detailed-solution">
            <p>Explanation</p>
            <p>In addition to being a cell phone, the iPhone can store and play
             your digital music.</p>
          </div>
        </solution>
      </solutionset>
    </multiplechoiceresponse>
  </problem>

.. seealso::
 :class: dropdown

  :ref:`Single Select Overview` (concept)
  :ref:`Single Select` (how to)
  :ref:`Single Select Problem XML` (reference)
  :ref:`Editing Single Select Problems using the Advanced Editor` (how to)