.. _Merge Legacy Library Exports:

Merge Legacy Library Exports into a New Library Archive
#########################################################

.. tags:: educator, how-to

Legacy (V1) content libraries exported from Studio produce an XML-based OLX
archive packaged as a ``.tar.gz`` file. New libraries use the
:ref:`Library Archive Format`, a different backup/restore archive format — a
``.zip`` of TOML metadata files plus XBlock XML.

Legacy libraries were designed to hold only a small bank of content. New
libraries can hold thousands of components and organize them internally into
collections, so rather than migrating each legacy library 1:1, it often makes
sense to merge several legacy libraries into a single new library.

This guide explains how a savvy operator can combine one or more legacy
library exports into a single new-library backup archive by hand, without
using an automated migration tool. If you only need to migrate a single
legacy library as-is, use the :ref:`one-click migration feature
<Migrating Legacy Libraries>` instead.

.. contents::
   :local:
   :depth: 2

Background: Format Differences
*******************************

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Aspect
     - Legacy library export
     - New library archive
   * - Container format
     - ``.tar.gz``
     - ``.zip``
   * - Library metadata
     - ``library.xml`` (XML)
     - ``package.toml`` (TOML)
   * - Component files
     - ``<type>/<block_id>.xml``
     - ``entities/xblock.v1/<type>/<uuid>/component_versions/v1/block.xml``
   * - HTML content
     - Stored in a separate ``.html`` file alongside the XML
     - Inlined as a CDATA section within ``block.xml``
   * - Static assets
     - ``static/<filename>``
     - ``entities/xblock.v1/<type>/<uuid>/component_versions/v1/static/<filename>``
   * - Identifiers
     - Short ``block_id`` strings
     - Unique key strings (assigned during merge)
   * - Version history
     - Not preserved
     - Single ``v1`` entry per component after merge
   * - Collections
     - Not supported
     - Can be added manually (optional)

.. note::

   After a merge restore, **course content that previously referenced legacy
   library blocks via** ``usage_key`` **will not automatically point at the
   new library's components**. Those references must be updated separately
   in each course.

.. note::

   This guide assumes that your legacy library ``.tar.gz`` archives follow
   the standard flat layout produced by Studio's export tool
   (``<type>/<block_id>.xml``). Hand-written or otherwise unusual legacy
   archives may be laid out differently, and you may need to adapt this
   guide to account for those differences.

Prerequisites
*************

* The legacy library export archive(s) (``.tar.gz``) produced by Studio's
  *Export* feature.
* Permission to create libraries on the target Open edX instance.
* Python 3.9+ and the ``tomlkit`` package (``pip install tomlkit``) if you
  want to generate the TOML files with a script instead of by hand.
* A basic familiarity with tar and ZIP archives (the standard ``tar`` and
  ``zip``/``unzip`` command-line tools or any GUI archive manager).

Step-by-Step Merge
*******************

1. Extract all legacy library archives
=======================================

Extract each legacy library export into its own directory::

    mkdir -p v1_library_A v1_library_B
    tar -xzf v1_library_A.tar.gz -C v1_library_A/
    tar -xzf v1_library_B.tar.gz -C v1_library_B/

Each directory will contain at minimum a ``library.xml`` file and one
subdirectory per XBlock type (e.g. ``html/``, ``problem/``, ``video/``).

2. Create the new-library directory skeleton
=============================================

::

    mkdir -p v2_library/collections
    mkdir -p v2_library/entities/xblock.v1

3. Write ``package.toml``
==========================

Create ``v2_library/package.toml`` using the metadata from one of the
``library.xml`` files (or supply new values for the merged library):

.. code-block:: toml

    [meta]
    format_version = 1
    created_by = "operator_username"
    created_at = 2025-01-01T00:00:00Z

    [learning_package]
    title = "Merged Library"
    key = "lib:MyOrg:MergedLib"
    description = "Combined from legacy library A and legacy library B."
    created = 2025-01-01T00:00:00Z
    updated = 2025-01-01T00:00:00Z

``key`` must be unique on the target instance. Use the pattern
``lib:<organization>:<library_code>``.

