.. _Create Cohort Specific Course Content:

###########################################
Create Cohort-Specific Course Content
###########################################

.. tags:: educator, how-to

This section provides information about setting up content for specific
cohorts.

.. contents::
  :local:
  :depth: 1

*********
Overview
*********

If you have :ref:`Enable Cohorts` in your
course, you can create different course experiences for learners in different
cohorts.

You can design your course so that some learners are given different content
than others. You do this by creating :ref:`content groups<About Content Groups>`
in Studio, and restricting access to specific components in your course to one
or more content groups. Then, if you associate one or more cohorts with a
content group, only the learners in cohorts associated with that content group
can see course content that you have designated for it.

For more details about content groups, see :ref:`About Content Groups`. For an
example of cohort-specific course content, see :ref:`Cohorted Courseware
Example`.

Complete these steps to create cohort-specific content in your course.

In Studio

#. :ref:`Enable cohorts in your course<Enabling and Configuring Cohorts>`.
#. :ref:`Create content groups<Creating Content Groups>`.
#. :ref:`Specify components or units as available only to particular content
   groups<Specify Content as Available Only to Certain Content Groups>`.

In the LMS

#. :ref:`Assign learners to cohorts<Options for Assigning Learners to
   Cohorts>`.
#. :ref:`Associate one or more cohorts with a content group<Associate Cohorts
   with Content Groups>`.
#. :ref:`Preview cohort-specific course content<Viewing Cohort Specific
   Courseware>`.

.. _Cohorted Courseware Example:

*****************************************
Example: Cohort-Specific Course Content
*****************************************

Suppose that you create two :ref:`cohorts<Cohorts Overview>` in your course:
University Alumni and Current University Students. Learners who are not in
either of these cohorts are automatically placed into a third cohort, the
default cohort, when they access the **Course** or **Discussion** tabs in the
course. For more information about enabling cohorts in your course and
assigning students to cohorts, see :ref:`Enabling and Configuring Cohorts`.

You intend all learners to have substantially the same course experience, with
the exception that only learners in the two university-related cohorts will
receive content that is specific to your university and therefore only of
interest to them.

At the end of every section, you intend to include a video message from various
university officials, including the university president and the dean of your
college. These videos will be shown only to learners in the university and
alumni cohorts. Also at the end of each section, you intend to include a quiz
to test knowledge of the concepts taught in that section. The quiz will be
shown to all learners enrolled in the course.

To achieve this, on the **Group Configurations** page in Studio you create one
content group called "University-Specific Content". In the Instructor
Dashboard, on the **Cohorts** tab, you associate both the "University Alumni"
and the "Current University Students" cohorts with the "University-Specific
Content" content group.

Then, in your course outline, you change the access settings for the video
component at the end of each section so that it is access is available only to
the "University-Specific Content" content group. You do not need to edit the
access settings of the quiz component, because if no content group is
specified in a component's access settings, that component is available to all
learners.

As a final step, you preview the course in the LMS to ensure that learners see
the content that is intended for them. You confirm that when you view the
course in the role of **Student** (in other words, any learner not in a content
group), you see a quiz at the end of each section, but do not see the
university-related videos. When you view the course as a learner in the
"University-Specific Content" group, you see a university-related video as well
as the quiz at the end of each section.

.. _About Content Groups:

**************
Content Groups
**************

Content groups are virtual groupings of learners who will see a particular set
of course content. You can use content groups to designate specific course
content as available to particular :ref:`cohorts<Cohorts Overview>` of learners.

You create content groups in Studio, and in your course outline you use the
**Access Settings** to designate whether a component is selectively available
only to one or more content groups. Any course components that do not have an
explicit restricted access setting are available to all learners, regardless of
their cohort.

Content groups do not have an actual impact on the availability of a course
component until you associate them with one or more cohorts. If you have
designated certain course content as restricted to a content group, and in
addition have associated that content group with one or more cohorts, then
only learners in those cohorts will see the designated content.

For an example of using content groups to create cohort-specific course
content, see :ref:`Cohorted Courseware Example`.

.. seealso::
 :class: dropdown

 :ref:`Cohorts Overview` (concept)

 :ref:`Manage Course Cohorts` (how-to)

 :ref:`About Divided Discussions` (concept)

 :ref:`Managing Divided Discussion Topics` (concept)

 :ref:`Moderating_discussions` (concept)

 :ref:`Setting Up Divided Discussions` (how-to)

 :ref:`Creating Content Groups` (how-to)
 
 :ref:`Specify Content as Available Only to Certain Content Groups` (how-to)
 
 :ref:`Associate Cohorts with Content Groups` (how-to)
 
 :ref:`Viewing Cohort Specific Courseware` (how-to)
 
 :ref:`Delete Content Groups` (how-to)