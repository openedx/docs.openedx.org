.. _XBlock Asides Reference:

#######################
XBlock Asides Reference
#######################

.. tags:: developer, reference

This reference describes the public API surface for XBlock Asides as
defined in the ``xblock`` package. It covers the
:class:`~xblock.core.XBlockAside` base class, the decorators and
classmethods that subclasses use, the runtime hooks that govern Aside
discovery and rendering, the entry point group that registers asides as
plugins, and the OLX serialization contract.

For an introduction to what asides are and when to use them, see
:ref:`About XBlock Asides`. For a guided walkthrough, see
:ref:`Add an XBlock Aside` or :ref:`XBlock Aside Quickstart`.

.. contents:: Contents
   :local:
   :depth: 1

The XBlockAside Class
*********************

The base class for all asides is ``xblock.core.XBlockAside``. It inherits
from ``Plugin`` and ``Blocklike``, so an Aside can declare scoped fields,
mark methods as handlers, and be loaded as a plugin in the same way as an
XBlock.

.. code-block:: python

   from xblock.core import XBlockAside

   class MyAside(XBlockAside):
       """An Aside that decorates one or more XBlock views."""

Class Attributes
================

``entry_point``
   The Python entry point group used to discover Aside plugins. Set on the
   base class to ``"xblock_asides.v1"``. Subclasses should not change this.

``fields``
   The set of fields declared on the Aside, automatically collected from
   class-level :class:`~xblock.fields.Field` declarations. Inherited from
   ``Blocklike``.

Decorators
**********

``XBlockAside.aside_for(view_name)``
====================================

A classmethod decorator that marks a method as the Aside view for the
named XBlock view. When the runtime renders an XBlock view called
``view_name``, every applicable Aside whose class declares a method
decorated with ``@XBlockAside.aside_for(view_name)`` is invoked, and the
returned fragments are appended to the host block's rendered fragment.

**Signature of the decorated method**

.. code-block:: python

   @XBlockAside.aside_for("student_view")
   def student_view_aside(self, block, context=None):
       ...
       return Fragment(...)

The decorated method takes:

* ``self`` — the Aside instance.
* ``block`` — the host XBlock instance being rendered.
* ``context`` — an optional dictionary of context data passed by the
  caller of ``render``.

The method must return a :class:`~web_fragments.fragment.Fragment`.

**Multiple views per Aside**

A single method may decorate multiple views by stacking decorators, and a
single Aside class may define different methods for different views.

.. code-block:: python

   class MyAside(XBlockAside):

       @XBlockAside.aside_for("student_view")
       def student_view_aside(self, block, context=None):
           return Fragment("<div>Student-side Aside</div>")

       @XBlockAside.aside_for("author_view")
       @XBlockAside.aside_for("studio_view")
       def studio_aside(self, block, context=None):
           return Fragment("<div>Author/Studio Aside</div>")

**Common view names**

The view names commonly decorated by asides include:

+----------------------+---------------------------------------------------+
| View name            | When the runtime renders it                       |
+======================+===================================================+
| ``student_view``     | The learner-facing view of a block in the LMS.    |
+----------------------+---------------------------------------------------+
| ``author_view``      | The author-facing preview of a block in Studio.   |
+----------------------+---------------------------------------------------+
| ``studio_view``      | The author-facing edit form of a block in Studio. |
+----------------------+---------------------------------------------------+

XBlocks may define additional views; an Aside can decorate any of them by
name.

Classmethods
************

``XBlockAside.should_apply_to_block(cls, block)``
=================================================

A classmethod that returns ``True`` if the Aside should apply to the given
``block``, and ``False`` otherwise. The default implementation returns
``True`` unconditionally.

Override this method to restrict the Aside to specific block types,
courses, or feature flags. The runtime calls this method on every
Aside-block pair before rendering, and asides for which it returns
``False`` are skipped.

.. code-block:: python

   @classmethod
   def should_apply_to_block(cls, block):
       block_type = getattr(block, "category", None)
       return block_type in {"problem", "video"}

The ``block`` argument is the host XBlock instance. Most filtering logic
inspects ``block.scope_ids.block_type``, ``block.category``, the course
context derived from ``block.scope_ids.usage_id``, or platform feature
flags.

Instance Methods
****************

``aside_view_declaration(view_name)``
=====================================

Return the bound method on this Aside instance that is decorated with
``@XBlockAside.aside_for(view_name)``, or ``None`` if no such method
exists. The runtime uses this method to look up the Aside's view function
when rendering. Subclasses do not normally need to call it directly.

``needs_serialization()``
=========================

