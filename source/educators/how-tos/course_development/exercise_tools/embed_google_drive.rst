.. _Embed Google Drive Files:

Embedding a Google Drive File in Your Course
##############################################

.. tags:: educator, how-to

To embed a Google Drive file in your course, follow these steps.

.. contents::
   :local:
   :depth: 1

.. _Enable the Google Drive Files Tool:

Enable the Google Drive Files Tool
***********************************

Before you can add Google Drive files to your course, you must enable the
Google Drive tool in Studio or OLX (open learning XML).

To enable the Google Drive tool in Studio, you add the ``"google-document"``
key to the **Advanced Module List** on the **Advanced Settings** page. For
more information, see :ref:`Enable Additional Exercises and Tools`.

Alternatively, you can use OLX to enable the Google Drive tool.

.. _Enable Google Drive Files in OLX:

Enable Google Drive Files in OLX
********************************

To enable Google Drive files in your course, you edit the XML file that
defines the course structure. You locate the ``course`` element's
``advanced-modules`` attribute, and add the string ``google-document``
to it.

For example, the following XML code enables Google Drive files in a course. It
also enables Google calendars.

.. code-block:: xml

  <course advanced_modules="[&quot;google-document&quot;,
      &quot;google-calendar&quot;]" display_name="Sample Course"
      start="2014-01-01T00:00:00Z">
      ...
  </course>

.. _Obtain the Google Drive File Embed Code:

Publish the Google Drive File and Obtain the Embed Code
********************************************************

Before you can add a Google Drive file to your course, you must publish the
file to the web and obtain the embed code for the file.

.. important::
 The task described in this section relies on the use of third-party software.
 Because the software is subject to change by its owner, the steps provided
 here are intended as guidelines and not as an exact procedure.

#. Open the Google Drive file.
#. From the **File** menu, select **Publish to the web**.

   .. image:: /_images/educator_how_tos/google-publish-to-web.png
    :alt: The Google Drive file Publish to the web dialog box.

#. Select **Publish**, and then select **OK** to confirm the action.
#. Select the **Embed** tab.

   .. image:: /_images/educator_how_tos/google-embed.png
    :alt: The Google Drive file Publish to web Embed tab

#. Copy the complete string in the **Embed** field, including the ``<iframe>``
   tags.

   .. note::
    Google images do not have an ``<iframe>`` tag. To embed an image, you copy
    the complete ``img`` tag.

   You use that string to configure the Google Drive file component.

.. seealso::
 :class: dropdown

 :ref:`Google Drive Files Tool` (reference)

 :ref:`Add a Google Drive File to Your Course` (how to)



**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
