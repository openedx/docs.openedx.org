.. _Teak Dev Notes:

Open edX Teak Developer & Operator Release Notes
################################################

These are the developer & operator release notes for the Teak release, the 20th
community release of the Open edX Platform, spanning changes from October 24,
2024 to April 25, 2025. You can also review details about :ref:`Open edX Release Notes` or
learn more about the `Open edX Platform`_.

To view the end-user facing docs, see the :ref:`Teak Product Notes`.

.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
*****************

* MFEs have been updated to React 18. This may impact plugins and customizations that are not compatible with React 18.
* Please review :ref:`Removed Toggles (Teak)` and :ref:`Removed Settings (Teak)` for settings you may be using that have been removed in Teak.
* Be sure to review :ref:`DEPR (Teak)` as well.


Administrators & Operators
**************************

Settings and Toggles
====================

Added Feature Toggles
---------------------

* +ENABLE_CODEJAIL_DARKLAUNCH: `xmodule/capa/safe_exec/remote_exec.py (line 32) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/xmodule/capa/safe_exec/remote_exec.py#L32>`_
   * Default value = False
   * Description: Turn on to send requests to both the codejail service and the installed codejail library for [output truncated, see link for full description]

* +FEATURES['IN_CONTEXT_DISCUSSION_ENABLED_DEFAULT']: `cms/envs/common.py (line 567) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L567>`_
   * Default value = True
   * Description: Set to False to disable in-context discussion for units by default.

* +USE_EXTRACTED_ANNOTATABLE_BLOCK: `lms/envs/common.py (line 5555) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5555>`_
   * Default value = False
   * Description: Enables the use of the extracted annotatable XBlock, which has been shifted to the ``openedx/xblocks-contrib`` repo.

* +USE_EXTRACTED_DISCUSSION_BLOCK: `lms/envs/common.py (line 5595) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5595>`_
   * Default value = False
   * Description: Enables the use of the extracted Discussion XBlock, which has been shifted to the ``openedx/xblocks-contrib`` repo.

* +USE_EXTRACTED_HTML_BLOCK: `lms/envs/common.py (line 5585) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5585>`_
   * Default value = False
   * Description: Enables the use of the extracted HTML XBlock, which has been shifted to the ``openedx/xblocks-contrib`` repo.

* +USE_EXTRACTED_LTI_BLOCK: `lms/envs/common.py (line 5575) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5575>`_
   * Default value = False
   * Description: Enables the use of the extracted LTI XBlock, which has been shifted to the ``openedx/xblocks-contrib`` repo.

* +USE_EXTRACTED_POLL_QUESTION_BLOCK: `lms/envs/common.py (line 5565) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5565>`_
   * Default value = False
   * Description: Enables the use of the extracted poll question XBlock, which has been shifted to the ``openedx/xblocks-contrib`` repo.

* +USE_EXTRACTED_PROBLEM_BLOCK: `lms/envs/common.py (line 5605) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5605>`_
   * Default value = False
   * Description: Enables the use of the extracted Problem XBlock, which has been shifted to the ``openedx/xblocks-contrib`` repo.

* +USE_EXTRACTED_VIDEO_BLOCK: `lms/envs/common.py (line 5615) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5615>`_
   * Default value = False
   * Description: Enables the use of the extracted Video XBlock, which has been shifted to the ``openedx/xblocks-contrib`` repo.

* +USE_EXTRACTED_WORD_CLOUD_BLOCK: `lms/envs/common.py (line 5545) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5545>`_
   * Default value = False
   * Description: Enables the use of the extracted Word Cloud XBlock, which has been shifted to the ``openedx/xblocks-contrib`` repo.

* +contentstore.enable_course_optimizer: `cms/djangoapps/contentstore/toggles.py (line 622) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L622>`_
   * Default value = False
   * Description: This flag enables the course optimizer tool in the authoring MFE.

* +contentstore.use_react_markdown_editor: `cms/djangoapps/contentstore/toggles.py (line 222) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L222>`_
   * Default value = False
   * Description: This flag enables the use of the Markdown editor when creating or editing problems in the authoring MFE

.. _legacy-studio flags:

