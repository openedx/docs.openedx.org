.. _About the LTI Component:

#######################
About the LTI Component
#######################

.. tags:: educator, concept

The Learning Tools Interoperability (LTI) component, also called the LTI
Consumer XBlock, allows educators to add external LTI tools to course content
in an Open edX course.

This page explains the decisions educators and site operators need to make when
setting up an LTI tool in their Open edX instance.

.. note::

   The Open edX platform can also be configured as an LTI tool provider, so
   that another learning management system launches content from the Open edX
   platform. That is a separate feature. For more information, see :ref:`using
   the Open edX platform as an LTI tool provider <Using your Open edX instance
   as an LTI Tool Provider>`.

The LTI Consumer XBlock supports LTI 1.1/1.2 tools and tools that comply with
the `LTI 1.3`_ specification. LTI 1.3 tools can also use LTI Advantage
services: `Deep Linking`_, `Assignment and Grade Services`_, and `Names and
Role Provisioning Services`_.

The Open edX platform has achieved LTI Advantage Complete certification for the
:ref:`Teak <Teak LTI Certification>`, :ref:`Ulmo <Ulmo LTI Certification>`, and
:ref:`Verawood <Verawood LTI Certification>` releases.


.. contents:: Contents
   :local:
   :depth: 2


********
Overview
********

Use the LTI component when a course needs to launch an external learning tool
from an Open edX course unit. The tool may provide a learning activity, an
assessment, host interactive content or enable video conferencing.

Depending on the tool and configuration, an LTI integration can simply launch
external content, or it can support workflows such as grade return,
content selection through deep linking, or sharing course role and enrollment
information with the tool.

For example, the following LTI component integrates a Cerego tool that learners
interact with into the LMS for a course.

.. image:: /_images/educator_references/LTIExample.png
   :alt: A page in the LMS showing the Cerego music player and a question for
    learners to answer about it.

.. note::
  Be sure to review all supplemental materials to ensure that they are accessible
  before making them available through your course. For more information, see
  :ref:`Accessibility Best Practices Checklist`.


***************************************
Available Methods for LTI Configuration
***************************************

The Open edX platform offers two methods for configuring an LTI tool. Both
methods support LTI 1.1/1.2, LTI 1.3, and LTI Advantage services. In both
methods, educators add an LTI Consumer XBlock to a course unit in Studio. The
difference is where the tool configuration is stored and who manages it.

#. **Configure the LTI Consumer XBlock directly in Studio.**

   Educators enter the tool configuration on the LTI Consumer XBlock itself. For
   LTI 1.1/1.2, they will need to create an *LTI passport* on the *Advanced
   Settings* page and reference that in the XBlock.

   For instructions, see :ref:`Set up an LTI 1.1/1.2 component <Set up an LTI
   1_1 component>` and :ref:`Set up an LTI 1.3 component <Set up an LTI 1_3
   component>`.

   To reuse the same configuration within a course, educators can duplicate or
   copy and paste the configured XBlock. However, changes made to the original
   XBlock are not reflected in the copies.

#. **Use an LTI Store configuration managed in Django Admin.**

   A site operator installs and enables the LTI Store plugin, then creates the
   tool configuration in Django Admin. Educators add an LTI Consumer XBlock in
   Studio and reference the stored configuration by using its *Filter key*.

   For instructions, site operators can see :ref:`Set up a Reusable LTI Store`.
   Educators can see :ref:`Set up an LTI component using a reusable
   configuration`.

   The *Filter key* allows reuse of the same tool configuration in multiple
   locations in a course or across multiple courses. Changes made to the LTI
   Store configuration are reflected in all LTI Consumer XBlocks that reference
   it.


*********************
Choose an LTI Version
*********************

LTI 1.3 is the current LTI integration standard and is required for LTI
Advantage services like Deep Linking, Assignment and Grade Services (AGS), and
Names and Role Provisioning Services (NRPS). Use LTI 1.3 when the external tool
supports it.

The LTI 1.1/1.2 specifications are older versions of the standard. Use LTI
1.1/1.2 when a tool requires that version.


**********************
LTI Advantage Features
**********************

LTI Advantage is a set of services for LTI 1.3 tools. The Open edX platform
supports the following LTI Advantage services:

* **Assignment and Grade Services (AGS)**, which allows a tool to send and
  manage learner grades in the Open edX platform.

* **Deep Linking**, which allows course teams to select tool content from
  Studio for each component instead of changing the *Launch URL*.

* **Names and Role Provisioning Services (NRPS)**, which allows a tool to
  retrieve course membership and role information from the Open edX instance.

For more information, see :ref:`LTI Advantage Services`.


************************
Privacy and Learner Data
************************

Some LTI tools require personally identifiable information (PII) to function
properly. Educators can configure each LTI Consumer XBlock to share one or more
attributes of the user launching the LTI tool:

* Email

* Username

* Full name

Site operators need to enable PII sharing for the course before a component can
share any personally identifiable information with an LTI tool. For more
information, see :ref:`Allow sharing PII to LTI Components`.



.. seealso::

 :ref:`Set up an LTI 1_1 component` (how-to)

 :ref:`Set up an LTI 1_3 component` (how-to)

 :ref:`LTI Advantage Services` (reference)

 :ref:`Using your Open edX instance as an LTI Tool Provider` (concept)


**Maintenance chart**

+--------------------+------------------------+----------+----------------+
| Review Date        | Working Group Reviewer | Release  | Test situation |
+--------------------+------------------------+----------+----------------+
| 2026-06-25         | Aamir Ayub             | Verawood | Pass           |
+--------------------+------------------------+----------+----------------+
| 2025-03-19         | Documentation WG       | Sumac    | Pass           |
+--------------------+------------------------+----------+----------------+
