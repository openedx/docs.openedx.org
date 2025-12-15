.. _The Courseware Structure:

##############################
The OLX Courseware Structure
##############################

.. tags:: educator, reference

The courseware structure in the ``course.xml`` file is defined in the top-level
directory. In Studio, the ``course.xml`` file is simple, and points to the specific
course run xml file in the ``course/run.xml`` file like so:

.. code-block:: xml

  <course url_name="2025" org="OpenedX" course="OLXex"/>

The rest of this page would describe the file that this ``course.xml`` points to,
called `course/2025.xml <https://github.com/openedx/training-courses/tree/main/olx_example_course/course/course/2025.xml>`_.

.. contents::
  :local:
  :depth: 1

.. admonition:: Other course.xml usages

  :ref:`The olx-example course.xml File` describes an alternative way of structuring
  the top-level ``course.xml`` file - it is not the format Studio exports in, and may
  not be supported by Studio.

*************************************
The ``course/run.xml`` File
*************************************

In our example ``course.xml`` file, we point to the 2025 run:

.. code-block:: xml

  <course url_name="2025" org="OpenedX" course="OLXex"/>

A partial example of the contents of a ``2025.xml`` file follows.

.. code-block:: xml

  <course advanced_modules="[&quot;edx_sga&quot;, &quot;lti&quot;, &quot;scorm&quot;, &quot;poll&quot;, &quot;survey&quot;]"
    course_image="Intro_to_OLX_course_card.png"
    display_name="OLX Example Course" end="2027-06-01T00:00:00Z" enrollment_end="2026-01-31T00:00:00Z"
    enrollment_start="2025-05-01T00:00:00Z" graceperiod="7200 seconds"
    language="en" lti_passports="[&quot;codeboard:codeboard_key_1:codeboard_secret_1234&quot;, &quot;jupyter:811a447706c152588c436ee13addeeb889e7f256033679408737bd5bc4118225:869e9639af7de74929b13ae17ad22e4efb60d9d112143e287589289102e1de00&quot;]"
    minimum_grade_credit="0.8" pdf_textbooks="[{&quot;tab_title&quot;: &quot;Education for a Digital World: Advice, Guidelines and Effective Practice from Around Globe&quot;, &quot;chapters&quot;: [{&quot;title&quot;: &quot;Full Book&quot;, &quot;url&quot;: &quot;/asset-v1:OpenedX+OLXex+2025+type@asset+block@Education_for_a_Digital_World.pdf&quot;}], &quot;id&quot;: &quot;6Education_for_a_Digital_World&quot;}]"
    start="2025-06-01T00:00:00Z">
    . . .
  </course>

==============================
``course`` Attributes
==============================

.. note::

  There are many more ``course`` attributes than described in this guide; no such complete guide of all
  available attributes currentliy exists. Many attributes can be discovered by setting them in Studio
  and then inspecting the exported ``course/run.xml`` file.

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``url_name``
     - The value in the course URL path directly after the domain,
       organization, and course name. The url_name must also be the name of the course run XML file (without the ``.xml`` extension).
   * - ``org``
     - The organization sponsoring the course. This value is in the course URL
       path, following the domain and ``/courses/``.
   * - ``course``
     - The name of the course. This value is in the course URL
       path, following the organization.
   * - ``advanced_modules``
     - The list of advanced modules, or custom XBlocks, used in the course.
   * - ``course_image``
     - The path to the course image, used in the Open edX Course Catalog and on the learner dashboard
   * - ``display_name``
     - The human-readable name, used throughout the course
   * - ``enrollment_start``
     - The date and time that learners can start enrolling in the course (defined as a UTC datestamp such as ``"2025-05-01T00:00:00Z"``)
   * - ``grace_period``
     -  The amount of time a learner is allowed to submit beyond a problem's due date (applies across all course elements)
   * - ``language``
     - The two-letter `ISO 639 language code <https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes>`_ that the course is authored in
   * - ``lti_passports``
     - A list of LTI passports required for LTI units in the course
   * - ``minimum_grade_credit``
     - A floating-point number less than or equal to 1.0 which defines the minimum grade required to obtain a course certificate
   * - ``pdf_textbooks``
     - A list of PDF textbooks, each defined with lists that contain information about each chapter and its associated asset file
   * - ``start``
     - The date and time that the course starts (defined as a UTC datestamp)


