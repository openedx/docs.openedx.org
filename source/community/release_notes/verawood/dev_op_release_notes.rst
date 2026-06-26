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
  upgrade panel from the Learning MFE core has been replaced with a pluggable
  widget registry system.

  * Instances using the upgrade panel: Add ``SIDEBAR_WIDGETS:
    [upgradeWidgetConfig]`` to ``env.config.jsx``.
  * Plugin slot consumers: Replace ``NotificationTraySlot`` /
    ``NotificationsDiscussionsSidebarSlot`` with ``RightSidebarSlot``. Replace
    ``NotificationsDiscussionsTriggerSlot`` with ``RightSidebarTriggerSlot``.
  * ``localStorage``: Old ``notificationStatus.{courseId}`` keys are not
    migrated; the new ``upgradeWidget.{courseId}`` key starts fresh.

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
  The management command still exists but is now a no-op with a deprecation
  warning. See the documentation on how to change default digest settings.

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

Settings and Toggles
********************

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