4. Convert each legacy component
=================================

For every block in the legacy archives, do the following.

a. **Assign an identifier** — rather than a random UUID, prefer a scheme
   that keeps a semantic connection between the source and target block.
   For a legacy library with org ``MyOrg`` and library slug ``MyLib``,
   a block with ``url_name`` ``MyBlock`` can become ``MyOrg_MyLib_MyBlock``
   in the new library. A block's identifier only needs to be unique within
   the new library, it does not need to be a UUID.

b. **Create the version directory**::

       ID=MyOrg_MyLib_MyBlock                       # use your generated identifier
       TYPE=html                                    # e.g. html, problem, video
       mkdir -p "v2_library/entities/xblock.v1/${TYPE}/${ID}/component_versions/v1/static"

c. **Copy the block XML**::

       cp "v1_library_A/${TYPE}/${BLOCK_ID}.xml" \
          "v2_library/entities/xblock.v1/${TYPE}/${ID}/component_versions/v1/block.xml"

   For most block types the XML content is unchanged. **HTML blocks are an
   exception**: the legacy format stores the HTML body in a separate
   ``html/<block_id>.html`` file referenced from the XML, but the new
   format requires that same content to be inlined as a CDATA section
   inside ``block.xml``. Concretely, take the content of
   ``v1_library_A/html/<block_id>.html`` and place it inside a CDATA block
   inside the copied ``<html>`` element, then drop the separate ``.html``
   file — it has no equivalent in the new format.

d. **Copy static assets** — any files from ``v1_library_A/static/`` that are
   referenced in this block's XML (look for ``/static/<filename>`` or
   ``static/<filename>``)::

       cp "v1_library_A/static/diagram.png" \
          "v2_library/entities/xblock.v1/${TYPE}/${ID}/component_versions/v1/static/"

e. **Write the entity TOML** at
   ``v2_library/entities/xblock.v1/<type>/<id>.toml``
   (the ``<type>/`` directory was already created by step 4b):

   .. code-block:: toml

       [entity]
       can_stand_alone = true
       key = "xblock.v1:html:MyOrg_MyLib_MyBlock"
       created = 2025-01-01T00:00:00Z

       [entity.draft]
       version_num = 1

       [entity.published]
       version_num = 1

       [[version]]
       title = "Untitled"
       version_num = 1

   Set ``title`` to the ``display_name`` attribute from the block XML if one
   is present.

Repeat steps (a)–(e) for every block across all legacy archives.

5. (Optional) Create collections
=================================

If you want to keep the blocks from each source library grouped together,
create one collection TOML file per source library in
``v2_library/collections/``. The ``entities`` list references the ``key``
value written for each block in step 4e:

.. code-block:: toml

    [collection]
    title = "From Library A"
    key = "from-library-a"
    description = ""
    created = 2025-01-01T00:00:00Z
    entities = [
        "xblock.v1:html:MyOrg_MyLib_MyBlock",
        "xblock.v1:problem:MyOrg_MyLib_OtherBlock",
    ]

6. ZIP the result
==================

The ZIP must be created from *inside* the ``v2_library/`` directory so that
``package.toml`` sits at the archive root (not nested under a
``v2_library/`` prefix)::

    cd v2_library/
    zip -r ../merged_library.zip .
    cd ..

Verify the root entry is correct::

    unzip -l merged_library.zip | head -5
    # Should show:   package.toml   (not v2_library/package.toml)

7. Load the archive
====================

Load the archive through the target instance's REST API for restoring a
library backup. Alternatively, on an instance where you have shell access,
the ``lp_load`` management command can load the archive directly::

    python manage.py lp_load merged_library.zip <username>

On success, the library will appear in Studio's library list under the key
specified in ``package.toml``.

.. seealso::

   :ref:`Library Archive Format` (reference)

   :ref:`Backup and Restore a Library` (how-to)

   :ref:`Migrating Legacy Libraries` (how-to)

   `Legacy Libraries Deprecation <https://github.com/openedx/edx-platform/issues/32457>`_
   — deprecation tracking issue for legacy (V1) content libraries.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
