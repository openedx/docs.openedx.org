.. _Enable Notifications:

Enable Notifications
####################

.. tags:: site operator, how-to

:ref:`Notifications <Notifications & Preferences>` keep you informed about activity in your
courses, alerting you via one or both of in-platform notifications and email notifications.
They span activities such as Discussions updates, Course updates, Grading updates, and ORA review reminders.

The **notification tray** allows learners to access platform notifications from
the top-right corner of the Open edX interface. **Notification emails** keep them updated when
they are away from the platform. We do not have support for push notifications for Open edX mobile app at the moment.

The recommended way to enable notifications is by using the official Tutor
plugin:
`tutor-contrib-platform-notifications <https://github.com/openedx/tutor-contrib-notifications>`_.

Install and enable the plugin
*****************************

Install the plugin:

.. code-block:: bash

   pip install tutor-contrib-platform-notifications

Enable the plugin in your Tutor environment:

.. code-block:: bash

   tutor plugins enable notifications

When enabled, the plugin automatically:

- Enables the following waffle flags:

  - ``notifications.enable_notifications``
  - ``notifications.enable_email_notifications``

- Sets the required environment variables for the notifications service

  - ``SHOW_EMAIL_CHANNEL`` (defaults to TRUE)
  - ``SHOW_PUSH_CHANNEL`` (defaults to FALSE)

.. important::

   After enabling the notifications plugin, site operators **must rebuild the
   MFE image** for the notification tray to appear in the user interface.

Rebuild the MFE image:

.. code-block:: bash

   tutor images build mfe


Configure the notifications plugin
**********************************

The notifications plugin exposes several configuration options that can be
customized through the `Tutor configuration <https://docs.tutor.edly.io/configuration.html#configuration>`_.
These options are as follows:


NOTIFICATIONS_DEFAULT_FROM_EMAIL
================================

Specifies the **From** email address used when sending notification emails.

If not explicitly set, this value defaults to the platform contact email.


NOTIFICATIONS_ENABLE_SHOW_EMAIL_CHANNEL
=======================================

Controls whether the **Email notifications** toggle is visible on the learner’s
account settings page.

- Type: Boolean
- Default: ``True``

When enabled, learners get toggle to opt in or out of receiving email notifications.

.. important::
   The Open edX platform does not currently support push notifications for mobile apps.
   This toggle is added as part of ground work for when that support will be built.

NOTIFICATIONS_ENABLE_SHOW_PUSH_CHANNEL
======================================

Controls whether the **Push notifications** toggle is visible on the learner’s
account settings page.

- Type: Boolean
- Default: ``False``

When enabled, learners get toggle to opt in or out of push notifications.

Notification Digest Email
#########################

Overview
********
This change replaces the `cron-job-driven` digest email system with a self-scheduling Celery task approach. Instead of a periodic job that sweeps all users at a fixed interval, digest emails are now scheduled automatically — per user, at the exact configured delivery time — the moment a qualifying notification is created.

How it works
************

.. code-block:: text 
      
   send_notifications(user_ids, ...)                                    ← called when a notification is created
         │
         ├── [immediate cadence users] ─────► send_immediate_cadence_email(...)
         │
         └── [daily/weekly cadence users]
                  │
                  ▼
         schedule_bulk_digest_emails({user_id: cadence_type, ...})
                  │
                  ├── get_next_digest_delivery_time(cadence_type)       ← compute ETA
                  ├── SELECT existing DigestSchedule records            ← 1 query, skip already-scheduled
                  ├── bulk_create new DigestSchedule records            ← 1 query
                  ├── Notification.objects.update(email_scheduled=True) ← 1 query
                  │
                  └── on transaction.commit():
                           send_user_digest_email_task.apply_async(
                              kwargs={user_id, cadence_type},
                              eta=delivery_time,
                              task_id=<dedupe_key>,                     ← Celery-level dedup
                           )

   ────────────── At configured delivery time ──────────────

   send_user_digest_email_task(user_id, cadence_type)
         │
         ├── _claim_digest_schedule(...)                                ← atomic DB delete (prevents double-send)
         │       └── returns False if row already gone                  → skip
         │
         ├── check: was digest already sent in this window?             ← cron co-existence guard
         │
         ├── send_digest_email_to_user(user, start_date, end_date, ...)
         │       └── Notification.filter(email_sent_on__isnull=True)    ← skip already-sent rows
         │
         └── Notification.update(email_scheduled=False)                 ← clean up flags

