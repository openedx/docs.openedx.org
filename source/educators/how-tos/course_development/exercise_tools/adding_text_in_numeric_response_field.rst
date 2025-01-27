.. _Add Text After the Numeric Response Field:

Add Text after the Numeric Response Field
#########################################

.. tags:: educator, how-to

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

 :ref:`Adding Numerical Input Problem` (how-to)

 :ref:`Awarding Partial Credit in a Numerical Input Problem` (how-to)

 :ref:`Use Feedback in a Numerical Input Problems` (how-to)

 :ref:`Editing Numerical Input Problems using the Advanced Editor` (how-to)

 :ref:`Numerical Input Problem XML` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
