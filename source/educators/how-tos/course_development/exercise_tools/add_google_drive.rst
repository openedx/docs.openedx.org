.. _Add a Google Drive File to Your Course:

Add a Google Drive File to Your Course
##########################################

.. tags:: educator, how-to

To add a Google Drive file in the course body, you create an advanced
component in Studio or create a Google Document XBlock in OLX.

.. _Add a Google Drive File Component in Open edX Studio:

Add a Google Drive File Component in Open edX Studio
******************************************************

Ensure you :ref:`enable Google Drive files<Enable the Google Drive Files Tool>`
before you add the component.

To add a Google Drive file component, follow these steps.

#. On the Course Outline page, open the unit where you want to add the Google
   Drive component.

#. Under **Add New Component**, select **Advanced**, and then select **Google
   Document**.

   The new component is added to the unit, with the default Google presentation
   embedded.

#. In the new component, select **Edit**.

#. In the **Display Name** field, enter the name for the component.

#. In the **Embed Code** field, paste the embed code you copied in the
   :ref:`Obtain the Google Drive File Embed Code` task.

#. Select **Save**.

You can then :ref:`Preview Unpublished Content` to see how the unit with the
Google drive file will appear to learners.

.. _Add a Google Drive File XBlock in OLX:

Add a Google Drive File XBlock in OLX
*******************************************

To add a Google Drive file XBlock in OLX, you create the
``google-document`` element. You can embed the ``google-document``
element in the ``vertical`` element, or you can create the
``google-document`` element as a stand-alone file you reference
in the vertical.

For example:

.. code-block:: xml

  <google-document url_name="c5804436419148f68e2ee44abd396b12"
    embed_code="&lt;iframe
    frameborder=&quot;0&quot; src=&quot;https://docs.google.com/spreadsheet/pub
    ?key=0AuZ_5O2JZpH5dGVUVDNGUE05aTFNcEl2Z0ZuTUNmWUE&amp;output=html&amp;widge
    t=true&quot;&gt;&lt;/iframe&gt;" display_name="Google Document"/>

The value of the ``embed_code`` attribute is the embed code you copied in the
:ref:`Obtain the Google Drive File Embed Code` task.

.. note::
  The Open edX LMS sets the height and width values for
  Google Drive files. If you add these attributes, the LMS overrides your
  changes.

.. seealso::
 

 :ref:`Google Drive Files Tool` (reference)

 :ref:`Embed Google Drive Files` (how to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