Return ``True`` if the Aside has any field whose value differs from its
default. The default implementation iterates over the Aside's fields and
returns ``True`` if any field is set on this instance. The runtime calls
this method during OLX export to decide whether to serialize the Aside as
an XML element. Subclasses rarely need to override this.

``parse_xml(node, runtime, keys)`` and ``add_xml_to_node(node)``
================================================================

Inherited from ``Blocklike``. Override these to customize how the Aside is
read from and written to OLX. The default implementations serialize the
Aside's fields as XML attributes and child elements, identical to the
default XBlock behavior.

Fields and Scopes
*****************

An Aside declares fields the same way an XBlock does, with class-level
field declarations. Fields are scoped, and the scope determines where the
field's value is stored and which entities share it.

.. code-block:: python

   from xblock.core import XBlockAside
   from xblock.fields import Boolean, Scope, String

   class MyAside(XBlockAside):
       enabled = Boolean(
           display_name="Enabled",
           default=False,
           scope=Scope.settings,
           help="Whether this Aside is active for this block.",
       )

       last_message = String(
           default="",
           scope=Scope.user_state,
           help="The most recent message for this user-block pair.",
       )

Before saving a field like ``last_message`` from a handler, see the
valid-scopes caveat below — saving a ``Scope.user_state`` field while
an Aside runs under Studio raises an error.

The supported scopes are the standard XBlock scopes from
:mod:`xblock.fields`: ``Scope.content``, ``Scope.settings``,
``Scope.user_state``, ``Scope.user_state_summary``,
``Scope.preferences``, and ``Scope.user_info``. An Aside's field values
are conceptually stored under the Aside's own usage ID, separate from
the host block's field values — but do not assume this means two
different Aside classes can safely share a field name, even though the
abstract ``xblock`` package's own key-construction logic embeds the
Aside's entry-point type into that usage ID.

**On the platform's Split modulestore — the default and current
modulestore — same-named ``Scope.content``/``Scope.settings`` fields on
different Asides collide, confirmed in practice.** The KVS the platform
actually uses to store course-structure data
(``SplitMongoKVS``, in ``xmodule/modulestore/split_mongo/split_mongo_kvs.py``)
buckets Aside field storage by the *host block's* type
(``key.block_scope_id.block_type``), not the Aside's own type — every
Aside attached to a given block type shares one dictionary of field
name to value for that block. The read path
(``xmodule/modulestore/split_mongo/runtime.py``) reinforces this: it
pre-merges every attached Aside's persisted fields into that single
per-block-type dictionary before any individual Aside instance is
even constructed. Two Aside classes attached to the same block type
that both declare a field named, say, ``enabled``, read and write the
*same* stored value — checking one Aside's checkbox in Studio's author
view can visibly and functionally check the other Aside's checkbox
too, even when the two Asides use entirely different JavaScript and
DOM selectors, because the underlying field value they're both bound
to really is the same one. Last-write-wins on export, too. This has
been directly reproduced with `ol-openedx-chat`_ and
`rapid-response-xblock`_ installed together, sharing a field name.

Choose a field name that no other Aside on your deployment is likely
to use — the confirmed collision above makes this a real data-safety
requirement, not just a debugging convenience. This is separate from,
and adds to, the render- and JavaScript-layer interference described
in the :ref:`About XBlock Asides` concept doc's "Multiple Asides on a
Single Block Are Not Reliable" limitation.

