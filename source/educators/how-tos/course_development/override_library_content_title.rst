.. _Override the Title of Library-Sourced Content:

Override the Title of Library-Sourced Content
#############################################

.. tags:: educator, how-to

When you add content from a content library to your course, it is linked to
its source library and its title reflects whatever was set in the library. You
can rename that content in your course without unlinking it from the library.
Title overrides are supported for all library-sourced content, including
sections, subsections, units, and components.

.. note::
   Title overrides are available starting with the Verawood release of the
   Open edX platform.

Prerequisites
*************

Before you begin, ensure that you have:

- A course open in Studio.
- At least one section, subsection, unit, or component that was added to the
  course from a content library.

Override a Title
****************

The steps for overriding a title depend on the type of content you are
renaming.

.. note::

   Once you save a title override, there is no indicator in the current release
   that marks the content as locally renamed. This is planned for a future
   release.

Rename a Section, Subsection, or Unit
======================================

#. In Studio, open the course outline.

#. Locate the library-sourced section, subsection, or unit you want to rename.

#. Select the pencil icon (or click the existing title) to make it editable.

   ..  image:: /_images/educator_how_tos/library_CourseOutline-1-PencilIcon.png
      :alt: The pencil icon appearing next to the title of a subsection within the course outline, to the right of the subsection's name.

#. Enter the new title.

   ..  image:: /_images/educator_how_tos/library_CourseOutline-2-TypeNewName.png
      :alt: The title is editable in-line in the course outline.

#. Press Enter on your keyboard, or select outside the field, to save the change.

   ..  image:: /_images/educator_how_tos/library_CourseOutline-3-RenameSaved.png
      :alt: The subsection is now renamed. The change is now staged for publish, indicated by the "Draft (Unpublished Changes)" label.

.. tip::

   The unit, subsection, or section must be re-published for the change to take affect in the LMS.

Rename a non-Text Component
===========================

#. In Studio, open the unit that contains the library-sourced component you
   want to rename.

#. Select the pencil icon next to the component's title to make it editable.

   ..  image:: /_images/educator_how_tos/library_UnitPageVideo-1-PencilIcon.png
      :alt: The pencil icon appears in the top right of the component editor, above the main content.

#. Enter the new title.

   ..  image:: /_images/educator_how_tos/library_UnitPageVideo-2-TypeEdits.png
      :alt: The new title is entered in the top bar of the component editor.

#. Press Enter on your keyboard, or select outside the field, to save the change.

   ..  image:: /_images/educator_how_tos/library_CourseOutline-3-RenameSaved.png
      :alt: The component is now renamed. The change is now staged for publish.

The component now displays your custom title in the course. The title in the
source library is not affected.

.. tip::

   The component must be re-published for the change to take affect in the LMS.

Rename a Text Component
=======================

#. In Studio, open the unit that contains the library-sourced component you want to rename.

#. Select the pencil icon next to the text component's title to make it editable.

   ..  image:: /_images/educator_how_tos/library_UnitPageText-1-PencilIcon.png
      :alt: The pencil icon appears in the top right of the component editor, above the main content.

#. Select the pencil icon next to the component's title in the modal.

   ..  image:: /_images/educator_how_tos/library_UnitPageText-2-ModalPencilIcon.png
      :alt: In the pop-up modal, the title bar of the text component will have a edit icon to the right of the text component's title.

#. Select the checkmark icon to save the new title.

   ..  image:: /_images/educator_how_tos/library_UnitPageText-4-SaveEdit1.png
      :alt: In the editable field, a checkmark icon (with tooltip "Save") appears inline with the editable field.

#. Select the save button at the bottom of the modal to save the change.

   ..  image:: /_images/educator_how_tos/library_UnitPageText-5-SaveEdit2.png
      :alt: After saving the title, focus returns to the modal. The Save button in the bottom right corner will save your changes.

.. tip::

   The text component must be re-published for the change to take affect in the LMS.

How Title Overrides Interact with Syncing
******************************************

When you sync library-sourced content that has a locally overridden title,
your custom title is always preserved. Syncing never overwrites a title
override, even if the title has been updated in the source library.

There is one exception: if a piece of content is deleted in the library and
you accept that sync, the content is removed from your course even if it had
a local title override.

.. seealso::

   :ref:`Add Library Content to a Course` (how-to)

   :ref:`Sync a Library update to your course` (how-to)

   :ref:`Override Text Content in a Library-Referenced Component` (how-to)

   :ref:`Override Text Content in a Library-Sourced Structural Block` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-04-08   | sarina                        | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+