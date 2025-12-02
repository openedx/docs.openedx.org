.. _Ulmo Frontend Plugin Slots:

New Frontend Plugin Slots for the Ulmo Release
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

In these release notes, we'll detail the new and updated plugin slots found in the Ulmo
release. The full list of existing plugin slots can be found in
:doc:`/site_ops/references/frontend-plugin-slots`, and usage instructions are
available at :doc:`/site_ops/how-tos/use-frontend-plugin-slots`.

.. contents::
  :local:
  :depth: 1

Where possible, descriptions of the plugin slots are provided. Click the name of
the slot to be brought to the documentation page which contains example
screenshots.

Note: Instance operators using these slots will need to use their
fully-qualified slot id provided in the descriptions, such as
``org.openedx.frontend.authoring.course_unit_sidebar.v1``.

Header
************************************

* Added `DesktopUserMenuToggleSlot <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/DesktopUserMenuToggleSlot>`_:
  This slot is used to replace/modify/hide the contents of the user menu toggle button on desktop sized screens.

* Added `LearningUserMenuToggleSlot <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/LearningUserMenuToggleSlot>`_:
  This slot is used to replace/modify/hide the contents of the learning user menu toggle button.

* Added `MobileUserMenuToggleSlot <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/MobileUserMenuToggleSlot>`_:
  This slot is used to replace/modify/hide the contents of the user menu toggle button on mobile screens.

* Added `StudioHeaderSearchButtonSlot <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/StudioHeaderSearchButtonSlot>`_:
  This slot is used to replace/modify/hide the search button in the studio header.


Footer
************************************

* Added `StudioFooterHelpButtonSlot <https://github.com/openedx/frontend-component-footer/tree/v14.9.3/src/plugin-slots/StudioFooterHelpButtonSlot>`_:
  This slot is used to repace/modify/hide the help button in the studio footer.

* Added `StudioFooterHelpContentSlot <https://github.com/openedx/frontend-component-footer/tree/v14.9.3/src/plugin-slots/StudioFooterHelpContentSlot>`_:
  This slot is used to repace/modify/hide the help content in the studio footer.

* Added `StudioFooterHelpSectionSlot <https://github.com/openedx/frontend-component-footer/tree/v14.9.3/src/plugin-slots/StudioFooterHelpSectionSlot>`_:
  This slot is used to repace/modify/hide the help section in the studio footer.

* Updated `FooterSlot <https://github.com/openedx/frontend-component-footer/tree/v14.9.3/src/plugin-slots/FooterSlot>`_:
  New alias available.


Account MFE
************************************

* Added `AdditionalProfileFieldsSlot <https://github.com/openedx/frontend-app-account/tree/release/ulmo/src/plugin-slots/AdditionalProfileFieldsSlot>`_:
  This slot is used to replace/modify/hide the additional profile fields in the account page.


Authoring MFE
************************************

* Added v2 `CourseAuthoringUnitSidebarSlot <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseAuthoringUnitSidebarSlot>`_:
  The new version has improved handling of styling and conditional rendering.
  The v1 slot is also available and retains the previous behavior.

* Added `CourseFilesSlot <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseFilesSlot>`_:
  This slot is used to replace/modify/hide the course file table UI.

* Added `CourseOutlinePageAlertsSlot <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseOutlinePageAlertsSlot>`_:
  This slot is used to add alerts to the course outline page.

* Added `CourseVideosSlot <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseVideosSlot>`_:
  This slot is used to replace/modify/hide the course video upload page UI.

* Added `EditFileAlertsSlot <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/EditFileAlertsSlot>`_:
  This slot is used to add alerts to the course file edit page.

* Added `EditVideoAlertsSlot <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/EditVideoAlertsSlot>`_:
  This slot is used to add alerts to the course video edit page.


Learning MFE
*********************************************

* Added `ContentIFrameErrorSlot <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/ContentIFrameErrorSlot>`_:
  This slot is used to replace/modify the content iframe error page.

* Added `CourseExitViewCoursesPluginSlot <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseExitPluginSlots/CourseExitViewCoursesPluginSlot>`_:
  This slot is used for modifying "View Courses" button in the course exit screen

* Added `DashboardFootnoteLinkPluginSlot <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseExitPluginSlots/DashboardFootnoteLinkPluginSlot>`_:
  This slot is used for modifying the link to the learner dashboard in the footnote on the course exit page

* Added `SequenceNavigationSlot <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/SequenceNavigationSlot>`_:
  This slot is used to replace/modify/hide the sequence navigation component that controls navigation between units within a course sequence.

* Updated `CourseBreadcrumbsSlot <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseBreadcrumbsSlot>`_:
  Added ``pluginProps``.

* Updated `NotificationTraySlot <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/NotificationTraySlot>`_:
  Added ``pluginProps``.

* Updated `UnitTitleSlot <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/UnitTitleSlot>`_:
  Modified ``pluginProps`` behavior, ``isEnabledOutlineSidebar`` is now always `true`. 


.. seealso::

   * :doc:`/site_ops/how-tos/use-frontend-plugin-slots`

   * :doc:`../sumac/customizing_learner_dashboard`

   * :doc:`../sumac/customizing_header`

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              | Frontend WG                   | Ulmo           |                                |
+--------------+-------------------------------+----------------+--------------------------------+
