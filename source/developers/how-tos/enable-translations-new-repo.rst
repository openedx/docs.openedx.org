Enabling Translations on a New Repo
###################################

.. contents::
 :local:
 :depth: 2

Quickstart
**********

To enable translations on a new repository according to the :ref:`openedx-proposals:OEP-58 Translations Management`:

- Start from an up-to-date cookiecutter (`frontend-template-application`_ for Micro-frontends, `edx-cookiecutters`_
  for Python)
- Configure the repository according to the appropriate section later in this document.

.. seealso::
  :doc:`/developers/concepts/oep58`

Configuration
*************

Python Django Plugins and XBlocks
=================================

To include a non-microservice Python repository (such as an XBlock, Open edX plugin, or library) in the translations
workflow:

#. Ensure your repository's Makefile has ``extract_translations``.

   If you are creating a new repository, use the `edx-cookiecutters`_ templates such as ``django-app`` or ``xblock``.

   For existing repos which don't have the ``make extract_translations`` command, it can be copied from the
   `edx-cookiecutters`_ Makefile in the corresponding template e.g. ``cookiecutter-xblock`` Makefile for XBlocks.

   .. note::

     Some repositories use ``django-manage makemessages``. The recommendation is to use ``i18n_tool extract``
     because it provides more options and cleans ``.po`` files.

#. Run ``make extract_translations``. Verify it extracts files to the ``my_xblock_module/conf/locale``
   directory. The ``.po`` filenames will vary depending on the use case:

   - XBlocks: ``text.po``
   - Django plugins: ``django.po``
   - If the repo uses ``gettext`` and has a ``static`` directory with JavaScript, it may include ``djangojs.po``

#. If you need JavaScript translations in your XBlock, use ``XBlockI18NService.get_javascript_i18n_catalog_url``. You can find an example of this in ``_get_statici18n_js_url`` in  ``xblock-drag-and-drop-v2/`` `here <https://github.com/openedx/xblock-drag-and-drop-v2/blob/3900a4eba5befbbaea636c5e256aaabcd985e64d/drag_and_drop_v2/drag_and_drop_v2.py#L343-L349>`_. Note: this requires `XBlock 1.9.1`_ or newer, and edx-platform Redwood or newer.

#. Add the repository to `extract-translation-source-files.yml`_ in the `openedx-translations repo`_.

   Add a new entry under the ``setup-matrix`` section. For example, the XBlock located at
   ``https://github.com/openedx/xblock-drag-and-drop-v2`` should have the following entry::

    const allPythonRepos = [
        ...
        'xblock-drag-and-drop-v2',
        ...
    ]


#. Add the repository to the `transifex.yml`_ file in the `openedx-translations repo`_.
   Copy the `Drag and Drop XBlock transifex.yml entry`_ and modify it to match the new repository.

#. Create a draft pull request in the `openedx-translations repo`_

#. Follow the instructions in the :ref:`testing-in-your-fork` section to verify new repository configuration.

#. Mark your pull request as ready for review and wait for it to be merged.

#. Verify the workflow is syncing the translations properly as described in the :ref:`debugging-translations` section.

#. Install the XBlock or plugin in your local `Tutor`_ environment. Run
   ``make pull_translations`` in the ``edx-platform`` repo to preview the translations.


Django Microservice Repos (IDAs)
================================

The terms "Microservice" and "Independently Deployable Application (IDA)" are used interchangeably throughout the Open
edX project. There are many Django microservices in the Open edX ecosystem, such as:

- `edx-platform`_
- `credentials`_
- `ecommerce`_
- `course-discovery`_

To include a Microservice Python repository in the translations workflow:

#. Ensure your repository's Makefile has ``extract_translations`` and ``pull_translations``.

   If you are creating a new repository, use the `cookiecutter-django-ida`_
   template.

   For existing repos which don't have the ``make extract_translations`` or
   ``make pull_translations`` command, they can be copied from the
   `edx-cookiecutters`_ Makefile in the ``cookiecutter-django-ida`` Makefile for Microservices.

#. Run ``make extract_translations``. Verify it extracts both ``django.po`` and ``djangojs.po``
   files into the ``conf/locale`` directory.

