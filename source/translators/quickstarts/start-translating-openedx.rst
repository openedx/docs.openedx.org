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

* You have joined the Transifex `openedx-translations project`_ with the language(s) you wish
  to translate to.

* You have to be fluent in both English and the language(s) you are translating to. You should
  have deep knowledge of English to be capable of translating phrases from the user
  interface and  documentation. You should become a translator only if you feel
  you are capable of translating in both English and your target language. Open edX is
  written in English, so all translations are done from English to another language.

* You have joined the Open edX Slack and Discourse (https://discuss.openedx.org) . Links to join are available at the
  `Open edX Community`_ page. Translation help is available in the
  ``#translations-working-group`` Slack channel!

* Note: If you want to translate for the Open edX platform, you should follow the steps above. 
  However, translating the edX website (https://openedx.org) occurs in a
  different application, so in order to become a collaborator with
  G-translate, you should contact our Open edX Community Manager Eden
  Huthmacher by writing an `email <ehuthmacher@tcril.org>`_.


.. _Transifex: https://www.transifex.com/signup/
.. _getting   started guide: https://docs.transifex.com/getting-started-1/translators
.. _Translating with the Web Editor: https://docs.transifex.com/translation/translating-with-the-web-editor
.. _openedx-translations project: https://explore.transifex.com/open-edx/openedx-translations/
.. _Open edX Community: https://openedx.org/community/connect/
.. _Understanding User Roles: https://docs.transifex.com/teams/understanding-user-roles

Finding a string to translate
*****************************

#. Once you have joined the openedx-translations project, you will be able to select the option
   "Languages" from the left hand menu under "openedx-translations":

   .. image:: /_images/SelectLanguages.png

#. Select the target language that you wish to translate to:

   .. image:: /_images/SelectTargetLang.png

#. If you are allowed to translate for this language the "Translate" button at the top
   will allow you to click it. If you are unable to click the button you may need to
   wait for approval to join the translation team for this language before proceeding:

   .. image:: /_images/ResourceList.png

#. **Select a resource**

   After you become a member of a translation team for a language, you can select any of
   the resources in the project to begin translating it:

   .. image:: /_images/SelectResource.png

#. **Translate a string**

   After you select a resource, you will see the number of untranslated and unreviewed strings.
   You can choose which string to translate and then click the button "Save Translation"
   after you have translated a string:

   .. image:: /_images/TranslateResource.png

#. After saving your translation, there is a possibility to make a QA test by clicking the button
   "QA Check" on the right side of the screen:

   .. image:: /_images/QACheck1.png

#. When you click such button, there are three possibilities for checking your translation by opening LexiQA:

  * Perform Changes:

    .. image:: /_images/QACheck2_PerformChanges.png

    If you click the first option of this menu,  it shows another screen detailing inconsistencies,
    or sentences/phrases same as source:

    .. image:: /_images/PerformChangesScreen2.png

  * View Reports:

    .. image:: /_images/QACheck3_ViewReports.png

    This option shows the same screen as below within LexiQA, and also another option called "Analytics".
    Under such option, you can check the following data:

    * File info
    * Errors
    * Statistics (see picture below)
    * Downloads

    .. image:: /_images/Analytics_Statistics3.png

  * Check Consistency:

    .. image:: /_images/QACheck4_Consistency.png

    This option shows the amount of inconsistencies found comparing to the source text,
    so that you can edit your translation:

    .. image:: /_images/ConsistencyScreen4.png

Details about how to translate things like HTML, placeholders, and other more complicate strings for Open edX
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
#. Your string is now ready for review! Every string must be reviewed and
   approved before it will be accepted into the official translations and
   released to the community.

Next Steps
**********

* Learn more about how to translate different types of strings in
  :doc:`/translators/concepts/index`
* Become a reviewer to help the translation process move more quickly
* Help keep this documentation up to date by submitting fixes or creating issues in the
  `docs.openedx.org Github repository`_

.. _docs.openedx.org Github repository: https://github.com/openedx/docs.openedx.org

Useful links
************

* `Confluence site for Translation Working Group <https://openedx.atlassian.net/wiki/spaces/COMM/pages/3157524644/Translation+Working+Group>`_
* `Open edX WG website link <https://openedx.org/open-edx-community-working-groups/>`_
* `Transifex lexiQA Integration <https://www.transifex.com/blog/2019/lexiqa-integration/>`_