**Only ``Scope.content`` and ``Scope.settings`` can be saved while an
Aside is running under Studio, confirmed in practice.**
``xmodule/modulestore/split_mongo/split_mongo_kvs.py:24`` defines
``SplitMongoKVS.VALID_SCOPES = (Scope.parent, Scope.children,
Scope.settings, Scope.content)`` — the two internal structural scopes,
plus the two course-structure scopes discussed above. Every other
field scope (``Scope.user_state``, ``Scope.user_state_summary``,
``Scope.preferences``, ``Scope.user_info``) is absent from that list.
Calling a handler that persists a field in one of those scopes (any
code path that reaches ``block.save()`` → ``force_save_fields`` →
``_field_data.set_many`` → the KVS's ``set``/``set_many``) raises
``xblock.exceptions.InvalidScopeError`` from that same ``set()``
method, because Studio's preview and author-view rendering is backed
by ``SplitMongoKVS``. This is distinct from the field-collision
problem above: it isn't that two Asides' values might collide, it's
that persisting a field in any of these four excluded scopes raises an
error in Studio at all, regardless of naming. If your Aside needs one
of these scopes for the learner-facing view, expect it to work only
through the LMS's runtime (not backed by ``SplitMongoKVS``), and never
invoke a save of such a field from a Studio-side handler or author
view.

Handlers
********

An Aside can define AJAX handlers using the standard
``@XBlock.handler`` decorator from ``xblock.core``. The handler URL is
generated by the runtime in the same way as for an XBlock, so an Aside's
view fragment can call its own handler with
``self.runtime.handler_url(self, "handler_name")``.

.. code-block:: python

   from xblock.core import XBlock, XBlockAside

   class MyAside(XBlockAside):

       @XBlock.handler
       def submit_feedback(self, request, suffix=""):
           ...
           return Response(json_body={"ok": True})

The handler signature, request object, and response handling are
identical to XBlock handlers.

Entry Point Registration
************************

An Aside is discovered by the runtime through a Python entry point in the
``xblock_asides.v1`` group. Declare the entry point in the package's
``pyproject.toml``:

.. code-block:: toml

   [project.entry-points."xblock_asides.v1"]
   my_aside = "my_package.Aside:MyAside"

Or in ``setup.py``:

.. code-block:: python

   setup(
       entry_points={
           "xblock_asides.v1": [
               "my_aside = my_package.Aside:MyAside",
           ],
       },
   )

The entry point name on the left of the equals sign is the Aside's
**type name**. It is used as the XML tag when the Aside is serialized to
OLX, and as the key in :class:`~xblock.scopes.ScopeIds` when an Aside
instance is constructed. Choose a name that is unique across all
installed asides on a deployment.

Entry points are loaded through ``XBlockAside.load_classes()``, which
defaults to ``fail_silently=True``: if an Aside's module raises an
exception on import, the loader logs a warning and simply omits that
Aside from the registered list, rather than raising. A broken Aside
package can therefore fail to load with no error visible anywhere
except the log — see :ref:`Add an XBlock Aside` for how this shows up
in practice when troubleshooting a missing Aside.

Runtime API
***********

The methods listed below are defined on
:class:`~xblock.runtime.Runtime` and govern Aside discovery, instantiation,
and rendering. Aside subclasses do not normally call these directly. They
are documented here so runtime implementors and Aside authors can
understand the lifecycle.

Discovery
=========

``runtime.applicable_aside_types(block)``
   Return the list of Aside type names that may apply to ``block``. The
   default implementation returns every Aside class registered through
   the ``xblock_asides.v1`` entry point. A runtime may override this to
   filter by user, course, or other context.

   The edx-platform LMS runtime overrides this through
   ``lms_applicable_aside_types`` in
   ``lms/djangoapps/lms_xblock/runtime.py``, which gates Aside rendering
   on the ``XBlockAsidesConfig`` Django configuration model. When the
   model's current revision has ``enabled=False``, no asides render in
   the LMS. When enabled, asides do not render on block types listed in
   the model's ``disabled_blocks`` field (default value:
   ``"about course_info static_tab"``).

   **Studio has its own, separate gate.** The CMS overrides Aside
   discovery independently, through ``preview_applicable_aside_types``
   in ``cms/djangoapps/contentstore/views/preview.py``, which consults
   ``StudioConfig.asides_enabled(block_type)`` — a second
   ``ConfigurationModel``, defined in
   ``cms/djangoapps/xblock_config/models.py``, with the same shape as
   ``XBlockAsidesConfig`` (an ``enabled`` flag plus a ``disabled_blocks``
   field, same default: ``"about course_info static_tab"``). This gate
   applies to every preview view Studio
   renders for a block — ``student_view``, ``public_view``, and
   ``author_view`` alike — not just one of them.

   ``XBlockAsidesConfig`` and ``StudioConfig`` are two independent
   ``ConfigurationModel`` rows. Like every ``ConfigurationModel``, each
   one defaults to ``enabled=False`` until an operator explicitly saves
   an enabled revision, so out of the box **no Aside renders in either
   the LMS or Studio**, regardless of installation or registration.
   Enabling one does not enable the other — an operator who wants an
   Aside to render in both the LMS and Studio must enable both models.
   See :ref:`Add an XBlock Aside` for the administrative steps.

   **Asides in the Authoring MFE.** The Authoring micro-frontend has no
   native code for rendering or toggling Asides. Its unit editor page
   embeds the legacy Studio unit page in an iframe
   (``container_embed_handler`` in
   ``cms/djangoapps/contentstore/views/component.py``), so an Aside's
   ``author_view`` fragment — gated by ``StudioConfig`` exactly as
   described above — appears inside that iframe when authors use the
   new MFE. There is no separate MFE-specific toggle. The embedded page
   and the MFE are not otherwise isolated: they already exchange a real
   ``postMessage`` today (a ``saveEditedXBlockData`` message the
   embedded page sends after a save, which the MFE listens for — see
   :ref:`Add an XBlock Aside` for where this shows up in an Aside's own
   JavaScript).

