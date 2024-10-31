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

Settings and Toggles
====================


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

Developer Experience
********************

Researcher & Data Experiences
*****************************


Known Issues
************
