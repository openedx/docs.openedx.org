.. _Add Hints via the Advanced Editor:


Add Hints via the Advanced Editor
#####################################

.. tags:: educator, how-to

In the advanced editor, you add the ``<demandhint>`` element immediately before
the closing ``</problem>`` tag, and then configure each hint using the
``<hint>`` element.

For example:

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
 
:ref:`About Problems Exercises and Tools` (concept)

:ref:`Core Problem Types` (reference)

:ref:`Working with Problem Components` (reference)

:ref:`Guide to Problem Settings` (reference)

:ref:`Gradebook Assignment Types` (reference)

:ref:`Feedback Best Practices` (concept)

:ref:`Adding Feedback and Hints to a Problem` (reference)

:ref:`Configure Hint` (how-to)

:ref:`Partial Credit` (reference)

:ref:`Set the Assignment Type and Due Date for a Subsection` (how-to)

:ref:`Adding Tooltips` (reference)

:ref:`Learner View of Problems` (reference)

:ref:`Advanced Editor` (reference)

:ref:`Modifying a Released Problem` (reference)

:ref:`Add Unsupported Exercises Problems` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
