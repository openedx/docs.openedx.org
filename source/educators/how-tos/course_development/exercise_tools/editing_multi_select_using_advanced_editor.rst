.. _Editing Multi select Problems using the Advanced Editor:

Editing Multi-select Problems using the Advanced Editor
#######################################################

If the simple editor is not enough to meet your needs, you can switch over to the
advanced editor. In the setting panels on the right of the editor, click
**Show advanced settings**, then scroll down and click
**Switch to advanced editor**.

You can use the advanced editor to identify the elements of a multi-select problem
with OLX. For more information, see :ref:`Multi-select Problem XML`. To format equations,
you can use MathJax. For more information, see :ref:`MathJax in Studio`.

You can see the OLX for the example problem from the Overview section below.

.. code-block:: xml

  <problem>
    <choiceresponse>
      <label>Learning about the benefits of preventative health care can be
      particularly difficult.</label>
      <description>Check all of the options below that might be reasons why.</description>
      <checkboxgroup>
        <choice correct="true">A large amount of time passes between
         undertaking a preventative measure and seeing the result.</choice>
        <choice correct="false">Non-immunized people will always fall sick.</choice>
        <choice correct="true">If others are immunized, fewer people will fall
         sick regardless of a particular individual's choice to get immunized
         or not.</choice>
        <choice correct="true">Trust in health care professionals and
         government officials is fragile.</choice>
      </checkboxgroup>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>People who are not immunized against a disease might still not
           fall sick from the disease. If someone is trying to learn whether
           or not preventative measures against the disease have any impact,
           he or she might see these people and conclude, since they have
           remained healthy despite not being immunized, that immunizations
           have no effect. Consequently, he or she would tend to believe that
           immunization (or other preventative measures) have fewer benefits
           than they actually do.</p>
        </div>
      </solution>
    </choiceresponse>
  </problem>

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any advanced OLX
  changes you make in the advanced editor, you may not be able to cannot
  switch back to the simple editor.

Adding Feedback
***************

There are several types of feedback you can add for a multi-select problem
and different ways to configure them:

.. contents::
  :local:
  :depth: 1

Adding Feedback for Individual Answers
======================================

In the advanced editor, you configure feedback with the following syntax.

.. code-block:: xml

  <choice correct="true">Choice label
    <choicehint selected="true">Feedback for when learner selects this
      answer.</choicehint>
    <choicehint selected="false">Feedback for when learner does not select
      this answer.</choicehint>
  </choice>

For example, the following problem has feedback for each answer.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>Which of the following is an example of a vegetable?</label>
      <description>You can select only one option.</description>
      <choicegroup type="MultipleChoice">
        <choice correct="false">apple
          <choicehint>An apple is the fertilized ovary that comes from an apple
          tree and contains seeds classifying it as a fruit.</choicehint>
        </choice>
        <choice correct="false">pumpkin
          <choicehint>A pumpkin is the fertilized ovary of a squash plant
          and contains seeds classifying it as a fruit.</choicehint>
        </choice>
        <choice correct="true">potato
          <choicehint>A potato is an edible part of a plant in tuber form and
          is classified as a vegetable.</choicehint>
        </choice>
        <choice correct="false">tomato
          <choicehint>Many people mistakenly think a tomato is a vegetable.
          However, because a tomato is the fertilized ovary of a tomato plant
          and contains seeds it is classified as a fruit.</choicehint>
        </choice>
      </choicegroup>
    </multiplechoiceresponse>
  </problem>

Adding Group Feedback
=====================

In the advanced editor, you define group feedback by adding a ``<compoundhint>``
element within the ``<checkboxgroup>`` element.

.. code-block:: xml

          .
          .
          .
        </choice>
        <compoundhint value="Answer Combination">Feedback when learner selects
         this combination of answers.</compoundhint>
      </checkboxgroup>

For example, the following group feedback is used when learners select
options **A, B, and D** or **A, B, C, and D**.

.. code-block:: xml

          .
          .
          .
        </choice>
        <compoundhint value="A B D">An apple, pumpkin, and tomato are all
         fruits as they all are fertilized ovaries of a plant and contain
         seeds.</compoundhint>
        <compoundhint value="A B C D">You are correct that an apple, pumpkin,
         and tomato are all fruits as they all are fertilized ovaries of a
         plant and contain seeds. However, a potato is not a fruit as it is an
         edible part of a plant in tuber form and is classified as a vegetable.
        </compoundhint>
      </checkboxgroup>

Adding Hints
============

See :ref:`Adding Feedback and Hints to a Problem` for more information on adding hints to a problem.

.. seealso::
 :class: dropdown

 :ref:`Multi select` (reference)

 :ref:`Adding a Checkbox Problem` (how-to)

 :ref:`Adding a Multi Select Problem` (how-to)

 :ref:`Adding Feedback and Hints to a Problem` (how-to)

 :ref:`Multi select Problem XML` (reference)

 :ref:`Awarding Partial Credit in a Multi select Problem` (how-to)
