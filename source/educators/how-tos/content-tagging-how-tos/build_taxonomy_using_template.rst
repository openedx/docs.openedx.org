.. _build-taxonomy-using-template:

#################################
Build a taxonomy using a template
#################################

.. tags:: educator, how-to

Tags that can be applied to content are organized into hierarchical taxonomies.
Currently, the only way to create or modify a taxonomy is by uploading a CSV or
JSON file.

The simplest type of taxonomy is a flat taxonomy that doesn't have any hierarchy -
see :ref:`create-flat-taxonomy` for a simpler procedure to create
such a flat taxonomy. For the purposes of this guide, we'll assume you want to
create a taxonomy of cities, like this:

* United States

  * California

    * Los Angeles

  * New York

    * New York City

* Mexico

  * Mexico City

1. Build a taxonomy using a template
************************************
  
* First, review your proposed taxonomy. Note that each tag must have a unique name (across all levels of the hierarchy). So, for example, we could not have “New York” as both a second-level (state) tag and third-level (city) tag - we have to rename one of them (e.g. “New York City” in this case)

* Navigate to Studio Home > Taxonomies. You should see Download Template in the top right. Click on that button, then select “CSV template”.

  .. image:: /_images/educator_how_tos/ctag_taxonomy_template_step2.png
     :alt: Screenshot clicking Download Template button.

* A file will download automatically. Open it using any spreadsheet application (Excel, Numbers, Google Sheets, etc.).

* It should look like this:

  .. image:: /_images/educator_how_tos/ctag_taxonomy_template_step4.png
     :alt: Image showing a fully-populated spreadsheet with four columns labeled: id, value, parent_id, and comments.

* Select and delete all of the entries except the first row, which contains the headings.

  .. image:: /_images/educator_how_tos/ctag_taxonomy_template_step5.png
     :alt: Image showing an empty spreadsheet with four columns labeled: id, value, parent_id, and comments.

2. Create the first tag
***********************

* Now, you can start to enter the tags that make up the taxonomy. The order doesn’t really matter, except that any tags which come “below” another tag should also be below/after it in the spreadsheet. For our example taxonomy, we shouldn’t put “California” before “United States”, because the “California” tag is below (is a child of) the “United States” tag. 
   
  Each row in the spreadsheet corresponds to one tag. To create the “United States” tag from our example, we’ll put “1” for the ID and “United States” for the value:

  .. image:: /_images/educator_how_tos/ctag_taxonomy_template_first_tag.png
     :alt: Populated spreadsheet with four columns labeled: id, value, parent_id, and comments.

  For a tag like “United States” which is a “root” tag in the taxonomy, we leave “parent_id” empty. We can also leave “comments” empty.

  **Choosing an ID:** The “id” column is required, but its exact value is not particularly important at this stage. The main requirement is that each row (each tag) has a unique ID. (Though remember that the “values” of each row also must be unique.) For learning purposes, feel free to use numbers like 1, 2, 3, 4 as the IDs. You could also just make the “id” the same as the “value” (i.e. put “United States” as both the ID and the value), or make up a short ID like “USA”. To understand more, and learn how IDs play an important role when updating the taxonomy, please read `Why does each tag need an ID when importing a taxonomy <https://docs.openedx.org/en/latest/educators/concepts/advanced_features/why_taxonomy_tag_id.html>`_

  

3. Creating "child" tags
************************

* Now, to add the “California” tag, we put it in the next row. Let’s give it the ID “2” and put the value as “California”. Now, because we want this tag to be a “child” of the “United States” tag in our taxonomy, we also need to set the **parent_id** field. In this case the parent is “United States”, which we gave the ID 1, so we’d put 1 as the parent_id, like this:

  .. image:: /_images/educator_how_tos/ctag_taxonomy_template_childtag1.png
     :alt: Populated spreadsheet with four columns labeled: id, value, parent_id, and comments.

* Likewise, to create “Los Angeles” as a child tag of “California”, we need to give it an ID (say, 3), and set its parent ID to the ID we gave to “California” (in this case, 2).

  .. image:: /_images/educator_how_tos/ctag_taxonomy_template_childtag2.png
     :alt: Populated spreadsheet with four columns labeled: id, value, parent_id, and comments.

  So far, this would result in the following taxonomy:

  * United States

    * California

      * Los Angeles

* Now, continue to add the rest of the tags. You can put notes in the “comments” column if you want; that column and any other columns besides “id”, “value”, and “parent_id” are ignored by the system during import.

  .. image:: /_images/educator_how_tos/ctag_taxonomy_template_childtag3.png
     :alt: Populated spreadsheet with four columns labeled: id, value, parent_id, and comments.

* Save the spreadsheet using the default format (e.g. .xlsx), in case you want to edit it later.

* Export the spreadsheet to a CSV file.

  * In Excel, use File > Save As…, and set the “File format” to “CSV UTF-8 (comma-delimited) (.csv)” (preferred) or “Comma Separated Values (.csv)” then enter a filename and save it.
  * In Google Sheets, use File > Download > Comma Separated Values (.csv).
  * In Numbers, use File > Export To > CSV… and use the default options.

* Import your taxonomy following the How To :ref:`import-export-taxonomy`.

.. seealso::
 :class: dropdown

 :ref: `Add and delete tags on courses` (how-to)

 :ref: `Create a flat taxonomy by uploading a CSV` (how-to) 

 :ref: `Import and export a taxonomy` (how-to)

 :ref: `Update/Re-import a taxonomy` (how-to)

 :ref: `Why does each tag need an ID when importing a taxonomy?` (concept)
 
 :ref: `Manage Permissions on a Taxonomy` (how-to)

 :ref: `Add and delete tags on courses` (how-to)

 :ref: `Export tag data from a course` (how-to)
