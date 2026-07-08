.. _Verawood Dev Notes:

Open edX Verawood Developer & Operator Release Notes
#####################################################

*Releasing June, 2026!*

These are the developer & operator release notes for the Verawood release, the 22nd
community release of the Open edX Platform, spanning changes from October 30,
2025 to April 9, 2026. You can also review details about :ref:`Open edX Release Notes` or
learn more about the `Open edX Platform`_.

To view the end-user facing docs, see the :ref:`Verawood Product Notes`.

.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
****************

* Notifications and notification emails are now enabled by default. The previous
  opt-in waffle flags, ``notifications.enable_notifications`` and
  ``notifications.enable_email_notifications``, have been replaced by opt-out
  flags. Operators who need to keep notifications disabled after upgrading must
  enable `notifications.disable_notifications
  <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/core/djangoapps/notifications/config/waffle.py#L10-L19>`_
  or `notifications.disable_email_notifications
  <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/core/djangoapps/notifications/config/waffle.py#L21-L30>`_.

* Course-level notification preferences have been removed. Integrations that
  read ``CourseNotificationPreference`` records should migrate to account-level
  notification preferences and the V3 preferences API. See the `model deletion
  migration
  <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/core/djangoapps/notifications/migrations/0010_delete_coursenotificationpreference.py#L12-L15>`_.

* Notification preference configuration no longer uses the ``is_core`` flag or
  ``core_web``, ``core_email``, and ``core_push`` fields. Clients that consume
  notification preference configuration data should use ``use_app_defaults`` and
  the plain channel fields exposed by the V3 preferences API. See the
  `notification type schema
  <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/core/djangoapps/notifications/base_notification.py#L27-L56>`_
  and `V3 preferences view
  <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/core/djangoapps/notifications/views.py#L253-L309>`_.

Deprecations & Removals
***********************

* The notification preferences V2 configuration API and its related manager
  classes have been removed. Integrations that called
  ``/api/notifications/v2/configurations/`` should use the
  ``/api/notifications/v3/configurations/`` endpoint instead. See the `V3 route
  <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/core/djangoapps/notifications/urls.py#L18-L23>`_
  and `V3 preferences view
  <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/core/djangoapps/notifications/views.py#L253-L309>`_.

* The ``send_email_digest`` management command is deprecated. Daily and weekly
  notification digests are now scheduled automatically with Celery when
  qualifying notifications are created. Cron jobs that still call this command
  will only emit a deprecation warning and should be removed.

* Several Learning MFE right-sidebar plugin slot names and "notification"
  aliases for the upgrade panel are deprecated. Existing plugin configurations
  continue to work through backward-compatible aliases, but new customizations
  should use the renamed right-sidebar and upgrade-panel slots. See the
  `upgrade widget migration notes
  <https://github.com/openedx/frontend-app-learning/blob/038c8f379a5c280019b03fe38fdda9a4aba2788d/docs/decisions/0010-upgrade-widget-extraction.md#deprecated-identifiers>`_.

Aspects Analytics
*****************************

Administrators & Operators
**************************

* The Learning MFE right sidebar now supports configurable widgets. Operators
  and plugin developers can register additional right-sidebar panels with
  ``SIDEBAR_WIDGETS`` in ``env.config.jsx``. The existing upgrade/upsell sidebar
  panel was renamed from "Notifications" to "Upgrade" to avoid confusion with
  platform notifications, and remains enabled by default for backward
  compatibility. Operators can disable it by configuring a widget entry with
  ``id: 'UPGRADE'`` and ``enabled: false``. See the `SIDEBAR_WIDGETS
  configuration key
  <https://github.com/openedx/frontend-app-learning/blob/038c8f379a5c280019b03fe38fdda9a4aba2788d/src/courseware/course/sidebar/constants.js#L11-L13>`_,
  `default sidebar widgets
  <https://github.com/openedx/frontend-app-learning/blob/038c8f379a5c280019b03fe38fdda9a4aba2788d/src/courseware/course/sidebar/defaultWidgets.js#L9-L27>`_,
  and `upgrade widget API
  <https://github.com/openedx/frontend-app-learning/blob/038c8f379a5c280019b03fe38fdda9a4aba2788d/src/widgets/upgrade/README.md#api>`_.