* +legacy_studio.advanced_settings: `cms/djangoapps/contentstore/toggles.py (line 259) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L259>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio Advanced Settings page.

* +legacy_studio.certificates: `cms/djangoapps/contentstore/toggles.py (line 450) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L450>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio Course Certificates page.

* +legacy_studio.configurations: `cms/djangoapps/contentstore/toggles.py (line 488) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L488>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio Configurations page.

* +legacy_studio.course_outline: `cms/djangoapps/contentstore/toggles.py (line 393) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L393>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio Course Outline editor.

* +legacy_studio.course_team: `cms/djangoapps/contentstore/toggles.py (line 431) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L431>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio Course Team page.

* +legacy_studio.custom_pages: `cms/djangoapps/contentstore/toggles.py (line 203) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L203>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio custom pages tab.

* +legacy_studio.exam_settings: `cms/djangoapps/contentstore/toggles.py (line 70) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L70>`_
   * Default value = False
   * Description: Temporarily fall back to the old proctored exam settings view.

* +legacy_studio.export: `cms/djangoapps/contentstore/toggles.py (line 335) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L335>`_
   * Default value = False
   * Description: Temporarily fall back to the old Course Export page.

* +legacy_studio.files_uploads: `cms/djangoapps/contentstore/toggles.py (line 354) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L354>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio Files &amp; Uploads page.

* +legacy_studio.grading: `cms/djangoapps/contentstore/toggles.py (line 278) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L278>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio Course Grading page.

* +legacy_studio.home: `cms/djangoapps/contentstore/toggles.py (line 184) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L184>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio logged-in landing page.

* +legacy_studio.import: `cms/djangoapps/contentstore/toggles.py (line 316) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L316>`_
   * Default value = False
   * Description: Temporarily fall back to the old Course Import page.

* +legacy_studio.logged_out_home: `cms/djangoapps/contentstore/toggles.py (line 642) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L642>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio “How it Works” page when unauthenticated

* +legacy_studio.problem_editor: `cms/djangoapps/contentstore/toggles.py (line 145) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L145>`_
   * Default value = False
   * Description: Temporarily fall back to the old Problem component (a.k.a. CAPA/problem block) editor.

* +legacy_studio.schedule_details: `cms/djangoapps/contentstore/toggles.py (line 240) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L240>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio Schedule &amp; Details page.

* +legacy_studio.text_editor: `cms/djangoapps/contentstore/toggles.py (line 89) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L89>`_
   * Default value = False
   * Description: Temporarily fall back to the old Text component (a.k.a. html block) editor.

* +legacy_studio.textbooks: `cms/djangoapps/contentstore/toggles.py (line 469) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L469>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio Textbooks page.

* +legacy_studio.unit_editor: `cms/djangoapps/contentstore/toggles.py (line 412) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L412>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio unit editing page.

* +legacy_studio.updates: `cms/djangoapps/contentstore/toggles.py (line 297) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L297>`_
   * Default value = False
   * Description: Temporarily fall back to the old Studio Course Updates page.

* +legacy_studio.video_editor: `cms/djangoapps/contentstore/toggles.py (line 108) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L108>`_
   * Default value = False
   * Description: Temporarily fall back to the old Video component (a.k.a. video block) editor.

* +send_to_submission_course.enable: `xmodule/capa/xqueue_interface.py (line 31) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/xmodule/capa/xqueue_interface.py#L31>`_
   * Default value = False
   * Description: Enables use of the submissions service instead of legacy xqueue for course problem submissions.

.. _Removed Toggles (Teak):

Removed Feature Toggles
-------------------------

* -FEATURES['ENABLE_BLAKE2B_HASHING']: `lms/envs/common.py (line 1060) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/lms/envs/common.py#L1060>`_
   * Description: Enables the memcache to use the blake2b hash algorithm instead of depreciated md4 for keys [output truncated, see link for full description]

* -FEATURES['ENABLE_EXAM_SETTINGS_HTML_VIEW']: `cms/djangoapps/contentstore/toggles.py (line 69) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L69>`_
   * Description: When enabled, users can access the new course authoring view for proctoring exams

