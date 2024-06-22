Studio Facelift Release Notes (Redwood)
#######################################

The Product and Engineering teams at Raccoon Gang, OpenCraft, 2U and Axim are
very excited to announce that Studio, the course authoring environment, has
undergone a facelift!

Studio has been redesigned and enhanced, with a number of new features that
significantly improve authoring efficiency.

The redesign revolves around a sleeker, modernized UI. Every page in Studio¹ has
been converted to the Paragon design system. This platform-wide design ensures
cohesion and consistency across every authoring workflow. Additionally, each
Studio page is now an independent Micro-Frontend (MFE), which will make it
easier to continue enhancing and building on these pages in the future.

These Release Notes provide a guided, page-by-page tour through the redesigned
Studio interface, including an overview of new features and enhancements.

All of the Studio pages are part of the Course Authoring Micro-Frontend. They are
enabled as the default experience for Redwood.

*¹ excluding the Unit Page, which will be live in Sumac*

.. toctree::
   :maxdepth: 1

Studio Home Page
****************

Studio Home is the entry point for authors and course teams to the authoring
environment. It has been updated to include a number of new features that make
it easier for course staff and authors to manage their courses and easily find
which course they may want to work in. In particular, enhancements will benefit
course teams that manage large numbers of courses.

IMAGE 1

New functionality
=================

* Search bar
* Course filter
* Course sort
* UI redesign
* Pagination

Details
=======

#. Search bar: Authors can now search for courses in their course lists by using
   free-text keyword searches. Searches apply across course titles and course
   metadata.

#. Filter: Course lists can be filtered by active courses or archived courses.
   Filters can be applied to full course lists or to search results.

#. Sort: Course lists can be sorted alphabetically, by A-Z or Z-A, or by newest
   first or oldest first. Course dates are based on date of course creation.
   Sorts can be applied to full course lists or to search results.

#. UI redesign: Actions that may be taken to courses have been consolidated into
   a three-dot menu. This includes the actions to re-run a course and to view it
   live.

#. Pagination: For course lists that contain more than 50 courses, pagination
   has been introduced to eliminate the need for scrolling.

Course Outline Page
*******************

The Course Outline Page has been updated to include new design elements, such as
clearer grouping of section content.

IMAGE

New functionality
=================

* Three-dot action menus

Details
=======

Three-dot action menus: Each course block - each section, each
subsection and each unit - has a consolidated three-dot menu where all actions
related to the block can be taken. Actions include publishing, configuring,
managing tags, moving, duplicating and copying to clipboard.

IMAGE

Course Updates Page
*******************

The Course Updates Page has a new, user-friendly, WYSIWYG editor for creating
course updates and course handouts. These editors eliminate the need for users
to interact with an html editor and makes it much easier to enhance a text entry
with basic word processing tools.

IMAGE

New functionality
=================

* Full text editors with complete suite of word processing tools

Details
=======

Full text editors: Authors can use a full suite of basic word processing
tools, such as bullet and numbered lists, bold/italic/underline, highlights,
quotes, tables and cells, emoticons, special characters, images and embedded
links. They can also embed html code into a text entry.

IMAGE

Pages & Resources Page
**********************

The Pages & Resources page has been redesigned to allow course teams to turn
certain features on and off via a simple toggle. These toggles replace some
advanced settings, removing the need for course teams to use json fields for
configuring key course features.

IMAGE

New functionality
=================

* Feature tiles
* Configuration toggles

Details
=======

#. Feature tiles: Major features that can be turned on or off at the course
   level each have a newly designed tile. The tiles contain a description of the
   feature and a settings wheel where the feature can be configured for the
   course.

#. Configuration toggles: Each feature can be toggled on or toggled off for the
   course. Configurable features include the learner progress bar, discussions,
   the wiki, the calculator, textbooks, custom pages and ORA settings.

Files Page
**********

The new Files page has been redesigned and enhanced with a number of new
features that make it easier for authors and course teams to manage large sets
of third-party content assets for their courses.

IMAGE

New functionality
=================

* Grid and list view
* Bulk delete
* Download and bulk download
* Search bar
* Filter and sort
* Asset info

Details
=======

#. Grid and list view: Authors can toggle between grid and list views for all of
   their third-party content assets. In the list view, at-a-glance info includes
   file name, file size, file type and access settings.

#. Bulk delete: Authors now have the option to select multiple files at a time,
   or to select all files at a time. Once selected, files can be deleted in
   bulk.

#. Bulk download: Authors now have the option to select multiple files at a
   time, or to select all files at a time. Once selected, files can be
   downloaded in bulk.

#. Search bar: Authors can search for files using a free-text keyword search.
   Searches cover file titles and metadata.

#. Content filter: Content can be filtered by content type (images, documents,
   audio, code and other). It can also be filtered by action/inaction and access
   setting (locked/public). Filters can be applied to full content lists or to
   search results.

#. Content sort: Content can be sorted alphabetically, by newest/oldest, and by
   file size. Sorts can be applied to full content lists or to search results.

#. Asset info: Each third-party content asset now contains a metadata panel,
   which includes a reference link to where the content is being used in the
   course. The panel also includes metadata such as the date added, the file
   size, urls and permissions.

Course Settings Pages
*********************

The following course settings pages have been updated to include new design
elements, such as clearer grouping configuration fields.

Schedule & Details Page
=======================

IMAGE

Grading Page
============

IMAGE

Course Team Page
================

IMAGE

Group Configurations Page
=========================

IMAGE

Advanced Settings Page
======================

IMAGE

Course Import
=============

IMAGE

Course Export
=============

IMAGE