* Notification preference defaults can now be managed at the instance level.
  Operators can override defaults for existing notification apps and types
  without code changes. See `How to override default notification preferences
  </site_ops/how-tos/enable_notifications.html#how-to-override-default-notification-preferences>`_.

* Immediate email notifications now use a configurable buffer window. The first
  notification is sent immediately; additional immediate-cadence notifications
  inside the window are combined into one buffered digest.

* Daily and weekly notification digest emails no longer require cron jobs. If
  you previously scheduled ``send_email_digest`` with cron, remove those jobs
  after upgrading. By default, daily digests are delivered at 17:00 UTC, and
  weekly digests are delivered on Monday at 17:00 UTC. See `Notification Digest
  Email </site_ops/how-tos/enable_notifications.html#notification-digest-email>`_.

* ORA reminder notifications are now available. Learners who submit an Open
  Response Assessment but still need to complete required peer or self review
  steps can receive ``ora_reminder`` web and email notifications. The Verawood
  backport registers the `ora_reminder notification type
  <https://github.com/openedx/edx-platform/blob/261008aa82d5b534645e5ea19ff14da2eaca1381/openedx/core/djangoapps/notifications/base_notification.py#L277-L289>`_
  and updates openedx-platform to `ora2 7.1.0
  <https://github.com/openedx/edx-platform/blob/261008aa82d5b534645e5ea19ff14da2eaca1381/requirements/edx/base.txt#L874>`_,
  which includes the reminder sweeper. See `ORA Reminder Notifications
  </site_ops/how-tos/ora_reminders.html>`_.

Settings and Toggles
********************

Added Settings
==============

* +NOTIFICATION_IMMEDIATE_EMAIL_BUFFER_MINUTES: `openedx/envs/common.py (line 2688) <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/envs/common.py#L2688>`_

  * Default value = ``15``
  * Description: Number of minutes to buffer additional immediate-cadence email
    notifications after the first immediate email is sent.

* +NOTIFICATION_DAILY_DIGEST_DELIVERY_HOUR: `openedx/envs/common.py (line 2694) <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/envs/common.py#L2694>`_

  * Default value = ``17``
  * Description: Hour of day, in UTC, to send daily digest emails.

* +NOTIFICATION_DAILY_DIGEST_DELIVERY_MINUTE: `openedx/envs/common.py (line 2695) <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/envs/common.py#L2695>`_

  * Default value = ``0``
  * Description: Minute of hour to send daily digest emails.

* +NOTIFICATION_WEEKLY_DIGEST_DELIVERY_DAY: `openedx/envs/common.py (line 2696) <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/envs/common.py#L2696>`_

  * Default value = ``0``
  * Description: Day of week to send weekly digest emails, where ``0`` is
    Monday and ``6`` is Sunday.

* +NOTIFICATION_WEEKLY_DIGEST_DELIVERY_HOUR: `openedx/envs/common.py (line 2697) <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/envs/common.py#L2697>`_

  * Default value = ``17``
  * Description: Hour of day, in UTC, to send weekly digest emails.

* +NOTIFICATION_WEEKLY_DIGEST_DELIVERY_MINUTE: `openedx/envs/common.py (line 2698) <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/envs/common.py#L2698>`_

  * Default value = ``0``
  * Description: Minute of hour to send weekly digest emails.

* +NOTIFICATION_APPS_OVERRIDE: `openedx/envs/common.py (line 2703) <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/envs/common.py#L2703>`_

  * Default value = ``{}``
  * Description: Overrides default notification preferences for existing
    notification apps. Supported override keys are ``web``, ``email``,
    ``push``, ``non_editable``, and ``email_cadence``.

