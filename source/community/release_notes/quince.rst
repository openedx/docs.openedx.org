Open edX Quince Release
#######################

These are the release notes for the Quince release, the 17th community release of the Open edX Platform, spanning changes from April 11 2023 to October 10 2023.  You can also review details about `earlier releases`_ or learn more about the `Open edX Platform`_.

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
****************

* `Include and enable the Indigo theme in the default Open edX image: <https://github.com/overhangio/tutor/issues/953>`__

* `Hostname migration: local.overhang.io -> local.edly.io & docs.tutor.overhang.io -> docs.tutor.edly.io: <https://github.com/overhangio/tutor/issues/945>`__


Learner Experiences
*******************

* `feat: fetch program subscription details <https://github.com/openedx/edx-platform/pull/32023>`__


Instructor Experiences
**********************


Administrators & Operators
**************************

* `feat: feature flag to disable Advanced Settings <https://github.com/openedx/edx-platform/pull/32015>`__

Which MFEs will be included?

* `frontend-app-learner-record: <https://github.com/openedx/frontend-app-learner-record>`__
* `frontend-app-learner-dashboard: <https://github.com/openedx/frontend-app-learner-dashboard>`__

New Waffle Flagts:

* `feat: add Waffle Flag to disable resetting self-paced deadlines by learners: <https://github.com/openedx/edx-platform/pull/32148>`__
* `feat: adds waffle flag for show notifications tray: <https://github.com/openedx/edx-platform/pull/32451>`__
* `feat: add course waffle flag for learner assistant: <https://github.com/openedx/edx-platform/pull/32657>`__

Deprecations & Removals
***********************

* `We have deprecated and migrated the openedx/xblock-utils library into openedx/XBlock: <https://github.com/openedx/XBlock/issues/675>`__

* `Most functionality has been removed from the long-deprecated Old Mongo Modulestore. For more details, please: <https://github.com/openedx/public-engineering/issues/62>`__

* `BasicAuthentication as default authentication class in edx-platform: <https://github.com/openedx/edx-platform/issues/33028>`__

* `Remove JWT_AUTH_REFRESH_COOKIE:  <https://github.com/openedx/public-engineering/issues/190>`__

* `feat: allow for forcing asymmetric jwts <https://github.com/openedx/edx-platform/pull/32045>`__

Developer Experience
********************

* `feat: Cross Product Recommendations Logic <https://github.com/openedx/edx-platform/pull/32003>`__

Researcher & Data Experiences
*****************************


Known Issues
************
