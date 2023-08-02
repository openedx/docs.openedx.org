OEP-58 Overview
###############

What is OEP-58?
===============

OEP-58 is a project to streamline translations management throughout the Open edX project.

How translations are managed now
================================

Where translations currently live
---------------------------------

Translations currently live in 2 places.

* In each repository in the form of ``.mo``, ``.po``, and ``.json`` files.
* In the ``edx-platform`` transifex project.

How translations are written
----------------------------

Translators edit translations in the ``edx-platform`` transifex project

How translations get into repositories from transifex
-----------------------------------------------------

Each repository has a jenkins job that:

* Pulls updated translations from transifex via the `deprecated`_ v2 api
* Commits the updated translations directly to the repo as `edx-transifex-bot`_

How translations currently get deployed
---------------------------------------

Translations are files in a repository that are built and deployed with the rest of the code.

How translations will be managed post OEP-58
============================================

Where translations will live
----------------------------

* In the `openedx-translations repository`_
* In the ``openedx-translations`` transifex project

How translations will be written
--------------------------------

Translators will edit translations in the ``openedx-translations`` transifex project

How translations will get from transifex to the `openedx-translations repository`_
----------------------------------------------------------------------------------

Translations will be committed to the `openedx-translations repository`_ via the supported `Transifex Integration GitHub App`_

How translations will be deployed
---------------------------------

The build process for each repository will be updated to use `openedx-atlas`_ to pull translations from the `openedx-translations repository`_.

What needs to happen for a repository to make the switch
--------------------------------------------------------
* The build process must be updated to support using `openedx-atlas`_ to pull translations from the `openedx-translations repository`_
* The repository must be configured to use the `openedx-atlas`_ method at build time
* The `openedx-translations repository`_ must be updated to include the source strings
* Translations must exist in the ``openedx-translations`` transifex project

Additional reading
==================
* `OEP-58: Translations Management — Open edX Proposals 1.0 documentation <https://open-edx-proposals.readthedocs.io/en/latest/architectural-decisions/oep-0058-arch-translations-management.html>`_
* `openedx-atlas README <https://github.com/openedx/openedx-atlas/blob/main/README.rst>`_
* `openedx-translations README <https://github.com/openedx/openedx-translations/blob/main/README.rst>`_

.. _deprecated: https://community.transifex.com/t/important-reminder-api-tx-cli-deprecation/3202
.. _edx-transifex-bot: https://github.com/edx-transifex-bot
.. _openedx-translations repository: https://github.com/openedx/openedx-translations
.. _Transifex Integration GitHub App: https://github.com/apps/transifex-integration
.. _openedx-atlas: https://github.com/openedx/openedx-atlas