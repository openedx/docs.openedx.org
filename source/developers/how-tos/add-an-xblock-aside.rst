.. _Add an XBlock Aside:

####################
Add an XBlock Aside
####################

.. tags:: developer, how-to

Add an XBlock Aside to attach behavior, UI, or stored data to one or more
existing XBlock types without modifying those XBlocks. Use this recipe
when you want a single, installable Python package that decorates the
views of XBlocks in your platform.

For background on what asides are and when to use them, read
:ref:`About XBlock Asides`. For a complete API reference, see
:ref:`XBlock Asides Reference`.

.. contents:: Contents
   :local:
   :depth: 1

Prerequisites
*************

Before you start, make sure you have:

* A working Open edX development environment in which you can install a
  Python package and restart the LMS and Studio services. Tutor devstack
  is the recommended environment.
* The installed Python version used by the target Open edX release.
* Familiarity with writing a basic XBlock view that returns a
  :class:`~web_fragments.fragment.Fragment`. If you have never written
  one, complete :ref:`XBlock Aside Quickstart` first.

This recipe builds a feedback-badge Aside that adds a "Report an issue"
link to Problem and Video blocks, with a course-author setting to enable
or disable it per block. Substitute your own block types and behavior as
needed.

Step 1: Scaffold a Python package
*********************************

Create a new directory for the Aside package, with the layout below:

.. code-block:: text

   feedback_badge_aside/
   ├── pyproject.toml
   ├── feedback_badge_aside/
   │   ├── __init__.py
   │   ├── Aside.py
   │   └── static/
   │       ├── html/
   │       │   └── studio_view.html
   │       ├── css/
   │       │   └── studio.css
   │       └── js/
   │           └── studio.js
   └── README.rst

The package name (``feedback_badge_aside``) and the module name
(``Aside.py``) are conventions; pick names that describe your Aside.
The ``static/html`` and ``static/js`` directories hold the template and
script for the author-facing toggle built in later steps — this
mirrors how production asides such as `ol-openedx-chat`_ lay out their
static assets.

Populate ``pyproject.toml`` with the package metadata and a placeholder
for the entry point you will add in :ref:`Step 8 <register entry point>`.

.. code-block:: toml

   [project]
   name = "feedback-badge-Aside"
   version = "0.1.0"
   description = "An XBlock Aside that adds a feedback link to Problem and Video blocks."
   requires-python = ">=X.Y"  # set to the minimum Python version for the target Open edX release
   dependencies = [
       "XBlock",
       "web-fragments",
   ]

   [build-system]
   requires = ["setuptools>=61.0"]
   build-backend = "setuptools.build_meta"

Step 2: Define the Aside class
******************************

In ``feedback_badge_aside/Aside.py``, define a subclass of
:class:`~xblock.core.XBlockAside`.

.. code-block:: python

   from xblock.core import XBlockAside


   class FeedbackBadgeAside(XBlockAside):
       """Adds a feedback link to learner-facing views of supported blocks."""

The class name does not need to match the entry point name, but keeping
them consistent makes debugging easier.

Step 3: Declare fields for course-author control
************************************************

Add a Boolean field that course authors can toggle to enable or disable
the Aside on a per-block basis. Scope the field to ``Scope.settings``,
which means the value is stored per block and travels with the course in
OLX export and import.

.. code-block:: python

   from xblock.core import XBlockAside
   from xblock.fields import Boolean, Scope


   class FeedbackBadgeAside(XBlockAside):
       """Adds a feedback link to learner-facing views of supported blocks."""

       is_feedback_badge_enabled = Boolean(
           display_name="Show feedback link",
           default=True,
           scope=Scope.settings,
           help="Whether to show a 'Report an issue' link on this block.",
       )

Name the field for the Aside, not generically
(``is_feedback_badge_enabled``, not ``enabled``). This is a real data
safety requirement, not just a readability nicety: on the platform's
Split modulestore, ``Scope.settings`` and ``Scope.content`` fields for
every Aside attached to a given block type are stored in one shared
bucket, keyed by field name — not by which Aside declared the field. A
Boolean field named ``enabled`` on this Aside and an identically-named
``Scope.settings`` field on a completely unrelated, independently
installed Aside attached to the same block type read and write the
*same* stored value. This has been directly reproduced: installing
`ol-openedx-chat`_ and `rapid-response-xblock`_ together with both
renamed to ``enabled`` makes checking one Aside's checkbox in Studio
also check the other's, even though they render different markup and
JavaScript. See :ref:`XBlock Asides Reference` for the mechanism. A
name specific to this Aside — ideally one no other installed Aside is
likely to reuse — is the only real protection against this.

