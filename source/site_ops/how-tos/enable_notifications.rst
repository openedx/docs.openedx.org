.. _Enable Notifications:
.. _Configure Platform Notifications:

Enable Notifications
####################

.. tags:: site operator, how-to

.. note::

   The notifications feature was rolled out in Ulmo and has been enabled by
   default since the Verawood release. Several notification changes were also
   introduced in Verawood. See :ref:`Verawood Dev Notes`.

This document describes how to enable, disable, or configure notifications.
To learn about the notifications feature, see :ref:`Notifications & Preferences`.

Before configuring notifications, confirm the following:

* Email delivery is configured for the platform.
* Celery workers are running for asynchronous notification and digest tasks.

Disable Notifications
*********************

Platform notifications are enabled by default. Unless the notification feature
is disabled, users see the notification tray in the LMS and Studio, and
notification preferences on the *Account Settings* page. Notification emails
are also enabled by default, but they are delivered only when a notification is
generated for a user whose email preference for that notification type is
enabled, and the Open edX instance is configured to send ACE email through an
email provider.

Use these waffle flags to disable notifications:

.. list-table::
   :header-rows: 1
   :widths: 35 10 55

   * - Waffle flag
     - Default
     - Description
   * - ``notifications.disable_notifications``
     - ``False``
     - Disables the notification feature and hides the notification tray and
       notification preferences.
   * - ``notifications.disable_email_notifications``
     - ``False``
     - Disables notification emails without disabling the notification tray.

The ``Web`` channel is always visible in notification preferences and controls
tray notifications. The ``Email`` channel is visible by default and can be
hidden by setting ``SHOW_EMAIL_CHANNEL`` to ``False`` and then rebuilding the
MFE image. Hiding the email channel does not disable email notifications.


Configure Notification Email Delivery
*************************************

Daily and weekly digest emails are scheduled through Celery when notifications
are created. Do not configure cron jobs for daily or weekly notification digest
emails.

Use these settings to configure notification email delivery:

.. list-table::
   :header-rows: 1
   :widths: 40 15 45

   * - Setting
     - Default
     - Description
   * - ``NOTIFICATIONS_DEFAULT_FROM_EMAIL``
     - ``"no-reply@example.com"``
     - The sender address used for notification emails. Override this value for
       production deployments.
   * - ``NOTIFICATION_IMMEDIATE_EMAIL_BUFFER_MINUTES``
     - ``15``
     - Buffer window, in minutes, for immediate notification emails. The first
       immediate email is sent right away; additional immediate notifications
       in the buffer window are grouped into a digest email.
   * - ``NOTIFICATION_DAILY_DIGEST_DELIVERY_HOUR``
     - ``17``
     - Hour of day, in UTC, when daily digest emails are sent.
   * - ``NOTIFICATION_DAILY_DIGEST_DELIVERY_MINUTE``
     - ``0``
     - Minute of the hour when daily digest emails are sent.
   * - ``NOTIFICATION_WEEKLY_DIGEST_DELIVERY_DAY``
     - ``0``
     - Day of the week when weekly digest emails are sent. ``0`` is Monday and
       ``6`` is Sunday.
   * - ``NOTIFICATION_WEEKLY_DIGEST_DELIVERY_HOUR``
     - ``17``
     - Hour of day, in UTC, when weekly digest emails are sent.
   * - ``NOTIFICATION_WEEKLY_DIGEST_DELIVERY_MINUTE``
     - ``0``
     - Minute of the hour when weekly digest emails are sent.


Configure Default Notification Preferences
******************************************

Operators can override the defaults used when notification preferences are
created for users.

Notification preferences are organized by notification app and notification
type. Some notification types have their own defaults while others
use app-level defaults by setting ``use_app_defaults: True``. These app-level
defaults are also used to bundle related notification types under one row on the
*Account Settings* page.

Overrides apply when new ``NotificationPreference`` rows are created. They do
not automatically update existing user preference rows.

Where to Configure These Settings
=================================

``NOTIFICATION_APPS_OVERRIDE`` and ``NOTIFICATION_TYPES_OVERRIDE`` are LMS
Django settings. For Tutor deployments, create a Tutor plugin file, for
example ``notification_preferences.py``, and patch the LMS settings with the
``openedx-lms-common-settings`` patch. For other deployments, add these values
to the LMS Django settings override used by the deployment.

For example:

.. code-block:: python

   from textwrap import dedent

   from tutor import hooks

   hooks.Filters.ENV_PATCHES.add_item((
       "openedx-lms-common-settings",
       dedent("""
       NOTIFICATION_APPS_OVERRIDE = {
           "discussion": {
               "email": True,
               "email_cadence": "Daily",
           },
       }
       """),
   ))


.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Setting
     - Description
   * - ``NOTIFICATION_TYPES_OVERRIDE``
     - Changes defaults for individual notification types.
   * - ``NOTIFICATION_APPS_OVERRIDE``
     - Changes app-level defaults used by notification types with
       ``use_app_defaults: True``.



Supported override keys are:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Key
     - Values
     - Description
   * - ``web``
     - ``True`` or ``False``
     - Enables or disables tray notifications for the preference.
   * - ``email``
     - ``True`` or ``False``
     - Enables or disables email notifications for the preference.
   * - ``email_cadence``
     - ``Immediately``, ``Daily``, ``Weekly``, or ``Never``
     - Sets the default email cadence.
   * - ``non_editable``
     - List containing ``web`` or ``email``
     - Lists channels that learners cannot change.

Unknown notification keys and unsupported override fields are ignored.

For notification types that use app-level defaults, prefer
``NOTIFICATION_APPS_OVERRIDE`` so every notification type in the grouped
preference row uses the same defaults. Use ``NOTIFICATION_TYPES_OVERRIDE`` for
notification types that have their own preference rows.

