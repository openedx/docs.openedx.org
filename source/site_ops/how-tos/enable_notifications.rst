.. _Enable Notifications:

Enable Notifications
####################

.. tags:: site operator, how-to

:ref:`Notifications <Notifications & Preferences>` keep you informed about activity in your
courses, alerting you via one or both of in-platform notifications and email notifications.
They span activities such as Discussions updates, Course updates, and Grading updates.

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

Configure daily and weekly email digests
****************************************

The notifications Tutor plugin does **not** provide built-in configuration for
cron jobs needed for email digests. However, the Open edX platform supports **daily and weekly
notification digests** through management commands.

.. important::
   Default preference for email notifications for all users is ``Daily``.
   Therefore, by default, users will not receive any notification emails unless this cron job is configured.

To enable these digests, site operators must configure `cron jobs <https://www.redhat.com/en/blog/linux-cron-command>`_ on the host machine where tutor
is being used to deploy the Open edX platform.

On the Linux host machine site operators need to run `crontab -e` for adding the cron jobs. This command opens up 
an editor where the below mentioned command needs to be written. Site operators can modify these command to customize the
time to send the notification email. They need to change the command to `tutor local ...` or `tutor k8s ...` depending on
if they are running the instance locally or using kubernetes.


Daily email digest
==================

The following cron job sends the daily digest at **10:00 PM**:

.. code-block:: bash

   0 22 * * * tutor local run lms ./manage.py lms send_email_digest Daily


Weekly email digest
===================

The following cron job sends the weekly digest every **Sunday at 10:00 PM**:

.. code-block:: bash

   0 22 * * SUN tutor local run lms ./manage.py lms send_email_digest Weekly

.. note::

   You can change the delivery time by modifying the cron schedule according to
   your operational requirements. For example, `0 22 * * *` schedules the command to run everyday at **10:00 PM**
   this can be modified to run at the hours/days of choice.


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|2025-12-18    | BTR WG                        | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+

