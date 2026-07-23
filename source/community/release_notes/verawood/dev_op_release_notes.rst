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

* ``HELP_TOKENS_BOOKS`` and ``help_tokens.ini`` now reference the official Open
  edX documentation.

  The ``HELP_TOKENS_BOOKS`` setting has been updated to reference the official
  Open edX documentation. Similarly, the ``help_tokens.ini`` file, which is
  specified in the ``HELP_TOKENS_INI_FILE`` setting, was updated in both the LMS
  and CMS configurations to ensure the paths align with the official Open edX
  documentation.

  This is a breaking change that many operators may want, but if you wish to
  retain the original values, you must provide overrides. See
  `Update HELP_TOKENS_BOOKS to use official Open edX docs <https://github.com/openedx/edx-platform/pull/37493>`_.

* **Possible failed migration during upgrade.** Due to a bug that was present in
  the last several releases, it was possible for users to create multiple
  courses with similar course IDs that differed only in capitalization. Such
  courses would only appear as a single course in most parts of the system, and
  may not work properly at all. That bug has been fixed, and a new database
  constraint will prevent that from happening going forward.

  However, if you have any of these "case duplicate" courses, the
  ``split_modulestore_django`` migration ``0004_courseid_unique_ci`` will fail
  with an ``IntegrityError``. If you encounter this, follow the instructions to
  delete the invalid course record(s), and then you should be able to apply the
  migration and continue.

* **edx-search Typesense server requirement update.** The ``typesense-python``
  client library was upgraded from 1.x to 2.0.0. This version is only compatible
  with Typesense Server >= v30.0.

  Action required if you use the Typesense search backend (``SEARCH_ENGINE =
  "search.typesense.TypesenseEngine"``): upgrade your Typesense server to v30.0
  or later before deploying this Open edX release. No action is needed if you
  use the default Elasticsearch backend. See
  `edx-search PR #254 <https://github.com/openedx/edx-search/pull/254>`_ and the
  `typesense-python compatibility matrix <https://github.com/typesense/typesense-python#compatibility>`_
  for details.

* **Upgrade/upsell ("notifications") panel replaced in Learning MFE.** The
  Learning MFE right sidebar now uses a configurable widget registry, and the
  upgrade/upsell widget was renamed internally from "Notifications" to
  "Upgrade."

  * The Upgrade widget remains enabled by default in Verawood; operators do
    not need to add it to ``SIDEBAR_WIDGETS``. To disable it, configure
    ``SIDEBAR_WIDGETS: [{ id: 'UPGRADE', enabled: false }]``.
  * Plugin developers should migrate the old notification-tray slot to the
    Upgrade Panel slot, and the old discussions-sidebar slots to the Right
    Sidebar and Right Sidebar Trigger slots. Deprecated aliases remain
    compatible for now.
  * Upgrade widget ``localStorage`` keys were renamed and are not migrated,
    so stored widget state may reset after upgrading.
  * See the `Upgrade Widget migration notes
    <https://github.com/openedx/frontend-app-learning/blob/master/docs/decisions/0010-upgrade-widget-extraction.md>`_
    for configuration examples and the complete identifier mapping.

* **Notifications and notification emails are now enabled by default.** The
  previous opt-in waffle flags, ``notifications.enable_notifications`` and
  ``notifications.enable_email_notifications``, have been replaced by
  opt-out flags. Operators who need to keep notifications disabled after
  upgrading must enable ``notifications.disable_notifications`` or
  ``notifications.disable_email_notifications``.

  * ``notifications.disable_notifications`` (default ``False``): when
    enabled, disables the Notifications feature; when unset, notifications
    are enabled by default.
  * ``notifications.disable_email_notifications`` (default ``False``): when
    enabled, disables notification emails; when unset, notification emails
    are enabled by default.
  * ``notifications.enable_notifications`` and
    ``notifications.enable_email_notifications`` have been removed; they are
    replaced by the flags above.

Deprecations & Removals
***********************

