.. _Set up an LTI 1_3 component:

Set Up an LTI 1.3 Component
###########################

.. tags:: educator, how-to

This document explains how to configure an LTI 1.3 tool using the
LTI Consumer XBlock.

The LTI 1.3 capability supports tool launch and grade passback from the tool to
the Open edX platform. It also supports the three LTI Advantage services: Deep
Linking, Assignments and Grades Services (AGS), and Names and Roles
Provisioning Service (NRPS).

.. note::

   If your instance has LTI Store enabled, a site operator can create a
   reusable LTI 1.3 configuration for you using the Django admin panel. See
   :ref:`Configure an LTI Tool Using Reusable Configuration`.

Before You Start
****************

.. figure:: /_images/educator_how_tos/lti_1p3_info_exchange.png
   :alt: Information that needs to be exchanged between the tool and the
         Open edX instance.
   :width: 80%

   Configuring an LTI 1.3 tool is a two-way process. You need to configure the
   tool in your Open edX instance and get your instance configured in the tool.

LTI 1.3 setup requires exchanging configuration values between your Open edX
instance and the external tool.

Before you configure the tool, ask the tool vendor or review the tool's
documentation for the following information.

* For the basic LTI 1.3 launch:

  * Tool's Launch URL.
  * Tool's Login URL, sometimes called the OIDC login URL.
  * Redirect URIs.

* For LTI Advantage services:

  * Public key or public keyset URL.
  * Deep Linking launch URL if the tool supports Deep Linking.
  * Whether the tool uses Names and Roles Provisioning Service (NRPS).
  * Whether the tool uses Assignments and Grades Services (AGS) to return
    scores.

* For grading:

  * Whether the tool or activity returns scores to the Open edX platform.
  * If the tool uses AGS to return scores, whether the tool
    needs to manage gradebook columns.

* For user information:

  * Whether the tool requires the learner's username, full name, or email
    address during launch.

After you configure and save the LTI Consumer XBlock, Studio shows values that
the tool will need to register your Open edX instance.

Step 1: Add and Configure the LTI Consumer XBlock
**************************************************

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

Configure Tab: Setup
====================

.. figure:: /_images/educator_how_tos/lti_13_setup_xblock.png
   :alt: Setup tab for an LTI Consumer XBlock with LTI Version set to LTI 1.3.
   :width: 80%

   Use the Setup tab to enter the LTI 1.3 launch values provided by the tool.

Configure the *Setup* tab as per the following table:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Setting
     - Guidance

   * - Configuration Type
     - Selects whether the tool configuration is entered directly in this
       XBlock or an existing configuration is loaded from LTI Store.

       Leave *Configuration Type* set to *New* unless your site operator
       has already created a reusable configuration in LTI Store.

   * - LTI Version
     - Set *LTI Version* to *LTI 1.3*.

   * - Launch URL
     - The URL for the specific tool activity or content the user is trying to
       open. Enter the launch URL you obtained from the tool
       vendor/documentation.

   * - Tool Initiate Login URL (OIDC)
     - The URL where the LMS starts the secure sign-in with the tool. Enter
       the login URL you obtained from the tool vendor/documentation.

   * - Registered Redirect URIs
     - The approved URLs where the LMS is allowed to send the user back to the
       tool after the secure sign-in is complete.

       Enter the values as a JSON list, such as
       ``["https://tool.example.com/launch",
       "https://tool.example.com/deeplink"]``

       If the tool does not require separate redirect URIs, leave this field
       blank. The Open edX platform uses the launch URL and, when configured,
       the Deep Linking Launch URL as defaults.

   * - Next
     - Click :guilabel:`Next` to save and continue.

Configure Tab: Advantage Settings
=================================

The *Advantage Settings* tab appears only for LTI 1.3 tools.

.. figure:: /_images/educator_how_tos/lti_13_advantage_settings_xblock.png
   :alt: Advantage Settings tab for an LTI Consumer XBlock in Studio.
   :width: 80%

   Use the Advantage Settings tab only when the LTI 1.3 tool supports LTI
   Advantage services.

