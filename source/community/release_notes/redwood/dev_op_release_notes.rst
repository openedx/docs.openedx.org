Open edX Redwood Release - Developer and Operator Release Notes
###############################################################

These are the Developer and Operator release notes for the Redwood release, the
18th community release of the Open edX Platform, spanning changes from October
10 2023 to May 09 2024. You can also review details about `earlier releases`_ or
learn more about the `Open edX Platform`_.

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
****************

-  Deployers must ensure that their
   ``JWT_AUTH['JWT_PRIVATE_SIGNING_JWK']`` Django setting in LMS
   contains the full complement of private key ``numbers.*``

   -  Background: In LMS, we switched from the pyjwkest
      library to PyJWT for signing JWTs. (pyjwkest is now unmaintained.)
      However, PyJWT has stricter requirements for the private key in
      ``JWT_PRIVATE_SIGNING_JWK``. Before you upgrade to Redwood, you
      will need to update this key using a script. Otherwise, JWT
      signing will fail, and users will be unable to log in.

   -  Steps:

      1. Locate ``JWT_PRIVATE_SIGNING_JWK`` in your deployment
         configuration.

      2. Check if the JSON contains all of the following params: ``p``,
         ``q``, ``dp``, ``dq``, and ``qi``. If it does, you don't need
         to do anything further. Otherwise, continue.

      3. In your edx-platform virtualenv, run
         ``python3 scripts/jwk-precompute-params.py`` and follow the
         prompts. (It will ask you to paste in the current JSON.)

      4. Update your config's ``JWT_AUTH['JWT_PRIVATE_SIGNING_JWK']``
         with the output of the script.

      5. You may wish to compare the contents of the private key before
         and after running the script, and verify that the only changes
         it has made to the contents of the JSON are that the ``p``,
         ``q``, ``dp``, ``dq``, and ``qi`` params have been added. (Some
         or all may already have been present.)

   -  Notes:

      1. This should be done while you are still running Quince—it is
         safe to do ahead of the upgrade, and should not have any
         visible effect at that time.

      2. This key must be handled very carefully. Anyone in possession
         of the key may impersonate users.

- `studio_home.enable_global_staff_optimization flag no longer works in Studio MFE <https://github.com/openedx/wg-build-test-release/issues/380>`_
   - Background: This flag works for the legacy Studio Home, improving performance by
     adding an organization search bar.  This flag does not work in the Studio Home MFE, as it
     is not needed within the MFE. The MFE already have a search bar and pagination, which
     improves performance for those home pages with lots of courses.

Learner & Instructor Experiences
********************************

For in-depth information on new learner and instructor facing features in the
Redwood release, please see the :doc:`feature_release_notes`. Instructions on how
to enable those features which need configuration are as follows.

.. _redwood-enable-search:

Enabling Studio Course Search
=============================

-  The Redwood release includes the :doc:`/community/release_notes/redwood/course_search`,
   which is disabled by default as it depends on a new search engine,
   Meilisearch. We encourage operators to install Meilisearch, test out this
   feature, and give us feedback on the viability of using Meilisearch as a
   replacement for Elasticsearch in future Open edX releases. Here's how to
   enable it:

   -  For tutor-based deployments, install the `tutor-contrib-mailsearch
      <https://github.com/open-craft/tutor-contrib-meilisearch>`_ plugin, and
      apply the changes to your deployment. See that plugin's README for
      details. Note in particular that the hostname configured as
      ``MEILISEARCH_PUBLIC_HOST`` must be resolvable on the public internet.

   -  If you are not using Tutor, you'll need to install Meilisearch manually
      (or use the cloud product) and explicitly set `the related config
      variables
      <https://github.com/openedx/edx-platform/blob/aac70563fd8a1492af25ae1b9aa9d14c42b36a18/cms/envs/common.py#L2958-L2969>`_
      in the CMS as well as set ``MEILISEARCH_ENABLED=true`` in the Course
      Authoring MFE settings.

   -  Whether or not you're using Tutor, you'll need to create and populate the
      search index. To do so, you must run a one-time command from the CMS
      shell: ``python manage.py cms reindex_studio --experimental``. This
      command may take a while if you have a lot of courses and/or libraries in
      Studio; it will display regular progress indicators while it is running.
      We are interested in hearing how long it takes for you - please share your
      experience (see next bullet). This command reads from MySQL/MongoDB but
      does not write to them; it only writes to Meilisearch. Once the indexing
      has completed, it should not be necessary to run it again; from that point
      forward, the indexes will be updated automatically as needed.

   -  Please share your feedback about Meilisearch, indexing, and operations in
      `this Discourse thread
      <https://discuss.openedx.org/t/is-meilisearch-a-viable-upgrade-alternative-to-opensearch/12400>`_
      or the `#ops <https://openedx.slack.com/archives/C08B4LZEZ>`_ Slack
      channel. Please share feedback about the new course search feature in
      general `in the discussion forums
      <https://discuss.openedx.org/t/feedback-thread-new-course-search/13076>`_
      or in the `#wg-product-core
      <https://openedx.slack.com/archives/C057J2D1WU9>`_ Slack channel.

