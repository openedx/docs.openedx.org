.. :diataxis-type: reference
.. _Math Expression Input:

##############################
Math Expression Input Problems
##############################

The math expression input problem type is a core problem type that can be added
to any course. At a minimum, math expression problems include a question or
prompt and a response field for a numeric answer.

.. contents::
  :local:
  :depth: 2

For more information about the core problem types, see
:ref:`Working with Problem Components`.

********
Overview
********

In math expression input problems, learners enter text that represents a
mathematical expression. The text is converted to a symbolic expression that
appears below the response field. Unlike numerical input problems, which only
allow integers and a few select constants, math expression input problems can
include unknown variables and more complicated symbolic expressions.

For more information about how learners enter expressions, see
:ref:`Math Formatting` in the *Open edX Learner's Guide*.

.. note::
  You can make a calculator tool available to your learners on every unit
  page. For more information, see :ref:`Calculator`.

For math expression input problems, the grader uses numerical sampling to
determine whether a learner's response matches the math expression that you
provide, to a specified numerical tolerance. You specify the allowed variables
in the expression as well as the range of values for each variable.

When you create a math expression input problem in Studio, you use `MathJax
<http://www.mathjax.org>`_ to format text strings into "beautiful math." For
more information about how to use MathJax in Studio, see :ref:`MathJax in
Studio`.

.. note:: Math expression input problems currently cannot include negative
 numbers raised to fractional powers, such as (-1)^(1/2). Math expression
 input problems can include complex numbers raised to fractional powers, or
 positive non-complex numbers raised to fractional powers.

=====================================
Example Math Expression Input Problem
=====================================

In the LMS, learners enter a value into a response field to complete a math
expression input problem. The following example shows a completed math
expression input problem that contains two questions.

.. image:: /_images/educator_references/MathExpressionInputExample.png
 :alt: A problem shown in the LMS that requests the symbolic expressions for
   displacement and for elongation of a blade. Both questions were answered
   correctly. The solutions are not shown.
 :width: 500

The open learning XML (OLX) markup for this example math expression input
problem follows.

.. code-block:: xml

  <problem>
    <formularesponse inline="1" type="cs" samples="R,omega,E,rho,L@0.1,0.1,0.1,0.1,0.1:10,10,10,10,10#10" answer="(rho*omega^2*L^2)/E*((11*L)/48 +(3*R)/8)">
      <label>Find a symbolic expression for the displacement of the blade mid-section, \( u_{x}(L/2) \), in terms of \(R\), \(L\), \(\rho\), \(\omega\), and \(E\).</label>
      <description>\(u_x(L/2) = \)</description>
      <responseparam type="tolerance" default="1%"/>
      <textline inline="1" math="1"/>
      <solution>
        <div class="worked-solution">
          <p><b>Obtaining the displacement at the mid-section \( u_{x}(x = L / 2)\):</b></p><p>According to the definition of strain,</p>
          \[ \frac {du_{x}(x)} {dx} = \epsilon_a(x).\]
          <p>Therefore, we can obtain the displacement field as</p>
          \[ u_x(x) = u_x(0) + \int_0^x \epsilon_a (x') dx' = u_x(0) + \left[ \frac{\rho \omega^2}{E} \left(\frac{L^2x'}{2} - \frac{(x')^3}{6} + RLx' - \frac{R(x')^2}{2} \right) \right]_0^x\]
          <p>Since the bar is fixed at x=0, therefore \(u_x(0)=0\). Hence we obtain</p>
          \[\Rightarrow u_x(x) = \frac{\rho\omega^2}{E} \left( \frac{L^2x}{2} - \frac{x^3}{6} + RLx - \frac{Rx^2}{2} \right).\]
          <p>The displacement of the bar at \(x=L/2\) is </p>
          \[u_{x}(L/2) = \frac {\rho\omega^2L^2}{E} \left( \frac {11L}{48} + \frac {3R}{8} \right).\]
        </div>
      </solution>
    </formularesponse>

    <formularesponse inline="1" type="cs" samples="R,omega,E,rho,L@0.1,0.1,0.1,0.1,0.1:10,10,10,10,10#10" answer="(rho*omega^2)/E*(L^3/3 + (R*L^2)/2)">
      <label>Find a symbolic expression for the blade elongation \( \delta \) in terms of \(R\), \(L\), \(\rho\), \(\omega\), and \(E\).</label>
      <description>\(\delta = \)</description>
      <responseparam type="tolerance" default="1%"/>
      <textline inline="1" math="1"/>
      <solution>
        <div class="worked-solution">
          \[  \delta = \frac {\rho \omega^2}{E} \left( \frac {L^3} {3} + \frac { RL^2} {2} \right) \]
          <p><b>Obtaining the total elongation of the blade  \( \delta \):</b></p>
          <p>The strain field in the bar is</p>
          \[  \epsilon_a(x) = \frac {\mathcal{N}(x)}{EA} = \frac {\rho \omega^2 \left( \frac {L^2 - x^2}{2} + R\left(L-x\right)\right)}{E}. \]
          <p>We can now calculate the elongation of the bar as the following.</p>
          \[ \delta = \int_0^L \epsilon_{a}(x)dx = \int_0^L \frac {\rho \omega^2}{E} \left( \frac {L^2 - x^2}{2} + R\left(L-x\right)\right)dx. \]
          \[ \Rightarrow \delta= \left[ \frac { \rho \omega^2}{E} \left( \frac {L^2x}{2}  - \frac {x^3}{6} + RLx - \frac {Rx^2}{2} \right)\right]_0^L.\]
          \[ \Rightarrow \delta = \frac {\rho \omega^2}{E} \left( \frac {L^3}{2} - \frac{L^3}{6} + RL^2 - \frac {RL^2}{2} \right).\]
          \[\Rightarrow \delta= \frac {\rho \omega^2}{E} \left( \frac {L^3}{3} + \frac {RL^2}{2} \right). \]
        </div>
      </solution>
    </formularesponse>
  </problem>

.. seealso::
 :class: dropdown

  :ref:`Adding Math Expression Problem` (how to)
  :ref:`Math Expression Input Problem XML` (reference)