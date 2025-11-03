Quince Feature Roundup
######################

The latest Open edX release, Quince, includes a number of improvements for
learners and course teams. In this post we'll highlight some of the biggest
changes that the Open edX community engineering and product teams have
contributed to this release. See also features previously discussed:
:doc:`copy_paste_b`, :doc:`demox_course`, :doc:`woocommerce`, and
:doc:`copy_paste_a`.

.. contents::
  :local:
  :depth: 3

For Learners
************

.. _Learner Home Quince:

New Learner Home
================

With the Quince Release comes the new Learner Home. The Learner Home comes with
an updated UI, a few new features, and extended functionality as well as many of
the same features that the previous course dashboard had.

Learner Home is the hub for learners to easily access and track courses in which
they're currently enrolled, and explore new courses. The Learner Home is
intended to replace the old course dashboard.

Updated UI
----------

Learner Home has a sleek, simpler, and easier-to-navigate UI, with
updates such as pagination that make it easier to manage large lists of courses.
The page is built with Paragon, allowing it to be easily styled with brand
colors and components.

   .. image:: /_images/release_notes/quince/quince-roundup-1.png

This new UI is a harbinger for a platform-wide UI facelift, coming in 2024.

   .. image:: /_images/release_notes/quince/quince-roundup-2.png


New Sort and Filter Feature
---------------------------

Learners can use the new “refine” button on Learner Home to filter through large
lists of courses by course status. They can also sort by the most recent enrollment date or title.

   .. image:: /_images/release_notes/quince/quince-roundup-3.png


Improvements to Course Cards
----------------------------

Like the prior course dashboard experience, courses are presented in a series of
course cards. Course cards display the course thumbnail, information about the
course, upgrade options, and pathways for learners to resume course content.
Further course actions, such as unenrolling and other opt-in settings, have been
moved to the triple-dot menu at the upper righthand corner of the course cards.

   .. image:: /_images/release_notes/quince/quince-roundup-4.png


.. _Masquerade Quince:

Masquerade Feature for Course Teams
-----------------------------------

Site staff can now masquerade as users on the platform by typing a username or
email in the “View as” box and hitting submit. This is designed to be “view
only” so change actions (e.g. enroll, unenroll, selecting a session) are blocked
in this view.

   .. image:: /_images/release_notes/quince/quince-roundup-5.png


.. _Discussions Quince:

New In-Context Discussion Sidebar
=================================

With new courses created in Quince, learners can interact with discussion forums
within course units, via a new collapsable discussion sidebar. The new
discussion sidebar replaces the old discussion XBlock experience.

This sidebar lets learners view, respond to, and initiate discussion threads
relevant to the course unit they are viewing, without having to navigate away
from the course content. Discussion topics will stay close to the content they
support. Learners will have a seamless experience interacting with peers as they
build their understanding and grasp on course learning objectives. 

We'll include highlights from the new sidebar in a future post.

For Course Authors
******************

Copy-Paste Course Components and Units
======================================

With Quince comes the ability to copy and paste course components (text blocks,
video blocks and problem blocks) and course units. This new feature makes it
easier to reuse course content, either within the same course or in a different
course.

For more information about unit copy and paste, see
:doc:`/educators/how-tos/copy_paste_units`.











**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-04-28    | Docs WG                       | Teak           | Deprecated: This is no longer the current release |
+--------------+-------------------------------+----------------+---------------------------------------------------+

