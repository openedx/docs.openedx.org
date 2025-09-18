###########################
Notifications & Preferences
###########################

Notifications keep you informed about activity in your courses.

.. _notification-types:

Notification Types
==================

Discussion Notifications
------------------------

#. Activity notifications: New responses or comments on your posts and on posts you follow, and endorsements **of** your responses and of responses on your posts.
#. New discussion posts: When a new discussion post is created.
#. New question posts: When a new question post is created.
#. New posts from instructors: When the instructor creates a post and chooses to notify learners.

.. image:: /_images/learners/Notification_tray_forum_notifications_learner.png
   :width: 400
   :align: center
   :alt: Clicking the bell on the top right opens the notifications tray.

Updates
-------

#. Course updates: When the instructor creates a new course update.

.. image:: /_images/learners/Notifications_tray_updates_screenshot.png
   :width: 400
   :align: center
   :alt: Screenshot of a course update notification in the tray.

Grading
-------

#. ORA grade received: When your submission for an open response assessment (ORA) receives a grade.

.. image:: /_images/learners/Notifications_tray_grading_screenshot_learner.png
   :width: 400
   :align: center
   :alt: Screenshot of grading notifications in the tray.

.. _delivery-channels:

Delivery Channels
=================

Tray
----

- The notification tray is intended to keep users informed while they are on the web platform.
- A bell icon in the top-right corner displays the count of unread notifications.
- When clicked, it opens a tray that organizes notifications into tabs based on platform area (Discussions, Grading, Updates).
- Each notification includes the relevant course name, an indicator showing it is unread, and a timestamp of when it was generated.
- A gear icon in the tray’s top-right corner links to the preferences center, where users can adjust notification settings.

.. image:: /_images/learners/Notifications_tray_screenshot.png
   :width: 700
   :align: center
   :alt: Clicking the bell on the top right opens the notifications tray.

Email Notifications
-------------------

- Notification emails keep users informed even when they are away from the platform.
- Users can choose to get notified immediately or receive a daily or weekly summary of notifications.

  - **Immediately:** Receive the email notification as soon as the activity happens.
  - **Daily:** Receive a summary of notifications from the past 24 hours, every day at 22:00 UTC.
  - **Weekly:** Receive a summary of notifications from the past 7 days, every Saturday at 22:00 UTC.

- Emails include a one-click unsubscribe option to turn off email notifications for all activity types.

.. image:: /_images/learners/Notification_daily_email_screenshot_learner.png
   :width: 400
   :align: center
   :alt: Screenshot of an email with the daily summary of notifications.

.. _managing-preferences:

Managing Preferences
====================

The preferences center allows users to control which notifications they receive, how often, and through which channel. Users can get to the preferences page via:

- The **Notifications** tab on the **Account Settings** page.
- The gear icon in the top-right corner of the notification tray.
- The **Notification Settings** link in email.

For each preference:

- Users can toggle tray and email preferences ON or OFF.
- Users can set the cadence for email notifications: Immediately, Daily, or Weekly.

.. image:: /_images/learners/Preference_center_learner.png
   :width: 700
   :align: center
   :alt: Screenshot of the preferences center on Account Settings.

Default Settings
----------------

- High-value notifications have tray and email ON by default.

  - “New posts from instructors” and “Course updates” are exceptions where email is OFF by default to prevent high email volume/cost for courses with large enrollments.

- High-volume notifications (e.g., new discussion posts) are OFF by default to prevent clutter.
- The default email cadence is set to **Daily** for all preferences where email is ON by default.

The table below shows defaults for each notification type.

.. list-table::
   :widths: 25 25 25 25
   :align: center
   :header-rows: 1

   * - Preference
     - Default Tray Preference
     - Default Email Preference
     - Visibility
   * - Activity notifications
     - ON
     - ON / Daily
     - All
   * - New discussion posts
     - OFF
     - OFF
     - All
   * - New question posts
     - OFF
     - OFF
     - All
   * - Reported content
     - ON
     - ON / Daily
     - Forum moderators
   * - Course updates
     - ON
     - OFF
     - All
   * - ORA grade received
     - ON
     - ON / Daily
     - All
   * - ORA new submissions
     - ON
     - OFF
     - Course staff, course admins

.. _notifications-grouping:

Notifications Grouping
======================

High-volume notifications, such as new discussion posts or new ORA submissions, can clutter the notification tray and reduce the visibility of other important notifications. To mitigate this, the notification grouping feature combines similar notifications into a single, unified notification based on context. Currently, grouping is supported for two notification types:

- **New discussion posts:** grouped by course.
- **New ORA submissions:** grouped by ORA assignment ID.

.. image:: /_images/learners/Notifications_grouping_ORA_screenshot.png
   :width: 400
   :align: center
   :alt: Screenshot of grouped and ungrouped ORA submission notifications.

.. _notifications-expiry:

Notifications Expiry
====================

Every day, notifications older than 60 days are deleted from the database to keep storage under control. Developers can change this duration from the Django settings.