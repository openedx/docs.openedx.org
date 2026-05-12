.. _Open edX as an LTI Provider to Canvas:

Open edX as an LTI Provider to Canvas
######################################

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


Configuring an LTI tool in Canvas has 2 steps:

#. Tool Configuration: Establishes the connection between Canvas and
   Open edX using the consumer key, secret, and domain. This is typically done once, at the
   account or course level.

#. Tool Placement: How learners reach a specific piece of Open edX content,
   such as a module item or an assignment. A single tool configuration can be
   "placed" in multiple locations. Instructors can override launch URLs during
   placement.

Canvas has two roles relevant to these steps:

#. Account Admin: Has access to Account Settings and can configure an External Tool at the account level
   which will then be available across all courses in the account. Instructors can place this tool
   anywhere in the course and also override the launch URL.

#. Instructor: Has access to Course Settings and can configure an External Tool at the course level
   which will then be available in that course only.


***************************************************
Step 1: Configuring Open edX as an External Tool
***************************************************

Open edX supports LTI 1.1 only as a tool provider. We can configure it as
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

   Canvas displays an *Apps* item in the account navigation sidebar by default
   for all account admins. This leads to the Apps Hub which supports
   LTI 1.3 only. This is NOT the place where you can configure Open edX.


#. On the External Apps page, click :guilabel:`+ App`. This will open a modal where you
   can add an LTI tool configuration.


   .. figure:: /_images/educator_how_tos/canvas_add_external_app_modal.png
      :alt: The add app modal in Canvas showing configuration fields including
            *Name*, *Consumer Key*, *Shared Secret*, *Launch URL*, *Domain*, and *Privacy*.
      :width: 60%

      The add app modal opens when you click :guilabel:`+ App` on the External
      Apps page. Fill in the fields as described in the steps below.


#. Select *Configuration Type* as *Manual Entry*. Of the 5 options available, this is the only one
   that allows LTI 1.1 configuration.


   .. figure:: /_images/educator_how_tos/canvas_external_app_config_type.png
      :alt: The Configuration Type dropdown in the Add App modal showing five
            options: *Manual Entry*, *By URL*, *Paste XML*, *By Client ID*, and *By LTI
            2 Registration URL*.
      :width: 60%

      The Configuration Type dropdown. Select *Manual Entry* to configure an
      LTI 1.1 tool. The other options do not support LTI 1.1.


#. Enter *Name* e.g. *My Open edX instance*.

#. Enter *Consumer Key* and *Shared Secret* that you got from your site operator.

#. Optionally, enter a *Launch URL*. If left blank, you can enter a URL during
   placement instead. If set here, it can still be overridden during placement.

#. In *Domain*, add your Open edX LMS domain, e.g. ``https://openedx.io``.

#. Set *Privacy Level* based on the :ref:`authentication mode <Authentication Modes>` your
   site operator has configured for your Open edX instance.

   #. Select *Anonymous* if your instance is configured to use *Anonymous* mode.

   #. Select *Email Only* if your instance is configured to use *Require Existing Account* mode.

   #. Select *Email Only* or *Public* if your instance is configured to use
      *Auto-Create with Personal Information* mode.


   .. figure:: /_images/educator_how_tos/canvas_external_app_privacy.png
      :alt: The Privacy dropdown in the Add App modal showing four options:
            Anonymous, Email Only, Name Only, and Public.
      :width: 60%

      The Privacy dropdown controls what learner information Canvas sends to
      Open edX at launch. Select the option that matches the authentication
      mode your site operator has configured.


#. Click :guilabel:`Submit`.


********************************************
Step 2: Add Open edX Content to your Course
********************************************

As an instructor, you can add content to your course using the Open edX
configuration you add in step 1. Let's add content to a module as an example:

#. In your Canvas course, go to *Modules*.

#. Click :guilabel:`+` on the module where you want to add content

#. Select *External Tool* from the item type dropdown.

#. Select the Open edX tool configured in Step 1.

#. In the *URL* field, paste the LTI content URL for this specific piece
   of content (see :ref:`Determine Content Addresses`)

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

   - Check the Canvas gradebook. Scores may sync after a 15min delay (see :ref:`Grade Pass back`).


.. seealso::

   :ref:`Using Open edX as an LTI Tool Provider` (educator)

   :ref:`Determine Content Addresses` (educator)

   :ref:`Content Compatibility for LTI` (educator)

   :ref:`Configuring an Open edX Instance as an LTI Tool Provider` (site-operator)

   :ref:`Open edX as an LTI Provider to Blackboard` (educator)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-12   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-06-04   | MITx                          | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
