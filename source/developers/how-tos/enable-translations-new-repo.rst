Enabling Translations on a New Repo
###################################

.. contents::
 :local:
 :depth: 2

Quickstart
**********

To enable translations on a new repository according to the `OEP-58 - Translations Management`_ proposal

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

#. Add the repository to `extract-translation-source-files.yml`_ in the `openedx-translations repo`_.

   Add a new entry under the ``python-translations`` section. For example, the XBlock located at
   ``https://github.com/openedx/xblock-drag-and-drop-v2`` should have the following entry::

    python-translations:
      strategy:
        matrix:
          repo:
            ...
            - repo_name: xblock-drag-and-drop-v2
            ...


#. Add the repository to the `transifex.yml`_ file in the `openedx-translations repo`_.
   Copy the `Drag and Drop XBlock transifex.yml entry`_ and modify it to match the new repository.

#. Create a draft pull request in the `openedx-translations repo`_

#. Follow the instructions in the :ref:`testing-in-your-fork` section to verify new repository configuration.

#. Mark your pull request as ready for review and wait for it to be merged.

#. Verify the workflow is syncing the translations properly as described in the :ref:`debugging-translations` section.

#. Install the XBlock or plugin in your local `Tutor`_ or `devstack`_ environment. Run
   ``OPENEDX_ATLAS_PULL=true make pull_translations`` in the ``edx-platform`` repo to preview the translations.


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

   Add a new entry under the ``python-translations`` section. For example for the `credentials`_ repo it should have
   the following entry::

    django-translations:
      strategy:
        matrix:
          repo:
            ...
            - repo_name: credentials
            ...

#. Create a draft pull request in the `openedx-translations repo`_

#. Follow the instructions in the :ref:`testing-in-your-fork` section to verify the new repository configuration.

#. Mark your pull request as ready for review and wait for it to be merged.

#. Verify the workflow is syncing the translations properly as described in the :ref:`debugging-translations` section.

#. Run ``OPENEDX_ATLAS_PULL=true make pull_translations`` to verify translations are pulled from the
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

#. Run ``make extract_translations``. Verify that it creates ``src/i18n/transifex_input.json``. This file should be
   excluded from the repo via the ``.gitignore`` file.

#. Add the repository to `extract-translation-source-files.yml`_ in the `openedx-translations repo`_.

   Add a new entry under the ``javascript-translations`` section. For example for the `frontend-app-learning`_ repo
   should have the following entry::

    js-translations:
      strategy:
        matrix:
          repo:
            ...
            - frontend-app-learning
            ...

#. Create a draft pull request in the `openedx-translations repo`_

#. Follow the instructions in the :ref:`testing-in-your-fork` section to verify the new repository configuration.

#. Mark your pull request as ready for review and wait for it to be merged.

#. Verify the workflow is syncing the translations properly as described in the :ref:`debugging-translations` section.

#. Depending on how you deploy the micro-frontend, include the ``pull_translations`` make rule with the
   ``OPENEDX_ATLAS_PULL`` environment variable set to ``true`` e.g
   ``$ OPENEDX_ATLAS_PULL=true make pull_translations``.

   This command needs to run before ``npm build`` in order to include updated translations in final micro-frontend
   build.


Testing and Debugging
*********************

.. _testing-in-your-fork:

Testing translations sync in your fork
======================================

Before submitting a pull request for review in the `openedx-translations repo`_, you should test the workflow
on a fork by following the steps below:

#. Fork the `openedx-translations repo`_.
#. Make a pull request to your fork and modify the `extract-translation-source-files.yml`_ workflow to use your
   repo, your organization name and the branch in the clone section.
   For example, the `frontend-lib-special-exams testing pull request`_ uses the ``Zeit-Labs/frontend-lib-special-exams`` repository with the branch
   set via ``ref: fix-i18n``.

#. Modify the `extract-translation-source-files.yml`_ workflow to run ``pull_request`` events.

#. Verify that an automated source translation pull request is created on your fork similar to the
   `chore - add updated translation source files`_ pull request.

#. Add any test translations to your fork of the `openedx-translations repo`_ in the repo directory to overcome the
   fact that translations don't exist in the upstream `openedx-translations repo`_ yet.

   We recommend copying existing translations. For example to test `credentials`_ we would copy the
   `course discovery translations`_ directory and modify it to include `credentials`_ conf/locale.

#. Temporarily edit the ``Makefile`` so the ``pull_translations`` step pulls from your fork e.g.
   ``atlas pull --repository=Zeit-Labs/openedx-translations``.

#. If you're testing and Open edX plugin, run the ``$ OPENEDX_ATLAS_PULL=true make pull_translations`` command in
   the ``edx-platform`` repo. Otherwise, run ``$ OPENEDX_ATLAS_PULL=true make pull_translations`` in the repository
   you're testing e.g. ``frontend-app-learning``.

#. Run the application (or plugin) and verify the translations you've added are working properly.

   .. note::

     This step assumes that you're already familiar with `Tutor`_ and/or `devstack`_.


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
.. _OEP-58 - Translations Management: https://docs.openedx.org/projects/openedx-proposals/en/latest/architectural-decisions/oep-0058-arch-translations-management.html
.. _extract-translation-source-files.yml: https://github.com/openedx/openedx-translations/blob/2566e0c9a30d033e5dd8d05d4c12601c8e37b4ef/.github/workflows/extract-translation-source-files.yml#L36-L43
.. _Transifex GitHub App sync logs: https://github.apps.transifex.com/projects/o:open-edx:p:openedx-translations/openedx/openedx-translations
.. _cookiecutter-django-ida: https://github.com/openedx/edx-cookiecutters/tree/master/cookiecutter-django-ida
.. _openedx-translations project: https://app.transifex.com/open-edx/openedx-translations/dashboard/
.. _openedx-translations GitHub Actions tab: https://github.com/openedx/openedx-translations/actions
.. _#wg-translations: https://openedx.slack.com/archives/C037XDB9KN1

.. _chore - add updated translation source files #615: https://github.com/openedx/openedx-translations/pull/615
.. _Updates for file translations/frontend-app-learning/src/i18n/transifex_input.json in de on branch main #598: https://github.com/openedx/openedx-translations/pull/598
.. _course discovery translations: https://github.com/openedx/openedx-translations/tree/f0315d4/translations/course-discovery/course_discovery/conf/locale
.. _frontend-lib-special-exams testing pull request: https://github.com/Zeit-Labs/openedx-translations/pull/1/files
.. _transifex.yml: https://github.com/openedx/openedx-translations/blob/main/transifex.yml
.. _Drag and Drop XBlock transifex.yml entry: https://github.com/openedx/openedx-translations/blob/19c0fcbbc334c56022df355fa5b529e5853d30f9/transifex.yml#L253-L259

.. _edx-platform: https://github.com/openedx/edx-platform
.. _credentials: https://github.com/openedx/credentials
.. _ecommerce: https://github.com/openedx/ecommerce
.. _course-discovery: https://github.com/openedx/course-discovery
.. _frontend-app-learning: https://github.com/openedx/frontend-app-learning

.. _Tutor: https://docs.tutor.overhang.io/
.. _devstack: https://github.com/openedx/devstack/
.. _chore - add updated translation source files: https://github.com/Zeit-Labs/openedx-translations/pull/49/commits/e872c962d6873b9f178f8901ef661c7f1c266397
