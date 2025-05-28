Available Frontend Plugin Slots
###############################

.. tags:: site operator, developer, reference

This is a list of all known plugin slots as of the *Sumac* release. More slots
may be available, and are discoverable by visiting the ``src/plugin-slots``
directory of any given MFE.

Header slots, available in MFEs that use ``frontend-component-header``:
***********************************************************************

- `org.openedx.frontend.layout.header_logo.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/LogoSlot>`_
- `org.openedx.frontend.layout.header_desktop.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/DesktopHeaderSlot>`_
- `org.openedx.frontend.layout.header_desktop_logged_out_items.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/DesktopLoggedOutItemsSlot>`_
- `org.openedx.frontend.layout.header_desktop_main_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/DesktopMainMenuSlot>`_
- `org.openedx.frontend.layout.header_desktop_secondary_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/DesktopSecondaryMenuSlot>`_
- `org.openedx.frontend.layout.header_desktop_user_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/DesktopUserMenuSlot>`_
- `org.openedx.frontend.layout.header_learning_course_info.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/CourseInfoSlot>`_
- `org.openedx.frontend.layout.header_learning_help.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/LearningHelpSlot>`_
- `org.openedx.frontend.layout.header_learning_logged_out_items.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/LearningLoggedOutItemsSlot>`_
- `org.openedx.frontend.layout.header_learning_user_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/LearningUserMenuSlot>`_
- `org.openedx.frontend.layout.header_mobile.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/MobileHeaderSlot>`_
- `org.openedx.frontend.layout.header_mobile_logged_out_items.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/MobileLoggedOutItemsSlot>`_
- `org.openedx.frontend.layout.header_mobile_main_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/MobileMainMenuSlot>`_
- `org.openedx.frontend.layout.header_mobile_user_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v6.4.0/src/plugin-slots/MobileUserMenuSlot>`_

Footer slots, available in MFEs that use ``frontend-component-footer``:
***********************************************************************

- `org.openedx.frontend.layout.footer.v1 <https://github.com/openedx/frontend-component-footer/tree/v14.7.0/src/plugin-slots/FooterSlot>`_
- `org.openedx.frontend.layout.studio_footer.v1 <https://github.com/openedx/frontend-component-footer/tree/v14.7.0/src/plugin-slots/StudioFooterSlot>`_
- `org.openedx.frontend.layout.studio_footer_logo.v1 <https://github.com/openedx/frontend-component-footer/tree/v14.7.0/src/plugin-slots/StudioFooterLogoSlot>`_

A slot only available in the Account MFE:
*****************************************

- `org.openedx.frontend.account.id_verification_page.v1 <https://github.com/openedx/frontend-app-account/tree/release/teak/src/plugin-slots/IdVerificationPageSlot>`_

Slots only available in the Authoring MFE:
******************************************

- `org.openedx.frontend.authoring.course_outline_header_actions.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseOutlineHeaderActionsSlot>`_
- `org.openedx.frontend.authoring.course_outline_sidebar.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseAuthoringOutlineSidebarSlot>`_
- `org.openedx.frontend.authoring.course_outline_subsection_card_extra_actions.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseOutlineSubsectionCardExtraActionsSlot>`_
- `org.openedx.frontend.authoring.course_outline_unit_card_extra_actions.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseOutlineUnitCardExtraActionsSlot>`_
- `org.openedx.frontend.authoring.course_unit_header_actions.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseUnitHeaderActionsSlot>`_
- `org.openedx.frontend.authoring.course_unit_sidebar.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/CourseAuthoringUnitSidebarSlot>`_
- `org.openedx.frontend.authoring.additional_course_content_plugin.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/AdditionalCourseContentPluginSlot>`_
- `org.openedx.frontend.authoring.additional_course_plugin.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/AdditionalCoursePluginSlot>`_
- `org.openedx.frontend.authoring.video_transcript_additional_translations_component.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/teak/src/plugin-slots/AdditionalTranslationsComponentSlot>`_