Key characteristics
*******************

+----------------------+--------------------------------------------------------------------------------+
|Aspect                |Detail                                                                          |
+======================+================================================================================+
|Trigger               |Automatically when ``send_notifications()`` creates a qualifying notification   |
+----------------------+--------------------------------------------------------------------------------+
|Entry point           |``schedule_bulk_digest_emails()`` inside ``tasks.send_notifications``           |
+----------------------+--------------------------------------------------------------------------------+
|Task                  |``send_user_digest_email_task`` — one task per user, ETA-scheduled              |
+----------------------+--------------------------------------------------------------------------------+
|Delivery time control |Settings: ``NOTIFICATION_DAILY_DIGEST_DELIVERY_HOUR/MINUTE``,                   |
|                      |``NOTIFICATION_WEEKLY_DIGEST_DELIVERY_DAY/HOUR/MINUTE``                         |
+----------------------+--------------------------------------------------------------------------------+
|Deduplication         |Three layers: ``DigestSchedule`` DB record,                                     |
|                      |Celery task ID, ``_claim_digest_schedule`` atomic delete                        |
+----------------------+--------------------------------------------------------------------------------+
|Failure handling      |Auto-retry up to 3×, exponential backoff (5 min → 10 min → 20 min)              | 
+----------------------+--------------------------------------------------------------------------------+
|Scalability           |~3 DB queries per cadence group regardless of user count; tasks run in parallel |
+----------------------+--------------------------------------------------------------------------------+
|Timezone handling     |``django.utils.timezone.now()`` (timezone-aware) throughout                     |
+----------------------+--------------------------------------------------------------------------------+

New Settings
************

As of Verawood, new settings have been added in
`openedx/envs/common.py <https://github.com/openedx/openedx-platform/blob/09878a18f071318aa446fd78b37a95ba81a62581/openedx/envs/common.py#L2694>`_
that govern how digests are delivered. 

.. code-block:: python
      
   NOTIFICATION_DAILY_DIGEST_DELIVERY_HOUR   = 17   # 5 PM UTC
   NOTIFICATION_DAILY_DIGEST_DELIVERY_MINUTE = 0

   NOTIFICATION_WEEKLY_DIGEST_DELIVERY_DAY   = 0    # Monday (0=Mon … 6=Sun)
   NOTIFICATION_WEEKLY_DIGEST_DELIVERY_HOUR  = 17   # 5 PM UTC
   NOTIFICATION_WEEKLY_DIGEST_DELIVERY_MINUTE = 0

Override these in your deployment settings to change when digests are delivered.

.. warning::
   ``send_email_digest`` management command, introduced in Ulmo, is DEPRECATED. You should remove any cron jobs that call it.

   The management command still exists but is now a no-op with a deprecation warning:
   ``WARNING: This command is deprecated. Digest emails are now scheduled automatically. Please remove cron jobs using this command.``

If you are on an Ulmo system, please view this doc in the ``ulmo`` version for instructions on cron job configuration.


Creating a new notification
###########################

This documentation provides instructions to developers on how to add new notifications to the existing notification system.

Overview of terms
*****************

Type
   every notification a user sees has a defined type. This type describes the notification's behaviour and template text.

App
   each notification type is associated with a notification app. A notification app is simply a way to group notifications, and to provide a mechanism for shared behaviour.
Core notification
   a notification type can be labelled as a core notification. In this case, the behaviour is managed at the app level, not at the level of the individual notification type.

Defining a notification
***********************

The configuration consists of notification types and notification apps. Follow the steps below to define a new notification type.

