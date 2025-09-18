.. _Notifications & Preferences:

###########################
Notifications & Preferences
###########################

Notifications keep you informed about activity in your courses.

.. _Notification Types:

Notification Types
##################

Discussions Notifications
*************************

#.  Activity notifications: New responses or comments on your posts and the ones you are following, and endorsements to your responses and the ones on your post.
#.  New discussion posts: When a new discussion post is created.
#.  New question posts: When a new question post is created.
#.  Reported content: When content is reported.

    #. This notification is only sent to users having a forum moderator role (discussion admin, discussion moderator, community TA and group community TA).

#.  New posts from instructors: When the instructor creates a post and chooses to notify the learners.


.. image:: /_images/educator_concepts/Notifications_tray_forum_screenshot.png
  :width: 400
  :align: center
  :alt: Clicking the bell on the top right opens the notifications tray.

Updates
********

#. Course updates: When the instructor creates a new course update.

.. image:: /_images/educator_concepts/Notifications_tray_updates_screenshot.png
  :width: 400
  :align: center
  :alt: Screenshot of a course update notification in tray.

Grading
********

#.  ORA grade received: When your submission for an open response assessment (ORA) receives a grade.
#.  ORA new submissions: When a learner submits an ORA that requires staff grading.

    #. This notification is only sent to users having a course staff or course admin role.

.. image:: /_images/educator_concepts/Notifications_tray_grading_screenshot.png
  :width: 400
  :align: center
  :alt: Screenshot of all grading notifications in tray.


.. _Delivery Channels:

Delivery Channels
#################

Tray
****

- The intent of notification tray is to keep users informed while they're on the web platform.
- A bell icon in the top-right corner displays the count of unread notifications.
- When clicked, it opens a tray that organizes notifications into tabs based on platform area (Discussions, Grading, Updates).
- Each notification includes the relevant course's name, a red dot to indicate it's unread (not clicked), and a timestamp showing when it was generated.
- A gear icon in the tray's top-right corner links to the preferences center, where users can adjust their notification settings.

.. image:: /_images/educator_concepts/Notifications_tray_screenshot.png
  :width: 700
  :align: center
  :alt: Clicking the bell on the top right opens the notifications tray.

Email Notifications
*******************

- The intent of notification email is to keep users informed even when they're away from the platform.
- Users can choose to get notified immediately or to receive a daily or weekly summary of notifications.

  - Immediately: Receive the email notification as soon as the activity happens.
  - Daily: Receive a summary of notifications for the past 24 hours, everyday at 2200hrs UTC.
  - Weekly: Receive a summary of notifications for the past 7 days, everyday Saturday at 2200hrs UTC.

- Emails have a one-click unsubscribe option which allows turning off email notifications for all activity types.

.. image:: /_images/educator_concepts/Notification_daily_email_screenshot.png
  :width: 400
  :align: center
  :alt: Screenshot of email having daily summary of notifications.

.. _Managing Preferences:

Managing Preferences
####################

Preferences center allows users to control which notifications they receive, how often, and through which channel. Users can get to the preferences page via:

- “Notifications” tab on the “Account Settings” page.
- Gear icon in top right corner in the notification tray.
- “Notification Settings” link in email.

For each preference:

- Users can toggle tray and email preference ON or OFF.
- Users can set cadence for email notifications: Immediately, Daily and Weekly.

.. image:: /_images/educator_concepts/Preference_center.png
  :width: 700
  :align: center
  :alt: Screenshot of preference center on Account Settings.


Default Settings
*****************

- High-value notifications have tray and email ON by default.

  - “New posts from instructors” and “Course updates” are exceptions where email is OFF by default to prevent high volume/cost of email due to courses with large enrollments.

- High-volume notifications (e.g., new discussion posts) are OFF by default to prevent clutter.
- Email cadence default is set to “Daily” for all preferences where email default ON.

The table below shows defaults for each notification type.

.. list-table::
   :widths: 25 25 25 25
   :align: center
   :header-rows: 1

   * - Preference
     - Default Tray Preference
     - Default Email Preference
     - Visibility
   * - Activity Notifications
     - ON
     - ON / Daily
     - All
   * - New Discussion Posts
     - OFF
     - OFF
     - All
   * - New Question Posts
     - OFF
     - OFF
     - All
   * - Reported Content
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
     - Course staff, Course admin

.. _Notifications Grouping:

Notifications Grouping
######################

High-volume notifications, such as new discussion posts or new ORA submissions, can clutter the notification tray. This clutter reduces the visibility of other important notifications, making it challenging for users to stay informed effectively. As a result, crucial but potentially high-volume notifications need to be turned off by default to avoid overwhelming users. The notification grouping feature mitigates this issue by combining similar notifications into a single, unified notification, based on their context. Currently, grouping is supported for two notification types:

- New discussion posts: Notifications are grouped by the specific course.
- New ORA submissions: Notifications are grouped by the ORA assignment ID.

.. image:: /_images/educator_concepts/Notificaitons_grouping_ORA_screenshot.png
  :width: 400
  :align: center
  :alt: Screenshot of grouped and ungrouped ORA submission received notification.

.. _Notifications Expiry:

Notifications Expiry
######################

Everyday, notifications older than 60 days are deleted from the database to keep the storage in control. Developers can change this duration from the django settings page.
