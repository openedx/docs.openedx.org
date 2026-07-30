.. _About XBlock Asides:

###################
About XBlock Asides
###################

.. tags:: developer, concept

An XBlock Aside is a class that injects content into the rendered views of
existing XBlocks without modifying those XBlocks. Asides let you add behavior,
data, and UI elements to many XBlock instances at once, across XBlock types you
do not own, while preserving the host XBlock's code, fields, and Open Learning
XML (OLX) representation.

.. contents:: Contents
   :local:
   :depth: 1

What an Aside Is
****************

An Aside is a Python class that subclasses :class:`~xblock.core.XBlockAside`,
declares one or more view-injection methods using the
:func:`~xblock.core.XBlockAside.aside_for` decorator, and is registered with
the platform through a Python entry point in the ``xblock_asides.v1`` group.
When the platform renders an XBlock view, the runtime collects every
applicable Aside, invokes its matching Aside view, and appends the resulting
fragments to the host XBlock's rendered fragment.

An Aside is **not** a child XBlock. It does not appear in the course outline,
it does not have its own URL, and it cannot be added to a course like a
regular block. It exists only in relation to a host block, and its lifecycle
is bound to that host block's lifecycle.

For the precise API surface, see :ref:`XBlock Asides Reference`.

The Problem Asides Solve
************************

When you want to enhance the behavior of an XBlock that you did not write,
you have three options:

#. Fork the XBlock and modify it directly.
#. Replace the XBlock with a new XBlock that wraps the original.
#. Attach an Aside to the existing XBlock.

The first two options carry significant costs. Forking creates a parallel
codebase that must be maintained against upstream changes. Replacing the
XBlock requires every existing course that uses the original to migrate, and
it does not scale when you want to enhance many different XBlock types in the
same way.

Asides solve this by externalizing the enhancement. The host XBlock is not
modified. The same Aside can apply to a Video block, a Problem block, or any
other block type, by overriding a single classmethod. Asides can serialize
their own scoped fields during course import and export.

Reach for an Aside when all of the following are true:

* You want to enhance one or more existing XBlock types without forking them.
* The enhancement is conceptually layered on top of the block, not a
  replacement for any of its behavior.
* The enhancement should apply to many block instances, possibly across
  block types, without per-instance configuration in the course outline.
* The enhancement may need its own settings or stored data, scoped to the
  block instance.

Reach for something else when:

* You are creating a brand new piece of course content. Write an XBlock.
* You only need to react to platform events. Consider an Open edX event
  receiver.

How an Aside Relates to Its Host Block
**************************************

The runtime maintains a many-to-many relationship between asides and host
blocks at runtime, but each Aside instance is bound to exactly one host block
during a single render. The relationship is established in three stages.

Per-Block Filtering
===================

For each candidate Aside type, the runtime instantiates the Aside and asks
it whether it should apply to this specific block by calling its
:meth:`~xblock.core.XBlockAside.should_apply_to_block` classmethod. The
default implementation returns ``True``. Real-world asides almost always
override this method to restrict themselves to specific block types, course
contexts, or feature flags.

Rendering and Layout
====================

For each Aside that survives filtering, the runtime invokes the Aside method
that was decorated with ``@XBlockAside.aside_for(view_name)`` for the view
being rendered. The Aside method returns a ``Fragment``, the runtime wraps
that fragment with identifying markup, and the runtime appends the wrapped
fragment to the host block's rendered output. A runtime can override
:meth:`~xblock.runtime.Runtime.layout_asides` to control where and how the
Aside fragments are placed.

Why Asides Are Worth the Trouble
********************************

The framing above describes the trade-offs from the perspective of someone
choosing among extension mechanisms. The deeper reasons asides exist, and
remain useful, come from the production deployments that depend on them.

Multiple Block Types, One Implementation
========================================

A single Aside class can decorate Video blocks, Problem blocks, and any
other block type the author chooses, by checking ``block.category`` or
``block.scope_ids.block_type`` inside ``should_apply_to_block``. The MIT
Open Learning chat Aside, for example, attaches an "AskTIM" chat button to
both Video and Problem blocks from a single class, with one entry point.
Without asides, the same outcome would require either two parallel forks
or replacement blocks for both types.

Course Author Control
=====================

