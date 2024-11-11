.. _Awarding Partial Credit in a Numerical Input Problem:

=========================================
Awarding Partial
=========================================

.. tags:: educator, how-to

You can configure a numerical input problem to award partial credit to learners
who submit an answer that is close or related to the correct answer. You must
use the :ref:`advanced editor<Advanced Editor>` to configure partial credit.

In the following example, the learner entered an answer that was close to the
correct answer and received partial credit.

.. image:: /_images/educator_how_tos/partial_credit_numerical_input.png
 :alt: A numerical input problem with partial credit for a close answer.


For an overview of partial credit in problems, see :ref:`Partial Credit`.

You can use the following methods to award partial credit in a numerical input
problem.

.. contents::
  :local:
  :depth: 1

.. note:: You can use these methods of awarding partial credit individually or
 in combination.

--------------------------
Identifying Close Answers
--------------------------

You can configure a numerical input problem so that answers that are close to
the correct answer receive partial credit.

To do so, you configure the tolerance for incorrect answers. Learners receive
partial credit for close answers based on the tolerance. By default, the
tolerance is multiplied by 2 and the following rules are applied.

* An answer within the tolerance receives 100% of the points for the problem.

* An answer within or equal to 2x of the tolerance receives 50%.

* An answer more than 2x the outside of the tolerance receives 0%.

You can optionally specify a different multiplier for the tolerance. For
example, you could set the multiplier to 3. In this case, the following rules
apply.

* An answer within the tolerance receives 100% of the points for the problem.

* An answer within or equal to 3x of the tolerance receives 50%.

* An answer more than 3x outside of the tolerance receives 0%.

^^^^^^^^^^^^^^^^^^^^^^^^
Configure Close Answers
^^^^^^^^^^^^^^^^^^^^^^^^

To configure a numerical input problem to award partial credit for close
answers, you add the following attributes to the problem XML.

* Add the ``partial_credit="close"`` attribute to the ``<numericalresponse>``
  element.

  You can use close answers in combination with a list. Set the
  attribute to ``partial_credit="close,list"``.

* Optionally, add the ``partial_range`` attribute to the ``<responseparam>``
  element and set its value to the tolerance multiplier. If you do not set the
  ``partial_range`` attribute, 2 is used as the tolerance multiplier.

For example, the following OLX shows a numerical problem that provides partial
credit for close answers.

.. code-block:: xml

  <problem>
    <numericalresponse answer="9.3*10^7" partial_credit="close">
      <label>How many miles away from Earth is the sun?</label>
      <description>Use scientific notation to answer.</description>
      <formulaequationinput/>
      <responseparam type="tolerance" default="1%" partial_range="3"/>
    </numericalresponse>
  </problem>

----------------------------------------------------
Awarding Partial Credit for Answers in a List
----------------------------------------------------

For some numerical input problems, mistakes do not help a learner arrive at the
correct answer. For example, a small mistake can lead to negative instead of
positive results, or to an answer that is off by a square root or numerical
factor.

For these types of problems, you can configure a list of wrong answers that
receive partial credit. Learners who submit answers that are on the list
receive 50% of the problem's points.

^^^^^^^^^^^^^^^^^^
Configure a List
^^^^^^^^^^^^^^^^^^

To configure a numerical input problem to award partial credit for answers in a
list, you add the following attributes to the problem XML.

* Add the ``partial_credit="list"`` attribute to the ``<numericalresponse>``
  element.

  You can use a list in combination with close answers. Set the
  attribute to ``partial_credit="close,list"``.

* Add the ``partial_answers`` attribute to the ``<responseparam>`` element. Set
  its value to one or more answers that should earn 50% of the problem's
  points. Separate multiple values by a comma (,).

For example, the following XML shows the numerical problem template
updated to provide partial credit for a different answer.

.. code-block:: xml

  <problem>
    <numericalresponse answer="9.3*10^7" partial_credit="close">
      <label>How many miles away from Earth is the sun?</label>
      <description>Use scientific notation to answer.</description>
      <formulaequationinput />
      <responseparam partial_answers="150*10^6"/>
    </numericalresponse>
  </problem>

=============================================
Adding Text after the Numeric Response Field
=============================================

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
 :class: dropdown

 :ref:`Numerical Input` (reference)

 :ref:`Adding Numerical Input Problem` (how to)

 :ref:`Use Feedback in a Numerical Input Problems` (how-to)

 :ref:`Editing Numerical Input Problems using the Advanced Editor` (how to)

 :ref:`Numerical Input Problem XML` (reference)