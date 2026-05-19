.. _About the LTI Component:

###########################
About the LTI Component
###########################

.. tags:: educator, site operator, concept

The Learning Tools Interoperability (LTI) component (LTI Consumer XBlock) allows educators to add
external learning tools that support LTI, to Open edX course content.

This page explains the decisions educators and site operators need to make when
setting up an LTI tool in their Open edX instance.

.. note::

   Open edX can also be configured as an LTI tool provider, so that another
   learning management system launches Open edX content. That is a separate
   feature. For more information, see :ref:`Using Open edX as an LTI Tool
   Provider`.

The LTI Consumer XBlock supports tools that comply with the `LTI 1.1`_ and
`LTI 1.3`_ specifications. LTI 1.3 tools can also use LTI Advantage services:
`Deep Linking`_, `Assignments and Grades services`_, and
`Names and Roles Provisioning Service`_.

As of the Ulmo release, the Open edX platform has achieved
:ref:`LTI Advantage Complete certification <Ulmo LTI Certification>`.

.. contents:: Contents
   :local:
   :depth: 2


*********************
Overview
*********************

Use the LTI component when a course needs to launch an external learning tool
from an Open edX unit. The tool may provide a learning activity, an assessment,
host interactive content or enable video conferencing.

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


****************************************
Available Methods for LTI Configuration
****************************************

Open edX offers two methods for configuring an LTI tool. Both methods support
LTI 1.1, LTI 1.3, and LTI Advantage services. In both methods, educators add an
LTI Consumer XBlock to a course unit in Studio. The difference is where the tool
configuration is stored and who manages it.

#. **Configure the LTI Consumer XBlock directly in Studio.**

  Educators enter the tool configuration on the LTI XBlock itself. For LTI 1.1,
  they will need to create an *LTI passport* on the *Advanced Settings* page and
  reference that in the XBlock.

  To reuse the same configuration within a course, educators can duplicate or
  copy and paste the configured XBlock. However, changes made to the original
  XBlock are not reflected in the copies.

#. **Use an LTI Store configuration managed in Django Admin.**

  A site operator installs and enables the LTI Store plugin, then creates the
  tool configuration in Django Admin. Educators add an LTI Consumer XBlock in
  Studio and reference the stored configuration by using its configuration key.

  The configuration key allows reuse of the same tool configuration in multiple course
  locations or across multiple courses. Changes made to the LTI Store
  configuration are reflected in all LTI Consumer XBlocks that reference it.


*****************************
Choose an LTI Version
*****************************

LTI 1.3 is the current LTI integration standard and is required for LTI
Advantage services like Deep Linking, Assignments and Grades services (AGS), and
Names and Roles Provisioning Service (NRPS). Use LTI 1.3 when the external tool
supports it.

LTI 1.1 and LTI 1.2 are older versions of the standard. Use LTI 1.1/1.2 when a
tool requires that version.


*****************************
LTI Advantage Features
*****************************

LTI Advantage is a set of services for LTI 1.3 tools. Open edX supports the
following LTI Advantage services:

* **Assignments and Grades services (AGS)**, which allows a tool to send and
  manage learner grades in Open edX.

* **Deep Linking**, which allows course teams to select tool content from
  Studio for each LTI XBlock instead of changing the `Launch URL`.

* **Names and Roles Provisioning Service (NRPS)**, which allows a tool to
  retrieve course membership and role information from the Open edX instance.

For more information, see :ref:`Enabling and using LTI Advantage features`.


*****************************
Privacy and Learner Data
*****************************

Some LTI tools require Personally Identifiable Information (PII) to function properly. Educators
can configure each LTI XBlock to share one or more of these attributes of
the user launching the LTI tool:

* Email

* Username

* Full name

Site operators need to enable PII sharing for the course before an XBlock
can be configured to share any Personally Identifiable Information (PII) with
an LTI tool. For more information, see :ref:`Allow sharing PII to LTI Components`.



.. seealso::

 :ref:`LTI Component Settings` (reference)

 :ref:`Enable_LTI_Components` (how-to)

 :ref:`Set up an LTI 1_1 component` (how-to)

 :ref:`Set up an LTI 1_3 component` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)

 :ref:`Using your Open edX instance as an LTI Tool Provider` (concept)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-03-19   |   Documentation WG            |     Sumac      |      Pass                      |
+--------------+-------------------------------+----------------+--------------------------------+