``runtime.load_aside_type(aside_type)``
   Return the :class:`XBlockAside` subclass corresponding to the given
   ``aside_type`` string. Raises if no Aside is registered under that
   name.

Instantiation
=============

``runtime.create_aside(block_type, keys)``
   Construct an Aside instance of the named ``block_type`` (the Aside
   type name, despite the parameter name) with the given ``ScopeIds``.
   Returns an :class:`XBlockAside` instance.

``runtime.get_aside_of_type(block, aside_type)``
   Construct an Aside of the named type that is bound to the given host
   ``block``. Generates the Aside's definition and usage IDs from the
   host block's IDs using the runtime's ``id_generator``. Returns an
   :class:`XBlockAside` instance.

``runtime.get_aside(aside_usage_id)``
   Construct an Aside instance from a previously known Aside usage ID.
   Used during OLX import and other paths where the Aside's identity is
   already established.

``runtime.get_asides(block)``
   Return the list of Aside instances that should decorate the given
   ``block``. This method composes ``applicable_aside_types`` and each
   Aside's ``should_apply_to_block`` filter, returning only the asides
   for which both pass.

Rendering
=========

``runtime.render_asides(block, view_name, frag, context)``
   Called by the runtime's ``render`` method after the block's own view
   has produced its fragment. Iterates over ``get_asides(block)``, looks
   up each Aside's view declaration for ``view_name``, and dispatches
   layout to ``layout_asides``. Returns the augmented
   :class:`Fragment`.

``runtime.layout_asides(block, context, frag, view_name, aside_frag_fns)``
   Execute the Aside view functions and combine their fragments with the
   block's fragment. The default implementation appends each Aside's
   wrapped fragment after the block's fragment. Override this to control
   the placement, ordering, or conditional inclusion of asides. Any
   override must call ``wrap_aside`` around each Aside fragment to
   preserve client-side identification.

``runtime.wrap_aside(block, Aside, view, frag, context)``
   Wrap an Aside's fragment with a ``<div>`` carrying the Aside's usage
   ID, the host block's usage ID, and any JavaScript initialization
   metadata. Override this if you need a different wrapping element or
   different ``data-`` attributes.

Talking to the Learning MFE via postMessage
********************************************

An Aside's fragment renders inside the same iframe as its host XBlock
whenever the Learning micro-frontend displays that block, so an Aside's
own JavaScript can use the browser's ``postMessage`` API to reach the
parent MFE page. There are three layers to this, from "already works"
to "build your own":

**Built-in message types.** ``frontend-app-learning`` listens for a
small set of message types on the iframe's parent window, split across
two hooks: ``useIFrameBehavior.ts`` (``plugin.resize``,
``plugin.videoFullScreen``, ``plugin.autoAdvance``, and a bare
``{ offset }`` scroll message) and ``useModalIFrameData.js``
(``plugin.modal`` / ``plugin.modal-close``). Both listeners branch only
on ``event.data.type`` and never check the sender, so any Aside can
trigger them with no MFE-side changes:

.. code-block:: javascript

   window.parent.postMessage(
       {type: 'plugin.modal', payload: {open: true}},
       learningMfeBaseUrl
   );

Avoid reusing ``plugin.resize`` for this purpose — the host page
already posts it from its own document-size observer on every DOM
mutation, so an Aside posting the same type competes with that loop
instead of adding a new capability. ``plugin.modal`` has no such
collision.

**Custom message type plus your own listener — the general recipe.**
The four built-in types above are the only ones ``frontend-app-learning``
recognizes out of the box. For anything else — a custom drawer, a
bespoke widget — an Aside can still post a message with any ``type`` it
likes, but something has to be listening for it. That "something" is a
deployment-time customization, not a core MFE feature: the Learning
MFE loads an ``env.config.jsx`` file at startup (the standard Open edX
MFE runtime-configuration mechanism), which can run arbitrary
side-effect JavaScript in addition to ordinary config values — for
example, dynamically importing and initializing a small script that
does its own ``window.addEventListener('message', ...)``, checks
``event.origin`` against an allow-listed origin and ``event.data.type``
against the string(s) it cares about, and mounts whatever UI it wants
in response. The recipe has two halves:

#. The Aside's JavaScript posts
   ``{type: 'your-namespace::your-event', payload: {...}}`` to a known
   target origin.
#. The Learning MFE's ``env.config.jsx`` (or equivalent build-time
   customization) registers a listener for that exact type and origin.

