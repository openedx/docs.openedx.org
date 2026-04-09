.. _Override Text Content in a Library-Referenced Component:

Override Text Content in a Library-Referenced Component
#######################################################

.. tags:: educator, how-to

When you add content from a content library to your course, that content is
linked to its source library and kept in sync with it. In most cases, you
cannot edit library-sourced content directly in a course — but text components
are an exception. You can override the text content of a library-sourced text
component to customize it for your course without unlinking the rest of the
content from the library.

This how-to covers standalone text component overrides. For information about
overriding text content within a library-sourced unit, subsection, or section,
see :ref:`Override Text Content in a Library-Sourced Structural Block`.

.. note::
   Text content overrides are available starting with the Verawood release of
   the Open edX platform.

Prerequisites
*************

Before you begin, ensure that you have:

- A course open in Studio.
- A published text component from a content library already added to the
  course as a standalone component (not nested inside a library-sourced unit,
  subsection, or section).

Override the Text Content
*************************

1. In Studio, open the unit that contains the library-sourced text component
   you want to customize.

2. Locate the text component. It will display an :guilabel:`Edit` button even
   though it is library-sourced.

3. Select :guilabel:`Edit` to open the text editor.

4. Make your changes to the text content.

5. Select :guilabel:`Save` to save the override.

The text component now displays your customized content in the course. The
original content in the source library is not affected.

.. note::
   Once you save an override, there is no indicator in the current release that
   marks the component as locally overridden. This is planned for a future
   release.

Sync Library Updates After an Override
***************************************

Overriding the text content of a standalone text component changes how syncing
works for that component. When a newer version of the component is published in
the source library, you can choose what happens to your override during a sync.

When you sync and the library has a newer version of the overridden text
component, Studio will prompt you to choose one of the following options.

- **Keep course content** — your local override is preserved and the library
  update is ignored for this component.
- **Update to published library content** — your override is discarded and the
  component is updated to the latest version from the library.

.. important::
   This choice — whether to keep or drop an override — is only available for
   standalone text component overrides. Other types of overrides (such as
   title overrides) are handled automatically during sync and cannot be
   selectively kept or dropped.

What You Cannot Override
*************************

Not all edits are allowed on library-sourced content. Overrides are limited to
text content on text components. Edits that would change the structure of
library content — such as reordering components within a library-sourced unit —
are not permitted. To make structural changes, you must first unlink the
content from its source library.

.. seealso::

   :ref:`Add Library Content to a Course` (how-to)

   :ref:`Sync a Library update to your course` (how-to)

   :ref:`Override the Title of Library-Sourced Content` (how-to)

   :ref:`Override Text Content in a Library-Sourced Structural Block` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-04-08   | sarina                        | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+