.. _Ulmo Libraries:

Library Updates in the Ulmo Release
###################################

Ulmo adds authoring support for Sections and Subsections (also known as
"structural blocks") in Libraries. You can now author all levels of content for
reuse in courses. Included are improvements to syncing changes made in a Content
Library to content that has been reused in courses.

Also new is a method of :ref:`migrating Legacy Library content <Migrating Legacy
Libraries>` to the new Content Libraries experience. Migrated content can be
edited, and changes can be published to courses that used the Legacy Library content.

.. admonition:: Migrate Legacy Libraries

   In Verawood, :ref:`Legacy Libraries <Legacy Content Libraries Overview>` will
   no longer be supported. Migrate legacy libraries to maintain functionality.
   To learn more view the :ref:`Migration documentation <Migrating Legacy
   Libraries>.

Structural Blocks in Libraries
******************************

Content Libraries now support Sections and Subsections authoring. With these
improvements, all levels of content can now be authored in Content Libraries and
reused in courses.

Structural Block Authoring
==========================

Author Sections, Subsections, Units, and content blocks within Libraries.

.. figure:: /_images/release_notes/ulmo/ulmo_libraries_1.png
   :alt: Homepage view of Libraries, showing four Subsections. On the card, the number of units in the subsection is displayed in the bottom right.
   :width: 800

   Homepage View of Libraries

.. figure:: /_images/release_notes/ulmo/ulmo_libraries_2.png
   :alt: A full page view of a Section, with three subsections, within a Content Library
   :width: 800

   Full page view of a Section in a Content Library


Content Library to Course Publishing
====================================

Newly created content or edits can be published via the new publish flow.
Publishes to structural blocks will publish all contained content. For example,
this means publishing a subsection will also publish all the units and content
blocks contained within that subsection.

.. figure:: /_images/release_notes/ulmo/ulmo_libraries_3.png
   :alt: The publishing dialog appears in the right sidebar on a Libraries edit page. The Confirm Publish dialog box at the top of the sidebar explains which of the Section's subsections will be published.
   :width: 800

   View how publishing affects content in the new Publish confirmation

Improvements to Syncing Library Changes to Courses
==================================================

Needs better text & screenshot here - commented on the wiki

Legacy Library Migration
************************

With the new :ref:`migration <Migrating Legacy Libraries>` feature, Legacy
Library content can now be moved into a Content Library. This enables editing,
remixing, and reusing content without breaking courses that used the Legacy
Library. Courses that use Legacy Library content can receive updates made to the
migrated content.

.. note::

   To receive updates in courses that previously used Legacy Library content
   prior to migration, educators must update the references in the courses. To
   learn more, see the :ref:`Legacy Library Migration documentation <Migrating
   Legacy Libraries>`.

.. figure:: /_images/release_notes/ulmo/ulmo_libraries_4.png
   :alt: The new Migrate Legacy Libraries tool, described more in the Legacy Library Migration documentation

   The new Migrate Legacy Libraries tool

Full Documentation
******************

All content management functionality extends to subsections and sections, including:

* Subsections and sections can be :ref:`searched, sorted and filtered <Search
  for content in a Library>`, enabling easy discovery and management

* Subsections and sections can be added to :ref:`collections <Build a Collection
  in a Library>`

* Subsections and sections can be :ref:`tagged <Add and Delete tags in Library
  content>`

* Subsections and sections can be :ref:`published <Publish Library content>`

* Subsections and sections can be :ref:`reused in courses <Add Library content
  to a course>`

* Subsections and sections can be updated in a library and :ref:`synced
  centrally <Sync a Library update to your course>`


.. seealso::

    :ref:`Create and Edit New Subsections and Sections`

    :ref:`Create a New Library`

    :ref:`Create and edit content in a Library`

    :ref:`Create and edit units in a Library`

    :ref:`Migrating Legacy Libraries`


**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-12-12    | Product WG                    | Ulmo           |  Pass                                             |
+--------------+-------------------------------+----------------+---------------------------------------------------+