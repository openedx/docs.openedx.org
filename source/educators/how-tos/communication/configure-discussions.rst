.. _Configuring Edx Discussions:

################################
Configuring Open edX Discussions
################################

.. tags:: educator, how-to

For opening Open edX discussions configuration page, follow these steps.

1. Open your course in Studio.

2. Select **Content**, then **Pages & Resources**.

3. Click on the gear icon on top-right of **Discussion** tile (as seen below).
This will take you to the discussions configuration page where you can select
a discussion provider.

.. image:: /_images/educator_how_tos/Discussion_tile_in_pages_and_resources.png
  :width: 300
  :alt: Appearance of Discussion tile in Pages & Resources.

4. Select Open edX as discussion provider by checking the box on top-right of **Open edX**
tile. Click Next.

.. image:: /_images/educator_how_tos/Tile_for_edx_discussion_provider.png
  :width: 300
  :alt: Appearance of tile for edx discussion provider in configuration.

5. This is the Open edX discussions configuration page. All configuration options
for Open edX discussions can be found here.

.. image:: /_images/educator_how_tos/edx_discussions_configurations_page.png
  :width: 300
  :alt: Appearance of edx discussions configurations page.

.. _Create CourseWide Discussion Topics:

************************************
Create Course-Wide Discussion Topics
************************************

All courses include a page named **Discussion**. When you create a course, a
course-wide discussion topic named "General" is already included by default.

You can add additional course-wide discussion topics to guide how learners
share and find information during your course. Such course-wide topics might
include Introduction and Announcements, Feedback, or Troubleshooting.
Discussions in these topics can begin as soon as your course is available.

.. note:: Make sure each discussion topic in your course has a unique name,
   whether it is a course-wide topic or a content-specific discussion topic
   that you add as a discussion component. If different discussion topics
   share the same name, learners might be confused as to which discussion
   topic they are participating in. For example, do not add a content-specific
   discussion topic named "General", because a course-wide discussion topic
   named "General" already exists in every course.

To create a course-wide discussion topic, follow these steps.

1. Navigate to Open edX discussion provider configuration page (see :ref:`Configuring Edx Discussions`).

2. Scroll down to **General discussion topics**. You would see a topic named **General**
already there. This topic cannot be deleted but can be renamed.

.. image:: /_images/educator_how_tos/General_discussion_topics_edx_discussions.png
  :width: 300
  :alt: A topic named General will already exist in General discussion topics.

3. Click on **Add topic** and add a topic name (e.g. "Course Q&A")

.. image:: /_images/educator_how_tos/Add_general_topic_name_edx_discussions.png
  :width: 300
  :alt: Adding general topic name.

4. Click Save.

When learners select the **Discussion** page for your course, the drop-down
Discussion list now includes the topic you added.

.. image:: /_images/educator_how_tos/New_general_discussion_topic.png
  :width: 300
  :alt: A new topic named Course Q&A in the list of discussion topics.

.. note:: In courses that use cohorts, the course-wide discussion topics that
   you add are unified. All posts can be read and responded to by every
   learner, regardless of the cohort that they belong to. You can optionally
   configure these topics to be divided by cohort. For more information, see
   :ref:`Divide Course Wide Discussion Topics`.


Upgraded Open edX Forum
=======================

Discussion can be enabled for a course unit, which is equivalent to adding
a content-specific discussion topic in that unit in the :ref:`legacy version of
the forum <Content Specific Discussion Topics>`. To enable discussion on a course unit:

1. Open unit’s configuration in Studio.

2. Check the **Enable discussion** checkbox.

.. image:: /_images/educator_how_tos/enable-discussion.png
  :width: 700
  :align: center
  :alt: Toggle switches for anonymous posts in edx discussions configuration.

3. Click **Save**.

Discussions will be enabled on the unit within 1 minute. Units that have
discussions enabled for them will show a **Discussion enabled** label in Studio.

.. image:: /_images/educator_how_tos/discussion-enabled.png
  :width: 700
  :align: center
  :alt: Toggle switches for anonymous posts in edx discussions configuration.

.. note:: To enable discussion for units in subsections marked as graded (but
  not **Timed Exams**), first enable the **Enable discussions on units in graded
  subsusections** toggle on discussion configuration page in studio (see :ref:`Configuring Edx Discussions`).

.. note:: Discussions can not be enabled for units belonging to subsections marked
  as **Timed Exams**.

Users can participate in these discussions using the **Discussion** tab or via the
discussion sidebar visible alongside the course unit.

.. image:: /_images/educator_how_tos/discussion-sidebar.png
  :width: 300
  :align: center
  :alt: Toggle switches for anonymous posts in edx discussions configuration.

To disable discussion for a unit, uncheck the **Discussion enabled** checkbox in the
unit’s configuration and click **Save**.

If the discussion topic for this unit contains at least 1 discussion thread, it
will appear under the **Archived** section in the **Topics** tab in the **Discussion**
tab. Otherwise it will be deleted.

If discussion is enabled again for this unit, the archived topic will be restored along
with the threads contained within it.

.. image:: /_images/educator_how_tos/archived.png
  :width: 300
  :height: 400
  :alt: Toggle switches for anonymous posts in edx discussions configuration.

.. warning:: If **Enable discussions on units in graded subsections** toggle on
  the discussion configuration page (see :ref:`Configuring Edx Discussions`) is turned
  off, any discussion topics associated with units belonging to graded subsections
  will be archived or deleted (if they don’t contain any threads). Enabling the
  toggle again will restore archived topics and replace deleted topics with new ones.

.. warning:: If a subsection is marked as **Timed Exam**, any discussion topics associated
  with units belonging to this subsection will be archived or deleted (if they don’t
  contain any threads). Un-marking the subsection will restore archived topics and
  replace deleted topics with new ones.


.. _Anonymous_posts:

Allowing Learners to Make Anonymous Discussion Posts
****************************************************

By default, when learners participate in a discussion, their usernames are
visible in the discussion. You can allow learners to make discussion posts
that are anonymous to other learners i.e. their usernames are not visible
to other learners.

To allow anonymous discussion posts in your course, follow these steps.

1. Navigate to Open edX discussion configuration page
(see :ref:`Configuring Edx Discussions`).

2. Toggle the **Allow anonymous discussion posts to peers** to enable learners to
make posts that are anonymous to everyone other learners.

 .. image:: /_images/educator_how_tos/anonymous-posting.png
  :width: 400
  :alt: Toggle switches for anonymous posts in Open edX discussions configuration.

3. Click **Save**.

Once the toggle has been enabled, forum users will have the option to create posts
that are anonymous to other learners, as seen below.

 .. image:: /_images/educator_how_tos/post-anonymously.png
  :width: 600
  :align: center
  :alt: Options for anonymous posting while creating a post.

.. seealso::
 :class: dropdown

 :ref:`Discussions` (concept)

  