.. _Text Input Problem XML:

Text Input Problem XML Reference
#################################

.. tags:: educator, reference

Template
*********

.. code-block:: xml

  <problem>
    <stringresponse answer="Correct answer 1" type="ci regexp">
      <label>Question text</label>
      <description>Optional tip</description>
      <correcthint>Provides feedback when learners submit the correct
       response.</correcthint>
      <additional_answer answer="Correct answer 2"/>
      <additional_answer answer="Correct answer 3"/>
      <stringequalhint answer="Incorrect answer 1">Provides feedback when
       learners submit the specified incorrect response.</stringequalhint>
      <stringequalhint answer="Incorrect answer 2">Provides feedback when
       learners submit the specified incorrect response.</stringequalhint>
      <textline size="20" />
    </stringresponse>
    <demandhint>
      <hint>The first text string to display when learners request a hint.</hint>
      <hint>The second text string to display when learners request a hint.</hint>
    </demandhint>
  </problem>


Elements
*********

For text input problems, the ``<problem>`` element can include this
hierarchy of child elements.

.. code-block:: xml

  <stringresponse>
      <label>
      <description>
      <additional_answer>
      <correcthint>
      <stringequalhint>
      <textline>
      <solution>
  <demandhint>
      <hint>

In addition, standard HTML tags can be used to format text.


``<stringresponse>``
=====================

Required. Indicates that the problem is a text input problem.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``answer`` (required)
     - Specifies the correct answer.

       Note that if you do not also add the ``type`` attribute and set it to
       ``regexp``, the learner's answer must match the value for this
       attribute exactly.

   * - ``type`` (optional)
     - Specifies whether the problem requires a case sensitive response and
       if it allows regular expressions.

       * If ``type="ci"``, the problem is not case sensitive.
       * If ``type="cs"``, the problem is case sensitive.
       * If ``type="regexp"``, the problem allows regular expressions.

       You can also combine these values in a space separated list. For
       example, ``<stringresponse type="regexp cs">`` specifies that the
       problem allows regular expressions and is case sensitive.


Children
---------

* ``<label>``
* ``<description>``
* ``<textline>``
* ``<additional_answer>``
* ``<correcthint>``
* ``<stringequalhint>``
* ``<solution>``


``<label>``
=============

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


``<textline>``
===============

Required. Creates a response field in the LMS where the learner enters a text
string.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``size``
     - Optional. Specifies the size, in characters, of the response field in
       the LMS. Defaults to 20.
   * - ``hidden``
     - Optional. If set to "true", learners cannot see the response field.
   * - ``correct_answer``
     - Optional. Lists the correct answer to the problem.
   * - ``trailing_text``
     - Optional. Specifies text to appear immediately after the response field.

.. reviewers, note that I could not get "correct_answer" to work ^^. The answer attribute of stringresponse is required and overrides whatever I put in here. Can this attribute be removed or marked as deprecated? - Alison 10 Aug


Children
---------

None.


``<additional_answer>``
========================

Optional. Specifies an additional correct answer for the problem. A problem can
contain an unlimited number of additional answers.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``answer``
     - Required. The text of the alternative correct answer.


Children
---------

``<correcthint>``


``<correcthint>``
===================

Optional. Specifies feedback to appear after the learner submits a correct
answer.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``label``
     - Optional. The text of the custom feedback label.


Children
---------

None.


``<stringequalhint>``
======================

Optional. Specifies feedback to appear after the learner submits an incorrect
answer.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``answer``
     - Required. The text of the incorrect answer.
   * - ``label``
     - Optional. The text of the custom feedback label.


Children
-----------

None.


``<solution>``
===============

Optional. Identifies the explanation or solution for the problem, or for one of
the questions in a problem that contains more than one question.

This element contains an HTML division ``<div>``. The division contains one or
more paragraphs ``<p>`` of explanatory text.


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
============

Required. Specifies additional information that learners can access if needed.


Attributes
-----------

None.


Children
---------

None.

.. seealso::
 

 :ref:`Text Input` (reference)

 :ref:`Add Text Input Problem` (how to)

 :ref:`Editing Text Input Problems using the Advanced Editor` (how to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