* -FEATURES['ENABLE_HOME_PAGE_COURSE_API_V2']: `cms/envs/common.py (line 540) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/envs/common.py#L540>`_
   * Description: Enables the new home page course v2 API, which is a new version of the home page course [output truncated, see link for full description]

* -account.redirect_to_microfrontend: `openedx/core/djangoapps/user_api/accounts/toggles.py (line 29) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/openedx/core/djangoapps/user_api/accounts/toggles.py#L29>`_
   * Description: Supports staged rollout of a new micro-frontend-based implementation of the account page. [output truncated, see link for full description]

* -block_structure.storage_backing_for_cache: `openedx/core/djangoapps/content/block_structure/config/__init__.py (line 12) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/openedx/core/djangoapps/content/block_structure/config/__init__.py#L12>`_
   * Description: When enabled, block structures are stored in a more permanent storage, [output truncated, see link for full description]

* -contentstore.enable_studio_content_api: `cms/djangoapps/contentstore/toggles.py (line 214) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L214>`_
   * Description: Enables the new (experimental and unsafe!) Studio Content REST API for course authors,

* -contentstore.new_studio_mfe.use_new_advanced_settings_page: `cms/djangoapps/contentstore/toggles.py (line 297-2) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L297>`_
   * Description: This flag enables the use of the new studio advanced settings page mfe

* -contentstore.new_studio_mfe.use_new_certificates_page: `cms/djangoapps/contentstore/toggles.py (line 497) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L497>`_
   * Description: This flag enables the use of the new studio course certificates page mfe

* -contentstore.new_studio_mfe.use_new_course_outline_page: `cms/djangoapps/contentstore/toggles.py (line 437) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L437>`_
   * Description: This flag enables the use of the new studio course outline page mfe

* -contentstore.new_studio_mfe.use_new_course_team_page: `cms/djangoapps/contentstore/toggles.py (line 477) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L477>`_
   * Description: This flag enables the use of the new studio course team page mfe

* -contentstore.new_studio_mfe.use_new_custom_pages: `cms/djangoapps/contentstore/toggles.py (line 257) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L257>`_
   * Description: This flag enables the use of the new studio custom pages mfe

* -contentstore.new_studio_mfe.use_new_export_page: `cms/djangoapps/contentstore/toggles.py (line 377) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L377>`_
   * Description: This flag enables the use of the new studio export page mfe

* -contentstore.new_studio_mfe.use_new_grading_page: `cms/djangoapps/contentstore/toggles.py (line 317) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L317>`_
   * Description: This flag enables the use of the new studio grading page mfe

* -contentstore.new_studio_mfe.use_new_group_configurations_page: `cms/djangoapps/contentstore/toggles.py (line 537) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L537>`_
   * Description: This flag enables the use of the new studio course group configurations page mfe

* -contentstore.new_studio_mfe.use_new_import_page: `cms/djangoapps/contentstore/toggles.py (line 357) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L357>`_
   * Description: This flag enables the use of the new studio import page mfe

* -contentstore.new_studio_mfe.use_new_schedule_details_page: `cms/djangoapps/contentstore/toggles.py (line 277) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L277>`_
   * Description: This flag enables the use of the new studio schedule and details mfe

* -contentstore.new_studio_mfe.use_new_textbooks_page: `cms/djangoapps/contentstore/toggles.py (line 517) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L517>`_
   * Description: This flag enables the use of the new studio course textbooks page mfe

* -contentstore.new_studio_mfe.use_new_unit_page: `cms/djangoapps/contentstore/toggles.py (line 457) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L457>`_
   * Description: This flag enables the use of the new studio course outline page mfe

* -contentstore.new_studio_mfe.use_new_updates_page: `cms/djangoapps/contentstore/toggles.py (line 337) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L337>`_
   * Description: This flag enables the use of the new studio updates page mfe

* -contentstore.new_studio_mfe.use_new_video_uploads_page: `cms/djangoapps/contentstore/toggles.py (line 417) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L417>`_
   * Description: This flag enables the use of the new video uploads page mfe

