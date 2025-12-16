.. _Teak Frontend Plugin Slots:

New Frontend Plugin Slots for the Teak Release
###############################################

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

In these release notes, we'll detail the new plugin slots found in the Teak
release. The full list of existing plugin slots can be found in
:doc:`/site_ops/references/frontend-plugin-slots`, and usage instructions are
available at * :doc:`/site_ops/how-tos/use-frontend-plugin-slots`.

.. contents::
  :local:
  :depth: 1

Where possible, descriptions of the plugin slots are provided. Click the name of
the slot to be brought to the documentation page which contains example
screenshots.

Note: Instance operators using these slots will need to use their
fully-qualified slot id provided in the descriptions, such as
``org.openedx.frontend.authoring.course_unit_sidebar.v1``.

Authoring MFE
************************************

* `AdditionalCourseContentPluginSlot <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/AdditionalCourseContentPluginSlot>`_:
  No description provided.

* `AdditionalCoursePluginSlot <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/AdditionalCoursePluginSlot>`_:
  This slot is used to add a custom card on the the page & resources page.

* `AdditionalTranslationsComponentSlot <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/AdditionalTranslationsComponentSlot>`_:
  This slot is used to add a custom block in the Video Transcription Settings drawer.

* `CourseAuthoringOutlineSidebarSlot <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseAuthoringOutlineSidebarSlot>`_:
  The slot wraps the sidebar that is displayed on the course outline page. It
  can be used to add additional sidebar components or modify the existing
  sidebar.

* `CourseAuthoringUnitSidebarSlot <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseAuthoringUnitSidebarSlot>`_:
  The slot wraps the sidebar that is displayed on the unit editor page. It can
  be used to add additional sidebar components or modify the existing sidebar.

* `CourseOutlineHeaderActionsSlot <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseOutlineHeaderActionsSlot>`_:
  The slot is positioned in the ``SubHeader`` section of the Course Outline
  page, suitable for adding action buttons. The slot by default contains the
  action buttons such as *+ New Section*, *Reindex*, *View Live*.

* `CourseOutlineSubsectionCardExtraActionsSlot <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseOutlineSubsectionCardExtraActionsSlot>`_:
  The slot is positioned right before the drop-down menu icon in the sub-section
  cards of the Course Outline page. It is best suited for adding icon buttons.
  The slot is empty by default.

* `CourseOutlineUnitCardExtraActionsSlot <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseOutlineUnitCardExtraActionsSlot>`_:
  The slot is positioned right before the drop-down menu icon in the Unit cards
  of the Course Outline page. It is best suited for adding icon buttons. The
  slot is empty by default.

* `CourseUnitHeaderActionsSlot <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseUnitHeaderActionsSlot>`_:
  The slot is positioned in the ``SubHeader`` section of the Course Unit editor
  page. It is suitable for adding action buttons. By default, the slot contains
  the action buttons like *View Live Version* and *Preview*.


Learner Dashboard MFE
**********************************************************************

* `CourseBannerSlot <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/teak/src/plugin-slots/CourseBannerSlot>`_:
  This slot is used for replacing or adding content for the "Course Banner"
  component. This banner is rendered as a child of the "Course Card".

* `DashboardModalSlot <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/teak/src/plugin-slots/DashboardModalSlot>`_:
  This slot is used for rendering a modal on a dashboard. 



Learning MFE
*********************************************

* `ContentIFrameLoaderSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ContentIFrameLoaderSlot>`_:
  This slot is used to customize the loading indicator displayed while course content is being loaded in an iframe. It appears when content is loading but hasn't fully rendered yet, providing a customizable loading experience for learners.

* `CourseBreadcrumbsSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseBreadcrumbsSlot>`_:
  This slot is used to replace/modify/hide the courseware top-navigation
  breadcrumbs.

* `CourseHomeSectionOutlineSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseHomeSectionOutlineSlot>`_:
  This slot is used to replace/modify/hide the course home section outline.

* `CourseOutlineMobileSidebarTriggerSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseOutlineMobileSidebarTriggerSlot>`_:
  This slot is used to replace/modify/hide the course outline sidebar mobile
  trigger.

