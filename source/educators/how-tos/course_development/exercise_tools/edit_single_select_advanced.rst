.. _Editing Single Select Problems using the Advanced Editor:

Edit Single Select Problems using the Advanced Editor
#####################################################

.. tags:: educator, how-to

If the simple editor is not enough to meet your needs, you can switch over to the
advanced editor. In the setting panels on the right of the editor, click
**Show advanced settings**, then scroll down and click
**Switch to advanced editor**.

You can use the advanced editor to identify the elements of a single select problem
with OLX. For more information, see :ref:`Single Select Problem XML`. To format equations,
you can use MathJax. For more information, see :ref:`MathJax in Studio`.

You can see the OLX for the example problem from the Overview section below.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>Lateral inhibition, as was first discovered in the horseshoe crab:</label>
      <choicegroup type="MultipleChoice">
        <choice correct="false">is a property of touch sensation, referring to
        the ability of crabs to detect nearby predators.</choice>
        <choice correct="false">is a property of hearing, referring to the
        ability of crabs to detect low frequency noises.</choice>
        <choice correct="false">is a property of vision, referring to the
        ability of crabs' eyes to enhance contrasts.</choice>
        <choice correct="true">has to do with the ability of crabs to use
        sonar to detect fellow horseshoe crabs nearby.</choice>
        <choice correct="false">has to do with a weighting system in the
        crab's skeleton that allows it to balance in turbulent water.</choice>
      </choicegroup>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>Horseshoe crabs were essential to the discovery of lateral
          inhibition, a property of vision present in horseshoe crabs as well
          as humans that enables enhancement of contrast at edges of objects
          as was demonstrated in class. In 1967, Haldan Hartline received the
          Nobel prize for his research on vision and in particular his
          research investigating lateral inhibition using horseshoe crabs.</p>
        </div>
      </solution>
    </multiplechoiceresponse>
  </problem>

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any advanced OLX
  changes you make in the advanced editor, you may not be able to cannot
  switch back to the simple editor.

Adding Feedback
***************

In the advanced editor, you configure feedback with the following syntax.

.. code-block:: xml

  <choice correct="false">Choice Label
    <choicehint>Feedback for when learner selects this answer.</choicehint>
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

.. _Targeted Feedback in a Single Select Problem:

Targeted Feedback
=================

You can configure a single select problem so that explanations for specific
answers are automatically shown to learners. You can use these explanations to
guide learners towards the right answer. Therefore, targeted feedback is most
useful for single select problems for which learners are allowed multiple attempts.

You configure the problem to provide targeted feedback by editing the OLX in
the :ref:`advanced editor<Advanced Editor>`.

* Add a ``targeted-feedback`` attribute to the ``<multiplechoiceresponse>``
  element, with no value: ``<multiplechoiceresponse targeted-feedback="">``.

* Add an ``explanation-id`` attribute with a unique value to each of the
  ``<choice>`` elements: ``<choice correct="false"
  explanation-id="feedback1">``.

* You can use the ``<solution>`` element for the correct answer.

* Add a ``<targetedfeedbackset>`` element after the
  ``<multiplechoiceresponse>`` element.

* Within ``<targetedfeedbackset>``, add one or more ``<targetedfeedback>``
  elements.

* Within each ``<targetedfeedback>`` element, add one of the unique identifying
  ``explanation-id`` attributes to map that feedback to a specific answer
  choice.

* Within each ``<targetedfeedback>`` element use HTML formatting, such as
  ``<p></p>`` tags, to enter your explanation for the specified answer option.

For example, the OLX for a single select problem follows, showing a unique ID
for each answer choice. This is immediately followed by OLX that defines the
targeted feedback.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse targeted-feedback="">
      <label>What Apple device competed with the portable CD player?</label>
      <choicegroup type="MultipleChoice">
        <choice correct="false" explanation-id="feedback1">The iPad</choice>
        <choice correct="false" explanation-id="feedback2">Napster</choice>
        <choice correct="true" explanation-id="correct">The iPod</choice>
        <choice correct="false" explanation-id="feedback3">The vegetable peeler</choice>
      </choicegroup>
      <solution explanation-id="correct">
        <div class="detailed-solution">
          <p>The iPod directly competed with portable CD players.</p>
        </div>
      </solution>
    </multiplechoiceresponse>
    <targetedfeedbackset>
      <targetedfeedback explanation-id="feedback1">
        <div class="detailed-targeted-feedback">
          <p>Targeted Feedback</p>
          <p>The iPad came out later and did not directly compete with
           portable CD players.</p>
         </div>
      </targetedfeedback>
      <targetedfeedback explanation-id="feedback2">
        <div class="detailed-targeted-feedback">
          <p>Targeted Feedback</p>
          <p>Napster was not an Apple product.</p>
        </div>
      </targetedfeedback>
      <targetedfeedback explanation-id="feedback3">
        <div class="detailed-targeted-feedback">
          <p>Targeted Feedback</p>
          <p>Vegetable peelers do not play music.</p>
        </div>
      </targetedfeedback>
    </targetedfeedbackset>
  </problem>

Adding Hints
************

You can add hints to a single select problem . For an overview of hints in
problems, see :ref:`Adding Feedback and Hints to a Problem`.

.. seealso::
 :class: dropdown

 :ref:`Single Select Overview` (concept)

 :ref:`Single Select` (how-to)

 :ref:`Single Select Problem XML` (reference)

 :ref:`Awarding Partial Credit in a Multiple Choice Problem` (how-to)
