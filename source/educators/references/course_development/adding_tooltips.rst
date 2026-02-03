.. _Adding Tooltips:

Adding Tooltips to a Problem
############################

.. tags:: educator, reference

.. START ADDING TOOLTIPS

.. warning::

  Tooltips are not exposed in the Open edX Studio problem editor.

  Studio and LMS support of tooltips is not guaranteed to work.

You can add inline tooltips to help learners understand terminology or other aspects of a problem. Tooltips display text to learners when they move their
cursors over a tooltip icon.

The following example problem includes two tooltips. The tooltip that provides
a definition for "ROI" is being shown.

.. image:: /_images/educator_references/tooltip.png
 :alt: An example of a tooltip from a learner's point of view.
 :width: 500

.. note::
  For learners using a screen reader, the tooltip expands to make its
  associated text accessible when the screen reader focuses on the tooltip
  icon.

To add the tooltip, you wrap the text that you want to appear as the tooltip in
the ``clarification`` element.  For example, the following problem contains two
tooltips.

.. code-block:: xml

  <problem>
      <text>
          <p>Given the data in Table 7 <clarification>Table 7: "Example PV
            Installation Costs", Page 171 of Roberts textbook</clarification>,
            compute the ROI <clarification><strong>ROI</strong>: Return on
            Investment</clarification> over 20 years.
          </p>
       . . .

.. END ADDING TOOLTIPS

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

  :ref:`Learner View of Problems` (reference)

  :ref:`Advanced Editor` (reference)

  :ref:`Add Hints via the Advanced Editor` (how-to)

  :ref:`Modifying a Released Problem` (reference)

  :ref:`Add Unsupported Exercises Problems` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
