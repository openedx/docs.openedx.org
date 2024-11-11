.. _Editing Text Input Problems using the Advanced Editor:

*********************************************************************
Editing Text Input Problems using the Advanced Editor
*********************************************************************

.. tags:: educator, how-to

If the simple editor is not enough to meet your needs, you can switch over to the
advanced editor. In the setting panels on the right of the editor, click
**Show advanced settings**, then scroll down and click
**Switch to advanced editor**.

You can use the advanced editor to identify the elements of a text input problem
with OLX. For more information, see :ref:`Text Input Problem XML`. To format
equations, you can use MathJax. For more information, see :ref:`MathJax in Studio`.

You can see the OLX for the example problem from the Overview section below.

.. code-block:: xml

  <problem>
  <stringresponse answer="Nanjing University" type="ci">
    <label>What was the first post-secondary school in China to allow both
     male and female students?</label>
    <description>Answer with a name from the modern period.</description>
    <additional_answer answer="National Central University"/>
    <additional_answer answer="Nanjing Higher Normal Institute"/>
    <additional_answer answer="Nanking University"/>
    <textline size="20"/>
    <solution>
      <div class="detailed-solution">
        <p>Explanation</p>
        <p>Nanjing University first admitted female students in 1920.</p>
      </div>
    </solution>
  </stringresponse>
  </problem>

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any advanced OLX
  changes you make in the advanced editor, you may not be able to cannot
  switch back to the simple editor.

=============================
Adding Feedback
=============================

In the advanced editor, you configure answer feedback with the following syntax.

.. code-block:: xml

  <problem>
    <stringresponse answer="Correct Answer" type="ci">
      <label>Question text</label>
      <correcthint>Feedback for the correct answer</correcthint>
      <stringequalhint answer="Incorrect Answer">Hint for the incorrect answer</stringequalhint>
      <textline size="20"/>
    </stringresponse>
  </problem>

For example, the following problem has feedback for the correct answer and two
common incorrect answers.

.. code-block:: xml

  <problem>
    <stringresponse answer="Alaska" type="ci">
      <label>What is the largest state in the U.S. in terms of land area?</label>
      <correcthint>Alaska is the largest state in the U.S. in terms of not
      only land area, but also total area and water area. Alaska is 576,400
      square miles, more than double the land area of the second largest
      state, Texas.</correcthint>
      <stringequalhint answer="Texas">While many people think Texas is the
      largest state in terms of land area, it is actually the second
      largest and contains 261,797 square miles.</stringequalhint>
      <stringequalhint answer="California">California is the third largest
      state and contains 155,959 square miles.</stringequalhint>
      <textline size="20"/>
    </stringresponse>
  </problem>


=============================
Adding Hints
=============================

For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

==========================================================
Adding Text after the Response Field
==========================================================

You might want to include a word, phrase, or sentence after the response field
in a text input problem to help guide your learners or resolve ambiguity.

.. image:: /_images/educator_how_tos/MC_trailing_text.png
 :alt: Text input problem with the word "Institute" after the response
    field.
 :width: 500

To do this, you use the advanced editor.

In the problem, locate the ``textline`` element. This element creates the
response field for the problem and is a child of the ``stringresponse``
element.

To add text after the response field, add the ``trailing_text`` attribute
together with the text that you want to use inside the ``textline`` element.  An example follows.

.. code-block:: xml

  <problem>
    <stringresponse answer="Ashmun" type="ci">
      <label>What Pennsylvania school was founded in 1854 to provide
        educational opportunities for African-Americans?</label>
      <textline size="20" trailing_text="Institute"/>
    </stringresponse>
  </problem>

==========================================================
Case Sensitivity and Text Input Problems
==========================================================

By default, text input problems do not require a case sensitive response. You
can change this default to require a case sensitive answer.

To make a text input response case sensitive, you use the advanced editor.

In the advanced editor, the ``stringresponse`` element has a ``type``
attribute. By default, the value for this attribute is set to ``ci``, for "case
insensitive". An example follows.

.. code-block:: xml

    <problem>
      <stringresponse answer="Paris" type="ci">
      .
      .
      .
      </stringresponse>
    </problem>

Learners who submit an answer of either "Paris" or "paris" are scored
as correct.

To make the response case sensitive, change the value of the ``type``
attribute to ``cs``.

.. code-block:: xml

    <problem>
      <stringresponse answer="Paris" type="cs">
      .
      .
      .
      </stringresponse>
    </problem>

Learners who submit an answer of "Paris" are scored as correct, but
learners who submit an answer of "PARIS" are scored as incorrect.

==========================================================
Response Field Length in Text Input Problems
==========================================================

You should preview the unit to ensure that the length of the response input
field accommodates the correct answer, and provides extra space for possible
incorrect answers.

If the default response field is not long enough, you can change it
using the advanced editor.

In the advanced editor, the ``textline`` element has a ``size`` attribute. By
default, the value for this attribute is set to ``20``. An example follows.

.. code-block:: xml

    <problem>
      <stringresponse answer="Democratic Republic of the Congo" type="ci">
        .
        .
        .
        <textline size="20"/>
      </stringresponse>
    </problem>

To change the response field length, change the value of the ``size``
attribute.

.. code-block:: xml

    <problem>
      <stringresponse answer="Democratic Republic of the Congo" type="ci">
        .
        .
        .
        <textline size="40" />
      </stringresponse>
    </problem>

===============================================================
Allowing Regular Expressions as Answers for Text Input Problems
===============================================================

You can configure a text input problem to allow a regular expression as an
answer. Allowing learners to answer with a regular expression can minimize the
number of distinct correct responses that you need to define for the problem:
if a learner responds with the correct answer formed as a plural instead of a
singular noun, or a verb in the past tense instead of the present tense, the
answer is marked as correct.

To do this, you use the advanced editor.

In the advanced editor, the ``stringresponse`` element has a ``type``
attribute. You can set the value for this attribute to ``regexp``, with or
without also including ``ci`` or ``cs`` for a case insensitive or case
sensitive answer. An example follows.

.. code-block:: xml

    <problem>
      <stringresponse answer="string pattern" type="regexp ci">
        .
        .
        .
      </stringresponse>
    </problem>

The regular expression that the learner enters must contain, in whole or in
part, the answer that you specify.

In this example, learners who submit an answer of "string pattern", "String
Patterns", "string patterned", or "STRING PATTERNING" are all scored as
correct, but learners who submit an answer of "Strings Pattern" or "string
patern" are scored as incorrect.

=========================
Disable MathJax rendering
=========================

You can configure a text input problem to accept raw expressions which could
resemble functions that are processed by MathJax by default. Sometimes this
might not be the expected behaviour, i.e., you want to accept raw expression as
well as display (show answer) it in its raw form. You can do this by simply
enclosing ``<stringresponse>`` element in ``<annotation-xml>`` tag. All elements
inside this tag will be ignored by MathJax processor. An example follows.

.. code-block:: xml

   <problem>
     <annotation-xml>
       <stringresponse class="tex2jax_ignore" answer="\s*n\s**?\s*x\[\s*n\s*\]\s*" type="ci">
         <div>Question</div>
         <additional_answer class="tex2jax_ignore" answer="or \s*x\[\s*n\s*\]\s**?\s*n\s*"></additional_answer>
         <textline size="20"></textline>
       </stringresponse>
     </annotation-xml>
   </problem>

.. seealso::
 :class: dropdown

 :ref:`Text Input` (reference)

 :ref:`Add Text Input Problem` (how to)

 :ref:`Text Input Problem XML` (reference)