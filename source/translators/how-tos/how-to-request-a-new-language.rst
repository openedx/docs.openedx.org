.. _How to request a new language for translation:

How to request a new language for translation
#############################################

Assumptions
***********

* The language you are interested in is not listed on the Transifex
  `openedx-translations Transifex project`_.

* A variant of the language that may meet your needs is also not listed
  (``Chinese`` vs ``Chinese-China``).

* Prefer a root locale over a variant locale (``de`` over ``de_DE``) whenever
  applicable so other locales can inherit from it e.g. ``de_AT``.

* If you request a new language, we ask that you commit to the success of your
  language's translation project. Particularly, we expect you to:

  * Be an active translator: Translate the ``edx-platform``, ``edx-platform-js``
    and main micro-frontends such as Learning MFE and other resources in the
    `openedx-translations Transifex project`_.

  * Work to recruit other translators and reviewers.

  * Monitor and address Transifex issues posted by translators.

  * Monitor and fix translations validation errors: :ref:`How to fix translation
    validation errors`.

  You will be responsible for advancing your target language to completion, with
  all strings translated and reviewed, so that we can publish your work to the
  Open edX community.

.. warning::

   Languages can be removed from the project if they are not actively
   maintained.

Steps
*****

#. Email ``oscm@axim.org`` to request a new language code. Please do *not*
   request a language from the `openedx-translations Transifex project`_,
   because we can't communicate with you via this channel. Please email instead.

#. Wait for an Open edX translation team member to respond to your request
   within a few days. Please keep the following in mind:

   * The Open edX team needs to verify the language code and often will have
     questions before accepting a new language. For example, a request for a
     specific locale (such as German for Germany ``de_DE`` or Arabic for Iraq ``ar_IQ``) will be weighed
     against a more global language code (such as global German ``de`` or global Arabic ``ar``).

   * A language will only be added with a commitment from an individual or group
     to manage the translators for the language for at least one release. The
     Open edX project is large, and there's high turnaround of translators which
     often results in low quality translations and in some cases invalid translations
     that cause server errors.

#. If the language that you request
   is approved, you become the coordinator of the project. You can add
   additional coordinators, reviewers, and translators as you wish.

.. _openedx-translations Transifex project: https://explore.transifex.com/open-edx/openedx-translations/


**Maintenance chart**

+--------------+-------------------------------+----------------+----------------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                        |
+--------------+-------------------------------+----------------+----------------------------------------------------------------------+
| 2025-10-03   | Omar                          | No release     | Pass                                                                 |
+--------------+-------------------------------+----------------+----------------------------------------------------------------------+