Step 4: Decorate the views you want to inject into
**************************************************

Add one method per XBlock view you want to decorate, using
:meth:`~xblock.core.XBlockAside.aside_for`. The method takes ``self``,
the host ``block``, and an optional ``context`` dictionary, and returns
a :class:`~web_fragments.fragment.Fragment`.

The learner-facing view is straightforward — a link, gated on the
field:

.. code-block:: python

   from web_fragments.fragment import Fragment
   from xblock.core import XBlockAside
   from xblock.fields import Boolean, Scope


   class FeedbackBadgeAside(XBlockAside):
       """Adds a feedback link to learner-facing views of supported blocks."""

       is_feedback_badge_enabled = Boolean(
           display_name="Show feedback link",
           default=True,
           scope=Scope.settings,
           help="Whether to show a 'Report an issue' link on this block.",
       )

       @XBlockAside.aside_for("student_view")
       def student_view_aside(self, block, context=None):
           """Render the feedback link for the learner view."""
           if not self.is_feedback_badge_enabled:
               return Fragment("")

           block_id = block.scope_ids.usage_id.block_id
           html = (
               f'<a class="feedback-badge" '
               f'href="/feedback?block={block_id}">Report an issue</a>'
           )
           return Fragment(html)

The author-facing toggle is where it's worth taking more care. Decorate
``author_view``, not ``studio_view``. This isn't a style preference:
Studio's own aside-rendering machinery only splices an Aside's fragment
into the views it treats as preview views — ``student_view``,
``public_view``, and ``author_view`` — and ``studio_view`` isn't one of
them, so an Aside decorating ``studio_view`` never actually appears in
Studio's unit editor. ``author_view`` is also what production asides
such as `ol-openedx-chat`_ use for exactly this purpose.

Add a small helper for loading the package's static files, and use it
to render the checkbox from a template instead of building HTML inline:

.. code-block:: python

   import pkg_resources


   def resource_string(path):
       """Load a static resource from this package as a decoded string."""
       return pkg_resources.resource_string(__name__, path).decode("utf8")


   class FeedbackBadgeAside(XBlockAside):
       # ... fields and student_view_aside from above ...

       @XBlockAside.aside_for("author_view")
       def author_view_aside(self, block, context=None):
           """Render the author-facing toggle in Studio's unit preview."""
           html = resource_string("static/html/studio_view.html").format(
               checked="checked" if self.is_feedback_badge_enabled else "",
           )
           fragment = Fragment(html)
           fragment.add_css(resource_string("static/css/studio.css"))
           fragment.add_javascript(resource_string("static/js/studio.js"))
           fragment.initialize_js("FeedbackBadgeStudioInit")
           return fragment

``static/html/studio_view.html`` — note the ``{checked}`` placeholder,
filled in by the ``.format()`` call in ``author_view_aside`` above, so
this is shown as plain text rather than as HTML:

.. code-block:: text

   <label class="feedback-badge-toggle-label">
     <input type="checkbox" {checked} class="feedback-badge-toggle">
     Show feedback link
   </label>

Note what this method does *not* do: it doesn't pass the checkbox state
through ``initialize_js``'s ``json_args`` parameter. That parameter
exists and is useful — ``student_view_aside`` could use it to hand
learner-facing JavaScript some initial state — but ``author_view_aside``
here gets its state a different way, by rendering it directly into the
HTML template's ``checked`` attribute. Keep the two mechanisms distinct
in your own Asides: use template context for what the initial markup
should look like, and ``json_args`` for values your JavaScript needs
after the page has already loaded.

The checkbox doesn't do anything yet — clicking it doesn't persist the
change. That's Step 5.

Step 5: Add a handler to persist the toggle
********************************************

Add an AJAX handler, using the standard ``@XBlock.handler`` decorator,
that reads the posted value and saves it to the field:

