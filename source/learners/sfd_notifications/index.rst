.. _Notifications & Preferences:

###########################
Notifications & Preferences
###########################

Notifications help you stay informed about activity in your courses. You can view notifications while on the
platform or receive them by email, depending on your preferences.

.. _delivery-channels:

Where Notifications Appear
===========================

Notification Tray
------------------


.. image:: /_images/learners/Notifications_tray_screenshot.png
   :width: 700
   :align: center
   :alt: Screenshot of notifications tray showing it's features.

   Clicking the bell icon on top right opens the notifications tray. Next to bell icon is the count of
   notifications yet to be seen by the user.


The notification tray keeps you updated while you’re browsing the site.

- Clicking the bell icon on top right opens the notifications tray with tabs such as Discussions,
  Updates and Grading.
- Each notification shows the course it belongs to, time elapsed since it was created
  and an red dot that indicates that it has not been clicked.
- A gear icon in the tray takes you directly to your notification preferences on Account Settings page.

If you have more notifications than can fit in the tray, a “Load more” button appears at the bottom.
Clicking it loads mores notifications.

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


.. _notification-types:

Notification Types
==================

Discussion Notifications
------------------------

1. **Activity notifications**: Notifies you of all activity related to posts or responses
   you’ve authored or are following.
2. **New posts from instructors**: Notifies you when an instructor creates a post.
3. **New discussion posts**: Notifies you when someone creates a new discussion type post.
4. **New question posts**: Notifies you when someone creates a new question type post.

.. image:: /_images/learners/Notification_tray_forum_notifications_learner.png
   :width: 400
   :align: center
   :alt: Clicking the bell on the top right opens the notifications tray.

Updates
-------

**Course updates**: When the instructor creates a new course update.

.. image:: /_images/learners/Notifications_tray_updates_screenshot.png
   :width: 400
   :align: center
   :alt: Screenshot of a course update notification in the tray.

Grading
-------

**ORA grade received**: When your submission for an open response assessment (ORA) receives a grade.

.. image:: /_images/learners/Notifications_tray_grading_screenshot_learner.png
   :width: 400
   :align: center
   :alt: Screenshot of grading notifications in the tray.


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
   * - New question qosts
     - OFF
     - OFF
     - All
   * - New posts from instructors
     - ON
     - ON
     - All
   * - Course updates
     - ON
     - OFF
     - All
   * - Essay assignment grade received
     - ON
     - ON / Daily
     - All

.. _notifications-expiry:

Notifications Expiry
====================

Every day, notifications older than 60 days are deleted from the database.