.. :diataxis-type: reference

.. _Multi select Problem XML:

***********************************
Multi-select Problem OLX Reference
***********************************

.. note:: You can also set attributes and options by adding a ``<script>`` element.
 For more information, see :ref:`Using the Script Element<Using the Script
 Element in Multi-select Problems>`.

============
Template
============

.. code-block:: xml

  <problem>
    <choiceresponse>
      <label>Question or prompt text</label>
      <description>Information about how to answer the question</description>
      <checkboxgroup>
        <choice correct="false">Answer option A (incorrect)</choice>
        <choice correct="true">Answer option B (correct)</choice>
        <choice correct="true">Answer option C (correct)</choice>
      </checkboxgroup>
    <solution>
      <div class="detailed-solution">
        <p>Optional header for the explanation or solution</p>
        <p>Optional explanation or solution text</p>
      </div>
    </solution>
    </choiceresponse>
    <demandhint>
      <hint>Hint 1</hint>
      <hint>Hint 2</hint>
    </demandhint>
  </problem>

=========
Elements
=========

For multi-select problems, the ``<problem>`` element can include this hierarchy of
child elements.


.. code-block:: xml

  <choiceresponse>
      <label>
      <description>
      <checkboxgroup>
            <choice>
                <choicehint>
            <compoundhint>
      <solution>
  <demandhint>
      <hint>

In addition, standard HTML tags can be used to format text.

--------------------------
``<choiceresponse>``
--------------------------

Required. Indicates that the problem is a multi-select problem.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``partial_credit``
     - Optional. Specifies the type of partial credit given. ``EDC`` or
       ``halves``.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

* ``<label>``
* ``<description>``
* ``<checkboxgroup>``
* ``<solution>``

--------------------------
``<label>``
--------------------------

Required. Identifies the question or prompt. You can include HTML tags within
this element.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

None.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

--------------------------
``<description>``
--------------------------

Optional. Provides clarifying information about how to answer the question. You
can include HTML tags within this element.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

None.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

--------------------------
``<checkboxgroup>``
--------------------------

Required. Indicates the beginning of the list of options.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

None.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

* ``<choice>``
* ``<compoundhint>``

``<choice>``
************

Required. Designates an answer option.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``correct``
     - Indicates a correct or incorrect answer.

       * When set to ``"true"``, the choice is a correct answer. At least one
         required.
       * When set to ``"false"``, the choice is an incorrect answer.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

``<choicehint>``

--------------------------
``<choicehint>``
--------------------------

Optional. Specifies feedback for the answer.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``selected``
     -  Required. ``true`` or ``false``. Indicates if the feedback is given
        when the answer option is selected, or when it is not selected.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

--------------------------
``<compoundhint>``
--------------------------

Optional. Specifies feedback for a specific combination of answers.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``value`` (at least one required)
     - Indicates the combination of selected answers that triggers this
       feedback. Answers are identified by uppercase letters, in ascending
       alphabetical order.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

--------------------------
``<solution>``
--------------------------

Optional. Identifies the explanation or solution for the problem, or for one of
the questions in a problem that contains more than one question.

This element contains an HTML division ``<div>``. The division contains one or
more paragraphs ``<p>`` of explanatory text.

--------------------------
``<demandhint>``
--------------------------

Optional. Specifies hints for the learner. For problems that include multiple
questions, the hints apply to the entire problem.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

None.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

``<hint>``

--------------------------
``<hint>``
--------------------------

Required. Specifies additional information that learners can access if needed.

^^^^^^^^^^^^^^^^^^^^
Attributes
^^^^^^^^^^^^^^^^^^^^

None.

^^^^^^^^^^^^^^^^^^^^
Children
^^^^^^^^^^^^^^^^^^^^

None.

.. _Using the Script Element in Multi-select Problems:

========================
Using the Script Element
========================

You can use the ``<script>`` element to programmatically set attributes and
options for your multi-select problems.  You could use this feature to display
different questions/answers depending on variable factors, like time of day, or
randomly generated numbers.

-------------------------------------------------------
Use the Advanced Editor to Configure the Script Element
-------------------------------------------------------

You must use the :ref:`advanced editor<Advanced Editor>` to configure a
``<script>`` element.

The contents of the ``<script>`` element must be enclosed in ``<![CDATA[`` ...
``]]>`` markers, to indicate that the enclosed code should not be interpreted
as XML.

The code in the ``<script>`` element is run on the server before the problem is
shown to learners.  Note that only Python script types are supported.

The following OLX example uses random numbers to generate different answer
choices for each learner, and mathematical operators to determine each choice's
correctness.

.. code-block:: xml

    <problem>
      <script type="text/python">
      <![CDATA[
      random.seed(anonymous_student_id)  # Use different random numbers for each student.
      a = random.randint(1,10)
      b = random.randint(1,10)
      c = a + b

      ok0 = c % 2 == 0 # check remainder modulo 2
      text0 = "$a + $b is divisible by 2"

      ok1 = c % 3 == 0 # check remainder modulo 3
      text1 = "$a + $b is divisible by 3"

      ok2 = c % 5 == 0 # check remainder modulo 5
      text2 = "$a + $b is divisible by 5"

      ok3 = not any([ok0, ok1, ok2])
      text3 = "None of the above statements is true."
      ]]>
      </script>
      <choiceresponse>
        <label>Which statements about the number $a+$b are true? Select all that apply.</label>
        <checkboxgroup direction="vertical">
          <choice correct="$ok0">$text0 ... (should be $ok0)</choice>
          <choice correct="$ok1">$text1 ... (should be $ok1)</choice>
          <choice correct="$ok2">$text2 ... (should be $ok2)</choice>
          <choice correct="$ok3">$text3 ... (should be $ok3)</choice>
        </checkboxgroup>
      </choiceresponse>
    </problem>

.. note:: After saving a block with scripts, you'll see an error on the block in your
  unit if your script cannot be executed. One common error is the indentation error.
  The script must start on no indentation regardless of the indentation of the previous
  line.

.. seealso::
 :class: dropdown

  :ref:`Multi select` (reference)
  :ref:`Adding a Multi Select Problem` (how to)
  :ref:`Adding Feedback and Hints to a Problem` (how to)
  :ref:`Awarding Partial Credit in a Multi select Problem` (how to)