.. code-block:: python

   import json

   from webob import Response
   from xblock.core import XBlock


   class FeedbackBadgeAside(XBlockAside):
       # ... fields and view methods from above ...

       @XBlock.handler
       def update_config(self, request, suffix=""):
           """Persist the course author's toggle setting."""
           data = json.loads(request.body)
           self.is_feedback_badge_enabled = bool(data.get("is_enabled", True))
           return Response(json_body={"is_enabled": self.is_feedback_badge_enabled})

This is a normal XBlock handler — an Aside's handlers work exactly like
an XBlock's, and the runtime generates a handler URL for the Aside the
same way it does for the host block.

Step 6: Add the JavaScript that wires up the checkbox
*******************************************************

The checkbox needs client-side code to listen for changes and call the
handler. ``static/js/studio.js``:

.. code-block:: javascript

   function FeedbackBadgeStudioInit(runtime, element) {
     var studioRuntime = new window.StudioRuntime.v1();
     var handlerUrl = studioRuntime.handlerUrl(element, "update_config");
     var checkbox = element.querySelector(".feedback-badge-toggle");

     checkbox.addEventListener("change", function () {
       $.ajax({
         type: "POST",
         url: handlerUrl,
         data: JSON.stringify({is_enabled: checkbox.checked}),
       }).done(function () {
         runtime.notify("save", {state: "end"});
       });
     });
   }

Two things worth noting, both taken from how `ol-openedx-chat`_ does
this in production:

* Use ``new window.StudioRuntime.v1()`` to get a runtime capable of
  building the handler URL, rather than the ``runtime`` argument
  ``initialize_js`` passes in directly — this is what Studio's
  JavaScript environment expects for saving Aside/XBlock data.
* Don't add a CSRF header to the request yourself. Studio already
  attaches one globally for every ``$.ajax``/``$.post`` call
  (``cms/static/cms/js/main.js`` calls ``$.ajaxSetup`` with the CSRF
  token once, at page load), and the platform's own Aside JavaScript
  (``cms/static/js/xblock_asides/structured_tags.js``) relies on this
  without adding its own header. Adding one yourself is redundant at
  best.

If your package also needs to tell the Authoring MFE that the embedded
unit page's content changed — for example, because the surrounding UI
needs to react to the save — post a ``saveEditedXBlockData`` message
to ``document.referrer`` after a successful save, the same message
`ol-openedx-chat`_'s own ``studio.js`` sends:

.. code-block:: javascript

       }).done(function () {
         runtime.notify("save", {state: "end"});
         window.parent.postMessage(
           {type: "saveEditedXBlockData"},
           document.referrer
         );
       });

``frontend-app-authoring`` listens for exactly this message type to
know the embedded unit iframe changed. This is a deliberate integration
point that already exists between Studio's Aside JavaScript and the
Authoring MFE, not incidental boilerplate — include it if your Aside's
save should be reflected in the surrounding MFE UI. This is also used to
enable the "Publish" button in the Authoring MFE when an Aside's checkbox
is toggled, otherwise, reloading the page will enable the "Publish" button.

Step 7: Filter to specific block types
**************************************

By default, an Aside applies to every block. Override
:meth:`~xblock.core.XBlockAside.should_apply_to_block` to restrict the
Aside to the block types you support.

.. code-block:: python

   @classmethod
   def should_apply_to_block(cls, block):
       """Apply this Aside to Problem and Video blocks only."""
       block_type = getattr(block, "category", None)
       return block_type in {"problem", "video"}

Add this classmethod to ``FeedbackBadgeAside``. Without it, the Aside
would attempt to render on every block in every course, including blocks
where the markup makes no sense.

For more sophisticated filtering, ``should_apply_to_block`` can also
inspect:

* ``block.scope_ids.usage_id.context_key`` to gate on a course or
  library.
* Platform feature flags such as Waffle flags.
* Course-level settings retrieved through a runtime service.

If your filter consults course settings or feature flags, guard against
the import and export paths where these may not be available; see
:ref:`About XBlock Asides` for the relevant limitations.

.. _register entry point:

Step 8: Register the Aside as an entry point
********************************************

In ``pyproject.toml``, add an entry point in the ``xblock_asides.v1``
group. The entry point name on the left side of the equals sign becomes
the Aside's type name and is used as the XML tag during OLX
serialization.

.. code-block:: toml

   [project.entry-points."xblock_asides.v1"]
   feedback_badge = "feedback_badge_aside.Aside:FeedbackBadgeAside"

