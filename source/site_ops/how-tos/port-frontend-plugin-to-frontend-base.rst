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
is not a tutorial on either.  Refer to the following for more information:

* `OEP-65: Frontend Composability <https://docs.openedx.org/projects/openedx-proposals/en/latest/architectural-decisions/oep-0065-arch-frontend-composability.html>`_
* `frontend-base on GitHub <https://github.com/openedx/frontend-base>`_
* `frontend-template-application (frontend-base branch) <https://github.com/openedx/frontend-template-application/tree/frontend-base>`_ - the reference implementation of a frontend-base ``App``, worth reading alongside the steps below
* `tutor-mfe README, "Frontend-base site" section <https://github.com/overhangio/tutor-mfe/tree/main#frontend-base-site>`_
* `frontend-base-compat <https://github.com/openedx/frontend-base-compat>`_ (escape hatch for plugins you can't port yet)

Understand the architectural shift
**********************************

In the legacy world, each MFE is effectively an independent single-page
application: it builds, deploys, and ships as its own Docker image, with its
own copy of shared dependencies, header, and footer. It reads its own
``env.config.jsx`` to discover plugin slot operations from the npm packages
installed in that image. Composition across these silos is bolted on after the
fact: the Tutor plugin's job is to (a) install the right npm packages into the
right MFE images, and (b) inject the slot operations into each MFE's
``env.config.jsx``.

frontend-base is the reference implementation of the OEP-65 **shell**: a
build-time host that composes independently-developed **apps** into a single
**site**, so they share one set of dependencies and render as one page rather
than as a collection of separate deployments. Instead of a per-MFE
``env.config.jsx``, a *site config* (``site.config.build.tsx`` for production,
``site.config.dev.tsx`` for development) imports the ``App`` objects the site
composes and registers them. An ``App`` is a first-class, self-contained unit
of composition: it carries its own routes, providers, config, and the slot
operations that place **widgets** into named **slots** - its own, or those of
other apps or the shell. Composition is thus part of the architecture, not an
add-on layered over otherwise siloed frontends.

Some practical consequences:

* ``@edx/frontend-platform`` is replaced by ``@openedx/frontend-base``.
* A plugin no longer needs to be installed "into" the learner-dashboard image;
  it is installed into the site's npm workspace once, as an ``App``.
* An ``App`` can target any number of slots across any number of frontend apps
  from one place.
* Shared dependencies: an ``App`` peer-depends on the shell's single copy of
  React, Paragon, and ``@openedx/frontend-base`` rather than bundling its own.
  Keeping those version ranges compatible with the shell and the other composed
  apps is now part of the work.
* Navigating between apps within the same site no longer triggers a full page
  refresh.

Port the frontend plugin (npm package)
**************************************

This is the bulk of the work: turning the npm package that held your React
components into a self-contained frontend-base ``App``. The steps below rewrite
its imports to point at ``@openedx/frontend-base``, move the slot wiring out of
the site operator's ``env.config.jsx`` and into the package itself as an
``App``, expose that ``App`` as the package's default export, and update the
build so it produces plain, pre-built output the shell can consume. Work
through them in order; each assumes the previous one is done.

Rewrite component imports
=========================

The first, most mechanical step is to point your component code at
frontend-base. ``@openedx/frontend-base`` re-exports the runtime surface that
used to be spread across ``@openedx/frontend-plugin-framework`` and
``@edx/frontend-platform`` (including its ``/auth`` and ``/i18n``
sub-modules), so most imports change only in the package they come from. The
table below lists the substitutions you'll hit most often:

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

Each entry in a slot's ``slots`` array is a single operation, and its ``op``
field says what that operation does to the slot: add a widget, remove the
default one, replace it, and so on. This is the frontend-base successor to
FPF's ``PLUGIN_OPERATIONS``, but the two don't map one-to-one. FPF leaned on a
handful of operations whose exact effect depended on surrounding config (for
instance, whether ``keepDefault`` was set); frontend-base breaks those apart
into explicit, self-describing ops, so a behavior that used to be implied by
config is now named directly on the operation.

Use the table below to translate each of your existing operations. The middle
column gives the ``WidgetOperationTypes`` value (or, for a couple of cases,
another operation type) to reach for, and the Notes column flags where the
mapping is not a straight rename:

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
   * - ``Hide`` + ``Insert``, or configuring a slot without ``keepDefault``
       (the FPF idioms for "replace")
     - ``REPLACE`` with ``relatedId: 'defaultContent'``
     - In FPF, ``keepDefault`` is ``true`` only for slots that have no config;
       once you add any config for a slot it defaults to falsy, so the default
       content is replaced rather than appended/prepended to unless you set
       ``keepDefault: true``. frontend-base makes this explicit as a single
       per-widget op.
   * - ``Wrap``
     - ``LayoutOperationTypes.REPLACE`` with a layout function
     - Less ergonomic; consider whether you really need it.
   * - ``Modify``
     - ``WidgetOperationTypes.OPTIONS`` (``widgetOptions``), where the slot
       supports it
     - There is no blanket equivalent, but the default widget of a
       frontend-base slot can be built to consume structured data passed via a
       ``widgetOptions`` operation (read with ``useWidgetOptions()``) or via a
       layout, preserving modify-style customization. See `this
       frontend-app-catalog slot
       <https://github.com/openedx/frontend-app-catalog/commit/fed5aecc664b4b5d9c98f02ee14bdfd79e26782d>`_
       for an example of structuring a slot this way. If a slot you rely on
       doesn't yet expose the data you need, PRs restructuring it to support
       these use cases are welcome; sharing your ``Modify`` use case on the
       forums helps get it supported during the port.

Slot id changes are also mechanical but **not** automatic. The mapping is
documented per-MFE in frontend-base-compat's `src/mappings/slotMaps/
<https://github.com/openedx/frontend-base-compat/tree/main/src/mappings/slotMaps>`_
and in each frontend-base app's ``src/slots/`` README. Two common ones:

* ``course_list_slot`` -> ``org.openedx.frontend.slot.learnerDashboard.courseList.v1``
* ``org.openedx.frontend.learner_dashboard.course_list.v1`` (legacy reverse-DNS)
  -> same as above

For widget ids inside ``relatedId``: the legacy ``default_contents`` becomes
``defaultContent``.

Update the package entry point
==============================

With the ``App`` defined, the package's entry point (``index.ts`` /
``index.js``) becomes a thin re-export layer. Where the legacy ``index.jsx``
re-exported the plugin component, it now exports the ``App`` as the default so
that site configs and Tutor's ``addApp(siteConfig, myApp)`` can import it with
no knowledge of the package's internals:

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

