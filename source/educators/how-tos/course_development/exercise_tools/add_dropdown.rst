.. _Add Dropdown:

Add a Dropdown Problem
######################

.. tags:: educator, how-to

You add dropdown problems in Studio by selecting the **Problem** component.
In the problem editor, select the **Dropdown** option. Fill in the fields on
this screen to create your problem.

.. image:: /_images/educator_how_tos/problem_editor_dropdown.png
 :alt: An example dropdown problem in the problem editor with number
    indicators labeling the various features.
 :width: 800

Creating a dropdown problem is as simple as:

#. Editing the **Display Name**. Click the pen symbol to edit.
#. Filling in the **Question** field.
#. Filling in the **Explanation** field. When this is shown to learners is
   based on the selection in the **Show answer** panel on the right.
#. Filling in the Answer fields. Select the correct answer by ticking off
   the radio button. Additional answers can be added by clicking the
   **Add answer** button. Answers can be deleted by clicking the trash can
   icon. Feedback can be provided for each answer. More information on
   feedback can be found in the following section.
#. Selecting and filling in any desired settings on the right.

If you have any questions on the specifics of using the simple editor, please
check out :ref:`Simple Editor` and :ref:`Guide toProblem Settings`.

.. _Editing Dropdown Problems using the Advanced Editor:

Editing Dropdown Problems using the Advanced Editor
***************************************************

If the simple editor is not enough to meet your needs, you can switch over to
the advanced editor. In the setting panels on the right of the editor, click
**Show advanced settings**, then scroll down and click **Switch to advanced
editor**.

You can use the advanced editor to identify the elements of a dropdown problem
with OLX. For more information, see :ref:`Dropdown Problem XML`. To format
equations, you can use MathJax. For more information, see :ref:`MathJax in
Studio`.

You can see the OLX for the example problem from the Overview section below.

.. code-block:: xml

  <problem>
    <optionresponse>
      <label>What type of data is age?</label>
      <optioninput options="('Nominal','Discrete','Continuous')"
      correct="Continuous"></optioninput>
    </optionresponse>
  </problem>

.. note:: You can begin work on the problem in the simple editor, and then
  switch to the advanced editor. However, after you save any advanced OLX
  changes you make in the advanced editor, you may not be able to cannot
  switch back to the simple editor.

.. seealso::
 

 :ref:`Dropdown` (reference)

 :ref:`Dropdown Problem XML` (reference)

 :ref:`Use Hints in a Dropdown Problem` (how-to)

 :ref:`Use Feedback in a Dropdown Problem` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
