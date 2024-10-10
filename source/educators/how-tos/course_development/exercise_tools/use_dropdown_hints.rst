.. :diataxis-type: how-to
.. _Use Hints in a Dropdown Problem:

============
Adding Hints
============

You can add hints to a dropdown problem. For an overview of hints in problems, see
:ref:`Adding Feedback and Hints to a Problem`.

In the settings panels on the right of the editor, you'll find a Hints panel.

.. image:: /_images/educator_how_tos/problem_editor_hints_box.png
 :alt: An example of the hints settings panel.
 :width: 200

Click the **Add hint** button to add a new hint text field. To delete any hints
you've added, click the trash can icon next to its respective hint field.

.. note::
  You can configure any number of hints. The learner views one hint at a time
  and views the next one by selecting **Hint** again.

========================================
Adding Hints
========================================

In the advanced editor, you add the ``<demandhint>`` element immediately before
the closing ``</problem>`` tag, and then configure each hint using the
``<hint>`` element.

.. code-block:: xml

  <problem>
  .
  .
  .
  <demandhint>
    <hint>Hint 1</hint>
    <hint>Hint 2</hint>
    <hint>Hint 3</hint>
  </demandhint>
  </problem>

For example, the following OLX for a single select problem shows two hints.

.. code-block:: xml

  <problem>
    <multiplechoiceresponse>
    .
    .
    .
    </multiplechoiceresponse>
    <demandhint>
      <hint>A fruit is the fertilized ovary from a flower.</hint>
      <hint>A fruit contains seeds of the plant.</hint>
    </demandhint>
  </problem>


  .. seealso::
 :class: dropdown

  :ref:`Dropdown` (reference)
  :ref:`Dropdown Problem XML` (reference)
  :ref:`Adding Dropdown` (how to)
  :ref:`Use Feedback in a Dropdown Problem` (how to)