Choose a type name that is unlikely to collide with other asides on the
same deployment. Treat the name as a stable public identifier; renaming
it later breaks OLX round-trips of any course that has used the Aside.

Step 9: Install the package and restart services
************************************************

Install the package into the LMS and Studio Python environments. With
Tutor:

.. code-block:: bash

   tutor mounts add lms,cms:/path/to/feedback_badge_aside:/openedx/feedback_badge_aside
   tutor dev exec lms bash
   pip install -e /openedx/feedback_badge_aside
   exit
   tutor dev restart lms
   tutor dev exec cms bash
   pip install -e /openedx/feedback_badge_aside
   exit
   tutor dev restart cms

Step 10: Enable asides in the LMS and Studio
*********************************************

The LMS and Studio each gate Aside rendering on their own, separate
Django configuration model. Enabling one does not enable the other.

**LMS.** ``XBlockAsidesConfig``, defined in
``lms/djangoapps/lms_xblock/models.py``. Until this model has an
enabled revision, no Aside renders in the LMS regardless of
installation or registration. Open the LMS Django admin and create a
new configuration revision:

.. code-block:: text

   http://<your-lms-host>/admin/lms_xblock/xblockasidesconfig/

Click :guilabel:`Add`, check :guilabel:`Enabled`, and save. The model is
a ``ConfigurationModel`` (revision-based), so each save creates a new
revision and the most recent enabled revision is treated as current.

The same form has a ``Disabled blocks`` field, a space-separated list of
block types on which asides will **never** render in the LMS. The
default value is ``about course_info static_tab``. If your Aside should
apply to one of these block types, remove that type from the list.

There is no per-course allowlist and no per-Aside-type allowlist. Once
``XBlockAsidesConfig`` is enabled and your Aside's host block type is
not in ``disabled_blocks``, the runtime offers your Aside to every
matching block in every course. Per-Aside filtering happens through
your Aside's own ``should_apply_to_block`` classmethod, which you wrote
in Step 7.

**Studio.** A separate model, ``StudioConfig``, defined in
``cms/djangoapps/xblock_config/models.py``, gates Aside rendering in
Studio — the LMS model above has no effect there. It has the same
shape (an ``enabled`` flag and a ``disabled_blocks`` field, same
default) and the same admin workflow, at a different URL:

.. code-block:: text

   http://<your-studio-host>/admin/xblock_config/studioconfig/

Both models are ``ConfigurationModel`` rows that default to
``enabled=False``, so out of the box your Aside renders in neither the
LMS nor Studio until you explicitly enable the model for each.

If your project uses the new Authoring MFE, there's no separate switch
to look for there: the MFE's unit editor embeds the same legacy Studio
unit page this ``StudioConfig`` setting controls, inside an iframe. Once
``StudioConfig`` is enabled, the ``author_view`` checkbox from Step 4
appears inside that embedded page when authors edit a unit in the new
MFE, exactly as it does in legacy Studio.

Step 11: Verify the Aside is rendering
***************************************

Open a course that contains a Problem or Video block, view it as a
learner, and confirm the feedback link appears at the bottom of the
block. To verify the author-side UI, open the same block's unit page in
Studio (or the Authoring MFE) and confirm the checkbox appears in the
author view. Click it, reload the page, and confirm the checkbox keeps
its new state — that confirms the handler from Step 5 is actually
persisting the value, not just rendering it once.

If the Aside does not appear at all:

#. Check that the entry point is registered. Run:

   .. code-block:: python

      from xblock.core import XBlockAside
      print(list(XBlockAside.load_classes()))

   in a Django shell. Your Aside's type name should be in the list. If
   it's missing, check the LMS/Studio logs for a ``log.warning`` about
   failing to load your Aside's entry point — a broken import in your
   package is dropped silently at this stage, with the Aside simply
   absent from the list above and no other error anywhere.
#. Check that ``should_apply_to_block`` returns ``True`` for the block
   you are testing.

If the Aside's fragment shows an error instead of your content, that's
a different situation: an exception was raised inside a view method
(``student_view_aside`` or ``author_view_aside``) or inside
``should_apply_to_block`` itself, after the Aside was already found and
loaded. None of these fail silently, in either environment: an
exception in ``author_view_aside`` or in ``should_apply_to_block``
renders as an error block on the unit page in Studio, and an exception
in ``student_view_aside`` or in ``should_apply_to_block`` renders as an
error block in the Learning MFE. Check the corresponding logs for the
underlying exception either way.

