.. _Using Open edX as an LTI Tool Provider:

Using Open edX as an LTI Tool Provider
######################################

.. tags:: educator, concept

.. note:: This feature was a closed pilot experiment. This feature is not
 supported for new users.

An experimental feature enabled the Open edX Edge site to be configured to be a
learning tool interoperability (LTI) provider to other systems and applications
that partner institutions use. After initial configuration and testing between
Edge and your system or application is complete, course teams could use this
feature to reuse Edge course content, including advanced problem types and
videos, in an on campus or in house learning management system. Examples
currently include courses running on Canvas and Blackboard.

You can also include content from an LTI provider in your Open edX courses. For
more information, see :ref:`LTI Component`.

.. _Grading Remote Content:

Grading Remote Content
**********************

.. note:: This feature was a closed pilot experiment. This feature is not
 supported for new users.

When you include the problem components in a graded Open edX subsection in an
external LMS, the Open edX system grades the learner responses to those
problems. The Open edX system then transfers the learner scores back to the
external LMS. This exchange between an external LMS, the Open edX system, and
the external LMS again is near real time. It can take a few moments to complete
this exchange for a single problem component, and up to several minutes to
return aggregated scores of all of the problems in a unit or subsection.

When you include Open edX problem components in an external LMS, note the
following requirements.

* The Open edX problem component must be in one of the graded subsections in
  your course.

* Your external LMS might also require that you use a specific part of the
  course for graded content. For example, in Canvas, you must add the LTI URL
  of a problem component to the "Assignments" section of a course, or to a
  module item that points to an assignment. In addition, the user who launches
  the LTI material must be eligible to get a grade for the assignment; that is,
  a learner and not a TA or course designer.

For more information about constructing an LTI URL for a course component, see
:ref:`Determine Content Addresses`.

.. seealso::
 :class: dropdown

 :ref:`Create a Duplicate Course for LTI use` (how-to)

 :ref:`Determine Content Addresses when using Open edX as an LTI Provider<Determine Content Addresses>` (how-to)

 :ref:`Planning for Content Reuse (LTI)<Planning for Content Reuse>` (reference)

 :ref:`Example: Open edX as an LTI Provider to Canvas<Open edX as an LTI Provider to Canvas>` (reference)

 :ref:`Example: edX as an LTI Provider to Blackboard<Open edX as an LTI Provider to Blackboard>` (reference)