* -course_modes.use_new_track_selection: `common/djangoapps/course_modes/views.py (line 50) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/common/djangoapps/course_modes/views.py#L50>`_
   * Description: This flag enables the use of the new track selection template for testing purposes before full rollout

* -learner_profile.redirect_to_microfrontend: `openedx/features/learner_profile/toggles.py (line 12) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/openedx/features/learner_profile/toggles.py#L12>`_
   * Description: Supports staged rollout of a new micro-frontend-based implementation of the profile page.

* -new_core_editors.use_advanced_problem_editor: `cms/djangoapps/contentstore/toggles.py (line 163) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L163>`_
   * Description: This flag enables the use of the new core problem xblock advanced editor as the default

* -new_core_editors.use_new_problem_editor: `cms/djangoapps/contentstore/toggles.py (line 144) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L144>`_
   * Description: This flag enables the use of the new core problem xblock editor

* -new_core_editors.use_new_text_editor: `cms/djangoapps/contentstore/toggles.py (line 88) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L88>`_
   * Description: This flag enables the use of the new core text xblock editor

* -new_core_editors.use_new_video_editor: `cms/djangoapps/contentstore/toggles.py (line 107) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L107>`_
   * Description: This flag enables the use of the new core video xblock editor

* -new_editors.add_game_block_button: `cms/djangoapps/contentstore/toggles.py (line 175) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L175>`_
   * Description: This flag enables the creation of the new games block

* -new_studio_mfe.use_new_home_page: `cms/djangoapps/contentstore/toggles.py (line 238) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/djangoapps/contentstore/toggles.py#L238>`_
   * Description: This flag enables the use of the new studio home page mfe

* -notifications.enable_new_notification_view: `openedx/core/djangoapps/notifications/config/waffle.py (line 53) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/openedx/core/djangoapps/notifications/config/waffle.py#L53>`_
   * Description: Waffle flag to enable new notification view

* -order_history.redirect_to_microfrontend: `openedx/core/djangoapps/user_api/accounts/toggles.py (line 9) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/openedx/core/djangoapps/user_api/accounts/toggles.py#L9>`_
   * Description: Supports staged rollout of a new micro-frontend-based implementation of the order history page.

Added Settings
---------------------

* +DISABLED_ORGS_FOR_PROGRAM_NUDGE: `lms/envs/common.py (line 5390) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5390>`_
   * Default value = "[]"
   * Description: List of organization codes that should be disabled

* +ORA_PEER_LEASE_EXPIRATION_HOURS: `lms/envs/common.py (line 3821) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L3821>`_
   * Default value = 8
   * Description: Amount of time before a lease on a peer submission expires

* +ORA_STAFF_LEASE_EXPIRATION_HOURS: `lms/envs/common.py (line 3826) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L3826>`_
   * Default value = 8
   * Description: Amount of time before a lease on a staff submission expires

* +LIBRARY_ENABLED_BLOCKS: `cms/envs/common.py (line 2904) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L2904>`_
   * Default value = "['problem', 'video', 'html', 'drag-and-drop-v2']"
   * Description: List of block types that are ready/enabled to be created/used

.. _Removed Settings (Teak):

Removed Settings
---------------------

* -DISABLED_COUNTRIES: `lms/envs/common.py (line 5535) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/lms/envs/common.py#L5535>`_
   * Description: List of country codes that should be disabled

* -WEBPACK_CONFIG_PATH: `lms/envs/common.py (line 2827) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/lms/envs/common.py#L2827>`_
   * Description: Path to the Webpack configuration file. Used by Paver scripts.

* -DISABLED_COUNTRIES: `cms/envs/common.py (line 2940) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/envs/common.py#L2940>`_
   * Description: List of country codes that should be disabled

* -JS_ENV_EXTRA_CONFIG: `cms/envs/common.py (line 1318) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/envs/common.py#L1318>`_
   * Description: JavaScript code can access this dictionary using ``process.env.JS_ENV_EXTRA_CONFIG`` [output truncated, see link for full description]

* -WEBPACK_CONFIG_PATH: `cms/envs/common.py (line 1509) <https://github.com/openedx/edx-platform/blob/a63a6a6fbaec6bf1c234b9b26b66c7b50c00e336/cms/envs/common.py#L1509>`_
   * Description: Path to the Webpack configuration file. Used by Paver scripts.

