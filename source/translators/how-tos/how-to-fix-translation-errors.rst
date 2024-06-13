How to fix translation validation errors
########################################

As part of OEP-58 (:doc:`/developers/concepts/oep58`), automatic translation validation has been added to avoid
breaking builds and deployments due to invalid translations.

As of writing this document, `validation scripts and GitHub Actions`_ checks .po files for compilation errors.
Other file formats are not checked, but `contributions to support .json and other files validation are welcome`_.

Steps
*****

#. Monitor the list of `invalid translations reports`_ in the `openedx-translations repository`_.
#. Identify the invalid translation entries in the pull requests of your language by checking the bot report in
   the comments.
#. Go to the `openedx-translations project page`_.
#. Search for the invalid translation entries in the Transifex resources.
#. Once the issues are fixed, the Transifex bot will update the pull request and it'll be automatically merged.

.. _openedx-translations project page: https://explore.transifex.com/open-edx/openedx-translations/
.. _contributions to support .json and other files validation are welcome: https://github.com/openedx/openedx-translations/issues/549
.. _validation scripts and GitHub Actions: https://github.com/openedx/openedx-translations/blob/main/.github/workflows/validate-translation-files.yml
.. _invalid translations reports: https://github.com/openedx/openedx-translations/pulls?q=is%3Apr+is%3Aopen+%22Some+translations+are+invalid.%22
.. _openedx-translations repository: https://github.com/openedx/openedx-translations
