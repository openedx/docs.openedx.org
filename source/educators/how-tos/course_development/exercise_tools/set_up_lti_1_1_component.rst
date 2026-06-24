.. _Set up an LTI 1_1 component:
.. _Set up an LTI 1_1 tool:

Set Up an LTI 1.1 Tool
######################

.. tags:: educator, how-to

This document explains how to configure an LTI 1.1 or LTI 1.2 tool using the
LTI Consumer XBlock.

The LTI 1.1/1.2 capability supports tool launch and grade passback from the
tool to the Open edX platform.
It does not support LTI Advantage services.

Before you start, you need this information from your tool:

* Launch URL
* Consumer key
* Shared secret

Setting up an LTI 1.1/1.2 tool is a two-step process:

#. Create an *LTI Passport* for the tool in your course.
#. Add an LTI Consumer XBlock to the course unit and configure it to use that
   passport.


.. note::

   If your instance has LTI Store enabled, a site operator can create a
   reusable LTI 1.1/1.2 configuration for you. See :ref:`Set up an LTI tool
   using a reusable configuration`. In that case, instead of an LTI passport,
   you configure the LTI Consumer XBlock to use the reusable configuration.


Step 1: Create an LTI Passport
******************************

An LTI passport holds the tool's credentials. It has three parts separated by
colons:

.. code-block:: text

   {LTI passport ID}:{Consumer key}:{Shared secret}


.. figure:: /_images/educator_how_tos/lti_passport.png
   :alt: Advanced Settings page in Studio showing the Lti passports field.
   :width: 80%

   Add the tool's LTI passport to the course advanced settings before
   configuring the LTI Consumer XBlock.


To add the LTI passport to your course, follow these steps.

#. In Studio, navigate to the *Advanced Settings* page from the *Settings*
   menu.
#. Locate the *Lti passports* field.
#. Choose an ID for your passport. This is an identifier that
   connects the LTI Consumer XBlock to the passport you are creating now.
#. Add the passport string, as described above, in the *Lti passports* field.

   For example:

   .. code-block:: json

      [
        "saLTIre:jisc.ac.uk:secret"
      ]

#. If the course has multiple LTI passports, separate each passport string
   with a comma.
#. Select :guilabel:`Save Changes`.


Step 2: Add and Configure the LTI Consumer XBlock
*************************************************

.. figure:: /_images/educator_how_tos/lti_consumer_xblock_add.png
   :alt: Advanced component picker in Studio showing the LTI Consumer
      component.
   :width: 80%

   Add the LTI Consumer XBlock from the Advanced component list in the course
   unit.


#. In Studio, open the course unit where you want to add the external tool.
#. In the *Add New Component* area, click :guilabel:`Advanced`.
#. Select *LTI Consumer*. Studio adds the LTI Consumer XBlock to the course
   unit.
#. Edit the XBlock to configure the tool.


.. note::

  For Teak and later releases, the *LTI Consumer* component is visible by
  default. If you do not see *LTI Consumer* in Studio, add
  ``"lti_consumer"`` to the *Advanced Module List* on the *Advanced
  Settings* page. If the list already includes other tools, separate each
  value with a comma.

  If both *LTI Consumer* and the older *LTI* XBlocks appear in Studio,
  select *LTI Consumer*.


Configure the Setup Tab
=======================

.. figure:: /_images/educator_how_tos/lti_11_ontheblock_config.png
   :alt: Setup tab for an LTI Consumer XBlock with LTI Version set to LTI
      1.1/1.2.
   :width: 80%

   Use the Setup tab to select the LTI passport ID and enter the tool launch
   URL.

Configure the *Setup* tab as per the following table:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Setting
     - Guidance

   * - Configuration Type
     - Selects whether the tool configuration is entered directly in this
       XBlock or an existing configuration is loaded from LTI Store.

       Leave *Configuration Type* set to *New* unless your site operator has
       already created a reusable configuration in LTI Store.

   * - LTI Version
     - Leave *LTI Version* set to *LTI 1.1/1.2*.

   * - LTI Passport ID
     - Select the ID of the passport you just created.

   * - LTI URL
     - Enter the tool launch URL.

   * - Next
     - Click :guilabel:`Next` to continue.