============================================================
``course`` Element Attributes and Course URLs
============================================================

The attributes of the ``course`` element are used to construct URLs in the
course.  The following example URL shows where these values are used (note
different areas of the platform have different URL structures, but the course
*key* (`course-v1:<@org value/<@course value>/<@url_name value>/>`)) will be
present in each URL.

.. code-block:: none

  https://apps.training.openedx.io/learning/course/course-v1:<@org value>/<@course value>/<@url_name value>/home

For example:

.. code-block:: none

  https://apps.training.openedx.io/learning/course/course-v1:OpenedX+DemoX+Demo_Course/home

*******************************
Course Sections
*******************************

Authors create a course section with the ``chapter`` element, as a child of the
``course`` element. Chapter elements are top-level sections of the course.
The Open edX platform renders navigation chrome around them (accordion on the left).

For example, the course outline is defined by elements in the following format,
defined in the ``course/run.xml`` (`course/2025.xml
<https://github.com/openedx/training-courses/tree/main/olx_example_course/course/course/2025.xml>`_,
in our example).

.. code-block:: xml

  <course advanced_modules="[&quot;edx_sga&quot;, &quot;lti&quot;, &quot;scorm&quot;, &quot;poll&quot;, &quot;survey&quot;]"
    course_image="Intro_to_OLX_course_card.png"
    display_name="OLX Example Course" end="2027-06-01T00:00:00Z" enrollment_end="2026-01-31T00:00:00Z"
    enrollment_start="2025-05-01T00:00:00Z" graceperiod="7200 seconds"
    language="en" lti_passports="[&quot;codeboard:codeboard_key_1:codeboard_secret_1234&quot;, &quot;jupyter:811a447706c152588c436ee13addeeb889e7f256033679408737bd5bc4118225:869e9639af7de74929b13ae17ad22e4efb60d9d112143e287589289102e1de00&quot;]"
    minimum_grade_credit="0.8" pdf_textbooks="[{&quot;tab_title&quot;: &quot;Education for a Digital World: Advice, Guidelines and Effective Practice from Around Globe&quot;, &quot;chapters&quot;: [{&quot;title&quot;: &quot;Full Book&quot;, &quot;url&quot;: &quot;/asset-v1:OpenedX+OLXex+2025+type@asset+block@Education_for_a_Digital_World.pdf&quot;}], &quot;id&quot;: &quot;6Education_for_a_Digital_World&quot;}]"
    start="2025-06-01T00:00:00Z">

    <chapter url_name="section_1_homework"/>
    <chapter url_name="section_2_exams"/>
    . . .
  </course>

==============================================
``chapter`` Attributes
==============================================

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``url_name``
     - The url_name must be the name of the XML file (without the ``.xml`` extension) in the ``chapter/`` directory.
   * - ``display_name``
     - The value that is displayed to learners as the name of the section.
   * - ``start``
     - The date and time, in UTC, that the section is released to learners.
       Before this date and time, learners do not see the section.

=========================
``chapter`` Children
=========================

The ``chapter`` element contains one or more children. Studio uses
*subsections*, defined by ``sequential`` elements, for all children of chapters.

The following example shows a chapter with two subsections, (``sequential`` items),
from `chapter/section_1_homework.xml <https://github.com/openedx/training-courses/tree/main/olx_example_course/course/chapter/section_1_homework.xml>`_.

.. code-block:: xml

  <chapter display_name="Course Section 1: Homework">
    <sequential url_name="subsection_1_ungraded"/>
    <sequential url_name="subsection_2_graded_as_homework"/>
  </chapter>

*******************************
Course Subsections
*******************************

Authors create a course subsection with the ``sequential`` element, for each
subsection in the chapter.

For example, the course can contain a subsection in this format, from
`sequential/subsection_2_graded_as_homework.xml
<https://github.com/openedx/training-courses/tree/main/olx_example_course/course/chapter/subsection_2_graded_as_homework.xml>`_.

