.. _Add an XBlock Aside:

####################
Add an XBlock Aside
####################

.. tags:: developer, how-to

Add an XBlock aside to attach behavior, UI, or stored data to one or more
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

This recipe builds a feedback-badge aside that adds a "Report an issue"
link to Problem and Video blocks, with a course-author setting to enable
or disable it per block. Substitute your own block types and behavior as
needed.

Step 1: Scaffold a Python package
*********************************

Create a new directory for the aside package, with the layout below:

.. code-block:: text

   feedback_badge_aside/
   ├── pyproject.toml
   ├── feedback_badge_aside/
   │   ├── __init__.py
   │   └── aside.py
   └── README.rst

The package name (``feedback_badge_aside``) and the module name
(``aside.py``) are conventions; pick names that describe your aside.

Populate ``pyproject.toml`` with the package metadata and a placeholder
for the entry point you will add in :ref:`Step 6 <register entry point>`.

.. code-block:: toml

   [project]
   name = "feedback-badge-aside"
   version = "0.1.0"
   description = "An XBlock aside that adds a feedback link to Problem and Video blocks."
   requires-python = ">=X.Y"  # set to the minimum Python version for the target Open edX release
   dependencies = [
       "XBlock",
       "web-fragments",
   ]

   [build-system]
   requires = ["setuptools>=61.0"]
   build-backend = "setuptools.build_meta"

Step 2: Define the aside class
******************************

In ``feedback_badge_aside/aside.py``, define a subclass of
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
the aside on a per-block basis. Scope the field to ``Scope.settings``,
which means the value is stored per block and travels with the course in
OLX export and import.

.. code-block:: python

   from xblock.core import XBlockAside
   from xblock.fields import Boolean, Scope


   class FeedbackBadgeAside(XBlockAside):
       """Adds a feedback link to learner-facing views of supported blocks."""

       enabled = Boolean(
           display_name="Show feedback link",
           default=True,
           scope=Scope.settings,
           help="Whether to show a 'Report an issue' link on this block.",
       )

Step 4: Decorate the views you want to inject into
**************************************************

Add one method per XBlock view you want to decorate, using
:meth:`~xblock.core.XBlockAside.aside_for`. The method takes ``self``,
the host ``block``, and an optional ``context`` dictionary, and returns
a :class:`~web_fragments.fragment.Fragment`.

.. code-block:: python

   from web_fragments.fragment import Fragment
   from xblock.core import XBlockAside
   from xblock.fields import Boolean, Scope


   class FeedbackBadgeAside(XBlockAside):
       """Adds a feedback link to learner-facing views of supported blocks."""

       enabled = Boolean(
           display_name="Show feedback link",
           default=True,
           scope=Scope.settings,
           help="Whether to show a 'Report an issue' link on this block.",
       )

       @XBlockAside.aside_for("student_view")
       def student_view_aside(self, block, context=None):
           """Render the feedback link for the learner view."""
           if not self.enabled:
               return Fragment("")

           block_id = block.scope_ids.usage_id.block_id
           html = (
               f'<a class="feedback-badge" '
               f'href="/feedback?block={block_id}">Report an issue</a>'
           )
           return Fragment(html)

       @XBlockAside.aside_for("studio_view")
       def studio_view_aside(self, block, context=None):
           """Render the author-side toggle UI in Studio."""
           checked = "checked" if self.enabled else ""
           html = (
               f'<label><input type="checkbox" {checked} '
               f'class="feedback-badge-toggle"> Show feedback link</label>'
           )
           return Fragment(html)

For production code, render templates from files with the runtime's
template service rather than building HTML strings inline. The strings
above keep the example readable.

Step 5: Filter to specific block types
**************************************

By default, an aside applies to every block. Override
:meth:`~xblock.core.XBlockAside.should_apply_to_block` to restrict the
aside to the block types you support.

.. code-block:: python

   @classmethod
   def should_apply_to_block(cls, block):
       """Apply this aside to Problem and Video blocks only."""
       block_type = getattr(block, "category", None)
       return block_type in {"problem", "video"}

Add this classmethod to ``FeedbackBadgeAside``. Without it, the aside
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

Step 6: Register the aside as an entry point
********************************************

