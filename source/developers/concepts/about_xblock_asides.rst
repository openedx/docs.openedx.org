.. _About XBlock Asides:

###################
About XBlock Asides
###################

.. tags:: developer, concept

An XBlock aside is a class that injects content into the rendered views of
existing XBlocks without modifying those XBlocks. Asides let you add behavior,
data, and UI elements to many XBlock instances at once, across XBlock types you
do not own, while preserving the host XBlock's code, fields, and Open Learning
XML (OLX) representation.

.. contents:: Contents
   :local:
   :depth: 1

What an Aside Is
****************

An aside is a Python class that subclasses :class:`~xblock.core.XBlockAside`,
declares one or more view-injection methods using the
:func:`~xblock.core.XBlockAside.aside_for` decorator, and is registered with
the platform through a Python entry point in the ``xblock_asides.v1`` group.
When the platform renders an XBlock view, the runtime collects every
applicable aside, invokes its matching aside view, and appends the resulting
fragments to the host XBlock's rendered fragment.

An aside is **not** a child XBlock. It does not appear in the course outline,
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
#. Attach an aside to the existing XBlock.

The first two options carry significant costs. Forking creates a parallel
codebase that must be maintained against upstream changes. Replacing the
XBlock requires every existing course that uses the original to migrate, and
it does not scale when you want to enhance many different XBlock types in the
same way.

Asides solve this by externalizing the enhancement. The host XBlock is not
modified. The same aside can apply to a Video block, a Problem block, or any
other block type, by overriding a single classmethod. Course authors keep
control over whether the enhancement is active for a given block, because
asides expose their own scoped fields. The enhancement travels with the
course in OLX export and import.

Reach for an aside when all of the following are true:

* You want to enhance one or more existing XBlock types without forking them.
* The enhancement is conceptually layered on top of the block, not a
  replacement for any of its behavior.
* The enhancement should apply to many block instances, possibly across
  block types, without per-instance configuration in the course outline.
* The enhancement may need its own settings or stored data, scoped to the
  block instance.

Reach for something else when:

* You are creating a brand new piece of course content. Write an XBlock.
* You need to change a behavior that is internal to a single block type and
  not visible in any view. Consider a runtime service or a filter from the
  Hooks Extension Framework.
* You only need to react to platform events. Consider an Open edX event
  receiver.

How an Aside Relates to Its Host Block
**************************************

The runtime maintains a many-to-many relationship between asides and host
blocks at runtime, but each aside instance is bound to exactly one host block
during a single render. The relationship is established in three stages.

Discovery
=========

When the runtime renders an XBlock view, it asks the runtime for the set of
applicable aside types. The default runtime returns every aside class
registered through the ``xblock_asides.v1`` entry point. A runtime may
override this to filter the set further, for example based on the current
user or the course.

Per-Block Filtering
===================

For each candidate aside type, the runtime instantiates the aside and asks
it whether it should apply to this specific block by calling its
:meth:`~xblock.core.XBlockAside.should_apply_to_block` classmethod. The
default implementation returns ``True``. Real-world asides almost always
override this method to restrict themselves to specific block types, course
contexts, or feature flags.

Rendering and Layout
====================

For each aside that survives filtering, the runtime invokes the aside method
that was decorated with ``@XBlockAside.aside_for(view_name)`` for the view
being rendered. The aside method returns a ``Fragment``, the runtime wraps
that fragment with identifying markup, and the runtime appends the wrapped
fragment to the host block's rendered output. A runtime can override
:meth:`~xblock.runtime.Runtime.layout_asides` to control where and how the
aside fragments are placed.

Why Asides Are Worth the Trouble
********************************

The framing above describes the trade-offs from the perspective of someone
choosing among extension mechanisms. The deeper reasons asides exist, and
remain useful, come from the production deployments that depend on them.

Multiple Block Types, One Implementation
========================================

A single aside class can decorate Video blocks, Problem blocks, and any
other block type the author chooses, by checking ``block.category`` or
``block.scope_ids.block_type`` inside ``should_apply_to_block``. The MIT
Open Learning chat aside, for example, attaches an "AskTIM" chat button to
both Video and Problem blocks from a single class, with one entry point.
Without asides, the same outcome would require either two parallel forks
or replacement blocks for both types.

Course Author Control
=====================

An aside can declare its own scoped fields, just like an XBlock. By exposing
those fields in an author view, an aside gives course authors a UI to enable
or disable the enhancement on a per-block basis. The settings are stored
under the aside's own scope, not the host block's, so they are preserved
across exports and imports without any change to the host block's data
model.

OLX Export and Import
=====================

When a course is exported to OLX, the platform serializes each aside as an
XML child element under its host block, named after the aside's entry point
name. On import, the runtime reconstitutes the asides automatically. This
means an aside-enhanced course is portable, with limitations described below.

