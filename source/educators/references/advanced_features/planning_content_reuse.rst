.. _Planning for Content Reuse:

Planning for Content Reuse (LTI)
################################

.. tags:: educator, reference

Before you begin work to reuse the content in an Open edX course, check with
your development operations (DevOps) team for information about the
website to use. At some sites, a completely separate Open edX instance, with
a different Studio website, is set up to be the LTI tool provider.

When you create links to course content in your external LMS, you can link
to components individually, to all of the content in a unit, or to all of the
content in a subsection.

As you plan which parts of the course you want to reuse, note the following
considerations.

* Some content can be confusing to learners when it appears in the context
  of an external LMS. For example, in some configurations, Open edX course discussion identify learners by their internally assigned IDs instead of
  by their usernames. Rather than linking to a subsection or unit that contains
  discussion components, you could plan to either link only to specific
  components or remove the discussion components from the unit or subsection,
  and then use the features available in your external LMS to add discussion
  forums to the course.

* Optional course features that create groups of learners based on their
  IDs, such as content experiments and cohorts, are not designed to provide
  results for external use. To use features like these for your course, you
  should plan to set them up in the external LMS.

* To ensure that the content remains available without interruption, the course
  content appears in the external LMS regardless of the start, end, or
  enrollment dates that are defined for the course in the Open edX instance.

* To ensure that learners see only content that is ready for use, only
  course content that is published appears in an external LMS.

For more information about features that might not be suitable for use with
LTI, see :ref:`Select Content in the Duplicate Course`.

The topics that follow assume use of the Open edX Studio user interface. However,
you can also complete these tasks by exporting the course and then reviewing or
editing its XML before you import.

.. _Select Content in the Duplicate Course:

Select Content in the Duplicate Course
***************************************

To select content in your duplicate Open edX course for reuse in an external LMS,
you use Studio to review the course outline and make note of the components,
units, and subsections you want to include.

Using an organizational tool, such as a spreadsheet, can be helpful. For
example, you can use a spreadsheet column to identify the type of content (for
example, component, unit, subsection), and add their display names to the next
column. Additional columns can contain the values that you use to construct the
addresses for your LTI links. For more information about addressing content,
see :ref:`Determine Content Addresses`.

Optionally, you can streamline the contents of units and subsections by
removing components, or disable course features that you do not plan to use.

.. list-table::
   :widths: 45 45
   :header-rows: 1

   * - Course Content or Feature
     - Works Well with LTI?
   * - Annotation Problem Components
     - No
   * - Cohorts
     - No
   * - Content Experiment Components
     - No
   * - Course-wide Discussions
     - No
   * - Discussion Components
     - No
   * - Text Components
     - Yes
   * - Internal Links
     - No
   * - Problem Components
     - Yes
   * - Randomized Content Block Problem Components
     - No
   * - Video Components
     - Yes

.. check on randomized content blocks, that's an assumption - Alison 22 Aug 15

For information about removing components, see :ref:`Delete a Component`. For
information about disabling cohorts, see :ref:`Disabling the Cohort Feature`.
To remove course-wide discussions, you select **Settings**, and then **Advanced
Settings**, and then delete the contents of the **Discussion Topic Mapping**
policy key. For more information, see :ref:`Create CourseWide Discussion
Topics`.

.. seealso::
 

 :ref:`Using Open edX as an LTI Tool Provider` (concept)

 :ref:`Create a Duplicate Course for LTI use` (how-to)

 :ref:`Determine Content Addresses when using Open edX as an LTI Provider<Determine Content Addresses>` (how-to)



**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-06-04   | MITx                          | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
