.. _XBlock Aside Quickstart:

##########################################
Quickstart: Build Your First XBlock Aside
##########################################

.. tags:: developer, quickstart

Build, install, and run a minimal XBlock Aside in a Tutor development
environment. By the end of this quickstart, you will have an Aside that
adds a small banner to every Problem block in a course, and you will
understand the four moving parts every Aside has: the class, the
decorated views, the entry point, and the install step.

This quickstart deliberately keeps the Aside trivial. For a more
realistic recipe, work through :ref:`Add an XBlock Aside` next. For the
conceptual background, see :ref:`About XBlock Asides`.

.. contents:: Contents
   :local:
   :depth: 1

Prerequisites
*************

You need:

* A running Tutor development environment with the LMS and Studio
  services accessible. Tutor's `Getting started`_ guide walks through
  the install if you do not have one yet.
* The installed Python version used by the target Open edX release.
* A course in your devstack with at least one Problem block. The Tutor
  demo course works.
* A text editor and a terminal.

You do **not** need:

* Prior experience writing XBlocks. The Aside in this quickstart uses
  plain Python and a hardcoded HTML string.
* Familiarity with the Open Learning XML (OLX) format.

Step 1: Create a Python package
*******************************

In a working directory of your choice, create the following file
structure:

.. code-block:: text

   hello_aside/
   ├── pyproject.toml
   └── hello_aside/
       ├── __init__.py
       └── Aside.py

Make ``__init__.py`` an empty file. The remaining steps describe what to
put in the other two files.

Step 2: Write the Aside class
*****************************

In ``hello_aside/Aside.py``, paste the following code:

.. code-block:: python

   from web_fragments.fragment import Fragment
   from xblock.core import XBlockAside


   class HelloAside(XBlockAside):
       """A trivial Aside that prints a banner above every Problem block."""

       @XBlockAside.aside_for("student_view")
       def student_view_aside(self, block, context=None):
           return Fragment(
               '<div style="padding:8px;background:#eef;border:1px solid #99c;">'
               'Hello from an XBlock Aside!'
               '</div>'
           )

       @classmethod
       def should_apply_to_block(cls, block):
           return getattr(block, "category", None) == "problem"

This is the entire implementation. Three things to notice:

* The class subclasses :class:`~xblock.core.XBlockAside`.
* The :meth:`~xblock.core.XBlockAside.aside_for` decorator marks
  ``student_view_aside`` as the method to call when an XBlock's
  ``student_view`` is being rendered.
* :meth:`~xblock.core.XBlockAside.should_apply_to_block` restricts the
  Aside to Problem blocks. Without it, the banner would appear on every
  block in every course.

Step 3: Configure the package
*****************************

In ``hello_aside/pyproject.toml``, paste:

.. code-block:: toml

   [project]
   name = "hello-Aside"
   version = "0.1.0"
   requires-python = ">=X.Y"  # set to the minimum Python version for the target Open edX release
   dependencies = ["XBlock", "web-fragments"]

   [project.entry-points."xblock_asides.v1"]
   hello_aside = "hello_aside.Aside:HelloAside"

   [build-system]
   requires = ["setuptools>=61.0"]
   build-backend = "setuptools.build_meta"

The critical line is the one under
``[project.entry-points."xblock_asides.v1"]``. It tells the Open edX
platform that a class called ``HelloAside``, in the ``hello_aside.Aside``
module, should be loaded as an Aside under the type name
``hello_aside``. This entry point group is how every Aside is
discovered.

Step 4: Install the package into Tutor
**************************************

From the directory containing ``hello_aside/``, mount the package into
Tutor and relaunch the development environment:

.. code-block:: bash

   tutor mounts add ./hello_aside
   tutor dev launch

The ``mounts add`` command tells Tutor to install the local package into
both the LMS and Studio containers each time they start. The
``dev launch`` command rebuilds and restarts the containers so the new
Aside is picked up.

If you are not using Tutor, install the package directly into the LMS
and Studio Python environments with ``pip install -e ./hello_aside``,
then restart both services.

