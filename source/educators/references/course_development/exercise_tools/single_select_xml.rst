.. _Single Select Problem XML:

Single Select Problem OLX Reference
####################################

.. tags:: educator, reference

.. note:: You can also set attributes and options by adding a ``<script>`` element.
 For more information, see :ref:`Using the Script Element<Using the Script
 Element in Single Select Problems>`.

Template
*********

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
      <label>Question or prompt text</label>
      <description>Optional information about how to answer the question</description>
      <choicegroup type="MultipleChoice">
        <choice correct="false" name="a">Incorrect choice
          <choicehint>Hint for incorrect choice.</choicehint>
        </choice>
        <choice correct="true" name="b">Correct choice
          <choicehint>Hint for correct choice.</choicehint>
        </choice>
      </choicegroup>
      <solution>
        <div class="detailed-solution">
          <p>Optional header for the explanation or solution</p>
          <p>Optional explanation or solution text</p>
        </div>
      </solution>
    </multiplechoiceresponse>
  <demandhint>
    <hint>Hint 1</hint>
    <hint>Hint 2</hint>
  </demandhint>
  </problem>


Elements
*********

For single select problems, the ``<problem>`` element can include this
hierarchy of child elements.

.. code-block:: xml

  <multiplechoiceresponse>
      <label>
      <description>
      <choicegroup>
            <choice>
                <choicehint>
      <solution>
  <demandhint>
      <hint>

In addition, standard HTML tags can be used to format text.


``<multiplechoiceresponse>``
============================

Required. Indicates that the problem is a single select problem.


Attributes
----------

  .. list-table::
    :widths: 20 80
    :header-rows: 1

    * - Attribute
      - Description
    * - ``partial_credit``
      - Optional. Specifies that the problem can award partial credit. If used,
        must be set to ``"points"``.
    * - ``targeted-feedback``
      - Optional. Set to targeted-feedback="" if using targeted feedback.
        Otherwise, do not add this attribute.


Children
---------

* ``<label>``
* ``<description>``
* ``<choicegroup>``
* ``<solution>``


``<label>``
============

Required. Identifies the question or prompt. You can include HTML tags within
this element.


Attributes
-----------

None.


Children
---------

None.


``<description>``
===================

Optional. Provides clarifying information about how to answer the question. You
can include HTML tags within this element.


Attributes
-----------

None.


Children
---------

None.


``<choicegroup>``
==================

Required. Indicates the beginning of the list of answer options.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``type``
     - Required. Must be set to ``"MultipleChoice"``.
   * - ``shuffle``
     - Optional. See :ref:`Shuffle Answers in a Single Select Problem`.
       When set to ``"true"``, answers are shuffled.
   * - ``answer-pool``
     - Optional. See :ref:`Answer Pools in a Single Select Problem`.
       Set a numerical value to indicate the number of answers to show to learners.


Children
---------

``<choice>``


``<choice>``
=============

Required. Lists an answer option.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``correct``
     - Indicates a correct, incorrect, or partially
       correct answer.

       * When set to ``"true"``, the choice is a correct answer. At least one
         required.
       * When set to ``"false"``, the choice is an incorrect answer.
       * When set to ``"partial"``, the learner receives partial credit for
         selecting the answer.

       You can specify more than one correct or partially correct answer,
       but learners can select only one choice to submit as their answer.
   * - ``point_value``
     - When ``correct="partial"``, indicates the percentage, as a decimal, of
       the points the learner receives for selecting this option. If
       ``point_value`` is not specified for a partial credit answer, 50% is
       used by default.
   * - ``name``
     - A unique name that is used internally to refer to the choice.
   * - ``fixed``
     - Optional. See :ref:`Shuffle Answers in a Single Select Problem`.
       When set to ``"true"`` while ``shuffle="true"`` in the ``<choicegroup>``
       element, this answer will not shuffle.
   * - ``explanation-id``
     - Optional. See :ref:`Targeted Feedback in a Single Select Problem`.
       Links this answer to the corresponding ``explanation-id`` of a
       ``<solution>`` or ``<targetedfeedback>`` element. For example,
       ``<choice correct="false" explanation-id="feedback1">`` links to
       ``<targetedfeedback explanation-id="feedback1">``.