* **Custom edx-val storage settings deprecated in favor of Django STORAGES.**

  The ``edx-val`` application previously relied on custom settings
  (``VIDEO_IMAGE_SETTINGS``, ``VIDEO_TRANSCRIPTS_SETTINGS``, etc.) to determine
  storage backends. This behavior is now deprecated in favor of the standard
  Django 5.2+ ``STORAGES`` configuration. The key within the ``STORAGES`` config
  for a custom video transcript location is ``video_transcripts``. See
  `edx-val PR #593 <https://github.com/openedx/edx-val/pull/593/files>`_.

  As of Verawood:

  * ``edx-val`` now correctly respects Django's ``STORAGES`` dict, giving it
    precedence over legacy per-feature storage settings.
  * Custom ``edx-val`` storage settings will continue to function during the
    Verawood cycle but are officially deprecated and will be removed in a
    future release.
  * Operators should migrate their storage configuration to Django's
    ``STORAGES`` format to ensure forward compatibility.

  **Required action for operators:**

  #. Define the required ``edx-val`` storages inside Django's ``STORAGES``
     dictionary (e.g., for transcripts, videos, and images).
  #. Remove or stop relying on deprecated ``edx-val`` -specific storage
     configuration variables.
  #. Review any existing custom overrides in ``lms/envs/common.py`` or
     deployment-specific files to ensure compatibility.

  Failure to migrate before the legacy settings are removed may result in
  incorrect storage backends being used.

* The ``SERVICE_VARIANT`` setting is no longer set from the environment. The
  setting will be set to ``'cms'`` in ``cms/envs/common.py`` and to ``'lms'`` in
  ``lms/envs/common.py`` regardless of any environment variable set.

* CMS settings ``ID_VERIFICATION_SUPPORT_LINK``,
  ``PASSWORD_RESET_SUPPORT_LINK``, ``ACTIVATION_EMAIL_SUPPORT_LINK``, and
  ``LOGIN_ISSUE_SUPPORT_LINK`` are now set to the value of the
  ``SUPPORT_SITE_LINK`` setting. Previously they defaulted to ``''``.

* The setting ``USE_L10N`` was removed since it was removed in Django 5.0.

* **Notifications** ``send_email_digest`` **management command deprecated.**
  The command still exists, but it is now a no-op that emits a deprecation
  warning. Daily and weekly notification digests are now scheduled
  automatically with Celery when qualifying notifications are created.
  Operators who previously scheduled ``send_email_digest`` with cron should
  remove those cron jobs after upgrading. By default, daily digests are
  delivered at 17:00 UTC, and weekly digests are delivered on Monday at
  17:00 UTC. See `edx-platform PR #38185
  <https://github.com/openedx/edx-platform/pull/38185>`_ and `Configure
  Notification Email Delivery
  <https://docs.openedx.org/en/latest/site_ops/how-tos/enable_notifications.html#configure-notification-email-delivery>`_.

  * ``NOTIFICATION_DAILY_DIGEST_DELIVERY_HOUR`` (default ``17``): hour of
    day, in UTC, to send daily digest emails.
  * ``NOTIFICATION_DAILY_DIGEST_DELIVERY_MINUTE`` (default ``0``): minute of
    the hour to send daily digest emails.
  * ``NOTIFICATION_WEEKLY_DIGEST_DELIVERY_DAY`` (default ``0``): day of the
    week to send weekly digest emails, where ``0`` is Monday and ``6`` is
    Sunday.
  * ``NOTIFICATION_WEEKLY_DIGEST_DELIVERY_HOUR`` (default ``17``): hour of
    day, in UTC, to send weekly digest emails.
  * ``NOTIFICATION_WEEKLY_DIGEST_DELIVERY_MINUTE`` (default ``0``): minute of
    the hour to send weekly digest emails.

* **REGISTRATION_EXTENSION_FORM replaced.** The ``REGISTRATION_EXTENSION_FORM``
  setting will stop working starting with the next release. It has been
  replaced with the ``PROFILE_EXTENSION_FORM`` setting.

  Previously, data was only stored as JSON in the ``UserProfile`` ``meta``
  field. Moving forward, this information will also be stored in the custom
  model that extends the fields.

  **Action for operators:** to prevent extended user fields from appearing
  empty or outdated after the update, you may need to write and run a custom
  data migration script to move existing information from the ``meta`` field
  to your custom model, and perform this migration before activating the new
  ``PROFILE_EXTENSION_FORM`` setting. See
  `edx-platform PR #37119 <https://github.com/openedx/edx-platform/pull/37119>`_
  for more details.

