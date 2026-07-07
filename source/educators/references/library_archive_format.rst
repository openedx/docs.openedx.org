.. _Library Archive Format:

The Library Archive Format
##########################

.. tags:: educator, reference

The Library Archive Format is the ZIP-based format used to
:ref:`Backup and Restore a Library` on the Open edX platform.

With a library archive, authors can:

* Move a library between different Open edX instances.
* Keep a portable backup copy of a library.
* Inspect, or even hand-edit, the contents of a library outside of Studio.

Because the archive keeps each component's content as OLX (open learning XML) —
the same format Studio uses internally — authors already familiar with
:ref:`OLX <What is Open Learning XML?>` will recognize the XML stored inside.

.. contents::
   :local:
   :depth: 2

Overview
********

A backup ZIP is a self-contained snapshot of one learning package. It captures
every component, collection, container (section / subsection / unit), and
static asset. For each component and container, only the current draft and
published versions are exported — the full version history is not preserved.

The archive uses `TOML <https://toml.io>`_ for all metadata files and keeps the
actual component XBlock content as XML (the same OLX format Studio has always
used). This makes backups both machine-readable and human-inspectable.


.. admonition:: A note on Learning Packages

   Every user-facing *Library* is backed in the database by a *Learning Package*,
   a general of repository of learning content. During the restore process,
   the system creates a standalone Learning Package for inspection; once the
   operator confirms the content, the Learning Package is promoted into a
   proper Library.  Because of this relationship, you will see the term
   ``learning_package`` used inside the archive's metadata files. In the
   future, this same archive format may be used to restore other kinds of
   Learning-Package-backed content.

.. admonition:: Schema versioning

   The current archive ``format_version`` is **1**. Future incompatible changes
   to the schema will increment this number so that tooling can detect them
   before attempting a restore.

Archive Structure
*****************

::

    <package>.zip
    ├── package.toml                          # library metadata + archive metadata
    ├── collections/
    │   └── <collection-key>.toml             # one file per collection
    └── entities/
        ├── <container-key>.toml              # sections, subsections, units
        └── xblock.v1/
            └── <block-type>/                 # e.g. html, problem, video
                ├── <component-code>.toml     # entity metadata + version list
                └── <component-code>/
                    └── component_versions/
                        └── v<N>/
                            ├── block.xml     # XBlock content (XML)
                            └── static/       # media assets referenced by block.xml

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

Component entity TOML (``entities/xblock.v1/<type>/<code>.toml``)
=================================================================

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
     - Entity reference in the form ``xblock.v1:<type>:<code>``
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

.. admonition:: Mapping archive keys to platform keys

   Restoring a component with an archive reference key
   ``xblock.v1:<type>:<component_code>`` to a library with the key
   ``lib:<org_code>:<lib_code>`` yields an XBlock with the usage key
   ``lb:<org_code>:<lib_code>:<type>:<component_code>``.


Container entity TOML (``entities/<key>.toml``)
===============================================

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

.. admonition:: Mapping archive keys to platform keys

   Restoring a container of kind ``<type>`` and archive reference ``<key>`` to
   a library with the key ``lib:<org_code>:<lib_code>`` yields a container with
   the key ``lct:<org_code>:<lib_code>:<type>:<key>``.


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
     - List of entity reference strings (e.g. ``xblock.v1:html:abc123``, ``unit-xyz789``)

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

The library archive format uses
:ref:`OLX (open learning XML) <What is Open Learning XML?>` to encode components,
similar to the course archive format, although there are few notable differences:

* Each library component version's OLX file is simply named ``block.xml``. Its key is
  separetely defined in the component's TOML metadata file. In the course OLX
  archive, the name of each XML file is derived from its block's key:
  ``<block_id>.xml``.

* Each library component stores its own static assets,
  ``component_versions/v<N>/static/<filename>`` and references them in its OLX
  file as ``/static/<filename>``. In the course archive, the course's static
  assets are all in one shared ``static/`` folder.

* Library HTML content is currently serialized inline using a CDATA section
  within the ``.xml`` file rather than being split into a separate ``.html``
  file. This differs from course archives, which support separate ``.xml`` and
  ``.html`` files. This is a known limitation of the library XBlock
  serialization layer.

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
