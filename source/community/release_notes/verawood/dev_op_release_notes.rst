.. _Verawood Dev Notes:

Open edX Verawood Developer & Operator Release Notes
#####################################################

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

Migrations to be aware of
*************************

A few migrations in this release touch existing data at scale, run
automatically without an explicit opt-in, or can fail depending on your
instance's data history. Review these before upgrading.

* **Course ID case-insensitive uniqueness constraint.** Due to a bug that was
  present in the last several releases, it was possible for users to create
  multiple courses with similar course IDs that differed only in
  capitalization. Such courses would only appear as a single course in most
  parts of the system, and may not work properly at all. That bug has been
  fixed, and a new database constraint will prevent that from happening going
  forward.

  However, if you have any of these "case duplicate" courses, the
  ``split_modulestore_django`` migration ``0004_courseid_unique_ci`` will fail
  with an ``IntegrityError``. If you encounter this, follow the instructions to
  delete the invalid course record(s), and then you should be able to apply the
  migration and continue. See
  `fix!: split modulestore's has_course(ignore_case=True) was not working
  <https://github.com/openedx/edx-platform/pull/38044>`_.

* **MariaDB UUID column conversion (edx-enterprise).** If you run MariaDB,
  upgrading ``edx-enterprise`` runs a migration that converts roughly 19 UUID
  columns from ``char(32)`` to MariaDB's native ``uuid`` type, with no flag to
  skip it. This includes enrollment and group-membership tables
  (``enterprise_licensedenterprisecourseenrollment``,
  ``enterprise_enterprisecourseentitlement``,
  ``enterprise_enterprisegroupmembership``) that can be large on instances
  with many enterprise customers. Changing a column's type this way forces
  MariaDB to rewrite the whole table (``ALGORITHM=COPY``), locking it for the
  duration. This migration is a no-op on PostgreSQL. See
  `fix: Convert UUIDField columns to uuid type for MariaDB
  <https://github.com/openedx/edx-enterprise/pull/2475>`_.

* **AuthZ course-authoring role migration (openedx-authz).** This is not a
  schema migration, it's a signal-triggered data migration. Enabling the
  ``authz.enable_course_authoring`` waffle flag for an organization triggers,
  synchronously inside that save, a full migration of every
  ``CourseAccessRole`` row for that org into the new Casbin-based
  authorization model, wrapped in a single transaction. Cost scales with how
  many courses and role assignments the org has, and there's no built-in
  batching. To control how much gets migrated at once, keep
  ``ENABLE_AUTOMATIC_AUTHZ_COURSE_AUTHORING_MIGRATION`` set to ``False`` (its
  default) and roll out with the ``authz_migrate_course_authoring``
  management command instead, scoped with ``--course-id-list`` or
  ``--org-id``. See
  `feat: course authoring automatic migration
  <https://github.com/openedx/openedx-authz/pull/259>`_.

* **Catalog course/run backfill (course_overviews).** A migration populates
  new ``CatalogCourse``/``CourseRun`` models by iterating every
  ``CourseOverview`` row, without batching. It can fail outright with a
  ``ValueError`` if a course's organization short code doesn't match the
  Organizations table, which is plausible on instances with years of
  accumulated data drift (case mismatches, orgs created outside the normal
  flow). If it fails, the error names the offending course and organization;
  create the missing Organization record (Django admin) or set
  ``active=False`` on it, then re-run the migration. See
  `feat: update openedx-core: new catalog models + backfill migration
  <https://github.com/openedx/edx-platform/pull/38023>`_.

