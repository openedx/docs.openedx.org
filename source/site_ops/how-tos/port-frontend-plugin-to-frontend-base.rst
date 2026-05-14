.. _Port a Frontend Plugin to frontend-base:

Port a Frontend Plugin from frontend-plugin-framework to frontend-base
######################################################################

.. tags:: site operator, developer, how-to

This how-to walks through porting an existing pair of plugins to
`frontend-base <https://github.com/openedx/frontend-base>`_:

* A **frontend plugin** (an npm package full of React components plugged in via
  ``env.config.jsx``), and
* A **Tutor plugin** (a Python module that registers the frontend plugin via
  ``tutormfe.hooks.PLUGIN_SLOTS`` and installs it into each MFE's image).

It assumes you understand the legacy stack and want to land on
``@openedx/frontend-base`` and ``tutor-mfe``'s frontend-base site support. It
is not a tutorial on either; for that, read:

* `frontend-base on GitHub <https://github.com/openedx/frontend-base>`_
* `tutor-mfe README, "Frontend-base site" section <https://github.com/overhangio/tutor-mfe#frontend-base-site>`_
* `frontend-base-compat <https://github.com/openedx/frontend-base-compat>`_ (escape hatch for plugins you can't port yet)

A worked example is available in the `sample-plugin repo
<https://github.com/openedx/sample-plugin>`_. The ported frontend-base App
lives in ``frontend-app-sample/``, a sibling of the legacy
``frontend-plugin-sample/``; the Tutor side lives in ``tutor-contrib-sample/``.

Understand the architectural shift
**********************************

The legacy world ships one Docker image per MFE. Each MFE reads its own
``env.config.jsx`` to discover plugin slot operations from the npm packages
installed in that image. The Tutor plugin's job is to (a) install the right npm
packages into the right MFE images, (b) inject imports into each
``env.config.jsx``, and (c) push ``PLUGIN_SLOTS`` entries that target an MFE
name and slot name.

frontend-base bundles every frontend app into a single **site**. The site's
``site.config.build.tsx`` (production) and ``site.config.dev.tsx`` (development)
import ``App`` objects and register them via ``addApp(siteConfig, app)``. An
``App`` carries its own slot operations, routes, providers, and config. There
is no per-MFE ``env.config.jsx``. There is no ``PLUGIN_OPERATIONS`` enum.

Practical consequences:

* A plugin no longer needs to be installed "into" the learner-dashboard image;
  it is installed into the site's npm workspace once.
* A plugin can target any number of slots across any number of frontend apps
  from one place.
* Scoping a plugin to a single legacy MFE's routes is done via
  ``condition: { active: [roleId] }`` on a slot op, not via the Tutor plugin's
  MFE-name parameter.
* ``@edx/frontend-platform`` is replaced by ``@openedx/frontend-base``. Both
  ``getConfig`` and ``getAuthenticatedHttpClient`` move there. ``LMS_BASE_URL``
  becomes ``lmsBaseUrl`` (camelCase) on ``getSiteConfig()``.

Port the frontend plugin (npm package)
**************************************

Rewrite component imports
=========================

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Legacy
     - frontend-base
   * - ``import { ... } from '@openedx/frontend-plugin-framework'``
     - ``import { ... } from '@openedx/frontend-base'``
   * - ``import { getConfig } from '@edx/frontend-platform'``
     - ``import { getSiteConfig } from '@openedx/frontend-base'``
   * - ``getConfig().LMS_BASE_URL``
     - ``getSiteConfig().lmsBaseUrl``
   * - ``getConfig().STUDIO_BASE_URL``
     - ``getSiteConfig().studioBaseUrl``
   * - ``import { getAuthenticatedHttpClient } from '@edx/frontend-platform/auth'``
     - ``import { getAuthenticatedHttpClient } from '@openedx/frontend-base'``
   * - ``import { useIntl, defineMessages } from '@edx/frontend-platform/i18n'``
     - ``import { useIntl, defineMessages } from '@openedx/frontend-base'``

Note the case change on config keys: legacy ``getConfig()`` exposed
``UPPER_SNAKE_CASE``; ``getSiteConfig()`` exposes the underlying ``camelCase``
object directly. Site-specific knobs that don't have a curated mapping live
under ``getSiteConfig().commonAppConfig`` (or under ``getAppConfig(appId)`` for
App-scoped settings declared on the App's ``config``).

Paragon imports (``@openedx/paragon``, ``@openedx/paragon/icons``) don't change.

Replace the slot-config shape with a frontend-base ``App``
==========================================================

Legacy plugins typically ship a ``plugin.jsx`` (the component) plus an
``index.jsx`` that just re-exports it. Site operators write the slot wiring
themselves in ``env.config.jsx``.

In frontend-base, the slot wiring is **part of the package**. Add an
``app.tsx`` (or ``app.jsx``) like:

.. code-block:: jsx

   import { WidgetOperationTypes } from '@openedx/frontend-base';
   import MyWidget from './MyWidget';

   const app = {
     appId: 'org.example.frontend.app.myPlugin',
     slots: [
       {
         slotId: 'org.openedx.frontend.slot.learnerDashboard.courseList.v1',
         id: 'org.example.frontend.widget.myPlugin.courseList.v1',
         op: WidgetOperationTypes.REPLACE,
         relatedId: 'defaultContent',
         component: MyWidget,
       },
     ],
   };

   export default app;

Translation table for the op field:

.. list-table::
   :header-rows: 1
   :widths: 35 35 30

   * - Legacy ``PLUGIN_OPERATIONS``
     - frontend-base ``WidgetOperationTypes``
     - Notes
   * - ``Insert`` (``DIRECT_PLUGIN``)
     - ``APPEND`` (default) / ``PREPEND`` / ``INSERT_BEFORE`` / ``INSERT_AFTER``
     - The new API distinguishes positions explicitly. ``relatedId`` anchors
       ``INSERT_BEFORE`` / ``INSERT_AFTER``.
   * - ``Insert`` (``IFRAME_PLUGIN``)
     - ``APPEND`` with ``url`` / ``title`` instead of ``component`` / ``element``
     - iframe widgets are first-class.
   * - ``Hide`` on ``default_contents``
     - ``REMOVE`` with ``relatedId: 'defaultContent'``
     -
   * - ``Hide`` + ``Insert`` (the FPF idiom for "replace")
     - ``REPLACE`` with ``relatedId: 'defaultContent'``
     - One op now.
   * - ``Wrap``
     - ``LayoutOperationTypes.REPLACE`` with a layout function
     - Less ergonomic; consider whether you really need it.
   * - ``Modify``
     - No direct equivalent
     - Pass overrides via slot context or App config instead.

Slot id changes are also mechanical but **not** automatic. The mapping is
documented per-MFE in frontend-base-compat's ``src/mappings/slotMaps/`` and in
each frontend-base app's ``src/slots/`` README. Two common ones:

* ``course_list_slot`` -> ``org.openedx.frontend.slot.learnerDashboard.courseList.v1``
* ``org.openedx.frontend.learner_dashboard.course_list.v1`` (legacy reverse-DNS)
  -> same as above

For widget ids inside ``relatedId``: the legacy ``default_contents`` becomes
``defaultContent``.

Update the package entry point
==============================

.. code-block:: jsx

   import sampleApp from './app';
   import MyWidget from './MyWidget';

   export default sampleApp;
   export { sampleApp, MyWidget };

The default export is the App. Named exports let consumers reach individual
pieces for testing or composition.

Update ``package.json``
=======================

Drop ``@openedx/frontend-build`` / ``fedx-scripts``, drop
``@edx/frontend-platform``, and switch to peer-depending on
``@openedx/frontend-base``:

.. code-block:: json

   {
     "name": "@org/my-plugin",
     "main": "dist/index.js",
     "exports": { ".": "./dist/index.js" },
     "files": ["dist"],
     "sideEffects": false,
     "scripts": {
       "build": "tsc --project tsconfig.build.json",
       "clean": "rm -rf dist"
     },
     "peerDependencies": {
       "@openedx/frontend-base": "^1.0.0",
       "@openedx/paragon": "^23",
       "@types/react": "^18",
       "react": "^18"
     }
   }

The build can be any vanilla bundler. The frontend-base learner-dashboard uses
``tsc``, which is the simplest option if you're not transforming SCSS or
assets. The legacy ``fedx-scripts babel src --out-dir dist`` no longer works
because consumers won't have those tools.

Add a ``tsconfig.json`` and ``tsconfig.build.json``:

.. code-block:: json

   // tsconfig.json
   {
     "extends": "@openedx/frontend-base/tools/tsconfig.json",
     "include": ["src/**/*"]
   }

.. code-block:: json

   // tsconfig.build.json
   {
     "extends": "./tsconfig.json",
     "compilerOptions": {
       "rootDir": "src",
       "outDir": "dist",
       "noEmit": false
     },
     "include": ["src/**/*"]
   }

Delete the old ``package-lock.json``: the dep tree changes substantially.

Port the Tutor plugin
*********************

Stop using ``PLUGIN_SLOTS`` for new code
========================================

``PLUGIN_SLOTS`` still works for legacy MFEs that remain in production, but it
has no effect on the frontend-base site. The frontend-base equivalents are:

* ``tutormfe.hooks.FRONTEND_APPS`` - declares which Apps are bundled into the
  site and where their npm packages come from.
* ``tutormfe.hooks.FRONTEND_SLOTS`` - registers ad-hoc slot operations directly
  on the site's ``customApp`` (no separate npm package needed). Best for
  one-off ops.
* The ``mfe-site-config-imports`` and ``mfe-site-config`` patches - inject
  imports and code into ``site.config.build.tsx`` and ``site.config.dev.tsx``.
  Use these in combination with ``FRONTEND_APPS`` to actually wire your App
  in.

The minimum viable wiring
=========================

.. code-block:: python

   from tutor import hooks
   from tutormfe.hooks import FRONTEND_APPS

   # Enable the built-in app whose slots you're targeting, if it ships disabled.
   @FRONTEND_APPS.add()
   def _enable_target(apps):
       apps["learner-dashboard"]["enabled"] = True
       return apps

   # Declare your App. tutor-mfe will `npm install` this into the site.
   @FRONTEND_APPS.add()
   def _add_my_app(apps):
       apps["my-plugin"] = {
           "npm_package": "@org/my-plugin",
           "npm_version": "^1.0.0",
           "enabled": True,
       }
       return apps

   hooks.Filters.ENV_PATCHES.add_item((
       "mfe-site-config-imports",
       "import myApp from '@org/my-plugin';",
   ))
   hooks.Filters.ENV_PATCHES.add_item((
       "mfe-site-config",
       "addApp(siteConfig, myApp);",
   ))

Three pieces, all required:

1. **FRONTEND_APPS enable** - some built-in apps (notably ``authn`` and
   ``learner-dashboard``) ship **disabled** in tutor-mfe; others (e.g.,
   ``instructor-dashboard``, ``notifications``) ship enabled. Check the
   tutor-mfe README, and flip ``enabled = True`` for any disabled app whose
   slots you target. Without it, the legacy per-MFE image is served and your
   slot ops are inert.
2. **FRONTEND_APPS add** - tutor-mfe handles the npm install during the site
   image build. Alternatively, set ``"source": "file://..."`` or a git URL to
   point at a local or forked checkout.

   .. note::

      ``source``-based installs are copied into the site as workspace packages
      under ``site/packages/frontend-app-<name>/``. During the site image
      build, ``npm install`` installs each workspace package's
      ``devDependencies``, and ``turbo run build`` invokes each package's own
      ``build`` script. That means your source package must declare a working
      ``build`` script (e.g., ``tsc --project tsconfig.build.json``) and any
      build-time tools not already provided by ``@openedx/frontend-base``
      (Babel, etc.) in ``devDependencies``; otherwise no transpilation happens
      and the site bundler will choke on raw TypeScript or JSX. Packages
      installed from npm are already built, so this caveat only applies to
      ``source``-based installs.
3. **mfe-site-config-imports + mfe-site-config** - this is what actually puts
   your App on the site.

Patch-name translation
======================

.. list-table::
   :header-rows: 1
   :widths: 35 35 30

   * - Legacy patch
     - frontend-base patch
     - What it does
   * - ``mfe-dockerfile-post-npm-install``
     - ``mfe-dockerfile-post-npm-install-site``
     - Install extra npm packages into a workspace. The legacy patch ran in
       every MFE image; the new patch runs in the site image.
   * - ``mfe-env-config-buildtime-imports``
     - ``mfe-site-config-imports``
     - Static imports at the top of the config file.
   * - ``mfe-env-config-buildtime-definitions``
     - ``mfe-site-custom-app-definitions``
     - Inline definitions reachable from the config. Less commonly needed;
       prefer an App package.
   * - (no equivalent)
     - ``mfe-site-config``
     - Arbitrary code that runs after ``siteConfig`` is created. Where
       ``addApp()`` calls go.
   * - ``mfe-lms-common-settings``
     - (unchanged)
     - LMS Python settings shared between MFE and frontend-base flows.

Slot id and operation translation
=================================

Same as on the frontend-plugin side. If you're using ``FRONTEND_SLOTS`` (the
simple path, no npm package), the slot-op string literal is the new format:

.. code-block:: python

   from tutormfe.hooks import FRONTEND_SLOTS

   FRONTEND_SLOTS.add_items([
       """
       {
         slotId: 'org.openedx.frontend.slot.footer.main.v1',
         op: 'widgetRemove',
         id: 'hideFooter',
         relatedId: 'defaultContent',
       }""",
   ])

The string ``'widgetRemove'`` (lowercase, camelCase) is equivalent to
``WidgetOperationTypes.REMOVE`` and avoids needing an extra import.

Don't want to port yet? Use the compat shim
*******************************************

For plugins you can't or don't want to rewrite, ``tutor-mfe`` ships a
translation layer via `@openedx/frontend-base-compat
<https://github.com/openedx/frontend-base-compat>`_. It runs your legacy
``env.config.jsx`` under a stub App on the frontend-base site.

Opt in coarsely (every ``PLUGIN_SLOTS`` contribution from one tutor plugin):

.. code-block:: python

   from tutormfe.hooks import FRONTEND_COMPAT_PLUGINS

   FRONTEND_COMPAT_PLUGINS.add_item("my-tutor-plugin")

Or finely (one slot at a time, kept in sync with ``PLUGIN_SLOTS``):

.. code-block:: python

   from tutormfe.hooks import PLUGIN_SLOTS, FRONTEND_COMPAT_SLOTS

   MY_SLOT = ("learning", "course_outline_sidebar.v1", "{ ... }")
   PLUGIN_SLOTS.add_item(MY_SLOT)
   FRONTEND_COMPAT_SLOTS.add_item(MY_SLOT)

Caveats the compat README spells out in detail:

* The shim covers the **runtime import surface** of ``@edx/frontend-platform``
  and ``@openedx/frontend-plugin-framework``. CSS selectors, the theme-variant
  ``data-`` attribute, and ``@openedx/frontend-build`` (``fedx-scripts``) are
  **not** shimmed. Brand stylesheets that key off the old
  ``data-paragon-theme-variant`` attribute or
  ``selected-paragon-theme-variant`` localStorage key must be updated.
* ``PLUGIN_OPERATIONS.Modify`` and ``slotOptions.mergeProps`` aren't translated.
* ``Wrap`` is translated best-effort; wrappers that read FPF-private context
  warn at runtime.

The shim is explicitly a migration aid. Plan to port to native frontend-base
App packages over time.

Conversion checklist
********************

For the frontend plugin (npm package):

* Replace every ``@openedx/frontend-plugin-framework`` import with
  ``@openedx/frontend-base``.
* Replace every ``@edx/frontend-platform`` import (including ``/auth``,
  ``/i18n``) with ``@openedx/frontend-base``.
* Replace every ``getConfig().UPPER_SNAKE_CASE`` with
  ``getSiteConfig().camelCase`` (or ``getAppConfig(appId).camelCase``).
* Add an ``app.tsx`` / ``app.jsx`` that exports a frontend-base ``App`` with
  the slot operations.
* Make the package's default export the ``App`` (named exports for components).
* Update slot ids to their reverse-DNS frontend-base equivalents.
* Replace ``PLUGIN_OPERATIONS`` values with ``WidgetOperationTypes`` values.
* Replace ``default_contents`` with ``defaultContent`` everywhere.
* Drop ``@openedx/frontend-build`` / ``fedx-scripts``. Build with ``tsc`` or
  an equivalent.
* Update ``package.json`` peer deps to ``@openedx/frontend-base``.
* Delete the stale ``package-lock.json``.

For the Tutor plugin:

* Confirm tutor-mfe is recent enough to expose ``FRONTEND_APPS``,
  ``FRONTEND_SLOTS``, and ``mfe-site-*`` patches.
* Enable any built-in ``FRONTEND_APPS`` whose slots you target (they ship
  disabled).
* Add your npm package via ``FRONTEND_APPS`` (or a ``source`` URL for local
  development).
* Replace ``mfe-dockerfile-post-npm-install*`` with
  ``mfe-dockerfile-post-npm-install-site`` (only if you're installing extra
  packages not covered by ``FRONTEND_APPS``).
* Replace ``mfe-env-config-buildtime-imports`` with ``mfe-site-config-imports``.
* Add an ``mfe-site-config`` patch that calls ``addApp(siteConfig, yourApp)``.
* Drop ``PLUGIN_SLOTS.add_item(("mfe-name", ...))`` calls (or keep them only
  for legacy MFEs you also support).
* If the brand override URL points at a CDN-served file, check the branch or
  tag in the URL still resolves.
* If you can't port immediately, opt in to ``FRONTEND_COMPAT_PLUGINS`` or
  ``FRONTEND_COMPAT_SLOTS`` instead.

Validation:

* ``npm install`` + ``npm run build`` succeeds in the frontend plugin package.
* ``tutor config save`` succeeds with the new plugin enabled.
* ``tutor images build mfe openedx`` succeeds (both pip and npm installs run
  at image-build time).
* The frontend-base site loads and renders the affected slot correctly at
  ``http://apps.local.openedx.io:8080``.
* The browser devtools show your widget id in the expected slot, with
  ``defaultContent`` removed if you used ``REPLACE``.

.. seealso::

   :ref:`Use A Frontend Plugin Framework Slot`

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-15   | Adolfo Brandes                | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
