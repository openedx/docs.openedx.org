.. _The Structure of a Sample Course:

####################################
The OLX Structure of a Sample Course
####################################

.. tags:: educator, reference

This topic describes the structure of a sample course known as the
`olx_example_course`_, a course with the structure of an Open edX Studio export.

.. contents::
  :local:
  :depth: 1

.. note::
  The structure and content of the *olx_example_course* can change without corresponding
  updates being made to this reference guide.

**************************************************
olx_example_course and Directory File Structures
**************************************************

All files and subdirectories that comprise *olx_example_course* are stored in the
`olx_example_course course`_ directory in the ``training-courses`` GitHub repository.

.. admonition:: TODO FIX THIS IMAGE

.. Image:: /_images/olx-example-images/olx-example-github.png
 :alt: The olx_example_course in GitHub, showing the file structure of the ``course/`` directory.

**********************
Top-level Directories
**********************

The `olx-example_course course`_ directory in the ``training-courses`` GitHub
repository contains the ``course.xml`` file as well as various XBlock and
Platform directories.

* The `course.xml`_ file contains the XML for the courseware. In the
  ``olx_example_course``, this simply contains the course key, ``<course
  url_name="2025" org="OpenedX" course="OLXex"/>``; this is how the Studio
  export works. It is possible to define course sections, subsections, and units
  (``chapter`` s, ``sequential`` s, and ``vertical`` s) within the ``course.xml`` file, however,
  if imported into Studio and then exported, the format of the
  ``olx_example_course`` will be applied.

* Course sections are defined in the ``chapter`` directory, subsections in the
  ``sequential`` directory, and units in the ``vertical`` directory.

* HTML units are referenced in the ``html`` directory, where you'll find two
  files: an XML file that calls an associated HTML file, which defines the HTML
  content.

* Videos are defined in the ``video`` directory.

* Problems are referenced in other directories, such as ``problem`` and ``lti``.

For more information, see the olx_example_course `course.xml`_ file.

==============================
Example of a Referenced XBlock
==============================

.. warning::

  This part of the guide was written in 2013. As of the Teak release, it is
  untested and not guaranteed to work when imported into Open edX Studio,
  either currently or in future releases.

You can reference an XBlock from the ``course.xml`` file.

For example, in ``course.xml``, the first vertical in the courseware contains a
single HTML XBlock with the display name ``Week overview``, which references
``Week_overview`` in the ``url_name`` attribute:

.. code-block:: html

  <chapter display_name="Pedagogical Foundations: Constructive Learning"
      url_name="Week_2_Technology_enabled_constructive_learning">
      <sequential format="Learning Sequence" graded="true"
          display_name="Overview (go here first)"
          url_name="Overview_go_here_first">
          <vertical display_name="Week's overview" url_name="Week_s_overview">
              <html display_name="Week overview" filename="Week_overview"
                  url_name="Week_overview"/>

There is a file called ``Week_overview.html`` in the ``html`` directory that
contains the content for that HTML component. For detailed information, see the
`Week_overview.html`_ file in GitHub.

For a learner, that HTML component appears as the first unit of the course.

.. Image:: /_images/olx-example-images/Insider-first-image.png
 :alt: The HTML component as a learner sees it.


==============================
Example of an Inline XBlock
==============================

.. warning::

  This part of the guide was written in 2013. As of the Teak release, it is
  untested and not guaranteed to work when imported into Open edX Studio,
  either currently or in future releases.

You can include XBlock content within the ``course.xml`` file. You can do
this for ease of reading and maintenance when you do not need to reuse the
content.

For example, in ``course.xml``, the sequential with the display name ``In-class
exercise`` contains embedded HTML content.

.. code-block:: html

  <sequential display_name="In-class exercise" url_name="in_class">
      <html display_name="Overview" url_name="overview">
          <p>In the on-line portion,
             we examined a way we used technology to allow efficient
             implementation of one theory from learning science – constructive
             learning – in Open edX. In designing the Open edX platform, we applied many
             such techniques. We took aspects of mastery learning, project-
             based learning, gamification and others. Other platforms have
             sophisticated techniques for targeting specific student
             misconceptions, enabling a range of student social experiences,
             assessing teacher performance, and hundreds of other research-
             based techniques. We would like to give you a chance to practice
             with designing software to enable good pedagogy.
          </p>
	      . . .
      </html>

For a student, that HTML component appears as a unit of the course in the same
way as a referenced HTML component does.

.. Image:: /_images/olx-example-images/Insider-first-exercise.png
 :alt: The HTML component as a student sees it.


********************
Platform Directories
********************

The olx_example_course course contains information in the course subdirectories as
described below.

====================
``about`` Directory
====================

The ``about`` directory contains the following files.

* ``overview.html``, which contains the content for the course overview page
  that students see in the Learning Management System (LMS).

* ``short_description.html``, which contains the content for the course in the
  course list.

For more information, see :ref:`Course Overview`.

====================
``info`` Directory
====================

The ``info`` directory contains the following files.

* ``handouts.html``, which contains the content for the **Course Handouts**
  page in the course.

* ``updates.html``, which contains the course updates students see when opening
  a course.

=======================
``policies`` Directory
=======================

The ``policies`` directory contains the following files.

* ``assets.json``, which defines all files used in the course, such as images.

* A course directory named ``2025`` (the "course run"), which contains:

  * ``grading_policy.json``, which defines how student work is graded in the
    course.

  * ``policy.json``, which defines various settings in the course.

For more information, see :ref:`Course Policies`.

====================
``static`` Directory
====================

The ``static`` directory contains the files used in the course, such as images
or PDFs.

For more information, see :ref:`Course Assets`.

=======================
``vertical`` Directory
=======================

The ``vertical`` directory contains the XML for the 14 units used in the
course.

You can embed *units* (verticals) in the ``course.xml`` file, however this method
is not guaranteed to work on Open edX Studio imports. It is recommended
to store XML for units in separate files in the ``vertical`` directory.

The *units* are referenced in associated XML files for course *subsections* (in the
``sequential/`` directory). For example, in
``sequential/subsection_1_midterm_exam.xml``, you'll see:

.. code-block:: html

  <sequential default_time_limit_minutes="0" display_name="Subsection 1: Midterm Exam" due="null" format="Midterm Exam" graded="true" hide_after_due="false" show_correctness="always" start="2025-06-01T00:00:00Z">
    <vertical url_name="unit_1_input_problems"/>
    <vertical url_name="unit_2_poll"/>
    <vertical url_name="unit_3_sga"/>
    <vertical url_name="unit_4_formula_response_midterm"/>
  </sequential>

And in ``vertical/unit_1_input_problems.xml``:

.. code-block:: html

  <vertical display_name="Unit 1: Input Problems">
    <problem url_name="numerical_input"/>
    <problem url_name="text_input"/>
  </vertical>

.. seealso::

  :ref:`What is Open Learning XML?` (concept)

  :ref:`OLX Components` (reference)

  :ref:`OLX Exercises, Tools, and Problem Types` (reference)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)

  :ref:`The Courseware Structure` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
| Review Date  | Reviewer                      |   Release      |    Test situation                                                                                                  |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                                                                                                               |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
| 2025-03-19   | Peter Pinch                   | Sumac          |`Fail content <https://github.com/openedx/docs.openedx.org/issues/949>`_                                            |
|              | Sarina Canelake               |                |`Fail insider course hosting <https://github.com/openedx/docs.openedx.org/issues/998>`_                             |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
