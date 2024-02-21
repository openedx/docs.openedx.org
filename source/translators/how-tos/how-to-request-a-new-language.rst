How to request a new language for translation
#############################################

Assumptions
***********

* The language you are interested in is not listed on the Transifex
  `openedx-translations Transifex project`_.

* A variant of the language that may meet your needs is also not listed
  (``Chinese`` vs ``Chinese-China``).

* Prefer a root locale over a variant locale (``de`` over ``de_DE``) whenever applicable so other locales can inherit
  from it e.g. ``de_AT``.

* If you request a new language, we ask that you commit to the success of your
  language’s translation project. Particularly, we expect you to:

  * Be an active translator: Translate the ``edx-platform``, ``edx-platform-js`` and main micro-frontends such as
    Learning MFE and other resources in the `openedx-translations Transifex project`_

  * Work to recruit other translators and reviewers

  * Monitor and address Transifex issues posted by translators.

  * Monitor and fix translations validation errors: :doc:`how-to-fix-translation-errors`.

  You will be responsible for advancing your target language to completion, with
  all strings translated and reviewed, so that we can publish your work to the
  Open edX community.

.. note::
   Languages can be removed from the project if they are not actively maintained.

Steps
*****

#. Go to the `openedx-translations Transifex project`_

#. Select the option :guilabel:`Request language` to start a new translation
   project for your target language.

#. Wait for an edX translation team member to
   respond to your request within a few days.

#. If the language that you request
   is approved, you become the coordinator of the project. You can add
   additional coordinators, reviewers, and translators as you wish.

.. _openedx-translations Transifex project: https://explore.transifex.com/open-edx/openedx-translations/
