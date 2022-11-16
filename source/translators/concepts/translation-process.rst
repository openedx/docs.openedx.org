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
      extract(Extract Strings For Translation) -->
      upload(Upload to Transifex) -->
      translate(Translate Strings) -->
      download(Download for Use)

Annotating and Extracting Strings
*********************************

Given code like this:

.. code-block::

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

.. Annotation reference issue: https://github.com/openedx/docs.openedx.org/issues/211

.. _django's builtin translation tooling: https://docs.djangoproject.com/en/4.1/topics/i18n/translation/
.. _react-intl: https://formatjs.io/docs/react-intl/

Getting Strings Translated
**************************

The tool we use to translate strings is Transifex. Once translation source strings are
extracted from code to files, the Transifex CLI tool can be used to upload them for
translation. Translation is done by the community and coordinated by the Translations
Working Group. For more information see :doc:`../quickstarts/start-translating-openedx`.

Using Translations
******************

In order to use translated strings, they must be downloaded as files. Translation files
are periodically updated in the openedx-translations_ repository.

The openedx-atlas_ CLI tool was built to help you download translation files for a
specific part of the codebase. 

.. code-block::

   cd /path/to/credentials
   # pull down the latest translations for all available
   # languages for the credentials application 
   atlas pull --directory credentials

Once the translations have been downloaded, you can simply start up the service and the
translations will be available to the user based on their profile settings.

.. Todo: add subsections here on how translations are used for Django and MFEs

.. _openedx-translations: https://github.com/openedx/openedx-translations
.. _openedx-atlas: https://github.com/openedx/openedx-atlas
