.. _Manage Numerical Input Problem: 

################################
Manage a Numerical Input Problem
################################

.. tags:: educator, how-to

.. contents::
  :local:
  :depth: 2

***********************************
Add a Numerical Input Problem
***********************************

.. youtube:: fkoF8ZDPMoQ

You add numerical input problems in Studio by selecting the **Problem**
component. In the problem editor, select the **Numerical Input** option. Fill in
the fields on this screen to create your problem.

.. image:: /_images/educator_how_tos/problem_editor_numerical_input.png
 :alt: An example numerical input problem in the problem editor with number
    indicators labeling the various features.
 :width: 800

Creating a numerical input problem is as simple as:

#. Editing the **Display Name**. Click the pen symbol to edit.
#. Filling in the **Question** field.
#. Filling in the **Explanation** field. When this is shown to learners is
   based on the selection in the **Show answer** panel on the right.
#. Filling in the **Answer** fields. For numerical input problems, only correct
   answers can be added here. Additional answers can be added by clicking the
   **Add answer** button. Answers can be deleted by clicking the trash can icon.
   Feedback can be provided for each answer. More information on feedback can be
   found in the following section.
#. Selecting and filling in any desired settings on the right.

.. note:: Only correct answers can be added to a numerical input problem.

If you have any questions on the specifics of using the simple editor, please check
out :ref:`Simple Editor` and :ref:`Guide to Problem Settings`.

*****************************
Add a Tolerance or a Range
*****************************

To give learners the option to receive full credit for a close approximation of
the correct answer, and to support a wide range of possible correct numerical
answers, you can specify a tolerance for the correct answer or a range of values
to mark as correct for the numerical input problem type.

.. contents::
  :local:
  :depth: 1

.. note:: You can either have a **tolerance** or an **answer range** for a
  numerical input problem. You cannot add both.

==================
Add a Tolerance
==================

You can specify a margin of error or tolerance for learner responses. You
can specify a percentage or number. The tolerance settings panel can be
found to the right of the editor.

.. image:: /_images/educator_how_tos/problem_editor_tolerance_box.png
 :alt: An example tolerance setting set to 5%.
 :width: 200

==========================
Specify an Answer Range
==========================

You can specify an answer range so that any learner response within that range
is marked correct.

Add an answer range by selecting the **Add answer range** button from the
**Add answer** dropdown. This option can only be selected if you only have one
answer. This will replace your answer field with an answer range field.

.. image:: /_images/educator_how_tos/problem_editor_answer_range_box.png
 :alt: An example answer range set from 1 to 10. This includes 1 but not 10.
 :width: 200

To format an answer range, you provide the starting and
ending values and then separate them with a comma character (``,``). You then
surround the range with bracket (``[ ]``) or parentheses characters (``( )``),
or a combination of one bracket and one parenthesis.

* Use a bracket to include the number next to it in the range, as in a less
  than or equal to, or greater than or equal to, inequality.

* Use a parenthesis to exclude the number from the range, as in a less than or
  greater than inequality.

For example, to identify the correct answers as 5, 6, or 7, but not 8, specify
``[5,8)``. To identify the correct answers as 6, 7, and 8, but not 5, specify
``(5,8]``.


**************************************************
Add Feedback and Hints via the Simple Editor
**************************************************

===================
Add Feedback
===================

For an overview of feedback in problems, see :ref:`Adding Feedback and Hints to
a Problem`. In numerical input problems, you can provide feedback for correct
responses. If you define multiple correct responses, you can define feedback
for each response. In numerical input problems, use feedback to reinforce the
process used to arrive at the correct answer.

You can add answer-specific feedback for each answer in a numerical input problem.
You can access the feedback panel shown below by clicking the button to the right
of the answer text.

.. image:: /_images/educator_how_tos/problem_editor_feedback_box_2.png
 :alt: An example of an expanded feedback section for dropdown problems showing
    the 'is selected' feedback field.
 :width: 600

Simply enter your feedback message in this text field. It will display when the
learner submits this answer.

.. note:: You cannot add feedback for an incorrect answer in numerical input
  problems. Add hints to guide the learners in the correct direction instead.

.. _Use Hints in a Numerical Input Problem:

===================
Add Hints
===================

You can add hints to a numerical input problem using the simple editor or the
advanced editor. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

.. _Editing Numerical Input Problems using the Advanced Editor:

******************************************************************
Edit Numerical Input Problems using the Advanced Editor
******************************************************************

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

==================================================
Add Feedback via the Advanced Editor
==================================================

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

==================================================
Add Hints via the Advanced Editor
==================================================

See :ref:`Add Hints via the Advanced Editor` for more information about adding hints to problems.

.. _Multiple Responses in Numerical Input Problems:

=======================================================
Add Multiple Correct Responses via the Advanced Editor
=======================================================

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

==================================================
Add a Tolerance via the Advanced Editor
==================================================

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

==================================================
Specify an Answer Range via the Advanced Editor
==================================================

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


.. _Add Text After the Numeric Response Field:

********************************************
Add Text after the Numeric Response Field
********************************************

You might want to include a word, phrase, or sentence after the response field
in a numerical input problem to help guide your students or resolve ambiguity.

.. image:: /_images/educator_how_tos/NI_trailing_text.png
 :width: 500
 :alt: Three numerical input problems with text after the response field:
     "km", a percent sign, and a symbol for meters per second squared.

To do this, you use the advanced editor.

In the problem, locate the ``formulaequationinput`` element. This element
creates the response field for the problem and is a child of the
``numericalresponse`` element.

To add text after the response field, add the ``trailing_text`` attribute
together with the symbol or text that you want to use inside the
``formulaequationinput`` element. An example problem follows with three
questions that use this attribute.

.. note:: You can use MathJax inside the ``trailing_text`` attribute, as the
 third question in this example shows. You cannot use HTML inside this
 attribute.

.. code-block:: xml

  <problem>
    <numericalresponse answer="12.87">
      <label>How far is 8 miles in kilometers?</label>
      <formulaequationinput trailing_text="km" />
    </numericalresponse>

    <numericalresponse answer="91">
      <label>According to the Pew Research Center's Internet and American Life
       Project, what percentage of the world's population had a cellular phone
       as of May 2013?</label>
      <formulaequationinput trailing_text="%" />
    </numericalresponse>

    <numericalresponse answer="9.81">
      <label>What is the strength of Earth's gravity, to two decimal places?</label>
      <formulaequationinput trailing_text="\(m/s^{2}\)" />
    </numericalresponse>
  </problem>

.. seealso::
 

 :ref:`About Numerical Input` (reference)

 :ref:`Numerical Input Problem XML` (reference)

 :ref:`Award Partial Credit in a Numerical Input Problem` (how to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
