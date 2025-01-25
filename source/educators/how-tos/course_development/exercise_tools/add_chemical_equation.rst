.. _Chemical Equation:

Add a Chemical Equation Problem
###############################

.. tags:: educator, how-to

The chemical equation problem type allows the learner to enter text that
represents a chemical equation into a text box. The system converts that text
into a chemical equation below the text box. The grader evaluates the
learner's response by using a Python script that you create and embed in the
problem.

.. image:: /_images/educator_how_tos/ChemicalEquationExample.png
 :alt: Image of a chemical equation response problem.

.. contents::
  :local:
  :depth: 1

.. note::
  You can make a calculator available to your learners on every
  unit page. For more information, see :ref:`Calculator`.

Create a Chemical Equation Problem
**********************************

Chemical equation problems use MathJax to create formulas. For more
information about using MathJax in Studio, see :ref:`MathJax in Studio`.

To create the above chemical equation problem, follow these steps.

#. In the unit where you want to create the problem, select **Problem** under
   **Add New Component**.
#. Select **Advanced problem types**. Then select **Blank Advanced Problem**.
#. In the component that appears, select **Edit**.
#. In the component editor, paste the code from below.
#. Select **Save**.

Sample Chemical Equation Problem Code
=====================================

.. code-block:: xml

  <problem>
    <startouttext/>
    <p>Some problems may ask for a particular chemical equation. Practice by writing out the following reaction in the box below.</p>

  \( \text{H}_2\text{SO}_4 \longrightarrow \text { H}^+ + \text{ HSO}_4^-\)

    <customresponse>
      <chemicalequationinput size="50" label="Enter the chemical equation"/>
      <answer type="loncapa/python">

  if chemcalc.chemical_equations_equal(submission[0], 'H2SO4 -> H^+ + HSO4^-'):
      correct = ['correct']
  else:
      correct = ['incorrect']

      </answer>
    </customresponse>
    <p>Some tips:</p>
    <ul>
    <li>Use real element symbols.</li>
    <li>Create subscripts by using plain text.</li>
    <li>Create superscripts by using a caret (^).</li>
    <li>Create the reaction arrow (\(\longrightarrow\)) by using "->".</li>
    </ul>

    <endouttext/>

   <solution>
   <div class="detailed-solution">
   <p>Solution</p>
   <p>To create this equation, enter the following:</p>
     <p>H2SO4 -> H^+ + HSO4^-</p>
   </div>
   </solution>
  </problem>

.. seealso::
 

 :ref:`Chemical Equation Problem XML` (reference)
