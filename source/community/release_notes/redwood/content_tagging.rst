.. _Content Tagging Release Notes (Redwood):

Content Tagging Release Notes (Redwood)
#######################################

The Product and Engineering Teams at OpenCraft and Axim are thrilled to announce
the release of Content Tagging!

.. contents::
  :local:
  :depth: 1

What is Content Tagging?
************************

With the Content Tagging feature, course authors and instructional designers are
able to add tags to their course content. This includes the ability to tag full
courses; individual blocks like problems and videos; and segments of the course
like units, subsections or sections.

   .. image:: /_images/release_notes/redwood/tagging_tag_drawer_course_outline.png


Tags are organized into structured taxonomies, or controlled vocabularies. The
platform supports the use of any third-party taxonomy, which means that course
administrators and subject matter experts are free to use any taxonomies they
wish. Administrators and SMEs can also create their own taxonomies. 

Taxonomies are uploaded to the platform as CSV or JSON files, and permissions
can be set at the organization or instance level. Once applied, course authors
can add tags from the taxonomy to their course content.

   .. image:: /_images/release_notes/redwood/tagging_taxonomy_page.png

.. note::

    Content Tagging is enabled by default in the Course Authoring Microfrontend,
    and the Course Authoring Microfrontend is enabled by default in the Redwood
    Release. For more information on how site operators can switch Content Tagging off, see
    :ref:`redwood-settings-toggles`.
 

Value Proposition and Example Use Cases
***************************************

Content tagging supports a diverse range of use cases for instructional
designers who wish to do subject matter alignment.

For example, instructional designers can align courses - or certain content
within a course - to skills or competencies that are required for achieving a
certification. A course about Financial Reporting may contain certain units or
lessons that teach the particular skills required for obtaining a third-party
certification, such as a Certified Public Accountant (CPA) certificate. By
tagging course content with the requisite skills tags from a standardized
Financial Reporting taxonomy, relevant course content is aligned with the
requirements needed for a certification. By successfully completing those units
or lessons, learners can demonstrate achievement of required learning outcomes.

Content tagging also improves content authoring and content reuse workflows.

For example, content authors may wish to find all of the videos in their courses
that cover a certain subject, like factoring binomial equations. When those
videos are tagged for "factoring binomial equations", authors can conduct a
search using those terms and easily find the content. Coupled with the
copy/paste feature, this makes it easy and straight-forward for authors to find
content and reuse it in other courses, which reduces authoring time and
increases efficiency and velocity.

New Functionality
*****************

* **Tag drawer** that lets authors add and delete tags to courses and to content within courses

* **Taxonomy dashboard** that lets any users see which taxonomies and tags are supported within their organization

* **Taxonomy import workflow** that lets administrators upload any third-party taxonomy, as well as update it

* **Taxonomy Templates** for creating or converting taxonomies for ingestion

* **Permissions Management Tools** that let administrators enable or disable taxonomies at the organization or instance level

* **Tag Export function** that lets course authors export a list all the tags
  used in a course

.. note::

    Beta functionality: The Redwood release also features a Beta Course Search
    Feature that lets course authors search for content in a single course, or
    across multiple courses, by tag. The search feature is not on yet by
    default, but can be optionally switched on. For more information about the
    Course Search, see :doc:`course_search`. For more information on how site
    operators can switch it on, see :ref:`redwood-enable-search`.
 

Notes on Scope
==============

Tags are only visible on the Studio side, by users who have staff access to
courses. Tags are not visible to learners.

Tags must be part of a structured taxonomy or a controlled vocabulary. Free
tagging is not yet available. 

Details
=======

Tag drawer
----------

The tag drawer is the place to view tags that have already been added
to content, add new tags, and delete tags. 

The tag drawer can be accessed from a couple of places. For adding tags to
courses, the tag drawer is accessed from the top of the course outline page,
under "manage tags".

   .. image:: /_images/release_notes/redwood/tagging_course_tags.png

From any content block, the tag drawer can be accessed from the three-dot
menu, under "manage tags".

   .. image:: /_images/release_notes/redwood/tagging_manage_tags_from_course_outline.png

Once tags have been added, the tag drawer can also be accessed from the tag
icon, which appears on the content block containing tags.

   .. image:: /_images/release_notes/redwood/tagging_tag_icons.png

Once the tag drawer is open, if there are already tags added, they will
display in a view-only state.

   .. image:: /_images/release_notes/redwood/tagging_tag_drawer_read_only.png
 

Users can add tags, either by conducting a keyword search for a tag, or by
scrolling through all the tags in a taxonomy and clicking the box by the tags
they wish to add.

Multi-level taxonomies may contain parent and children tags, where children tags
are nested underneath the parent tag. When a child tag is selected, its parent
tag is automatically added as well. When a parent tag is selected, its children
tags are not automatically added.

   .. image:: /_images/release_notes/redwood/tagging_choose_tags.png

Users can delete tags by clicking on the "x" next to tags in the drawer.

In multi-level taxonomies, deleting a child tag will automatically delete its
parent tag.

   .. image:: /_images/release_notes/redwood/tagging_delete_tags.png

Taxonomy Dashboard
------------------

