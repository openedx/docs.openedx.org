.. _Open edX Quince Release:

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

* .. _Include and enable the Indigo theme in the default Open edX image: https://github.com/overhangio/tutor/issues/953

* .. _Hostname migration: local.overhang.io -> local.edly.io & docs.tutor.overhang.io -> docs.tutor.edly.io: https://github.com/overhangio/tutor/issues/945


Learner Experiences
*******************


Instructor Experiences
**********************


Administrators & Operators
**************************

Which MFEs will be included?

* .. _frontend-app-learner-record: https://github.com/openedx/frontend-app-learner-record
* .. _frontend-app-learner-dashboard: https://github.com/openedx/frontend-app-learner-dashboard

New Waffle Flagts:

* .. _feat: add Waffle Flag to disable resetting self-paced deadlines by learners: https://github.com/openedx/edx-platform/pull/32148
* .. _feat: adds waffle flag for show notifications tray: https://github.com/openedx/edx-platform/pull/32451
* .. _feat: add course waffle flag for learner assistant: https://github.com/openedx/edx-platform/pull/32657

Deprecations & Removals
***********************
* .. _We have deprecated and migrated the openedx/xblock-utils library into openedx/XBlock: https://github.com/openedx/XBlock/issues/675 .

* .. _Most functionality has been removed from the long-deprecated Old Mongo Modulestore. For more details, please: https://github.com/openedx/public-engineering/issues/62 

* .. _BasicAuthentication as default authentication class in edx-platform: https://github.com/openedx/edx-platform/issues/33028

* .. _Remove JWT_AUTH_REFRESH_COOKIE:  https://github.com/openedx/public-engineering/issues/190

Developer Experience
********************


Researcher & Data Experiences
*****************************


Known Issues
************
