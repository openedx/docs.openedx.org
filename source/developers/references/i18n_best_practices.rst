Internationalization Best Practices (Work-in-Progress)
######################################################

The Open edX platform has many different type of repositories. This guide
provides the best practices for them including XBlocks, edx-platform,
Micro-frontends and others.

This is an in-progress document and is updated as part of the `OEP-58`_
project which mostly involves:
 - Remove source and language translations from the repositories, hence no ``.json``, ``.po`` or ``.mo`` files will be committed into the repos.
 - Add standardized ``make extract_translations`` in all repositories
 - Push user-facing messages strings into [openedx/openedx-translations](https://github.com/openedx/openedx-translations/).
 - Integrate root repositories with [openedx/openedx-atlas](https://github.com/openedx/openedx-atlas/) to pull translations on build/deploy time


Adding a Repository to ``openedx/openedx-translations`` repository
******************************************************************

TBD

Pulling translation files via Atlas
***********************************

TBD


Micro-frontends (MFEs) best practices
*************************************

TBD

Use ``frontend-platform``.



XBlock best practices
*********************

TBD

 - Add translations in ``xblock/conf/locale`` instead of ``xblock/translations``.


.. _OEP-58: https://open-edx-proposals.readthedocs.io/en/latest/architectural-decisions/oep-0058-arch-translations-management.html