Other Operator Changes
======================

- The Authoring MFE is now the default course authoring experience, and the
  legacy experience will be removed in Ulmo. See :ref:`Studio Changes (Teak)`
  for more details.

  - Operators can, for the Teak release, revert back to legacy Studio pages
    using the ``legacy_studio.*`` flags detailed in the :ref:`Toggles section
    above <legacy-studio flags>` on a page-by-page basis. These flags will be
    removed in Ulmo.

- In LMS and CMS, Celery now uses task protocol 2.
   - *Action*: Any operator using custom Celery tooling should ensure it is compatible with protocol 2. For other operators, no action is required.
   - *Background*: Celery 4.0 `switched how task messages are structured <https://docs.celeryq.dev/en/stable/history/whatsnew-4.0.html#new-protocol-highlights>`_ and
     the new message format is called protocol 2. The version of Celery we currently use (anything >=4.0) can create and consume both protocol versions and it should
     be safe to switch between them with zero downtime.

      - By default, Celery 4.0 and higher produce messages in this format, and Celery 3.1.25 and higher can read messages in this format.
      - edx-platform was pinned to protocol 1 `during the upgrade <https://github.com/openedx/edx-platform/pull/24916>`_ to Celery 4, presumably as a precaution. 
        This change is the long-delayed unpinning of the protocol version so that Celery can use its default version.
      - Operators can still override the protocol version using the Django setting ``CELERY_TASK_PROTOCOL`` although there is no guarantee that protocol 1 compatibility
        will be preserved in the future.

- When codejail is used by LMS and CMS, it no longer requires write access to the sandbox virtualenv ``.config`` or ``.cache`` directories.
   - *Action*: If you run codejail, it is recommended that you remove write permissions to ``<SANDENV>/.config`` and ``<SANDENV>/.cache`` from your AppArmor profile,
     if possible.
   - *Background*: Running ``import matplotlib`` in a custom Python-evaluated XBlock in Sumac and earlier required the AppArmor profile to allow write access to one of 
     these directories. In Teak, `edxapp now sets <https://github.com/openedx/edx-platform/pull/36456>`_ the `MPLCONFIGDIR` environment variable for inputs sent to
     codejail, so matplotlib will now write to the ``./tmp/`` subdirectory inside the codejail-created sandbox.

      - You should be able to identify these exclusions by looking for lines like ``/home/sandbox/.config/ wrix``, although the exact parent directory may vary. Other
        temporary directories may have been allowed instead, such as ``/tmp``. Any such write permission to a global directory is inadvisable, since it reduces the 
        ability of codejail to perform effective sandboxing. Removing these lines in Teak will (appropriately) reduce the permissions of sandboxed code. They should 
        not be removed before Teak, however, as this will cause matplotlib to fail to load.
      - Operators who have not previously needed to support matplotlib in instructor or learner code may not have these 
        exclusions in their AppArmor configurations.
        If this is your situation, no action is required.
      - Removing these lines may cause other, unanticipated failures in sandboxed code. Monitor your codejail logs and 
        failure rates when deploying this change.
- **All MFEs have been upgraded to React 18**.  If you have forked an MFE and want to pull in the upstream changes from Teak, you will need to ensure all dependencies work with React 18.

- MFE slots now follow a versioned naming convention, for example, ``footer_slot`` is now ``org.openedx.frontend.layout.footer.v1``.

  - Aliases are present for existing slots, and will be throughout the lifecycle of the available slot. Any version bump to a slot will have an associated DEPR ticket.
  - See the `slot renaming ADR <https://github.com/openedx/frontend-plugin-framework/blob/master/docs/decisions/0003-slot-naming-and-life-cycle.rst>`_ for more details on the new naming scheme. All new slots will use this naming scheme, and developers making new slots should pay attention to the ADR.