* +NOTIFICATION_TYPES_OVERRIDE: `openedx/envs/common.py (line 2704) <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/envs/common.py#L2704>`_

  * Default value = ``{}``
  * Description: Overrides default notification preferences for existing
    notification types. Supported override keys are ``web``, ``email``,
    ``push``, ``non_editable``, and ``email_cadence``.

* +ENABLE_ORA_REMINDERS: `edx-ora2/settings/base.py (line 187) <https://github.com/openedx/edx-ora2/blob/95c188d3329cdcd0d77f0c38995750f0e2dbe46f/settings/base.py#L187>`_

  * Default value = ``True``
  * Description: Enables scheduled ORA reminder notifications for learners who
    need to complete peer or self reviews.

* +ORA_REMINDER_MAX_COUNT: `edx-ora2/settings/base.py (line 190) <https://github.com/openedx/edx-ora2/blob/95c188d3329cdcd0d77f0c38995750f0e2dbe46f/settings/base.py#L190>`_

  * Default value = ``3``
  * Description: Maximum number of reminders sent per learner per ORA
    submission.

* +ORA_REMINDER_INTERVAL_HOURS: `edx-ora2/settings/base.py (line 193) <https://github.com/openedx/edx-ora2/blob/95c188d3329cdcd0d77f0c38995750f0e2dbe46f/settings/base.py#L193>`_

  * Default value = ``48``
  * Description: Hours between consecutive ORA reminder notifications.

* +ORA_REMINDER_INITIAL_DELAY_HOURS: `edx-ora2/settings/base.py (line 199) <https://github.com/openedx/edx-ora2/blob/95c188d3329cdcd0d77f0c38995750f0e2dbe46f/settings/base.py#L195-L199>`_

  * Default value = ``0``
  * Description: Hours after submission before the first ORA reminder is sent.

* +ORA_REMINDER_SWEEP_INTERVAL_SECONDS: `edx-ora2/settings/base.py (line 203) <https://github.com/openedx/edx-ora2/blob/95c188d3329cdcd0d77f0c38995750f0e2dbe46f/settings/base.py#L201-L203>`_

  * Default value = ``1800``
  * Description: How often the ORA reminder sweeper Celery task re-schedules
    itself.

* +ORA_REMINDER_SWEEP_BATCH_SIZE: `edx-ora2/settings/base.py (line 207) <https://github.com/openedx/edx-ora2/blob/95c188d3329cdcd0d77f0c38995750f0e2dbe46f/settings/base.py#L205-L207>`_

  * Default value = ``1000``
  * Description: Maximum number of ORA reminder rows processed per sweep cycle.

* +ORA_REMINDER_CHECK_AGAIN_HOURS: `edx-ora2/settings/base.py (line 211) <https://github.com/openedx/edx-ora2/blob/95c188d3329cdcd0d77f0c38995750f0e2dbe46f/settings/base.py#L209-L211>`_

  * Default value = ``12``
  * Description: Hours to wait before re-checking when no peer submissions are
    available yet.

Added Feature Toggles
=====================

* +notifications.disable_notifications: `openedx/core/djangoapps/notifications/config/waffle.py (line 10) <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/core/djangoapps/notifications/config/waffle.py#L10-L19>`_

  * Default value = ``False``
  * Description: Disables the Notifications feature when enabled. When unset,
    notifications are enabled by default.

* +notifications.disable_email_notifications: `openedx/core/djangoapps/notifications/config/waffle.py (line 21) <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/core/djangoapps/notifications/config/waffle.py#L21-L30>`_

  * Default value = ``False``
  * Description: Disables notification emails when enabled. When unset,
    notification emails are enabled by default.

Removed Feature Toggles
=======================

* -notifications.enable_notifications

  * Description: Replaced by ``notifications.disable_notifications``.

* -notifications.enable_email_notifications

  * Description: Replaced by ``notifications.disable_email_notifications``.

Developer Experience
********************

Known Issues
************

See the `Build Test Release project board <https://github.com/orgs/openedx/projects/28>`_ for known open issues.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
