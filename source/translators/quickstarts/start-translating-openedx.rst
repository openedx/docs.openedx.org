Quick Start: How to start translating for Open edX
##################################################

.. contents:: Steps to translate strings in Open edX using Transifex
   :local:
   :class: no-bullets

Welcome to the Quickstart guide for new Open edX translators. By the end of
this tutorial, you will have completed all the steps necessary to begin
submitting translations to the Open edX project.

Before you start
****************

This tutorial assumes the following:

* You have signed up for a `Transifex`_ account and have read through their `getting
  started guide`_. For help getting started with Transifex, please review their
  `Translating with the Web Editor`_ page, and understand the roles and permissions
  as documented in `Understanding User Roles`_. You will start off in the "Translator"
  role.
* You have joined the Transifex `edx-platform project`_ with the language(s) you wish
  to translate to
* Fluency in both English and the language(s) you are translating to. You should
  have deep knowledge of English to be capable of translating phrases from the user
  interface and  documentation. You should become a translator only if you feel
  you are capable of translating in both English and your target language. Open edX is
  written in English, so all translations are done from English to another language
* You have joined the Open edX Slack or Discuss. Links to join are available at the
  `Open edX Community`_ page. Translation help is available in the
  ``#translations-working-group`` Slack channel!

.. _Transifex: https://www.transifex.com/signup/
.. _getting   started guide: https://docs.transifex.com/getting-started-1/translators
.. _Translating with the Web Editor: https://docs.transifex.com/translation/translating-with-the-web-editor
.. _edx-platform project: https://explore.transifex.com/open-edx/edx-platform/
.. _Open edX Community: https://openedx.org/community/connect/
.. _Understanding User Roles: https://docs.transifex.com/teams/understanding-user-roles

Finding a string to translate
*****************************

#. Once you have joined the edx-platform project, you will be able to select the option
   "Languages" from the left hand menu under "edx-platform"

![Image1](source/_images/Lang2.png) 

#. Select the target language that you wish to translate to

![Image2](source/_images/Lang3.png)

#. If you are allowed to translate for this language the "Translate" button at the top
   will allow you to click it. If you are unable to click the button you may need to
   wait for approval to join the translation team for this language before proceeding.

![Image3](source/_images/Lang4.png)

#. Select a resource

After you become a member of a translation team for a language, you can select any of
the resources in the project to begin translating it.

![Image4](source/_images/Lang5.png)

After you select a resource, you will see the number of untranslated strings and unreviewed. 
You are able to choose which string to translate and then ckick the button "Save Translation"
after you have tranlsated such string.

![Image5](source/_images/Lang6.png)

Details about how to translate
things like HTML, placeholders, and other more complicate strings for Open edX
are in the :doc:`/translators/concepts/index` section.

Each language page lists a set of distinct resources to translate. A resource can be
a Python and Django web service, a Javascript frontend, or even a single Javascript
file. You should start by focusing on translating the non-Studio resources. That is,
please first translate and review these resources, in this order, before anything else:

* messages
* mako
* django-partial
* djangojs-partial
* wiki
* notifier-django
* comments-service

Only after the above resources are 100% translated and reviewed in your target language,
move on to the Studio resources.

* mako-studio
* djangojs-studio
* django-studio

Beyond those, it is best to ask what to work on next in Slack or Discuss to make sure
your translations are as useful as possible to the community!

Translating
***********
Transifex's `Translating with the Web Editor`_ page has details on how to use their
tool to find and translate strings within a resource. Please use that as a guide
to locate an simple untranslated string (something that is just a word or short phrase)
that you feel confident in translating.

#. Select your string
#. Enter the translation in the center box
#. Press "Save Translation"
#. Your string is now ready for review! Every string must be reviewed and approved before
   it will be accepted into the official translations and released to the community.

Next Steps
**********
* Learn more about how to translate different types of strings in
  :doc:`/translators/concepts/index`
* Become a reviewer to help the translation process move more quickly
* Help keep this documentation up to date by submitting fixes or creating issues in the
  `docs.opened.org Github repository`_

.. _docs.opened.org Github repository: https://github.com/openedx/edx-documentation