* **Enterprise academies auto-enabled for existing customers (edx-enterprise).** Any
  enterprise customer that already has
  ``enable_integrated_customer_learner_portal_search=True`` gets
  ``enable_academies=True`` automatically. This is opt-out, not opt-in, and
  the reverse migration is an explicit no-op: there's no way to determine or
  restore the prior state after the fact. See
  `feat: enable academies by default for all enterprise customers with search
  <https://github.com/openedx/edx-enterprise/pull/2594>`_.

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
  <https://github.com/openedx/edx-platform/pull/38185>`_ and :ref:`Configure
  Notification Email Delivery <Configure Notification Email Delivery>`.

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

* **SchoolYourself and Concept XBlocks Deprecated**: The following Open edX
  forked repositories have been archived and are no longer maintained. Operators
  should refer to their respective upstream repositories for continued support:

  * ``schoolyourself-xblock``
  * ``ConceptXBlock``

* **Deprecation of legacy built-in XBlock implementations.** Several previously
  built-in XBlocks have been extracted from ``edx-platform`` into the shared
  `xblocks-core <https://github.com/openedx/xblocks-core>`_ repository, and the
  extracted implementations are used by default in Verawood. The legacy
  "built-in" block code is considered deprecated. Starting in Willow, the
  deprecated built-in implementations are planned to be removed from
  ``edx-platform``, leaving only the extracted variants in ``xblocks-core``.

  The following blocks have been extracted and now live in ``xblocks-core``:

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

* **Consolidation of several XBlock packages into xblocks-extra.** The following
  standalone XBlock packages have been consolidated into `xblocks-extra
  <https://github.com/openedx/xblocks-extra>`_. The following standalone
  repositories have been marked deprecated:

  * ``audio-xblock``
  * ``feedback-xblock``
  * ``openedx-xblock-image-modal``
  * ``xblock-qualtrics-survey``
  * ``xblock-sql-grader``
  * ``xblock-submit-and-compare``

  Operators who have any of these packages installed should migrate to
  ``xblocks-extra`` and follow the migration guidelines.

* **Legacy Libraries Deprecation**: :ref:`Legacy Libraries <Legacy Content
  Libraries Overview>` are now deprecated and must be :ref:`migrated to Content
  Libraries <Migrating Legacy Libraries>` this release.

  Operators can see if any legacy libraries exist on their instance by visiting
  the "Legacy Libraries" tab on the Studio homepage, and clicking the
  :guilabel:`Review Legacy Libraries` button. Operators or course teams may
  perform the migration using the migration UI.

  .. figure:: /_images/release_notes/verawood/migrate_legacy_libraries.png
    :alt: The Studio homepage's Legacy Libraries tab has a banner indicating that legacy libraries must be migrated. The "Review Legacy Libraries" button is on the right side of this banner.
    :align: center

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
  detail see the :ref:`Use PostgreSQL how-to <use postgresql>`.

* **Notification preference defaults can now be managed at the instance
  level.** Operators can override default preferences for existing
  notification applications and notification types without code changes.
  See :ref:`Configure Default Notification Preferences`.

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
  :ref:`Configure ORA Reminder Notifications <ora-reminder-notifications>`.

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

  If you'd rather continue using a third-party pdf implementation, then :ref:`follow
  the steps to replace a preinstalled XBlock with a custom implementation
  <xblock:Replace a Preinstalled XBlock With a Custom Implementation>`.
  In either case, the third-party implementation must be removed from the
  ``xblock.v1`` entrypoint, otherwise you will see an ``AmbiguousPluginError``.
  Additionally, you will want to enable the ``legacy_studio.pdf_editor`` toggle
  to allow the third-party pdf implementation to render its editor.

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

* **Catalog MFE is the default experience.** Introduced in Ulmo, the new
  :ref:`Catalog MFE <Ulmo catalog>` is now the default experience. Verawood will
  be the last release that supports the legacy experience; the `legacy
  experience will be removed in Willow
  <https://github.com/openedx/openedx-platform/issues/36785>`_.

.. _Enabling RBAC in Verawood:

