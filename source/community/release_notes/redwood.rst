Open edX Redwood Release
########################

These are the release notes for the Redwood release, the 18th community release of the Open edX Platform, spanning changes from October 10 2023 to May 09 2024.  You can also review details about `earlier releases`_ or learn more about the `Open edX Platform`_.

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
****************


Learner Experiences
*******************


Instructor Experiences
**********************


Administrators & Operators
**************************

Settings and Toggles
====================

Waffle flags:

contentstore.new_studio_mfe.use_new_advanced_settings_page
contentstore.new_studio_mfe.use_new_certificates_page
contentstore.new_studio_mfe.use_new_course_outline_page
contentstore.new_studio_mfe.use_new_course_team_page
contentstore.new_studio_mfe.use_new_custom_pages
contentstore.new_studio_mfe.use_new_export_page
contentstore.new_studio_mfe.use_new_files_uploads_page
contentstore.new_studio_mfe.use_new_grading_page
contentstore.new_studio_mfe.use_new_group_configurations_page
contentstore.new_studio_mfe.use_new_import_page
contentstore.new_studio_mfe.use_new_schedule_details_page
contentstore.new_studio_mfe.use_new_textbooks_page
contentstore.new_studio_mfe.use_new_unit_page (disabled)
contentstore.new_studio_mfe.use_new_updates_page
contentstore.new_studio_mfe.use_new_video_uploads_page (disabled)
new_studio_mfe.use_new_home_page
new_studio_mfe.use_tagging_taxonomy_list_page
contentstore.enable_copy_paste_units

Course authoring MFE config:

ENABLE_UNIT_PAGE: "false"
ENABLE_NEW_EDITOR_PAGES: "true"
ENABLE_TAGGING_TAXONOMY_PAGES: "true"
ENABLE_ASSETS_PAGE: "true"
ENABLE_HOME_PAGE_COURSE_API_V2: "true"

Other Operator Changes
======================

-  The default minimum password length has been updated from 2
   characters to 8 characters. `(PR) <https://github.com/openedx/edx-platform/pull/33373>` _.

   -  If you have an existing password, this change along will not
      force you to update it. However if you reset your password or go
      to change it, you'll have to conform to the new guidelines. If you
      would like to force people to update their password, you'll
      probably want to take a look at .. _the password_policy plugin and its settings: https://github.com/openedx/edx-platform/blob/2033dcf6ace133719aaeb72dc5dd6ee521a7ac42/openedx/core/djangoapps/password_policy/settings/common.py#L13 .*

-  Deployers must ensure that their
   ``JWT_AUTH['JWT_PRIVATE_SIGNING_JWK']`` Django setting in LMS
   contains the full complement of private key numbers.*

   -  **Background:**\ *In LMS, we are switching from the pyjwkest
      library to PyJWT for signing JWTs. (pyjwkest is now unmaintained.)
      However, PyJWT has stricter requirements for the private key in
      ``JWT_PRIVATE_SIGNING_JWK``. Before you upgrade to Redwood, you
      will need to update this key using a script. Otherwise, JWT
      signing will fail, and users will be unable to log in.*

   -  **Steps:**

      1. Locate ``JWT_PRIVATE_SIGNING_JWK`` in your deployment
         configuration.*

      2. Check if the JSON contains all of the following params: ``p``,
         ``q``, ``dp``, ``dq``, and ``qi``. If it does, you don’t need
         to do anything further. Otherwise, continue.*

      3. In your edx-platform virtualenv, run
         ``python3 scripts/jwk-precompute-params.py`` and follow the
         prompts. (It will ask you to paste in the current JSON.)*

      4. Update your config’s ``JWT_AUTH['JWT_PRIVATE_SIGNING_JWK']``
         with the output of the script.*

      5. You may wish to compare the contents of the private key before
         and after running the script, and verify that the only changes
         it has made to the contents of the JSON are that the ``p``,
         ``q``, ``dp``, ``dq``, and ``qi`` params have been added. (Some
         or all may already have been present.)*

   -  **Notes:**

      1. This should be done while you are still running Quince—it is
         safe to do ahead of the upgrade, and should not have any
         visible effect at that time.*

      2. This key must be handled very carefully. Anyone in possession
         of the key may impersonate users.*

-  The following `requirements update <https://github.com/openedx/credentials/commit/1cd7c25c04a955aa9aaa263fb40ebd3f73d0937e>` _ into credentials might have implications for anyone
   who has a massive ``usersocialauth`` table.  This is because that
   table grows endlessly, and the migrations on the table caused by
   updating the ``social-auth-app-django`` package can run out of
   memory. If maintainers have migration failures on this upgrade, they
   should run the management command `truncate_social_auth <https://github.com/openedx/credentials/blob/master/credentials/apps/core/management/commands/truncate_social_auth.py>` _.*

   -  This will remove all entries from the ``usersocialauth`` table
      that haven't been updated in 90 days, which makes the size of the
      table tractable for the dependency's migration. This is harmless
      in the ``Credentials`` IDA.*

