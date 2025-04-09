Open edX Sumac Developer & Operator Release Notes
#################################################

These are the developer & operator release notes for the Sumac release, the 19th
community release of the Open edX Platform, spanning changes from May 9, 2024
to October 24th, 2024. You can also review details about :doc:`../index` or learn
more about the `Open edX Platform`_.

To view the end-user facing docs, see the :doc:`feature_release_notes`.

.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
****************

No breaking changes in Sumac.


User Facing Experiences
*************************

See the :doc:`feature_release_notes` for more detail on user-facing changes in this release.


Administrators & Operators
**************************

- Most search functionality included in the core platform now supports Meilisearch as an alternative to Elasticsearch. For instances deployed using Tutor, only Meilisearch is supported, and Tutor will automatically provision Meilisearch and create the indexes during the upgrade.
   - Two recent features, Studio Course Search and the new Content Libraries (beta), require Meilisearch and will be hidden from the UI if Meilisearch is not available. (For the Content Libraries beta, this affects only the UI - developers can still use the APIs without Meilisearch.)
   - The new Content Libraries (beta) can be hidden entirely in Sumac by setting the waffle flag ``contentstore.new_studio_mfe.disable_new_libraries`` to "Yes". This option will be removed in Teak.
   - After upgrading, if you wish to use the new Content Libraries (beta) or Studio Course Search features, you will need to run ``manage.py cms reindex_studio --experimental --incremental`` to populate the new Studio Search index with your existing content (courseware/libraries). Studio search results will be incomplete until this command has finished.
   - A new media storage setting is required for new Content Libraries. This should be specified as OPENEDX_LEARNING['MEDIA']. Tutor will `provide this setting automatically <https://github.com/overhangio/tutor/blob/33d2bc2c71e3cd30545417afb18ba2bd989a19fd/tutor/templates/apps/openedx/settings/partials/common_all.py#L251-L258>`_, and can be used as an example for those who are running different infrastructure. For those not running Tutor, **please ensure that the file storage location is not publicly accessible**.
- `Course assets are now served by a view rather than a middleware <https://github.com/openedx/edx-platform/issues/34702>`_
   - Background: The LMS/CMS previously handled course asset requests (asset-v1: andc4x URLs) via a middleware called StaticContentServer. This middleware has been converted to a view.
   - Action: If your deployment has a custom MIDDLEWARE list in Django, you will need to remove this item at the time of upgrade to Sumac. Otherwise, no action is needed.
- Ubuntu 22.04 Related Operators Note
   - `PR <https://github.com/openedx/edx-platform/pull/35450>`_
   - In newer versions of ubuntu the MD4 hashing algorithm is disabled by default. To enable it the openssl config needs to be updated in a manner similar to what's being done here. Alternatively, you can set the FEATURES['ENABLE_BLAKE2B_HASHING'] setting to True which will switch to a newer hashing algorithm where MD4 was previously used.
      Because this hashing is being used as a part of the edx-platform caching mechanism, this will effectively clear the cache for the items that use this hash. The will impact any items where the cache key might have been too big to store in memcache so it's hard to predict exactly which items will be impacted.
- Added override options to commerce related CTA URLs in edx-platform
   - Background: Extension points have been added have been added to commerce app in: `PR1 <https://github.com/openedx/edx-platform/pull/35441>`_, `PR2 <https://github.com/openedx/edx-platform/pull/35501>`_ so Open edX community members who wants to extend the commerce functionality can do so without explicitly adding code into edx-platform codebase. For more information into extension points see Pluggable override section in `Extension Points <https://github.com/openedx/edx-platform/blob/master/docs/concepts/extension_points.rst>`_.
   - Additional Considerations: Commerce app itself is slated for deprecation. `See the associated DEPR ticket <https://github.com/openedx/public-engineering/issues/22>`_. 
- `courseware.enable_navigation_sidebar <https://github.com/openedx/edx-platform/blob/38f73442e78a8b9afb5543facd170dca830acb1a/lms/djangoapps/courseware/toggles.py#L86>`_  is now enabled by default. It was disabled by default in Redwood.

- New Forums Implementation (migration from Ruby to Python forums backend)

   - For users running Tutor, they will automatically switch to the new app. Instructions to migrate data from mongodb to mysql is available in the plugin README https://github.com/overhangio/tutor-forum/ (not yet merged, see `feat: upgrade to sumac <https://github.com/overhangio/tutor-forum/pull/49/files>`_).

   - Users not running Tutor will by default remain on the legacy `cs_comments_service` app. They need to read this part of the forum app README: https://github.com/openedx/forum?tab=readme-ov-file#forum-v2-toggle Some settings need to be defined even for legacy app users.