* `CourseOutlineSidebarSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseOutlineSidebarSlot>`_:
  This slot is used to replace/modify/hide the course outline sidebar.

* `CourseOutlineSidebarTriggerSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseOutlineSidebarTriggerSlot>`_:
  This slot is used to replace/modify/hide the course outline sidebar trigger.

* `CourseOutlineTabNotificationsSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseOutlineTabNotificationsSlot>`_:
  This slot is used to add custom notification components to the course outline tab sidebar. It appears in the right sidebar of the course outline/home tab, positioned between the Course Tools widget and the Course Dates widget.

* `CourseRecommendationsSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseRecommendationsSlot>`_:
  This slot is used for modifying the recommendations provided when a course is
  completed.

* `GatedUnitContentMessageSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/GatedUnitContentMessageSlot>`_:
  This slot is used to customize the message displayed when course content is gated or locked for learners who haven't upgraded to a verified track. It appears when a unit contains content that requires a paid enrollment (such as graded assignments) and the learner is on the audit track.

* `NextUnitTopNavTriggerSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/NextUnitTopNavTriggerSlot>`_:
  This slot is used to replace/modify/hide the next button used for unit and
  sequence navigation at the top of the unit page.

* `NotificationTraySlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/NotificationTraySlot>`_:
  This slot is used to customize the notification tray that appears in the courseware sidebar. The notification tray displays upgrade-related notifications and alerts for learners in verified mode courses. It provides a way to show contextual notifications about course access, deadlines, and upgrade opportunities.

* `NotificationWidgetSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/NotificationWidgetSlot>`_:
  This slot is used to customize the notification widget that appears in the discussions-notifications sidebar. The widget is displayed as a compact notification component that shows upgrade-related alerts and can trigger the full notification tray when clicked.

* `NotificationsDiscussionsSidebarSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/NotificationsDiscussionsSidebarSlot>`_:
  This slot is used to replace/modify/hide the notifications discussions
  sidebar.

* `NotificationsDiscussionsSidebarTriggerSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/NotificationsDiscussionsSidebarTriggerSlot>`_:
  This slot is used to replace/modify/hide the notifications discussions sidebar
  trigger.

* `ProgressCertificateStatusSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressCertificateStatusSlot>`_:
  This slot is used for modify the content in the "Certificate Status" in the
  progress page for specific enrollment tracks.

* `ProgressTabCertificateStatusMainBodySlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressTabCertificateStatusMainBodySlot>`_:
  This slot is used to replace or modify the "Certificate Status" component in
  the main body of the Progress Tab.

* `ProgressTabCertificateStatusSidePanelSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressTabCertificateStatusSidePanelSlot>`_:
  This slot is used to replace or modify the "Certificate Status" component in
  the side panel of the Progress Tab.

* `ProgressTabCourseGradeSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressTabCourseGradeSlot>`_:
  This slot is used to replace or modify the Course Grades view in the Progress
  Tab.

* `ProgressTabGradeBreakdownSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressTabGradeBreakdownSlot>`_:
  This slot is used to replace or modify the "Grade Summary" and "Details
  Breakdown" view in the Progress Tab.

* `ProgressTabRelatedLinksSlot <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressTabRelatedLinksSlot>`_:
  This slot is used to replace or modify the related links view in the Progress
  Tab.


.. seealso::

   * :doc:`/site_ops/how-tos/use-frontend-plugin-slots`

   * :doc:`/site_ops/how-tos/use-frontend-plugin-slots`

   * :doc:`../sumac/customizing_learner_dashboard`

   * :doc:`../sumac/customizing_header`

**Maintenance chart**

+--------------+-------------------------------+----------------+------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                      |
+--------------+-------------------------------+----------------+------------------------------------+
|2025-12-18    | BTR WG                        | Ulmo           | Deprecated: Not the latest release |
+--------------+-------------------------------+----------------+------------------------------------+
|  2025-05-08  | Frontend WG                   | Teak           |   Pass                             |
+--------------+-------------------------------+----------------+------------------------------------+
