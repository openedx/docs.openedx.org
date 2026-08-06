.. _Verawood Frontend Plugin Slots:

New Frontend Plugin Slots for the Verawood Release
##################################################

Utilizing *frontend plugin slots*, site operators now have the ability to
customize various portions of the site.

A “frontend plugin slot” refers to an area of a web page - comprising one or
more visual elements - that can be “swapped out” with other visual elements. For
example, one plugin slot allows you to remove the "Help" button in the header.

Overhead and hassle is minimized using the plugin slot system. Site operators
can leverage a plugin slot using a configuration file; the codebase does not
need to be copied (“forked”) nor are extensive changes needed. A snippet of code
is all that is needed to use a plugin slot. A site operator places that code
within a configuration file. Site operators should refer to the
``src/plugin-slots`` directory within each MFE's codebase to view documentation
for that MFE's plugin slot(s).

In these release notes, we'll detail the new and updated plugin slots found in the Ulmo
release. The full list of existing plugin slots can be found in
:ref:`Available Frontend Plugin Slots`, and usage instructions are
available at :ref:`Use A Frontend Plugin Framework Slot`.

.. contents::
  :local:
  :depth: 1

Where possible, descriptions of the plugin slots are provided. Click the name of
the slot to be brought to the documentation page which contains example
screenshots.

Note: Instance operators using these slots will need to use their
fully-qualified slot id provided in the descriptions, such as
``org.openedx.frontend.authoring.course_unit_sidebar.v1``.

frontend-app-authoring
**********************

**Added:**

- `org.openedx.frontend.authoring.page_banner.v1
  <https://github.com/openedx/frontend-app-authoring/tree/release/verawood/src/plugin-slots/PageBannerSlot>`_:
  This slot wraps the Paragon ```PageBanner`` component to allow plugins to replace,
  modify, or hide the banner shown on pages like Schedule & Details. By default,
  it renders the standard ``PageBanner`` with the provided props and children.

frontend-app-discussions
************************

**Added:**

- `org.openedx.frontend.layout.header_discussions.v1
  <https://github.com/openedx/frontend-app-discussions/tree/release/verawood/src/plugin-slots/HeaderSlot>`_:
  This slot is used to replace/modify/hide the discussions header.

frontend-app-learning
*********************

**Added:**

- `org.openedx.frontend.learning.course_tab_links.v1
  <https://github.com/openedx/frontend-app-learning/tree/release/verawood/src/plugin-slots/CourseTabLinksSlot>`_:
  This slot is used to replace/modify/hide the course tabs.
- `org.openedx.frontend.learning.course_tabs_navigation.v1
  <https://github.com/openedx/frontend-app-learning/tree/release/verawood/src/plugin-slots/CourseTabsNavigationSlot>`_:
  This slot is used to replace/modify/hide the entire course tab navigation.
- `org.openedx.frontend.learning.learner_tools.v1
  <https://github.com/openedx/frontend-app-learning/tree/release/verawood/src/plugin-slots/LearnerToolsSlot>`_:
  This plugin slot provides a location for learner-facing tools and features to
  be displayed during course content navigation. The slot is rendered via a
  React portal to ``document.body`` to ensure proper positioning and stacking
  context.

**Updated:**

See `ADR-10 Extract Update Widget from Core MFE
<https://github.com/openedx/frontend-app-learning/blob/release/verawood/docs/decisions/0010-upgrade-widget-extraction.md>`_
for more detail.

- `NotificationTraySlot
  <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/NotificationTraySlot>`_
  is now `org.openedx.frontend.learning.upgrade_panel.v1
  <https://github.com/openedx/frontend-app-learning/tree/release/verawood/src/widgets/upgrade>`_.
  Note The old ``org.openedx.frontend.learning.notification_tray.v1`` still
  exists `as an alias
  <https://github.com/openedx/frontend-app-learning/blob/038c8f379a5c280019b03fe38fdda9a4aba2788d/src/widgets/upgrade/src/UpgradePanel.jsx#L92-L94>`_.
  So ``NotificationTraySlot`` is deprecated but still exists for this release.
- `NotificationsDiscussionsSidebarSlot
  <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/NotificationsDiscussionsSidebarSlot>`_
  is now `org.openedx.frontend.learning.right_sidebar.v1
  <https://github.com/openedx/frontend-app-learning/tree/release/verawood/src/plugin-slots/RightSidebarSlot>`_.
  The `alias still exists for this release
  <https://github.com/openedx/frontend-app-learning/blob/038c8f379a5c280019b03fe38fdda9a4aba2788d/src/plugin-slots/RightSidebarSlot/index.tsx#L10-L16>`_
  but is deprecated.
- `NotificationsDiscussionsSidebarTriggerSlot
  <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/NotificationsDiscussionsSidebarTriggerSlot>`_
  is now `org.openedx.frontend.learning.right_sidebar_trigger.v1
  <https://github.com/openedx/frontend-app-learning/tree/release/verawood/src/plugin-slots/RightSidebarTriggerSlot>`_

**Removed:**

- `NotificationWidgetSlot <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/NotificationWidgetSlot>`_


frontend-app-instructor-dashboard
**********************************

This repository is new as of Verawood, and is enabled by default. It can be optionally disabled; see the :ref:`Verawood operator notes <Verawood operators>`.

**Added:**

- `org.openedx.frontend.slot.header.primaryLinks.v1
  <https://github.com/openedx/frontend-app-instructor-dashboard/tree/v1.2.0/src/slots/CourseInfoSlot>`_:
  The content of this slot renders the current course's organization, course
  number, and title next to the site logo while a user is on any instructor
  dashboard page, giving instructors an at-a-glance reminder of the course they
  are working in.
- `org.openedx.frontend.slot.instructorDashboard.enrollmentActions.v1
  <https://github.com/openedx/frontend-app-instructor-dashboard/tree/v1.2.0/src/slots/EnrollmentActionsSlot>`_:
  This slot is used to replace/modify/hide the action buttons in the header of
  the Enrollments tab. By default it renders Add Beta Testers and Enroll
  Learners with no permission gating, so out of the box the behavior is
  unchanged.
- `org.openedx.frontend.slot.instructorDashboard.tabs.v1
  <https://github.com/openedx/frontend-app-instructor-dashboard/tree/v1.2.0/src/slots/PlaceholderSlot>`_:
  A placeholder for adding new tabs & routes to the instructor dashboard. Both
  slots ship empty. The instructor dashboard already renders a built-in set of
  tabs (Course Info, Enrollments, Course Team, Cohorts, Grading, etc.); these
  slots exist so a site operator can add new tabs alongside them.

frontend-app-[authn, learner-dashboard, notifications]
******************************************************

Note that if you are testing out any of these repositories' :ref:`frontend-base
implementations <frontend-base in Verawood>`, slot IDs may have changed. Site
operators should review :ref:`Port a Frontend Plugin to frontend-base` for more
detail.

.. seealso::

   * :ref:`Use A Frontend Plugin Framework Slot`

   * :ref:`Frontend Slots Learner Dash (Sumac)`

   * :ref:`Frontend Slots Header (Sumac)`

**Maintenance chart**

+--------------+-------------------------------+----------------+------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                      |
+--------------+-------------------------------+----------------+------------------------------------+
| 2026-07-30   | Frontend WG                   | Verawood       | Pass                               |
+--------------+-------------------------------+----------------+------------------------------------+