Neither half requires forking or patching ``frontend-app-learning``
itself.

**A working example of the pattern.** MIT Open Learning's
`ol-openedx-chat`_ Aside implements exactly this: its
``ai_chat.js`` posts ``{type: "smoot-design::tutor-drawer-open", ...}``
to a target origin sourced from ``settings.LEARNING_MICROFRONTEND_URL``
(passed into the fragment's JavaScript through
``initialize_js(json_args=...)``, which is the safer, explicit
convention — prefer it over relying on ``document.referrer``). On the
receiving side, MIT's deployment injects `smoot-design`_'s
``AiDrawerManager`` bundle through their own ``env.config.jsx``, which
listens for that exact message type (and its current name,
``smoot-design::ai-drawer-open``) and mounts a chat drawer. This is
cited as one concrete, running implementation of the pattern above, not
as something every deployment needs to depend on — an operator can
build an equivalent listener around any custom message type without
using MIT's packages at all.

OLX Serialization
*****************

When a course is exported to OLX, the runtime serializes every Aside
that returns ``True`` from ``needs_serialization()`` as an XML child
element of its host block. The XML tag of the Aside element is the
Aside's entry point name. Field values are written as attributes or
nested elements according to the Aside's ``add_xml_to_node``
implementation.

On import, the runtime detects Aside elements by looking up their tag
names in the registered ``xblock_asides.v1`` entry points. If a tag
does not resolve to a registered Aside, the import does not raise an
error and does not report a failure — but it also does not simply
drop the Aside element and keep the host block. **The host block that
carried the unresolvable Aside is dropped from the course entirely,**
with no error block, no placeholder, and nothing in the import result
indicating anything went wrong. Field values for any
successfully-matched Aside are read by its ``parse_xml`` implementation
as usual.

Two practical consequences:

* An Aside's data only round-trips through OLX if both the source and
  destination platforms have the same Aside installed under the same
  entry point name. If they don't, the cost isn't limited to that
  Aside's data — the host block goes missing too.
* Some XBlocks do not preserve Aside child elements through their own
  export and import paths. See :ref:`About XBlock Asides` for the
  current list of known issues.

Render Pipeline Summary
***********************

The full sequence of calls when a runtime renders an XBlock view is:

#. ``runtime.render(block, view_name, context)`` is called.
#. The runtime invokes the block's view function and obtains a fragment.
#. The runtime calls ``runtime.wrap_xblock`` on that fragment.
#. The runtime calls ``runtime.render_asides(block, view_name, frag, context)``.
#. ``render_asides`` calls ``runtime.get_asides(block)``, which uses
   ``applicable_aside_types(block)`` and each Aside's
   ``should_apply_to_block(block)`` to compute the filtered list. An
   exception here is not caught by ``xblock`` either — confirmed in
   both Studio and the Learning MFE, it renders as an error block the
   same as an exception raised inside a view method (see the note on
   ``layout_asides`` below).
#. For each surviving Aside, ``render_asides`` calls
   ``Aside.aside_view_declaration(view_name)`` to find the matching
   method.
#. ``render_asides`` calls ``layout_asides``, which invokes each Aside
   view function, calls ``wrap_aside`` on each result, and appends the
   wrapped fragments to the block's fragment. Neither ``xblock`` nor
   ``layout_asides`` catches an exception raised by an Aside's view
   function here — it propagates out of the render call. A platform
   catches it at a higher layer instead: an exception raised inside an
   Aside's ``student_view`` renders as an error block in place of the
   host block in the Learning MFE, and an exception raised inside
   ``author_view`` renders as an error block on the unit page in
   Studio. Either way, a broken Aside visibly breaks its host block's
   display rather than failing invisibly. (This is distinct from an
   Aside failing to *load* as a plugin, which is silent — see "Entry
   Point Registration" above.)
#. The combined fragment is returned to the original caller.

.. seealso::

   :ref:`About XBlock Asides` (concept)
       Why asides exist, what problem they solve, and current limitations.

   :ref:`Add an XBlock Aside` (how-to)
       A step-by-step recipe for adding an Aside to existing XBlocks.

   :ref:`XBlock Aside Quickstart` (quickstart)
       A beginner-friendly walkthrough from zero to a running Aside.

.. _ol-openedx-chat: https://github.com/mitodl/open-edx-plugins/tree/main/src/ol_openedx_chat
.. _rapid-response-xblock: https://github.com/mitodl/open-edx-plugins/tree/main/src/rapid_response_xblock
.. _smoot-design: https://github.com/mitodl/smoot-design

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
