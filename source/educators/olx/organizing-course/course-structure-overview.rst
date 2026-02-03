.. _OLX Course Building Blocks:

###############################
OLX Course Building Blocks
###############################

.. tags:: educator, concept

Before beginning to use OLX (open learning XML) to set up a course, it is
important to understand the building blocks of an Open edX course.

.. contents::
  :local:
  :depth: 1

**************
Courseware
**************

Courseware is the main content of a course and consists mainly of lessons
and assessments. The following list describes how courseware is organized in
OLX.

* Course sections are at the top level of a course and typically
  represent a time period. In OLX, sections are defined in the ``chapter`` directory.

* A section contains one or more children ("subsections") which correspond to
  top-level pages in the course. In Studio, these
  are defined within ``sequential`` elements at this level.

  .. note::

    Technically, OLX supports any XBlock at this level. This is not
    guaranteed to work upon Studio import.

* Courses are composed of structural elements, such as ``sequential`` (subsections),
  ``vertical`` (units), and leaf-nodes (content elements/components), such as
  ``html`` or ``problem``. Studio has a fixed hierarchy where children
  of ``sequential`` elements are ``vertical`` elements (called units),
  and children of ``vertical`` elements are leaf elements (called components).

  * :ref:`Course Components<OLX Components>`
  * :ref:`Problems<Components and Activities TOC>`

For more information, see :ref:`The Courseware Structure`.

****************************
Supplemental Course Content
****************************

In addition to the courseware described above, a course can contain
supplemental content, such as textbooks, custom pages, and files.  The
following list describes the types of supported content.

* Course about pages appear in the default Open edX course catalog for prospective students and are
  used to market a course. For more information, see :ref:`Course Overview`.

* Course assets are any supplemental files used in a course, such as a
  syllabus as a PDF file or an image that appears in an HTML component. For
  more information, see :ref:`Course Assets`.

* Course pages are custom pages that appear in the top navigation
  menu of a course. For more information, see :ref:`Create tabs, or pages, in a course<Course Tabs OLX>`.

****************************
Course Policies
****************************

Course policies determine how a course functions. For example, policies
control grading and content experiments. For more information, see
:ref:`Course Policies`.

.. seealso::

  :ref:`What is Open Learning XML?` (concept)

  :ref:`OLX Components` (reference)

  :ref:`Components and Activities TOC` (reference)

  :ref:`The Courseware Structure` (concept)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
