Open edX Quince Release - Developer & Operator Notes
####################################################

These are the release notes for the Quince release, the 17th community release of the Open edX Platform, spanning changes from April 11 2023 to October 10 2023.  You can also review details about :doc:`index` or learn more about the `Open edX Platform`_.

.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
****************

* `Include and enable the Indigo theme in the default Open edX image <https://github.com/overhangio/tutor/issues/953>`__
  * Deployers running OpenEdX with the default theme and no additional plugins will have the Indigo theme enabled automatically.
* `Deployers must ensure that for all of their IDAs, any JWT_PUBLIC_SIGNING_JWK_SET Django setting does not contain whitespace inside of the Base64 strings of the encoded keys <https://github.com/openedx/edx-drf-extensions/blob/master/CHANGELOG.rst#880---2023-05-16>`__
* Django-storages upgraded to latest version and it has some breaking changes.
  * The constructor kwarg bucket is no longer accepted. Instead, use bucket_name.
  * define default_acl value explicitly in constructor kwarg e.g default_acl: public-read. in previous versions django-storages provides default value as public-read but now it is none. So it's important to mention it explicitly as per your use case.
* For Django 4.2 ``CSRF_TRUSTED_ORIGINS`` must include scheme. Update all urls there with schemes. e.g ``.edx.org`` changes to ``https://*.edx.org``.
* Docker requirements have changed: They are now: Docker v24.0.5+, with BuildKit 0.11+.

Learner Experiences
*******************

* A new Sidebar enhances the current discussion provider by enabling learners to interact with forums using a collapsible sidebar that accompanies course units. This replaces the use of discussion xblocks.

New course runs and re-runs created after you upgrade to quince will automatically use this new provider. However, existing course runs will not be affected.

To learn more about this upgrade, visit the `wiki page <https://openedx.atlassian.net/wiki/spaces/COMM/pages/3470655498/Discussions+upgrade+Sidebar+and+new+topic+structure>`__.

* `feat: fetch program subscription details <https://github.com/openedx/edx-platform/pull/32023>`__


Instructor Experiences
**********************

* `Copy and Paste For Course Content <https://docs.openedx.org/en/open-release-quince.master/educators/how-tos/copy_paste_course_components.html>`__

Administrators & Operators
**************************

New Learner Home Page
=====================

No longer experimental, the new Learner Home has many of the same features as the old learner dashboard, with some extended functionality and
performance enhancements.

* The Learner Home is now built with Paragon, the Open edX design pattern library. It is accessible and easy to style with brand colors.
* Course cards show the course thumbnail, information about the course, and the ability to upgrade to a paid track or view/begin a course (if applicable). Further course actions (e.g. unenroll, email opt-out settings, and social media share) have been moved to the menu/triple dot icon on the course card.
* Clicking the “Refine” button opens options to filter by course status or sort either by most recent enrollment (default) or title.

.. image:: /_images/community/release_notes/palm/new_learner_home_filtering.png
    :alt: The Refine pop-up with Course State and Sort options

* All of a user’s courses are fetched on page load. To make the page manageable, we paginate that list, showing 25 courses at a time. To view other courses, a user should page through their list of courses using the pagination controls at the bottom of the course list.

.. image:: /_images/community/release_notes/palm/new_learner_home_pagination.png
    :alt: Next, previous and page number buttons appear below the list of courses

* Site staff can now masquerade as users on the platform by typing a username or email in the “View as” box and hitting submit. This is designed to be “view only” so change actions (e.g. enroll, unenroll, selecting a session) are blocked in this view.
* There is a complete list of changes in the `Open edX wiki <https://openedx.atlassian.net/wiki/spaces/OEPM/blog/2022/11/21/3584589831/2U+New+Learner+Home+Page#Comparison-with-old-experience>`_.
* `feat: feature flag to disable Advanced Settings <https://github.com/openedx/edx-platform/pull/32015>`__
* `Tutor Credentials Plugin offers an admin panel where user can do configurations for the certificates of courses and programs. <https://github.com/overhangio/tutor-credentials>`__


New Settings:

* `EXAMS_DASHBOARD_MICROFRONTEND_URL <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/lms/envs/common.py#L4992>`__
* `ELASTIC_SEARCH_INDEX_PREFIX <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/lms/envs/common.py#L1410>`__

New Waffle Flags:

* `CREATE_COURSE_WITH_DEFAULT_ENROLLMENT_START_DATE <https://github.com/openedx/edxplatform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/xmodule/course_block.py#L61>`__
* `SHOW_REGISTRATION_LINKS <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/lms/envs/common.py#L782>`__
* `IGNORED_ERRORS[N]['LOG_ERROR'] <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/openedx/core/lib/request_utils.py#L162>`__
* `IGNORED_ERRORS[N]['LOG_STACK_TRACE'] <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/openedx/core/lib/request_utils.py#L162>`__
* `SEND_CERTIFICATE_CREATED_SIGNAL <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/lms/djangoapps/certificates/config.py#L20>`__
* `SEND_CERTIFICATE_REVOKED_SIGNAL <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/lms/djangoapps/certificates/config.py#L33>`__
* `TPA_AUTOMATIC_LOGOUT_ENABLED <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/lms/envs/common.py#L1263>`__
* `content_tagging.auto <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/openedx/core/djangoapps/content_tagging/toggles.py#L8>`__
* `contentstore.default_enable_flexible_peer_openassessments <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L519>`__
* `contentstore.enable_copy_paste_units <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L201>`__
* `contentstore.enable_studio_content_api <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L217>`__
* `contentstore.mock_video_uploads <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L500>`__
* `contentstore.new_studio_mfe.use_new_advanced_settings_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L300>`__
* `contentstore.new_studio_mfe.use_new_course_outline_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L300>`__
* `contentstore.new_studio_mfe.use_new_course_team_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L480>`__
* `contentstore.new_studio_mfe.use_new_custom_pageS <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L260>`__
* `contentstore.new_studio_mfe.use_new_export_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L380>`__
* `contentstore.new_studio_mfe.use_new_files_uploads_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L400>`__
* `contentstore.new_studio_mfe.use_new_grading_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L320>`__
* `contentstore.new_studio_mfe.use_new_import_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L360>`__
* `contentstore.new_studio_mfe.use_new_schedule_details_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L280>`__
* `contentstore.new_studio_mfe.use_new_unit_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L460>`__
* `contentstore.new_studio_mfe.use_new_updates_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L340>`__
* `contentstore.new_studio_mfe.use_new_video_uploads_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L420>`__
* `course_experience.relative_dates_disable_reset <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/openedx/features/course_experience/__init__.py#L55>`__
* `course_home.course_home_mfe_progress_tab <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/lms/djangoapps/course_home_api/toggles.py#L9>`__
* `courseware.learning_assistant <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/lms/djangoapps/courseware/toggles.py#L112>`__
* `courseware.mfe_courseware_search <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/lms/djangoapps/courseware/toggles.py#L58>`__
* `learner_dashboard.enable_b2c_subscriptions <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/lms/djangoapps/learner_dashboard/config/waffle.py#L41>`__
* `new_core_editors.use_video_gallery_flow <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L125>`__
* `new_editors.add_game_block_button <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L162>`__
* `new_studio_mfe.use_new_home_page <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/cms/djangoapps/contentstore/toggles.py#L241>`__
* `notifications.enable_notifications <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/openedx/core/djangoapps/notifications/config/waffle.py#L10>`__
* `notifications.show_notifications_tray <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/openedx/core/djangoapps/notifications/config/waffle.py#L21>`__
* `xblocks.xblock_skill_tag_verification <https://github.com/openedx/edx-platform/blob/d3d203cbac609adf23a6a8f003731fef12bd1ea1/xmodule/vertical_block.py#L38>`__

Removed Waffle Flags:

* BLOCK_STRUCTURES_SETTINGS['PRUNING_ACTIVE']
* EXPECTED_ERRORS[N]['IS_IGNORED']
* EXPECTED_ERRORS[N]['LOG_ERROR']
* EXPECTED_ERRORS[N]['LOG_STACK_TRACE']
* block_structure.invalidate_cache_on_publish
* contentstore.enable_copy_paste_feature
* learner_home_mfe.enable_learner_home_amplitude_recommendations
* registration.enable_failure_logging


Deprecations & Removals
***********************

* `We have deprecated and migrated the openedx/xblock-utils library into openedx/XBlock <https://github.com/openedx/XBlock/issues/675>`__

* `Most functionality has been removed from the long-deprecated Old Mongo Modulestore. For more details, please <https://github.com/openedx/public-engineering/issues/62>`__

* `BasicAuthentication as default authentication class in edx-platform <https://github.com/openedx/edx-platform/issues/33028>`__

* `Remove JWT_AUTH_REFRESH_COOKIE:  <https://github.com/openedx/public-engineering/issues/190>`__

* `feat: allow for forcing asymmetric jwts <https://github.com/openedx/edx-platform/pull/32045>`__

* `[DEPR]: Expected error part of EXPECTED_ERRORS <https://github.com/openedx/edx-platform/issues/32405>`__

* `[DEPR]: Remove JWT_AUTH_REFRESH_COOKIE - only in credentials <https://github.com/openedx/public-engineering/issues/190>`__

* `Remove bok-choy usage <https://github.com/openedx/credentials/issues/1989>`__

* `[DEPR]: BLOCK_STRUCTURES_SETTINGS['PRUNING_ACTIVE'] in edx-platform <https://github.com/openedx/public-engineering/issues/31>`__

* `[DEPR]: BasicAuthentication as default authentication class in edx-platform <https://github.com/openedx/edx-platform/issues/33028>`__

* `[DEPR]: Removal of Deprecated and unused feature flags from Mobile-Config Repo <https://github.com/openedx/public-engineering/issues/213>`__

* `[DEPR]: edx-user-state-client repo <https://github.com/openedx/public-engineering/issues/167>`__

* `[DEPR]: AnimationXBlock <https://github.com/openedx-unsupported/AnimationXBlock/issues/88>`__

* `[DEPR]: block_structure.invalidate_cache_on_publish in edx-platform <https://github.com/openedx/public-engineering/issues/33>`__

* `[DEPR]: edx-sphinx-theme  <https://github.com/openedx/public-engineering/issues/200>`__

* `[DEPR]: paver update_db <https://github.com/openedx/edx-platform/issues/32683>`__

* `[DEPR]: Remove FOOTER_ORGANIZATION_IMAGE django settings <https://github.com/openedx/public-engineering/issues/52>`__

* `[DEPR]: registration.enable_failure_logging <https://github.com/openedx/public-engineering/issues/84>`__


Developer Experience
********************

* `Hostname migration: local.overhang.io -> local.edly.io <https://github.com/overhangio/tutor/issues/945>`__
  * This should only effect plugin maintainers.

Known Issues
************

* `Search isn't available in the new Learner Dashboard <https://github.com/openedx/wg-build-test-release/issues/321>`__
