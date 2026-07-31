.. _Course Live:

########################################################
Add Live Sessions with an LTI Video Conferencing Tool
########################################################

.. tags:: educator, how-to

Add a **Live** page to your course where you can host video
sessions and learners can join them from the course navigation.

You can currently add Zoom and BigBlueButton for live sessions. Both integrations
use LTI 1.1.

*************************
Find the Live settings
*************************

#. In Studio header, select **Content**, then **Pages & Resources**.

#. On the **Live** card, select the settings icon.

   .. image:: /_images/educator_how_tos/Live_configuration_card.png
      :width: 600
      :alt: The Live card on the Pages & Resources page.

#. Enable **Live** from the toggle on the top right of the settings modal.

#. Select Zoom or BigBlueButton.

   .. image:: /_images/educator_how_tos/Live_app_configuration.png
      :width: 600
      :alt: The Live settings with Zoom selected.

#. Complete the steps for your selected tool.

**************
Configure Zoom
**************

First, create LTI credentials in Zoom:

#. Add the `Zoom LTI Pro app
   <https://marketplace.zoom.us/apps/f8JUB3eeQv2lXsjKq5B2FA>`_ to your Zoom
   account.
#. Open the app configuration and add a credential.
#. Name the credential and select **LTI 1.1**.
#. Copy the generated LTI URL, LTI key, and LTI secret.
#. In the credential settings:

   * Set **Email or Employee Unique ID Attribute Name** to
     ``instructor_email``.
   * Add the domain of your Open edX Learning site to **Approved Domains**.
     For example, use ``learning.example.com`` if that is where you view your
     course.

Then return to the Live settings in Studio:

#. Enter the Zoom values in the matching fields:

   * Enter the LTI key in **Consumer Key**.
   * Enter the LTI secret in **Consumer Secret**.
   * Enter the LTI URL in **Launch URL**.
   * Enter the email address for your Zoom account in **Launch Email**.

#. Select **Save**.

The **Live** page now appears in the course navigation. Course staff can
schedule or start Zoom meetings. Learners can join those meetings.

.. image:: /_images/educator_how_tos/Zoom_in_Live_tab.png
   :width: 600
   :alt: Zoom displayed on the Live page in a course.

*************************
Configure BigBlueButton
*************************

BigBlueButton offers commercial, and self-hosted options. The
configuration shares the usernames and email addresses of learners and course
staff with BigBlueButton.

#. Get LTI credentials from your deployment or hosting provider.

#. In the Live settings, select **BigBlueButton**.

#. From **Select a plan**, select **Commercial/self-hosted**.

#. Enter the LTI credentials.

#. Select **Save**.

For deployment help, see the BigBlueButton documentation:

* `Install BigBlueButton
  <https://docs.bigbluebutton.org/administration/install/>`_
* `Configure the BigBlueButton LTI integration
  <https://docs.bigbluebutton.org/administration/lti/>`_
* `Find a BigBlueButton hosting provider
  <https://bigbluebutton.org/commercial-support/>`_

The **Live** page now appears in the course navigation. Course staff can
create BigBlueButton sessions. Learners can join those sessions.

.. image:: /_images/educator_how_tos/BBB_in_live_tab.png
   :width: 600
   :alt: BigBlueButton displayed on the Live page in a course.


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                      |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------+
| 2026-07-31   | Aamir Ayub                    | Verawood       | `Fail <https://github.com/openedx/xblock-lti-consumer/issues/691>`_|
+--------------+-------------------------------+----------------+--------------------------------------------------------------------+
| 2025-04-13   | Docs WG                       | Sumac          | Pass                                                               |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------+
| 07/03/2025   | Docs WG                       | Sumac          | `Fail <https://github.com/openedx/docs.openedx.org/issues/956>`_   |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------+