- New feature: Codejail local/remote darklaunch

  .. admonition:: Not relevant to Tutor deployments
   
   This is not relevant to Tutor, which does not support local codejail.

  -  **Audience:** Deployers who support codejail (e.g. custom Python-graded problem blocks) and are not already using a 
     remote codejail service.

  - **Background:** Historically, codejail execution has been performed on the same hosts as LMS and CMS, aka “local codejail”. There is a new 
    `codejail-service <https://github.com/openedx/codejail-service>`_ that allows performing this code execution 
    remotely. This allows for additional security
    restrictions, and the new code includes several security enhancements.

  - **Purpose:** The darklaunch feature allows operators to gain confidence in preparing for a switch from local to remote 
    codejail. When enabled, it can send all 
    codejail executions to both local and remote codejail, while only using the results of the local execution and 
    suppressing all errors from the remote side. 
    This allows operators to discover issues in the remote service’s configuration under real production traffic
    conditions.

  - **Usage:** To use darklaunch to switch from local to remote:

    - Create a codejail-service cluster
    - Configure LMS and CMS to call it by configuring ``CODE_JAIL_REST_SERVICE_HOST`` but not ``ENABLE_CODEJAIL_REST_SERVICE`` (which must remain disabled for the moment).
    - Begin the dark launch by setting ``ENABLE_CODEJAIL_DARKLAUNCH`` to true. Traffic will begin flowing to the new service, but the results will be ignored.

      - The only user-visible impact should be that codejail executions take twice as long, as the local and remote executions are performed serially.

    - Observe telemetry to discover errors and behavior mismatches.

      - Mismatches can include:

        - One side failed to execute entirely (“unexpected error”) while the other did not. This might include network issues.
        - One side returned an error from the submitted code, while the other did not, or produced a different error.
        - Both sides succeeded, but the returned globals dictionaries differed.

      - Error and warning logs from ``safe_exec.py`` in edxapp containing ``codejail darklaunch`` will tell you about configuration problems, unexpected errors, and mismatches in behavior between the two environments.
      - Span-based telemetry (New Relic, Datadog, etc.) can be used to track rates of mismatches and break them down by course ID and type. See ``set_custom_attribute`` calls starting with ``codejail``. in `safe_exec.py <https://github.com/openedx/edx-platform/blob/release/teak.master/xmodule/capa/safe_exec/safe_exec.py>`_  
           for available attributes. The local-only, remote-only and local/remote darklaunch calls all have different span names as well, e.g. ``safe_exec.remote_exec_darklaunch``.
      - Use ``CODEJAIL_DARKLAUNCH_EMSG_NORMALIZERS`` to normalize away spurious mismatches between the environments. (Not all mismatches can be readily ignored, such 
           as ordering differences in sets.)

    - Once behavior and performance differences are resolved, remove ``ENABLE_CODEJAIL_DARKLAUNCH`` and set ``ENABLE_CODEJAIL_REST_SERVICE`` to true. This will complete the migration, and codejail executions will only be performed on the remote service.

.. _Accredible Badging Configuration:

- **New feature**: Accredible Integration for Open edX Credentials Badges. See :ref:`Badging (Teak)` for more product details. Configuration instructions are as follows:

  - **Audience:** Operators and deployers who wish to issue digital badges from Accredible.

  - **History:** previously Verifiable Credentials sharing and Credly integration were implemented to provide a new credentials sharing 
    capabilities to the Open edX ecosystem. Now we provide another integration option for Providers.

  - **Purpose:** Add another badging backend to Open edX Credentials.

  - **Usage:**

    - For tutor based deployments, install and enable the `tutor-contrib-badges <https://github.com/raccoongang/tutor-contrib-badges/tree/teak>`_ plugin. See that plugin’s README for details.

    - Besides the Accredible integration, the Tutor plugin that adds and configuring features for sharing to different "providers":

      - `Verifiable Credentials <https://edx-credentials.readthedocs.io/en/latest/verifiable_credentials/overview.html#>`_ with different credential stores that support standards like VC1.1, OBv3 such as `LCWallet <https://lcw.app/>`_ for example.

        - program certificate

        - course certificate

      - Badges:

        - `Credly <https://info.credly.com/>`_
        - `Accredible <https://www.accredible.com/>`_

  - To start using this feature an Accredible account is necessary.

    - Register on Accredible and create your account.
    - Create at least 1 group.

  - Badges feature is optional and it is disabled by default. So, it must be enabled to be accessible::

      # LMS service:
      FEATURES["BADGES_ENABLED"] = True

      # Credentials service:
      BADGES_ENABLED = True
         
