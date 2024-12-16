.. _Getting Started with Course Content Development:

###############################################
Getting Started with Course Content Development
###############################################

.. tags:: educator, reference

When you have finished setting up your course, you are ready to build your course content.

This section provides an outline of the steps involved in developing your
course content, with links to more details.

.. contents::
  :local:
  :depth: 1

.. _Understanding Course Building Blocks:

************************************************
Understanding Course Building Blocks
************************************************

Before you begin, you should understand the building blocks of courses built on the Open edX® platform.

* :ref:`The course outline<Developing Your Course Outline>` is the container
  for all of your course content. The outline contains one or more sections.
* :ref:`Course sections<Developing Course Sections>` are at the top level of
  your course and typically represent a time period. A section contains one or
  more subsections.
* :ref:`Course subsections<Developing Course Subsections>` are parts of a
  section, and usually represent a topic or other organizing principle. A
  subsection contains one or more units.
* :ref:`Course units <Developing Course Units>` are lessons in a subsection
  that learners view as single pages. A unit contains one or more components.
* :ref:`Course components<Developing Course Components>` are objects within
  units that contain your actual course content.

.. _Creating New Course Content:

****************************************
Creating New Course Content
****************************************

Once you understand the way courses are structured on Open edX®, you can start
organizing your content and entering it into Studio.

You create :ref:`sections<Create a Section>`, :ref:`subsections<Create a
Subsection>`, and :ref:`units<Create a Unit>` in the :ref:`course
outline<Developing Your Course Outline>`.

For graded subsections, you also
:ref:`set the assignment type and due date<Set the Assignment Type and Due Date
for a Subsection>`.

You :ref:`create components<Add a Component>` in the unit
page.

In addition, you :ref:`control content visibility<Controlling Content
Visibility>` by setting release dates on the outline and publishing units.

The following diagram summarizes the content creation workflow:

.. image:: /_images/educator_references/workflow-create-content.png
 :alt: Diagram of the content creation process
 :width: 600

It is recommended that you :ref:`test course content <Testing Your Course
Content>` throughout the creation process, including making sure that the
content is available for learners who access courses using the mobile apps.
For more information, see :ref:`design for mobile <Designing for Mobile>`.

.. note:: Keep in mind that course updates that you make might take longer to
   appear in the mobile apps than on your course website. In particular, newly
   published content can take up to an hour to update on the Android app.


.. _Making Course Content Visible to Students:

*******************************************
Making Course Content Visible to Students
*******************************************

Course content visibility depends on the following factors.

* The :ref:`course start date <Set Start and End Dates>`.
* The release dates of the :ref:`section<Set a Section Release Date>` and
  :ref:`subsection<Set a Subsection Release Date>`.
* The :ref:`prerequisite subsections<configuring_prerequisite_content>` that
  you configure.
* The :ref:`publishing status<Hide a Unit from Students>` of the unit.
* The :ref:`Hide content from learners<Hide a Unit from Students>` setting.

* The :ref:`content groups<About Content Groups>` or :ref:`enrollment track
  groups<About Enrollment Track Groups and Access>` that you have allowed to access the content.

* The use of the :ref:`Results Visibility<Problem Results Visibility>`
  setting.

For more information, see :ref:`Controlling Content Visibility`.



.. _Making Course Content Searchable:

***********************************
Making Course Content Searchable
***********************************

Learners can search course text in :ref:`Text components<Working with Text
Components>` and video transcripts by using the **Search** box at the top of
the **Course** page.

Before learners can search your course, Studio must index the content. Studio
indexes all new course content automatically when you :ref:`publish<Publish a
Unit>` the content.

If necessary, you can manually reindex all of the content in your course at
any time. Typically, you would only manually reindex your course content if
learners see unexpected search results. To reindex your course content,
select **Reindex Content** at the top of the **Course Outline** page.
Reindexing usually takes less than 30 seconds.

.. _Revising Content:

****************************
Revising Content
****************************

You can revise your course content at any time.

* When you :ref:`reorganize sections, subsections, and units<Reorganize the
  Course Outline>` in the outline, the new order is immediately visible to
  learners if the section and subsection are released.

* When you :ref:`edit a unit<Edit a Unit>`, or :ref:`components<Add a
  Component>` within a unit, you must :ref:`publish<Publish a Unit>` those
  changes to make them visible to learners.

The following diagram summarizes the content revision workflow and content
visibility:

.. image:: /_images/educator_references/workflow-revise-content.png
 :alt: Diagram of the content creation process
 :width: 500

It is recommended that you :ref:`test course content <Testing Your Course
Content>` during the revision process, including making sure that the content
is available for learners who access courses using the mobile apps. For
more information, see :ref:`Designing for Mobile`.

.. note:: Keep in mind that course updates that you make might take longer to
   appear in the mobile apps than on your course website. In particular, newly
   published content can take up to an hour to update on the Android app.


.. seealso::
 :class: dropdown
 
 :ref:`Course Outline` (concept)
 :ref:`Creating a New Course in Studio <Creating a New Course>` (how-to)
 :ref:`Create a Course` (how-to)
 :ref:`Create the Course About Page` (how-to)
 :ref:`Understanding a Course Outline <Understanding Your Course Outline>` (reference)
 :ref:`Add Content in the Course Outline` (reference)
 :ref:`Developing Your Course Outline` (reference)
 :ref:`Modify Settings for Objects in the Course Outline` (reference)
 :ref:`Publish Content from the Course Outline` (reference)
 :ref:`Developing Course Sections` (reference)
 :ref:`Developing Course Subsections` (reference)
 :ref:`Create a Section` (how-to)
 :ref:`Create a Subsection` (how-to)
 :ref:`Hiding a Subsection from Learners  <Hide a Subsection from Students>` (how-to)
 :ref:`Add Course Metadata` (how-to)
 :ref:`Use a Section from a Course independently of the Course Outline` (how-to)
 :ref:`Resources for Course Teams <Resources for Course Teams>` (reference)
 :ref:`Resources for Open edX` (reference)   