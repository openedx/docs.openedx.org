.. _Numerical Input Problem XML:

Numerical Input Problem OLX Reference
#####################################

.. tags:: educator, reference

Templates
*********

The following templates represent problems without, and with, a Python script.

Problem with No Tolerance
=========================

.. code-block:: xml

  <problem>
    <numericalresponse answer="ANSWER (NUMBER)">
      <label>Question text</label>
      <description>Optional tip</description>
      <formulaequationinput />
      <correcthint>Feedback for the correct answer.</correcthint>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>TEXT OF SOLUTION</p>
        </div>
      </solution>
    </numericalresponse>
  </problem>


Answer Created Using a Script
=============================

.. note:: The following example includes a Python script. When you add a
  script to a problem component, make sure that it is not indented. A "jailed
  code" error message appears when you save the problem in Studio if the script
  element is indented.

.. code-block:: xml

  <problem>
    <numericalresponse answer="$computed_response">
      <label>Question text</label>
      <description>Optional tip</description>
      <responseparam type="tolerance" default="0.0001" />
  <script type="loncapa/python">
  computed_response = math.sqrt(math.fsum([math.pow(math.pi,2), math.pow(math.e,2)]))
  </script>
      <formulaequationinput />
      <correcthint>Feedback for the correct answer.</correcthint>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>TEXT OF SOLUTION</p>
        </div>
      </solution>
    </numericalresponse>
  </problem>

Elements
********

For numerical input problems, the ``<problem>`` element can include this
hierarchy of child elements.

.. code-block:: xml

  <numericalresponse>
      <label>
      <description>
      <formulaequationinput>
      <additional_answer>
      <correcthint>
      <responseparam>
      <script>
      <solution>
  <demandhint>
      <hint>

In addition, standard HTML tags can be used to format text.


``<numericalresponse>``
=======================

Required. Indicates that the problem is a numerical input problem.

The ``<numericalresponse>`` element is similar to the ``<formularesponse>``
element used by the :ref:`math expression input<Math Expression Input>` problem
type, but the ``<numericalresponse>`` element does not allow unspecified
variables.


Attributes
----------

.. list-table::
  :widths: 20 80
  :header-rows: 1

  * - Attribute
    - Description
  * - ``answer``
    - Required. The correct answer to the problem, given as a mathematical
      expression.
  * - ``partial_credit``
    - Optional. Specifies the type of partial credit given. ``close``,
      ``list``, or a combination of both in any order separated by a comma (,).

.. note:: If you include a variable name preceded with a dollar sign
 ($) in the problem ``answer``, you can include a script in the problem that
 computes the expression in terms of that variable.

The grader evaluates the answer that you provide and the learner's response
in the same way. The grader also automatically simplifies any numeric
expressions that you or a learner provides. Answers can include simple
expressions such as "0.3" and "42", or more complex expressions such as
"1/3" and "sin(pi/5)".


Children
--------

* ``<label>``
* ``<description>``
* ``<formulaequationinput>``
* ``<additional_answer>``
* ``<responseparam>``
* ``<correcthint>``
* ``<script>``
* ``<solution>``


``<label>``
===========

Required. Identifies the question or prompt. You can include HTML tags within
this element.


Attributes
-----------

None.


Children
--------

None.


``<description>``
=================

Optional. Provides clarifying information about how to answer the question. You
can include HTML tags within this element.


Attributes
----------

None.


Children
---------

None.


``<formulaequationinput>``
==========================

Required. Creates a response field in the LMS where learners enter a response.

.. note::
    Some older problems use a ``<textline math="1" />`` element instead of
    ``<formulaequationinput>``. However, the ``<textline math="1" />``
    element has been deprecated. All new problems should use the
    ``<formulaequationinput>`` element.


Attributes
----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``size``
     - Optional. Defines the width, in characters, of the response field in
       the LMS.
   * - ``trailing_text``
     - Optional. Specified text to appear immediately after the response field.


Children
--------

None.


``<additional_answer>``
=======================

Optional. Specifies an additional correct answer for the problem. A problem can
contain an unlimited number of additional answers.


Attributes
----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``answer``
     - Required. The alternative correct answer.


Children
---------

``correcthint``


``<responseparam>``
===================

Specifies a tolerance, or margin of error, for an answer.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``type``
     - Optional. ``"tolerance"`` defines a tolerance for a number.
   * - ``default``
     - Optional. A number or a percentage specifying a numerical or percent
        tolerance.
   * - ``partial_range``
     - Optional. For partial credit problems of ``type="close"``, a
       multiplier for the tolerance. Default is 2.
   * - ``partial_answers``
     - Optional. For partial credit problems of ``type="list"``, a comma-
         separated list of values that are to receive 50% credit.

Children
--------

None.


``<correcthint>``
=================

Optional. Specifies feedback to appear after the learner submits the correct
answer.


Attributes
----------

.. list-table::
   :widths: 20 80

   * - Attribute
     - Description
   * - ``label``
     - Optional. The text of the custom feedback label.


Children
--------

None.


``<script>``
=============

Optional. Specifies a script that the grader uses to evaluate a learner's
response. A problem behaves as if all of the code in all of the ``<script>``
elements were in a single ``<script>`` element. Specifically, any variables
that are used in multiple ``<script>`` elements share a namespace and can be
overridden.

As with all Python, indentation matters, even though the code is embedded in
XML.


Attributes
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``type``
     - Required. Must be set to ``loncapa/python``.


Children
---------

None.


``<solution>``
===============

Optional. Identifies the explanation or solution for the problem, or for one of
the questions in a problem that contains more than one question.

This element contains an HTML division ``<div>``. The division contains one or
more paragraphs ``<p>`` of explanatory text.


``<demandhint>``
================

Optional. Specifies hints for the learner. For problems that include multiple
questions, the hints apply to the entire problem.


Attributes
----------

None.

Children
---------

``<hint>``


``<hint>``
==========

Required. Specifies additional information that learners can access if needed.


Attributes
-----------

None.


Children
---------

None.

.. seealso::
 :class: dropdown

 :ref:`Numerical Input` (reference)

 :ref:`Adding Numerical Input Problem` (how to)

 :ref:`Editing Numerical Input Problems using the Advanced Editor` (how to)

 :ref:`Awarding Partial Credit in a Numerical Input Problem` (how to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
