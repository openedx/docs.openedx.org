.. _Ulmo Dev Notes:

Open edX Ulmo Developer & Operator Release Notes
################################################

These are the developer & operator release notes for the Ulmo release, the 21st
community release of the Open edX Platform, spanning changes from April 25,
2025 to October 30, 2025. You can also review details about :ref:`Open edX Release Notes` or
learn more about the `Open edX Platform`_.

To view the end-user facing docs, see the :ref:`Ulmo Product Notes`.

.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Improvements
*************

**Decreased Docker build time for operators**

The time it takes to install dependencies and build static assets for
edx-platform has decreased from Teak due to pruning of legacy code (e.g. legacy
Studio pages), removal of some unnecessary dependencies (e.g.
edx-proctoring-proctortrack), and upgrades to build tools (e.g. webpack).

Breaking Changes
****************

* The ``VERIFY_STUDENT["STORAGE_CLASS"]`` configuration used for the
  ``_storage`` property in the ``SoftwareSecurePhotoVerification`` class is
  being deprecated in favor of the modern ``STORAGES`` dictionary introduced in
  Django 4.2.
  
  The updated implementation prioritizes the ``STORAGES["verify_student"]``
  backend. If this is not defined, it falls back to the legacy
  ``VERIFY_STUDENT["STORAGE_CLASS"]`` configuration for backward compatibility.
  
  **Breaking change**: Previously, the legacy setting defaulted to
  ``storages.backends.s3boto3.S3Boto3Storage``. Now, it defaults to the global
  default storage instead. See `feat: deprecate get_storage_class in core/storage.py <https://github.com/openedx/edx-platform/pull/36910>`_.

* There is a change to the session_inactivity_timeout middleware. A new setting,
  ``SESSION_ACTIVITY_SAVE_DELAY_SECONDS``, has been added with a default value
  of 15 minutes.
  
  This new setting modifies how the system handles the
  ``SessionInactivityTimeout``. It prevents the session ID from changing with
  every request, which improves efficiency, while still correctly enforcing the
  session timeout. While this change resolves an existing issue, it's considered
  a "breaking change" to highlight the fact that the default behavior of the
  application's session middleware has been altered. The new default is a
  reasonable starting point, but it's important for to be aware of the change.
  
  For more context `fix!: session ID stability while maintaining inactivity timeout <https://github.com/openedx/edx-platform/pull/36896>`_.

Deprecations & Removals
***********************

* ``newrelic`` as a baseline Python dependency in Django IDAs

  * **Audience**: Deployers who use New Relic for Python-based observability, or
    who have custom IDA code directly referencing the newrelic Python package.
  * **Action**: If you use New Relic from Python, ensure that you install the
    newrelic Python package, as it will no longer be installed by default.
  * Nothing else is changing with respect to New Relic support at this time;
    edx-django-utils continues to support New Relic telemetry (and even defaults
    to using it, if the package is present). For more context: `[DEPR]: newrelic
    as baseline dependency in Django IDAs <https://github.com/openedx/public-engineering/issues/360>`_

* The variable ``CSRF_TRUSTED_ORIGINS_WITH_SCHEMES``, added during the Django
  3.2 to 4.2 upgrade, has been completely removed. Operators should replace any
  use of this setting with ``CSRF_TRUSTED_ORIGINS``.

* The ``cs_comments_service`` has been archived, and all calls to it have been
  removed from ``edx-platform``. The MongoDB backend for ``forums`` is still
  supported via the new forums app through the Ulmo release, so no forums data
  migration is *required* for this release, but it is *highly advised*. We will
  not support serving forums data from MongoDB in Verawood. For more operational
  and migration details, please see the `Administration section of the forum repo
  README <https://github.com/openedx/forum?tab=readme-ov-file#administration>`_.

* The ``PROFILE_IMAGE_BACKEND`` setting will be replaced with the ``profile_image``
  storage class defined in the ``STORAGES`` setting.  For Ulmo it will still fall
  back to the values set in the ``PROFILE_IMAGE_BACKEND`` setting but it is
  recommended that you migrate to the profile_image setting in ``STORAGES`` now that
  it available. The ``PROFILE_IMAGE_BACKEND`` setting could be dropped as early as
  Verawood. See `feat!: upgrade code and fix get_storage_class <https://github.com/openedx/edx-platform/pull/36628>`_.

* The ``COURSE_METADATA_EXPORT_STORAGE`` setting will be replaced with the
  ``course_metadata_export`` storage class defined in the ``STORAGES`` setting.  For
  Ulmo it will still fall back to the values set in the
  ``COURSE_METADATA_EXPORT_STORAGE`` setting but it is recommended that you migrate
  to the course_metadata_export setting in ``STORAGES`` now that it available. The
  ``COURSE_METADATA_EXPORT_STORAGE`` setting could be dropped as early as Verawood.
  See `feat: removing get_storage_class from COURSE_METADATA_EXPORT_STORAGE
  <https://github.com/openedx/edx-platform/pull/36761>`_.

* The ``USER_TASKS_ARTIFACT_STORAGE`` setting is being deprecated in favor of the
  modern ``STORAGES`` dictionary introduced in Django 4.2.
  
  This update changes the logic to first look for a storage backend defined under
  ``STORAGES["user_task_artifacts"]``. If not found, it will fall back to the
  previously supported ``USER_TASKS_ARTIFACT_STORAGE`` setting via the optional ``import_path`` parameter.

  It is recommended that you migrate to using the user_task_artifacts storage in
  the ``STORAGES`` dictionary. The legacy ``USER_TASKS_ARTIFACT_STORAGE`` setting may be
  removed as early as the Verawood release. See `Fixing get_storage functionality as per new django52 <https://github.com/openedx/django-user-tasks/pull/421>`_.

* The ``SGA_STORAGE_SETTINGS`` configuration is being deprecated in favor of the
  modern ``STORAGES`` dictionary introduced in Django 4.2. This update
  prioritizes the ``STORAGES["sga_storage"]`` backend. If not defined, it falls
  back to the legacy ``SGA_STORAGE_SETTINGS`` for backward compatibility. It is
  recommended to migrate to the ``STORAGES`` -based configuration.

  Support for ``SGA_STORAGE_SETTINGS`` may be removed as early as the Verawood release.
  See `feat!: Adding django52 support. <https://github.com/mitodl/edx-sga/pull/368>`_

* In Credentials, the ``DEFAULT_FILE_STORAGE`` and ``STATICFILES_STORAGE``
  settings are being deprecated in favor of the modern ``STORAGES`` dictionary
  introduced in Django 4.2.

* The ``SEND_CATALOG_INFO`` setting has been removed.  The behavior is now as if
  the settings is permanently set to ``True``. See `feat: Remove the
  SEND_CATALOG_INFO_SIGNAL toggle
  <https://github.com/openedx/edx-platform/pull/37269>`_.

Aspects Analytics
*****************************

Upgrading to `Aspects v2.5.1
<https://github.com/openedx/tutor-contrib-aspects/releases/tag/v2.5.1>`_ will
give you the latest Aspects functionality with Ulmo. See the upgrade
instructions here: :ref:`openedx-aspects:upgrade-aspects`.

Then run this to update materialized views that have new/removed columns::

   tutor local do dbt --only_changed False -c 'run --full-refresh --select dim_learner_last_response dim_problem_results problem_events dim_subsection_problem_results'

.. _Ulmo operators:

Administrators & Operators
**************************

* A new Catalog MFE is optionally available in Ulmo.1. See the :ref:`Catalog
  release notes <Ulmo catalog>` for more information about the catalog, and the
  `Catalog README
  <https://github.com/openedx/frontend-app-catalog?tab=readme-ov-file#installing>`_
  for information about how to enable this on your instance.

* For Libraries, access control is now represented as explicit, library scoped
  roles that are evaluated through the `AuthZ
  <https://github.com/openedx/openedx-authz>`_ service. These roles are mapped
  to permission sets that control what users can do in a given library,
  centralizing how roles and permissions are defined, stored and enforced, while
  keeping behavior aligned with the previous release. See :ref:`Ulmo Roles and
  Permissions` for more information.

* A ``getExternalLinkUrl`` function is provided in ``config.js`` which can be
  used to override default external links in MFEs. To make use of this function,
  provide an object that maps default links to custom links. This object should
  be added to the config object defined in the ``env.config.[js,jsx,ts,tsx]``,
  and must be named ``externalLinkUrlOverrides``. See the `frontend-platform
  README <https://github.com/openedx/frontend-platform?tab=readme-ov-file#overriding-default-external-links>`_.

* SAML Configuration Version Alignment Update
  
  A fix has been implemented to ensure that all SAML provider configurations
  always reference the latest version of the SAML configuration. Previously,
  some providers continued pointing to outdated versions after updates, causing
  inconsistencies. With this change, provider configurations will automatically
  align with the newest SAML configuration version, eliminating the need for
  manual updates and ensuring consistent authentication behavior.
  
  A new management command is included to verify alignment::
   
   ./manage.py lms saml --run-check

  Temporary feature toggle added: ``ENABLE_SAML_CONFIG_SIGNAL_HANDLERS`` must be
  enabled to activate this behavior.

  See: `SAML PR1 <https://github.com/openedx/edx-platform/pull/36954>`_, `SAML
  PR2 <https://github.com/openedx/edx-platform/pull/37294>`_, `SAML PR3
  <https://github.com/openedx/edx-platform/pull/37377>`_.


.. _Configuring Forums Spam:

Configuring Forum Moderation & Spam Prevention Features
=======================================================

#. Preventing harmful content from being viewed: A configurable feature was
   added that replaces content containing certain strings with a custom message.

   **Configuration**: 
   
   #. Add a list of URLs, keywords, or regex patterns to the Django setting ``DISCUSSION_SPAM_URLS``. Regular expressions are supported.

      Each pattern matching part of a forum post will be removed or replaced, for example::

         DISCUSSION_SPAM_URLS = [
           r"https?://chat\.whatsapp\.com/[A-Za-z0-9]+",
           r"https?://bit\.ly/[A-Za-z0-9]+",
         ]

   #. Define the replacement text in the Django setting
      ``CONTENT_FOR_SPAM_POSTS``. If this value is set, the entire content will
      be replaced by this value; if this value is left blank, only the matched
      portion (URL or text) will be removed, leaving the rest of the post
      unchanged. For example, if the value was set like so::

         CONTENT_FOR_SPAM_POSTS = "[removed: suspected spam link]"

      Any text that was a match for a regex in ``DISCUSSION_SPAM_URLS`` would be replaced with the text ``[removed: suspected spam link]``.

#. reCAPTCHA was added to the forum content creation API to prevent automated
   posting. It does not apply to users who have a course or forum role, or whose
   accounts are more than one month old.

   **Configuration**: To enable reCAPTCHA v3, configure the following in django LMS settings:

   #. ``RECAPTCHA_PROJECT_ID``

   #. ``RECAPTCHA_PRIVATE_KEY``

   #. Set ``RECAPTCHA_SITE_KEYS`` with the proper keys for web, ios, and android::

         RECAPTCHA_SITE_KEYS = {
            'web': '',
            'ios': '',
            'android': '',
         }

   #. Then, enable the waffle flag flag ``discussion.enable_captcha``. 