* **RBAC AuthZ for Course Authoring (opt-in).** Verawood introduces a new,
  opt-in, RBAC-based authorization system for course authoring in Studio,
  powered by `openedx-authz <https://github.com/openedx/openedx-authz>`_.
  This replaces the legacy ``CourseAccessRole``-based permission model with a
  more granular, role-based system. See `ADR: AuthZ for Course Authoring
  Implementation Plan
  <https://github.com/openedx/openedx-authz/blob/main/docs/decisions/0009-authz-for-course-authoring.rst>`_.

  This flag will be turned on by default in the next release, Willow, and
  the legacy permission system will be removed in Xylon (June 2027). To set up an
  individual course, a specific organization, or your whole site to use the
  new system, you need to both enable the appropriate feature flag(s) and
  run migrations.

  * **Enabling the feature flag.** The feature is controlled by the waffle
    flag ``authz.enable_course_authoring``, which can be enabled at three
    levels of granularity (course, organization, global). When disabled (the
    default), the legacy permission system remains in effect and no behavior
    changes.

    * Course-level: add a "Waffle flag course override" at
      ``/admin/waffle_utils/waffleflagcourseoverridemodel/`` for
      ``authz.enable_course_authoring``, with the course key, "Force
      On"/"Force Off", marked "Enabled".
    * Org-level: add a "Waffle flag org override" at
      ``/admin/waffle_utils/waffleflagorgoverridemodel/`` the same way,
      using the org short name.
    * Global: add a Flag named ``authz.enable_course_authoring`` at
      ``/admin/waffle/flag/`` with "Everyone" set to "Yes".
    * Course and org overrides work as overrides over the global flag, not
      independent switches. If the override is "Disabled", the effective
      state follows the global flag. If the global flag is off, an override
      "Enabled" + "Force On" turns the flag on for that scope; if the global
      flag is on, "Enabled" + "Force Off" turns it off for that scope.
    * Global enablement affects all courses on the instance. If automatic
      migrations are not enabled (see below), you must run the migration
      management commands manually before or after toggling the global flag.

    See `ADR: Feature Flag Implementation Details
    <https://github.com/openedx/openedx-authz/blob/main/docs/decisions/0010-course-authoring-flag.rst>`_.

  * **Migrating permission data.** Existing legacy role assignments
    (``CourseAccessRole``) must be migrated to ``openedx-authz`` when
    enabling the new system. Two management commands are provided, scoped by
    either ``--course-id-list`` or ``--org-id`` (mutually exclusive; one is
    required):

    * Forward migration (legacy to openedx-authz): ``./manage.py cms
      authz_migrate_course_authoring --delete --course-id-list <course_key1>
      [course_key2 ...]`` or ``--org-id <org_name>``
    * Rollback migration (openedx-authz to legacy): ``./manage.py cms
      authz_rollback_course_authoring --delete --course-id-list
      <course_key1> [course_key2 ...]`` or ``--org-id <org_name>``
    * Both accept ``--delete``, which removes the successfully migrated role
      assignments from the source system after migration (prompts for
      confirmation). Without ``--delete``, the migration copies but does not
      move, and source records are preserved.
    * Using ``--delete`` is strongly recommended. The system expects
      permission data to exist in only one system at a time for a given
      resource. If assignments remain in both systems they can diverge over
      time: for example, a course may keep appearing in a user's Studio
      course list after their permissions were removed in one system,
      because the assignment still exists in the other. Running without
      ``--delete`` should only be used for development/testing before the
      definitive migration.
    * Both operations run within a database transaction. During rollback,
      roles that exist only in the new system (no legacy equivalent) remain
      in ``openedx-authz`` and are not migrated back; warnings are logged.

    See `ADR: Migration Process Details
    <https://github.com/openedx/openedx-authz/blob/main/docs/decisions/0011-course-authoring-migration-process.rst>`_.

  * **Automatic migrations (opt-in).** Set
    ``ENABLE_AUTOMATIC_AUTHZ_COURSE_AUTHORING_MIGRATION = True`` (default
    ``False``) to have course/org-level flag toggles in Django Admin
    automatically trigger the corresponding data migration (forward on
    enable, rollback on disable). Migration status and errors are recorded
    in the ``AuthzCourseAuthoringMigrationRun`` model, viewable in Django
    Admin. A runtime constraint prevents concurrent migrations on the same
    scope.

    * Automatic migration only applies to course-level and org-level flag
      changes. Global (instance-wide) flag changes do not trigger it, due to
      performance risk on large instances, and must be migrated manually
      with the management commands above.
    * This setting is disabled by default. Only enable it if you understand
      that the migration then runs synchronously within the Django Admin
      request.

    See `ADR: Automatic Migration Details
    <https://github.com/openedx/openedx-authz/blob/main/docs/decisions/0013-course-authoring-automatic-migration.rst>`_.

  * **Audit trail.** Role assignment and removal operations in
    ``openedx-authz`` are now recorded in a ``RoleAssignmentAudit`` table
    (operation type, affected user, role, scope, actor), registered in
    Django Admin for inspection. An ``OpenedxPublicSignal`` is also emitted
    on every role lifecycle event for downstream consumers. See `ADR:
    Auditability
    <https://github.com/openedx/openedx-authz/blob/main/docs/decisions/0012-auditability.rst>`_.

  * **Known caveat: Admin Console and courses without the flag enabled.**
    The Admin Console displays all courses in scope selectors when assigning
    roles, regardless of whether ``authz.enable_course_authoring`` is
    enabled for those courses. Roles can be assigned to any course through
    the admin, but those assignments won't take effect unless the flag is
    enabled for that course, its org, or globally. This can look like roles
    were assigned but permissions aren't enforced. This limitation does not
    affect content libraries, which don't use the legacy permission system.

    As of `frontend-app-admin-console PR #176
    <https://github.com/openedx/frontend-app-admin-console/pull/176>`_, the
    Admin Console's filters and role assignment wizard all read flag state directly
    from ``GET /api/authz/v1/waffle-flag-states/`` and hide course content the flag
    doesn't cover yet, independently of whether the underlying Casbin
    migration has run. The Team Members table and Audit User view display all
    course assignments; however, course or organization assignments that are
    not enabled via the ``authz.enable_course_authoring`` flag can only be viewed,
    but not deleted. Observed behavior:

    .. list-table::
       :header-rows: 1

       * - Scenario
         - Expected behaviour
       * - Flag OFF globally, no overrides
         - Role filter hides course groups; scope filter hides all courses;
           org filter hides all orgs for course-only users; wizard has no
           course roles
       * - Flag OFF globally, org A forced ON
         - Courses in org A appear in scope/org filters and wizard; all
           other orgs/courses hidden
       * - Flag ON globally, course X forced OFF
         - Course X hidden in scope filter and wizard scope list; all other
           courses visible
       * - Flag ON globally, org B forced OFF
         - Org B and its courses hidden for course-only users
       * - User has only library roles
         - Libraries appear in all filters regardless of flag state
       * - User has both library and course roles, flag OFF
         - Library content visible everywhere; course content hidden
       * - ``waffle-flag-states`` endpoint unreachable
         - Error toast appears with retry button; all course content hidden
       * - Loading state (slow network)
         - Course content hidden until flag state resolves; library content
           unaffected

    Flag-state resolution here is intentionally separate from permission
    validation, since Casbin state can lag behind the flag when automatic
    migration is disabled or the global flag changes.

