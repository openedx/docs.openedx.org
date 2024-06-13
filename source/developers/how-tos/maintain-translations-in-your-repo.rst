#####################################
Maintaining Translations on Your Repo
#####################################

.. contents::
 :local:
 :depth: 2

================
How To Use Atlas
================

`atlas`_ is a tool that pulls translations from the `openedx-translations`_ into your repository's directory.

The recommended way to use ``atlas pull`` is to call the ``make pull_translations`` command in the repository which
is described in details in the :doc:`enable-translations-new-repo` document.

The `atlas README`_ has up to-date command line usage instructions. For example the following command pulls
translations into the `edx-platform`_ repository:

.. code-block:: bash

    cd /path/to/edx-platform
    make pull_translations

The ``make pull_translations`` command will (roughly) run the following command:

.. code-block:: bash

    atlas pull translations/edx-platform/conf/locale:conf/locale

==============
Is It Working?
==============

To check if the translations pull command is working is to check the target directory ``conf/locale``
for the presence of the translations:

.. code-block:: bash

    tree conf/locale  # or ls conf/locale
    git status  # Should show the new files

Run your application and test translations by changing the user langauge from the Account Settings page.

===============================
What To Do If It's Not Working?
===============================

If the translations aren't being pulled or not working as expected, here are some problems to check for:

**Missing translations:** Ensure the translations you're looking to pull is available in the `openedx-translations`_
repository. Otherwise, an empty directory will be created. Use ``tree conf/locale`` to check if the translations are
present.

**.mo files are missing in Python applications:** Ensure the translations are compiled to ``.po`` files after
pulling the translations, because Python applications needs compiled ``.mo`` files.

**Empty src/i18n/index.js in Micro-frontends:** Ensure the ``src/i18n/index.js`` file is built after pulling the
translations. Compile the ``i18n/index.js`` as seen the `Makefile via intl-imports.js in the frontend-template-app`_
to ensure the translations are available in the application.

**Repo translations aren't being pushed to transifex:** Ensure the translations are enabled and pushed to and from
Transifex as described in the :doc:`enable-translations-new-repo` document.


.. seealso::
  :doc:`enable-translations-new-repo` and :doc:`/developers/concepts/oep58`

.. _atlas: https://github.com/openedx/openedx-atlas?tab=readme-ov-file#usage
.. _atlas README: https://github.com/openedx/openedx-atlas?tab=readme-ov-file#usage
.. _Makefile: https://github.com/openedx/edx-platform/blob/b6366b67b37c7b53428efeda675a5e16cb498c38/Makefile#L87
.. _edx-platform: https://github.com/openedx/edx-platform
.. _openedx-translations: https://github.com/openedx/openedx-translations/tree/main/translations
.. _Makefile via intl-imports.js in the frontend-template-app: https://github.com/openedx/frontend-template-application/blob/d4c053a9987d4fc3195a525bdcd14bf9421ca41a/Makefile#L43