.. code-block:: xml

  <sequential display_name="Subsection 2: Graded as Homework"
    due="null" format="Homework" graded="true" hide_after_due="false" show_correctness="always"
    start="2025-06-01T00:00:00Z">

    <vertical url_name="unit_1_video"/>
    <vertical url_name="unit_2_selection_problems"/>
    <vertical url_name="unit_3_lti"/>
    <vertical url_name="unit_4_formula_response_homework"/>
  </sequential>


==============================================
``sequential`` Attributes
==============================================

.. note::

  There may be more ``sequential`` attributes than described in this guide; no such complete guide of all
  available attributes currentliy exists. Many attributes can be discovered by setting them in Studio
  and then inspecting the exported ``sequential/<name>.xml`` file.


.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``url_name``
     - The url_name must be the name of the XML file (without the ``.xml`` extension) in the ``sequential/`` directory.
   * - ``display_name``
     - The value that is displayed to learners as the name of the sequential,
       or subsection.
   * - ``due``
     - The date and time, in UTC, that the subsection is due.
       After this date and time, learners cannot answer questions in this subsection.
   * - ``start``
     - The date and time, in UTC, that the subsection is released to learners.
       Before this date and time, learners do not see the subsection.
   * - ``graded``
     - Whether the subsection is a graded subsection; ``true`` or ``false``.
   * - ``format``
     - If the subsection is graded, the assignment type.
   * - ``graceperiod``
     - If the subsection is graded, the number of seconds in the grace period.
   * - ``hide_after_due``
     - Whether the subsection should be visible past the due date; ``true`` or ``false``.
   * - ``show_correctness``
     - Defines when to show whether a learner's answer to the problem is correct;
       ``"always"``, ``"never"``, or ``"past_due"``
   * - ``showanswer``
     - Defines when to show the answer to the problem. ``"always"``, ``"answered"``, ``"attempted"``, ``"closed"``,
       ``"finished"``, ``"correct_or_past_due"``, ``"past_due"``, ``"never"``, ``"after_attempts"``, ``"after_all_attempts"``,
       ``"after_all_attempts_or_correct"``, ``"attempted_no_past_due"``, or ``"never_show_correctness_but_include_grade_description"``

.. admonition:: "never_show_correctness_but_include_grade_description"

  This option was added to the Ulmo release. In this option, learners do not see
  question-level correctness or scores before or after the due date. However,
  once the due date passes, they can see their overall score for the subsection
  on the Progress page.

==============================================
``sequential`` Children (Course Units)
==============================================

In the course structure, a course unit serves the following functions.

* Defines the display name for the unit.
* Organizes components.

The ``sequential`` element contains one or more units (child ``vertical`` elements).

The ``vertical`` element references a unit in the course.

For example, the subsection can contain units in this format, from
`vertical/unit_2_selection_problems.xml`_.

.. code-block:: xml

  <vertical display_name="Unit 2: Selection Problems">
    <problem url_name="single_select"/>
    <problem url_name="multi_select"/>
    <problem url_name="dropdown"/>
  </vertical>

=========================
``vertical`` Attributes
=========================

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``url_name``
     - The url_name must be the name of the XML file (without the ``.xml`` extension) in the ``vertical/`` directory.
   * - ``display_name``
     - The value that is displayed to learners as the name of the sequential,
       or subsection.

==============================
``vertical`` Children
==============================

The ``vertical`` element contains one or more child elements for each component
in the unit.

.. warning::

  A unit element can also contain a vertical element, potentially creating a recursive definition of verticals.
  This is unsupported by Studio and not guaranteed to render properly - or at all - in the Open edX LMS or Libraries.

Child elements of ``vertical`` refer to components in the course. The Open edX
platform supports a wide range of components, including custom XBlocks.

.. note::
  Some course components appear as a reference to a component in a directory, such as the ``problem`` components referenced in `vertical/unit_2_selection_problems.xml`_.

  However, some course components, such as custom XBlocks like LTI or ORA components, appear directly in-line in the ``vertical`` element.
  See `vertical/unit_3_lti.xml <https://github.com/openedx/training-courses/blob/main/olx_example_course/course/vertical/unit_3_lti.xml>`_ for an example of this.

.. seealso::

  :ref:`What is Open Learning XML?` (concept)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+

.. _vertical/unit_2_selection_problems.xml: https://github.com/openedx/training-courses/tree/main/olx_example_course/course/vertical/unit_2_selection_problems.xml