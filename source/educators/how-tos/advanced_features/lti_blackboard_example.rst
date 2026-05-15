.. _Open edX platform as an LTI Provider to Blackboard:

Open edX platform as an LTI Provider to Blackboard
##################################################

.. tags:: educator, how-to


.. note:: This feature has not been recently tested with Blackboard.
          It has been tested with :ref:`Canvas <Open edX platform as an LTI Provider to Canvas>` as of Verawood release.


To use Open edX course content in the Blackboard LMS, you add a new app to the course and then add external tool module items.

.. note:: This example relies on the use of a third-party tool. Because this
  tool is subject to change by its owner, the steps and illustrations provided
  here are intended as guidelines and not as exact procedures.

#. In Blackboard, select your course.

#. From the course control panel, select **Customizations**. In the **Tool
   Availability** section, verify that the LTI tool has been enabled.

#. Open a **Content Area** page, and from the **Build Content** menu select
   **Web Link**.

   .. image:: /_images/educator_references/lti_blackboard_contentarea.png
     :alt: An image of the Blackboard navigation choices from Content Area to
         Build Content to Web Link.

#. On the **Create Web Link** page, enter an identifying name and the URL for
   the edX content you want to include.

   The **URL** is the LTI URL that you determined for the course content.
   

   .. image:: /_images/educator_references/lti_blackboard_create_link.png
     :alt: The Blackboard Create Web Link page with example name and URL
         values.

   For more information, see :ref:`Determine Content Addresses`.

#. Review the content to verify that it appears as you expect.

   .. image:: /_images/educator_references/lti_blackboard_example.png
     :alt: An Open edX platform drag and drop problem shown as part of a course running on a
      Blackboard system.

.. seealso::
 

 :ref:`Using your Open edX instance as an LTI Tool Provider` (concept)

 :ref:`Determine Content Addresses` (how-to)

 :ref:`Content Compatibility for LTI` (reference)

 :ref:`Configuring an Open edX Instance as an LTI Tool Provider` (site-operator)

 :ref:`Open edX platform as an LTI Provider to Canvas` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-12   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-06-04   | MITx                          | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
