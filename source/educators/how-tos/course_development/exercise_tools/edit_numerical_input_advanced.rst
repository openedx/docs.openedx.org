.. _Editing Numerical Input Problems using the Advanced Editor:

Edit Numerical Input Problems using the Advanced Editor
#######################################################

.. tags:: educator, how-to

If the simple editor is not enough to meet your needs, you can switch over to the
advanced editor. In the setting panels on the right of the editor, click
**Show advanced settings**, then scroll down and click
**Switch to advanced editor**.

You can use the advanced editor to identify the elements of a numerical input problem
with OLX. For more information, see :ref:`Numerical Input Problem XML`. To format
equations, you can use MathJax. For more information, see :ref:`MathJax in Studio`.

You can see the OLX for the example problem from the Overview section below.

.. code-block:: xml

  <problem>
    <numericalresponse answer="10">
      <label>In what base is the decimal numeral system?</label>
      <formulaequationinput/>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>The decimal numeral system is base ten.</p>
        </div>
      </solution>
    </numericalresponse>
  </problem>

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any advanced OLX
  changes you make in the advanced editor, you may not be able to cannot
  switch back to the simple editor.

.. _Use Feedback in a Numerical Input Problems:

Adding Feedback
***************

In the advanced editor, you configure feedback with the following syntax.

.. code-block:: xml

  <problem>
    <numericalresponse answer="Correct Answer">
      <label>Question text</label>
      <formulaequationinput />
      <correcthint>Feedback for the correct answer</correcthint>
    </numericalresponse>
  </problem>

For example, the following problem has feedback for each answer.

.. code-block:: xml

  <problem>
    <numericalresponse answer="4">
      <label>What is the arithmetic mean for the following set of numbers?
      (1, 5, 6, 3, 5)</label>
      <formulaequationinput />
      <correcthint>The mean for this set of numbers is 20 / 5 which equals 4.</correcthint>
    </numericalresponse>
  </problem>

If you define multiple correct responses, you can define feedback for each response.

Adding Hints
************

See :ref:`Add Hints via the Advanced Editor` for more information about adding hints to problems.

.. _Multiple Responses in Numerical Input Problems:

Adding Multiple Correct Responses
*********************************

You can specify more than one specific, correct response for numerical input problems.
To do this, use the advanced editor.

If you specify multiple correct responses, you cannot also specify a tolerance, a range,
or a text string as correct answers. For example, when you define multiple correct
responses, you can specify a numeric value for each correct answer but not a tolerance,
range, or text string.

To specify an additional correct response in the advanced editor, within the
``<numericalresponse>`` element add the ``<additional_answer />`` element with an
``answer=""`` attribute value.

.. code-block:: xml

  <problem>
    <numericalresponse answer="9.3*10^7">
      <label>How many miles away from Earth is the sun?</label>
      <description>Use scientific notation to answer.</description>
      <additional_answer answer="9.296*10^7"/>
      <formulaequationinput/>
    </numericalresponse>
  </problem>

Adding a Tolerance
******************

You can specify a margin of error or tolerance for learner responses. You can
specify a percentage, number, or range.

To add a tolerance in the advanced editor you include a ``<responseparam>``
element with a ``type="tolerance"`` attribute and a ``default`` attribute set
to either a number or a percentage value.

The following example shows a problem with a decimal tolerance.

.. code-block:: xml

  <problem>
    <numericalresponse answer="ANSWER (NUMBER)">
      <label>Question text</label>
      <responseparam type="tolerance" default=".02" />
      <formulaequationinput />
    </numericalresponse>
  </problem>

The following example shows a problem with a percentage tolerance.

.. code-block:: xml

  <problem>
    <numericalresponse answer="ANSWER (NUMBER)">
      <label>Question text</label>
      <responseparam type="tolerance" default="3%" />
      <formulaequationinput />
    </numericalresponse>
  </problem>

Specifying an Answer Range
**************************

You can specify an answer range so that any learner response within that
range is marked correct. To format an answer range, you provide the starting
and ending values and then separate them with a comma character (``,```). You
then surround the range with bracket (``[ ]``) or parentheses characters
(``( )``), or a combination of one bracket and one parenthesis.

* Use a bracket to include the number next to it in the range, as in a less
  than or equal to, or greater than or equal to, inequality.

* Use a parenthesis to exclude the number from the range, as in a less than or
  greater than inequality.

For example, to identify the correct answers as 5, 6, or 7, but not 8, specify
``[5,8)``. To identify the correct answers as 6, 7, and 8, but not 5, specify
``(5,8]``.

To specify a range in the advanced editor, you enter the complete, formatted
range in the ``<numericalresponse>`` element as the value for the ``answer``
attribute: ``<numericalresponse answer="[5,8)">`` or
``<numericalresponse answer="(5,8]">``.

.. seealso::
 

 :ref:`Numerical Input` (reference)

 :ref:`Adding Numerical Input Problem` (how-to)

 :ref:`Use Feedback in a Numerical Input Problems` (how-to)

 :ref:`Numerical Input Problem XML` (reference)

 :ref:`Awarding Partial Credit in a Numerical Input Problem` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