Define the Notification App
===========================

The first step to defining a new notification is deciding on an app to associate it with. Either choose an existing one or create a new one in `COURSE_NOTIFICATION_APPS <https://github.com/openedx/openedx-platform/blob/1ffedf456c60e72aa2cdeccb2cb9fb7c90f0dda3/openedx/core/djangoapps/notifications/base_notification.py#L331>`_. For example, here is an app named "discussion":

.. code-block:: python

   COURSE_NOTIFICATION_APPS = {
      'discussion': {
         'enabled': True,
         'core_info': '',
         'core_web': True,
         'core_email': True,
         'core_push': True,
         'non_editable': [],
         'core_email_cadence': 'weekly'
      }
   }

The app name (the key) can be any name you wish to add but ideally it should represent existing Django apps in the project.
For an explanation of the available fields, see `NotificationApp <https://github.com/openedx/openedx-platform/blob/1ffedf456c60e72aa2cdeccb2cb9fb7c90f0dda3/openedx/core/djangoapps/notifications/base_notification.py#L299>`_.

Define the Notification Type
============================

Now you can define the notification type itself.
To do this, add a new entry to `COURSE_NOTIFICATION_TYPES <https://github.com/openedx/openedx-platform/blob/1ffedf456c60e72aa2cdeccb2cb9fb7c90f0dda3/openedx/core/djangoapps/notifications/base_notification.py#L63>`_.
For example, here is a notification defined for a new response to a discussion forum post, associated with the "discussion" app example from the previous step:

.. code-block:: python

   COURSE_NOTIFICATION_TYPES = {
      'new_response': {
         'notification_app': 'discussion',
         'name': 'new_response',
         'is_core': False,
         'web': True,
         'email': True,
         'push': True,
         'info': 'Response on post',
         'non_editable': [],
         'content_template': _('<{p}><{strong}>{replier_name}</{strong}> responded to your post <{strong}>{post_title}</{strong}></{p}>'),
         'content_context': {
               'post_title': 'Post title',
               'replier_name': 'replier name',
         },
         'email_template': '',
      },
   }

For an explanation of the available fields, see `NotificationType <https://github.com/openedx/openedx-platform/blob/1ffedf456c60e72aa2cdeccb2cb9fb7c90f0dda3/openedx/core/djangoapps/notifications/base_notification.py#L19>`_.

Sending a notification
======================

To send a notification, you need to send the ``USER_NOTIFICATION_REQUESTED`` signal with an instance of ``UserNotificationData`` containing information about the notification to send.

Below is an example function to build and send the ``new_response`` notification type from earlier.

.. code-block:: python

   from openedx_events.learning.signals import USER_NOTIFICATION_REQUESTED
   from openedx_events.learning.data import UserNotificationData

   def send_new_response_notification(user_ids, course, thread, replier_user):
      notification_data = UserNotificationData(
         user_ids=user_ids,
         notification_type="new_response",
         content_url=f"/{course.id}/posts/{thread.id}",
         app_name='discussion',
         course_key=course.id,
         context={
               'post_title': thread.title,
               'replier_name': replier_user.username,
         },
      )
      USER_NOTIFICATION_REQUESTED.send_event(notification_data=notification_data)

Explanation of the parameters for ``UserNotificationData``:

+------------------+---------------+---------------------------------------------------------------------------+
|Name              |Type           |Description                                                                |
+==================+===============+===========================================================================+
|user_ids          |list[int]      |List of user IDs to send the notification to.                              |
+------------------+---------------+---------------------------------------------------------------------------+
|notification_type |str            |The type of notification to send.                                          |
|                  |               |This must be a key of `COURSE_NOTIFICATION_TYPES`.                         |
+------------------+---------------+---------------------------------------------------------------------------+
|content_url       |str            |Url the user will navigate to if they click on the notification.           |
+------------------+---------------+---------------------------------------------------------------------------+
|app_name          |str            |The app this notification is associated with.                              |
|                  |               |This must be a key of `COURSE_NOTIFICATION_APPS`.                          |
+------------------+---------------+---------------------------------------------------------------------------+
|course_key        |CourseKey      |The course that this notification will be associated with.                 |
+------------------+---------------+---------------------------------------------------------------------------+
|context           |dict[str, str] |Context variables and values to pass to the notification content template. |
|                  |               |Keys are the variable names defined in the notification type.              |
+------------------+---------------+---------------------------------------------------------------------------+