In ``pyproject.toml``, add an entry point in the ``xblock_asides.v1``
group. The entry point name on the left side of the equals sign becomes
the aside's type name and is used as the XML tag during OLX
serialization.

.. code-block:: toml

   [project.entry-points."xblock_asides.v1"]
   feedback_badge = "feedback_badge_aside.aside:FeedbackBadgeAside"

Choose a type name that is unlikely to collide with other asides on the
same deployment. Treat the name as a stable public identifier; renaming
it later breaks OLX round-trips of any course that has used the aside.

Step 7: Install the package and restart services
************************************************

Install the package into the LMS and Studio Python environments. With
Tutor:

.. code-block:: bash

   tutor mounts add /path/to/feedback_badge_aside
   tutor dev launch

Or, if you are managing the environment manually:

.. code-block:: bash

   pip install -e /path/to/feedback_badge_aside

After installing, restart both the LMS and Studio. Asides are discovered
at process start, so newly installed asides do not appear until the
services restart.

Step 8: Enable asides in the LMS
********************************

The edx-platform LMS gates aside rendering on a Django configuration
model, ``XBlockAsidesConfig``, defined in
``lms/djangoapps/lms_xblock/models.py``. Until this model has an enabled
revision, no aside renders in the LMS regardless of installation or
registration.

Open the LMS Django admin and create a new configuration revision:

.. code-block:: text

   http://<your-lms-host>/admin/lms_xblock/xblockasidesconfig/

Click :guilabel:`Add`, check :guilabel:`Enabled`, and save. The model is
a ``ConfigurationModel`` (revision-based), so each save creates a new
revision and the most recent enabled revision is treated as current.

The same form has a ``Disabled blocks`` field, a space-separated list of
block types on which asides will **never** render in the LMS. The
default value is ``about course_info static_tab``. If your aside should
apply to one of these block types, remove that type from the list.

There is no per-course allowlist and no per-aside-type allowlist. Once
``XBlockAsidesConfig`` is enabled and your aside's host block type is
not in ``disabled_blocks``, the runtime offers your aside to every
matching block in every course. Per-aside filtering happens through
your aside's own ``should_apply_to_block`` classmethod, which you wrote
in Step 5.

The Studio runtime does not consult this configuration. Asides render
in Studio author views independently of ``XBlockAsidesConfig``, as soon
as they are installed and registered.

Step 9: Verify the aside is rendering
*************************************

Open a course that contains a Problem or Video block, view it as a
learner, and confirm the feedback link appears at the bottom of the
block. To verify the author-side UI, open the same block in Studio and
confirm the toggle appears in the studio view.

If the aside does not appear:

#. Check that the entry point is registered. Run:

   .. code-block:: python

      from xblock.core import XBlockAside
      print(list(XBlockAside.load_classes()))

   in a Django shell. Your aside's type name should be in the list.

#. Check that ``should_apply_to_block`` returns ``True`` for the block
   you are testing.
#. Check that the aside is allowlisted for the course.
#. Check the LMS and Studio logs for any exceptions raised inside your
   aside view.

Next Steps
**********

Once the basic aside is working, common follow-ups include:

* **Add an AJAX handler.** Decorate a method with ``@XBlock.handler``
  and call it from the rendered fragment with
  ``self.runtime.handler_url(self, "handler_name")``.
* **Render from templates.** Use the runtime's template service to
  render HTML from ``.html`` files in your package's static assets.
* **Persist user-specific state.** Add fields with
  ``Scope.user_state`` to store per-learner data alongside the aside.
* **Customize layout.** If you need the aside to render somewhere other
  than after the host block, override the runtime's ``layout_asides``
  in your platform integration.

For the complete API surface, see :ref:`XBlock Asides Reference`. For
the conceptual background, including known limitations of the aside
mechanism, see :ref:`About XBlock Asides`.

.. seealso::

   :ref:`About XBlock Asides` (concept)
       Why asides exist, what problem they solve, and current limitations.

   :ref:`XBlock Asides Reference` (reference)
       The complete API surface for ``XBlockAside`` and its runtime hooks.

   :ref:`XBlock Aside Quickstart` (quickstart)
       A beginner-friendly walkthrough from zero to a running aside.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
