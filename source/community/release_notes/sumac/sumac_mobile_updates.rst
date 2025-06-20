.. _Mobile Updates Sumac:

Mobile Updates (Sumac)
#######################

New Features (iOS and Android)
********************************

* Plugin Architecture v1. Connect any analytics service without changes to the codebase.
* New Dashboard level navigation. Primary course experience.
* New Course Home experience.
* FCM integration for push notifications.
* Calendar integration.
* Atlas (Translations) integration.
* SAML-based single sign-on.
* Offline mode - Note! This is experimental

New Features (iOS only)
********************************

* Password Field: Added an eye icon to toggle password visibility.
* Media & Playback: Implemented saving of video playback speed and improved YouTube handling (e.g., full-screen support on iPad).
* Social Auth: Introduced banners for linked social accounts and enhanced sign-in/register flows.

New Features (Android only)
********************************

* Browser-Based Authentication: Added support for login and registration via a
  browser custom tab, enabling third-party authentication flows.

Fixes
******

* (iOS) Logout & Cookies: Ensured cookies are cleared on logout.
* (iOS) UI Issues: Fixed layout padding, tab bar colors, grid spacing, and Elm theme inconsistencies.
* (iOS) Swift 6 Migration: Addressed several issues related to the Swift 6 migration (e.g., JavaScript evaluation and download cancelation bugs).
* (iOS) Gestures & Logins: Resolved iOS 18 tap gesture issues and fixed the Microsoft login problem.
* (Android) Course & Unit Handling:

  * Fixed the issue with dataValue for CourseOutline.
  * Addressed problems handling units with no descendants and prevented a crash when retrieving the first topic.

* (Android) Transcription & Analytics:

  * Caught exceptions during transcription file parsing.
  * Improved analytics event tracking and added missing events.

* (Android) Bulk Download & Offline Mode:

  * Fixed a crash during bulk downloads by validating progress values.
  * Resolved issues with opening courses in offline mode.

Installation
*************

The mobile apps for Sumac can be installed using the ``open-release/sumac.3`` tags in each mobile app repository:

* `openedx-app-ios Sumac release <https://github.com/openedx/openedx-app-ios/tree/open-release/sumac.3>`_
* `openedx-app-android Sumac release <https://github.com/openedx/openedx-app-android/tree/open-release/sumac.3>`_

Full Release Notes
********************

See `iOS v2.1 release notes
<https://github.com/openedx/openedx-app-ios/releases>`_ and `Android v2.1
release notes <https://github.com/openedx/openedx-app-android/releases>`_.