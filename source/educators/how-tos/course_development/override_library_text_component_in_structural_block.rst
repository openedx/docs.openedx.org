.. _Override Text Content in a Library-Sourced Structural Block:

Override Text Content in a Library-Sourced Structural Block
###########################################################

.. tags:: educator, how-to

When you add a section, subsection, or unit from a content library to your
course, the content is linked to its source library. In most cases, you cannot
edit library-sourced content directly in a course — but text components are an
exception. You can override the text content of any text component within a
library-sourced structural block to customize it for your course, without
unlinking the rest of the block from the library.

For information about overriding a standalone library-sourced text component
(one that is not nested inside a library-sourced section, subsection, or unit),
see :ref:`Override Text Content in a Library-Referenced Component`.

.. note::
   Text content overrides within structural blocks are available starting with
   the Verawood release of the Open edX platform.

Prerequisites
*************

Before you begin, ensure that you have:

- A course open in Studio.
- A section, subsection, or unit that was added to the course from a content
  library, containing at least one text component.

Override Text Content Within a Structural Block
***********************************************

1. In Studio, open the unit that contains the library-sourced text component
   you want to customize. The unit may itself be library-sourced, or it may be
   a course unit that contains a library-sourced section or subsection.

2. Locate the text component. It will display an :guilabel:`Edit` button even
   though it is part of a library-sourced block.

3. Select :guilabel:`Edit` to open the text editor.

4. Make your changes to the text content.

5. Select :guilabel:`Save` to save the override.

The text component now displays your customized content in the course. The
original content in the source library is not affected.

.. note::
   Once you save an override, there is no indicator in the current release that
   marks the component as locally overridden. This is planned for a future
   release.

How Text Overrides Interact with Syncing
*****************************************

Overriding the text content of a component within a structural block changes
how that component is handled during future syncs. The following rules apply.

- **Overridden components are excluded from content syncs.** When you sync the
  structural block or any of its parents, the overridden text component is
  ignored. Its content is never updated from the library, even if a newer
  version has been published.
- **Position changes are still applied.** If the component is moved up or down
  within the structural block in the source library, its position in your
  course is updated when you sync, but its content remains unchanged.
- **Deleted components are still removed.** If the component is deleted in the
  source library and you accept that sync on its parent block, the component is
  removed from your course even if it had a local override.
- **Other components in the block sync normally.** Overriding one text
  component does not affect your ability to sync updates to the rest of the
  structural block.

.. important::
   Unlike standalone text component overrides, syncing a structural block does
   not give you a choice to keep or drop individual text overrides. Overridden
   components are always excluded from the sync automatically.

.. seealso::

   :ref:`Add Library Content to a Course` (how-to)

   :ref:`Sync a Library update to your course` (how-to)

   :ref:`Override Text Content in a Library-Referenced Component` (how-to)

   :ref:`Override the Title of Library-Sourced Content` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-04-08   | sarina                        | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+