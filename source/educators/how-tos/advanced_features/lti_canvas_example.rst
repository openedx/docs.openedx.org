.. _Open edX as an LTI Provider to Canvas:

Use Open edX Platform as an LTI Provider to Canvas (Example)
#############################################################

.. tags:: educator, how-to

To use Open edX course content in the Canvas LMS, you add a new app to the course and then add external tool module items.

.. note::

   This example relies on the use of a third-party tool. Because this
   tool is subject to change by its owner, the steps and illustrations provided
   here are intended as guidelines and not as exact procedures.


This guide assumes:

- You have been provided with LTI *Consumer Key* and *Consumer Secret* by your site
  operator (see :ref:`Configuring Credentials for a Tool Consumer`)
- You have constructed URLs for content you want to show in Canvas
  (see :ref:`Determine Content Addresses`)


.. figure:: /_images/educator_how_tos/canvas_add_external_app_modal.png
   :alt: STAFF DEBUG INFO button on the unit page.
   :width: 60%

   Staff Debug Info button is located at the end of every component on the unit page.


.. figure:: /_images/educator_how_tos/canvas_external_app_config_type.png
   :alt: STAFF DEBUG INFO button on the unit page.
   :width: 60%

   Staff Debug Info button is located at the end of every component on the unit page.


.. figure:: /_images/educator_how_tos/canvas_external_app_privacy.png
   :alt: STAFF DEBUG INFO button on the unit page.
   :width: 60%

   Staff Debug Info button is located at the end of every component on the unit page.


Configuring an LTI tool in Canvas has 2 steps:

#. **Tool Configuration**: Establishes the connection between Canvas and
   Open edX using the consumer key, secret, and domain. This is typically done once, at the
   account or course level.

#. **Tool Placement**: How learners reach a specific piece of Open edX content e.g. Modules, Assignments etc.
   A single tool configuration can be "placed" in multiple locations. Instructors can override launch URLs during placement.

Canvas has two roles relevant to these steps:

#. **Account Admin**: Has access to Account Settings and can configure an External Tool at the account level
   which will then be available across all courses in the account. Instructors can place this tool
   anywhere in the course and also override the launch URL.

#. **Instructor**: Has access to Course Settings and can configure an External Tool at the course level
   which will then be available in that course only.


***************************************************
Step 1: Configuring Open edX as an External Tool
***************************************************

Open edX supports **LTI 1.1 only** as a tool provider and we can configure it as
an External Tool in Canvas.

External Tool configuration can be accessed via:

#. Account Nav -> Settings -> Apps if you have an Admin role.

   .. figure:: /_images/educator_how_tos/canvas_external_apps_account_nav.png
      :alt: Screenshot of accessing External Apps page via account navigation.
      :width: 60%

      In account navigation, select Settings and then the Apps tab to access configuration page for External Apps.


#. Course Nav -> Settings -> Apps if you have an Instructor role.

   .. figure:: /_images/educator_how_tos/canvas_external_apps_course_nav.png
      :alt: Screenshot of accessing External Apps page via course navigation.
      :width: 60%

      In course navigation, select Settings and then the Apps tab to access configuration page for External Apps.


.. note::

   Canvas displays an **Apps** item in the account navigation sidebar by default
   for all account admins. This leads to the Apps Hub which supports
   **LTI 1.3 only**. This is not the place where you can configure Open edX.


#. Navigate to External Apps page as described above, via course navigation or account navigation.
   If you configure it at the account level it'll be available in all courses in that account.

#. Click on :guilabel:`+ App`.

#. Select *Configuration Type* As *Manual Entry*. Of the 5 options available, this is the only one
   that allows LTI 1.1 configuration.

#. Add *Name* e.g. *My Open edX instance*.

#. Add *Consumer Key* and *Shared Secret* that you got from your site operator.

#. You can add *Launch URL* now or you can leave it blank and add later during placement. If you add it now, you can override it during placement.

#. In *Domain*, add your Open edX LMS domain, e.g. ``https://openedx.io``.

#. Set *Privacy Level* based on the :ref:`authentication mode <Authentication Modes>` your
   site operator has configured for your Open edX instance.

   #. Select *Anonymous* if your instance is configured to use *Anonymous* mode.

   #. Select *Email Only* if your instance is configured to use *Require Existing Account* mode.

   #. Select *Email Only* or *Public* if your instance is configured to use
   *Auto-Create with Personal Information* mode.

#. Click :guilabel:`Submit`.


**********************************************
Step 2: Add Open edX Content to a your Course
**********************************************

*Done once per piece of content. Requires Teacher role.*

1. In your Canvas course, go to **Modules**
2. Click **+** on the module where you want to add content
3. Select **External Tool** from the item type dropdown
4. Select the Open edX tool configured in Step 1
5. In the **URL** field, paste the LTI content URL for this specific piece
   of content (see *Determining the LTI Content Address*)
6. Check **Load in a new tab**

   .. note::

      Interactive problem components cannot run inside a Canvas iframe.
      Enabling this setting opens content in a new browser tab, which is
      required for learners to interact with problems. Text and video
      components work either way, but enabling it consistently avoids
      unexpected behavior.

7. Give the item a meaningful title and click **Add Item**

****************
Step 3: Verify
****************

1. In your Canvas course, click **Student View** (top right corner)
2. Open the module item you added
3. Confirm the Open edX content loads in a new tab
4. If the content includes graded problems:

   - Submit a response as the student
   - Check the Canvas gradebook — scores sync after a delay
     (default: 15 minutes)

***********
Limitations
***********

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Limitation
     - Detail
   * - **LTI version**
     - Open edX supports LTI 1.1 only as a provider. Canvas's modern Apps Hub requires LTI 1.3 and is not compatible with this integration.
   * - **Compatible content**
     - Not all Open edX content types work via LTI. See *LTI Content Compatibility*.
   * - **Sections**
     - Top-level course sections cannot be shared via LTI. Use subsections, units, or individual components.
   * - **Iframe embedding**
     - Interactive problems require a new tab. Canvas's default iframe embed will prevent learners from submitting responses.
   * - **Hidden content**
     - Open edX "Hide from students" settings are ignored when content is accessed via LTI.
   * - **Enrollment dates**
     - Open edX enrollment and course date restrictions do not apply to LTI-delivered content.
   * - **Grade sync delay**
     - Scores appear in the Canvas gradebook after a delay (15 minutes by default).

.. seealso::

   :ref:`Using Open edX as an LTI Tool Provider` (concept)

   :ref:`Determine Content Addresses when using Open edX as an LTI Provider <Determine Content Addresses>` (how-to)

   :ref:`Content Compatibility for LTI` (reference)

   :ref:`Example - edX as an LTI Provider to Blackboard <Open edX as an LTI Provider to Blackboard>` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-06-04   | MITx                          | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
