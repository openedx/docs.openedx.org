.. :diataxis-type: how-to

.. _Setting Up Divided Discussions:

******************************
Setting Up Divided Discussions
******************************

.. note::
   You must set up divided discussions before your course starts. You cannot
   divide discussions after the course start date.


By default, all :ref:`course-wide discussion topics<Create CourseWide
Discussion Topics>` and :ref:`content-specific discussion topics<Create
ContentSpecific Discussion Topics>` are unified: all learners can interact
with all posts, responses, and comments. You can change discussion topics of
either type to be divided or unified on the discussions configuration page
(see :ref:`Create CourseWide Discussion Topics`).


.. warning::
   If you change settings of discussion topics in a live course after learners
   have begun reading and contributing to discussion posts, you are changing
   their course experience. Learners might see posts that were previously not
   visible to them, or they might no longer see posts that were previously
   available to all learners.

For information about settings for discussion topics, see the following
topics.

.. contents::
  :local:
  :depth: 1

.. _Divide All Content Specific Discussion Topics:

**********************************************
Divide All Content-Specific Discussion Topics
**********************************************

When you :ref:`create content-specific discussion topics<Create
ContentSpecific Discussion Topics>` by adding discussion components to units
in Studio, these discussion topics are by default unified. All learners in the
course can see and respond to posts from all other learners. You can change
content-specific discussion topics to be divided, so that only members of the
same group (cohort) can see and respond to each other's posts. To do so, follow
the steps below.

.. warning:: If you make changes to discussion division settings in a running
   course, be aware that learners will be affected by your changes.

1. Navigate to edx discussion provider configuration page
(see :ref:`Configuring Edx Discussions`).

2. Turn on the toggle for **Divide discussions by cohort** to divide all
   content-specific discussion topics by cohort.

.. image:: /_images/educator_how_tos/Discussions_toggle_cohort.png
   :width: 300
   :alt: An image showing the toggle for dividing content-specific discussion topics

3. Click **Save** at the bottom-right of the configuration page.

All content-specific discussion topics in the course are now divided
by cohort.

For information about managing discussions that are divided, see
:ref:`Managing Divided Discussion Topics`.

.. _Divide Course Wide Discussion Topics:

*************************************
Divide Course-Wide Discussion Topics
*************************************

When you create :ref:`course-wide discussion topics<Create CourseWide
Discussion Topics>`, they are by default unified. All learners in the
course can see and respond to posts from all other learners.

.. note::
   To divide course-wide discussion topics, you will first need to divide
   content-specific discussion topics. Consequently, course-wide discussion
   topics cannot be divided without dividing all content-specific
   discussion topics.

.. warning:: If you make changes to discussion division settings in a running
   course, be aware that learners will be affected by your changes.

To specify that one or more course-wide discussion topics are divided,
follow these steps.

1. Navigate to edx discussion provider configuration page (see :ref:`Configuring Edx Discussions`).

2. Turn on the toggle for **Divide discussions by cohort** to divide all
   content-specific discussion topics by cohort.

.. image:: /_images/educator_how_tos/Discussions_toggle_cohort.png
   :width: 300
   :alt: An image showing the toggle for dividing content-specific discussion topics

3. Turn on the toggle for **Divide course-wide discussion topics** to divide all
   course-wide discussion topics by cohort.

.. image:: /_images/educator_how_tos/Discussion_toggle_cohort_coursewide.png
   :width: 300
   :alt: An image showing the toggle and options for dividing course-wide discussion topics

4. Uncheck the topic names that you want to keep unified.

5. Click **Save** at the bottom-right of the configuration page.

For information about managing discussions that are divided, see :ref:`Managing
Divided Discussion Topics`.

.. seealso::
 :class: dropdown

 :ref:`About Divided Discussions` (concept)
