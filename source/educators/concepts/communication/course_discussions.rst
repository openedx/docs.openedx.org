.. _About Course Discussions:

About Course Discussions
###########################

.. tags:: educator, concept

.. contents::
 :local:
 :depth: 1

Discussions in an Open edX course include both course-wide topics of interest to
all learners (such as "Feedback", "Troubleshooting", or "Technical Help") as
well as content-specific topics that you add to course units as discussion
components. You can create both types of discussion topics in Studio.

For information about creating discussion topics, see the following sections.

For information about creating discussions in which learners in a group (cohort)
only interact with posts from other learners in the same group,
see :ref:`About Divided Discussions`.

For information about running and moderating course discussions, see
:ref:`Best Practices for Configuring Course Discussions` and :ref:`Best Practices for Moderating Course Discussions`.

.. _Visibility of Discussion Topics:

Understanding When Learners Can See Discussion Topics
*****************************************************

The names that you specify as the category and subcategory names for discussion
components are not visible on the Discussion page in the LMS until after
the course has started and the unit is released.

However, "seed" posts that you create in content-specific discussion topics
before a course starts, or before the unit is released, are immediately visible
on the Discussion page, even though the containing category or subcategory
names are not visible. The recommendation is that you do not create posts in
content-specific discussion topics before a unit is released. For more
information about release dates and the visibility of components, see
:ref:`Controlling Content Visibility`.

In contrast, :ref:`course-wide discussion topics<Create CourseWide Discussion
Topics>` that you create on the course discussions configuration page in Studio,
including the default "General" discussion topic, are immediately visible,
regardless of whether the course has started. They are not associated with any
particular section or subsection of the course, and are not subject to
release dates.

.. _Discussions on Mobile Apps:

Discussions in the Open edX Mobile App
***************************************

Learners can participate in course discussions using the Open edX mobile app of your instance as
they do on the website, but there are some differences in the actions that
moderators can take in discussions using the mobile app. To perform moderation
or administrative tasks for your course discussions, you need to work in a web
browser.

The following actions are not supported on the Open edX mobile apps.

  * Pinning posts
  * Marking responses to question posts as answers
  * Endorsing responses to discussion posts
  * Closing posts

.. _The Upgraded Discussion Forum:

The Upgraded Discussion Forum
*****************************************

Course runs created on or after May 16, 2023, use an upgraded version of
the Open edX discussion forum. Learn more about it `here`_. 

.. _here: https://openedx.atlassian.net/wiki/spaces/COMM/pages/3470655498/Discussions+upgrade+Sidebar+and+new+topic+structure.

.. _Content Specific Discussion Topics:


Content-specific Discussion Topics (Legacy)
********************************************

To create a content-specific discussion topic, you add a discussion component
to a unit. Typically, you do this while you are designing and creating your
course in Studio. Follow the instructions in :ref:`Configure Open edX Discussions Legacy`. The result is a discussion topic associated with a unit and its
content. Learners can access content-specific topics both in the course unit
and on the Discussion page.

.. warning:: Follow the recommended steps to add discussion components. Do not
   create discussion topics by using the Duplicate button in Studio, and do
   not reference the same discussion ID in more than one place in your course.
   Duplicated discussion components result in discussion topics that contain the
   same conversations, even if learners post in different discussion topics.

For information about the visibility of content-specific discussion
topics, see :ref:`Visibility of Discussion Topics`.

.. note:: In courses with cohorts enabled, when you add discussion components to
   units in Studio, these discussion topics are by default unified. All learners
   in the course can see and respond to posts from all other learners. You can
   change content-specific discussion topics to be divided, so that only members
   of the same group can see and respond to each other's posts. For information,
   see :ref:`Divide All Content Specific Discussion Topics`.

.. seealso::
 

 :ref:`Configure Open edX Discussions` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