-  The scripts related to user retirement across all services
   have been moved to the ``edx-platform`` repository. If you’ve been
   using the \`tubular repo to run retirement scripts you should update
   your code.*

   -  *Relevant Tickets*
      - `Move user retirement code to edx-platform and drop it from Tubular <https://github.com/openedx/axim-engineering/issues/881>`_.
      - `Move user retirement scripts code from the tubular repo <https://github.com/openedx/edx-platform/pull/34063>`_.
      - `Deprecate User Retirement Scripts <https://github.com/openedx-unsupported/tubular/pull/736>`_.

-  *edx-platform and cs_comment_service Mongo Upgrades*
      - `chore: add mongo 7 to testing matrix <https://github.com/openedx/edx-platform/pull/34213>`_.
      - `build: Build with newer ruby and mongo versions. <https://github.com/openedx/cs_comments_service/pull/426>`_.

-  The Redwood release includes the `Studio Course Search [BETA] <https://openedx.atlassian.net/wiki/spaces/OEPM/pages/4247257093/BETA+Course+Search+-+Product+Release+Notes>` _, which is disabled by default
   as it depends on a new search engine, Meilisearch. We encourage
   operators to install Meilisearch, test out this feature, and give us
   feedback on the viability of using Meilisearch as a replacement for
   Elasticsearch in future releases of Open edX. Here’s how:*

   -  For tutor-based deployments, install the `tutor-contrib-mailsearch <https://github.com/open-craft/tutor-contrib-meilisearch>`_ plugin, and apply the
      changes to your deployment. See that plugin’s README for details.
      Note in particular that the hostname configured as
      ``MEILISEARCH_PUBLIC_HOST`` must be resolvable on the public
      internet.*

   -  If you are not using Tutor, you’ll need to install Meilisearch
      manually (or use the cloud product), and to explicitly set `the related config variables <https://github.com/openedx/edx-platform/blob/aac70563fd8a1492af25ae1b9aa9d14c42b36a18/cms/envs/common.py#L2958-L2969>`_ in the
      CMS as well as set ``MEILISEARCH_ENABLED=true`` in the Course
      Authoring MFE settings.*

   -  To create and populate the search index, you must run a one-time
      command from the CMS shell:
      ``python manage.py cms reindex_studio --experimental``. This
      command may take a while if you have a lot of courses and/or
      libraries in Studio; it will display regular progress indicators
      while it is running. We are interested in hearing how long it
      takes for you - please share your experience (see next bullet).
      This command reads from MySQL/MongoDB but does not write to them;
      it only writes to Meilisearch. Once the indexing has completed, it
      should not be necessary to run it again; from that point forward,
      the indexes will be updated automatically as needed.*

   -  Please share your feedback about Meilisearch, indexing, and
      operations in `this Discourse thread <https://discuss.openedx.org/t/is-meilisearch-a-viable-upgrade-alternative-to-opensearch/12400>`_ or the `#ops <https://openedx.slack.com/archives/C08B4LZEZ>`_ Slack channel. Please share feedback about
      the new course search feature in general `in the discussion forums <https://discuss.openedx.org/t/feedback-thread-new-course-search/13076>`_ or in the `#wg-product-core <https://openedx.slack.com/archives/C057J2D1WU9>`_ Slack channel.*


Deprecations & Removals
***********************

-  *Badges app has been deprecated and removed from ``edx-platform``.
   See `[DEPR]: lms/djangoapps/badges <https://github.com/openedx/edx-platform/issues/31541>`_ .*

   -  *``accomplishments_shared`` field is removed from payloads and
      settings*

   -  *``ENABLE_OPENBADGES`` is no longer available for configuration in
      ``FEATURES``*

   -  *``BADGING_BACKEND``, ``BADGR_BASE_URL``, ``BADGR_ISSUER_SLUG``,
      ``BADGR_USERNAME``, ``BADGR_PASSWORD``,
      ``BADGR_TOKENS_CACHE_KEY``, ``BADGR_TIMEOUT``,
      ``BADGR_ENABLE_NOTIFICATIONS`` are also not configurable anymore.*

-  * In edxapp, the Waffle switch ``ip.legacy`` is removed. See `[DEPR]: legacy_ip code and Waffle switch <https://github.com/openedx/edx-platform/issues/33733>`_ .*

   -  *Any deployment that has been relying on this legacy IP address
      option will need to switch to setting
      ``CLOSEST_CLIENT_IP_FROM_HEADERS`` appropriately. See `Nutmeg Announcement <https://openedx.atlassian.net/wiki/spaces/COMM/pages/3205201949>`_ for
      details.*

-  *Asset Processing (webpack, collectstatic, etc.) using Paver Commands in edx-platform is now Deprecated and will not be available in Sumac*
   - `[DEPR]: Asset processing in Paver <https://github.com/openedx/edx-platform/issues/31895>`_.
   -  *This should cover everything that a site operator needs to do as a part of deployment.*
   -  *Non deployment paver commands will be removed by Sumac*

-  *The django-splash capability was removed from edx-platform and the
   relevant code has been archived.*
   - https://github.com/openedx/public-engineering/issues/224

Developer Experience
********************

Researcher & Data Experiences
*****************************


Known Issues
************
