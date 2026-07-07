.. _Library Archive Format:

The Library Archive Format
##########################

.. tags:: educator, reference

The Library Archive Format is the ZIP-based format used to back up and restore
content libraries on the Open edX Platform.

With a library archive, authors can:

* Move a library between different Open edX instances.
* Keep a portable backup copy of a library.
* Inspect, or even hand-edit, the contents of a library outside of Studio.

Because the archive keeps each component's content as OLX (open learning XML) —
the same format Studio uses internally — authors already familiar with
:ref:`OLX <What is Open Learning XML?>` will recognize the XML stored inside.

.. note::

   This page documents the *format* of a library archive. For step-by-step
   instructions on creating and restoring one in Studio, see
   :ref:`Backup and Restore a Library`.

.. contents::
   :local:
   :depth: 2

Overview
********

.. note::

   A **Library** (the user-facing content library) has exactly one **Learning
   Package** where it stores its content, but Learning Packages can also exist
   independently. During a restore, the system first creates a standalone
   Learning Package for inspection; once the operator confirms the content,
   that Learning Package is associated with a newly created Library. Because of
   this relationship, you will see the term ``learning_package`` used inside the
   archive's metadata files.

A backup ZIP is a self-contained snapshot of one learning package. It captures
every component, collection, container (section / subsection / unit), and
static asset. For each component and container, only the current draft and
published versions are exported — the full version history is not preserved.

The archive uses `TOML <https://toml.io>`_ for all metadata files and keeps the
actual component XBlock content as XML (the same OLX format Studio has always
used). This makes backups both machine-readable and human-inspectable.

.. note::

   The current archive ``format_version`` is **1**. Future incompatible changes
   to the schema will increment this number so that tooling can detect them
   before attempting a restore.

Archive Structure
*****************

::

    <package>.zip
    ├── package.toml                          # library metadata + archive metadata
    ├── collections/
    │   └── <collection-key>.toml            # one file per collection
    └── entities/
        ├── <container-slug>.toml            # sections, subsections, units
        └── xblock.v1/
            └── <block-type>/               # e.g. html, problem, video
                ├── <uuid>.toml             # entity metadata + version list
                └── <uuid>/
                    └── component_versions/
                        └── v<N>/
                            ├── block.xml   # XBlock content (XML)
                            └── static/     # media assets referenced by block.xml

File Format Reference
*********************

package.toml
============

Located at the root of the archive. Contains two sections:

``[meta]`` — archive metadata (for inspection only):

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Field
     - Required
     - Description
   * - ``format_version``
     - yes
     - Integer schema version; currently ``1``
   * - ``created_by``
     - no
     - Username of the operator who ran the export
   * - ``created_by_email``
     - no
     - Email address of the exporting user
   * - ``created_at``
     - yes
     - UTC timestamp when the archive was created
   * - ``origin_server``
     - no
     - Free-form string identifying the origin CMS instance (typically a
       hostname or URL; stored as-is with no format validation)

``[learning_package]`` — library data. Note that ``key`` may be overridden when
the library is restored under a new reference, and ``updated`` is written to the
archive for reference but is not applied during a restore:

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Field
     - Required
     - Description
   * - ``title``
     - yes
     - Human-readable name of the library
   * - ``key``
     - yes
     - Package reference string, e.g. ``lib:MyOrg:MyLib``
   * - ``description``
     - yes
     - Free-text description (may be blank)
   * - ``created``
     - yes
     - UTC timestamp when the library was originally created
   * - ``updated``
     - yes
     - UTC timestamp of the library's last modification (written to the
       archive for reference; **not** applied during restore)

Example::

    [meta]
    format_version = 1
    created_by = "lp_user"
    created_by_email = "lp_user@example.com"
    created_at = 2025-10-05T18:23:45.180535Z
    origin_server = "cms.test"

    [learning_package]
    title = "Library test"
    key = "lib:WGU:LIB_C001"
    description = ""
    created = 2025-08-19T04:25:10.988166Z
    updated = 2025-08-19T04:25:10.988166Z

Component entity TOML (``entities/xblock.v1/<type>/<uuid>.toml``)
================================================================

Each XBlock component gets one TOML file.

