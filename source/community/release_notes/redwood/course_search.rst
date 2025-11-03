.. _Course Search Redwood:

Course Search Beta Release Notes (Redwood)
##########################################

The Redwood Release includes a beta release of the new Course Search feature.
Course Search enables course authors to conduct searches within a course, or
across courses, to find content. While it is in Beta, Course Search is not
enabled by default, but Operators can choose to enable it. Operators should see
the :ref:`redwood-enable-search` for details about how to enable.

.. note::

    Consult with your IT team to determine if the new technology that powers
    Course Search, known as Meilisearch, can be installed on your Open edX
    environment. If you encounter reasons why it cannot be installed, we'd love
    to learn more - please reach out `in the discussion forums`_ or
    in the `#wg-product-core`_ Slack channel.

    If it can be, we encourage you to use this feature and provide your feedback
    to the Open edX community `in the discussion forums`_ or in the
    `#wg-product-core`_ Slack channel. This feature is in beta and hasn't yet seen
    widespread testing, so you may encounter bugs, unexpected behavior, or
    incomplete results. However, we are confident that, even if you encounter a
    bug or two, that overall this feature will enhance your use of Open edX
    Studio.

.. _in the discussion forums: https://discuss.openedx.org/t/feedback-thread-new-course-search/13076
.. _#wg-product-core: https://openedx.slack.com/archives/C057J2D1WU9

.. contents::
  :local:
  :depth: 2

What is Course Search?
**********************

With Course Search, authors can conduct searches for content in Studio. Searches
can be conducted within a single course, or across multiple courses. Results
turn up at all levels of the course content, including individual component
blocks, units, subsections and sections.

Course Search makes it easy and quick for authors to find content that they may
wish to edit or reuse. This is particularly helpful for authors who are staff
members on multiple different courses, or on courses that have been built by
multiple authors.

   .. image:: /_images/release_notes/redwood/Search_main_screen.png

New functionality
=================

* Search bar
* Search refinements
* Search results

Details
*******

1. Search Bar
=============

The search bar is accessible from the top header in Studio, via the search icon.
It can be accessed from Studio Home or via any Course Outline Page.

   .. image:: /_images/release_notes/redwood/Search_icon.png

When accessed via Studio Home, searches are automatically conducted across all
courses that the user has staff access to. When accessed via a Course Page, the
user has the option to conduct the search within that course or to expand the
search to all courses.

   .. image:: /_images/release_notes/redwood/Search_this_course.png


2. Search Refinements
=====================

Search refinements can be applied after a search has been conducted, in order to
refine the results. Refinements can also be used without search terms, so users
can effectively apply filters across all of their content.

There are two ways to refine content:

**By type**: Refine your content or your search results by component type (text,
video, problems) or by content type (units, subsections, sections)..

   .. image:: /_images/release_notes/redwood/Search_type_refinement.png

**By tag**: Refine your content or your search results by tag. If multiple tags are
chosen as refinements, only content which matches all of the selected tags will
be shown in the search results (that is, the tags are using an AND filter). For
more information on tagging, see :doc:`content_tagging`.

   .. image:: /_images/release_notes/redwood/Search_tag.png


3. Search Results
=================

Search Results are displayed based on relevance. Each result contains a link out
that takes the user directly to the content, in a new tab. Results also contain
breadcrumbs to provide context for which course the content is coming from, and
where in the course it can be found.

   .. image:: /_images/release_notes/redwood/Search_breadcrumbs.png


4. Advanced Operators
=====================

In the search keywords field, you can use "double quotes" to search for an exact
phrase. For example, a simple search for ``Adam Smith`` would include results with
text like "*Adam* Sandler and Will *Smith* co-starred in...". To make the search
more specific, use double quotes (i.e. ``"Adam Smith"``) so that only results with
that exact phrase will be included.

You can also use **negative keywords**: a search for ``Homer`` might return results
relating to both a Greek poet and a yellow cartoon character. But a search for
``Homer -Simpson`` will exclude any results that include the word "Simpson."


Leveraging Course Search with Tagging and Copy/Paste
****************************************************

When used in tandem with :doc:`content_tagging` and
:doc:`/educators/how-tos/copy_paste_course_components`, the search feature is a
powerful tool for course teams to easily find content, manage content, and reuse
content, all contributing to authoring efficiency and velocity.

The content tagging feature enables authors to add tags to course content.
Authors can tag individual course components like videos and problems, or full
units, sections and subsections.

The copy/paste feature enables authors to copy any part of the course and paste
it into any other course. Authors can copy individual course components like
videos and problems, or full units, subsections and sections.

Taken together, these 3 features yield powerful results. For example, content
authors may wish to find all of the videos in their courses that cover the
subject of “factoring binomial equations”. When all of the relevant videos are
tagged for “factoring binomial equations”, authors can conduct a search and
easily find this content. If they wish to reuse a particular video, they can
then copy it and paste it into any other course.


**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-04-28    | Docs WG                       | Teak           | Deprecated: This is no longer the current release |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2024-06-01    |Docs WG                        | Redwood        |  Pass                                             |
+--------------+-------------------------------+----------------+---------------------------------------------------+