Example configurations:

.. code-block:: python

   NOTIFICATION_APPS_OVERRIDE = {
       # Applies to discussion notification types that use app-level defaults.
       "discussion": {
           "email": True,
           "email_cadence": "Daily",
       },
   }

   NOTIFICATION_TYPES_OVERRIDE = {
       # Applies to a specific notification type.
       "course_updates": {
           "web": True,
           "email": True,
           "email_cadence": "Immediately",
       },
   }

Notification Apps and Types
===========================

Operators need internal notification app and type keys when writing default
preference overrides. Notification apps provide app-level defaults. Notification
types either inherit those app defaults or define their own defaults.

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Notification app key
     - Tray default
     - Email default
     - Email cadence default
   * - ``discussion``
     - ``True``
     - ``True``
     - ``Daily``
   * - ``updates``
     - ``True``
     - ``True``
     - ``Daily``
   * - ``grading``
     - ``True``
     - ``True``
     - ``Daily``

.. list-table::
   :header-rows: 1
   :widths: 28 16 14 24 18

   * - Notification type key
     - App key
     - Uses app defaults
     - Preference name
     - Default
   * - ``new_response``
     - ``discussion``
     - Yes
     - Activity notifications
     - App default
   * - ``new_comment``
     - ``discussion``
     - Yes
     - Activity notifications
     - App default
   * - ``new_comment_on_response``
     - ``discussion``
     - Yes
     - Activity notifications
     - App default
   * - ``response_on_followed_post``
     - ``discussion``
     - Yes
     - Activity notifications
     - App default
   * - ``comment_on_followed_post``
     - ``discussion``
     - Yes
     - Activity notifications
     - App default
   * - ``response_endorsed_on_thread``
     - ``discussion``
     - Yes
     - Activity notifications
     - App default
   * - ``response_endorsed``
     - ``discussion``
     - Yes
     - Activity notifications
     - App default
   * - ``content_reported``
     - ``discussion``
     - No
     - Reported content
     - Tray on, email daily
   * - ``new_discussion_post``
     - ``discussion``
     - No
     - New discussion posts
     - Tray off, email off
   * - ``new_question_post``
     - ``discussion``
     - No
     - New question posts
     - Tray off, email off
   * - ``new_instructor_all_learners_post``
     - ``discussion``
     - No
     - New posts from instructors
     - Tray on, email daily
   * - ``course_updates``
     - ``updates``
     - No
     - Course updates
     - Tray on, email daily
   * - ``ora_staff_notifications``
     - ``grading``
     - No
     - New ORA submission for staff grading
     - Tray on, email off
   * - ``ora_grade_assigned``
     - ``grading``
     - No
     - Essay assignment grade received
     - Tray on, email daily
   * - ``ora_reminder``
     - ``grading``
     - No
     - Essay assignment reminders
     - Tray on, email daily

For learner-facing explanations of these activities, see
:ref:`Notifications & Preferences` and
:ref:`Staying Updated with Notifications`.

.. _ora-reminder-notifications:

Configure ORA Reminder Notifications
************************************

ORA reminders notify learners who have submitted an ORA response but have not
completed required peer or self review steps.

ORA reminder notifications are enabled by default. Set
``ENABLE_ORA_REMINDERS`` to ``False`` to disable scheduled ORA reminders.

Configuration Settings
======================

The following ORA reminder settings have defaults and only need to be changed
when a deployment requires different reminder timing, reminder limits, or sweep
behavior.

.. list-table::
   :header-rows: 1
   :widths: 35 10 55

   * - Setting
     - Default
     - Description
   * - ``ORA_REMINDER_INITIAL_DELAY_HOURS``
     - ``0``
     - Hours after submission before the first reminder is sent.
   * - ``ORA_REMINDER_INTERVAL_HOURS``
     - ``48``
     - Hours between consecutive reminders after the first reminder.
   * - ``ORA_REMINDER_MAX_COUNT``
     - ``3``
     - Maximum number of reminders sent per learner per ORA submission.
   * - ``ORA_REMINDER_SWEEP_INTERVAL_SECONDS``
     - ``1800``
     - How often, in seconds, the sweeper task schedules itself.
   * - ``ORA_REMINDER_SWEEP_BATCH_SIZE``
     - ``1000``
     - Maximum number of reminder rows processed in each sweep cycle.
   * - ``ORA_REMINDER_CHECK_AGAIN_HOURS``
     - ``12``
     - Hours to wait before checking again when a peer review reminder is due
       but no peer submissions are available for the learner to review.

Add ORA reminder settings to the same LMS Django settings override that is used
for the notification settings in this document.

For example:

.. code-block:: python

   ORA_REMINDER_INITIAL_DELAY_HOURS = 48
   ORA_REMINDER_INTERVAL_HOURS = 72
   ORA_REMINDER_MAX_COUNT = 2

How ORA Reminders Work
======================

When a learner submits an ORA response that requires peer or self review, Open
edX creates a reminder row for that learner and submission. A Celery sweeper
task runs on a configurable interval and processes reminder rows whose next
reminder time has passed.

The sweeper sends an ``ora_reminder`` notification when the learner still has a
required peer or self review step to complete. The reminder is not sent when
the learner has completed the required step, the relevant deadline has passed,
the course has ended, or the maximum reminder count has been reached.

For peer review steps, if no peer submissions are available for the learner to
review, the reminder is deferred by ``ORA_REMINDER_CHECK_AGAIN_HOURS``. That
deferral does not count toward ``ORA_REMINDER_MAX_COUNT``.

Related Documentation
*********************

* :ref:`Notifications & Preferences`
* :ref:`Staying Updated with Notifications`


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| Jul 09, 2026 | Aamir Ayub                    | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