.. _redwood-enable-sidebar:

Courseware Sidebar
==================

To enable the new Courseware Sidebar, set the
``courseware.enable_navigation_sidebar`` waffle flag to True.

Connect Teams in a course to Content Groups
===========================================

#. Go to your site's Django Admin Panel

#. Enable the teams feature by turning on the waffle flag:
   ``teams.enable_teams_app``

#. Then, turn on the ``teams.content_groups_for_teams`` waffle flag for everyone
   or specific courses with a waffle flag course overrides

Make Sections available independently of the course outline
===========================================================

Enable this feature flag: ``FEATURES["ENABLE_HIDE_FROM_TOC_UI"] = True`` to your
deployment configurations to enable the feature system-wide.

Administrators & Operators
**************************

.. _redwood-settings-toggles:

Settings and Toggles
====================

Waffle flags added In Redwood:

* `ANONYMOUS_SURVEY_REPORT <https://github.com/openedx/edx-platform/blob/7d11c889bbbf55dfa69c734122de72d83c1893bf/lms/envs/common.py#L5523>`_
* `ENFORCE_SESSION_EMAIL_MATCH <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/envs/common.py#L5110>`_
* `FEATURES['ENABLE_BLAKE2B_HASHING'] <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/envs/common.py#L1068>`_
* `FEATURES['ENABLE_CERTIFICATES_INSTRUCTOR_MANAGE] <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/djangoapps/instructor/settings/common.py#L95>`_
* `FEATURES['ENABLE_COURSEWARE_SEARCH_VERIFIED_REQUIRED'] <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/envs/common.py#L1059>`_
* `FEATURES['ENABLE_GRADING_METHOD_IN_PROBLEMS'] - LMS <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/envs/common.py#L1050>`_
* `FEATURES['ENABLE_GRADING_METHOD_IN_PROBLEMS'] - CMS <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/cms/envs/common.py#L575>`_
* `FEATURES['ENABLE_HIDE_FROM_TOC_UI'] <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/cms/envs/common.py#L555>`_
* `FEATURES['ENABLE_HOME_PAGE_COURSE_API_V2'] <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/cms/envs/common.py#L565>`_
* `FEATURES['ENABLE_LTI_PII_ACKNOWLEDGEMENT'] <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/cms/envs/common.py#L497>`_
* `FEATURES['ENABLE_SEND_XBLOCK_LIFECYCLE_EVENTS_OVER_BUS'] <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/cms/envs/common.py#L542>`_
* `FEATURES['SEND_LEARNING_CERTIFICATE_LIFECYCLE_EVENTS_TO_BUS'] <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/envs/common.py#L1038>`_
* `JWT_AUTH_ADD_KID_HEADER: <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/openedx/core/djangoapps/oauth_dispatch/jwt.py#L279>`_
* `SURVEY_REPORT_ENABLE <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/envs/common.py#L5571>`_
* `agreements.enable_lti_pii_acknowledgement <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/openedx/core/djangoapps/agreements/toggles.py#L8>`_
* `commerce.transition_to_coordinator.checkout <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/djangoapps/commerce/waffle.py#L9>`_
* `commerce.transition_to_coordinator.refund <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/djangoapps/commerce/waffle.py#L23>`_
* `content_tagging.disabled <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/openedx/core/djangoapps/content_tagging/toggles.py#L22>`_
* `course_home.new_discussion_sidebar_view <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/djangoapps/course_home_api/toggles.py#L24>`_
* `teams.content_groups_for_teams <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/openedx/core/lib/teams_config.py#L22>`_
* `courseware.always_open_auxiliary_sidebar <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/djangoapps/courseware/toggles.py#L98>`_
* `courseware.disable_navigation_sidebar_blocks_caching <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/djangoapps/courseware/toggles.py#L71>`_
* `courseware.discovery_default_language_filter <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/djangoapps/courseware/toggles.py#L159>`_
* `courseware.enable_navigation_sidebar <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/djangoapps/courseware/toggles.py#L86>`_
* `discussions.enable_reported_content_notifications <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/djangoapps/discussion/toggles.py#L16>`_
* `notifications.enable_coursewide_notifications <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/openedx/core/djangoapps/notifications/config/waffle.py#L41>`_
* `notifications.enable_email_notifications <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/openedx/core/djangoapps/notifications/config/waffle.py#L61>`_
* `notifications.enable_notifications_filters <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/openedx/core/djangoapps/notifications/config/waffle.py#L31>`_
* `notifications.enable_ora_staff_notifications <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/openedx/core/djangoapps/notifications/config/waffle.py#L51>`_
* `student.redirect_to_courseware_after_enrollment <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/common/djangoapps/student/toggles.py#L29>`_
* `studio.enable_course_update_notifications <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/cms/djangoapps/contentstore/config/waffle.py#L58>`_
* `user_tours.tours_disabled <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/lms/djangoapps/user_tours/toggles.py#L7>`_
* `video_config.transcript_feedback <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/openedx/core/djangoapps/video_config/toggles.py#L19>`_
* `video_config.xpert_translations_ui <https://github.com/openedx/edx-platform/blob/b3df1ddb670e9d4dfd68d1a696ea528aed859550/openedx/core/djangoapps/video_config/toggles.py#L30>`_
* `ENABLE_AUTO_GENERATED_USERNAME <https://github.com/openedx/edx-platform/blob/7d11c889bbbf55dfa69c734122de72d83c1893bf/openedx/core/djangoapps/user_authn/toggles.py#L38>`_
* `EDX_DRF_EXTENSIONS[ENABLE_JWT_AND_LMS_USER_EMAIL_MATCH] <https://github.com/openedx/edx-drf-extensions/blob/85880da4c50fcfd7d3d5190444b848ae9f174968/edx_rest_framework_extensions/config.py#L19>`_
* `FEATURES['ENABLE_ORA_SELECTABLE_LEARNER_WAITING_REVIEW'] <https://github.com/openedx/edx-ora2/blob/8b320d69745a92aa64696c5f2617bd76dff88cb3/openassessment/xblock/config_mixin.py#L175>`_
* `enterprise.enterprise_groups_v1 <https://github.com/openedx/edx-enterprise/blob/007abaf5b10707607d47a9f9d89572b36d18b8e2/enterprise/toggles.py#L34>`_
* `enterprise.feature_prequery_search_suggestions <https://github.com/openedx/edx-enterprise/blob/007abaf5b10707607d47a9f9d89572b36d18b8e2/enterprise/toggles.py#L22>`_
* `EVENT_BUS_PRODUCER_CONFIG['org.openedx.content_authoring.course.catalog_info.changed.v1'] <https://github.com/openedx/edx-platform/blob/7d11c889bbbf55dfa69c734122de72d83c1893bf/cms/envs/common.py#L2849>`_
* `EVENT_BUS_PRODUCER_CONFIG['org.openedx.learning.course.unenrollment.completed.v1'] <https://github.com/openedx/edx-platform/blob/7d11c889bbbf55dfa69c734122de72d83c1893bf/lms/envs/common.py#L5428>`_
* `EVENT_BUS_PRODUCER_CONFIG['org.openedx.learning.xblock.skill.verified.v1'] <https://github.com/openedx/edx-platform/blob/7d11c889bbbf55dfa69c734122de72d83c1893bf/lms/envs/common.py#L5443>`_