Frontend-base
*************

Verawood is the first release that supports the new `frontend-base
architecture <https://github.com/openedx/frontend-base/>`_. It enables
frontend apps to be loaded as direct plugins within a unified "shell,"
rather than as separate, independently deployed MFEs. There are several
advantages to this paradigm, including improved learner UX, reduced page
load time, faster builds, and a broader-scoped plugin API. For more
information on what motivated this change, see :ref:`openedx-proposals:OEP-65 Frontend Composability`.

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

It is expected that by Xylon (June 2027), all
Open edX MFEs will have been converted to frontend-base apps. Operators are
therefore encouraged to enable the Authn and Learner Dashboard apps to test
pre-existing customizations on their instances. It is likely that any
branding, plugins, and forks of MFEs will need to be ported accordingly.
Documentation on how to do so is provided at:

* `frontend-base theming docs
  <https://github.com/openedx/frontend-base/blob/main/docs/how_tos/theming.md>`_
* :ref:`Port a Frontend Plugin to frontend-base`
* `Migrate a frontend app how-to
  <https://github.com/openedx/frontend-base/blob/main/docs/how_tos/migrate-frontend-app.md>`_

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

If you deploy your Open edX instance using something other than Tutor, start by looking at
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

Known Issues
************

See the `Build Test Release project board <https://github.com/orgs/openedx/projects/28/views/19>`_ for known open issues.

**Maintenance chart**

+--------------+-------------------------------+----------------+------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                      |
+--------------+-------------------------------+----------------+------------------------------------+
|2026-07-30    | BTR WG                        | Verawood       | Pass                               |
+--------------+-------------------------------+----------------+------------------------------------+
