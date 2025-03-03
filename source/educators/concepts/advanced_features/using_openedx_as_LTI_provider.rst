.. _Using Open edX as an LTI Tool Provider:

Using Open edX as an LTI Tool Provider
######################################

.. tags:: educator, concept

You can also include content from an LTI provider in your courses. For more
information, see :ref:`About the LTI Component`.

.. _Grading Remote Content:

Grading Remote Content
**********************

.. warning:: This feature was a closed pilot experiment. This feature is poorly
  documented and may not work properly.

When you include problem components from a graded subsection in your Open edX
instance in an external LMS, your Open edX instance will grade the learner
responses to those problems. Your instance then transfers the learner scores
back to the external LMS. This exchange between an external LMS, your Open edX
instance, and the external LMS again is near real time. It can take a few
moments to complete this exchange for a single problem component, and up to
several minutes to return aggregated scores of all of the problems in a unit or
subsection.

When you include problem components from your Open edX instance in an external
LMS, note the following requirements.

* The problem component must be in one of the graded subsections in your course.
* Your external LMS might also require that you use a specific part of the
  course for graded content. For example, in Canvas, you must add the LTI URL
  of a problem component to the "Assignments" section of a course, or to a
  module item that points to an assignment. In addition, the user who launches
  the LTI material must be eligible to get a grade for the assignment; that is,
  a learner and not a TA or course designer.

For more information about constructing an LTI URL for a course component, see
:ref:`Determine Content Addresses`.

.. seealso::
 

 :ref:`Create a Duplicate Course for LTI use` (how-to)

 :ref:`Determine Content Addresses` (how-to)

 :ref:`Planning for Content Reuse` (reference)

 :ref:`Open edX as an LTI Provider to Canvas` (how-to)

 :ref:`Open edX as an LTI Provider to Blackboard` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