.. _course-authoring-flags:

Flags specific to the new Course Authoring MFE
----------------------------------------------

Every page in the new Course Authoring MFE can be toggled on and off
individually. By default, these flags default to True when using Tutor.

* `new_studio_mfe.use_new_home_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L225>`_
* `contentstore.new_studio_mfe.use_new_custom_pages
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L244>`_
* `contentstore.new_studio_mfe.use_new_schedule_details_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L264>`_
* `contentstore.new_studio_mfe.use_new_advanced_settings_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L284>`_
* `contentstore.new_studio_mfe.use_new_grading_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L304>`_
* `contentstore.new_studio_mfe.use_new_updates_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L324>`_
* `contentstore.new_studio_mfe.use_new_import_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L344>`_
* `contentstore.new_studio_mfe.use_new_export_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L364>`_
* `contentstore.new_studio_mfe.use_new_files_uploads_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L384>`_
* `contentstore.new_studio_mfe.use_new_video_uploads_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L404>`_
* `contentstore.new_studio_mfe.use_new_course_outline_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L424>`_
* `contentstore.new_studio_mfe.use_new_unit_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L444>`_
* `contentstore.new_studio_mfe.use_new_course_team_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L464>`_
* `contentstore.new_studio_mfe.use_new_certificates_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L484>`_
* `contentstore.new_studio_mfe.use_new_textbooks_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L504>`_
* `contentstore.new_studio_mfe.use_new_group_configurations_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L524>`_
* `contentstore.new_studio_mfe.use_new_textbooks_page
  <https://github.com/openedx/edx-platform/blob/f256684646aec6fd0d5519c6900ec99077e7db50/cms/djangoapps/contentstore/toggles.py#L504>`_