New And Updated Settings and Toggles
====================================
- `contentstore.new_studio_mfe.disable_legacy_libraries <https://github.com/openedx/edx-platform/blob/2c575209f1177f095860a89b0c0ac080db9442a1/cms/djangoapps/contentstore/toggles.py#L613>`_
- `contentstore.new_studio_mfe.disable_new_libraries <https://github.com/openedx/edx-platform/blob/2c575209f1177f095860a89b0c0ac080db9442a1/cms/djangoapps/contentstore/toggles.py#L641C1-L641C2>`_
- `DISABLED_COUNTRIES <https://github.com/openedx/edx-platform/blob/b07464ba2dc4e397af799e40effd2e267516ea2a/cms/envs/common.py#L2956>`_
- `GRADEBOOK_FREEZE_DAYS <https://github.com/openedx/edx-platform/blob/b07464ba2dc4e397af799e40effd2e267516ea2a/lms/envs/common.py#L1098>`_
- `XBLOCK_RUNTIME_V2_EPHEMERAL_DATA_CACHE <https://github.com/openedx/edx-platform/blob/b07464ba2dc4e397af799e40effd2e267516ea2a/cms/envs/common.py#L1034>`_
- `course_experience.enable_ses_for_goalreminder <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/openedx/features/course_experience/__init__.py#L37>`_
- `discounts.enable_first_purchase_discount_override <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/openedx/features/discounts/applicability.py#L32>`_
- `new_core_editors.use_advanced_problem_editor <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/cms/djangoapps/contentstore/toggles.py#L163>`_
- `notifications.enable_new_notification_view <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/openedx/core/djangoapps/notifications/config/waffle.py#L53>`_
- `notifications.enable_notification_grouping <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/openedx/core/djangoapps/notifications/config/waffle.py#L42C19-L42C61>`_
- `notifications.enable_ora_grade_notifications <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/openedx/core/djangoapps/notifications/config/waffle.py#L40>`_
- `ENABLE_ORA_PEER_CONFIGURABLE_GRADING <https://github.com/openedx/edx-ora2/blob/5ce41562e7b874856c541a20eb8288880628b3f0/openassessment/xblock/config_mixin.py#L186-L198>`_
- `RBAC_IGNORE_INVALID_JWT_COOKIE <https://github.com/openedx/edx-rbac/blob/b354112ff24181ceb7ca660db493b5a03d62f808/edx_rbac/constants.py#L7-L16>`_
- `enterprise.enterprise_customer_support_tool <https://github.com/openedx/edx-enterprise/blob/7ca07317c5dc05ab70b83451144192a0e1c4162f/enterprise/toggles.py#L46-L56>`_
- `enterprise.enterprise_groups_v2 <https://github.com/openedx/edx-enterprise/blob/7ca07317c5dc05ab70b83451144192a0e1c4162f/enterprise/toggles.py#L58-L68>`_

Removed Settings and Toggles
============================

- COURSEGRAPH_DUMP_COURSE_ON_PUBLISH
- FEATURESENABLE_LIBRARY_AUTHORING_MICROFRONTEND
- FEATURESENABLE_V2_CERT_DISPLAY_SETTINGS
- commerce.transition_to_coordinator.checkout
- commerce.transition_to_coordinator.refund
- contentstore.library_authoring_mfe
- discussions.enable_reported_content_notifications
- learner_dashboard.enable_b2c_subscriptions
- notifications.enable_coursewide_notifications
- notifications.enable_notifications_filters
- notifications.enable_ora_staff_notifications
- notifications.show_notifications_tray
- studio.enable_course_update_notifications
- BLOCKSTORE_BUNDLE_CACHE_TIMEOUT
- BUNDLE_ASSET_STORAGE_SETTINGS
- BUNDLE_ASSET_URL_STORAGE_KEY
- BUNDLE_ASSET_URL_STORAGE_SECRET
- BLOCKSTORE_BUNDLE_CACHE_TIMEOUT
- COURSEGRAPH_CONNECTION
- COURSEGRAPH_JOB_QUEUE


Other Operator Changes
======================


Deprecations & Removals
***********************

