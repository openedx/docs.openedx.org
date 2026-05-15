.. _Open edX platform as an LTI Provider to Canvas:

Open edX platform as an LTI Provider to Canvas
###############################################

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


Configuring an LTI tool in Canvas has two steps:

#. **Tool Configuration**: Establishes the connection between Canvas and
   your Open edX instance using the consumer key, secret, and domain. This is
   typically done once, at the account or course level.

#. **Tool Placement**: How learners reach a specific piece of Open edX content,
   such as a module item or an assignment. A single tool configuration can be
   reused in multiple locations. Instructors can override launch URLs during
   placement.

Canvas has two roles relevant to these steps:

#. **Account Admin**: Has access to Account Settings and can configure an External Tool at the account level
   which will then be available across all courses in the account. Instructors can place this tool
   anywhere in the course and also override the launch URL.

#. **Instructor**: Has access to Course Settings and can configure an External Tool at the course level
   which will then be available in that course only.


**************************************************************
Step 1: Configuring your Open edX instance as an External Tool
**************************************************************

The Open edX platform supports LTI 1.1 only as a tool provider. You can configure it as
an External Tool in Canvas.

#. Navigate to the External Apps page:

   #. Account Nav → Settings → Apps if you have an Admin role.

      .. figure:: /_images/educator_how_tos/canvas_external_apps_account_nav.png
         :alt: Screenshot of accessing External Apps page via account navigation.
         :width: 100%

         In account navigation, select Settings and then the Apps tab to access configuration page for External Apps.


   #. Course Nav → Settings → Apps if you have an Instructor role.

      .. figure:: /_images/educator_how_tos/canvas_external_apps_course_nav.png
         :alt: Screenshot of accessing External Apps page via course navigation.
         :width: 100%

         In course navigation, select Settings and then the Apps tab to access configuration page for External Apps.


   .. note::

      Canvas displays an *Apps* item in the account navigation sidebar by default
      for all account admins. This leads to the Apps Hub which supports
      LTI 1.3 only. This is not the place where you can configure your Open edX instance.


#. On the External Apps page, click :guilabel:`+ App`. This will open a modal where you
   can add an LTI tool configuration.


   .. figure:: /_images/educator_how_tos/canvas_add_external_app_modal.png
      :alt: The add app modal in Canvas showing configuration fields including
            *Name*, *Consumer Key*, *Shared Secret*, *Launch URL*, *Domain*, and *Privacy*.
      :width: 100%

      The add app modal opens when you click :guilabel:`+ App` on the External
      Apps page. Fill in the fields as described in the steps below.


#. Select *Configuration Type* as *Manual Entry* which is the only option that supports LTI 1.1.


   .. figure:: /_images/educator_how_tos/canvas_external_app_config_type.png
      :alt: The Configuration Type dropdown in the Add App modal showing five
            options: *Manual Entry*, *By URL*, *Paste XML*, *By Client ID*, and *By LTI
            2 Registration URL*.
      :width: 30%

      The Configuration Type dropdown. Select *Manual Entry* to configure an
      LTI 1.1 tool. The other options do not support LTI 1.1.


#. Enter a *Name*, e.g. *My Open edX instance*.

#. Enter *Consumer Key* and *Shared Secret* provided by your site operator.

#. Optionally, enter a *Launch URL*. If left blank, you can enter a URL during
   placement instead. If set here, it can still be overridden during placement.

#. In *Domain*, enter your Open edX instance domain, e.g. ``openedx.io``.

#. Set *Privacy Level* based on the :ref:`authentication mode <Authentication Modes>` your
   site operator has configured for your Open edX instance.

   #. Select *Anonymous* if your instance is configured to use *Anonymous* mode.

   #. Select *Email Only* if your instance is configured to use *Require Existing Account* mode.

   #. Select *Email Only* or *Public* if your instance is configured to use
      *Auto-Create with Personal Information* mode.


   .. figure:: /_images/educator_how_tos/canvas_external_app_privacy.png
      :alt: The Privacy dropdown in the Add App modal showing four options:
            Anonymous, Email Only, Name Only, and Public.
      :width: 40%

      The Privacy dropdown controls what learner information Canvas sends to
      your Open edX instance at launch. Select the option that matches the authentication
      mode your site operator has configured.


#. Click :guilabel:`Submit`.


********************************************
Step 2: Add Open edX Content to your Course
********************************************

As an instructor, you can add content from your Open edX instance you configured
in step 1, to your course. Follow these steps to add content to a module.

#. In your Canvas course, go to *Modules*.

#. Click :guilabel:`+` on the module where you want to add content.

#. Select *External Tool* from the item type dropdown.

#. Select the Open edX tool configured in Step 1.

#. In the *URL* field, paste the LTI content URL for this specific piece
   of content (see :ref:`Determine Content Addresses`).

#. Check *Load in a new tab*.

   .. note::

      Interactive problem components cannot run inside a Canvas iframe.
      Enabling this setting opens content in a new browser tab, which is
      required for learners to interact with problems. Text and video
      components work either way.

#. Enter the content page name and click :guilabel:`Add Item`.


****************
Step 3: Verify
****************

#. In your Canvas course, click :guilabel:`Student View` (top right corner).

#. Open the module item you added.

#. Confirm the Open edX content loads in the same or a new tab (depending on your configuration).

#. If the content includes graded problems:

   - Submit a response as the student.

   - Check the Canvas gradebook. Scores may sync after a 15-minute delay (see :ref:`Grade Passback`).


.. seealso::

   :ref:`Using your Open edX instance as an LTI Tool Provider` (concept)

   :ref:`Determine Content Addresses` (how-to)

   :ref:`Content Compatibility for LTI` (reference)

   :ref:`Configuring an Open edX Instance as an LTI Tool Provider` (site-operator)

   :ref:`Open edX platform as an LTI Provider to Blackboard` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-12   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-06-04   | MITx                          | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
