.. _Configure an LTI Tool Using Reusable Configuration:

Configure an LTI Tool Using Reusable Configuration
##################################################

.. tags:: educator, how-to

Use this procedure when a site operator has already created a reusable LTI
configuration in LTI Store. In this workflow, the tool configuration is stored
in Django Admin, and the LTI Consumer XBlock in Studio references that stored
configuration.

Reusable LTI configurations can be used for LTI 1.1/1.2 and LTI 1.3 tools.
They are useful when the same tool configuration needs to be used in more than
one course or in more than one location in a course.

When you use a reusable configuration, you do not enter the tool credentials,
LTI 1.3 registration values, or LTI Advantage settings in Studio. Those values
come from LTI Store.

Before You Start
****************

Before you configure the component, make sure you have:

* Edit access to the course in Studio
* The LTI version used by the reusable configuration
* The reusable configuration's *Filter key* from your site operator

In Studio, you enter the Filter key in the *LTI Reusability ID* field. A
Filter key usually looks like ``lti_store:reference_tool``.

.. note::

   The site operator creates and manages the reusable configuration in Django
   Admin. For LTI 1.3 tools, this includes tool registration values and LTI
   Advantage settings such as Deep Linking, grade services, and Names and Roles.
   If those settings need to change, contact your site operator.

Step 1: Add the LTI Consumer XBlock
***********************************

.. figure:: /_images/educator_how_tos/lti_consumer_xblock_add.png
   :alt: Advanced component picker in Studio showing the LTI Consumer
      component.
   :width: 100%

   Add the LTI Consumer XBlock from the Advanced component list in the course
   unit.

#. In Studio, open the course unit where you want to add the external tool.
#. In the *Add New Component* area, click :guilabel:`Advanced`.
#. Select *LTI Consumer*. Studio adds the LTI Consumer XBlock to the course
   unit.

   .. note::

      For Teak and later releases, the *LTI Consumer* component is visible by
      default. If you do not see *LTI Consumer* in Studio, add
      ``"lti_consumer"`` to the *Advanced Module List* on the *Advanced
      Settings* page. If the list already includes other tools, separate each
      value with a comma.

      If both *LTI Consumer* and the older *LTI* XBlocks appear in Studio,
      select *LTI Consumer*.

#. Edit the XBlock to configure the tool.

Step 2: Configure the Reusable Configuration
********************************************

#. On the *Setup* tab, set *Configuration Type* to *Existing*.
#. Set *LTI Version* to the version used by the reusable configuration.
#. In *LTI Reusability ID*, enter the Filter key provided by your site
   operator.

When *Configuration Type* is set to *Existing*, Studio does not show the tool
credential fields. For LTI 1.3 reusable configurations, Studio also does not
show the *Advantage Settings* tab. Those values come from the reusable
configuration in LTI Store.

Step 3: Configure Review Options
********************************

On the *Review Options* tab, configure the learner-facing behavior for the LTI
component, such as the display name, grading, information sharing, custom
parameters, and appearance.

.. figure:: /_images/educator_how_tos/lti_review_options_xblock.png
   :alt: Review Options tab for an LTI Consumer XBlock in Studio.
   :width: 100%

   Use the Review Options tab to configure learner-facing settings for the LTI
   component.

Common Review Options include:

* *Display Name*
* Grading settings, such as *This activity is graded*, *Grade Weight*, and
  *Accept grades after due date*
* Information sharing settings, such as *Share Username*, *Share Full name*,
  and *Share Email*, when PII sharing is enabled for the course
* Display settings, such as *Hide External Tool*, *Open tool in*, and launch
  button text

Save and Test
*************

#. Select :guilabel:`Save`.
#. Publish the unit.
#. Open the unit in the LMS and launch the LTI tool as a learner and, if
   relevant, as staff or admin.
#. Confirm that the tool opens correctly.
#. If the reusable configuration includes LTI Advantage services, test each
   enabled service. For example, confirm that grades return to the Open edX
   platform or that selected Deep Linking content appears in the course.

.. seealso::

 :ref:`Set up a Reusable LTI Store` (site operator how-to)

 :ref:`Set up an LTI 1_1 component` (how-to)

 :ref:`Set up an LTI 1_3 component` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        | Release        | Test situation                 |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-12-05   | LTI WG                        | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
