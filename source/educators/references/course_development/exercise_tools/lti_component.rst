.. :diataxis-type: reference
.. _LTI Component:

###############
LTI Component
###############

You can integrate remote learning tools, such as applications and textbooks,
into your course with the learning tools interoperability (LTI) component. The
LTI component supports tools with the :ref:`LTI 1.1` and :ref:`LTI 1.3` specifications.
Additionally, the LTI 1.3 tools can use the following LTI Advantage extensions:
:ref:`Deep Linking`, :ref:`Assignments and Grades services` and
:ref:`Names and Roles Provisioning Service`.

.. contents::
   :local:
   :depth: 2

Before you make tools from an external site available through your course, be
sure to review the tools to ensure that they are accessible to people with
disabilities. For example, in addition to testing the LTI components that you
add to your course, you can ask third party providers to confirm that a tool is
accessible, and, if available, contact your on campus accessibility support
services for additional guidance. For more information, see :ref:`Accessibility
Best Practices for Course Content Development`.

*********************
Overview
*********************

You can use an LTI component in several ways.

* You can add remote LTI tools that display content only, and that do
  not require a learner response. An example is a digital copy of a textbook in
  a format other than PDF.

* You can add remote LTI tools that do require a learner response. A remote
  LTI tool provider grades the responses.

* You can use the LTI component as a placeholder for synchronizing with a
  remote grading system.

For example, the following LTI component integrates a Cerego tool that learners
interact with into the LMS for a course.

.. image:: /_images/educator_references/LTIExample.png
   :alt: A page in the LMS showing the Cerego music player and a question for
    learners to answer about it.

When you add an LTI component to your course, the edX Learning Management
System (LMS) is the LTI tool consumer, and the external tool or content is the
LTI tool provider.

Be sure to review all supplemental materials to ensure that they are accessible
before making them available through your course. For more information, see
:ref:`Accessibility Best Practices for Course Content Development`.

You can also integrate content from a course into a remote learning management
system such as Canvas or Blackboard.

For more information about how to use Studio as an LTI tool provider, see
:ref:`Using Open edX as an LTI Tool Provider<using open edx as an lti tool provider>`.

.. note the slightly different destination links ^. Alison 23 Nov 2015

.. seealso::
 :class: dropdown

  :ref:`Enable LTI Components` (how to)
  :ref:`LTI Component settings` (reference)