Configure the Review Options Tab
================================

On the *Review Options* tab, configure the learner-facing behavior for the LTI
component, such as the display name, grading, information sharing, custom
parameters, and appearance.

.. figure:: /_images/educator_how_tos/lti_review_options_xblock.png
   :alt: Review Options tab for an LTI Consumer XBlock in Studio.
   :width: 80%

   Use the Review Options tab to configure learner-facing settings for the LTI
   component.


Configure the *Review Options* tab as per the following table:


.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Setting
     - Guidance

   * - Display Name
     - Enter a title for this component so users can identify the activity in
       the course.

   * - This activity is graded
     - Controls whether the component can receive a numerical score from the
       LTI tool.

       Set this to *Graded* if you are expecting the tool to return
       scores to your Open edX instance.

   * - Grade Weight
     - Sets the number of points possible for the activity.

   * - Accept grades after due date
     - Controls whether the LTI tool can send grades after the due date.

   * - Share Username, Share Full Name, and Share Email
     - These settings control whether the learner's username, full name, or
       email address is sent to the tool during LTI launch. They appear only
       when a site operator has enabled PII sharing for the course. For more
       information, see :ref:`Allow sharing PII to LTI Components`.

   * - Data Sharing Notice
     - A notice that appears before launch when any information-sharing setting
       is enabled. For more information, see :ref:`Allow sharing PII to LTI
       Components`.

   * - Custom Parameters
     - Sends custom parameters during tool launch.

       If the tool requires custom parameters, enter each parameter as
       ``{key}={value}`` in a JSON list. For example,
       ``["page=144", "activity=quiz"]``.

   * - Send extra parameters
     - Leave this setting unchanged unless the tool's instructions ask you to
       change it.

   * - Hide External Tool
     - Controls whether the LTI tool is visible to learners.

       Set this to *True* for hidden tool launches, such as launches used only
       for grade synchronization. Leave this to *False* to display the tool to
       learners.

   * - Open tool in
     - Controls how the course page opens and displays the LTI tool. Options
       include *Inline*, *Modal*, and *New Window*.

   * - Inline Height (px)
     - Sets the height of the inline tool frame in pixels when *Open tool in*
       is set to *Inline*.

   * - Modal Height (%)
     - Sets the height of the modal window as a percentage of the visible
       browser window height. Appears when *Open tool in* is set to *Modal*.

   * - Modal Width (%)
     - Sets the width of the modal window as a percentage of the browser
       window width. Appears when *Open tool in* is set to *Modal*.

   * - Launch Button Text
     - Sets the custom label for the button that opens the LTI tool. Appears
       when *Open tool in* is set to *Modal* or *New Window*.

   * - Save
     - Click :guilabel:`Save` to save all configurations.


.. note::

   Open edX can receive and store a score for the LTI Consumer XBlock only when
   *This activity is graded* is set to *Graded*. For the stored score to
   contribute to the learner's course grade, the unit must also be part of a
   graded subsection.

Publish and Test
****************

#. Publish the unit.
#. Open the unit in the LMS and launch the LTI tool as a learner and, if
   relevant, as staff or admin.
#. Confirm that the tool opens correctly.
#. If the component is graded, confirm that scores return to the Open edX
   platform as expected.


.. figure:: /_images/educator_how_tos/lti_11_saltire_launch.png
   :alt: An LTI tool launched from an Open edX course unit in the LMS using LTI
      1.1.
   :width: 80%

   After publishing the unit, launch the tool from the LMS to confirm that the
   LTI 1.1/1.2 configuration works.


.. seealso::

 :ref:`About the LTI Component` (concept)

 :ref:`Set up an LTI 1_3 tool` (how-to)

 :ref:`Set up an LTI tool using a reusable configuration` (how-to)


**Maintenance chart**

+-------------+------------------------+---------+----------------+
| Review Date | Working Group Reviewer | Release | Test situation |
+-------------+------------------------+---------+----------------+
|             |                        |         |                |
+-------------+------------------------+---------+----------------+
