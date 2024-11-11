.. :diataxis-type: reference
.. _Numerical Input:

########################
Numerical Input Problem
########################

The numerical input problem type is a simple problem type that can be added to
any course. At a minimum, numerical input problems include a question or
prompt and a response field for a numeric answer. By adding hints, feedback, or
both, you can give learners guidance and help when they work on a problem.

.. contents::
  :local:
  :depth: 2

For more information about the simple problem types, see
:ref:`Working with Problem Components`.

**********
Overview
**********

In numerical input problems, learners enter numbers or specific and relatively
simple mathematical expressions to answer a question. The LMS automatically
converts the answer that learners enter into a symbolic expression that appears
below the response field.

Responses for numerical input problems can include integers, fractions, and
constants such as pi and *g*. Responses can also include text representing
common functions, such as square root (sqrt) and log base 2 (log2), as well as
trigonometric functions and their inverses, such as sine (sin) and arcsine
(arcsin). For these functions, learners enter text that is converted into
mathematical symbols. The following example shows a response entered by a
learner and the numerical expression that results.

.. image:: /_images/educator_references/Math5.png
 :alt: A learner typed n*x^(n-1) to enter the symbolic expression n times x to
     the n minus 1 power.

For more information about how learners enter expressions, see
`Math Formatting`_ in the *Open edX Learner's Guide*.

Some of the options for numerical input problems include the following.

* You can specify a correct answer explicitly or use a Python script.

* You can specify a margin of error, or tolerance, for the answers to numerical
  input problems so that learners' responses do not have to be exact.

.. note::
  You can make a calculator tool available to your learners on every unit
  page. For more information, see :ref:`Calculator`.

================================
Example Numerical Input Problem
================================

In the LMS, learners enter a value into a response field to complete a
numerical input problem. An example of a completed numerical input problem follows.

.. image:: /_images/educator_references/NumericalInputExample.png
 :alt: A problem with one question, answered correctly, in the LMS.

.. seealso::
 :class: dropdown

 :ref:`Editing Numerical Input Problems using the Advanced Editor` (how to)

 :ref:`Use Feedback in a Numerical Input Problems` (how-to)

 :ref:`Adding Numerical Input Problem` (how to)

 :ref:`Numerical Input Problem XML` (reference)

 :ref:`Awarding Partial Credit in a Numerical Input Problem` (how to)