The Taxonomy Dashboard is the home for viewing and managing all taxonomies that
are supported on an instance. Any user can access the Dashboard to view all
taxonomies that are enabled for their organization or instance, while
administrators are reserved the right to set permissions on taxonomies, import
and export taxonomies, and update taxonomies.

The Dashboard is accessed via Studio Home.

   .. image:: /_images/release_notes/redwood/tagging_studio_home_taxonomies.png

Once on the Dashboard, any user may view the Taxonomy Page for any given
taxonomy. This is a good way for course teams to become familiar with all the
tags that are available for them to add to their courses, by exploring the list
of tags associated with each taxonomy.

   .. image:: /_images/release_notes/redwood/tagging_taxonomy_page.png

Taxonomy Import and Updates
---------------------------

The platform supports the use of any third-party taxonomy, which means that
course administrators and subject matter experts are free to use any taxonomies
they wish. For example, taxonomies may come from academic, governmental or
professional organizations like the `Open Skills Network`_, the `World Economic
Forum Work Skills Initiative`_, the `Common Core Standards`_, the `Mathematical
Association of America`_, or from proprietary sources like Lightcast Skills.

.. _Open Skills Network: https://www.openskillsnetwork.org/
.. _World Economic Forum Work Skills Initiative: https://www3.weforum.org/docs/WEF_Skills_Taxonomy_2021.pdf
.. _Common Core Standards: https://www.thecorestandards.org/
.. _Mathematical Association of America: https://maa.org/press/periodicals/loci/joma/subject-taxonomy

Administrators and SMEs can also create their own taxonomies. 

Administrators can upload taxonomies to the platform as CSV or JSON files, via
the Taxonomy Dashboard. 

The platform supports both flat and hierarchical taxonomies. Flat taxonomies are
the simplest types of taxonomies, consisting of simple lists of tags. For
example, a Taxonomy for tagging the "difficulty" of problems might contain tags
like these:

.. code block:: text

    Taxonomy: Problem Difficulty

       Easy
       Medium
       Hard

Hierarchical taxonomies are more complex, consisting of one or more levels of
hierarchical, or nested, tags. These tags are often called Parent Tags, Children
Tags, Grandchildren Tags, etc. For example, a hierarchical taxonomy of locations
might contain tags like these:

.. code block:: text

    Taxonomy: Cities
       United States
          California
             Los Angeles

Regardless of whether a taxonomy is pulled from a third-party source or created
from scratch, it must be formatted prior to upload in a CSV or JSON file. For
in-depth instructions on how to create and format taxonomies, see the How-To articles
:doc:`/educators/how-tos/content-tagging-how-tos/build_taxonomy_using_template`
and
:doc:`/educators/how-tos/content-tagging-how-tos/Create_flat_taxonomy_by_uploading_CSV`.

Taxonomies are dynamic and often require updates. For example, the Lightcast
Skills Taxonomy is updated on a weekly or biweekly basis. Administrators can
perform updates on taxonomies by exporting a taxonomy from the platform via a
CSV or JSON file, applying the updates locally, and re-importing the file. A
change log will display for verification. Upon verification, the updates will be
applied across the instance or organization. In other words, if a tag is
replaced, changed or deleted, those updates will automatically apply to any
piece of content where the tag had been applied.

   .. image:: /_images/release_notes/redwood/tagging_taxonomy_updates_log.png

Taxonomy templates
------------------

The Taxonomy Dashboard comes with pre-built taxonomy templates to make it easier
for administrators to format third-party taxonomies. For in-depth instructions
on how to create and format taxonomies, see
:doc:`/educators/how-tos/content-tagging-how-tos/build_taxonomy_using_template`.

   .. image:: /_images/release_notes/redwood/tagging_taxonomy_templates.png

Permissions Management Tools
----------------------------

Administrators have the ability to set taxonomy permissions via the Taxonomy
Dashboard.

Taxonomies can be enabled or disabled for one organization, multiple
organizations, or all organizations. First, select "Manage Organizations" from
the three-dot menu on the taxonomy dashboard:

   .. image:: /_images/release_notes/redwood/tagging_permissions_mgmt.png

From there, one or more organizations can be assigned to the taxonomy:

   .. image:: /_images/release_notes/redwood/tagging_permissions_mgmt2.png

For single-org instances, enabling can be accomplished by checking "Assign to
all orgs". Once enabled, a taxonomy and all its tags are visible in all courses.

Currently, there is not the ability to enable or disable a taxonomy at the
individual course level.

Tag Export
----------

Course staff can export a CSV file that reports on which tags have been added to
which parts of the course. This is helpful for tracking all tags on a course in
a single view. The export includes the full course outline and all of the tags
that are added to each part of the course.

   .. image:: /_images/release_notes/redwood/tagging_tag_export.png

The export can then be loaded into any program that reads CSV files.

   .. image:: /_images/release_notes/redwood/tagging_tag_export_csv.png
 

What's coming in future releases?
=================================

On the horizon for Sumac and beyond include:

* Adding tags to Library content
* Ability to search, filter and sort Library content by tags
* Ability to bulk add tags to content
* Reports and analytics on content by tags
* In-platform taxonomy editing functionality