#. A rate limit was added to forums content creation, to limit the number of
   posts a single author can add within a set period of time.

   **Configuration**:
   
   #. Configure rate limit using django setting ``DISCUSSION_RATELIMIT`` (default = '100/m').
   #. Configure the age of learner account beyond which rate limit is not applied in django setting ``SKIP_RATE_LIMIT_ON_ACCOUNT_AFTER_DAYS`` (default = 0)
   #. Enable waffle flag ``discussions.enable_rate_limit``.

#. Given almost all spam accounts use unverified or random email addresses, a
   feature was built to limit forums posts to only those with verified accounts.

   Turning this on runs the risk of reducing engagement by adding friction for
   genuine learners, and it has been seen that spammers can work around this
   limitation.

   **Configuration**: Enable the ``discussions.only_verified_users_can_post``
   waffle flag on a specific course or for the whole site.

Added Settings
*********************

* +LEARNING_MICROFRONTEND_URL: `openedx/envs/common.py (line 1532) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1532>`_
   * Default value = None
   * Description: Base URL of the micro-frontend-based courseware page.

* +LOGIN_REDIRECT_WHITELIST: `openedx/envs/common.py (line 1204) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1204>`_
   * Default value = "empty list ([])"
   * Description: While logout, if logout request has a redirect-url as query strings, [output truncated, see link for full description]

* +MAX_FAILED_LOGIN_ATTEMPTS_ALLOWED: `openedx/envs/common.py (line 1898) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1898>`_
   * Default value = 6
   * Description: Specifies the maximum failed login attempts allowed to users. Once the user reaches this [output truncated, see link for full description]

* +MAX_FAILED_LOGIN_ATTEMPTS_LOCKOUT_PERIOD_SECS: `openedx/envs/common.py (line 1907) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1907>`_
   * Default value = "30 * 60"
   * Description: Specifies the lockout period in seconds for consecutive failed login attempts. Once the user [output truncated, see link for full description]

* +PARENTAL_CONSENT_AGE_LIMIT: `openedx/envs/common.py (line 1336) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1336>`_
   * Default value = 13
   * Description: The age at which a learner no longer requires parental consent, [output truncated, see link for full description]

* +PLATFORM_NAME: `openedx/envs/common.py (line 619) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L619>`_
   * Default value = "Your Platform Name Here"
   * Description: The display name of the platform to be used in [output truncated, see link for full description]

* +PREPEND_LOCALE_PATHS: `openedx/envs/common.py (line 2327) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L2327>`_
   * Default value = "[]"
   * Description: A list of the paths to locale directories to load first e.g. [output truncated, see link for full description]

* +REGISTRATION_EMAIL_PATTERNS_ALLOWED: `openedx/envs/common.py (line 1364) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1364>`_
   * Default value = None
   * Description: Optional setting to restrict registration / account creation [output truncated, see link for full description]

* +REGISTRATION_RATELIMIT: `openedx/envs/common.py (line 502) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L502>`_
   * Default value = "60/7d"
   * Description: New users are registered on edx via RegistrationView. [output truncated, see link for full description]

* +REGISTRATION_VALIDATION_RATELIMIT: `openedx/envs/common.py (line 493) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L493>`_
   * Default value = "30/7d"
   * Description: Whenever a user tries to register on edx, the data entered during registration [output truncated, see link for full description]

* +RETIRED_EMAIL_DOMAIN: `openedx/envs/common.py (line 2101) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L2101>`_
   * Default value = "retired.invalid"
   * Description: Set the domain part of hashed emails for retired users. Used by the derived [output truncated, see link for full description]

* +RETIRED_EMAIL_FMT: `openedx/envs/common.py (line 2114) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L2114>`_
   * Default value = "retired__user_{}@retired.invalid"
   * Description: Set the format a retired user email field gets transformed into, where {} is [output truncated, see link for full description]

* +RETIRED_EMAIL_PREFIX: `openedx/envs/common.py (line 2095) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L2095>`_
   * Default value = "retired__user_"
   * Description: Set the prefix part of hashed emails for retired users. Used by the derived [output truncated, see link for full description]

* +RETIRED_USERNAME_FMT: `openedx/envs/common.py (line 2107) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L2107>`_
   * Default value = "retired__user_{}"
   * Description: Set the format a retired user username field gets transformed into, where {} [output truncated, see link for full description]

* +RETIRED_USERNAME_PREFIX: `openedx/envs/common.py (line 2089) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L2089>`_
   * Default value = "retired__user_"
   * Description: Set the prefix part of hashed usernames for retired users. Used by the derived [output truncated, see link for full description]

* +RETIRED_USER_SALTS: `openedx/envs/common.py (line 2121) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L2121>`_
   * Default value = "['abc', '123']"
   * Description: Set a list of salts used for hashing usernames and emails on users retirement.

* +RETIREMENT_SERVICE_WORKER_USERNAME: `openedx/envs/common.py (line 2129) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L2129>`_
   * Default value = "RETIREMENT_SERVICE_USER"
   * Description: Set the username of the retirement service worker user. Retirement scripts [output truncated, see link for full description]

* +RETIREMENT_STATES: `openedx/envs/common.py (line 2135) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L2135>`_
   * Default value = "RETIREMENT_SERVICE_USER"
   * Description: Set a list that defines the name and order of states for the retirement [output truncated, see link for full description]

* +STATIC_URL_BASE: `openedx/envs/common.py (line 2315) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L2315>`_
   * Default value = ""None""
   * Description: The LMS and CMS use this to construct ``STATIC_URL`` by appending [output truncated, see link for full description]

* +XBLOCK_EXTRA_MIXINS: `openedx/envs/common.py (line 1637) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1637>`_
   * Default value = "()"
   * Description: Custom mixins that will be dynamically added to every XBlock and XBlockAside instance. [output truncated, see link for full description]

* +XBLOCK_FIELD_DATA_WRAPPERS: `openedx/envs/common.py (line 1644) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1644>`_
   * Default value = "()"
   * Description: Paths to wrapper methods which should be applied to every XBlock’s FieldData.
* +XBLOCK_FIELD_DATA_WRAPPERS: `openedx/envs/common.py (line 1660) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1660>`_
   * Default value = "default"
   * Description: The django cache key of the cache to use for storing anonymous user state for XBlocks.

* +XBLOCK_SETTINGS: `openedx/envs/common.py (line 1652) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1652>`_
   * Default value = "{}"
   * Description: Dictionary containing server-wide configuration of XBlocks on a per-type basis. [output truncated, see link for full description]

* +CATALOG_MICROFRONTEND_URL: `lms/envs/common.py (line 3218) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L3218>`_
   * Default value = None
   * Description: Base URL of the micro-frontend-based course catalog page.

* +CCX_MAX_STUDENTS_ALLOWED: `lms/envs/common.py (line 2983) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L2983>`_
   * Default value = 200
   * Description: Maximum number of students allowed in a CCX (Custom Courses for edX), This is an arbitrary [output truncated, see link for full description]

* +CELERY_EXTRA_IMPORTS: `lms/envs/common.py (line 1958) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L1958>`_
   * Default value = "[]"
   * Description: Adds extra packages that don’t get auto-imported (Example: XBlocks). [output truncated, see link for full description]

