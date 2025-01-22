.. _Update/Re-import a taxonomy:

Update/Re-import a taxonomy
###########################

In order to update taxonomies, they must be updated locally and re-imported.
This document walks through that process.

Updating a taxonomy locally
***************************

Before a taxonomy can be re-imported, it must be updated locally. Here's how to
do that.

#. Export the taxonomy you wish to update. See :ref:`import-export-taxonomy` for
   instructions on how to export.

#. Open the file locally. It should look like this:

   .. image:: /_images/educator_how_tos/taxonomy-csv-export.png
      :alt: A screenshot showing a CSV export of a taxonomy in Google Sheets. There are three columns labeled "id", "value", and "parent_id".

#. Find the tag value that you wish to modify. Only tags in the “Value” column
   should be changed.

   .. image:: /_images/educator_how_tos/taxonomy-csv-modify-tag.png
      :alt: A screenshot showing a CSV export of a taxonomy in Google Sheets. A value in the second column, labeled "value", is highlighted in yellow.

   .. note::
      
      DO NOT change the tag id. This will render the taxonomy un-usable.
      See :ref:`tag-ids-for-taxonomy-import` for more detail.

#. Once you've finished making changes, export the file as a CSV or JSON file
   and navigate back to the Taxonomy Dashboard.

#. Find the taxonomy you wish to update. Click on the three-dot menu and click
   on :guilabel:`Re-import`:

   .. image:: /_images/educator_how_tos/taxonomy-three-dot-reimport.png
      :alt: A screenshot showing the Re-import option in the three-dot menu from a taxonomy card on Studio Home.

#. You will be prompted with an option to export and save a copy of the taxonomy
   in its current state, before updating it. During the update process, the
   current taxonomy will be replaced with the updated version, and its advisable
   to keep a copy of the current version in case something goes wrong in the
   updating process.

#. After exporting a copy of your taxonomy in its current state, click :guilabel:`Next`.

#. Find your local file, upload, and click :guilabel:`Import`.

#. You will be prompted to accept a list of changes. If everything looks ok,
   click :guilabel:`Continue`:

   .. image:: /_images/educator_how_tos/taxonomy-reimport-diff.png
      :alt: A screenshot showing a pop-up that lists the changes between the current taxonomy and the newly reimported one.

#. You will be prompted with a notification when the re-import is complete.

#. To view your newly imported taxonomy, find the taxonomy card in your taxonomy
   listing and click the title. You will see your taxonomy and all its
   associated tags in the taxonomy view page.

.. seealso::
 :class: dropdown

 :ref:`build-taxonomy-using-template` (how-to)

 :ref:`import-export-taxonomy` (how-to)

 :ref:`Update/Re-import a taxonomy` (how-to)

 :ref:`tag-ids-for-taxonomy-import` (concept)
 
 :ref:`Manage Permissions on a Taxonomy` (how-to)

 :ref:`add-tags-to-a-course` (how-to)

 :ref:`Add and delete tags on course content` (how-to)

 :ref:`create-flat-taxonomy` (how-to)

 