* **Course-level notification preferences removed.** Integrations that read
  ``CourseNotificationPreference`` records should migrate to account-level
  notification preferences and the V3 preferences API. See the `model
  deletion migration
  <https://github.com/openedx/edx-platform/blob/0a9cb22fc562507387d29db31cb26ee2a35f86c2/openedx/core/djangoapps/notifications/migrations/0010_delete_coursenotificationpreference.py#L12-L15>`_.

* **``is_core`` notification preference flag removed.** Notification
  preference configuration no longer uses the ``is_core`` flag or the
  ``core_web``, ``core_email``, and ``core_push`` fields. Clients that
  consume notification preference configuration data should use
  ``use_app_defaults`` and the plain channel fields exposed by the V3
  preferences API.

* **Notification preferences V2 configuration API removed.** The
  notification preferences V2 configuration API and its related manager
  classes have been removed. Integrations that called
  ``/api/notifications/v2/configurations/`` should use
  ``/api/notifications/v3/configurations/`` instead.

* **Removal of temporary SAML toggle.** The SAML feature toggle previously
  introduced as a temporary safeguard no longer exists. Any configuration
  setting this toggle should be removed. See
  `fix: removal of temporary saml toggle <https://github.com/openedx/edx-platform/pull/37651>`_.

* **Consolidation of several XBlock packages into xblocks-extra.** The
  following standalone XBlock packages have been consolidated into
  ``xblocks-extra``. The standalone repositories have already been marked
  deprecated:

  * ``audio-xblock``
  * ``feedback-xblock``
  * ``openedx-xblock-image-modal``
  * ``xblock-qualtrics-survey``
  * ``xblock-sql-grader``
  * ``xblock-submit-and-compare``

  Operators who have any of these packages installed should migrate to
  ``xblocks-extra`` and follow the migration guideline.

  Additionally, the following Open edX forked repositories have been archived
  and are no longer maintained. Operators should refer to their respective
  upstream repositories for continued support:

  * ``schoolyourself-xblock``
  * ``ConceptXBlock``

* **Deprecation of legacy built-in XBlock implementations.** Several previously
  built-in XBlocks have been extracted from ``edx-platform`` into the shared
  ``xblock-contrib`` repository, and the extracted implementations are used by
  default in Verawood. The legacy "built-in" block code is considered
  deprecated. Starting in Willow, the deprecated built-in implementations are
  planned to be removed from ``edx-platform``, leaving only the extracted
  variants in ``xblock-contrib``.

  The following blocks have been extracted and now live in ``xblock-contrib``:

  * HTML Block
  * Video Block
  * Problem Block
  * Word Cloud Block
  * Annotatable Block
  * LTI Block
  * Poll Block

  If you encounter problems with the extracted blocks, you can temporarily
  revert to the built-in implementations using the feature flags in
  ``openedx/envs/common.py``, following the pattern ``USE_EXTRACTED_*_BLOCK``
  (for example, ``USE_EXTRACTED_VIDEO_BLOCK``).

Aspects Analytics
*****************

Upgrading to `Aspects v4.0.0
<https://github.com/openedx/tutor-contrib-aspects/releases>`_ will give you the
latest Aspects functionality including Superset 6.0! See the upgrade
instructions here: :ref:`openedx-aspects:upgrade-aspects`.

This is a **BREAKING CHANGE** upgrade. Aspects will now use Python v3.12 which
was introduced in the Tutor Verawood release.

.. _Verawood operators:

Administrators & Operators
**************************

* **PostgreSQL is now supported as a backend (fresh installs only).** For more
  detail see the `Use PostgreSQL how-to
  <https://docs.openedx.org/en/latest/site_ops/how-tos/use_postgresql.html>`_.