Configure the *Advantage Settings* tab as per the following table:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Setting
     - Guidance

   * - Deep linking
     - Deep linking enables course teams to select content offered by the tool
       from within Studio.

       By default, *Deep linking* is *Disabled*. Enable this setting
       if the tool supports it.

   * - Deep Linking Launch URL
     - Enter the Deep Linking launch URL provided by the tool.

       This field is required and only appears when *Deep linking* is
       *Enabled*.

   * - Assignment and Grades
     - Assignment and Grade Services (AGS) allows the tool to send grades to
       the LMS and manage gradebook columns.

       *Declarative* (default): The Open edX platform creates a gradebook
       column (line item) automatically and shares it with the tool during
       launch.

       *Programmatic*: The Open edX platform does not create a gradebook column
       automatically but allows the tool to create and manage columns (line
       items).

       Set to *Disabled* if the tool does not support AGS.


   * - Names & Roles (NRPS)
     - Names and Role Provisioning Services (NRPS) allows the tool to access
       enrollment and role information.

       It is disabled by default. Enable this setting only if the tool requires
       enrollment or role information from the Open edX platform.

   * - Tool Public Key Mode
     - Appears when any LTI Advantage service is enabled.

       Choose how the Open edX platform gets the tool's public key for
       validating LTI Advantage requests from the tool. Select *Keyset URL* if
       the tool provides a JWKS or keyset URL. Use *Public Key* only when the
       tool provides a static public key.

   * - Tool Public Key
     - Appears when *Tool Public Key Mode* is set to *Public Key*.

       Enter the public key provided by the tool. The key usually starts with
       ``-----BEGIN PUBLIC KEY-----``.

   * - Tool Keyset URL
     - Appears when *Tool Public Key Mode* is set to *Keyset URL*.

       Enter the tool's JWKS or keyset URL. Use this option when available
       because it supports key rotation without updating the component.

   * - Next
     - Click :guilabel:`Next` to save and continue.


Configure Tab: Review Options
=============================

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


.. _Register your Open edX instance with the Tool:

Step 3: Register your Open edX instance with the Tool
*****************************************************

LTI 1.3 setup requires registration in both systems. You enter the tool's
values in the LTI Consumer XBlock, and the external tool also needs values from
your Open edX instance.

After you save the LTI Consumer XBlock, Studio shows the Open edX instance
values that the external tool will need.

.. figure:: /_images/educator_how_tos/lti_xblock_13_values.png
   :alt: LTI Consumer XBlock showing the values an external tool needs to register the Open edX instance.
   :width: 80%

Common Open edX platform values required by LTI 1.3 tools include:

* Issuer (your instance domain e.g. https://openedx.io)
* Client ID
* Deployment ID
* Keyset URL
* Access Token URL
* Login URL

External tools may use different names for these values and may not require
all of them. Follow the tool vendor's instructions.

Step 4: Use Deep Linking to Select Tool Content
***********************************************


.. figure:: /_images/educator_how_tos/lti_xblock_deeplink.png
   :alt: Deep Linking Launch - Configure tool link in the LTI Consumer XBlock.
   :width: 80%

   Use the configure tool link to launch the external tool's content
   selection workflow.

If you enabled *Deep linking* for the component, use these steps to select content:

#. In Studio, open the unit containing the XBlock you just configured.
#. Click the :guilabel:`Deep Linking Launch - Configure tool` link on the XBlock.
#. Select the content in the external tool.
#. When the tool redirects back to Studio, confirm that the selected content is
   configured for the XBlock. Details of the content will appear on the XBlock in
   Studio.

   .. figure:: /_images/educator_how_tos/lti_xblock_deeplink_success.png
      :alt: Deep Linking Launch - Configure tool link in the LTI Consumer XBlock.
      :width: 80%

      Use the configure tool link to launch the external tool's content
      selection workflow.

#. Open the unit in the LMS and confirm that the selected content appears.


Publish and Test
*****************

#. Publish the unit.
#. Open the unit in the LMS and launch the LTI tool as a learner and, if
   relevant, as staff or admin.
#. Confirm that the tool opens correctly.
#. If the component is graded, confirm that scores return to the Open edX
   platform as expected.

.. note::

   LTI 1.3 launches work only with published blocks and only from the LMS,
   not Studio. Publish the unit before launching the tool.



.. seealso::
 
 :ref:`About the LTI Component` (concept)

 :ref:`Set up an LTI 1_1 component` (how-to)

 :ref:`Configure an LTI Tool Using Reusable Configuration` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)


**Maintenance chart**

+-------------+------------------------+---------+----------------+
| Review Date | Working Group Reviewer | Release | Test situation |
+-------------+------------------------+---------+----------------+
|             |                        |         |                |
+-------------+------------------------+---------+----------------+
