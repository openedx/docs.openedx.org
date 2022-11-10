Translations Process
####################

High Level
**********

Your code needs to annotate strings so tooling can know that you want those strings translated. The tooling needs to extract those strings in order to be shared with translators. Once the strings have been extracted and made available to translators, strings can be translated to a variety of languages. Tooling will then download the translated strings and make them available to your running code.
.. This could be a diagram!

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

.. Name all the ways/tools that you can use to annotate and extract strings: django, javascript, etc.
.. Tooling (django, react-intl, etc.) generates 
To learn more about how to annotate strings for translation, see the annotation reference (link tbd).

Getting Strings Translated
**************************

The tool we use to translate strings is Transifex. Once translation source strings are extracted from code to files, the Transifex CLI tool can be used to upload them for translation. Translation is done by the community and coordinated by the Translations Working Group. For more information see :doc:`../quickstarts/start-translating-openedx`.

Using Translations
******************

In order to use translated strings, they must be downloaded as files. Translation files are periodically updated in the openedx-translations_ repository.

.. _openedx-translations: https://github.com/openedx/openedx-translations