Step 12: Talk to the Learning MFE via postMessage (optional)
**************************************************************

If your Aside needs to reach beyond its own iframe — to trigger
something in the surrounding Learning MFE page — use ``postMessage``.
This step is optional; skip it if your Aside's UI is self-contained.

For simple cases, the Learning MFE already recognizes a few built-in
message types with no extra setup on either side. For example, to
open a modal from your Aside's learner-facing JavaScript:

.. code-block:: javascript

   window.parent.postMessage(
     {type: "plugin.modal", payload: {open: true}},
     learningMfeBaseUrl
   );

(Avoid ``plugin.resize`` for this purpose — the host page already posts
it on its own from a document-size observer, so an Aside posting the
same type competes with that loop instead of adding a new capability.)

For anything the built-in types don't cover — a custom drawer, a
bespoke widget — post your own message type, and pair it with a
listener you register yourself:

.. code-block:: javascript

   window.parent.postMessage(
     {type: "your-namespace::your-event", payload: {...}},
     learningMfeBaseUrl
   );

Nothing in ``frontend-app-learning`` reacts to a made-up type by
default, so this only works once something is listening for it. That
listener is a deployment-time addition — the Learning MFE loads an
``env.config.jsx`` file at startup that can run arbitrary side-effect
JavaScript, including dynamically importing and initializing a small
script that does its own ``window.addEventListener("message", ...)``,
checks ``event.origin`` and ``event.data.type``, and mounts whatever UI
it wants in response. Neither half of this requires forking or
patching ``frontend-app-learning``.

Get ``learningMfeBaseUrl`` from the server side and pass it into your
fragment's JavaScript through ``initialize_js``'s ``json_args``, rather
than guessing at a URL client-side — a mismatched target origin drops
the message with no console error on either end. `ol-openedx-chat`_
sources this value from ``settings.LEARNING_MICROFRONTEND_URL``.

MIT Open Learning's "AskTIM" chat button is a complete, running example
of this whole pattern: `ol-openedx-chat`_'s ``ai_chat.js`` posts a
custom message type to the Learning MFE, and a small companion script
MIT deploys alongside the MFE (built on `smoot-design`_'s
``AiDrawerManager``, registered through their own ``env.config.jsx``)
listens for it and opens a chat drawer. Treat it as a reference to read,
not a dependency to add — the pattern works with any custom message
type and any listener you write yourself. See :ref:`XBlock Asides
Reference` for the full mechanics.

Next Steps
**********

Once the basic Aside is working, common follow-ups include:

* **Persist user-specific state.** Add fields with ``Scope.user_state``
  to store per-learner data alongside the Aside — but only save them
  from a handler invoked in the LMS. Saving a ``Scope.user_state``
  field from a handler while the Aside runs under Studio raises
  ``xblock.exceptions.InvalidScopeError``; see :ref:`XBlock Asides
  Reference` for why.
* **Customize layout.** If you need the Aside to render somewhere other
  than after the host block, override the runtime's ``layout_asides``
  in your platform integration.
* **Study more real-world Asides.** `ol-openedx-chat`_ (MIT Open
  Learning) and the platform's own `StructuredTagsAside`_ show two more
  points on the spectrum of author-facing configuration — see
  :ref:`About XBlock Asides` for a tour of all of them.

For the complete API surface, see :ref:`XBlock Asides Reference`. For
the conceptual background, including known limitations of the Aside
mechanism, see :ref:`About XBlock Asides`.

.. seealso::

   :ref:`About XBlock Asides` (concept)
       Why asides exist, what problem they solve, and current limitations.

   :ref:`XBlock Asides Reference` (reference)
       The complete API surface for ``XBlockAside`` and its runtime hooks.

   :ref:`XBlock Aside Quickstart` (quickstart)
       A beginner-friendly walkthrough from zero to a running Aside.

.. _ol-openedx-chat: https://github.com/mitodl/open-edx-plugins/tree/main/src/ol_openedx_chat
.. _rapid-response-xblock: https://github.com/mitodl/open-edx-plugins/tree/main/src/rapid_response_xblock
.. _StructuredTagsAside: https://github.com/openedx/openedx-platform/blob/release/verawood/cms/lib/xblock/tagging/tagging.py#L17
.. _smoot-design: https://github.com/mitodl/smoot-design

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