* +CONTENT_FOR_SPAM_POSTS: `lms/envs/common.py (line 3228) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L3228>`_
   * Default value = """"
   * Description: Content to replace spam posts with

* +COURSE_MEMBER_API_ENROLLMENT_LIMIT: `lms/envs/common.py (line 2918) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L2918>`_
   * Default value = 1000
   * Description: This limits the response size of the `get_course_members` API, throwing an exception [output truncated, see link for full description]

* +DISABLED_ORGS_FOR_PROGRAM_NUDGE: `lms/envs/common.py (line 3502) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L3502>`_
   * Default value = "[]"
   * Description: List of organization codes that should be disabled

* +DISCUSSION_SPAM_URLS: `lms/envs/common.py (line 3223) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L3223>`_
   * Default value = "[]"
   * Description: Urls to filter from discussion content to avoid spam

* +HIBP_LOGIN_BLOCK_PASSWORD_FREQUENCY_THRESHOLD: `lms/envs/common.py (line 3291) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L3291>`_
   * Default value = 5.0
   * Description: Log10 threshold in effect for ENABLE_AUTHN_LOGIN_BLOCK_HIBP_POLICY. [output truncated, see link for full description]

* +HIBP_LOGIN_NUDGE_PASSWORD_FREQUENCY_THRESHOLD: `lms/envs/common.py (line 3267) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L3267>`_
   * Default value = 3.0
   * Description: Log10 threshold in effect for ENABLE_AUTHN_LOGIN_NUDGE_HIBP_POLICY. [output truncated, see link for full description]

* +HIBP_REGISTRATION_PASSWORD_FREQUENCY_THRESHOLD: `lms/envs/common.py (line 3252) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L3252>`_
   * Default value = 3.0
   * Description: Log10 threshold in effect for ENABLE_AUTHN_REGISTER_HIBP_POLICY. [output truncated, see link for full description]

* +LTI_CUSTOM_PARAMS: `lms/envs/common.py (line 2953) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L2953>`_
   * Default value = "[]"
   * Description: This expands the list of optional LTI parameters that the [output truncated, see link for full description]

* +PROFILE_INFORMATION_REPORT_PRIVATE_FIELDS: `lms/envs/common.py (line 2795) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L2795>`_
   * Default value = "["year_of_birth"]"
   * Description: List of private fields that will be hidden from the profile information report.

* +PYTHON_LIB_FILENAME: `lms/envs/common.py (line 1180) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L1180>`_
   * Default value = "python_lib.zip"
   * Description: Name of the course file to make available to code in [output truncated, see link for full description]

* +RECAPTCHA_PRIVATE_KEY: `lms/envs/common.py (line 3637) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L3637>`_
   * Default value = "empty string"
   * Description: Add recaptcha private key to use captcha feature in discussion app.

* +RECAPTCHA_PROJECT_ID: `lms/envs/common.py (line 3659)`_
   * Default value = None
   * Description: Add recaptcha project id to use captcha feature in discussion app.

* +RECAPTCHA_SITE_KEYS: `lms/envs/common.py (line 3642) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L3642>`_
   * Default value = "empty dictionary"
   * Description: Add recaptcha site keys to use captcha feature in discussion app.

* +DEFAULT_ORG_LOGO_URL: `cms/envs/common.py (line 1787) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L1787>`_
   * Default value = "Derived(lambda settings: settings.STATIC_URL + 'images/logo.png')"
   * Description: The default logo url for organizations that do not have a logo set.

Removed Settings
*************************

* -CCX_MAX_STUDENTS_ALLOWED: `lms/envs/common.py (line 4522) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4522>`_
   * Description: Maximum number of students allowed in a CCX (Custom Courses for edX), This is an arbitrary [output truncated, see link for full description]

* -CELERY_EXTRA_IMPORTS: `lms/envs/common.py (line 2825) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L2825>`_
   * Description: Adds extra packages that don’t get auto-imported (Example: XBlocks). [output truncated, see link for full description]

* -COURSE_MEMBER_API_ENROLLMENT_LIMIT: `lms/envs/common.py (line 4396) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4396>`_
   * Description: This limits the response size of the `get_course_members` API, throwing an exception [output truncated, see link for full description]

* -DISABLED_ORGS_FOR_PROGRAM_NUDGE: `lms/envs/common.py (line 5390) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5390>`_
   * Description: List of organization codes that should be disabled

* -LEARNING_MICROFRONTEND_URL: `lms/envs/common.py (line 5032) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L5032>`_
   * Description: Base URL of the micro-frontend-based courseware page.

* -LOGIN_REDIRECT_WHITELIST: `lms/envs/common.py (line 3692) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L3692>`_
   * Description: While logout, if logout request has a redirect-url as query strings, [output truncated, see link for full description]

* -MAX_FAILED_LOGIN_ATTEMPTS_ALLOWED: `lms/envs/common.py (line 3835) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L3835>`_
   * Description: Specifies the maximum failed login attempts allowed to users. Once the user reaches this [output truncated, see link for full description]

* -MAX_FAILED_LOGIN_ATTEMPTS_LOCKOUT_PERIOD_SECS: `lms/envs/common.py (line 3844) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L3844>`_
   * Description: Specifies the lockout period in seconds for consecutive failed login attempts. Once the user [output truncated, see link for full description]

* -PLATFORM_NAME: `lms/envs/common.py (line 76) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L76>`_
   * Description: The display name of the platform to be used in [output truncated, see link for full description]

* -PREPEND_LOCALE_PATHS: `lms/envs/common.py (line 4594) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4594>`_
   * Description: A list of the paths to locale directories to load first e.g. [output truncated, see link for full description]

* -REGISTRATION_RATELIMIT: `lms/envs/common.py (line 3446) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L3446>`_
   * Description: New users are registered on edx via RegistrationView. [output truncated, see link for full description]

* -REGISTRATION_VALIDATION_RATELIMIT: `lms/envs/common.py (line 3437) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L3437>`_
   * Description: Whenever a user tries to register on edx, the data entered during registration [output truncated, see link for full description]

* -RETIRED_EMAIL_DOMAIN: `lms/envs/common.py (line 4924) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4924>`_
   * Description: Set the domain part of hashed emails for retired users. Used by the derived [output truncated, see link for full description]

* -RETIRED_EMAIL_FMT: `lms/envs/common.py (line 4935) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4935>`_
   * Description: Set the format a retired user email field gets transformed into, where {} is [output truncated, see link for full description]

* -RETIRED_EMAIL_PREFIX: `lms/envs/common.py (line 4919) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4919>`_
   * Description: Set the prefix part of hashed emails for retired users. Used by the derived [output truncated, see link for full description]

* -RETIRED_USERNAME_FMT: `lms/envs/common.py (line 4929) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4929>`_
   * Description: Set the format a retired user username field gets transformed into, where {} [output truncated, see link for full description]

* -RETIRED_USERNAME_PREFIX: `lms/envs/common.py (line 4913) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4913>`_
   * Description: Set the prefix part of hashed usernames for retired users. Used by the derived [output truncated, see link for full description]

* -RETIRED_USER_SALTS: `lms/envs/common.py (line 4941) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4941>`_
   * Description: Set a list of salts used for hashing usernames and emails on users retirement.

* -RETIREMENT_SERVICE_WORKER_USERNAME: `lms/envs/common.py (line 4948) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4948>`_
   * Description: Set the username of the retirement service worker user. Retirement scripts [output truncated, see link for full description]

* -RETIREMENT_STATES: `lms/envs/common.py (line 4954) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L4954>`_
   * Description: Set a list that defines the name and order of states for the retirement [output truncated, see link for full description]

* -XBLOCK_EXTRA_MIXINS: `lms/envs/common.py (line 1652) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L1652>`_
   * Description: Custom mixins that will be dynamically added to every XBlock and XBlockAside instance. [output truncated, see link for full description]

* -XBLOCK_FIELD_DATA_WRAPPERS: `lms/envs/common.py (line 1659) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L1659>`_
   * Description: Paths to wrapper methods which should be applied to every XBlock’s FieldData.
* -XBLOCK_FIELD_DATA_WRAPPERS: `lms/envs/common.py (line 1675) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L1675>`_
   * Description: The django cache key of the cache to use for storing anonymous user state for XBlocks.

* -XBLOCK_SETTINGS: `lms/envs/common.py (line 1667) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L1667>`_
   * Description: Dictionary containing server-wide configuration of XBlocks on a per-type basis. [output truncated, see link for full description]

* -CODE_JAIL_REST_SERVICE_CONNECT_TIMEOUT: `cms/envs/common.py (line 1197) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L1197>`_
   * Description: Set the number of seconds CMS will wait to establish an internal [output truncated, see link for full description]

* -CODE_JAIL_REST_SERVICE_HOST: `cms/envs/common.py (line 1193) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L1193>`_
   * Description: Set the codejail remote service host

* -CODE_JAIL_REST_SERVICE_READ_TIMEOUT: `cms/envs/common.py (line 1201) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L1201>`_
   * Description: Set the number of seconds CMS will wait for a response from the [output truncated, see link for full description]

* -CODE_JAIL_REST_SERVICE_REMOTE_EXEC: `cms/envs/common.py (line 1188) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L1188>`_
   * Description: Set the python package.module.function that is reponsible of [output truncated, see link for full description]

* -COMPREHENSIVE_THEME_DIRS: `cms/envs/common.py (line 2178) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L2178>`_
   * Description: A list of paths to directories, each of which will [output truncated, see link for full description]

* -COMPREHENSIVE_THEME_LOCALE_PATHS: `cms/envs/common.py (line 2186) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L2186>`_
   * Description: See LMS annotation. [output truncated, see link for full description]

* -CUSTOM_RESOURCE_TEMPLATES_DIRECTORY: `cms/envs/common.py (line 2211) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L2211>`_
   * Description: Path to an existing directory of YAML files containing [output truncated, see link for full description]

* -DEFAULT_SITE_THEME: `cms/envs/common.py (line 2198) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L2198>`_
   * Description: See LMS annotation.

* -PREPEND_LOCALE_PATHS: `cms/envs/common.py (line 2192) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L2192>`_
   * Description: A list of the paths to locale directories to load first e.g. [output truncated, see link for full description]

* -XBLOCK_EXTRA_MIXINS: `cms/envs/common.py (line 1006) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L1006>`_
   * Description: Custom mixins that will be dynamically added to every XBlock and XBlockAside instance. [output truncated, see link for full description]
* -XBLOCK_EXTRA_MIXINS: `cms/envs/common.py (line 1016) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L1016>`_
   * Description: The django cache key of the cache to use for storing anonymous user state for XBlocks.


Added Feature Toggles
*********************


* +ALLOW_PUBLIC_ACCOUNT_CREATION: `openedx/envs/common.py (line 884) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L884>`_
   * Default value = True
   * Description: Desc: Allow public account creation. If this is disabled, users will no longer have access to [output truncated, see link for full description]

* +AUTOMATIC_AUTH_FOR_TESTING: `openedx/envs/common.py (line 720) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L720>`_
   * Default value = False
   * Description: Desc: Set to True to perform acceptance and load test. Auto auth view is responsible for load [output truncated, see link for full description]

* +BADGES_ENABLED: `openedx/envs/common.py (line 1022) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1022>`_
   * Default value = False
   * Description: Desc: Set to True to enable badges functionality.

* +CERTIFICATES_HTML_VIEW: `openedx/envs/common.py (line 805) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L805>`_
   * Default value = False
   * Description: Desc: Set to True to enable course certificates on your instance of Open edX.

* +DISABLE_START_DATES: `openedx/envs/common.py (line 631) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L631>`_
   * Default value = False
   * Description: Desc: When True, all courses will be active, regardless of start [output truncated, see link for full description]

* +DISABLE_UNENROLLMENT: `openedx/envs/common.py (line 1001) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1001>`_
   * Default value = False
   * Description: Desc: Set to True to disable self-unenrollments via REST API. [output truncated, see link for full description]

* +EDX_DRF_EXTENSIONS[ENABLE_JWT_AND_LMS_USER_EMAIL_MATCH]: `.venv/lib/python3.11/site-packages/edx_rest_framework_extensions/config.py (line 19) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/edx_rest_framework_extensions/config.py#L19>`_
   * Default value = False
   * Description: Desc: Toggle to add a check for matching user email in JWT and LMS user email [output truncated, see link for full description]

* +EDX_DRF_EXTENSIONS[ENABLE_SET_REQUEST_USER_FOR_JWT_COOKIE]: `.venv/lib/python3.11/site-packages/edx_rest_framework_extensions/config.py (line 5) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/edx_rest_framework_extensions/config.py#L5>`_
   * Default value = False
   * Description: Desc: Toggle for setting request.user with jwt cookie authentication. This makes the JWT cookie [output truncated, see link for full description]

* +EMBARGO: `openedx/envs/common.py (line 744) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L744>`_
   * Default value = False
   * Description: Desc: Turns on embargo functionality, which blocks users from [output truncated, see link for full description]

* +ENABLE_CHANGE_USER_PASSWORD_ADMIN: `openedx/envs/common.py (line 931) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L931>`_
   * Default value = False
   * Description: Desc: Set to True to enable changing a user password through django admin. This is disabled by [output truncated, see link for full description]

* +ENABLE_CREDIT_ELIGIBILITY: `openedx/envs/common.py (line 1031) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1031>`_
   * Default value = True
   * Description: Desc: When enabled, it is possible to define a credit eligibility criteria in the CMS. A “Credit [output truncated, see link for full description]

* +ENABLE_CSMH_EXTENDED: `openedx/envs/common.py (line 862) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L862>`_
   * Default value = True
   * Description: Desc: Write Courseware Student Module History (CSMH) to the extended table: this logs all [output truncated, see link for full description]

* +ENABLE_DISCUSSION_SERVICE: `openedx/envs/common.py (line 644) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L644>`_
   * Default value = True
   * Description: Desc: When True, it will enable the Discussion tab in courseware for all courses. Setting this [output truncated, see link for full description]

* +ENABLE_GRADING_METHOD_IN_PROBLEMS: `openedx/envs/common.py (line 1013) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L1013>`_
   * Default value = False
   * Description: Desc: Enables the grading method feature in capa problems.

* +ENABLE_HELP_LINK: `openedx/envs/common.py (line 683) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L683>`_
   * Default value = True
   * Description: Desc: When True, a help link is displayed on the main navbar. Set False to hide it.

* +ENABLE_INTEGRITY_SIGNATURE: `openedx/envs/common.py (line 968) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L968>`_
   * Default value = False
   * Description: Desc: Whether to display honor code agreement for learners before their first grade assignment.

* +ENABLE_LTI_PII_ACKNOWLEDGEMENT: `openedx/envs/common.py (line 979) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L979>`_
   * Default value = False
   * Description: Desc: Enables the lti pii acknowledgement feature for a course

* +ENABLE_MKTG_SITE: `openedx/envs/common.py (line 758) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L758>`_
   * Default value = False
   * Description: Desc: Toggle to enable alternate urls for marketing links.

* +ENABLE_OAUTH2_PROVIDER: `openedx/envs/common.py (line 668) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L668>`_
   * Default value = False
   * Description: Desc: Enable this feature to allow this Open edX platform to be an OAuth2 authentication [output truncated, see link for full description]

* +ENABLE_ORA_ALL_FILE_URLS: `openedx/envs/common.py (line 943) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L943>`_
   * Default value = False
   * Description: Desc: A “work-around” feature toggle meant to help in cases where some file uploads are not [output truncated, see link for full description]

* +ENABLE_ORA_USER_STATE_UPLOAD_DATA: `openedx/envs/common.py (line 956) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L956>`_
   * Default value = False
   * Description: Desc: A “work-around” feature toggle meant to help in cases where some file uploads are not [output truncated, see link for full description]

* +ENABLE_PASSWORD_RESET_FAILURE_EMAIL: `openedx/envs/common.py (line 906) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L906>`_
   * Default value = False
   * Description: Desc: Whether to send an email for failed password reset attempts or not. This happens when a [output truncated, see link for full description]

* +ENABLE_SAML_CONFIG_SIGNAL_HANDLERS: `common/djangoapps/third_party_auth/toggles.py (line 21) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/common/djangoapps/third_party_auth/toggles.py#L21>`_
   * Default value = False
   * Description: Desc: Controls whether SAML configuration signal handlers are active. [output truncated, see link for full description]

* +ENABLE_SPECIAL_EXAMS: `openedx/envs/common.py (line 827) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L827>`_
   * Default value = False
   * Description: Desc: Enable to use special exams, aka timed and proctored exams.

* +ENABLE_TEXTBOOK: `openedx/envs/common.py (line 657) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L657>`_
   * Default value = True
   * Description: Desc: Add PDF and HTML textbook tabs to the courseware.

* +EVENT_BUS_KAFKA_AUDIT_LOGGING_ENABLED: `.venv/lib/python3.11/site-packages/edx_event_bus_kafka/internal/utils.py (line 16) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/edx_event_bus_kafka/internal/utils.py#L16>`_
   * Default value = True
   * Description: Desc: If True, whenever an event is produced or consumed, log enough [output truncated, see link for full description]

* +EVENT_BUS_KAFKA_CONSUMERS_ENABLED: `.venv/lib/python3.11/site-packages/edx_event_bus_kafka/internal/consumer.py (line 44) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/edx_event_bus_kafka/internal/consumer.py#L44>`_
   * Default value = True
   * Description: Desc: If set to False, consumer will exit immediately. This can be used as an emergency kill-switch [output truncated, see link for full description]

* +EVENT_BUS_REDIS_AUDIT_LOGGING_ENABLED: `.venv/lib/python3.11/site-packages/edx_event_bus_redis/internal/utils.py (line 16) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/edx_event_bus_redis/internal/utils.py#L16>`_
   * Default value = True
   * Description: Desc: If True, whenever an event is produced or consumed, log enough [output truncated, see link for full description]

* +EVENT_BUS_REDIS_CONSUMERS_ENABLED: `.venv/lib/python3.11/site-packages/edx_event_bus_redis/internal/consumer.py (line 26) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/edx_event_bus_redis/internal/consumer.py#L26>`_
   * Default value = True
   * Description: Desc: If set to False, consumer will exit immediately. This can be used as an emergency kill-switch [output truncated, see link for full description]

* +FEATURES['ENABLE_ENHANCED_STAFF_GRADER']: `.venv/lib/python3.11/site-packages/openassessment/xblock/config_mixin.py (line 161) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/openassessment/xblock/config_mixin.py#L161>`_
   * Default value = False
   * Description: Desc: Set to True to enable the enhanced staff grader feature

* +FEATURES['ENABLE_ORA_MOBILE_SUPPORT']: `.venv/lib/python3.11/site-packages/openassessment/xblock/config_mixin.py (line 131) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/openassessment/xblock/config_mixin.py#L131>`_
   * Default value = False
   * Description: Desc: Set to True to enable the ORA2 Xblock to be rendered [output truncated, see link for full description]

* +FEATURES['ENABLE_ORA_PEER_CONFIGURABLE_GRADING']: `.venv/lib/python3.11/site-packages/openassessment/xblock/config_mixin.py (line 191) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/openassessment/xblock/config_mixin.py#L191>`_
   * Default value = False
   * Description: Desc: Enable configurable grading for peer review.

* +FEATURES['ENABLE_ORA_RUBRIC_REUSE']: `.venv/lib/python3.11/site-packages/openassessment/xblock/config_mixin.py (line 146) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/openassessment/xblock/config_mixin.py#L146>`_
   * Default value = False
   * Description: Desc: Set to True to enable the reuse of rubric feature

* +FEATURES['ENABLE_ORA_SELECTABLE_LEARNER_WAITING_REVIEW']: `.venv/lib/python3.11/site-packages/openassessment/xblock/config_mixin.py (line 175) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/openassessment/xblock/config_mixin.py#L175>`_
   * Default value = False
   * Description: Desc: Enable selectable learner in the waiting step list ORA2. [output truncated, see link for full description]

* +LICENSING: `openedx/envs/common.py (line 795) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L795>`_
   * Default value = False
   * Description: Desc: Toggle platform-wide course licensing. The course.license attribute is then used to append [output truncated, see link for full description]

* +RBAC_IGNORE_INVALID_JWT_COOKIE: `.venv/lib/python3.11/site-packages/edx_rbac/constants.py (line 7) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/edx_rbac/constants.py#L7>`_
   * Default value = False
   * Description: Desc: When true, causes instances of `jwt.exceptions.InvalidTokenError` [output truncated, see link for full description]

* +RESTRICT_AUTOMATIC_AUTH: `openedx/envs/common.py (line 732) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L732>`_
   * Default value = True
   * Description: Desc: Prevent auto auth from creating superusers or modifying existing users. Auto auth is a [output truncated, see link for full description]

* +SEND_TRACKING_EVENT_EMITTED_SIGNAL: `.venv/lib/python3.11/site-packages/eventtracking/config.py (line 8) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/eventtracking/config.py#L8>`_
   * Default value = False
   * Description: Desc: When True, the system will publish `TRACKING_EVENT_EMITTED` signals to the event bus. The [output truncated, see link for full description]

* +SHOW_FOOTER_LANGUAGE_SELECTOR: `openedx/envs/common.py (line 852) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L852>`_
   * Default value = False
   * Description: Desc: When set to True, language selector will be visible in the footer.

* +SHOW_HEADER_LANGUAGE_SELECTOR: `openedx/envs/common.py (line 836) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L836>`_
   * Default value = False
   * Description: Desc: When set to True, language selector will be visible in the header.

* +SHOW_REGISTRATION_LINKS: `openedx/envs/common.py (line 894) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L894>`_
   * Default value = True
   * Description: Desc: Allow registration links. If this is disabled, users will no longer see buttons to the [output truncated, see link for full description]

* +annotated_flag&#10;\ \ \ \ \ \ \ \ WaffleFlag(NAMESPACE,\ 'annotated_flag')&#10;&#10;\ \ \ \ \ \ \ \ #\ ..\ toggle_name:\ course_waffle_annotated_flag&#10;\ \ \ \ \ \ \ \ CourseWaffleFlag(NAMESPACE,\ 'course_waffle_annotated_flag')&#10;&#10;\ \ \ \ \ \ \ \ NotAFlag(NAMESPACE,\ NOT_A_WAFFLE_FLAG)&#10;&#10;\ \ \ \ \ \ \ \ #\ ..\ wrong_annotation&#10;\ \ \ \ \ \ \ \ WaffleFlag(NAMESPACE,\ 'flag_with_bad_annotation')\ #=A&#10;&#10;\ \ \ \ \ \ \ \ WaffleFlag(NAMESPACE,\ FLAG_WITHOUT_ANNOTATION)\ #=B&#10;&#10;\ \ \ \ \ \ \ \ DerivedWaffleFlag(NAMESPACE,\ DERIVED_FLAG_WITHOUT_ANNOTATION)\ #=C&#10;&#10;\ \ \ \ \ \ \ \ WaffleSwitch(NAMESPACE,\ SWITCH_WITHOUT_ANNOTATION)\ #=D&#10;&#10;\ \ \ \ \ \ \ \ CourseWaffleFlag(NAMESPACE,\ COURSE_WAFFLE_FLAG_WITHOUT_ANNOTATION)\ #=E&#10;&#10;\ \ \ \ \ \ \ \ MissingCourseWithKwarg\ =\ CourseWaffleFlag(\ #=F&#10;\ \ \ \ \ \ \ \ \ \ \ \ waffle_namespace=waffle_flags(),&#10;\ \ \ \ \ \ \ \ \ \ \ \ flag_name=u'missing_course_with_kwarg',&#10;\ \ \ \ \ \ \ \ ): `.venv/lib/python3.11/site-packages/test/plugins/test_annotations_check.py (line 8) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/test/plugins/test_annotations_check.py#L8>`_
   * Default value = "Not defined"
   * Description: Desc: NaN

* +completion.enable_completion_tracking: `.venv/lib/python3.11/site-packages/completion/waffle.py (line 11) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/completion/waffle.py#L11>`_
   * Default value = False
   * Description: Desc: Indicates whether or not to track completion of individual blocks. Keeping this disabled [output truncated, see link for full description]

* +contentstore.enable_course_optimizer_check_prev_run_links: `cms/djangoapps/contentstore/toggles.py (line 600) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/djangoapps/contentstore/toggles.py#L600>`_
   * Default value = False
   * Description: Desc: When enabled, allows the Course Optimizer to detect and update links pointing to previous course runs. [output truncated, see link for full description]

* +contentstore.new_studio_mfe.use_new_video_uploads_page: `cms/djangoapps/contentstore/toggles.py (line 316) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/djangoapps/contentstore/toggles.py#L316>`_
   * Default value = False
   * Description: Desc: This flag enables the use of the new studio video uploads page mfe

* +course_assets.allow_download_code_library: `openedx/core/djangoapps/contentserver/views.py (line 274) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/core/djangoapps/contentserver/views.py#L274>`_
   * Default value = False
   * Description: Desc: Whether to allow learners to download the course code library [output truncated, see link for full description]

* +course_home.send_course_progress_analytics_for_student: `lms/djangoapps/course_home_api/toggles.py (line 39) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/djangoapps/course_home_api/toggles.py#L39>`_
   * Default value = False
   * Description: Desc: This toggle controls whether the system will enqueue a Celery task responsible for emitting an [output truncated, see link for full description]

* +discussion.enable_captcha: `lms/djangoapps/discussion/config/settings.py (line 25) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/djangoapps/discussion/config/settings.py#L25>`_
   * Default value = False
   * Description: Desc: When the flag is ON, users will be able to see captcha for discussion

* +discussions.enable_rate_limit: `lms/djangoapps/discussion/toggles.py (line 32) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/djangoapps/discussion/toggles.py#L32>`_
   * Default value = False
   * Description: Desc: Waffle flag to enable rate limit on discussions

* +discussions.only_verified_users_can_post: `lms/djangoapps/discussion/toggles.py (line 20) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/djangoapps/discussion/toggles.py#L20>`_
   * Default value = False
   * Description: Desc: Waffle flag to allow only verified users to post in discussions

* +drag_and_drop_v2.grading_ignore_decoys: `.venv/lib/python3.11/site-packages/drag_and_drop_v2/compat.py (line 10) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/drag_and_drop_v2/compat.py#L10>`_
   * Default value = False
   * Description: Desc: Enables alternative grading for the xblock [output truncated, see link for full description]

* +edx_search.default_elastic_search: `.venv/lib/python3.11/site-packages/search/search_engine_base.py (line 10) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/search/search_engine_base.py#L10>`_
   * Default value = False
   * Description: Desc: This flag forces the use of ElasticSearch. [output truncated, see link for full description]

* +edxval.override_existing_imported_transcripts: `.venv/lib/python3.11/site-packages/edxval/config/waffle.py (line 11) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/edxval/config/waffle.py#L11>`_
   * Default value = False
   * Description: Desc: Enables overriding existing transcripts when importing courses with already [output truncated, see link for full description]

* +enterprise.TOP_DOWN_ASSIGNMENT_REAL_TIME_LCM: `.venv/lib/python3.11/site-packages/enterprise/toggles.py (line 10) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/enterprise/toggles.py#L10>`_
   * Default value = False
   * Description: Desc: Enables top-down assignment

* +enterprise.admin_portal_learner_profile_view_enabled: `.venv/lib/python3.11/site-packages/enterprise/toggles.py (line 59) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/enterprise/toggles.py#L59>`_
   * Default value = False
   * Description: Desc: Enables an admin to view a learner’s profile

* +enterprise.catalog_query_search_filters_enabled: `.venv/lib/python3.11/site-packages/enterprise/toggles.py (line 71) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/enterprise/toggles.py#L71>`_
   * Default value = False
   * Description: Desc: Enables filtering search results by catalog queries vs. enterprise-specific attributes.

* +enterprise.edit_highlights_enabled: `.venv/lib/python3.11/site-packages/enterprise/toggles.py (line 95) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/enterprise/toggles.py#L95>`_
   * Default value = False
   * Description: Desc: Enables the Edit Highlights experience.

* +enterprise.enterprise_admin_onboarding: `.venv/lib/python3.11/site-packages/enterprise/toggles.py (line 83) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/enterprise/toggles.py#L83>`_
   * Default value = False
   * Description: Desc: Enables the admin onboarding tour on the admin-portal.

* +enterprise.enterprise_customer_support_tool: `.venv/lib/python3.11/site-packages/enterprise/toggles.py (line 35) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/enterprise/toggles.py#L35>`_
   * Default value = False
   * Description: Desc: Enables the enterprise customer support tool

* +enterprise.enterprise_learner_bff_enabled: `.venv/lib/python3.11/site-packages/enterprise/toggles.py (line 47) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/enterprise/toggles.py#L47>`_
   * Default value = False
   * Description: Desc: Enables the enterprise learner BFF

* +enterprise.feature_prequery_search_suggestions: `.venv/lib/python3.11/site-packages/enterprise/toggles.py (line 22) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/enterprise/toggles.py#L22>`_
   * Default value = False
   * Description: Desc: Enables prequery search suggestions

* +forum_v2.enable_mysql_backend: `.venv/lib/python3.11/site-packages/forum/toggles.py (line 9) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/.venv/lib/python3.11/site-packages/forum/toggles.py#L9>`_
   * Default value = False
   * Description: Desc: Waffle flag to use the MySQL backend instead of Mongo backend.

* +notifications.enable_push_notifications: `openedx/core/djangoapps/notifications/config/waffle.py (line 32)`_
   * Default value = False
   * Description: Desc: Waffle flag to enable push Notifications feature on mobile devices

* +settings.ALLOW_ADMIN_ENTERPRISE_COURSE_ENROLLMENT_DELETION: `lms/envs/common.py (line 616) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L616>`_
   * Default value = False
   * Description: Desc: If true, allows for the deletion of EnterpriseCourseEnrollment records via Django Admin.

* +settings.ALLOW_COURSE_RERUNS: `cms/envs/common.py (line 152) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L152>`_
   * Default value = True
   * Description: Desc: This will allow staff member to re-run the course from the studio home page and will [output truncated, see link for full description]

* +settings.ALLOW_EMAIL_ADDRESS_CHANGE: `lms/envs/common.py (line 522) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L522>`_
   * Default value = True
   * Description: Desc: Allow users to change their email address on the Account Settings page. If this is [output truncated, see link for full description]

* +settings.ALWAYS_REDIRECT_HOMEPAGE_TO_DASHBOARD_FOR_AUTHENTICATED_USER: `lms/envs/common.py (line 330) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L330>`_
   * Default value = True
   * Description: Desc: When a logged in user goes to the homepage (‘/’) the user will be redirected to the [output truncated, see link for full description]

* +settings.AUTOMATIC_VERIFY_STUDENT_IDENTITY_FOR_TESTING: `lms/envs/common.py (line 269) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L269>`_
   * Default value = False
   * Description: Desc: If set to True, then we want to skip posting anything to Software Secure. Bypass posting [output truncated, see link for full description]

* +settings.BADGES_ENABLED: `lms/envs/common.py (line 690) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L690>`_
   * Default value = False
   * Description: Desc: Set to True to enable badges functionality.

* +settings.COURSES_ARE_BROWSABLE: `lms/envs/common.py (line 178) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L178>`_
   * Default value = True
   * Description: Desc: When this is set to True, all the courses will be listed on the /courses page and Explore [output truncated, see link for full description]

* +settings.CUSTOM_CERTIFICATE_TEMPLATES_ENABLED: `lms/envs/common.py (line 436) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L436>`_
   * Default value = False
   * Description: Desc: Set to True to enable custom certificate templates which are configured via Django admin.

* +settings.DEPRECATE_OLD_COURSE_KEYS_IN_STUDIO: `cms/envs/common.py (line 176) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L176>`_
   * Default value = True
   * Description: Desc: Warn about removing support for deprecated course keys. [output truncated, see link for full description]

* +settings.DISABLE_ADVANCED_SETTINGS: `cms/envs/common.py (line 214) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L214>`_
   * Default value = False
   * Description: Desc: Set to `True` to disable the advanced settings page in Studio for all users except those [output truncated, see link for full description]

* +settings.DISABLE_ALLOWED_ENROLLMENT_IF_ENROLLMENT_CLOSED: `lms/envs/common.py (line 659) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L659>`_
   * Default value = False
   * Description: Desc: Set to True to disable enrollment for user invited to a course

* +settings.DISABLE_COURSE_CREATION: `cms/envs/common.py (line 192) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L192>`_
   * Default value = False
   * Description: Desc: If set to True, it disables the course creation functionality and hides the “New Course” [output truncated, see link for full description]

* +settings.DISABLE_HONOR_CERTIFICATES: `lms/envs/common.py (line 227) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L227>`_
   * Default value = False
   * Description: Desc: Set to True to disable honor certificates. Typically used when your installation only [output truncated, see link for full description]

* +settings.DISABLE_LOGIN_BUTTON: `lms/envs/common.py (line 158) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L158>`_
   * Default value = False
   * Description: Desc: Removes the display of the login button in the navigation bar. [output truncated, see link for full description]

* +settings.DISABLE_MOBILE_COURSE_AVAILABLE: `openedx/envs/common.py (line 921) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L921>`_
   * Default value = False
   * Description: Desc: Set to True to remove Mobile Course Available UI Flag from Studio’s Advanced Settings [output truncated, see link for full description]

* +settings.DISPLAY_DEBUG_INFO_TO_STAFF: `lms/envs/common.py (line 78) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L78>`_
   * Default value = True
   * Description: Desc: Add a “Staff Debug” button to course blocks for debugging [output truncated, see link for full description]

* +settings.DISPLAY_HISTOGRAMS_TO_STAFF: `lms/envs/common.py (line 88) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L88>`_
   * Default value = False
   * Description: Desc: This displays histograms in the Staff Debug Info panel to course staff.

* +settings.EDITABLE_SHORT_DESCRIPTION: `cms/envs/common.py (line 103) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L103>`_
   * Default value = True
   * Description: Desc: This feature flag allows editing of short descriptions on the Schedule &amp; Details page in [output truncated, see link for full description]

* +settings.ENABLE_ACCOUNT_DELETION: `lms/envs/common.py (line 560) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L560>`_
   * Default value = True
   * Description: Desc: Whether to display the account deletion section on Account Settings page. Set to False to [output truncated, see link for full description]

* +settings.ENABLE_AUTHN_MICROFRONTEND: `lms/envs/common.py (line 570) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L570>`_
   * Default value = False
   * Description: Desc: Supports staged rollout of a new micro-frontend-based implementation of the logistration.

* +settings.ENABLE_BULK_ENROLLMENT_VIEW: `lms/envs/common.py (line 532) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L532>`_
   * Default value = False
   * Description: Desc: When set to True the bulk enrollment view is enabled and one can use it to enroll multiple [output truncated, see link for full description]

* +settings.ENABLE_BULK_USER_RETIREMENT: `lms/envs/common.py (line 625) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L625>`_
   * Default value = False
   * Description: Desc: Set to True to enable bulk user retirement through REST API. This is disabled by [output truncated, see link for full description]

* +settings.ENABLE_CATALOG_MICROFRONTEND: `lms/envs/common.py (line 582) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L582>`_
   * Default value = False
   * Description: Desc: Supports staged rollout of a new micro-frontend-based implementation of the catalog.

* +settings.ENABLE_CERTIFICATES_IDV_REQUIREMENT: `lms/envs/common.py (line 649) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L649>`_
   * Default value = False
   * Description: Desc: Whether to enforce ID Verification requirements for course certificates generation

* +settings.ENABLE_COMBINED_LOGIN_REGISTRATION_FOOTER: `lms/envs/common.py (line 362) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L362>`_
   * Default value = False
   * Description: Desc: Display the standard footer in the login page. This feature can be overridden by a site- [output truncated, see link for full description]

* +settings.ENABLE_CONTENT_LIBRARIES_LTI_TOOL: `cms/envs/common.py (line 133) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L133>`_
   * Default value = False
   * Description: Desc: When set to True, Content Libraries in [output truncated, see link for full description]

* +settings.ENABLE_COOKIE_CONSENT: `lms/envs/common.py (line 508) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L508>`_
   * Default value = False
   * Description: Desc: Enable header banner for cookie consent using this service: [output truncated, see link for full description]

* +settings.ENABLE_COSMETIC_DISPLAY_PRICE: `lms/envs/common.py (line 258) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L258>`_
   * Default value = False
   * Description: Desc: Enable the display of “cosmetic_display_price”, set in a course advanced settings. This [output truncated, see link for full description]

* +settings.ENABLE_COURSEWARE_SEARCH: `lms/envs/common.py (line 395) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L395>`_
   * Default value = False
   * Description: Desc: When enabled, this adds a Search the course widget on the course outline and courseware [output truncated, see link for full description]

* +settings.ENABLE_COURSEWARE_SEARCH_FOR_COURSE_STAFF: `lms/envs/common.py (line 408) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L408>`_
   * Default value = False
   * Description: Desc: When enabled, this adds a Search the course widget on the course outline and courseware [output truncated, see link for full description]

* +settings.ENABLE_COURSEWARE_SEARCH_VERIFIED_REQUIRED: `lms/envs/common.py (line 681) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L681>`_
   * Default value = False
   * Description: Desc: When enabled, the courseware search feature will only be enabled [output truncated, see link for full description]

* +settings.ENABLE_COURSE_ASSESSMENT_GRADE_CHANGE_SIGNAL: `lms/envs/common.py (line 605)`_
   * Default value = False
   * Description: Desc: Set to True to start sending signals for assessment level grade updates. Notably, the only [output truncated, see link for full description]

* +settings.ENABLE_COURSE_DISCOVERY: `lms/envs/common.py (line 447) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L447>`_
   * Default value = False
   * Description: Desc: Add a course search widget to the LMS for searching courses. When this is enabled, the [output truncated, see link for full description]

* +settings.ENABLE_COURSE_FILENAME_CCX_SUFFIX: `lms/envs/common.py (line 460) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L460>`_
   * Default value = False
   * Description: Desc: If set to True, CCX ID will be included in the generated filename for CCX courses.

* +settings.ENABLE_COURSE_HOME_REDIRECT: `lms/envs/common.py (line 352) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L352>`_
   * Default value = True
   * Description: Desc: When enabled, along with the ENABLE_MKTG_SITE feature toggle, users who attempt to access a [output truncated, see link for full description]

* +settings.ENABLE_COURSE_SORTING_BY_START_DATE: `lms/envs/common.py (line 341) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L341>`_
   * Default value = True
   * Description: Desc: When a user goes to the homepage (‘/’) the user sees the courses listed in the [output truncated, see link for full description]

* +settings.ENABLE_CREDIT_ELIGIBILITY: `lms/envs/common.py (line 699) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L699>`_
   * Default value = True
   * Description: Desc: When enabled, it is possible to define a credit eligibility criteria in the CMS. A “Credit [output truncated, see link for full description]

* +settings.ENABLE_DASHBOARD_SEARCH: `lms/envs/common.py (line 421) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L421>`_
   * Default value = False
   * Description: Desc: When enabled, this adds a Search Your Courses widget on the dashboard page for searching [output truncated, see link for full description]

* +settings.ENABLE_DISCUSSION_EMAIL_DIGEST: `lms/envs/common.py (line 112) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L112>`_
   * Default value = False
   * Description: Desc: Set this to True if you want the discussion digest emails [output truncated, see link for full description]

* +settings.ENABLE_DISCUSSION_HOME_PANEL: `lms/envs/common.py (line 101) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L101>`_
   * Default value = True
   * Description: Desc: Hides or displays a welcome panel under the Discussion tab, which includes a subscription [output truncated, see link for full description]

* +settings.ENABLE_DJANGO_ADMIN_SITE: `lms/envs/common.py (line 138) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L138>`_
   * Default value = True
   * Description: Desc: Set to False if you want to disable Django’s admin site.

* +settings.ENABLE_EDXNOTES: `openedx/envs/common.py (line 772) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/envs/common.py#L772>`_
   * Default value = False
   * Description: Desc: This toggle enables the students to save and manage their annotations in the [output truncated, see link for full description]

* +settings.ENABLE_FOOTER_MOBILE_APP_LINKS: `lms/envs/common.py (line 375) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L375>`_
   * Default value = False
   * Description: Desc: Set to True if you want show the mobile app links (Apple App Store &amp; Google Play Store) in [output truncated, see link for full description]

* +settings.ENABLE_HIDE_FROM_TOC_UI: `cms/envs/common.py (line 237) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L237>`_
   * Default value = False
   * Description: Desc: When enabled, exposes hide_from_toc xblock attribute so course authors can configure it as

* +settings.ENABLE_HTML_XBLOCK_STUDENT_VIEW_DATA: `lms/envs/common.py (line 545) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L545>`_
   * Default value = False
   * Description: Desc: Whether HTML Block returns HTML content with the Course Blocks API when the API [output truncated, see link for full description]

* +settings.ENABLE_LOGIN_MICROFRONTEND: `lms/envs/common.py (line 239) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L239>`_
   * Default value = False
   * Description: Desc: Enable the login micro frontend.

* +settings.ENABLE_LTI_PII_ACKNOWLEDGEMENT: `cms/envs/common.py (line 204) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L204>`_
   * Default value = False
   * Description: Desc: Enables the lti pii acknowledgement feature for a course

* +settings.ENABLE_LTI_PROVIDER: `lms/envs/common.py (line 495) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L495>`_
   * Default value = False
   * Description: Desc: When set to True, Open edX site can be used as an LTI Provider to other systems [output truncated, see link for full description]

* +settings.ENABLE_MASQUERADE: `lms/envs/common.py (line 150) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L150>`_
   * Default value = True
   * Description: Desc: None

* +settings.ENABLE_MAX_FAILED_LOGIN_ATTEMPTS: `lms/envs/common.py (line 293) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L293>`_
   * Default value = True
   * Description: Desc: This feature will keep track of the number of failed login attempts on a given user’s [output truncated, see link for full description]

* +settings.ENABLE_NEW_BULK_EMAIL_EXPERIENCE: `lms/envs/common.py (line 637) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L637>`_
   * Default value = False
   * Description: Desc: When true, replaces the bulk email tool found on the [output truncated, see link for full description]

* +settings.ENABLE_ORA_USERNAMES_ON_DATA_EXPORT: `lms/envs/common.py (line 593) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L593>`_
   * Default value = False
   * Description: Desc: Set to True to add deanonymized usernames to ORA data [output truncated, see link for full description]

* +settings.ENABLE_SEND_XBLOCK_LIFECYCLE_EVENTS_OVER_BUS: `cms/envs/common.py (line 224) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L224>`_
   * Default value = False
   * Description: Desc: Enables sending xblock lifecycle events over the event bus. Used to create the [output truncated, see link for full description]

* +settings.ENABLE_SPECIAL_EXAMS: `lms/envs/common.py (line 486) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L486>`_
   * Default value = False
   * Description: Desc: Enable to use special exams, aka timed and proctored exams.

* +settings.ENABLE_STUDENT_HISTORY_VIEW: `lms/envs/common.py (line 200) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L200>`_
   * Default value = True
   * Description: Desc: This provides a UI to show a student’s submission history in a problem by the Staff Debug [output truncated, see link for full description]

* +settings.ENABLE_THIRD_PARTY_AUTH: `lms/envs/common.py (line 316) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L316>`_
   * Default value = False
   * Description: Desc: Turn on third-party auth. Disabled for now because full implementations are not yet [output truncated, see link for full description]

* +settings.ENABLE_UNICODE_USERNAME: `lms/envs/common.py (line 127) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L127>`_
   * Default value = False
   * Description: Desc: Set this to True to allow unicode characters in username. Enabling this will also [output truncated, see link for full description]

* +settings.ENABLE_XBLOCK_VIEW_ENDPOINT: `lms/envs/common.py (line 167) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L167>`_
   * Default value = False
   * Description: Desc: Enable an API endpoint, named “xblock_view”, to serve rendered XBlock views. This might be [output truncated, see link for full description]

* +settings.HIDE_DASHBOARD_COURSES_UNTIL_ACTIVATED: `lms/envs/common.py (line 190) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L190>`_
   * Default value = False
   * Description: Desc: When set, it hides the Courses list on the Learner Dashboard page if the learner has not [output truncated, see link for full description]

* +settings.IN_CONTEXT_DISCUSSION_ENABLED_DEFAULT: `cms/envs/common.py (line 247) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/cms/envs/common.py#L247>`_
   * Default value = True
   * Description: Desc: Set to False to disable in-context discussion for units by default.

* +settings.SEND_LEARNING_CERTIFICATE_LIFECYCLE_EVENTS_TO_BUS: `lms/envs/common.py (line 669) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L669>`_
   * Default value = False
   * Description: Desc: When True, the system will publish certificate lifecycle signals to the event bus. [output truncated, see link for full description]

* +settings.SKIP_EMAIL_VALIDATION: `lms/envs/common.py (line 248) <https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L248>`_
   * Default value = False
   * Description: Desc: Turn this on to skip sending emails for user validation. [output truncated, see link for full description]

Removed Feature Toggles
*************************
* -COOKIE_NAME_CHANGE_ACTIVATE: `openedx/core/djangoapps/cookie_metadata/middleware.py (line 60) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/openedx/core/djangoapps/cookie_metadata/middleware.py#L60>`_
   * Description: Desc: Used to enable CookieNameChange middleware which changes a cookie name in request.COOKIES

* -FEATURES['ALLOW_ADMIN_ENTERPRISE_COURSE_ENROLLMENT_DELETION']: `lms/envs/common.py (line 933) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L933>`_
   * Description: Desc: If true, allows for the deletion of EnterpriseCourseEnrollment records via Django Admin.

* -FEATURES['ALLOW_COURSE_RERUNS']: `cms/envs/common.py (line 309) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L309>`_
   * Description: Desc: This will allow staff member to re-run the course from the studio home page and will [output truncated, see link for full description]

* -FEATURES['ALLOW_EMAIL_ADDRESS_CHANGE']: `lms/envs/common.py (line 798) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L798>`_
   * Description: Desc: Allow users to change their email address on the Account Settings page. If this is [output truncated, see link for full description]

* -FEATURES['ALLOW_PUBLIC_ACCOUNT_CREATION']: `lms/envs/common.py (line 762) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L762>`_
   * Description: Desc: Allow public account creation. If this is disabled, users will no longer have access to [output truncated, see link for full description]

* -FEATURES['ALWAYS_REDIRECT_HOMEPAGE_TO_DASHBOARD_FOR_AUTHENTICATED_USER']: `lms/envs/common.py (line 487) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L487>`_
   * Description: Desc: When a logged in user goes to the homepage (‘/’) the user will be redirected to the [output truncated, see link for full description]

* -FEATURES['AUTOMATIC_AUTH_FOR_TESTING']: `lms/envs/common.py (line 348) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L348>`_
   * Description: Desc: Set to True to perform acceptance and load test. Auto auth view is responsible for load [output truncated, see link for full description]

* -FEATURES['AUTOMATIC_VERIFY_STUDENT_IDENTITY_FOR_TESTING']: `lms/envs/common.py (line 402) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L402>`_
   * Description: Desc: If set to True, then we want to skip posting anything to Software Secure. Bypass posting [output truncated, see link for full description]

* -FEATURES['BADGES_ENABLED']: `cms/envs/common.py (line 559) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L559>`_
   * Description: Desc: Set to True to enable the Badges feature.

* -FEATURES['CERTIFICATES_HTML_VIEW']: `lms/envs/common.py (line 630) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L630>`_
   * Description: Desc: Set to True to enable course certificates on your instance of Open edX.

* -FEATURES['COURSES_ARE_BROWSABLE']: `lms/envs/common.py (line 252) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L252>`_
   * Description: Desc: When this is set to True, all the courses will be listed on the /courses page and Explore [output truncated, see link for full description]

* -FEATURES['CUSTOM_CERTIFICATE_TEMPLATES_ENABLED']: `lms/envs/common.py (line 643) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L643>`_
   * Description: Desc: Set to True to enable custom certificate templates which are configured via Django admin.

* -FEATURES['DEPRECATE_OLD_COURSE_KEYS_IN_STUDIO']: `cms/envs/common.py (line 432) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L432>`_
   * Description: Desc: Warn about removing support for deprecated course keys. [output truncated, see link for full description]

* -FEATURES['DISABLE_ADVANCED_SETTINGS']: `cms/envs/common.py (line 517) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L517>`_
   * Description: Desc: Set to `True` to disable the advanced settings page in Studio for all users except those [output truncated, see link for full description]

* -FEATURES['DISABLE_ALLOWED_ENROLLMENT_IF_ENROLLMENT_CLOSED']: `lms/envs/common.py (line 1022) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L1022>`_
   * Description: Desc: Set to True to disable enrollment for user invited to a course

* -FEATURES['DISABLE_COURSE_CREATION']: `cms/envs/common.py (line 448) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L448>`_
   * Description: Desc: If set to True, it disables the course creation functionality and hides the “New Course” [output truncated, see link for full description]

* -FEATURES['DISABLE_HONOR_CERTIFICATES']: `lms/envs/common.py (line 336) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L336>`_
   * Description: Desc: Set to True to disable honor certificates. Typically used when your installation only [output truncated, see link for full description]

* -FEATURES['DISABLE_LOGIN_BUTTON']: `lms/envs/common.py (line 217) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L217>`_
   * Description: Desc: Removes the display of the login button in the navigation bar. [output truncated, see link for full description]

* -FEATURES['DISABLE_MOBILE_COURSE_AVAILABLE']: `cms/envs/common.py (line 386) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L386>`_
   * Description: Desc: Set to True to remove Mobile Course Available UI Flag from Studio’s Advanced Settings [output truncated, see link for full description]

* -FEATURES['DISABLE_START_DATES']: `lms/envs/common.py (line 123) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L123>`_
   * Description: Desc: When True, all courses will be active, regardless of start [output truncated, see link for full description]

* -FEATURES['DISABLE_UNENROLLMENT']: `cms/envs/common.py (line 505) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L505>`_
   * Description: Desc: Set to True to disable self-unenrollments via REST API. [output truncated, see link for full description]

* -FEATURES['DISPLAY_DEBUG_INFO_TO_STAFF']: `lms/envs/common.py (line 100) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L100>`_
   * Description: Desc: Add a “Staff Debug” button to course blocks for debugging [output truncated, see link for full description]

* -FEATURES['DISPLAY_HISTOGRAMS_TO_STAFF']: `lms/envs/common.py (line 110) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L110>`_
   * Description: Desc: This displays histograms in the Staff Debug Info panel to course staff.

* -FEATURES['EDITABLE_SHORT_DESCRIPTION']: `cms/envs/common.py (line 234) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L234>`_
   * Description: Desc: This feature flag allows editing of short descriptions on the Schedule &amp; Details page in [output truncated, see link for full description]

* -FEATURES['EMBARGO']: `lms/envs/common.py (line 444) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L444>`_
   * Description: Desc: Turns on embargo functionality, which blocks users from [output truncated, see link for full description]

* -FEATURES['ENABLE_ACCOUNT_DELETION']: `lms/envs/common.py (line 848) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L848>`_
   * Description: Desc: Whether to display the account deletion section on Account Settings page. Set to False to [output truncated, see link for full description]

* -FEATURES['ENABLE_ANNOUNCEMENTS']: `openedx/features/announcements/settings/common.py (line 5) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/openedx/features/announcements/settings/common.py#L5>`_
   * Description: Desc: This feature can be enabled to show system wide announcements [output truncated, see link for full description]

* -FEATURES['ENABLE_AUTHN_MICROFRONTEND']: `lms/envs/common.py (line 872) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L872>`_
   * Description: Desc: Supports staged rollout of a new micro-frontend-based implementation of the logistration.

* -FEATURES['ENABLE_BULK_ENROLLMENT_VIEW']: `lms/envs/common.py (line 808) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L808>`_
   * Description: Desc: When set to True the bulk enrollment view is enabled and one can use it to enroll multiple [output truncated, see link for full description]

* -FEATURES['ENABLE_BULK_USER_RETIREMENT']: `lms/envs/common.py (line 942) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L942>`_
   * Description: Desc: Set to True to enable bulk user retirement through REST API. This is disabled by [output truncated, see link for full description]

* -FEATURES['ENABLE_CERTIFICATES_IDV_REQUIREMENT']: `lms/envs/common.py (line 1012) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L1012>`_
   * Description: Desc: Whether to enforce ID Verification requirements for course certificates generation

* -FEATURES['ENABLE_CHANGE_USER_PASSWORD_ADMIN']: `cms/envs/common.py (line 396) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L396>`_
   * Description: Desc: Set to True to enable changing a user password through django admin. This is disabled by [output truncated, see link for full description]

* -FEATURES['ENABLE_COMBINED_LOGIN_REGISTRATION_FOOTER']: `lms/envs/common.py (line 523) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L523>`_
   * Description: Desc: Display the standard footer in the login page. This feature can be overridden by a site- [output truncated, see link for full description]

* -FEATURES['ENABLE_CONTENT_LIBRARIES_LTI_TOOL']: `cms/envs/common.py (line 281) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L281>`_
   * Description: Desc: When set to True, Content Libraries in [output truncated, see link for full description]

* -FEATURES['ENABLE_COOKIE_CONSENT']: `lms/envs/common.py (line 781) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L781>`_
   * Description: Desc: Enable header banner for cookie consent using this service: [output truncated, see link for full description]

* -FEATURES['ENABLE_COSMETIC_DISPLAY_PRICE']: `lms/envs/common.py (line 391) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L391>`_
   * Description: Desc: Enable the display of “cosmetic_display_price”, set in a course advanced settings. This [output truncated, see link for full description]

* -FEATURES['ENABLE_COURSEWARE_SEARCH']: `lms/envs/common.py (line 579) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L579>`_
   * Description: Desc: When enabled, this adds a Search the course widget on the course outline and courseware [output truncated, see link for full description]

* -FEATURES['ENABLE_COURSEWARE_SEARCH_FOR_COURSE_STAFF']: `lms/envs/common.py (line 592) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L592>`_
   * Description: Desc: When enabled, this adds a Search the course widget on the course outline and courseware [output truncated, see link for full description]

* -FEATURES['ENABLE_COURSEWARE_SEARCH_VERIFIED_REQUIRED']: `lms/envs/common.py (line 1053) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L1053>`_
   * Description: Desc: When enabled, the courseware search feature will only be enabled [output truncated, see link for full description]

* -FEATURES['ENABLE_COURSE_ASSESSMENT_GRADE_CHANGE_SIGNAL']: `lms/envs/common.py (line 922) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L922>`_
   * Description: Desc: Set to True to start sending signals for assessment level grade updates. Notably, the only [output truncated, see link for full description]

* -FEATURES['ENABLE_COURSE_DISCOVERY']: `lms/envs/common.py (line 654) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L654>`_
   * Description: Desc: Add a course search widget to the LMS for searching courses. When this is enabled, the [output truncated, see link for full description]

* -FEATURES['ENABLE_COURSE_FILENAME_CCX_SUFFIX']: `lms/envs/common.py (line 667) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L667>`_
   * Description: Desc: If set to True, CCX ID will be included in the generated filename for CCX courses.

* -FEATURES['ENABLE_COURSE_HOME_REDIRECT']: `lms/envs/common.py (line 509) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L509>`_
   * Description: Desc: When enabled, along with the ENABLE_MKTG_SITE feature toggle, users who attempt to access a [output truncated, see link for full description]

* -FEATURES['ENABLE_COURSE_SORTING_BY_START_DATE']: `lms/envs/common.py (line 498) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L498>`_
   * Description: Desc: When a user goes to the homepage (‘/’) the user sees the courses listed in the [output truncated, see link for full description]

* -FEATURES['ENABLE_CREDIT_ELIGIBILITY']: `lms/envs/common.py (line 3659)`_
   * Description: Desc: When enabled, it is possible to define a credit eligibility criteria in the CMS. A “Credit [output truncated, see link for full description]

* -FEATURES['ENABLE_CSMH_EXTENDED']: `lms/envs/common.py (line 741) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L741>`_
   * Description: Desc: Write Courseware Student Module History (CSMH) to the extended table: this logs all [output truncated, see link for full description]

* -FEATURES['ENABLE_DASHBOARD_SEARCH']: `lms/envs/common.py (line 605)`_
   * Description: Desc: When enabled, this adds a Search Your Courses widget on the dashboard page for searching [output truncated, see link for full description]

* -FEATURES['ENABLE_DISCUSSION_EMAIL_DIGEST']: `lms/envs/common.py (line 171) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L171>`_
   * Description: Desc: Set this to True if you want the discussion digest emails [output truncated, see link for full description]

* -FEATURES['ENABLE_DISCUSSION_HOME_PANEL']: `lms/envs/common.py (line 160) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L160>`_
   * Description: Desc: Hides or displays a welcome panel under the Discussion tab, which includes a subscription [output truncated, see link for full description]

* -FEATURES['ENABLE_DISCUSSION_SERVICE']: `lms/envs/common.py (line 136) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L136>`_
   * Description: Desc: When True, it will enable the Discussion tab in courseware for all courses. Setting this [output truncated, see link for full description]

* -FEATURES['ENABLE_DJANGO_ADMIN_SITE']: `lms/envs/common.py (line 197) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L197>`_
   * Description: Desc: Set to False if you want to disable Django’s admin site.

* -FEATURES['ENABLE_EDXNOTES']: `lms/envs/common.py (line 549) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L549>`_
   * Description: Desc: This toggle enables the students to save and manage their annotations in the [output truncated, see link for full description]

* -FEATURES['ENABLE_FOOTER_MOBILE_APP_LINKS']: `lms/envs/common.py (line 536) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L536>`_
   * Description: Desc: Set to True if you want show the mobile app links (Apple App Store &amp; Google Play Store) in [output truncated, see link for full description]

* -FEATURES['ENABLE_GRADING_METHOD_IN_PROBLEMS']: `cms/envs/common.py (line 550) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L550>`_
   * Description: Desc: Enables the grading method feature in capa problems.

* -FEATURES['ENABLE_HELP_LINK']: `cms/envs/common.py (line 460) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L460>`_
   * Description: Desc: When True, a help link is displayed on the main navbar. Set False to hide it.

* -FEATURES['ENABLE_HIDE_FROM_TOC_UI']: `cms/envs/common.py (line 540) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L540>`_
   * Description: Desc: When enabled, exposes hide_from_toc xblock attribute so course authors can configure it as

* -FEATURES['ENABLE_HTML_XBLOCK_STUDENT_VIEW_DATA']: `lms/envs/common.py (line 821) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L821>`_
   * Description: Desc: Whether HTML Block returns HTML content with the Course Blocks API when the API [output truncated, see link for full description]

* -FEATURES['ENABLE_INTEGRITY_SIGNATURE']: `cms/envs/common.py (line 470) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L470>`_
   * Description: Desc: Whether to replace ID verification course/certificate requirement

* -FEATURES['ENABLE_LOGIN_MICROFRONTEND']: `lms/envs/common.py (line 372) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L372>`_
   * Description: Desc: Enable the login micro frontend.

* -FEATURES['ENABLE_LTI_PII_ACKNOWLEDGEMENT']: `cms/envs/common.py (line 482) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L482>`_
   * Description: Desc: Enables the lti pii acknowledgement feature for a course

* -FEATURES['ENABLE_LTI_PROVIDER']: `lms/envs/common.py (line 702) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L702>`_
   * Description: Desc: When set to True, Open edX site can be used as an LTI Provider to other systems [output truncated, see link for full description]

* -FEATURES['ENABLE_MASQUERADE']: `lms/envs/common.py (line 209) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L209>`_
   * Description: Desc: None

* -FEATURES['ENABLE_MAX_FAILED_LOGIN_ATTEMPTS']: `lms/envs/common.py (line 426) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L426>`_
   * Description: Desc: This feature will keep track of the number of failed login attempts on a given user’s [output truncated, see link for full description]

* -FEATURES['ENABLE_MKTG_SITE']: `lms/envs/common.py (line 474) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L474>`_
   * Description: Desc: Toggle to enable alternate urls for marketing links.

* -FEATURES['ENABLE_NEW_BULK_EMAIL_EXPERIENCE']: `lms/envs/common.py (line 975) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L975>`_
   * Description: Desc: When true, replaces the bulk email tool found on the [output truncated, see link for full description]

* -FEATURES['ENABLE_OAUTH2_PROVIDER']: `lms/envs/common.py (line 226) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L226>`_
   * Description: Desc: Enable this feature to allow this Open edX platform to be an OAuth2 authentication [output truncated, see link for full description]

* -FEATURES['ENABLE_ORA_ALL_FILE_URLS']: `cms/envs/common.py (line 406) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L406>`_
   * Description: Desc: A “work-around” feature toggle meant to help in cases where some file uploads are not [output truncated, see link for full description]

* -FEATURES['ENABLE_ORA_USERNAMES_ON_DATA_EXPORT']: `lms/envs/common.py (line 910) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L910>`_
   * Description: Desc: Set to True to add deanonymized usernames to ORA data [output truncated, see link for full description]

* -FEATURES['ENABLE_ORA_USER_STATE_UPLOAD_DATA']: `cms/envs/common.py (line 420) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L420>`_
   * Description: Desc: A “work-around” feature toggle meant to help in cases where some file uploads are not [output truncated, see link for full description]

* -FEATURES['ENABLE_PASSWORD_RESET_FAILURE_EMAIL']: `lms/envs/common.py (line 833) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L833>`_
   * Description: Desc: Whether to send an email for failed password reset attempts or not. This happens when a [output truncated, see link for full description]

* -FEATURES['ENABLE_SEND_XBLOCK_LIFECYCLE_EVENTS_OVER_BUS']: `cms/envs/common.py (line 527) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L527>`_
   * Description: Desc: Enables sending xblock lifecycle events over the event bus. Used to create the [output truncated, see link for full description]

* -FEATURES['ENABLE_SPECIAL_EXAMS']: `lms/envs/common.py (line 693) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L693>`_
   * Description: Desc: Enable to use special exams, aka timed and proctored exams.

* -FEATURES['ENABLE_STUDENT_HISTORY_VIEW']: `lms/envs/common.py (line 284) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L284>`_
   * Description: Desc: This provides a UI to show a student’s submission history in a problem by the Staff Debug [output truncated, see link for full description]

* -FEATURES['ENABLE_TEXTBOOK']: `lms/envs/common.py (line 149) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L149>`_
   * Description: Desc: Add PDF and HTML textbook tabs to the courseware.

* -FEATURES['ENABLE_THIRD_PARTY_AUTH']: `lms/envs/common.py (line 463) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L463>`_
   * Description: Desc: Turn on third-party auth. Disabled for now because full implementations are not yet [output truncated, see link for full description]

* -FEATURES['ENABLE_UNICODE_USERNAME']: `lms/envs/common.py (line 186) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L186>`_
   * Description: Desc: Set this to True to allow unicode characters in username. Enabling this will also [output truncated, see link for full description]

* -FEATURES['ENABLE_XBLOCK_VIEW_ENDPOINT']: `lms/envs/common.py (line 237) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L237>`_
   * Description: Desc: Enable an API endpoint, named “xblock_view”, to serve rendered XBlock views. This might be [output truncated, see link for full description]

* -FEATURES['HIDE_DASHBOARD_COURSES_UNTIL_ACTIVATED']: `lms/envs/common.py (line 274) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L274>`_
   * Description: Desc: When set, it hides the Courses list on the Learner Dashboard page if the learner has not [output truncated, see link for full description]

* -FEATURES['IN_CONTEXT_DISCUSSION_ENABLED_DEFAULT']: `cms/envs/common.py (line 567) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/envs/common.py#L567>`_
   * Description: Desc: Set to False to disable in-context discussion for units by default.

* -FEATURES['LICENSING']: `lms/envs/common.py (line 620) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L620>`_
   * Description: Desc: Toggle platform-wide course licensing. The course.license attribute is then used to append [output truncated, see link for full description]

* -FEATURES['RESTRICT_AUTOMATIC_AUTH']: `lms/envs/common.py (line 360) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L360>`_
   * Description: Desc: Prevent auto auth from creating superusers or modifying existing users. Auto auth is a [output truncated, see link for full description]

* -FEATURES['SEND_LEARNING_CERTIFICATE_LIFECYCLE_EVENTS_TO_BUS']: `lms/envs/common.py (line 1032) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L1032>`_
   * Description: Desc: When True, the system will publish certificate lifecycle signals to the event bus. [output truncated, see link for full description]

* -FEATURES['SHOW_FOOTER_LANGUAGE_SELECTOR']: `lms/envs/common.py (line 731) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L731>`_
   * Description: Desc: When set to True, language selector will be visible in the footer.

* -FEATURES['SHOW_HEADER_LANGUAGE_SELECTOR']: `lms/envs/common.py (line 715) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L715>`_
   * Description: Desc: When set to True, language selector will be visible in the header.

* -FEATURES['SHOW_REGISTRATION_LINKS']: `lms/envs/common.py (line 772) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L772>`_
   * Description: Desc: Allow registration links. If this is disabled, users will no longer see buttons to the [output truncated, see link for full description]

* -FEATURES['SKIP_EMAIL_VALIDATION']: `lms/envs/common.py (line 381) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/lms/envs/common.py#L381>`_
   * Description: Desc: Turn this on to skip sending emails for user validation. [output truncated, see link for full description]

* -SEND_CATALOG_INFO_SIGNAL: `cms/djangoapps/contentstore/signals/handlers.py (line 74) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/signals/handlers.py#L74>`_
   * Description: Desc: When True, sends to catalog-info-changed signal when course_published occurs. [output truncated, see link for full description]

* -contentstore.new_studio_mfe.use_new_files_uploads_page: `cms/djangoapps/contentstore/toggles.py (line 373) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L373>`_
   * Description: Desc: This flag enables the use of the new studio files and uploads page mfe

* -discussions.enable_forum_v2: `openedx/core/djangoapps/discussions/config/waffle.py (line 49) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/openedx/core/djangoapps/discussions/config/waffle.py#L49>`_
   * Description: Desc: Waffle flag to use the forum v2 instead of v1(cs_comment_service)

* -legacy_studio.files_uploads: `cms/djangoapps/contentstore/toggles.py (line 354) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L354>`_
   * Description: Desc: Temporarily fall back to the old Studio Files &amp; Uploads page.

* -legacy_studio.home: `cms/djangoapps/contentstore/toggles.py (line 184) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L184>`_
   * Description: Desc: Temporarily fall back to the old Studio logged-in landing page.

* -legacy_studio.text_editor: `cms/djangoapps/contentstore/toggles.py (line 89) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/cms/djangoapps/contentstore/toggles.py#L89>`_
   * Description: Desc: Temporarily fall back to the old Text component (a.k.a. html block) editor.

* -notifications.enable_notification_grouping: `openedx/core/djangoapps/notifications/config/waffle.py (line 42) <https://github.com/openedx/edx-platform/blob/b0588452088a6dd48e865f51d27e8d0e6f609bdc/openedx/core/djangoapps/notifications/config/waffle.py#L42>`_
   * Description: Desc: Waffle flag to enable the Notifications Grouping feature

* -notifications.enable_ora_grade_notifications: `openedx/core/djangoapps/notifications/config/waffle.py (line 32)`_
   * Description: Desc: Waffle flag to enable ORA grade notifications


Known Issues
************

See the `Build Test Release project board <https://github.com/orgs/openedx/projects/28>`_ for known open issues.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|  Dec  2025   |  BTR                          |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+

.. _lms/envs/common.py (line 3659): https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L3659
.. _lms/envs/common.py (line 605): https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/lms/envs/common.py#L605
.. _openedx/core/djangoapps/notifications/config/waffle.py (line 32): https://github.com/openedx/edx-platform/blob/cf48323639bf24eed5ef120dfbd9e98cf0fd64af/openedx/core/djangoapps/notifications/config/waffle.py#L32