Children
---------

``<choicehint>``


``<choicehint>``
=================

Optional. Specifies feedback for the answer.


Attributes
-----------

None.


Children
--------

None.


``<solution>``
===============

Optional. Identifies the explanation or solution for the problem, or for one of
the questions in a problem that includes multiple questions.

This element contains an HTML division ``<div>``. The division contains one or
more paragraphs ``<p>`` of explanatory text.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``explanation-id``
     - Optional. See :ref:`Targeted Feedback in a Single Select Problem`.
       Links this answer to the corresponding ``<choice>`` element. For example,
       ``<solution explanation-id="correct">`` links to
       ``<choice correct="true" explanation-id="correct">``.


``<demandhint>``
=================

Optional. Specifies hints for the learner. For problems that include multiple
questions, the hints apply to the entire problem.


Attributes
-----------

None.


Children
---------

``<hint>``


``<hint>``
===========

Required. Specifies additional information that learners can access if needed.


Children
---------

None.


``<targetedfeedbackset>``
==========================

Optional. Groups a set of targeted feedbacks that assist learners. See
:ref:`Targeted Feedback in a Single Select Problem`.


Attributes
-----------

None.


Children
---------

``<targetedfeedback>``


``<targetedfeedback>``
=======================

Optional. Specifies targeted feedback shown automatically to learners. This element
contains an HTML division ``<div>``. The division contains one or more paragraphs
``<p>`` of explanatory text. See :ref:`Targeted Feedback in a Single Select Problem`.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``explanation-id``
     - Optional. See :ref:`Targeted Feedback in a Single Select Problem`.
       Links this answer to the corresponding ``<choice>`` element. For example,
       ``<targetedfeedback explanation-id="feedback1">`` links to
       ``<choice correct="false" explanation-id="feedback1">``.


``<solutionset>``
==================

Optional. Groups a set of explanations that assist learners. See
:ref:`Answer Pools in a Single Select Problem`.


Attributes
-----------

None.


Children
---------

``<solution>``


``<solution>``
===============

Optional. Specifies the explanation shown to learners for a given answer. This
element contains an HTML division ``<div>``. The division contains one or more
paragraphs ``<p>`` of explanatory text. See
:ref:`Answer Pools in a Single Select Problem`.

Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``explanation-id``
     - Optional. See :ref:`Answer Pools in a Single Select Problem`.
       Links this answer to the corresponding ``<choice>`` element. For example,
       ``<solution explanation-id="solution1">`` links to
       ``<choice correct="false" explanation-id="solution1">``.

.. _Using the Script Element in Single Select Problems:

Using the Script Element
*************************

You can use the ``<script>`` element to programmatically set attributes and
options for your single select problems.  You could use this feature to
display different questions/answers depending on variable factors, like time of
day, or randomly generated numbers.

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
        text0 = "$a + $b is even"

        ok1 = c % 2 == 1 #check remainder modulo 2
        text1 = "$a + $b is odd"
        ]]>
        </script>
        <multiplechoiceresponse>
          <label>Is $a+$b even or odd? Select the true statement.</label>
          <choicegroup type="MultipleChoice">
            <choice correct="$ok0">$text0 ... (should be $ok0)</choice>
            <choice correct="$ok1">$text1 ... (should be $ok1)</choice>
          </choicegroup>
        </multiplechoiceresponse>
    </problem>

.. note:: After saving a block with scripts, you'll see an error on the block in your
  unit if your script cannot be executed. One common error is the indentation error.
  The script must start on no indentation regardless of the indentation of the previous
  line.

.. seealso::
 

 :ref:`About Single Select` (concept)

 :ref:`Single Select` (how to)

 :ref:`Awarding Partial Credit in a Multiple Choice Problem` (how to)

 :ref:`Editing Single Select Problems using the Advanced Editor` (how to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
