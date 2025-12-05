.. _Available Frontend Plugin Slots:

Available Frontend Plugin Slots
###############################

.. tags:: site operator, developer, reference

This is a list of all known plugin slots as of the *Ulmo* release. More slots
may be available, and are discoverable by visiting the ``src/plugin-slots``
directory of any given MFE.

Header slots, available in MFEs that use ``frontend-component-header``:
***********************************************************************

- `org.openedx.frontend.layout.header_logo.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/LogoSlot>`_
- `org.openedx.frontend.layout.header_desktop.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/DesktopHeaderSlot>`_
- `org.openedx.frontend.layout.header_desktop_logged_out_items.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/DesktopLoggedOutItemsSlot>`_
- `org.openedx.frontend.layout.header_desktop_main_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/DesktopMainMenuSlot>`_
- `org.openedx.frontend.layout.header_desktop_secondary_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/DesktopSecondaryMenuSlot>`_
- `org.openedx.frontend.layout.header_desktop_user_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/DesktopUserMenuSlot>`_
- `org.openedx.frontend.layout.header_desktop_user_menu_toggle.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/DesktopUserMenuToggleSlot>`_
- `org.openedx.frontend.layout.header_learning_course_info.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/CourseInfoSlot>`_
- `org.openedx.frontend.layout.header_learning_help.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/LearningHelpSlot>`_
- `org.openedx.frontend.layout.header_learning_logged_out_items.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/LearningLoggedOutItemsSlot>`_
- `org.openedx.frontend.layout.header_learning_user_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/LearningUserMenuSlot>`_
- `org.openedx.frontend.layout.header_learning_user_menu_toggle.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/LearningUserMenuToggleSlot>`_
- `org.openedx.frontend.layout.header_mobile.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/MobileHeaderSlot>`_
- `org.openedx.frontend.layout.header_mobile_logged_out_items.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/MobileLoggedOutItemsSlot>`_
- `org.openedx.frontend.layout.header_mobile_main_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/MobileMainMenuSlot>`_
- `org.openedx.frontend.layout.header_mobile_user_menu.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/MobileUserMenuSlot>`_
- `org.openedx.frontend.layout.header_mobile_user_menu_trigger.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/MobileUserMenuToggleSlot>`_
- `org.openedx.frontend.layout.studio_header_search_button_slot.v1 <https://github.com/openedx/frontend-component-header/tree/v8.1.0/src/plugin-slots/StudioHeaderSearchButtonSlot>`_

Footer slots, available in MFEs that use ``frontend-component-footer``:
***********************************************************************

- `org.openedx.frontend.layout.footer.v1 <https://github.com/openedx/frontend-component-footer/tree/v14.9.3/src/plugin-slots/FooterSlot>`_
- `org.openedx.frontend.layout.studio_footer.v1 <https://github.com/openedx/frontend-component-footer/tree/v14.9.3/src/plugin-slots/StudioFooterSlot>`_
- `org.openedx.frontend.layout.studio_footer_help_button.v1 <https://github.com/openedx/frontend-component-footer/tree/v14.9.3/src/plugin-slots/StudioFooterHelpButtonSlot>`_
- `org.openedx.frontend.layout.studio_footer_help-content.v1 <https://github.com/openedx/frontend-component-footer/tree/v14.9.3/src/plugin-slots/StudioFooterHelpContentSlot>`_
- `org.openedx.frontend.layout.studio_footer_help_section.v1 <https://github.com/openedx/frontend-component-footer/tree/v14.9.3/src/plugin-slots/StudioFooterHelpSectionSlot>`_
- `org.openedx.frontend.layout.studio_footer_logo.v1 <https://github.com/openedx/frontend-component-footer/tree/v14.9.3/src/plugin-slots/StudioFooterLogoSlot>`_

A slot only available in the Account MFE:
*****************************************

- `org.openedx.frontend.account.additional_profile_fields.v1 <https://github.com/openedx/frontend-app-account/tree/release/ulmo/src/plugin-slots/AdditionalProfileFieldsSlot>`_
- `org.openedx.frontend.account.id_verification_page.v1 <https://github.com/openedx/frontend-app-account/tree/release/ulmo/src/plugin-slots/IdVerificationPageSlot>`_

Slots only available in the Authoring MFE:
******************************************

- `org.openedx.frontend.authoring.additional_course_content_plugin.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/AdditionalCourseContentPluginSlot>`_
- `org.openedx.frontend.authoring.additional_course_plugin.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/AdditionalCoursePluginSlot>`_
- `org.openedx.frontend.authoring.course_outline_header_actions.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseOutlineHeaderActionsSlot>`_
- `org.openedx.frontend.authoring.course_outline_page_alerts.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseOutlinePageAlertsSlot>`_
- `org.openedx.frontend.authoring.course_outline_sidebar.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseAuthoringOutlineSidebarSlot>`_
- `org.openedx.frontend.authoring.course_outline_subsection_card_extra_actions.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseOutlineSubsectionCardExtraActionsSlot>`_
- `org.openedx.frontend.authoring.course_outline_unit_card_extra_actions.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseOutlineUnitCardExtraActionsSlot>`_
- `org.openedx.frontend.authoring.course_unit_header_actions.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseUnitHeaderActionsSlot>`_
- `org.openedx.frontend.authoring.course_unit_sidebar.v2 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseAuthoringUnitSidebarSlot>`_
- `org.openedx.frontend.authoring.course_unit_sidebar.v1 <https://github.com/openedx/frontend-app-authoring/blob/release/ulmo/src/plugin-slots/CourseAuthoringUnitSidebarSlot/README.v1.md>`_
- `org.openedx.frontend.authoring.edit_file_alerts.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/EditFileAlertsSlot>`_
- `org.openedx.frontend.authoring.edit_video_alerts.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/EditVideoAlertsSlot>`_
- `org.openedx.frontend.authoring.files_upload_page_table.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseFilesSlot>`_
- `org.openedx.frontend.authoring.video_transcript_additional_translations_component.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/AdditionalTranslationsComponentSlot>`_
- `org.openedx.frontend.authoring.videos_upload_page_table.v1 <https://github.com/openedx/frontend-app-authoring/tree/release/ulmo/src/plugin-slots/CourseVideosSlot>`_