Step 5: Enable the Aside system in the LMS
******************************************

The LMS gates Aside rendering on a global Django configuration model,
``XBlockAsidesConfig``. Until that model is enabled, no Aside renders on
any block, regardless of whether it is registered or installed.

Open the LMS Django admin in your browser:

.. code-block:: text

   http://<your-lms-host>/admin/lms_xblock/xblockasidesconfig/

Click :guilabel:`Add` to create a new revision. Check :guilabel:`Enabled`
and click :guilabel:`Save`. The new revision becomes the current
configuration immediately.

The same form has a ``Disabled blocks`` field that holds a
space-separated list of block types on which asides will **never**
render. The default value is ``about course_info static_tab``. The
``hello_aside`` example targets ``problem`` blocks, which are not in the
default disabled list, so no further changes are needed.

The Studio runtime does not consult this model. Asides will render in
Studio author views as soon as they are installed, independently of
whether ``XBlockAsidesConfig`` is enabled.

Step 6: Verify the Aside is rendering
*************************************

Open a course in the LMS, navigate to a unit that contains a Problem
block, and confirm a light blue banner reading "Hello from an XBlock
Aside!" appears below the problem. If you see the banner, your Aside is
working.

If the banner does not appear, work through these checks in order:

#. **The Aside is registered.** Open a Django shell and run:

   .. code-block:: python

      from xblock.core import XBlockAside
      print(list(XBlockAside.load_classes()))

   The list should include ``hello_aside``. If it does not, the entry
   point is not installed; recheck Step 3 and Step 4.

#. **The block type matches.** Your test block must have
   ``category == "problem"``. A Video block, an HTML block, or a
   Discussion block will not trigger the Aside.

#. **No exceptions are being swallowed.** Check the LMS logs for any
   exception raised inside ``student_view_aside`` or
   ``should_apply_to_block``. The runtime catches some Aside exceptions
   silently, which can make a broken Aside look like a missing one.

What You Just Built
*******************

You have a working Aside with all four required pieces:

A class
   ``HelloAside`` subclasses ``XBlockAside``.

A decorated view
   ``student_view_aside`` is decorated with
   ``@XBlockAside.aside_for("student_view")``, so it is invoked
   whenever the runtime renders any block's ``student_view``.

A filter
   ``should_apply_to_block`` restricts the Aside to Problem blocks.

An entry point
   The ``xblock_asides.v1`` entry point in ``pyproject.toml`` makes the
   Aside discoverable by the platform at startup.

Every production Aside has the same four pieces, plus additional
features such as scoped fields, AJAX handlers, author-side UI, and
template-rendered HTML.

Where to Go Next
****************

To turn this trivial example into something useful:

* **Add a course-author toggle.** Declare a ``Boolean`` field with
  ``Scope.settings`` and conditionally render the banner based on its
  value. The :ref:`Add an XBlock Aside` how-to walks through this.
* **Render from a template.** Replace the inline HTML string with a
  template loaded from your package's static assets, rendered through
  the runtime's template service.
* **Add an AJAX handler.** Decorate a method with ``@XBlock.handler``
  and call it from JavaScript in your fragment to support interactive
  behavior.
* **Decorate the author view.** Add a second method decorated with
  ``@XBlockAside.aside_for("author_view")`` to render an author-facing
  preview in Studio.

For each of these extensions, the :ref:`XBlock Asides Reference` is the
authoritative source. For the trade-offs and current limitations of the
Aside mechanism, read :ref:`About XBlock Asides` before scaling up your
design.

.. _Getting started: https://docs.tutor.edly.io/quickstart.html

.. seealso::

   :ref:`About XBlock Asides` (concept)
       Why asides exist, what problem they solve, and current limitations.

   :ref:`Add an XBlock Aside` (how-to)
       A step-by-step recipe for adding an Aside to existing XBlocks.

   :ref:`XBlock Asides Reference` (reference)
       The complete API surface for ``XBlockAside`` and its runtime hooks.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
