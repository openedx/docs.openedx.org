.. :diataxis-type: how-to
.. _Use Feedback in a Dropdown Problem:

===============
Adding Feedback
===============

For an overview of feedback in problems, see :ref:`Adding Feedback and Hints to
a Problem`. You can add feedback for each of the answer options you provide in
the problem. Use the following guidelines when providing feedback.

* Use feedback for the incorrect answers to target common misconceptions and
  mistakes.

* Ensure feedback provides some guidance to the learner about how to arrive at
  the correct answer.

* Use feedback for the correct answer to reinforce why the answer is correct.
  Because learners are able to guess, ensure that feedback provides a reason
  why the answer is correct for learners who might have selected that answer by
  chance.

.. image:: /_images/educator_how_tos/problem_editor_feedback_box_2.png
 :alt: An example of an expanded feedback section for dropdown problems showing
    the 'is selected' feedback field.
 :width: 600

===============
Adding Feedback
===============

In the advanced editor, you configure feedback with the following syntax.

.. code-block:: xml

  <option correct="False">Option Label
    <optionhint>Feedback for when a learner selects this incorrect answer.</optionhint>
  </option>

For example, the following problem has feedback for each answer.

.. code-block:: xml

  <problem>
    <optionresponse>
      <label>A/an ________ is an example of a vegetable.</label>
      <optioninput>
        <option correct="False">apple
          <optionhint>An apple is the fertilized ovary that comes from an
          apple tree and contains seeds classifying it as a fruit.</optionhint>
        </option>
        <option correct="False">pumpkin
          <optionhint>A pumpkin is the fertilized ovary of a squash plant and
          contains seeds classifying it as a fruit.</optionhint>
        </option>
        <option correct="True">potato
          <optionhint>A potato is an edible part of a plant in tuber form and
          is classified as a vegetable.</optionhint>
        </option>
        <option correct="False">tomato
          <optionhint>Many people mistakenly think a tomato is a vegetable.
          However, because a tomato is the fertilized ovary of a tomato plant
          and contains seeds it is classified as a fruit.</optionhint>
        </option>
      </optioninput>
    </optionresponse>
  </problem>

-----------------------------
Customizing Feedback Labels
-----------------------------

By default, the feedback labels shown to learners are **Correct** and
**Incorrect**. If you do not define feedback labels, learners see these terms
when they submit an answer, as in the following example.

::

  Incorrect: A pumpkin is the fertilized ovary of a squash plant and contains
  seeds classifying it as a fruit.

You can configure the problem to override the default labels. For example, you
can configure a custom label for a specific wrong answer.

::

  Not Quite: Many people mistakenly think a tomato is a vegetable. However,
  because a tomato is the fertilized ovary of a tomato plant and contains seeds
  it is classified as a fruit.

In the :ref:`advanced editor<Advanced Editor>`, you configure custom feedback
labels with the following syntax.

.. code-block:: xml

  <choice correct="true or false">Answer
    <choicehint label="Custom Label">Feedback for learners who select this
    answer.</choicehint>
  </choice>

For example, the feedback for the following answer option is configured to use
a custom label.

.. code-block:: xml

  <choice correct="false">tomato
    <choicehint label="Not Quite">Many people mistakenly think a tomato is a
    vegetable. However, because a tomato is the fertilized ovary of a tomato
    plant and contains seeds, it is a fruit.</choicehint>
  </choice>

.. note::
  The default labels **Correct** and **Incorrect** display in the learner's
  requested language. If you provide custom labels, they display as you define
  them to all learners. They are not translated into different languages.

.. seealso::
 :class: dropdown

  :ref:`Dropdown` (reference)
  :ref:`Dropdown Problem XML` (reference)
  :ref:`Adding Dropdown` (how to)
  :ref:`Use Hints in a Dropdown Problem` (how to)