That's it! You have implemented the code to send a new user notification using the ``USER_NOTIFICATION_REQUESTED`` signal.

Grouping notifications
======================

For some notification types, the volume for a learner can be huge and can cause annoyance. For example, if a learner creates a post, and other learners and staff members start adding responses to his post, if for each comment, we add a response, it could result in dozens of notifications. To avoid these scenarios, we have implemented a feature that allows grouping more than one similar notifications into a single notification.

Steps to group a notification:

#. Enable grouping waffle flag ``notifications.enable_notification_grouping``.
#. Add ``group_by_id`` in context before sending the ``USER_NOTIFICATION_REQUESTED`` event (see `discussions_notifications.py <https://github.com/openedx/openedx-platform/blob/cddc25cd791bb78f76833896e4778f668861df12/lms/djangoapps/discussion/rest_api/discussions_notifications.py#L88-L95>`_ for an example).
#. Implement a `grouper class <https://github.com/openedx/openedx-platform/blob/cddc25cd791bb78f76833896e4778f668861df12/openedx/core/djangoapps/notifications/grouping_notifications.py>`_ to modify content_context.

Legal
=====

When adding a new notification type, you will need a Privacy threshold assessment done by legal.

Troubleshooting
===============

If you have followed the above steps and notifications are still not working, check if the ``notifications.enable_notifications`` waffle flag is enabled.


How to override default notification preferences
################################################
This document explains how to override notification preferences defaults for new users who sign up on the platform. Learn more about notification, preferences and defaults `here <https://docs.openedx.org/en/latest/learners/sfd_notifications/index.html>`_.

.. note::
   
   These overrides will only apply to new users who sign up after the override has been configured.

Definitions
***********

Notification
   An alert that goes out to the user as a result of some activity e.g. "Mark responded to your post" etc.

Notification Preference
   A per-user setting for each notification type (web, email etc.). This is explained in the table below.

Notification apps
   For organization purposes, notification preferences are grouped by apps/platform workflows that they are related to. As of now, we have 3 apps: discussions, grading, and updates. Note that there is no app-level on/off switch for notifications types in it.

App-level defaults / Bundled preferences
   Each app discussed above has a set of app-level defaults (bundled preferences). A notification type marked `use_app_defaults: True` inherits its preferences from the app's app-level defaults instead of using its own default preferences. This enables grouping several notification types under one row of preferences visible to the user. For example, in case of discussions, 7 notification types are controlled by the app-level defaults of the discussions app, which appears on the Account Settings page as a single row labeled "Activity Notifications". This reduces clutter on the settings page.

What you can override
*********************

The table below lists all the preferences that you can override for each notification along with possible values. You can override defaults for both using the following dictionaries in your ``lms.yml``, ``cms.yml``, or ``settings.py``:

* Use ``NOTIFICATION_TYPES_OVERRIDE`` to override defaults for individual notification types.
* Use ``NOTIFICATION_APPS_OVERRIDE`` to override app-level defaults for notification types marked as ``use_app_defaults: True``. Use the internal keys listed below (``web``, ``email``, ``push``, ``email_cadence``, ``non_editable``).