.. _DEPR (Teak):

Deprecations & Removals
***********************

- [UPCOMING] In Ulmo, pre-design-tokens brand packages will no longer be
  supported. With design tokens, theme authors will instead override core
  Paragon tokens by defining their own JSON tokens that get deep merged
  alongside the core Paragon tokens, thus overriding any tokens that were
  defined by the theme author. See `the associated DEPR ticket for details
  <https://github.com/openedx/brand-openedx/issues/23>`_, and follow the
  :ref:`Ulmo Design Tokens` page for more detail. Operators will be able to try
  out Design Tokens using the `Teak Design Tokens branches <https://openedx.atlassian.net/wiki/spaces/BPL/pages/5050499077/Using+Teak+Design+Tokens+branches>`_.

- `[DEPR]: block_structure.storage_backing_for_cache in edx-platform <https://github.com/openedx/public-engineering/issues/32>`_ This is a simplification to how course content is cached. It should be invisible to all end users.

- The flag ``ENABLE_BLAKE2B_HASHING`` was removed. blake2b hashing is now used for caching instead of the deprecated md4 hashing. After upgrading, it’s possible that performance could be degraded as the cache rebuilds. 

- `[DEPR]: django-oauth2-provider (DOP) related tables <https://github.com/openedx/public-engineering/issues/82>`_

  - For LMS and CMS, there is a new script to 
    `clean up old DOP-related authentication tables. <https://github.com/edx/configuration/blob/master/util/drop_dop_tables/drop_dop_tables.py>`_
  - If you have an old installation of the Open edX platform (Palm or earlier), you may have many outdated/unused 
    authentication-related tables that can lead to confusion when looking at the database.
  - The script is not related to Teak other than it now being available, and should be ok to run on any installation using Palm, Redwood, or Sumac.

- `[DEPR]: Support for footer replacement via npm installing forked footers <https://github.com/openedx/frontend-component-footer/issues/459>`_

  - It is possible to work around this breaking change by also exporting your forked ``Footer`` component as ``FooterSlot`` and your forked ``StudioFooter`` component as ``StudioFooterSlot``

- `[DEPR]: DISPLAY_COURSE_SOCK_FLAG <https://github.com/openedx/edx-platform/issues/36429>`_

  - The ``DISPLAY_COURSE_SOCK_FLAG`` was a waffle flag that was used to determine whether verification related upsell messaging
    should be displayed in the courseware. This data was used to determine whether the sock should be displayed in the legacy
    courseware which is itself `deprecated <https://github.com/openedx/edx-platform/issues/35803>`_.

Researcher & Data Experiences
*****************************

Upgrading to `Aspects v2.3.1 <https://github.com/openedx/tutor-contrib-aspects/releases/tag/v2.3.1>`_
will give you the latest Aspects functionality with Teak, including :ref:`In-Context Analytics (Teak)`. See the upgrade instructions here:
:doc:`openedx-aspects:technical_documentation/how-tos/upgrade`.

Next, be sure to:

* Enable the ``ASPECTS_ENABLE_STUDIO_IN_CONTEXT_METRICS`` toggle - Enables or
  disables in-context metrics.

* Ensure this setting: ``ASPECTS_IN_CONTEXT_DASHBOARDS`` is populated - A
  dictionary mapping block types to in-context dashboards. You can use this
  option to remove or replace the in-context dashboard for a block type. The key
  course defines the in-context dashboard for course overview.

* And finally, to ensure in-context analytics are enabled, be sure to rebuild
  your MFE image::

   tutor images build mfe --no-cache

Mobile Updates
***************

No new changes were introduced in Teak. See :ref:`Mobile Updates Teak` for more detail.

Known Issues
************

See the `Build Test Release project board <https://github.com/orgs/openedx/projects/28>`_ for known open issues.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|  June 2025   |  BTR                          |  Teak          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
