.. _Math Expression Input Problem XML:

Math Expression Input Problem OLX Reference
###########################################

.. tags:: educator, reference


Template
********

.. note:: The following template includes a Python script. When you add a
  script to a problem component, do not add to or change its internal
  indentation. A "jailed code" error message appears when you save
  the problem in Studio if the ``<script>`` element is indented.

.. code-block:: xml

  <problem>
    <formularesponse type="ci" samples="R_1,R_2,R_3@1,2,3:3,4,5#10"  answer="$computed_response">
      <label>Problem text</label>
      <responseparam type="tolerance" default="0.00001"/>
      <formulaequationinput size="20" />

  <script type="loncapa/python">
  computed_response = PYTHON SCRIPT
  </script>

      <solution>
        <div class="detailed-solution">
          <p>Explanation or solution header</p>
          <p>Explanation or solution text</p>
        </div>
      </solution>
    </formularesponse>
  </problem>

This template includes a placeholder value for the ``samples`` attribute of
``samples="R_1,R_2,R_3@1,2,3:3,4,5#10"``. You enter values for this attribute
in the following format:
``samples="VARIABLES@LOWER_BOUNDS:UPPER_BOUNDS#NUMBER_OF_SAMPLES"``. Additional detail follows in the description of the ``<formularesponse>``
element.


Elements
********

For math expression input problems, the ``<problem>`` element can include this
hierarchy of child elements.

.. code-block:: xml

  <problem>
      <formularesponse>
          <label>
          <description>
          <formulaequationinput>
          <responseparam>
          <script>
          <solution>

In addition, standard HTML tags can be used to format text.

``<formularesponse>``
=====================

Required. Indicates that the problem is a math expression input problem.

The ``<formularesponse>`` tag is similar to the ``<numericalresponse>`` tag
used  by :ref:`numerical input<Numerical Input>` problem types, but
``<formularesponse>`` allows unknown variables.

Attributes
----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``type``
     - Can be ``"cs"`` for case sensitive, which is the default, or ``"ci"``
       for case insensitive, so that capitalization does not matter in variable
       names.
   * - ``answer``
     - The correct answer to the problem, given as a mathematical expression.

       If you precede a variable name in the problem with a dollar sign ($),
       you can include a script in the problem that computes the expression
       in terms of that variable.

   * - ``samples``
     - Specifies important information about the problem in the following
       lists.

       * ``variables``: A set of variables that learners can enter.
       * ``lower_bounds``: For every defined variable, a lower bound on the
         numerical tests to use for that variable.
       * ``upper_bounds``: For every defined variable, an upper bound on the
         numerical tests to use for that variable.
       * ``num_samples``: The number of times to test the expression.

       Commas separate items inside each of the four individual lists. The at
       sign (@), colon (:), and hash tag (#) characters separate the lists.
       An example of the format follows.

       ``"variables@lower_bounds:upper_bounds#num_samples"``

       For example, a ``<formularesponse>`` element that includes the
       ``samples`` attribute might look like either of the following.

       ``<formularesponse samples="x,n@1,2:3,4#10">``

       ``<formularesponse samples="R_1,R_2,R_3@1,2,3:3,4,5#10">``

Variable names must be at least one character long. They must start with a letter, which can be followed by letters, numbers and underscores. We strongly recommend only using one underscore, which renders to students as a subscript.

Tensor notation is also supported, as ``Name_{ijk}^{123}``, where the name must start with a letter, but can otherwise contain letters or numbers, subscripts are contained in the lower braces, and superscripts are contained in the raised braces. Superscripts and subscripts must only be letters or numbers. No other underscores can appear in the name. Note that the subscript must come first, and the braces ensure that the superscripts are not confused with exponentiation.

All variable names (standard and tensor formats) may contain one or more apostrophes (primes) at the end of the variable name, for example, to indicate a derivative or new coordinate system. Note that some students may have trouble entering primes, which some browsers/operating systems automatically convert to a "smart apostrophe" (tablets are most likely to have this issue). We recommend providing a variable name that students may copy and paste to get around this problem.

The following are examples of valid variable names: ``V_out``, ``m_1``, ``G_{ij}``, ``H^{xy}``, ``f'``, ``x_1''``, and ``H_{ij}^{12}''``.


Children
--------

* ``<label>``
* ``<description>``
* ``<formulaequationinput>``
* ``<responseparam>``
* ``<script>``
* ``<solution>``

``<label>``
===========

Required. Identifies the question or prompt. You can include HTML tags within
this element.

Attributes
----------

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
--------

None.

``<formulaequationinput>``
==========================

Required. Creates a response field in the LMS where learners enter a response.

Learners also see a second field below the response field that displays a
typeset version of the entered response. The parser that renders a learner's
plain text into typeset math is the same parser that evaluates the response for
grading.

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

Children
--------

None.

``<responseparam>``
===================

Used to define an upper bound on the variance of the numerical methods used to
approximate a test for equality.

Attributes
----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``type``
     - ``"tolerance"`` defines a tolerance for a number.
   * - ``default``
     - Required. A number or a percentage specifying how close the learner
       and grader expressions must be. If you do not include a tolerance, the
       expression is vulnerable to rounding errors during sampling. The
       result of such unavoidable errors is that the grader can mark some
       learner input as incorrect, even if it is algebraically equivalent.

Children
--------

None.

``<script>``
============

Optional. Specifies a script that the grader uses to evaluate a learner's
response. A problem behaves as if all of the code in all of the script elements
were in a single script element. Specifically, any variables that are used in
multiple ``<script>`` elements share a namespace and can be overridden.

As with all Python code, indentation matters, even though the code is embedded
in XML.

Attributes
----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``type``
     - Required. Must be set to ``loncapa/python``.

Children
--------

None.

``<solution>``
==============

Optional. Identifies the explanation or solution for the problem, or for one of
the questions in a problem that contains more than one question.

This element contains an HTML division ``<div>``. The division contains one or
more paragraphs ``<p>`` of explanatory text.

.. seealso::
 

 :ref:`Math Expression Input` (reference)

 :ref:`Adding Math Expression Problem` (reference)



**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