Slots only available in the Learner Dashboard MFE:
**************************************************

- `org.openedx.frontend.learner_dashboard.course_card_action.v1 <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/teak/src/plugin-slots/CourseCardActionSlot>`_
- `org.openedx.frontend.learner_dashboard.widget_sidebar.v1 <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/teak/src/plugin-slots/WidgetSidebarSlot>`_
- `org.openedx.frontend.learner_dashboard.course_list.v1 <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/teak/src/plugin-slots/CourseListSlot>`_
- `org.openedx.frontend.learner_dashboard.no_courses_view.v1 <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/teak/src/plugin-slots/NoCoursesViewSlot>`_
- `org.openedx.frontend.learner_dashboard.dashboard_modal.v1 <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/teak/src/plugin-slots/DashboardModalSlot>`_

Slots only available in the Learning MFE:
*****************************************

- `org.openedx.frontend.layout.header_learning.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/HeaderSlot>`_
- `org.openedx.frontend.learning.content_iframe_loader.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ContentIFrameLoaderSlot>`_
- `org.openedx.frontend.learning.course_breadcrumbs.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseBreadcrumbsSlot>`_
- `org.openedx.frontend.learning.course_home_section_outline.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseHomeSectionOutlineSlot>`_
- `org.openedx.frontend.learning.course_outline_mobile_sidebar_trigger.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseOutlineMobileSidebarTriggerSlot>`_
- `org.openedx.frontend.learning.course_outline_sidebar_trigger.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseOutlineSidebarTriggerSlot>`_
- `org.openedx.frontend.learning.course_outline_sidebar.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseOutlineSidebarSlot>`_
- `org.openedx.frontend.learning.course_outline_tab_notifications.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseOutlineTabNotificationsSlot>`_
- `org.openedx.frontend.learning.course_recommendations.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/CourseRecommendationsSlot>`_
- `org.openedx.frontend.learning.gated_unit_content_message.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/GatedUnitContentMessageSlot>`_
- `org.openedx.frontend.learning.next_unit_top_nav_trigger.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/NextUnitTopNavTriggerSlot>`_
- `org.openedx.frontend.learning.notification_tray.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/NotificationTraySlot>`_
- `org.openedx.frontend.learning.notification_widget.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/NotificationWidgetSlot>`_
- `org.openedx.frontend.learning.notifications_discussions_sidebar_trigger.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/NotificationsDiscussionsSidebarTriggerSlot>`_
- `org.openedx.frontend.learning.notifications_discussions_sidebar.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/NotificationsDiscussionsSidebarSlot>`_
- `org.openedx.frontend.learning.progress_certificate_status.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressCertificateStatusSlot>`_
- `org.openedx.frontend.learning.progress_tab_certificate_status_main_body.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressTabCertificateStatusMainBodySlot>`_
- `org.openedx.frontend.learning.progress_tab_certificate_status_side_panel.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressTabCertificateStatusSidePanelSlot>`_
- `org.openedx.frontend.learning.progress_tab_course_grade.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressTabCourseGradeSlot>`_
- `org.openedx.frontend.learning.progress_tab_grade_breakdown.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressTabGradeBreakdownSlot>`_
- `org.openedx.frontend.learning.progress_tab_related_links.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/ProgressTabRelatedLinksSlot>`_
- `org.openedx.frontend.learning.sequence_container.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/SequenceContainerSlot>`_
- `org.openedx.frontend.learning.unit_title.v1 <https://github.com/openedx/frontend-app-learning/tree/release/teak/src/plugin-slots/UnitTitleSlot>`_

.. seealso::

   * :doc:`/site_ops/how-tos/use-frontend-plugin-slots`

   * :doc:`/community/release_notes/sumac/customizing_header`

   * :doc:`/community/release_notes/sumac/customizing_learner_dashboard`

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
