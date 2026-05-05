.. _Determine Content Addresses:

Determine Content Addresses when using Open edX as an LTI Provider
#######################################################################

.. tags:: educator, how-to

To include Open edX course content in another system, you construct an LTI URL that identifies the
specific content. This URL combines a course ID and a usage ID that you find in the Open edX LMS.

.. contents::
   :local:
   :depth: 2

You might find using a spreadsheet helpful to organize the course ID and usage IDs for the content
you want to include.

Find the Course ID
******************

The course ID has the format ``{key type}:{org}+{course}+{run}``, for example,
``course-v1:OpenedX+DemoX+2024``.

To find the course ID:

1. In your Open edX LMS, open your course.

2. In the URL shown by your browser, find the course ID.

   For example, the URL
   ``https://training.openedx.io/learning/course/course-v1:OpenedX+DemoX+DemoCourse/home``
   contains the course ID ``course-v1:OpenedX+DemoX+Demo_Course``.

The same course ID applies to every item of content in the course.

.. note::

   Courses created before Fall 2014 may use an older format: ``{org}/{course}/{run}``,
   for example, ``OpenedX/DemoX/2014``.

Find usage ID for content
*************************

The usage ID identifies a specific component, unit, or subsection. It has the format

``{key type}:{course ID}+type@{type}+block@{block ID}``

For example, ``block-v1:OpenedX+DemoX+DemoCourse+type@html+block@d4e2624ae8b3479db698413bd8947b6f``

You must have the Staff or Admin role in a course to find usage IDs.

The following terms in the usage ID indicate the level of the content:

.. list-table::
   :widths: 45 45
   :header-rows: 1

   * - Studio term
     - Usage ID term
   * - subsection
     - sequential
   * - unit
     - vertical
   * - component
     - problem, html, or video

.. note::

   Courses created before Fall 2014 may use an older usage ID format:
   ``i4x:;_;_{org};_{course};_{type};_{display name}``.

Find usage ID of unit or component
==================================

1. In your Open edX LMS, open the course.

2. Go to the page that contains the unit or component.

3. Click on **STAFF DEBUG INFO**.

4. Usage ID of a component is value of the ``location`` field.

5. Usage ID of a unit is value of the ``parent`` field.

The usage ID begins with ``block-v1``.

.. note:: For courses created before Fall 2014, the usage ID begins with ``i4x://``.

Find usage ID of subsection
===========================

While you are on a unit of the relevant subsection, copy the url. Here's an example:

.. code-block:: text

   https://master.openedx.io/learning/course/course-v1:OpenedX+DemoX+DemoCourse/block-v1:OpenedX+DemoX+DemoCourse+type@sequential+block@f5c59ce5928f42f4af485e187a93963e/block-v1:OpenedX+DemoX+DemoCourse+type@vertical+block@619390d971ba4e6e8b150417e3730d7e

Here's what the format of this example URL is:

``https://training.openedx.io/learning/course/{course ID}/{usage ID of subsection}/{usage ID of unit}``

So the usage ID of subsection is in the URL.

Construct the LTI URL
*********************

The LTI URL has the following format:

``https://{host}/lti_provider/courses/{course_id}/{usage_id}``

Examples:

Subsection (sequential):

.. code-block:: text

   https://master.openedx.io/lti_provider/courses/course-v1:OpenedX+DemoX+DemoCourse/block-v1:OpenedX+DemoX+DemoCourse+type@sequential+block@f5c59ce5928f42f4af485e187a93963e

Unit (vertical):

.. code-block:: text

   https://master.openedx.io/lti_provider/courses/course-v1:OpenedX+DemoX+DemoCourse/block-v1:OpenedX+DemoX+DemoCourse+type@vertical+block@619390d971ba4e6e8b150417e3730d7e

Text component (html):

.. code-block:: text

   https://master.openedx.io/lti_provider/courses/course-v1:OpenedX+DemoX+DemoCourse/block-v1:OpenedX+DemoX+DemoCourse+type@html+block@d4e2624ae8b3479db698413bd8947b6f


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-05   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+