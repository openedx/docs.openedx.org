Translations Process
####################

Overview
********

The Open edX Platform supports running in multiple languages. This page explains the
process by which we accomplish this. To begin with, your code needs to annotate strings
so tooling can know that you want those strings translated. The tooling needs to extract
those strings in order to be shared with translators. Once the strings have been
extracted and made available to translators, strings can be translated to a variety of
languages. Tooling will then download the translated strings and make them available to
your running code.

.. mermaid::

   flowchart TD
      annotate(Annotate Strings) -->
      extract(Extract Source Strings for Translation) -->
      upload(Upload Source Strings to Transifex) -->
      translate(Translate Strings) -->
      sync(Sync Translated Strings to openedx-translations) -->
      use(Using Translation)

Annotating and Extracting Strings
*********************************

Given code like this:

.. code-block:: python

   from django.utils.translation import ugettext as _

   # Translators: This will help the translator
   message = _("Welcome!")

   # Translators: This is a very long comment that needs to wrap
   # over multiple lines because it would be too long otherwise.
   message = _("Hello world")

Our tooling will extract the following strings:

* ``Welcome!``

* ``Hello world``

A similar process to the one noted above occurs in our Javascript frontend code as well.
For our django backed services, we use `django's builtin translation tooling`_ to extract
strings for translation. In our React based frontends, we use react-intl_ to extract
strings for translation.

To learn more about how to annotate strings for translation, see the annotation reference
(link tbd).

The `extraction process`_ is managed by the `openedx-translations repository`_
which stores the English source translations in git.

.. Annotation reference issue: https://github.com/openedx/docs.openedx.org/issues/211

.. _django's builtin translation tooling: https://docs.djangoproject.com/en/4.1/topics/i18n/translation/
.. _react-intl: https://formatjs.io/docs/react-intl/

Getting Strings Translated
**************************

The tool we use to translate strings is Transifex. Once translation source strings are
extracted from code to files, the `GitHub Transifex App`_ will upload the soruce translations
to Transifex so translators can do their work.

Translation is done by the community and coordinated by the Translations
Working Group. For more information see :doc:`../quickstarts/start-translating-openedx`.

Using Translations
******************

In order to use translated strings, they must be downloaded as files. Translation files
are automatically synced into the openedx-translations_ repository by the `GitHub Transifex App`_.

The openedx-atlas_ CLI tool has been built to help you download translation files for a
specific part of the codebase. This process is automated and included in the `Tutor Dockerfile`_.

During development, it is possible to download the latest files into a repositories source code e.g. ``edx-platform`` or ``frontend-app-learning`` by running the ``make pull_translations`` command in the desired repository's source code.

The specifics the Makefile program and ``atlas pull`` parameters are described in details in the :doc:`/developers/how-tos/enable-translations-new-repo` document.

Once the translations have been downloaded, you can simply start up the service and the
translations will be available to the user based on their profile settings.

.. Todo: add subsections here on how translations are used for Django and MFEs

.. _openedx-translations: https://github.com/openedx/openedx-translations
.. _openedx-atlas: https://github.com/openedx/openedx-atlas
.. _GitHub Transifex App: https://github.com/apps/transifex-integration
.. _openedx-translations repository: https://github.com/openedx/openedx-translations
.. _extraction process: https://github.com/openedx/openedx-translations/actions/workflows/extract-translation-source-files.yml
.. _Tutor Dockerfile: https://docs.tutor.edly.io/configuration.html#getting-and-customizing-translations
