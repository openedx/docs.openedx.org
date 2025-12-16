.. _Mobile Updates (Ulmo):

Mobile Updates (Ulmo)
######################

Ulmo introduces changes to the course experience for learners. The course home
has been significantly changed to serve as a hub for learners; the “Videos” tab
has been replaced with a “Content” tab that shows various views of course
content, and a course Progress page has been added.

.. contents::
  :local:
  :depth: 1

New Course Home
***************

The course home has been redesigned. It now contains an area called the Course
Home Carousel that serve as a progress and re-entry point for learners. The
Carousel is highlighted in red below.

.. figure:: /_images/release_notes/ulmo/ulmo_mobile_home.png
  :alt: The Course Home Carousel is located on the bottom half of the mobile view in this image, below the course's image and name.
  :scale: 30

  Redesigned Course Home. The Course Home Carousel is outlined in red.

The Course Home Carousel has four views, each with a different view and action
for learners described below.

.. list-table::
   :header-rows: 1

   * - Carousel View
     - Description
     - Action
   * - Course Completion
     - Total progress through a course and the next unfinished subsection
     - Resume the learner's current subsection / view course outline
   * - Videos
     - Total video progress and the next unfinished video
     - Resume watching / view all course videos
   * - Assignments
     - Assignment progress and the next assignment
     - Start next assignment / view all course assignments
   * - Grades
     - Total progress towards a passing grade and progress through all assignment types
     - View the course progress page

.. figure:: /_images/release_notes/ulmo/ulmo_mobile_carousel.png
  :alt: The four views described in the above table

  All Course Home Carousel views

Course Content Views
********************

The Videos tab has been replaced with a Content tab. Within the content tab, there are now three views:

* **All** - The course outline organized into sections

* **Videos** - All course videos organized into sections

* **Assignments** - All course assignments organized into assignment types

.. figure:: /_images/release_notes/ulmo/ulmo_mobile_content_views.png

  Screenshots of the three Content views


Course Progress Tab
*******************

A Course Progress tab has been added to allow learners to view their progress through their course.

.. figure:: /_images/release_notes/ulmo/ulmo_mobile_progress.png
  :alt: The progress page shows the course completion as a percentage, the overall grade in the course so far, and details on grade breakdown per assignment type.
  :scale: 25

Upgrading To Ulmo
*****************

To upgrade, use the ``release/ulmo`` branch for the `iOS app
<https://github.com/openedx/openedx-app-ios>`_ and the `Android app
<https://github.com/openedx/openedx-app-android>`_. Merge the branch into your
repo, and fix the merge conflicts if they exist.

If you experence issues or need further assistance, please post in the `Open edX
Discussion Forums <https://discuss.openedx.org/>`_.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|2025-12-18    | Mobile Product WG             | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+