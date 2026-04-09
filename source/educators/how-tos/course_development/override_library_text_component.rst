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

#. In Studio, open the unit that contains the library-sourced text component
   you want to customize.

#. Locate the text component. It will display an edit button (pencil icon) even
   though it is library-sourced.

#. Select the pencil icon to open the text editor.

   ..  image:: /_images/educator_how_tos/library_TextComponent_PencilIcon.png
     :alt: The pencil icon appears in the top right of the component editor, above the main content.

#. Make your changes to the text content.

#. Select :guilabel:`Save` to save the override.

   ..  image:: /_images/educator_how_tos/library_TextComponent_EditModalandSave.png
    :alt: Once the text has been edited, select the "Save" button in the lower right corner of the editor modal.

The text component now displays your customized content in the course. The
original content in the source library is not affected.

.. note::
   Once you save an override, there is no indicator that marks the component as locally overridden.
   This is planned for a future release.

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
   :ref:`title overrides <Override the Title of Library-Sourced Content>`)
   are handled automatically during sync and cannot be selectively kept or dropped.

What You Cannot Override
*************************

Overrides are limited to text content on text components. Edits that would
change the structure of library content — such as reordering components within a
library-sourced unit — are not permitted. To make structural changes, you must
first unlink the content from its source library.

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