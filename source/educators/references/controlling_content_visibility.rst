.. _Controlling Content Visibility:

#########################################################
Guide to Controlling Content Visibility and Access
#########################################################

.. tags:: educator, reference

As a member of the course team, you must carefully control which content is
available to which learners, and when. Visibility settings, together with
publishing states, are used to hide content from learners while still allowing
course staff to view it. Access settings are used to specify which learner
groups can access particular components or units.

You can control content visibility and access using the following Studio
features.

.. contents::
  :local:
  :depth: 1


You can also configure Open edX so that courses or course outlines are visible
to anyone, not just registered and enrolled learners. For information, see
:ref:`Enable Public Course Content`.


.. _Release Dates:

***********************
Release Dates
***********************

In instructor-paced courses, you can specify release dates and times for
sections and subsections. By defining release dates, you ensure that course
content is available to learners on a planned schedule, without requiring
manual intervention while the course is running.

.. note:: Self-paced courses do not have release dates for sections and
  subsections. For more information about instructor-paced and self-paced
  courses, see :ref:`Course Pacing`.

By default, a subsection inherits the release date and time of the section it
is in. You can change the release date of the subsection to another date.

Published units are not visible to learners until the scheduled release date
and time. When the section and subsection have different release schedules,
published units are not visible until both dates have passed.

Course team members can access content that has not been released by
:ref:`previewing the course <Preview Unpublished Content>`.

.. note::
   When you set release times in Studio, times are in Coordinated Universal
   Time (UTC). You might want to verify that you have specified the times that
   you intend by using a time zone converter such as `Time and Date Time Zone
   Converter`_.

   Learners who have specified a time zone in their account settings see course
   dates and times converted to their specified time zone. Learners who have
   not specified a time zone in their account settings see course dates and
   times on their dashboards, in the body of the course, and on their
   **Progress** pages in the time zone that their browsers specify. Learners
   see other course dates and times in UTC.

For more information about setting release dates in an instructor-paced course,
see the following topics.

* :ref:`Set a Section Release Date`
* :ref:`Set a Subsection Release Date`

***********************
Unit Publishing Status
***********************

You publish units to make them visible to learners. In both instructor-paced
and self-paced courses, units must be published to be visible to learners.
Learners see the last published version of a unit if the section and subsection
it is in are released.

Learners do not see units that have never been published, and they do not see
unpublished changes to units or components within units. Therefore, you can
make changes to units in released subsections without disrupting the learner
experience.

For more information, see :ref:`Unit Publishing Status`.

You can publish all changes in a section or subsection at once, or publish
changes to individual units. For more information about publishing units, see
the following topics.

* :ref:`Publish all Units in a Section`
* :ref:`Publish all Units in a Subsection`
* :ref:`Publish a Unit`


.. _Content Hidden from Students:

*******************
Visibility Settings
*******************

You can use the visibility controls in Studio to hide content from learners in
both instructor-paced and self-paced courses.

You might choose to hide a unit from learners, for example, when that unit
contains an answer to a problem in another unit in the same subsection. After
the problem's due date, you can make the unit that contains the answer
visible. You might also permanently hide a unit from learners if that unit
provides instructions or guidance that is intended only for the course team.
Only course team members would see that unit in the course.

Content that is hidden by being excluded from the course outline is never
available to learners, regardless of the release and publishing status.

.. important::
   Content that you make "invisible" to learners by excluding it
   from the course outline is also excluded from grading. As a best practice,
   do not hide sections, subsections, or units that contain graded content by
   excluding them from the course outline.

   Instead, if you want to prevent learners from accessing graded content at
   certain times, you can use options to hide content based on due date or
   course end date. For more information, see :ref:`Hiding Graded Content` and
   :ref:`Hide a Subsection After its Due Date`.

You can hide content at different levels, as described in the following topics.

* :ref:`Hide a Section from Students`
* :ref:`Hide a Subsection from Students`
* :ref:`Hide a Unit from Students`
* :ref:`Problem Results Visibility`

.. note::
   Units and subsections inherit visibility settings from their parent
   subsections or sections. Be aware that when you make a previously hidden
   section or subsection visible to learners, all child subsections or units
   also become visible, unless you have explicitly hidden the subsection or
   unit. Subsections or units that are explicitly hidden remain hidden
   even when you change the visibility of their parent section or subsection.

.. _Hiding Graded Content:

*********************
Hiding Graded Content
*********************

Grading is affected if you hide sections, subsections, or units that contain
graded problems in such a way that they are not included in the course
navigation. When the platform performs grading for a learner, the grading
process does not include problems that are not included in that learner's
course outline.

If you want the problems in the subsection to remain visible, but you want to
hide learners' results for these problems, see :ref:`Problem Results
Visibility`.

.. note:: As a best practice, do not hide graded sections, subsections, or
   units by excluding them from the course outline. Content that is hidden in
   this way is not included when the platform performs grading for learners.

   Instead, if you want to prevent learners from accessing the content of a
   subsection while the subsection itself remains visible in the course
   navigation, you can use the option to hide a subsection or timed exam's
   content based on date. In instructor-led courses, you can hide a subsection
   based on its due date. In self-paced courses, you can hide a subsection
   based on the course's end date. For more details, see :ref:`Hide a
   Subsection After its Due Date`.


.. _Access Settings:

*******************
Access Settings
*******************

In the course outline in Studio, you can use access settings to specify which
learner groups can access particular components or units. You can restrict
access based on one group type, such as :ref:`content group<About Content
Groups>` or :term:`Enrollment Track`.

For example, if you have cohorts enabled in your course, you can use content
groups to give access to particular components or units in your course only to
learners in specific cohorts. If your course has more than one enrollment
track, you might provide the same practice assignments to all learners yet
provide learners in the certificate track with different exams from non-certificate learners.


* :ref:`Modify access settings for a unit<Set Access Restrictions For a Unit>`

* :ref:`Modify access settings for a component<Restrict Access to a Component>`

For information about creating differentiated content based on cohorts, see
:ref:`Guide to Creating Cohort Specific Course Content`.

For information about creating differentiated content based on enrollment
track, see :ref:`Enrollment Track Specific Courseware Overview`.

.. seealso::
  

  :ref:`Prerequisite Course Subsections <Manage Subsection Prerequisites>` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