* **Notification preference defaults can now be managed at the instance
  level.** Operators can override default preferences for existing
  notification applications and notification types without code changes.
  See `how to override default notification preferences
  <https://docs.openedx.org/en/latest/site_ops/how-tos/enable_notifications.html#how-to-override-default-notification-preferences>`_.

  * ``NOTIFICATION_APPS_OVERRIDE`` (default ``{}``): overrides default
    preferences for existing notification applications. Supported override
    keys are ``web``, ``email``, ``push``, ``non_editable``, and
    ``email_cadence``.
  * ``NOTIFICATION_TYPES_OVERRIDE`` (default ``{}``): overrides default
    preferences for existing notification types. Supported override keys
    are ``web``, ``email``, ``push``, ``non_editable``, and
    ``email_cadence``.

* **Immediate email notifications now use a configurable buffer window.**
  The first notification is sent immediately; additional
  immediate-cadence notifications created inside the window are combined
  into one buffered digest.

  * ``NOTIFICATION_IMMEDIATE_EMAIL_BUFFER_MINUTES`` (default ``15``): number
    of minutes to buffer additional immediate-cadence email notifications
    after the first immediate email is sent.

* **ORA reminder notifications are now available.** Learners who submit an
  Open Response Assessment but still need to complete required peer or self
  review steps can receive ``ora_reminder`` web and email notifications. See
  `Configure ORA Reminder Notifications
  <https://docs.openedx.org/en/latest/site_ops/how-tos/enable_notifications.html#configure-ora-reminder-notifications>`_.

  * ``ENABLE_ORA_REMINDERS`` (default ``True``): enables scheduled ORA
    reminder notifications for learners who need to complete peer or self
    reviews.
  * ``ORA_REMINDER_MAX_COUNT`` (default ``3``): maximum number of reminders
    sent per learner per ORA submission.
  * ``ORA_REMINDER_INTERVAL_HOURS`` (default ``48``): hours between
    consecutive ORA reminder notifications.
  * ``ORA_REMINDER_INITIAL_DELAY_HOURS`` (default ``0``): hours after
    submission before the first ORA reminder is sent.
  * ``ORA_REMINDER_SWEEP_INTERVAL_SECONDS`` (default ``1800``): how often
    the ORA reminder sweeper Celery task reschedules itself.
  * ``ORA_REMINDER_SWEEP_BATCH_SIZE`` (default ``1000``): maximum number of
    ORA reminder rows processed per sweep cycle.
  * ``ORA_REMINDER_CHECK_AGAIN_HOURS`` (default ``12``): hours to wait
    before checking again when no peer submissions are available.

* **Built-in pdf XBlock.** The pdf XBlock is now built into the platform core
  and installed by default. If you previously installed a third-party pdf
  implementation such as open-craft's ``xblock-pdf``, then the built-in
  implementation will likely work as a drop-in replacement, so you can
  uninstall the third-party implementation.

  If you'd rather continue using a third-party pdf implementation, then
  follow the steps to replace a preinstalled XBlock with a custom
  implementation. In either case, the third-party implementation must be
  removed from the ``xblock.v1`` entrypoint, otherwise you will see an
  ``AmbiguousPluginError``. Additionally, you will want to enable the
  ``legacy_studio.pdf_editor`` toggle to allow the third-party pdf
  implementation to render its editor.

* **New Instructor Dashboard MFE is the default experience.** The new
  instructor dashboard MFE will be the default experience in Verawood. The
  ``instructor.legacy_instructor_dashboard`` waffle flag will disable the
  redirection that makes the new frontend app the default experience and
  revert to the legacy instructor dashboard.

  If you were using the
  ``org.openedx.learning.instructor.dashboard.render.started.v1`` filter to
  modify the instructor dashboard tabs, you can achieve a similar outcome by
  using ``org.openedx.learning.instructor.dashboard.tabs.generated.v1``, which
  will give you access to the API endpoint currently consumed to render the
  tabs on the frontend app. You'll also need to add a widget to the proper
  slot to render the content. See the instructor dashboard MFE README for
  more details.

Frontend-base
*************