``[entity]``:

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Field
     - Required
     - Description
   * - ``can_stand_alone``
     - yes
     - Whether this component can be used independently (almost always ``true``)
   * - ``key``
     - yes
     - Entity reference in the form ``xblock.v1:<type>:<uuid>``
   * - ``created``
     - yes
     - UTC creation timestamp

``[entity.draft]`` / ``[entity.published]`` — each contains ``version_num``
pointing at the current draft or published ``[[version]]`` entry respectively.
``[entity.draft]`` is absent when the entity has no draft.
``[entity.published]`` is **always present** — when the entity has no
published version it is written as an empty table with an explanatory comment
(see the container example below).

``[[version]]`` — at most two entries: the current draft version first, then
the current published version if it differs from draft. The full version
history is not stored.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Field
     - Required
     - Description
   * - ``title``
     - yes
     - Display name of the component at this version
   * - ``version_num``
     - yes
     - Monotonically increasing integer starting at 1

Example::

    [entity]
    can_stand_alone = true
    key = "xblock.v1:html:e32d5479-9492-41f6-9222-550a7346bc37"
    created = 2025-08-19T04:25:43.685529Z

    [entity.draft]
    version_num = 5

    [entity.published]
    version_num = 4

    # ### Versions

    [[version]]
    title = "Text"
    version_num = 5

    [[version]]
    title = "Text"
    version_num = 4

Container entity TOML (``entities/<slug>.toml``)
================================================

The ``<slug>`` is derived from the last segment of the container's
``entity_ref``. If two containers share the same last segment (e.g. a Unit
and a Subsection both named "intro"), a short hash is appended to the
second to avoid filename collisions (e.g. ``intro-48afa3.toml``).

Sections, subsections, and units share the same base structure with an
additional ``[entity.container.<type>]`` marker (``section``, ``subsection``,
or ``unit``) and a ``[version.container]`` table that lists child keys.

Example (section)::

    [entity]
    can_stand_alone = true
    key = "section1-8ca126"
    created = 2025-09-04T22:51:40.919872Z

    [entity.draft]
    version_num = 2

    [entity.published]
    # unpublished: no published_version_num

    [entity.container.section]

    # ### Versions

    [[version]]
    title = "Section1"
    version_num = 2

    [version.container]
    children = ["subsection1-48afa3"]

Collection TOML (``collections/<key>.toml``)
============================================

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Field
     - Required
     - Description
   * - ``title``
     - yes
     - Collection display name
   * - ``key``
     - yes
     - Unique key within the library
   * - ``description``
     - yes
     - Free-text description (may be blank)
   * - ``created``
     - yes
     - UTC creation timestamp
   * - ``entities``
     - yes
     - List of entity reference strings (``xblock.v1:<type>:<uuid>``)

Example::

    [collection]
    title = "Collection test1"
    key = "collection-test"
    description = ""
    created = 2025-08-19T04:25:27.754968Z
    entities = [
        "xblock.v1:html:e32d5479-9492-41f6-9222-550a7346bc37",
        "xblock.v1:problem:256739e8-c2df-4ced-bd10-8156f6cfa90b",
    ]

XBlock content (``component_versions/v<N>/block.xml``)
======================================================

:ref:`OLX (open learning XML) <What is Open Learning XML?>` for the component,
in the same format Studio uses internally. Static assets (images, PDFs, etc.)
referenced with ``/static/<filename>`` in the XML are stored alongside under
``component_versions/v<N>/static/``.

.. note::

   Unlike the old modulestore OLX export — where each component's file was
   named after its ``block_id`` (often a machine-generated UUID) — this format
   always names the file ``block.xml``. The component's identifier lives in
   the parent TOML file, not the filename.

.. note::

   **HTMLBlock limitation:** HTML content is currently serialized inline using
   a CDATA section rather than stored in a separate ``.html`` file. This
   differs from old course OLX exports and is a known limitation of the current
   XBlock serialization layer.

Example ``block.xml``::

    <html display_name="Text">
      <![CDATA[<p>Hello <img src="/static/me.png" alt="Me" /></p>]]>
    </html>

.. seealso::

   :ref:`Backup and Restore a Library` (how-to)

   :ref:`What is Open Learning XML?` (concept)

   :ref:`OLX Documentation <OLX TOC>` (reference)

   :ref:`OLX Directory Structure` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