Within the Tutor MFE plugin, `additional flags must be set
<https://github.com/overhangio/tutor-mfe/commit/68fa38778aa96f44a0f41893c1c9318ba3aaeed7>`_.

* ``MFE_CONFIG["ENABLE_ASSETS_PAGE"]``
* ``MFE_CONFIG["ENABLE_HOME_PAGE_COURSE_API_V2"]``
* ``MFE_CONFIG["ENABLE_PROGRESS_GRAPH_SETTINGS"]``
* ``MFE_CONFIG["ENABLE_TAGGING_TAXONOMY_PAGES"]``


Other Operator Changes
======================

-  The default minimum password length has been updated from 2
   characters to 8 characters. `(PR) <https://github.com/openedx/edx-platform/pull/33373>`_.

   -  For users with an existing password, this change alone will not
      force them to update it. However if they reset their password or go
      to change it, they'll have to conform to the new guidelines. If you
      would like to force people to update their password, you
      should take a look at `the password_policy plugin and its settings <https://github.com/openedx/edx-platform/blob/2033dcf6ace133719aaeb72dc5dd6ee521a7ac42/openedx/core/djangoapps/password_policy/settings/common.py#L13>`_

-  The Credentials service `updated some requirements <https://github.com/openedx/credentials/commit/1cd7c25c04a955aa9aaa263fb40ebd3f73d0937e>`_ and may have implications for anyone
   who has a massive ``usersocialauth`` table.  This is because that
   table grows endlessly, and the migrations on the table caused by
   updating the ``social-auth-app-django`` package can run out of
   memory. If maintainers have migration failures on this upgrade, they
   should run the management command `truncate_social_auth <https://github.com/openedx/credentials/blob/master/credentials/apps/core/management/commands/truncate_social_auth.py>`_.

   -  This will remove all entries from the ``usersocialauth`` table
      that haven't been updated in 90 days, which makes the size of the
      table tractable for the dependency's migration. This is harmless
      in the ``Credentials`` IDA.

-  The scripts related to user retirement across all services
   have been moved to the ``edx-platform`` repository. If you've been
   using the `unsupported tubular repository <https://github.com/openedx-unsupported/tubular>`_ to run retirement scripts you should update
   your code.

   -  Relevant Tickets

      - `Move user retirement code to edx-platform and drop it from Tubular <https://github.com/openedx/axim-engineering/issues/881>`_.
      - `Move user retirement scripts code from the tubular repo <https://github.com/openedx/edx-platform/pull/34063>`_.
      - `Deprecate User Retirement Scripts <https://github.com/openedx-unsupported/tubular/pull/736>`_.

-  edx-platform and cs_comment_service Mongo Upgrades
      - Operators will need to `update their Mongo databases to Mongo 7 <https://www.mongodb.com/docs/manual/tutorial/upgrade-revision/#upgrade-to-the-latest-patch-release-of-mongodb>`_ to ensure their deployments don't break in the future. 
      - Operators will need to update their forums' Ruby version from 3.0 to 3.3.
      - If you're running Tutor and your Mongo/Ruby are in Tutor, they will get automatically upgraded.
      - `chore: add mongo 7 to testing matrix <https://github.com/openedx/edx-platform/pull/34213>`_.
      - `build: Build with newer ruby and mongo versions. <https://github.com/openedx/cs_comments_service/pull/426>`_.


