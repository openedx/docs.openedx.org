.. _create-flat-taxonomy:

#########################################
Create a flat taxonomy by uploading a CSV
#########################################

.. tags:: educator, how-to

.. note::

    Users must be organization or instance level administrators in order to
    import taxonomies.

Tags that can be applied to content are organized into hierarchical taxonomies.
Currently, the only way to create or modify a taxonomy is by uploading a CSV or
JSON file.

The simplest type of taxonomy is a flat taxonomy that doesn't have any
hierarchy. For example, if you want to tag the “difficulty” of problems as
either “Easy”, “Medium”, or “Hard”, you could do that by creating a flat
taxonomy. Here's how to do that:

#. Open any spreadsheet application (Excel, Numbers, Google Sheets, etc.) and
   create a new blank spreadsheet. In the first row, add two columns called
   **id** and **value**.

   .. image:: /_images/educator_how_tos/ctag_create_taxonomy_step1.png
      :alt: Screenshot showing new blank spreadsheet with one row and two columns, the first column called id and the second called value.

#. Below that, enter the new tags that you want to create in the “value” column,
   and give each tag an ID in the “id” column. The “id” for each tag is
   required, but mostly relevant when you are aligning your taxonomy with some
   external system that uses IDs for each tag. If you don't have that use case,
   just enter the same text for the id as for the value.

   .. image:: /_images/educator_how_tos/ctag_create_taxonomy_step2.png
      :alt: Screenshot showing a spreadsheet with two columns, the first column called id and the second called value. The same tag values are populated in the id column and the value column. 

#. Save the spreadsheet using the default format, in case you want to edit it
   later.
#. Export the spreadsheet to a CSV file.

   #. In Excel, use File > Save As…, and set the “File format” to “CSV UTF-8
      (comma-delimited) (.csv)” (preferred) or “Comma Separated Values (.csv)”
      then enter a filename and save it.
   #. In Google Sheets, use File > Download > Comma Separated Values (.csv).
   #. In Numbers, use File > Export To > CSV… and use the default options.

#. Import the taxonomy following the :ref:`import-export-taxonomy`  guide.


.. seealso::
 

 :ref:`build-taxonomy-using-template` (how-to)

 :ref:`import-export-taxonomy` (how-to)

 :ref:`Update/Re-import a taxonomy` (how-to)

 :ref:`tag-ids-for-taxonomy-import` (concept)
 
 :ref:`Manage Permissions on a Taxonomy` (how-to)

 :ref:`add-tags-to-a-course` (how-to)

 :ref:`Export tag data from a course` (how-to)

 :ref:`Add and delete tags on course content` (how-to)



**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 07/07/2025   | Leira (Curricu.me)            | Sumac          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
