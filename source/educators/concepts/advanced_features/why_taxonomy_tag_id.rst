.. _tag-ids-for-taxonomy-import:

Why does each tag need an ID when importing a taxonomy?
#######################################################

When creating a taxonomy via import, or updating one via re-import, the “id”
column is required. In addition, it must be unique for every row. There are two
reasons why such IDs are required.

Renaming tags
*************

First, the IDs allow you to rename tags. When you upload a new version of the
taxonomy, the IDs are compared to determine when a tag has been renamed or
deleted.

For example, if you uploaded this taxonomy and used it to tag content in your
courses:

+---------------+--------------------------------------------------------------+
| **ID**        | **Value**                                                    |
+---------------+--------------------------------------------------------------+
| 1             | *Untied* States                                              |
+---------------+--------------------------------------------------------------+
| 3             | *Canadia*                                                    |
+---------------+--------------------------------------------------------------+

Then you fixed the spelling to create this new version of the taxonomy, and re-imported it:

+---------------+--------------------------------------------------------------+
| **ID**        | **Value**                                                    |
+---------------+--------------------------------------------------------------+
| 1             | United States                                                |
+---------------+--------------------------------------------------------------+
| 17            | Canada                                                       |
+---------------+--------------------------------------------------------------+

You would find that your "*Untied* States" content would be properly tagged as
"United States", while your "*Canadia*" content would be entirely untagged. Why?

Because the ID of the first tag is the same (1), any content that was tagged
with “*Untied* States” will now be fixed to show “United States”. But because the
ID of the second tag has been changed, it is treated as a totally new tag - all
instances of the *"Canadia"* tag will be deleted, and a new “Canada” tag will be
created in the taxonomy, but no content will have that tag yet.

By keeping the ID the same (or not), you can control what will happen with new
versions of the taxonomy - adding, renaming, moving, and deleting tags as
needed. (Note that during the re-import workflow, you'll get a chance to preview
what changes will be applied before you finalize the update. That's a good time
to double-check that the right thing - rename or delete - is about to happen.) 

If in doubt, a good rule of thumb is to **never change the ID once a tag has been
created**, unless you're certain you want to delete all occurrences of that tag
and re-create a new similar tag from scratch. If a tag's ID is wrong and you
need to replace it without losing the tag, see `Changing a tag's ID`_.

Changing a tag's ID
*******************

To give an existing tag a new ID, add a ``previous_id`` column to the import
file. Put the tag's current ID in ``previous_id`` and the new ID in ``id``. On
re-import, the tag keeps its content tags and gets the new ID.

+-------------------+---------------+----------------------------------------------+
| **previous_id**   | **ID**        | **Value**                                    |
+-------------------+---------------+----------------------------------------------+
| 3                 | 17            | Canada                                       |
+-------------------+---------------+----------------------------------------------+

In this example, the tag with ID ``3`` is renamed to ID ``17`` and keeps its
content tags, instead of being deleted and re-created.

The ``previous_id`` column is used only during import; exported files do not
include it. A row that does not use ``previous_id`` cannot take an ID that
another row in the same file is renaming away from.

In the Studio REST API, a tag's ID is its ``external_id`` field.

Matching external systems/taxonomies
************************************

Secondly, the IDs can be used to keep your taxonomy in sync with an external
system.

For example, you could have an airports taxonomy:

+---------------+--------------------------------------------------------------+
| **ID**        | **Value**                                                    |
+---------------+--------------------------------------------------------------+
| ORD           | Chicago O'Hare International Airport                         |
+---------------+--------------------------------------------------------------+
| LAS           | Harry Reid International Airport                             |
+---------------+--------------------------------------------------------------+
| LAX           | Los Angeles International Airport                            |
+---------------+--------------------------------------------------------------+
| BOS           | Boston Logan International Airport                           |
+---------------+--------------------------------------------------------------+

In this case, using the airport codes as the ID makes it easy to align the tags
with other systems that reference airports, accounting for the fact that some
airport names may be different (e.g. the Boston airport may be called “General
Edward Lawrence Logan International Airport” or “Logan Airport”; the “Harry Reid
International Airport in Las Vegas” was previously known as “McCarran
International Airport”; etc.)

As another example, learning outcome standards often have unique identifiers
assigned to individual concepts. For example, the mathematics skill “`Extend The
Properties Of Exponents To Rational Exponents`_” has the ID “HS.N-RN.A.1“, which
can be used to cross-reference it across various systems and publications. If
you are creating a taxonomy related to learning outcomes, you can use these
unique identifiers as the IDs.

.. _Extend The Properties Of Exponents To Rational Exponents: https://tools.achievethecore.org/coherence-map/HS/N/118/633/632/

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