Slots only available in the Learner Dashboard MFE:
**************************************************

- `org.openedx.frontend.learner_dashboard.course_card_action.v1 <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/ulmo/src/plugin-slots/CourseCardActionSlot>`_
- `org.openedx.frontend.learner_dashboard.widget_sidebar.v1 <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/ulmo/src/plugin-slots/WidgetSidebarSlot>`_
- `org.openedx.frontend.learner_dashboard.course_list.v1 <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/ulmo/src/plugin-slots/CourseListSlot>`_
- `org.openedx.frontend.learner_dashboard.no_courses_view.v1 <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/ulmo/src/plugin-slots/NoCoursesViewSlot>`_
- `org.openedx.frontend.learner_dashboard.dashboard_modal.v1 <https://github.com/openedx/frontend-app-learner-dashboard/tree/release/ulmo/src/plugin-slots/DashboardModalSlot>`_

Slots only available in the Learning MFE:
*****************************************

- `org.openedx.frontend.layout.header_learning.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/HeaderSlot>`_
- `org.openedx.frontend.learning.content_iframe_error.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/ContentIFrameErrorSlot>`_
- `org.openedx.frontend.learning.content_iframe_loader.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/ContentIFrameLoaderSlot>`_
- `org.openedx.frontend.learning.course_breadcrumbs.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseBreadcrumbsSlot>`_
- `org.openedx.frontend.learning.course_exit_dashboard_footnote_link.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseExitPluginSlots/DashboardFootnoteLinkPluginSlot>`_
- `org.openedx.frontend.learning.course_exit_view_courses.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseExitPluginSlots/CourseExitViewCoursesPluginSlot>`_
- `org.openedx.frontend.learning.course_home_section_outline.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseHomeSectionOutlineSlot>`_
- `org.openedx.frontend.learning.course_outline_mobile_sidebar_trigger.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseOutlineMobileSidebarTriggerSlot>`_
- `org.openedx.frontend.learning.course_outline_sidebar_trigger.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseOutlineSidebarTriggerSlot>`_
- `org.openedx.frontend.learning.course_outline_sidebar.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseOutlineSidebarSlot>`_
- `org.openedx.frontend.learning.course_outline_tab_notifications.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseOutlineTabNotificationsSlot>`_
- `org.openedx.frontend.learning.course_recommendations.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/CourseExitPluginSlots/CourseRecommendationsSlot>`_
- `org.openedx.frontend.learning.gated_unit_content_message.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/GatedUnitContentMessageSlot>`_
- `org.openedx.frontend.learning.next_unit_top_nav_trigger.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/NextUnitTopNavTriggerSlot>`_
- `org.openedx.frontend.learning.notification_tray.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/NotificationTraySlot>`_
- `org.openedx.frontend.learning.notification_widget.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/NotificationWidgetSlot>`_
- `org.openedx.frontend.learning.notifications_discussions_sidebar_trigger.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/NotificationsDiscussionsSidebarTriggerSlot>`_
- `org.openedx.frontend.learning.notifications_discussions_sidebar.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/NotificationsDiscussionsSidebarSlot>`_
- `org.openedx.frontend.learning.progress_certificate_status.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/ProgressCertificateStatusSlot>`_
- `org.openedx.frontend.learning.progress_tab_certificate_status_main_body.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/ProgressTabCertificateStatusMainBodySlot>`_
- `org.openedx.frontend.learning.progress_tab_certificate_status_side_panel.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/ProgressTabCertificateStatusSidePanelSlot>`_
- `org.openedx.frontend.learning.progress_tab_course_grade.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/ProgressTabCourseGradeSlot>`_
- `org.openedx.frontend.learning.progress_tab_grade_breakdown.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/ProgressTabGradeBreakdownSlot>`_
- `org.openedx.frontend.learning.progress_tab_related_links.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/ProgressTabRelatedLinksSlot>`_
- `org.openedx.frontend.learning.sequence_container.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/SequenceContainerSlot>`_
- `org.openedx.frontend.learning.sequence_navigation.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/SequenceNavigationSlot>`_
- `org.openedx.frontend.learning.unit_title.v1 <https://github.com/openedx/frontend-app-learning/tree/release/ulmo/src/plugin-slots/UnitTitleSlot>`_

Special exams slots, available in MFEs that use ``frontend-lib-special-exams``:
*******************************************************************************

- `org.openedx.frontend.special_exams.submitted_timed_exam_instructions.v1 <https://github.com/openedx/frontend-lib-special-exams/tree/v4.1.0/src/plugin-slots/SubmittedTimedExamInstructionsSlot>`_

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
