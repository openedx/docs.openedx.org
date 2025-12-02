.. _OLX Directory Structure:

###############################################
What is the OLX Course Structure?
###############################################

.. tags:: educator, concept

Courses can be exported from Open edX Studio. When courses are exported, a
``.tar.gz`` file with the OLX (open learning XML) course content is made
available to download. Using local tools or a source control system such as
GitHub (see :ref:`Work with the targz File`), the downloaded course OLX files
can be extracted. This article describes the structure of an OLX (open learning
XML) course in the format that Open edX Studio exports it in.

.. warning::

  There are other ways to structure an OLX course that may currently import successfully into Studio that
  these pages won't get into, as they're not guaranteed by the Open edX project to work in Open edX Studio in the future.

  Additionally, however a course is written, if that course is imported into Studio, Studio will export
  it in the specifically structured form of OLX *containers* described in this guide.


This section documents how Open edX Studio currently exports courses, so that
authors can understand and manually navigate through the structure of exported
courses.


.. contents::
  :local:
  :depth: 1

For more information about how a specific OLX course is structured, see
:ref:`The Structure of a Sample Course`.

****************************************
OLX and Directory File Structures
****************************************

All files and subdirectories that comprise an OLX course are stored within
a single directory, called the ``course/`` directory.

************************
Top-level Directory
************************

The top-level ``course.xml`` file *can* contain an entire course, but in Studio
exports, content is split out into individual files. This is done at the level
of *containers* such as sections (``chapter``), subsections (``sequential``) &
units (``vertical``), and *components*, such as problems, videos, or HTML (text
components). Certain components, such as `the LTI component
<https://github.com/openedx/training-courses/blob/main/olx_example_course/course/vertical/unit_3_lti.xml>`_,
appear in-line, while others appear in their own files as detailed below.

For example, the `Open edX DemoX Course
<https://github.com/openedx/openedx-demo-course>`_ contains a course with many
component types, and the `OLX Example Course
<https://github.com/openedx/training-courses/tree/main/olx_example_course>`_
(described in more detail in :ref:`The Structure of a Sample Course`) has
human-readable names to better help authors follow the flow of Studio OLX exports.

Descriptions of the directories needed for a typical course follow. To manually
develop course content, these directories will need to be set up if not already
present.


.. note::

  Custom blocks cannot be put in their own directory; they must be put in-line, such as ``edx-sga``.

*******************
XBlock Directories
*******************

Open edX course *containers* and *components* can be broken out of the main ``course.xml`` file
into individual files. Those files go into directories of the name of
the component type (XML tag). For example, components of type ``html``
can be placed as individual files in the ``html`` directory. If a
course does not contain ``.html`` files, or if they are all embedded in
their top-level components, an ``html`` directory does not need to be created.
Studio will place all text components into the ``html`` directory.

As another example, the ``problem`` directory holds one XML file per default
problem type (eg, multiselect, dropdown) in the course. Note that in Studio and
within the pages on docs.openedx.org, these types of problems are known as
"course components".

There are other directories for other types of course components, such as the
``html``, ``lti``, or ``video`` directories.

For information about several examples of these directories, see the following topics.

* :ref:`HTML Components`
* :ref:`Problems<Components and Activities TOC>`
* :ref:`Video Components`

As the set of XBlocks grows, so does the set of associated XML tags
and directories.

.. _Open edX Platform Directories:

Open edX Platform Directories
*******************************

In addition to the course hierarchy, OLX courses contain a set of JSON and HTML
files that specify course policies and non-courseware content.

====================
``about`` Directory
====================

The ``about`` directory contains the following files:

* ``overview.html``, which contains the content for the course overview page
  that learners see in the Learning Management System (LMS).

* ``short_description.html``, which contains the content for the course in the
  course list.

Courses exported from Studio will have more in this directory, such as
``about_sidebar.html``, ``entrance_exam_enabled.html``, and ``duration.html``.
We won't go through these files in this documentation at this time.

For more information, see :ref:`Course Overview`.

==========================
``chapter`` Directory
==========================

The ``chapter`` directory holds one XML file per "course section" in the course.
Note that in Studio and within the pages on docs.openedx.org, "course section"
will be the term used for anything in the ``chapter`` directory. ``chapter``
files are known as *containers*.

====================
``info`` Directory
====================

The ``info`` directory contains the following files:

* ``handouts.html``, which contains the content for the **Course Handouts**
  page in the course.

* ``updates.html``, which contains the course updates learners see when opening
  a course.

=======================
``policies`` Directory
=======================

The ``policies`` directory contains:

* ``assets.json``, which defines all files used in the course, such as images.

The ``policies`` directory also contains a folder for the course run, which holds:

* ``grading_policy.json``, which defines how work is graded in the course run.

* ``policy.json``, which defines various settings in the course run.

For more information, see :ref:`Course Policies`.

==========================
``sequential`` Directory
==========================

The ``sequential`` directory holds one XML file per "course subsection" in the course.
Note that in Studio and within the pages on docs.openedx.org, "course subsection"
will be the term used for anything in the ``sequential`` directory. ``sequential``
files are known as *containers*.


====================
``static`` Directory
====================

The ``static`` directory contains the files used in a course, such as images
or PDFs.

For more information, see :ref:`Course Assets`.

====================
``tabs`` Directory
====================

The ``tabs`` directory contains an HTML file for each custom page in the course.

For more information, see :ref:`Create tabs, or pages, in a course<Course Tabs OLX>`.

==========================
``vertical`` Directory
==========================

The ``vertical`` directory holds one XML file per "course unit" in the course.
Note that in Studio and within the pages on docs.openedx.org, "course unit"
will be the term used for anything in the ``vertical`` directory. ``vertical``
files are known as *containers*.


.. seealso::

  :ref:`What is Open Learning XML?` (concept)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`The Courseware Structure` (reference)

  :ref:`Work with the targz File` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
