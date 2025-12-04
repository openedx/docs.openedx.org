Palm Feature Roundup
####################

In the latest Open edX release, Palm, there have been many improvements, big and
small. In this blog, we've done a deep dive into :doc:`new_problem_editor`, the
:doc:`ora_improvements`, and :doc:`discussions_improvements`. In this post,
we'll check out some of the smaller changes that the Open edX engineering teams
have contributed to this release.

.. contents::
  :local:
  :depth: 1

.. _Palm bulk email:

New Bulk Email Experience
*************************

The new bulk email experience for instructors is enabled automatically in Palm.
It allows instructors to schedule bulk emails, instead of sending them
immediately.

The instructor editing experience is largely the same, with choices of who to
send the email to, and places to author the subject and body of the email:

   .. image:: /_images/release_notes/palm/roundup1.png

There is an experimental feature enabling instructors to schedule emails to be
sent in the future. This is not natively included in the Palm install, but
system operators can view the release notes if they wish to implement the
feature.

This experience is part of the new Communications MFE.

Improved “New Component” Interface
**********************************

When creating a new component in Studio, the New Component interface has been
improved:

   .. image:: /_images/release_notes/palm/roundup2.png


Previously, “Advanced” components were hidden under the “Problem” menu, and the
“Drag and Drop” problem type was hidden within Advanced components.

Experimental Feature: New Learner Homepage
******************************************

The Learner Home MFE is included in Palm as an experiment - it is not guaranteed
to fully work correctly, but is included in order to give the community a chance
to preview it. The new Learner Home has many of the same features of the old
learner dashboard, with some extended functionality and performance
enhancements. It is accessible and easy to style with brand colors.

Course cards show the course thumbnail, information about the course, and the
ability to upgrade to a paid track or view/begin a course (if applicable).

   .. image:: /_images/release_notes/palm/roundup3.png

Further course actions (e.g. unenroll, email opt-out settings, and social media
share) have been moved to the menu/triple dot icon on the course card.

   .. image:: /_images/release_notes/palm/roundup4.png



At the top of the Learner Home is a new button, :guilabel:`Refine`; clicking
this button opens options to filter by course status or sort either by most
recent enrollment (default) or title.

   .. image:: /_images/release_notes/palm/roundup5.png

Courses on the homepage are now *paginated*, meaning only 25 courses will show at
one time. This improves the loading time of the page.

.. _DEPR Rate:

Rate XBlock
***********

A note that the Rate XBlock is no longer supported. We recommend using the
`Feedback XBlock <https://github.com/openedx/FeedbackXBlock>`_.

How can I get these changes?
****************************

These improvements are available as of the Open edX Palm release. `Upgrading your
local installation to Palm <https://docs.tutor.edly.io/install.html#upgrading>`_
will guarantee that your system is up-to-date with the latest features,
including everything listed in this post.


**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-04-28    | Docs WG                       | Teak           | Deprecated: This is no longer the current release |
+--------------+-------------------------------+----------------+---------------------------------------------------+