An Aside can declare its own scoped fields, just like an XBlock. By exposing
those fields in an author view, an Aside gives course authors a UI to enable
or disable the enhancement on a per-block basis. The settings are stored
under the Aside's own scope, not the host block's, so they are preserved
across exports and imports without any change to the host block's data
model.

OLX Export and Import
=====================

When a course is exported to OLX, the platform serializes each Aside as an
XML child element under its host block, named after the Aside's entry point
name. On import, the runtime reconstitutes the asides automatically. This
means an Aside-enhanced course is portable, with limitations described below.

Reaching Outside the Iframe
============================

An Aside's fragment renders inside the same iframe as its host block, so
its JavaScript is confined to that iframe unless it does something about
it. The browser's ``postMessage`` API is the way out. The Learning
micro-frontend already recognizes a handful of built-in message types
(for things like opening a modal or resizing the frame) that any Aside
can send for free, with no setup. Beyond those, an Aside can post a
message with any custom ``type`` it defines, but nothing reacts to a
made-up type by default — something has to be listening for it. That
listener is a deployment-time addition, registered through the Learning
MFE's own runtime configuration, not a fork of the MFE itself. MIT Open
Learning's "AskTIM" chat button (the `ol-openedx-chat`_ Aside, described
next under "Real-World Examples") works exactly this way: its
JavaScript posts a message, and a small companion script MIT deploys
alongside the MFE listens for it and opens a chat drawer. See
:ref:`XBlock Asides Reference` for the full mechanics and
:ref:`Add an XBlock Aside` for a worked example of both halves.

Real-World Examples
*******************

Three implementations in the wild illustrate the range of what asides can
do, from a bare waffle-flag toggle to a fully wired author-facing UI.

Rapid Response XBlock
=====================

The `rapid-response-xblock`_ from MIT Open Learning is a single Aside that
applies to Problem blocks restricted to a single multiple-choice response
type. It overlays an instructor-only control on the problem in the LMS
that lets a live instructor open and close response windows during a
lecture, and it renders a real-time chart of student responses. A Boolean
field enables or disables it per problem, exposed through a checkbox in
its ``studio_view``; a companion, Django-settings-gated ``author_view``
shows the same checkbox in Studio's author preview. The repository name
calls it an "xblock" but the implementation is purely an Aside.

Open Learning Chat Aside
========================

The `ol-openedx-chat`_ Aside, also from MIT Open Learning, attaches an
"AskTIM" chat button to Video and Problem blocks. The button opens a
context-aware chat drawer that streams messages to a backend large language
model, passing block-specific context such as a video transcript identifier
or a problem's siblings. A single Aside class, registered as one entry
point, handles both block types and uses ``should_apply_to_block`` to gate
on a course-level waffle flag, the block-type check, and a course-level
enabled setting together. A course-author checkbox in its ``author_view``
toggles the button per block, backed by a scoped field and an AJAX handler.
See :ref:`Add an XBlock Aside` for a full walkthrough of this pattern.

Structured Tags Aside
=====================

The `StructuredTagsAside`_ ships with Open edX itself, in
``cms/lib/xblock/tagging/tagging.py``. It attaches a tag picker to
Problem blocks so course authors can apply structured tags for content
search and organization. Unlike the other examples, its entire
author-facing configuration UI *is* its ``AUTHOR_VIEW`` fragment — there
is no separate toggle checkbox, just the tag picker itself, and the
picker only appears at all when Studio's aside-rendering gate (see
:ref:`XBlock Asides Reference`) is enabled. It has no
``should_apply_to_block``
override; it instead checks ``isinstance(block, ProblemBlock)`` inline
inside its view method. Its own author view method is, confusingly,
still named ``student_view_aside`` even though it is decorated for
``AUTHOR_VIEW`` — a reminder that an Aside's view method names are
conventions, not requirements enforced by the framework.

Limitations
***********

Asides are a real, working feature in production deployments, but the
ecosystem around them is incomplete. The list below is drawn from the
state of the codebase as of the Sumac release and from a 2025 Open edX
Conference talk by Peter Pinch of MIT Open Learning. Read it before
committing to an Aside-based design.

No Native Authoring Story in the Course Authoring MFE
======================================================

