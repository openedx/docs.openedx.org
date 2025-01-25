.. _The Unit Workflow:

##################
The Unit Workflow
##################

.. tags:: educator, reference

When you have set up the :ref:`section<Developing Course Sections>` and
:ref:`subsection<Developing Course Subsections>` in the course outline, you then work with units.

The typical workflow includes these steps.

#. :ref:`Create a unit<Create a Unit>`.
#. :ref:`Add components to the unit<Add a Component>`.
#. :ref:`Modify components in the unit<Add a Component>`.

.. The following image could use some re-work to make the contrast greater.

.. image:: /_images/educator_references/workflow-create-unit.png
 :alt: Diagram of the unit development workflow.
 :width: 800

You :ref:`publish the unit<Publish a Unit>` after you add all of its
components. If you make additional modifications, you must publish the unit
again for the changes to be visible to learners.

As you work through these steps, the publishing status of the unit changes.
The publishing status controls the content available to learners, along with
:ref:`release dates<Release Dates>` (in an instructor-paced course). See the
next section for more information.

.. note:: Release dates apply only to instructor-paced courses. For more
  information about instructor-paced and self-paced courses, see :ref:`Setting
  Course Pacing`.

.. _Unit States and Visibility to Students:

*************************************************
Unit Publishing Status and Visibility to Learners
*************************************************

The following information summarizes whether or not learners can see a unit.

* Learners never see a unit with the publishing status `Draft (Never
  Published)`_.

* Learners never see a unit with the publishing status `Visible to Staff
  Only`_. For more information, see :ref:`Hide a Unit from Students`.

* Learners do not see a unit with the publishing status `Published Not Yet
  Released`_ until the :ref:`release date <Release Dates>` (in an
  instructor-paced course). On the release date, the status changes to
  `Published and Live`_.

* If the publishing status is `Published and Live`_, learners see the current
  version of the unit.

* If the publishing status is `Draft Unpublished Changes`_, learners see the
  last published version of the unit if the :ref:`release dates<Release Dates>`
  for the containing section and subsection have passed.

* If you used :ref:`access settings<Access Settings>` to specify that a unit
  is available only to specific groups of learners (such as content groups
  associated with particular cohorts, or enrollment track groups), only those
  learners who are in groups to which you have given access can see the unit
  after it is published and live.

For more information, see :ref:`Controlling Content Visibility`. For
information about testing content, see :ref:`Testing Your Course Content`.


.. _Unit Publishing Status:

************************************************
Unit Publishing Statuses
************************************************

As a course author, you work with units that have the following statuses.

.. contents::
   :depth: 1
   :local:


.. _Draft Never Published:

========================
Draft (Never Published)
========================

When you create a new unit and add components to it, the unit's publishing
status is **Draft (Never Published)**, as shown in the status panel.

.. image:: /_images/educator_references/unit-never-published.png
 :alt: Status panel of a unit that has never been published, with "Draft (Never
     published)" at the top.
 :width: 200

.. note:: The **Release** section applies only to instructor-paced courses. It
 does not appear for units in self-paced courses. For more information about
 instructor-paced and self-paced courses, see :ref:`Setting Course Pacing`.

In Studio, you see the draft content as you develop the unit. Though you do not
see the unit in the LMS, you can :ref:`preview the unit<Preview Unpublished
Content>`.

Learners never see a unit with this status, even after the release date (in an
instructor-paced course). You must :ref:`publish the unit<Publish a Unit>` for
it to be included in the LMS.

.. _Published and Live:

====================
Published and Live
====================

You published the unit and have not modified it. The release dates for the
section and subsection have passed (in an instructor-paced course). You, and
enrolled learners, see the current version of the unit.

.. image:: /_images/educator_references/unit-published.png
 :alt: Status panel of a unit that is published, with "Published and Live" at
     the top.
 :width: 200

The **Release** section applies only to instructor-paced courses. It does not
appear for units in self-paced courses. For more information, see :ref:`Setting
Course Pacing`.

.. _Published Not Yet Released:

====================================
Published (not yet released)
====================================

You published the unit, but the release date is still in the future. Learners
cannot see this unit until the release date passes.

.. image:: /_images/educator_references/unit-published_unreleased.png
 :alt: Status panel of a unit that is published but not released, with
     "Published (not yet released)" at the top.
 :width: 200

This status applies only to instructor-paced courses. It does not apply to
self-paced courses.

.. _Draft Unpublished Changes:

===========================
Draft (Unpublished changes)
===========================

When you edit a published unit, whether or not it is released, the unit's
publishing status changes to **Draft (Unpublished Changes)**, as shown in the
status panel.

.. image:: /_images/educator_references/unit-pending-changes.png
 :alt: Status panel of a unit that has pending changes, with "Draft
     (Unpublished Changes)" at the top.
 :width: 200

The **Release** section applies only to instructor-paced courses. It does not
appear for units in self-paced courses.

In Studio, you see the draft content as you develop the unit. You can
:ref:`preview the changes to a unit<Preview Unpublished Content>` to test how
your changes will appear to learners after you publish the unit.

If the release date has passed in an instructor-paced course, learners see the
last published version of the unit. If the release date is in the future,
learners cannot see your content. You must :ref:`publish the unit<Publish a
Unit>` for learners to see your changes.

.. _Visible to Staff Only:

===========================
Visible to Staff Only
===========================

When you :ref:`hide a unit from learners<Hide a Unit from Students>`, the
unit's publishing status changes to **Visible to Staff Only**.

The publishing status of a unit also changes to **Visible to Staff Only** if
you hide the parent :ref:`section<Hide a Section from Students>` or
:ref:`subsection<Hide a Subsection from Students>` from learners.

Learners never see a unit with this status, even if it has been published and
the release date has passed (in an instructor-paced course).

.. image:: /_images/educator_references/unit-hide.png
 :alt: Status panel of a unit that is hidden from learners, with an icon and
     "Hide from learners" text visible.
 :width: 200

The **Release** section applies only to instructor-paced courses. It does not
appear for units in self-paced courses.

.. seealso::
 

 :ref:`Create a Unit` (how-to)

 :ref:`Set Access Restrictions For a Unit` (how-to)

 :ref:`Copy and Paste Course Units <Copy and Paste Course Units>` (how-to)

 :ref:`Hide a Unit from Learners <Hide a Unit from Students>` (how-to)

 :ref:`Copy and Paste Course Content <Copy and Paste Course Content>` (how-to)

 :ref:`Developing Course Units` (reference)

