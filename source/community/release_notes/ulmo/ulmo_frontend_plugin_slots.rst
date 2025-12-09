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
  Modified ``pluginProps`` behavior, ``isEnabledOutlineSidebar`` is now always ``true``. 

Catalog MFE
*********************************************

* Added `org.openedx.frontend.catalog.home_page.banner <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/HomeBannerSlot>`_:
  This slot is used to replace/modify/hide the entire Home page banner.

* Added `org.openedx.frontend.catalog.home_page.overlay_html <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/HomeOverlayHtmlSlot>`_:
  This slot is used to replace/modify/hide the entire Home page overlay HTML.

* Added `org.openedx.frontend.catalog.home_page.promo_video_button <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/HomePromoVideoSlots/HomePromoVideoButtonSlot>`_:
  This slot is used to replace/modify/hide the entire Home page promo video button.

* Added `org.openedx.frontend.catalog.home_page.promo_video_modal <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseAboutIntroVideoSlots/CourseAboutIntroVideoModalSlot>`_:
  This slot is used to replace/modify/hide the entire Course about page intro video modal.

* Added `org.openedx.frontend.catalog.home_page.promo_video_modal_content <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseAboutIntroVideoSlots/CourseAboutIntroVideoModalContentSlot>`_:
  This slot is used to replace/modify/hide the entire Course about page intro video modal content.

* Added `org.openedx.frontend.catalog.home_page.courses_list <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/HomeCoursesListSlot>`_:
  This slot is used to replace/modify/hide the entire Home page courses list.

* Added `org.openedx.frontend.catalog.home_page.course_card <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/HomeCourseCardSlot>`_:
  This slot is used to replace/modify/hide the entire Home page course card.

* Added `org.openedx.frontend.catalog.generic.loader <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/LoaderSlot>`_:
  This slot is used to replace/modify/hide the entire content of a specified container during a loading state.

* Added `org.openedx.frontend.catalog.course_about_page.enrollment_button <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseAboutEnrollmentButtonSlot>`_:
  This slot is used to replace/modify/hide the entire course enrollment button on the Course about page.

* Added `org.openedx.frontend.catalog.course_about_page.intro <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseAboutIntroSlot>`_:
  This slot is used to replace/modify/hide the entire Course about page intro section.

* Added `org.openedx.frontend.catalog.course_about_page.intro_video_button <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseAboutIntroVideoSlots/CourseAboutIntroVideoButtonSlot>`_:
  This slot is used to replace/modify/hide the entire Course about page video button.

* Added `org.openedx.frontend.catalog.course_about_page.intro_video_modal_content <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseAboutIntroVideoSlots/CourseAboutIntroVideoModalContentSlot>`_:
  This slot is used to replace/modify/hide the entire Course about page intro video modal content.

* Added `org.openedx.frontend.catalog.course_about_page.intro_video_modal <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseAboutIntroVideoSlots/CourseAboutIntroVideoModalSlot>`_:
  This slot is used to replace/modify/hide the entire Course about page intro video modal.

* Added `org.openedx.frontend.catalog.course_about_page.course_image <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseAboutCourseImageSlot>`_:
  This slot is used to replace/modify/hide the entire Course about page course image.

* Added `org.openedx.frontend.catalog.course_about_page.course_media <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseAboutCourseMediaSlot>`_:
  This slot is used to replace/modify/hide the entire Course about page course media section.

* Added `org.openedx.frontend.catalog.course_about_page.sidebar <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseAboutSidebarSlot>`_:
  This slot is used to replace/modify/hide the entire Course about page sidebar.

* Added `org.openedx.frontend.catalog.course_catalog_page.intro <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseCatalogIntroSlot>`_:
  This slot is used to replace/modify/hide the entire Course catalog page intro section.

* Added `org.openedx.frontend.catalog.course_catalog_page.data_table.course_card <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseCatalogDataTableSlots/CourseCatalogDataTableCardViewSlot/CourseCatalogDataTableCourseCardSlot>`_:
  This slot is used to replace/modify/hide the entire Course catalog page data table course card.

* Added `org.openedx.frontend.catalog.course_catalog_page.data_table.card_view <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseCatalogDataTableSlots/CourseCatalogDataTableCardViewSlot>`_:
  This slot is used to replace/modify/hide the entire Course catalog page data table card view section.

* Added `org.openedx.frontend.catalog.course_catalog_page.data_table.control_bar <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseCatalogDataTableSlots/CourseCatalogDataTableControlBarSlot>`_:
  This slot is used to replace/modify/hide the entire Course catalog page data table control bar.

* Added `org.openedx.frontend.catalog.course_catalog_page.search_field <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseCatalogSearchFieldSlot>`_:
  This slot is used to replace/modify/hide the entire Course catalog page search field.

* Added `org.openedx.frontend.catalog.course_catalog_page.data_table <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseCatalogDataTableSlots/CourseCatalogDataTableSlot>`_:
  This slot is used to replace/modify/hide the entire Course catalog page data table.

* Added `org.openedx.frontend.catalog.course_catalog_page.data_table.table_footer <https://github.com/openedx/frontend-app-catalog/tree/release/ulmo/src/plugin-slots/CourseCatalogDataTableSlots/CourseCatalogDataTableTableFooterSlot>`_:
  This slot is used to replace/modify/hide the entire Course catalog page data table footer.


.. seealso::

   * :ref:`Use A Frontend Plugin Framework Slot`

   * :ref:`Frontend Slots Learner Dash (Sumac)`

   * :ref:`Frontend Slots Header (Sumac)`

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-12-05   | Frontend WG                   | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
