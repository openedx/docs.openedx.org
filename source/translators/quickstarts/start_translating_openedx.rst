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

    * You have signed up for a `Transifex`_ account
    * You have joined the Transifex `edx-platform project`_, which is where all of our
translations are stored
    * Fluency in both English and the language(s) you are translating to. You should
have deep knowledge of English to be capable of translating phrases from the user
interface and  documentation. You should become a translator only if you feel
you are capable of translating in both English and your target language. Open edX is
written in English, so all translations are done from English to another language.

.. _Transifex: https://www.transifex.com/signup/
.. _edx-platform project: https://www.transifex.com/projects/p/edx-platform/

Finding a string to translate
*****************************

Once you have joined the edx-platform project, you will be able to select the option
"Languages" from the left hand menu.

Select the target language

Click the "Translate" button at the top

Select a resource

After you become a member of a translation or review team, you can select any of the
resources in the project to begin translating it. Before you begin, be sure to review
the Guidelines for Translators.

For help documentation on Transifex, review the section Transifex translators help desk.
Each language page lists a set of distinct resources to translate, like in the picture
below:
First, you should be focused on translating the non-Studio resources. That is, please
first translate and review these resources, in this order, before anything else:

* messages
* mako
* django-partial
* djangojs-partial
* wiki
* notifier-django
* comments-service

Only after the above resources are 100% translated and reviewed, move on to the Studio resources.
* mako-studio
* djangojs-studio
* django-studio
