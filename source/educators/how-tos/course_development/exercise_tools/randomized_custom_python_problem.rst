.. _Create a Randomized Custom Python Evaluated Input Problem:

Create a Randomized Custom Python-Evaluated Input Problem
#########################################################

.. tags:: educator, how-to

You can create a custom Python-evaluated input problem that randomizes
variables in the Python code.

#. In the unit where you want to create the problem, select **Problem** under
   **Add New Component**.

#. In the problem editor, select **Advanced problem types**. Then select **Custom Python-Evaluated Input**.

#. In the component editor, modify the example as needed.

#. Select the randomization option that applies better to your exercise. The option selected will define when to randomize the variables specified in the associated Python script. The options you can select are Never, Always, Per Student, and On Reset.

.. note::
  In the problem settings, you must set the **Randomization** value to
  something other than **Never** to have Python variables randomized. See
  :ref:`Randomization` for more information.

#. Select **Save**.

Example:
========

The following example demonstrates using randomization with a Python-evaluated
input problem.

.. note::
 This example uses the method ``random.randint`` to generate random numbers.
 You can use any standard Python library for this purpose.

.. code-block:: xml

  <problem>
    <p>Some problems in the course will utilize randomized parameters.
       For such problems, after you check your answer you will have the option
       of resetting the question, which reconstructs the problem with a new
       set of parameters.</p>
  <script type="loncapa/python">
  x1 = random.randint(0, 100)
  x2 = random.randint(0, 100)
  y = x1+x2
  </script>
  <p>Let (x_1 = $x1) and (x_2 = $x2). What is the value of (x_1+x_2)?</p>
  <numericalresponse answer="$y">
    <responseparam type="tolerance" default="0.01%" name="tol"
      description="Numerical Tolerance"/>
    <textline size="10"/>
  </numericalresponse>
  <solution>
    <p><b>Explanation:</b></p>
  </solution>
  </problem>

.. seealso::
 :class: dropdown

 :ref:`Custom Python-evaluated Input Problem (Write-Your-Own-Grader)` (reference)

 :ref:`Create a Custom Python Evaluated Input Problem in Studio` (how to)

 :ref:`Create a Custom Python Evaluated Input Problem in Script Tag Format` (how to)

 :ref:`Script Tag Format` (concept)

 :ref:`Award Partial Credit` (concept)