Verawood is the first release that supports the new `frontend-base
architecture <https://github.com/openedx/frontend-base/>`_. It enables
frontend apps to be loaded as direct plugins within a unified "shell,"
rather than as separate, independently deployed MFEs. There are several
advantages to this paradigm, including improved learner UX, reduced page
load time, faster builds, and a broader-scoped plugin API. For more
information on what motivated this change, see `OEP-65
<https://open-edx-proposals.readthedocs.io/en/latest/architectural-decisions/oep-0065-arch-frontend-composability.html>`_.

In practice, frontend apps are NPM packages that plug into a single
frontend-base site. Verawood ships with four of these:

* ``@openedx/frontend-app-authn``: replaces the Authn MFE; *disabled by
  default*
* ``@openedx/frontend-app-learner-dashboard``: replaces the Learner
  Dashboard MFE; *disabled by default*
* ``@openedx/frontend-app-instructor-dashboard``: replaces the legacy
  instructor dashboard; *enabled by default*
* ``@openedx/frontend-app-notifications``: ports
  ``@edx/frontend-plugin-notifications`` to the frontend-base ecosystem;
  *enabled by default*

The tutor-mfe implementation allows each of these to be easily enabled or
disabled without requiring a rebuild of the Tutor image, as documented in
the `tutor-mfe README
<https://github.com/overhangio/tutor-mfe/tree/main#frontend-base-site>`_.
When an app that replaces an existing MFE is enabled (such as Authn or
Learner Dashboard), its MFE counterpart is automatically disabled.

It is expected that by Xylon (the Open edX release following Willow), all
Open edX MFEs will have been converted to frontend-base apps. Operators are
therefore encouraged to enable the Authn and Learner Dashboard apps to test
pre-existing customizations on their instances. It is likely that any
branding, plugins, and forks of MFEs will need to be ported accordingly.
Documentation on how to do so is provided at:

* `frontend-base theming docs
  <https://github.com/openedx/frontend-base/blob/main/docs/how_tos/theming.md>`_
* `docs.openedx.org PR #1459
  <https://github.com/openedx/docs.openedx.org/pull/1459>`_
* `Migrate a frontend app how-to
  <https://github.com/brian-smith-tcril/frontend-base/blob/main/docs/how_tos/migrate-frontend-app.md>`_

As a migration aid for unconverted legacy plugins, a `frontend-base-compat
<https://github.com/openedx/frontend-base-compat>`_ shim lets legacy
``env.config.jsx`` configuration run on top of frontend-base sites. It is
also implemented by tutor-mfe: refer to `the corresponding section
<https://github.com/overhangio/tutor-mfe/tree/main#compat-shim-for-fpf-built-plugins>`_
of its documentation for information on how to use it.

Finally, note that tutor-mfe's frontend-base implementation automatically
makes use of the new ``/api/frontend_site_config/v1/`` runtime configuration
endpoint, which converts existing ``MFE_CONFIG`` and ``MFE_CONFIG_OVERRIDES``
to frontend-base's ``SiteConfig`` structure. You can find out more `here
<https://github.com/overhangio/tutor-mfe/tree/main#backward-compatibility-with-mfe_config>`_.

What if I don't use Tutor?
==========================

If you deploy Open edX using something other than Tutor, start by looking at
`frontend-template-site <https://github.com/openedx/frontend-template-site>`_.
This is the canonical representation of how a frontend-base site should be
configured. Operators are meant to fork and modify it as required for their
own instances. Everything in it is considered user-configuration, including
``index.html``.

Loading External Scripts
*************************

It is now possible to configure either MFEs or frontend apps to load
arbitrary external scripts, such as ones used to configure hosted analytics
services. Where before only Google Analytics was supported, now operators
are free to load whatever external service they need. See `the
corresponding tutor-mfe documentation
<https://github.com/overhangio/tutor-mfe/tree/main#configuring-external-scripts>`_.

For an example implementation, refer to a sample Tutor plugin that loads
Google Analytics dynamically on both MFEs and frontend apps:
`tutor-contrib-google-analytics
<https://github.com/openedx/openedx-tutor-plugins/tree/main/plugins/tutor-contrib-google-analytics>`_.

Settings and Toggles
********************

Developer Experience
********************

Known Issues
************

See the `Build Test Release project board <https://github.com/orgs/openedx/projects/28/views/19>`_ for known open issues.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