#. Add the repository to `extract-translation-source-files.yml`_ in the `openedx-translations repo`_.

   Add a new entry under the ``setup-matrix`` section. For example for the `credentials`_ repo it should have
   the following entry::

    const allPythonRepos = [
        ...
        'credentials',
        ...
    ]

#. Create a draft pull request in the `openedx-translations repo`_

#. Follow the instructions in the :ref:`testing-in-your-fork` section to verify the new repository configuration.

#. Mark your pull request as ready for review and wait for it to be merged.

#. Verify the workflow is syncing the translations properly as described in the :ref:`debugging-translations` section.

#. Run ``make pull_translations`` to verify translations are pulled from the
   `openedx-translations repo`_ into the ``conf/locale`` directory. To generate JavaScript translation
   files you will likely also need to run ``make static``/``make static.dev``.

React Repos
===========

To include a React repository in the translations workflow:

#. Ensure your repository's Makefile has ``extract_translations`` and ``pull_translations``.

   If you are creating a new repository, use `frontend-template-application`_.

   For existing repos which don't have the ``make extract_translations`` or
   ``make pull_translations`` command, they can be copied from the
   `frontend-template-application Makefile`_.

   The ``make pull_translations`` command should accept a ``ATLAS_OPTIONS`` environment variable. This is used to
   pass options to the ``atlas pull`` command during build processes like `Tutor MFE Docker build`_.

#. Run ``make extract_translations``. Verify that it creates ``src/i18n/transifex_input.json``. This file should be
   excluded from the repo via the ``.gitignore`` file.

#. Add the repository to `extract-translation-source-files.yml`_ in the `openedx-translations repo`_.

   Add a new entry under the ``setup-matrix`` section. For example for the `frontend-app-learning`_ repo
   should have the following entry::

    const allJavascriptRepos = [
        ...
        'frontend-app-learning',
        ...
    ]

#. Create a draft pull request in the `openedx-translations repo`_

#. Follow the instructions in the :ref:`testing-in-your-fork` section to verify the new repository configuration.

#. Mark your pull request as ready for review and wait for it to be merged.

#. Verify the workflow is syncing the translations properly as described in the :ref:`debugging-translations` section.

.. note::

  While deploying or building the micro-frontend, ensure ``make pull_translations`` is ran before ``npm build`` in
  order to include updated translations in final micro-frontend build.


Testing and Debugging
*********************

.. _testing-in-your-fork:

Testing translations sync in your fork
======================================

Before submitting a pull request for review in the `openedx-translations repo`_, you should test the workflow
on a fork by following the steps below:

#. Add the ``make extract_translation`` into your fork of the new repository e.g. ``your-github-user-or-org/credentials`` in a new branch e.g. ``your-branch-name``
#. Fork the `openedx-translations repo`_ e.g. ``your-github-user-or-org/openedx-translations``.
#. In your fork, modify the `extract-translation-source-files.yml`_ file in a new branch e.g. ``your-branch-name``.
#. Go to the ``Actions`` tab in your repository (i.e. ``your-github-user-or-org/openedx-translations``)
#. From the left section, pick the `"Extract Translation Source Files" section in your fork`_
#. Click on the "Run workflow" dropdown button with the following parameters:

   - **Use workflow from your branch:** ``your-branch-name``
   - **Repository to extract translation source files from:** ``credentials``
   - **The ref to extract translation source files from:** ``omar/add-pull-translations``
   - Click on the "Run workflow" button

#. Verify the action ran successfully
#. Verify the new automated branch e.g. ``automated/extract-translation-source-files-20230903T001829`` has been created with a new commit e.g. ``chore: add updated translation source files`` has been created

Once all the above steps are verified, the extraction step is ready for use and the pull request has been tested.

In order to test the ``make pull_translations`` step, please follow the steps below:

#. Add any test translations to your fork of the `openedx-translations repo`_ in the repo directory to overcome the
   fact that translations don't exist in the upstream `openedx-translations repo`_ yet.

   We recommend copying existing translations. For example to test `credentials`_ we would copy the
   `course discovery translations`_ directory and modify it to include `credentials`_ conf/locale.

#. Temporarily pull translations from the fork using the Makefile command e.g. ``make ATLAS_OPTIONS="--repository=your-github-user-or-org/openedx-translations --revision=your-branch-name" pull_translations``