The build can be any vanilla bundler. The core frontend-base apps use ``tsc``,
which is the simplest option if you're not transforming SCSS or assets. The
legacy ``fedx-scripts babel src --out-dir dist`` no longer works because
consumers won't have those tools.

Add ``tsconfig.json`` and ``tsconfig.build.json``:

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

Delete the old ``package-lock.json`` and regenerate it: the dep tree changes
substantially.

Port the Tutor plugin
*********************

With the npm package now an ``App``, the Tutor plugin's job changes from
wiring plugins into per-MFE images to composing your ``App`` into the site. In
practice that means swapping the ``PLUGIN_SLOTS`` and ``env.config.jsx`` hooks
for their ``FRONTEND_*`` and ``mfe-site-*`` equivalents: declaring the ``App``
so tutor-mfe installs it, and patching the site config so the shell actually
registers it. The subsections below cover which hooks to stop using, the
minimum wiring to get the ``App`` onto the site, and how the old patch names
map to the new ones.

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

Putting those hooks together, here is the smallest Tutor plugin that gets a
ported ``App`` rendering on the site. It does three things: enables the
built-in app whose slots you're targeting, declares your package so tutor-mfe
installs it, and patches the site config to import and register your ``App``.
Each piece is explained below the snippet.

.. code-block:: python

   from tutor import hooks
   from tutormfe.hooks import FRONTEND_APPS

   # Enable the built-in app whose slots you're targeting, if it ships disabled.
   @FRONTEND_APPS.add()
   def _enable_target(apps):
       apps["learner-dashboard"]["enabled"] = True
       return apps

   # Declare your plugin. tutor-mfe will `npm install` this into the site.
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

All of the above are required:

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
   your plugin app on the site.

Patch-name translation
======================

If your Tutor plugin reaches beyond the ``FRONTEND_APPS`` and ``FRONTEND_SLOTS``
hooks above and patches the config files directly, the patch names change too:
the legacy patches operated on each MFE's ``env.config.jsx``, while their
frontend-base counterparts operate on the site's ``site.config.*.tsx``. The
table below maps the ones you're most likely to have used. Anything not listed
either has no equivalent or is unchanged:

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

The slot ids and operation types are the same ones you translated on the
frontend-plugin side (see `Replace the slot-config shape with a frontend-base
App`_): reverse-DNS ``slotId`` values and ``WidgetOperationTypes`` ops, with
``defaultContent`` as the default widget's ``relatedId``.

The difference here is how you express them. ``FRONTEND_SLOTS`` is the simple
path for one-off operations that don't warrant their own npm package: rather
than importing an ``App``, you hand tutor-mfe the slot operation as a string
literal that it drops onto the site's ``customApp``. Because it's a plain
string, you name the op with its camelCase string form (for example,
``'widgetRemove'``) instead of importing the ``WidgetOperationTypes`` enum:

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

The shim can be opted into at two granularities, depending on how much of a
tutor plugin you want to run through it.

The coarse option takes everything at once: pass a tutor plugin's name and
every ``PLUGIN_SLOTS`` contribution it makes is run through the shim. This is
the least effort and a good starting point when you just want an unported
plugin working on the site, but it's all-or-nothing, so you can't port some of
that plugin's slots natively while shimming the rest.

.. code-block:: python

   from tutormfe.hooks import FRONTEND_COMPAT_PLUGINS

   FRONTEND_COMPAT_PLUGINS.add_item("my-tutor-plugin")

The fine option takes one slot at a time. You register the same
``PLUGIN_SLOTS`` tuple with both ``PLUGIN_SLOTS`` and ``FRONTEND_COMPAT_SLOTS``,
which lets you shim individual slots while porting others in the same plugin.
The catch is that the two registrations must be kept in sync by hand: if the
slot definition drifts in one place and not the other, the legacy MFE and the
site will disagree.

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

The preceding sections explain the why and the how; this is the condensed
punch list to work against once you understand them. It gathers every discrete
change described above into three groups - the frontend plugin, the Tutor
plugin, and the validation steps that confirm the port - so you can track a
port to completion without re-reading the prose. If a line here is unfamiliar,
the section it came from has the full detail.

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

To validate the migration:

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
| Review Date  | Working Group Reviewer        | Release        | Test situation                 |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-15   | Adolfo Brandes                | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
