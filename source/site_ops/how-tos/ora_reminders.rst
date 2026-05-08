.. _ora-reminder-notifications:

ORA Reminder Notifications
##########################

.. tags:: site operator, how-to

ORA reminders send periodic nudges to learners who have submitted a response
but have not yet completed their required **peer** or **self** review steps.

Enabling
********

Set ``ENABLE_ORA_REMINDERS`` to ``True`` in your Django settings:

.. code-block:: python

    ENABLE_ORA_REMINDERS = True

The notification type ``ora_reminder`` must also be registered in openedx-platform's
``openedx.core.djangoapps.notifications.base_notification`` (already included
starting with Verawood release).

Configuration Settings
**********************

All settings have sensible defaults and only need to be overridden when you
want non-default behaviour.

.. list-table::
   :header-rows: 1
   :widths: 35 10 55

   * - Setting
     - Default
     - Description
   * - ``ORA_REMINDER_INITIAL_DELAY_HOURS``
     - ``0``
     - Hours after submission before the **first** reminder is sent. Gives
       learners time to complete reviews on their own before being nudged.
   * - ``ORA_REMINDER_INTERVAL_HOURS``
     - ``48``
     - Hours between consecutive reminders after the first one.
   * - ``ORA_REMINDER_MAX_COUNT``
     - ``3``
     - Maximum number of reminders sent per learner per ORA submission.
       Once this limit is reached the reminder row is deactivated.
   * - ``ORA_REMINDER_SWEEP_INTERVAL_SECONDS``
     - ``1800``
     - How often (in seconds) the sweeper re-schedules itself. Each run
       processes all rows whose ``next_reminder_at`` has passed.
   * - ``ORA_REMINDER_SWEEP_BATCH_SIZE``
     - ``1000``
     - Maximum rows processed per sweep cycle. If more rows are due they
       will be picked up on the next sweep. Rows are ordered oldest-first so
       no reminder is permanently skipped. Increase this value for deployments
       with a large number of concurrent active learners.
   * - ``ORA_REMINDER_CHECK_AGAIN_HOURS``
     - ``12``
     - Hours to wait before re-checking when a peer-step reminder is due
       but no peer submissions are available for the learner to review yet.
       Prevents sending useless reminders to very early submitters.

To override these settings, create a Tutor plugin that patches the LMS
settings using the ``openedx-lms-common-settings``
`patch <https://docs.tutor.edly.io/reference/patches/index.html>`_,
which applies to both production and development environments.

For example, create a file ``ora_reminders_plugin.py``:

.. code-block:: python

    from tutor import hooks

    hooks.Filters.ENV_PATCHES.add_item((
        "openedx-lms-common-settings",
        """
          ORA_REMINDER_INITIAL_DELAY_HOURS = 48
          ORA_REMINDER_INTERVAL_HOURS = 72
          ORA_REMINDER_MAX_COUNT = 2
    """
    ))

Then install and enable it in your Tutor environment, according to the `Tutor documentation <https://docs.tutor.edly.io/reference/patches/index.html>`_.


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-05   | Ahtisham Shahid               | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
