Open edX Sumac Developer & Operator Release Notes
#################################################

These are the developer & operator release notes for the Sumac release, the 19th
community release of the Open edX Platform, spanning changes from May 10, 2024
to October 23, 2024. You can also review details about :doc:`../index` or learn
more about the `Open edX Platform`_.

To view the end-user facing docs, see the :doc:`feature_release_notes`.

.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
****************


Learner Experiences
*******************


Instructor Experiences
**********************


Administrators & Operators
**************************

- `Course assets should be served by a view rather than a middleware <https://github.com/openedx/edx-platform/issues/34702>`_
   - Background: The LMS/CMS previously handled course asset requests (asset-v1: andc4x URLs) via a middleware called StaticContentServer. This middleware has been converted to a view.
   - Action: If your deployment has a custom MIDDLEWARE list in Django, you will need to remove this item at the time of upgrade to Sumac. Otherwise, no action is needed..
- Ubuntu 22.04 Related Operators Note
   - `PR <https://github.com/openedx/edx-platform/pull/35450>`_
   - In newer versions of ubuntu the MD4 hashing algorithm is disabled by default. To enable it the openssl config needs to be updated in a manner similar to what's being done here. Alternatively, you can set the FEATURES['ENABLE_BLAKE2B_HASHING'] setting to True which will switch to a newer hashing algorithm where MD4 was previously used.
      Because this hashing is being used as a part of the edx-platform caching mechanism, this will effectively clear the cache for the items that use this hash. The will impact any items where the cache key might have been too big to store in memcache so it's hard to predict exactly which items will be impacted.
   - Added override options to commerce related CTA URLs in edx-platform
   - Background: Extension points have been added have been added to commerce app in: `PR1 <https://github.com/openedx/edx-platform/pull/35441>`_, `PR2 <https://github.com/openedx/edx-platform/pull/35501>` so openedX community members who wants to extend the commerce functionality can do so without explicitly adding code into edx-platform codebase. For more information into extension points see Pluggable override section in `Extension Points <https://github.com/openedx/edx-platform/blob/master/docs/concepts/extension_points.rst>`_.
   - Additional Considerations: Commerce app itself is slated for deprecation nevertheless.
   - `courseware.enable_navigation_sidebar <https://github.com/openedx/edx-platform/blob/38f73442e78a8b9afb5543facd170dca830acb1a/lms/djangoapps/courseware/toggles.py#L86>`_  is now enabled by default. It was disabled by default in Redwood.

Settings and Toggles
====================
- `contentstore.new_studio_mfe.disable_legacy_libraries <https://github.com/openedx/edx-platform/blob/2c575209f1177f095860a89b0c0ac080db9442a1/cms/djangoapps/contentstore/toggles.py#L613>`_
- `contentstore.new_studio_mfe.disable_new_libraries <https://github.com/openedx/edx-platform/blob/2c575209f1177f095860a89b0c0ac080db9442a1/cms/djangoapps/contentstore/toggles.py#L641C1-L641C2>`_
- `DISABLED_COUNTRIES <https://github.com/openedx/edx-platform/blob/b07464ba2dc4e397af799e40effd2e267516ea2a/cms/envs/common.py#L2956>`_
- `GRADEBOOK_FREEZE_DAYS <https://github.com/openedx/edx-platform/blob/b07464ba2dc4e397af799e40effd2e267516ea2a/lms/envs/common.py#L1098>`_
- `XBLOCK_RUNTIME_V2_EPHEMERAL_DATA_CACHE <https://github.com/openedx/edx-platform/blob/b07464ba2dc4e397af799e40effd2e267516ea2a/cms/envs/common.py#L1034>`_
- `contentstore.new_studio_mfe.disable_legacy_libraries <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/cms/djangoapps/contentstore/toggles.py#L613>`_
- `contentstore.new_studio_mfe.disable_new_libraries <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/cms/djangoapps/contentstore/toggles.py#L641C3-L641C4`_
- `course_experience.enable_ses_for_goalreminder <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/openedx/features/course_experience/__init__.py#L37>`_
- `discounts.enable_first_purchase_discount_override <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/openedx/features/discounts/applicability.py#L32>`_
- `new_core_editors.use_advanced_problem_editor <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/cms/djangoapps/contentstore/toggles.py#L163>`_
- `notifications.enable_new_notification_view <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/openedx/core/djangoapps/notifications/config/waffle.py#L53>`_
- `notifications.enable_notification_grouping <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/openedx/core/djangoapps/notifications/config/waffle.py#L42C19-L42C61>`_
- `notifications.enable_ora_grade_notifications <https://github.com/openedx/edx-platform/blob/dafcac780ae96a2ca93a2dc94425d3a3e27bbc83/openedx/core/djangoapps/notifications/config/waffle.py#L40>`_


Other Operator Changes
======================


Deprecations & Removals
***********************

- In `frontend-app-learner-dashboard <https://github.com/openedx/frontend-app-learner-dashboard>`_ 
   - support for Optimizely has been removed along with the ProductRecommendations widget.
   - `DEPR: Optimizely Support <https://github.com/openedx/frontend-app-learner-dashboard/issues/387>`_
   - Removed the RecommendationsPanel widget
   - `DEPR: RecommendationsPanel <https://github.com/openedx/frontend-app-learner-dashboard/issues/410>`_
- In edx-platform:
   - ``commerce-coordinator`` related code has been removed
   - `PR: <https://github.com/openedx/edx-platform/pull/35527>`_
- [UPCOMING] In Teak pre-design-tokens brand packages will no longer be supported. With design tokens, theme authors will instead override core Paragon tokens by defining their own JSON tokens that get deep merged alongside the core Paragon tokens, thus overriding any tokens that were defined by the theme author. See `the associated DEPR ticket for details <https://github.com/openedx/brand-openedx/issues/23>`_.
Developer Experience
********************

Researcher & Data Experiences
*****************************


Known Issues
************
