.. :diataxis-type: reference
.. _Dropdown Problem XML:

******************************
Dropdown Problem OLX Reference
******************************

========
Template
========

.. code-block:: xml

  <problem>
    <optionresponse>
      <label>Question or prompt text</label>
      <description>Optional information about how to answer the question</description>
      <option correct="False">Option Label
        <optionhint>Feedback for when learner selects this answer.</optionhint>
      </option>
      <option correct="True">Option Label
        <optionhint>Feedback for when learner selects this answer.</optionhint>
      </option>
      <solution>
        <div class="detailed-solution">
          <p>Explanation or Solution Header</p>
          <p>Explanation or solution text</p>
        </div>
      </solution>
    </optionresponse>
    <demandhint>
      <hint>Hint 1</hint>
      <hint>Hint 2</hint>
      <hint>Hint 3</hint>
    </demandhint>
  </problem>

========
Elements
========

For dropdown problems, the ``<problem>`` element can include this
hierarchy of child elements.

.. code-block:: xml

  <optionresponse>
      <label>
      <description>
      <optioninput>
            <option>
                <optionhint>
      <solution>
  <demandhint>
      <hint>

In addition, standard HTML tags can be used to format text.

--------------------
``<optionresponse>``
--------------------

Required. Indicates that the problem is a dropdown problem.

^^^^^^^^^^
Attributes
^^^^^^^^^^

None.

^^^^^^^^
Children
^^^^^^^^

* ``<label>``
* ``<description>``
* ``<optioninput>``
* ``<solution>``

-----------
``<label>``
-----------

Required. Identifies the question or prompt. You can include HTML tags within
this element.

^^^^^^^^^^
Attributes
^^^^^^^^^^

None.

^^^^^^^^
Children
^^^^^^^^

None.

-----------------
``<description>``
-----------------

Optional. Provides clarifying information about how to answer the question. You
can include HTML tags within this element.

^^^^^^^^^^
Attributes
^^^^^^^^^^

None.

^^^^^^^^
Children
^^^^^^^^

None.

-----------------
``<optioninput>``
-----------------

Required. Designates an answer option.

^^^^^^^^^^
Attributes
^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``options``
     - Either this attribute or a set of ``<option>`` child elements for
       ``<optioninput>`` is required. Accepts a comma separated list of
       values in the following format.

       ``options="('Answer1','Answer2','Answer3')"``

   * - ``correct``
     - Used if the ``options`` attribute is set. Required. Indicates
       which of the answer options is correct.

^^^^^^^^
Children
^^^^^^^^

* ``<option>``
* ``<optionhint>``

------------
``<option>``
------------

Designates an answer option. Either a set of ``<option>`` child elements or the
``options`` attribute for ``<optioninput>`` is required.

^^^^^^^^^^
Attributes
^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``correct``
     - Required. Indicates whether the answer option is correct or incorrect.
       When set to ``"true"``, the choice is a correct answer. At least one
       required. When set to ``"false"``, the choice is an incorrect answer.

If the ``<option>`` element is used, ``<optionhint>`` is a child of
``<option>``.

----------------
``<optionhint>``
----------------

Optional. Specifies feedback for the answer.

^^^^^^^^^^
Attributes
^^^^^^^^^^

None.

^^^^^^^^
Children
^^^^^^^^

None.

--------------
``<solution>``
--------------

Optional. Identifies the explanation or solution for the problem, or for one of
the questions in a problem that contains more than one question.

This element contains an HTML division ``<div>``. The division contains one or
more paragraphs ``<p>`` of explanatory text.

----------------
``<demandhint>``
----------------

Optional. Specifies hints for the learner. For problems that include multiple
questions, the hints apply to the entire problem.

^^^^^^^^^^
Attributes
^^^^^^^^^^

None.

^^^^^^^^
Children
^^^^^^^^

``<hint>``

----------
``<hint>``
----------

Required. Specifies additional information that learners can access if needed.

^^^^^^^^^^
Attributes
^^^^^^^^^^

None.

^^^^^^^^
Children
^^^^^^^^

None.


.. seealso::
 :class: dropdown

  :ref:`Dropdown` (reference)
  :ref:`Adding Dropdown` (how to)
  :ref:`Use Hints in a Dropdown Problem` (how to)
  :ref:`Use Feedback in a Dropdown Problem` (how to)