Deprecations & Removals
***********************

-  Badges app has been deprecated and removed from ``edx-platform``.
   See `[DEPR]: lms/djangoapps/badges <https://github.com/openedx/edx-platform/issues/31541>`_ .
-  - In edxapp, the Waffle switch ``ip.legacy`` is removed. See `[DEPR]: legacy_ip code and Waffle switch <https://github.com/openedx/edx-platform/issues/33733>`_ .

   -  Any deployment that has been relying on this legacy IP address
      option will need to switch to setting
      ``CLOSEST_CLIENT_IP_FROM_HEADERS`` appropriately. See `Nutmeg Announcement <https://openedx.atlassian.net/wiki/spaces/COMM/pages/3205201949/Nutmeg#CLOSEST_CLIENT_IP_FROM_HEADERS>`_ for
      details.
-  Asset Processing (webpack, collectstatic, etc.) using Paver Commands in edx-platform is now Deprecated and will not be available in Sumac

   - `[DEPR] Asset processing in Paver`_.
   -  *Non deployment paver commands will be removed by Sumac*

-  The ``django-splash`` capability was removed from ``edx-platform`` and the relevant code has been archived.

   - https://github.com/openedx/public-engineering/issues/224

Flags and toggles removed in Redwood
==================================== 

* ``accomplishments_shared`` field is removed from payloads and settings
* ``ENABLE_OPENBADGES``, ``ENABLE_SEND_XBLOCK_EVENTS_OVER_BUS`` are no longer available for configuration in ``FEATURES`` 
* ``BADGING_BACKEND``, ``BADGR_BASE_URL``, ``BADGR_ISSUER_SLUG``,
* ``BADGR_USERNAME``, ``BADGR_PASSWORD``,
* ``BADGR_TOKENS_CACHE_KEY``, ``BADGR_TIMEOUT``,
* ``BADGR_ENABLE_NOTIFICATIONS``, ``SEND_CERTIFICATE_REVOKED_SIGNAL``,
* ``blockstore.use_blockstore_app_api``,
* ``contentstore.enable_copy_paste_units``,
* ``course_apps.proctoring_settings_modal_view``,
* ``course_live.enable_big_blue_button``,
* ``course_live.enable_course_live``,
* ``courseware.learning_assistant``,
* ``discussions.enable_learners_stats``,
* ``discussions.enable_learners_tab_in_discussions_mfe``,
* ``discussions.enable_moderation_reason_codes``,
* ``discussions.enable_reported_content_email_notifications``,
* ``learner_recommendations.enable_course_about_page_recommendations``,
* ``learner_recommendations.enable_dashboard_recommendations``,
* ``student.enable_2u_recommendations``,
* ``student.enable_amplitude_recommendations``,
* ``student.enable_fallback_recommendations``,
* ``blockstore.use_blockstore_app_api`` are also not configurable anymore.

Developer Experience
********************

-  Asset Processing (webpack, collectstatic, etc.) using Paver Commands in edx-platform is now Deprecated and will not be available in Sumac

   -    - `[DEPR] Asset processing in Paver`_.
   -  Non deployment paver commands will be removed by Sumac

.. _[DEPR] Asset processing in Paver: https://github.com/openedx/edx-platform/issues/31895

Researcher & Data Experiences
*****************************

`Aspects <https://docs.openedx.org/projects/openedx-aspects/en/latest/index.html>`_ 
is an analytics system for the Open edX platform, bringing actionable data
about course and learner performance to instructors and site operators. It is primarily
a Tutor plugin that ties together data from the Open edX learning management system
and Studio using open source tools to aggregate and transform learning traces into data
visualizations.

See the `Aspects configuration documentation <https://docs.openedx.org/projects/openedx-aspects/en/latest/technical_documentation/how-tos/production_configuration.html>`_
to learn about setting up Aspects for your production environment.

Known Issues
************

Please refer to `this board <https://github.com/orgs/openedx/projects/28/views/16>`_ for known issues with Redwood.
