.. _Determine Content Addresses:

#######################################################################
Determine Content Addresses when using Open edX as an LTI Provider
#######################################################################

.. tags:: educator, how-to

.. note:: This feature was a closed pilot experiment. This feature is not
 supported for new users.

To include the content of an existing course in another system, you use the Open edX
LMS to find the location identifiers for the content you want to include. You
then format the identifiers into an LTI URL.

.. contents::
   :local:
   :depth: 2

You might find using a tool like a spreadsheet helpful as a way to organize the
course ID and each of the usage IDs that correspond to the course content you
want to include in an external LMS.

.. _Find the Course ID:

********************
Find the Course ID
********************

The identifier for your course can be in one of these formats.

* ``{key type}:{org}+{course}+{run}``, for example,
  ``course-v1:OpenedX+DemoX+2024``

* ``{org}/{course}/{run}`` (for courses created prior to 2015), for example, ``OpenedX/DemoX/2014``

Courses created since Fall 2014 typically have an ID that uses the first
format, while older courses have IDs that use the second format.

To find the course ID for your course, follow these steps.

#. In your Open edX LMS, open your course.

#. In the URL shown by your browser, find the course ID.

For example, you open the "Open edX Demo Course" course to the **Course**
page for the course. The URL for the **Course** page is
``https://training.openedx.io/courses/course-v1:OpenedX+DemoX+Demo_Course/about``. From
the URL, you determine that the course ID is ``course-v1:OpenedX+DemoX+Demo_Course``.

The same course ID applies to every item of content in the course.

.. _Finding the Usage ID for Course Content:

****************************************
Finding the Usage ID for Course Content
****************************************

The identifier for a specific component, unit, or subsection in your course can
be in one of these formats.

* ``{key type}:{org}+{course}+{run}+type@{type}+block@{display name}``, for
  example, ``block-v1:OpenedX+DemoX+Demo_Course+type@sequential+block@basic_questions``

* ``i4x:;_;_{org};_{course};_{type};_{display name}``, for example,
  ``i4x:;_;_OpenedX;_DemoX;_sequential;_basic_questions``

Courses created since Fall 2014 typically have usage IDs in the first format,
while older courses have usage IDs in the second format.

The following terms are used in the usage identifiers to indicate subsections,
units, and components.

.. list-table::
   :widths: 45 45
   :header-rows: 1

   * - Studio
     - Page Source
   * - subsection
     - sequential
   * - unit
     - vertical
   * - component
     - problem, html, or video

The example usage IDs shown above include the word "sequential", so they
indicate subsections in a course.

Several methods are available to help you find the usage IDs for items in your
course.

To find the usage ID for a unit or a component in the LMS, you can use
either of these methods.

* :ref:`View staff debug info<View Staff Debug Info for the Usage ID>` for the
  unit or component.

* :ref:`View the page source<View the Page Source for the Usage ID>` for the
  unit or component.

To find the usage ID for a subsection, you
:ref:`view the page source<View the Page Source for the Usage ID>`.

.. note:: You must have the Staff or Admin role in a course to follow these
  procedures for finding usage IDs.

.. _View Staff Debug Info for the Usage ID:

==========================================
View Staff Debug Info for the Usage ID
==========================================

To find the usage ID for a unit or component in the LMS, follow these steps.

#. In your Open edX LMS, open the course.

#. Select **Course**, and then go to the page that contains the unit or
   component.

#. Select **Staff Debug Info**.

#. To find the usage ID for a component, find the **location**.

   For example, ``location = block-v1:OpenedX+DemoX+Demo_Course+type@html+block@054cef851ecc415e969cd82c06a3307b``

#. To find the usage ID for a unit, scroll down to find the **parent**.

   For example, ``parent  block-v1:OpenedX+DemoX+Demo_Course+type@vertical+block@7be7c1ea72f94d08b8bca998aa81f898``

The usage ID value begins with ``block-v1`` for newer courses or ``i4x://`` for
older courses. If you are using a spreadsheet to organize your location
identifiers, you can select the usage ID value, and then copy and paste it into
the spreadsheet.

To close the Staff Debug viewer, click on the browser page outside of the
viewer.

For more information, see :ref:`Staff Debug Info`.

.. _View the Page Source for the Usage ID:

==========================================
View the Page Source for the Usage ID
==========================================

To find the usage ID for a subsection, unit, or component, you view the
HTML page source for that page of the course.

To find the usage ID for a subsection, unit, or component, follow these steps.

#. In your Open edX LMS, open your course.

#. Select **Course**, and then go to the page with the content that you
   want to include in an external LMS.

#. Open the HTML source for the page. For example, in a Chrome browser you
   right click on the page, and then select **View Page Source**.

#. Use your browser's Find feature to locate the term ``data-usage-id``. This
   attribute contains the usage ID.
   ..note:: This step needs review because is not working in the last versions of the Open edX platform.

#. Review the value for the usage id to determine the part of the course it
   identifies: the sequential (subsection), a unit (vertical) or a specific
   component (problem, html, or video).

   .. important:: You might need to search beyond the first match to retrieve
     the usage ID for the content you want to identify. Be sure to check the
     ``data-usage-id`` for sequential, vertical, or problem, html, or video to
     be sure that you specify the content that you want.


For example, you want to link to a subsection in the Open edX Demo course. You open
the course, go to the problem, and then right click to view the page source.
When you search for ``data-usage-id``, the first match is
``block-v1:OpenedX+DemoX+Demo_Course+type@sequential+block@basic_questions``. You
verify that this usage ID value is for the subsection by checking for the
presence of ``sequential``.

If you are using a spreadsheet to organize your location identifiers, you can
select the usage ID value within the quotation marks or ``&#34;`` ISO codes,
and then copy and paste it into the spreadsheet.

************************
Constructing the LTI URL
************************

To identify the edX content that you want to include in an external LMS, you
provide its URL. This URL has the following format.

  ``https://{host}/lti_provider/courses/{course_id}/{usage_id}``

To construct the LTI URL, you add your course ID and the specific content ID.

Examples of the possible formats for an LTI URL follow.

LTI URLs for a subsection include "sequential", as follows.

  ``https://openedx-lti.org/lti_provider/courses/course-v1:OpenedX+01-2024+2024-1/block-v1:OpenedX+01-2024+2024-1+type@sequential+block@4e1de5e13fc3422997fe246b40a43aa1/block-v1:OpenedX+01-2024+2024-1+type@vertical+block@78b75020d3894fdfa8b4994f97275294``

LTI URLs for a unit include "vertical", as follows.

  ``https://openedx-lti.org/lti_provider/courses/course-v1:OpenedX+01-2024+2024-1/block-v1:OpenedX+01-2024+2024-1+type@vertical+block@78b75020d3894fdfa8b4994f97275294``

LTI URLs for Text components include "html+block" or "html", as follows.

  ``https://openedx-lti.org/lti_provider/courses/course-v1:OpenedX+01-2024+2024-1/block-v1:OpenedX+01-2024+2024-1+type@html+block@f9f3a25e7bab46e583fd1fbbd7a2f6a0``

.. seealso::
 :class: dropdown

 :ref:`Using Open edX as an LTI Tool Provider` (concept)

 :ref:`Create a Duplicate Course for LTI use` (how-to)

 :ref:`Planning for Content Reuse (LTI)<Planning for Content Reuse>` (reference)

 :ref:`Example: edX as an LTI Provider to Canvas<edX as an LTI Provider to Canvas>` (reference)

 :ref:`Example: edX as an LTI Provider to Blackboard<edX as an LTI Provider to Blackboard>` (reference)