#. If you're testing an XBlock or an ``edx-platform`` plugin, run the ``make pull_translations`` command in
   the ``edx-platform``.

#. Run the application (or plugin) and verify the translations you've added are working properly.

   .. note::

     This step assumes that you're already familiar with `Tutor`_.


.. _debugging-translations:


Debugging translations workflows
================================

After adding a repository to the `openedx-translations repo`_ verify the following the next day:

#. The `extract-translation-source-files.yml`_ GitHub workflow worked successfully and the build passes in the
   `openedx-translations GitHub Actions tab`_. If something fails, ask for help in the `#wg-translations`_ Open edX
   Slack channel. An example of a successfully generated and merged pull request by the workflow's
   ``edx-transifex-bot`` is the `chore - add updated translation source files #615`_ pull request.

#. Verify that the `openedx-translations project`_ has a new resource for the repo.

#. Ensure the new Transifex resource is 100% translated. Alternatively, Open edX Transifex admins can force sync via
   the "Manual Sync" button in the `Transifex GitHub App sync logs`_ page.

#. Wait for the next sync. The sync is managed by Transifex and usually takes less than an hour
   (which we'll verify in the next step). The `Transifex GitHub App sync logs`_ show the most recent sync results.

#. Verify that the Transifex GitHub App created sync pull requests and auto-merged it to the repo.
   An example of a successfully merged pull request is the
   `Updates for file translations/frontend-app-learning/src/i18n/transifex_input.json in de on branch main #598`_ pull
   request.

#. Verify that the translations can be pulled in the repo as described in the sections above depending on the repo
   type.



.. _openedx-translations repo:  https://github.com/openedx/openedx-translations
.. _edx-cookiecutters:  https://github.com/openedx/edx-cookiecutters
.. _frontend-template-application: https://github.com/openedx/frontend-template-application
.. _frontend-template-application Makefile: https://github.com/openedx/frontend-template-application/blob/master/Makefile
.. _extract-translation-source-files.yml: https://github.com/openedx/openedx-translations/blob/2566e0c9a30d033e5dd8d05d4c12601c8e37b4ef/.github/workflows/extract-translation-source-files.yml#L36-L43
.. _Transifex GitHub App sync logs: https://github.apps.transifex.com/projects/o:open-edx:p:openedx-translations/openedx/openedx-translations
.. _cookiecutter-django-ida: https://github.com/openedx/edx-cookiecutters/tree/master/cookiecutter-django-ida
.. _openedx-translations project: https://app.transifex.com/open-edx/openedx-translations/dashboard/
.. _openedx-translations GitHub Actions tab: https://github.com/openedx/openedx-translations/actions
.. _#wg-translations: https://openedx.slack.com/archives/C037XDB9KN1

.. _chore - add updated translation source files #615: https://github.com/openedx/openedx-translations/pull/615
.. _Updates for file translations/frontend-app-learning/src/i18n/transifex_input.json in de on branch main #598: https://github.com/openedx/openedx-translations/pull/598
.. _course discovery translations: https://github.com/openedx/openedx-translations/tree/f0315d4/translations/course-discovery/course_discovery/conf/locale
.. _transifex.yml: https://github.com/openedx/openedx-translations/blob/main/transifex.yml
.. _Drag and Drop XBlock transifex.yml entry: https://github.com/openedx/openedx-translations/blob/19c0fcbbc334c56022df355fa5b529e5853d30f9/transifex.yml#L253-L259
.. _XBlock 1.9.1: https://github.com/openedx/XBlock/releases/tag/xblock-1.9.1
.. _"Extract Translation Source Files" section in your fork: https://github.com/Zeit-Labs/openedx-translations/actions/workflows/extract-translation-source-files.yml

.. _edx-platform: https://github.com/openedx/edx-platform
.. _credentials: https://github.com/openedx/credentials
.. _ecommerce: https://github.com/openedx/ecommerce
.. _course-discovery: https://github.com/openedx/course-discovery
.. _frontend-app-learning: https://github.com/openedx/frontend-app-learning

.. _Tutor: https://docs.tutor.overhang.io/
.. _Tutor MFE Docker build: https://github.com/overhangio/tutor-mfe/blob/master/tutormfe/templates/mfe/build/mfe/Dockerfile


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
