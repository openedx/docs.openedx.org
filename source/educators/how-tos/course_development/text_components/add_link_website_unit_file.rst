.. _Add Link to Website Course Unit or File:

#############################################
Add Link to Website, Course Unit, or a File
#############################################

.. tags:: educator, how-to

.. _Add a Link in a Text Component:

******************************
Add a Link in a Text Component
******************************

When you use the visual editor, to add a link to a website, course unit, or
file in a Text component, you work with the **Insert link** dialog box.

For more information, see the following tasks.

* :ref:`Add a Link to a Website`
* :ref:`Add a Link to a Course Unit`
* :ref:`Add a Link to a File`

.. _Add a Link to a Website:

=======================
Add a Link to a Website
=======================

#. Select the text that you want to use as the link text.

#. Select the link icon in the toolbar.

#. In the **Insert/Edit link** dialog box, enter the URL of the website that
   is the destination for your link in the **URL** field.

#. If you want the link to open in a new window, select the dropdown arrow
   next to the **Open Link In...** field, and then select **New Window**.
   If not, you can leave the default value.

#. Select **OK**.

#. Save the Text component.

#. To test the link, select **View Live Version** or **Preview**. When the unit
   opens in the LMS, select the linked text and verify that the correct website
   opens.

.. _Add a Link to a Course Unit:

===========================
Add a Link to a Course Unit
===========================

.. note::
  When you create a link to another component, the unit of that destination
  component must be published for the link to work.

#. Obtain the location ID of the unit you want to link to.

   #. In Studio, open the page for the unit that you want to link to in Studio,
      and then locate **Unit Location** in the right pane.

   #. Under **Unit Location**, select and copy the alphanumeric text in the
      **Location ID** field.

      .. image:: /_images/educator_references/UnitIdentifier.png
       :alt: The **Unit Location** area in the right pane of a unit page, with
           the unit's location ID circled.

#. Open the Text component where you want to add the link.

#. Select the text that you want to make into the link.

#. Select the link icon in the toolbar.

#. In the **Insert link** dialog box, enter a value that resembles the
   following value in the **URL** field.

   ``/jump_to_id/<location ID>``

   Make sure to replace <location ID> (including the brackets) with the
   location ID that you copied in step 1, and make sure that you include both
   forward slashes (/).

  .. caution::
    Ensure you use ``/jump_to_id/<location ID>`` as the URL value. Do not
    use the URL of the unit that you see in the browser address bar.  If you do
    not use ``/jump_to_id/<location ID>``, the link will be broken if you
    export and then import the course.

#. If you want the link to open in a new window, select the dropdown arrow
   next to the **Open Link In...** field, and then select **New Window**. If
   not, you can leave the default value.

#. Select **Insert**.

#. Save the Text component and test the link.

.. _Add a Link to a File:

====================
Add a Link to a File
====================

.. tip::
 When you add links to files, open the Text component and the **Files &
 Uploads** page in separate browser windows. You can then more quickly copy
 file URLs.

You can add a link in a Text component to any file that is uploaded for the
course. For more information about uploading files, see :ref:`Add Files to a
Course`.

.. note::
 Do not use this method to add images to Text components. Instead, use the
 method in :ref:`Add an Image to a Text Component`.


#. On the **Files & Uploads** page, locate the file that you want, and then
   select **Studio** in the **Copy URLs** column.

  .. note::
   You must use the **Studio** URL to link to the file, not the **Web** URL.
   For more information, see :ref:`Add Files to a Course`.

#. In the Text component where you want to add the link, select the text that
   you want to make into the link.

#. In the toolbar, select the link icon.

#. In the **Insert link** dialog box, paste the Studio URL for the file in the
   **URL** field. For example, the URL might resemble the following URL.

   ``/static/FileName.pdf``

   Make sure that you include both forward slashes (/).

#. (optional) If you want the link to open in a new window, select the dropdown
   arrow next to the **Open Link In...** field, and then select **New Window**.
   If not, you can leave the default value.

#. Select **OK**.

#. Save the Text component and test the link.

.. seealso::
 :class: dropdown

 :ref:`Working with Text Components` (reference)

 :ref:`Create a Text Component` (how-to)

 :ref:`Paste without Formatting in a Text Component` (how-to)

 :ref:`Add an Image to a Text Component` (how-to)

 :ref:`Work with HTML code` (how-to)

 :ref:`Work with Latex Code` (how-to)

