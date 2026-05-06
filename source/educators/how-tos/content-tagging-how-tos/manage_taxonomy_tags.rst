.. _manage-taxonomy-tags:

####################
Manage Taxonomy Tags
####################

.. tags:: educator, how-to

This guide describes how to create, organize, and manage tags within a taxonomy using the Taxonomy Detail. A detail page for a taxonomy can be found by navigating to the Taxonomies tab in the Studio, then selecting a taxonomy, which will then show that taxonomy's detail page. 

Taxonomy Tab:

.. image:: /_images/educator_how_tos/taxonomy_tab.png
   :alt: Screenshot of the tabs in Studio home, with an arrow pointing to the Taxonomies tab.

Taxonomy Overview Page:

.. image:: /_images/educator_how_tos/taxonomy_overview_page.png
   :alt: Screenshot of the Taxonomies Overview page showing multiple taxonomies.

Taxonomy Detail Page:

.. image:: /_images/educator_how_tos/taxonomy_detail_page.png
   :alt: Screenshot of the Taxonomies Overview page showing multiple taxonomies.

Overview
********

Tags allow you to organize and label content across:

* Courses
* Course content
* Content libraries

From the Taxonomy Detail page, you can:

* View tag hierarchy
* See usage counts
* Add root-level tags and sub-tags
* Rename existing tags
* Delete tags and sub-tags

View Tag Usage Counts
*********************

Each tag can display a usage count indicating how many unique content objects are associated with it.

How Usage Is Calculated
=======================

Counts include:
  
* Courses
* Course content
* Content library items
  
Both published and unpublished content items are included.

Each object counts once per tag, even if:
  
* Multiple child tags are applied
* The same tag is applied multiple times


Parent Tag Aggregation
======================

Parent tags include usage from all child tags.

Example:

* ``Object A`` is tagged with ``Chemistry``
* ``Object B`` is tagged with ``Physics`` and ``Chemistry``

Parent tag ``Natural Science`` shows a usage count of ``2`` because
``Object A`` and ``Object B`` are each counted once.

.. image:: /_images/educator_how_tos/taxonomy_tag_usage_count.png
   :alt: Screenshot of usage count badges displayed in the taxonomy tag list.

No Usage Display
================

If a tag has no associated content, no usage count is shown.

Add a Root-Level Tag
********************

To create a new top-level tag:

#. Navigate to the Taxonomies page from Studio Home
#. Choose a Taxonomy to add to and select it
#. Select the + (plus) icon at the top of the tag list

   .. image:: /_images/educator_how_tos/taxonomy_add_root_tag_button.png
      :alt: Screenshot of the plus icon used to create a root-level tag.

#. Enter a tag name in the inline input field

   .. image:: /_images/educator_how_tos/taxonomy_add_root_tag_input.png
      :alt: Screenshot of the inline input field for adding a root-level tag.

#. Click Save or press Enter

After the tag is saved, the new tag appears at the top of the list and a
success notification is displayed.

Cancel Tag Creation
==============================

To cancel a tag creation, select Cancel or press Esc. The input
row is removed, and the tag is not created.

   .. image:: /_images/educator_how_tos/taxonomy_cancel_tag.png
      :alt: Screenshot of the cancel button to cancel the process of adding a root-level tag.

Validation Rules
===============================

You cannot save a tag if:

* The input is empty
* The input contains only whitespace
* The name includes invalid characters:

  * Leading or trailing whitespace
  * TAB character
  * > (space-greater-than-space)
  * ; (semicolon) 
  
* The name duplicates an existing tag, regardless of letter casing.

  * Example: “Learning” and “learning” are considered duplicates

Add a Sub-Tag
*************

To create a tag under an existing parent:

#. Locate the parent tag
#. Open the actions menu by selecting the three dots
#. Select Add sub-tag

   .. image:: /_images/educator_how_tos/taxonomy_add_sub_tag_menu.png
      :alt: Screenshot of the Add sub-tag option in the tag actions menu.

#. Enter the sub-tag name

   .. image:: /_images/educator_how_tos/taxonomy_add_sub_tag_input.png
      :alt: Screenshot of the inline input field for adding a sub-tag.

#. Select Save, or press Enter

After the sub-tag is saved, the sub-tag appears directly beneath the parent tag
and is indented to reflect hierarchy.

Cancel Tag Creation
=======================

To cancel tag creation, select Cancel or press Esc. The row is
removed without saving.

Sub-Tag Validation Rules
========================

Sub-tags follow the same rules as root tags:

* No empty or whitespace-only names
* No invalid characters
* No duplicates under the same parent (case-insensitive)

Rename a Tag
************

To rename a tag:

#. Open the actions menu next to the tag by selecting the three dots
#. Select Rename

   .. image:: /_images/educator_how_tos/taxonomy_rename_tag_menu.png
      :alt: Screenshot of the Rename option in the tag actions menu.

#. Edit the tag name inline
#. Select Save, or press Enter

After the tag is renamed:

* The updated name is displayed immediately.
* A success notification appears.
* All tag associations are updated across courses, libraries, and the search
  index.

Cancel Rename
=============

To cancel a rename, select Cancel or press Esc. The original name is
restored, and no changes are saved.

.. note::

   The Save button is disabled until the tag name is changed. Usage counts
   remain unchanged after rename.

Delete a Tag
************

.. warning::

   Deleting a parent tag also deletes its sub-tags. Any uses of the deleted tag
   or its sub-tags are removed from associated content.

Delete a Tag Without Sub-Tags
=============================

To delete a tag that does not have sub-tags:

#. Open the actions menu for the tag
#. Select Delete

   .. image:: /_images/educator_how_tos/taxonomy_delete_tag_menu.png
      :alt: Screenshot of the Rename option in the tag actions menu.
     
#. In the confirmation dialog, type ``DELETE``
#. Confirm deletion

Delete a Tag With Sub-Tags
==========================

To delete a tag that has sub-tags:

#. Open the actions menu for the tag
#. Select Delete
#. Review the warning that sub-tags will also be deleted
#. Type ``DELETE ALL # TAGS``, where ``#`` is the number of tags being deleted
#. Confirm deletion

After deletion:

* The tag is removed
* All sub-tags, if any, are removed
* All tag associations are removed from content
* A confirmation notification is displayed

Keyboard Accessibility
**********************

All workflows support keyboard interaction. Users can:

* Navigate menus using keyboard controls
* Trigger actions such as Rename, Delete, and Add sub-tag
* Save using Enter
* Cancel using Esc

Permissions
***********

Only users with admin permissions can:

* Add root-level tags
* Add sub-tags
* Rename tags
* Delete tags

Users without admin permissions do not see the controls for these actions.

.. seealso::

 :ref:`build-taxonomy-using-template` (how-to)

 :ref:`create-flat-taxonomy` (how-to)

 :ref:`import-export-taxonomy` (how-to)

 :ref:`Update/Re-import a taxonomy` (how-to)

 :ref:`tag-ids-for-taxonomy-import` (concept)

 :ref:`Manage Permissions on a Taxonomy` (how-to)

 :ref:`add-tags-to-a-course` (how-to)

 :ref:`Add and delete tags on course content` (how-to)

 :ref:`Export tag data from a course` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        | Release        | Test situation                 |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-05   | Unicon                        | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