+--------------+----------------+-------------------------------------+-------------------------------------------------------+
|Key           |Type            |Possible values                      |What it does                                           |
+==============+================+=====================================+=======================================================+
|web           |bool            |True OR False                        |Determines if the user gets notifications in the tray. |
+--------------+----------------+-------------------------------------+-------------------------------------------------------+
|email         |bool            |True OR False                        |Determines if the user gets notification in email.     |
+--------------+----------------+-------------------------------------+-------------------------------------------------------+
|push          |bool            |True OR False                        |Determines if user gets push notification in mobile    |                  
|              |                |                                     |apps (not implemented)                                 |
+--------------+----------------+-------------------------------------+-------------------------------------------------------+
|email_cadence |string          |'Immediately' OR 'Daily'             |Determines when a user receives email notification.    |
|              |                |OR 'Weekly' OR 'Never'               |                                                       |
+--------------+----------------+-------------------------------------+-------------------------------------------------------+
|non_editable  |list of strings |Any subset of ['web','email','push'] |Determines toggles of which of the 3 channels          |
|              |                |                                     |will not be editable by the user.                      |
+--------------+----------------+-------------------------------------+-------------------------------------------------------+

Notification keys are listed in the table below. More notifications may be added in the future. You can find notification keys in `this code <https://github.com/openedx/edx-platform/blob/2aeac459945e3e11c153fdb5203ea020514548d5/openedx/core/djangoapps/notifications/base_notification.py#L66>`_

+----+------------------+----------------------------------+-------------------+-------------------------------------+
|#   |Notification app  |Notification key                  |uses app defaults  |Appears on Account Settings page as  |
+====+==================+==================================+===================+=====================================+
|1   |discussion        |new_response                      |True               |Activity Notifications               |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|2   |discussion        |new_comment                       |True               |Activity Notifications               |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|3   |discussion        |new_comment_on_response           |True               |Activity Notifications               |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|4   |discussion        |response_on_followed_post         |True               |Activity Notifications               |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|5   |discussion        |comment_on_followed_post          |True               |Activity Notifications               |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|6   |discussion        |response_endorsed_on_thread       |True               |Activity Notifications               |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|7   |discussion        |response_endorsed                 |True               |Activity Notifications               |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|8   |discussion        |content_reported                  |False              |Reported content                     |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|9   |discussion        |new_question_post                 |False              |New question posts                   |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|10  |discussion        |new_discussion_post               |False              |New discussion posts                 |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|11  |discussion        |new_instructor_all_learners_post  |False              |New posts from instructors           |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|12  |updates           |course_updates                    |False              |Course updates                       |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|13  |grading           |ora_staff_notifications           |False              |New ORA submission for staff         |
+----+------------------+----------------------------------+-------------------+-------------------------------------+
|14  |grading           |ora_grade_assigned                |False              |ORA grade received                   |
+----+------------------+----------------------------------+-------------------+-------------------------------------+

Example configurations
**********************

Example configuration for overriding notification preferences

.. code-block:: python

   NOTIFICATION_TYPES_OVERRIDE = {
      # Turn off tray and turn on email notifications for new discussion posts and set daily cadence.
      'new_discussion_post': {
         'email': True,
         'web': False,
         'email_cadence': 'Daily',
      },
      # Turn off email notifications for "Course Updates" and prevent users from changing it.
      'course_updates': {
         'email': False,
         'non_editable': ['email'],
      }
   }

Example configuration for overriding app-level defaults for notifications marked as use_app_defaults: True

.. code-block:: python

   NOTIFICATION_APPS_OVERRIDE = {
      # For the 'discussion' app, set tray on and email off for all app-default notifications.
      'discussion': {
         'email': False,
         'web': True,
         'email_cadence': 'Immediately',
      }
   }

Why isn't my override working?
==============================

* See if you are using the exact key name (e.g. ``new_discussion_post`` and not ``New_discussion_post``).
* If a notification is marked as ``use_app_defaults: True`` in the code, it will ignore overrides in ``NOTIFICATION_TYPES_OVERRIDE``. You must override using ``NOTIFICATION_APPS_OVERRIDE`` instead.


.. seealso::

   :ref:`ora-reminder-notifications` — configure periodic nudges for learners who have not completed peer or self review steps in ORA assignments.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  |         Reviewer              |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|2026-05-05    | Ahtisham Shahid               | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
|2026-04-30    | Sara Burns                    | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
|2025-12-18    | BTR WG                        | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+

