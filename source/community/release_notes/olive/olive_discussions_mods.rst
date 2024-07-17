Moderation & Authoring Tools for the New Discussions Feature (Olive)
####################################################################

The new Community Release, Olive, contains many long-awaited updates to the
Discussions Forums experience, for learners, course teams and forum moderators.
See :doc:`olive_discussions` for a look at the new UI of the forums. This post dives
into new features and substantial improvements made for moderators & course
authors. The following video gives a short overview, and the post dives into
more detail.

.. youtube:: l1g-oRzSN3w

.. contents::
  :local:
  :depth: 2

New features for Forum Moderators
*********************************

The following features streamline Moderator workflows and standardize
touchpoints between Moderators and Learners. In a post's three dot menu,
moderators and staff will see options to edit, pin, close, or delete any forums
post (post authors may edit or delete their own posts as well).

Reasons for closing a post
==========================

Moderators may now specify reasons for their decision to close a post from a
pre-selected list.

      .. image:: /_images/release_notes/olive/close_post.gif


Reasons for editing a post
==========================

Moderators may now specify the reasons for editing a post author's content.

      .. image:: /_images/release_notes/olive/edit_post_reasons.gif


For both editing and closing a post, the reason supplied can be seen by all
other staff members as well as the post's author in a banner at the top of the
post.

Endorsing a response
====================

Moderators may endorse a response to a question, which pushes it to the top of
the list of responses. This is done using the three-dot context menu on the
response itself.

      .. image:: /_images/release_notes/olive/discussB1.png


Improved filtering and sorting of post stats
============================================

Moderators now have access to the following stats from the new Learners' Tab:

#. Sort menus for learners by “Most Activity” and “Recent Activity”

         .. image:: /_images/release_notes/olive/discussB2.png


#. Count of total content (posts and responses) authored by learner

         .. image:: /_images/release_notes/olive/discussB3.png


#. List of threads interacted with by individual learner

         .. image:: /_images/release_notes/olive/discussB4.png



#. Red label for reported content in a learner's history

          .. image:: /_images/release_notes/olive/discussB5.png


#. Additional filters for searching the post history of individual learners, such as filtering by “Question” or “Discussion” post types

         .. image:: /_images/release_notes/olive/discussB6.png



Authoring Experience
********************

Adding a discussion to a unit
=============================

When authoring course content, you no longer need to create a discussion block
and manually set a category and subcategory. With the new mechanism, you simply
tick a checkbox for a Unit, and it will automatically be associated with a topic
with the same name as the unit, and the discussions UI will show up for that
Unit. By default, all Units will automatically be discussable unless they are in
graded or exam subsections.

For units in graded subsections, discussions can be enabled by clicking the Gear
icon from the Studio outline page:

      .. image:: /_images/release_notes/olive/enable_discussion_studio.gif


This new configuration mechanism does mean certain scenarios are no longer
supported:

* Previously, it was possible to have multiple discussion blocks in a single
  Unit, thus allowing multiple topics for a single unit. Now there can only be
  one.
* Previously, you had to specify a separate category and subcategory for each
  topic, and these did not need to match the course hierarchy. Now, the
  categories are defined automatically with no override.
* Additionally, discussion units in exams are no longer possible.
* There was an undocumented, and somewhat broken, mechanism for having
  discussion topic hierarchies of arbitrary depths. This is no longer possible.

Configuring discussions for your course
=======================================

The new discussions experience is turned on for every new course in your
instance. To configure it, visit the Content > Pages & Resources menu, which has
a new and improved look:

      .. image:: /_images/release_notes/olive/discussB7.png



Clicking on the gear icon for “Discussions” will lead you to a menu where you
can choose the “edX” discussion experience. Choosing this option will bring you
to a page where you can set up discussion cohorts, discussion blackout dates,
and more.

      .. image:: /_images/release_notes/olive/discussB8.png



You will notice there are also choices for 3rd-party discussion providers. These
solutions are not built into the Open edX platform, may cost money, and require
effort from site administrators to enable. See
:doc:`olive_3rd_party_discussions` for more detail.

*Thank you to `Kshitij Sobti
<https://opencraft.com/a-look-at-the-recent-enhancements-to-discussions-in-open-edx/>`_
and the team at OpenCraft for the gifs shown in this post.*