The Authoring micro-frontend has no native code for rendering or
toggling Asides — it does not know Asides exist. What it does have is
a unit editor that embeds the legacy Studio unit page in an iframe, so
an Aside's ``author_view`` UI (a checkbox, a tag picker, whatever the
Aside renders) shows up inside that embedded page when authors use the
new MFE, exactly as it would in legacy Studio, gated by the same
``StudioConfig`` setting. There is no separate MFE-specific toggle to
configure. The embedded page and the MFE aren't otherwise isolated
from each other, either — they already exchange at least one real
``postMessage`` today. See :ref:`XBlock Asides Reference` for the full
mechanics of both the Studio-side gate and this iframe relationship.

A Host Block Vanishes Silently If Its Aside Is Uninstalled
=============================================================

If a course was authored with an Aside attached to one of its blocks,
and that Aside is later uninstalled or its entry point renamed,
re-importing the course does not raise any error — the import reports
success. What actually happens is worse than losing the Aside's data:
the **host block that carried the Aside is dropped from the course
entirely**. It does not appear as an error block or a placeholder; it
simply isn't there. There is no warning that anything was lost. If you
depend on a course's blocks surviving its lifecycle, treat uninstalling
or renaming an Aside that's in use as a breaking, silent change to
every course that has it attached to a block, and audit affected
courses before doing so.

Not All XBlocks Round-Trip Through OLX
======================================

OLX export and import for asides depends on the host XBlock cooperating
with the export process. Some XBlocks, including ORA2, do not preserve
Aside data through their export and import paths. If your Aside must
survive a course export and re-import on a course that uses one of these
blocks, test the round trip end to end before depending on it. (This is
a different failure mode from the previous limitation: here the host
XBlock is present but doesn't cooperate with serialization; there, the
Aside itself is simply gone.)

Multiple Asides on a Single Block Are Not Reliable
==================================================

The runtime supports multiple Aside types decorating the same block in
principle, but interactions between asides on the same block are not
well-tested, and this goes deeper than rendering. Two Asides attached
to the same block type that happen to declare an identically-named
``Scope.content`` or ``Scope.settings`` field share the *same stored
value* on the platform's Split modulestore, confirmed by directly
installing `ol-openedx-chat`_ and `rapid-response-xblock`_ together
with both fields renamed to ``enabled``: toggling one Aside's checkbox
in Studio's author view visibly checks the other Aside's checkbox too,
even though the two render entirely different markup and JavaScript.
See :ref:`XBlock Asides Reference` for the mechanism. Two Asides that
both decorate ``student_view`` can also render correctly in isolation
and break when combined, independent of field naming. If you need
multiple Asides on the same block type, give every field a name that's
unlikely to collide with another installed Aside, and build a single
Aside that composes the behaviors instead of relying on two independent
Asides to coexist wherever you can.

JavaScript Library Loading Is Limited
=====================================

Asides use the same fragment-based JavaScript loading mechanism as XBlocks,
which assumes a single set of static assets. If your Aside needs a JS
library that is not already loaded by the host page, you must add it
through the fragment, and you must handle ordering and conflicts yourself.
There is no shared Aside-level mechanism for declaring library dependencies.

Where to Go Next
****************

If you are ready to build an Aside, start with :ref:`XBlock Aside Quickstart`.
If you already have a target XBlock in mind and want a step-by-step recipe, read
:ref:`Add an XBlock Aside`. For the complete list of classes, decorators,
methods, and entry points, consult :ref:`XBlock Asides Reference`. The
`rapid-response-xblock`_, `ol-openedx-chat`_, and `StructuredTagsAside`_
implementations described above are also worth reading directly as
reference material.

.. _rapid-response-xblock: https://github.com/mitodl/open-edx-plugins/tree/main/src/rapid_response_xblock
.. _ol-openedx-chat: https://github.com/mitodl/open-edx-plugins/tree/main/src/ol_openedx_chat
.. _StructuredTagsAside: https://github.com/openedx/openedx-platform/blob/release/verawood/cms/lib/xblock/tagging/tagging.py#L17

.. seealso::

   :ref:`XBlock Asides Reference` (reference)
       The complete API surface for ``XBlockAside`` and its runtime hooks.

   :ref:`Add an XBlock Aside` (how-to)
       A step-by-step recipe for adding an Aside to existing XBlocks.

   :ref:`XBlock Aside Quickstart` (quickstart)
       A beginner-friendly walkthrough from zero to a running Aside.

   :ref:`Hooks Extension Framework` (concept)
       An alternative extension mechanism for non-view-based behaviors.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