- The existing "Content Libraries" feature has been renamed to "Legacy Libraries" and will be deprecated in the next release (Teak), and removed entirely in Ulmo in favor of the new "Content Libraries" feature. The Teak release will include a tool for migrating content from Legacy Libraries into new Content Libraries.
- In `frontend-app-learner-dashboard <https://github.com/openedx/frontend-app-learner-dashboard>`_ 
   - support for Optimizely has been removed along with the ProductRecommendations widget.
   - `DEPR: Optimizely Support <https://github.com/openedx/frontend-app-learner-dashboard/issues/387>`_
   - Removed the RecommendationsPanel widget
   - `DEPR: RecommendationsPanel <https://github.com/openedx/frontend-app-learner-dashboard/issues/410>`_
- In edx-platform:
   - ``commerce-coordinator`` related code has been removed. `PR: <https://github.com/openedx/edx-platform/pull/35527>`_
- [UPCOMING] In Ulmo pre-design-tokens brand packages will no longer be supported. With design tokens, theme authors will instead override core Paragon tokens by defining their own JSON tokens that get deep merged alongside the core Paragon tokens, thus overriding any tokens that were defined by the theme author. See `the associated DEPR ticket for details <https://github.com/openedx/brand-openedx/issues/23>`_.
- [UPCOMING] Between now and the release of Teak, all Dockerfiles will be removed from the Open edX organization. As an alternative, Tutor provides `production-ready Docker images <https://hub.docker.com/u/overhangio/>`_ for all supported Open edX services. And each Open edX service repository should contain documentation describing how it can be installed and executed, allowing anyone to write a Dockerfile that provisions the repository. See `this associated DEPR ticket for details <https://github.com/openedx/public-engineering/issues/263>`_. 
- The cs_comments_service application is being replaced by forum. `[DEPR]: Replace cs_comments_service #437 <https://github.com/openedx/cs_comments_service/issues/437>`_
- The Zooming Image Tool will be deprecated in Sumac. `[DEPR] Zooming Image Tool (HTML block template) #31436 <https://github.com/openedx/edx-platform/issues/31436>`_
- The EdxRestApiClient has been deprecated and removed in this release. See `[DEPR]: Complete removal of `EdxRestApiClient <https://github.com/openedx/public-engineering/issues/189>`_ for details. 
- The Demographics app has been removed. It was added to support a private edX Demographics IDA for collecting additional user info. See `[DEPR]: Demographics Django app #35127 <https://github.com/openedx/edx-platform/issues/35127>`_.
- The programs_listing endpoint in the credentials application has been removed. `[DEPR]: /program-listing endpoint <https://github.com/openedx/credentials/issues/2642>`_.
- The skill_level endpoint has been removed `[DEPR]: endpoint /user/v1/skill_level/{job_id}/ <https://github.com/openedx/edx-platform/issues/35302>`_.
- [UPCOMING] The Toggle 'block_structure.storage_backing_for_cache' will be removed, with a default setting of True. You may want to test enabling in Sumac before it becomes the default behavior in Teak. See `[DEPR]: block_structure.storage_backing_for_cache in edx-platform <https://github.com/openedx/public-engineering/issues/32>`_.
- As part of the `Oscare Ecommerce Stack deprecation <https://github.com/openedx/public-engineering/issues/22>`_ , the following repositories have been archived:
   - https://github.com/openedx/ecommerce
   - https://github.com/openedx/ecommerce-worker
   - https://github.com/openedx/frontend-app-payment
   - https://github.com/openedx/frontend-app-ecommerce
   - https://github.com/openedx/ecommerce-scripts


Developer Experience
********************

- With the launch of the new Content Libraries feature, many new or updated APIs are now ready for developers to start using (though some are in beta and may change). This includes the entire `Learning Core API <https://github.com/openedx/openedx-learning/blob/main/openedx_learning/api/authoring.py>`_ (Components, Contents, Publishing, Collections), `Content Tagging API <https://github.com/openedx/edx-platform/blob/master/openedx/core/djangoapps/content_tagging/api.py>`_, `Content Libraries API <https://github.com/openedx/edx-platform/blob/master/openedx/core/djangoapps/content_libraries/api.py>`_, and `Learning Core XBlock API <https://github.com/openedx/edx-platform/blob/master/openedx/core/djangoapps/xblock/api.py>`_. Most of these APIs (other than tagging) are only useful in content libraries at the moment, but when courseware is eventually moved to Learning Core as well, the Learning Core APIs will be recommended way to work with all learning content in the platform, and the modulestore APIs will be deprecated.

.. _Sumac Aspects Notes:

Researcher & Data Experiences
*****************************

Upgrading Aspects to v1.3.1 will get you the latest Aspects functionality with Sumac. See the upgrade instructions here: :doc:`openedx-aspects:technical_documentation/how-tos/upgrade`.

Known Issues
************