Real-World Examples
*******************

Three implementations in the wild illustrate the range of what asides can
do.

Rapid Response XBlock
=====================

The `rapid-response-xblock`_ from MIT Open Learning is a single aside that
applies to Problem blocks. It overlays an instructor-only control on the
problem in the LMS that lets a live instructor open and close response
windows during a lecture, and it renders a real-time chart of student
responses. Course authors enable it per problem in Studio. The repository
name calls it an "xblock" but the implementation is purely an aside.

Open Learning Chat Aside
========================

The `ol-openedx-chat`_ aside, also from MIT Open Learning, attaches an
"AskTIM" chat button to Video and Problem blocks. The button opens a
context-aware chat drawer that streams messages to a backend large language
model, passing block-specific context such as a video transcript identifier
or a problem's siblings. A single aside class, registered as one entry
point, handles both block types and uses ``should_apply_to_block`` to gate
on a course-level waffle flag and per-course settings.

Thumbs Sample Aside
===================

The `xblock-sdk`_ repository contains a ``ThumbsAside`` class in
``sample_xblocks/thumbs/thumbs.py``. It is **not functional** and is not
registered through any entry point. The class comment in the source notes:
"Asides aren't ready yet, so this is currently not being installed in
setup.py." It exists as a syntactic example of the decorator pattern, not
as a working aside. Treat it as illustrative only.

Limitations
***********

Asides are a real, working feature in production deployments, but the
ecosystem around them is incomplete. The list below is drawn from the
state of the codebase as of the Sumac release and from a 2025 Open edX
Conference talk by Peter Pinch of MIT Open Learning. Read it before
committing to an aside-based design.

No Authoring Story in the Course Authoring MFE
==============================================

The Studio author view for an aside is rendered by the legacy course
authoring frontend. The current Course Authoring micro-frontend has no
defined location to display aside author UI. If your project depends on the
new MFE for authoring, plan to render the aside's author UI through a
different mechanism, or accept that authors will use the legacy Studio for
this part of the workflow.

Not All XBlocks Round-Trip Through OLX
======================================

OLX export and import for asides depends on the host XBlock cooperating
with the export process. Some XBlocks, including ORA2, do not preserve
aside data through their export and import paths. If your aside must
survive a course export and re-import on a course that uses one of these
blocks, test the round trip end to end before depending on it.

Multiple Asides on a Single Block Are Not Reliable
==================================================

The runtime supports multiple aside types decorating the same block in
principle, but interactions between asides on the same block are not
well-tested. Two asides that both decorate ``student_view`` on the same
block may render correctly in isolation and break when combined. If you
need this, build a single aside that composes both behaviors rather than
relying on two independent asides to coexist.

JavaScript Library Loading Is Limited
=====================================

Asides use the same fragment-based JavaScript loading mechanism as XBlocks,
which assumes a single set of static assets. If your aside needs a JS
library that is not already loaded by the host page, you must add it
through the fragment, and you must handle ordering and conflicts yourself.
There is no shared aside-level mechanism for declaring library dependencies.

Documentation Has Historically Been Sparse
==========================================

XBlock Asides have been part of the platform for years but have had no
user-facing documentation until this set of articles. The original work was
done by Dave Ormsbee. Most of the institutional knowledge has lived in
docstrings, test code, and the implementations of a handful of asides
maintained outside the core platform. If you find this documentation lacks
detail your project needs, the test file at ``xblock/test/test_asides.py``
in the XBlock repository is the most reliable source of behavioral truth.

Where to Go Next
****************

If you are ready to build an aside, start with
:ref:`XBlock Aside Quickstart`. If you already have a target XBlock in mind
and want a step-by-step recipe, read :ref:`Add an XBlock Aside`. For the
complete list of classes, decorators, methods, and entry points, consult
:ref:`XBlock Asides Reference`.

.. _rapid-response-xblock: https://github.com/mitodl/rapid-response-xblock
.. _ol-openedx-chat: https://github.com/mitodl/open-edx-plugins/tree/main/src/ol_openedx_chat
.. _xblock-sdk: https://github.com/openedx/xblock-sdk

.. seealso::

   :ref:`XBlock Asides Reference` (reference)
       The complete API surface for ``XBlockAside`` and its runtime hooks.

   :ref:`Add an XBlock Aside` (how-to)
       A step-by-step recipe for adding an aside to existing XBlocks.

   :ref:`XBlock Aside Quickstart` (quickstart)
       A beginner-friendly walkthrough from zero to a running aside.

   :ref:`Hooks Extension Framework` (concept)
       An alternative extension mechanism for non-view-based behaviors.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
