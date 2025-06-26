.. _Teak Potpourri:

Smaller Changes (Potpourri)
############################

.. contents::
  :local:
  :depth: 1

Preview Button Improvement
****************************

The “Preview” button in Studio now uses the Learning MFE rather than the legacy
experience. This will improve your ability to understand how the content you
author will be seen by learners in your course.

.. _Studio Changes (Teak):

Studio UI Modernization
************************

* Open edX Studio is now entirely displayed using the Studio MFE, debuted in
  Sumac. Teak adds the Unit Page editor to the MFE. Note that the legacy Studio
  pages will be removed in Ulmo.

* Similar to the old editor, when course authors add new components to their
  course outlines, the component editors (text editor, video editor, etc) float
  in context above the course outline. This ensures that authors can maintain
  their place within the course structure when creating new content, rather than
  navigating away from the outline. This reduces the chance of error and makes
  the authoring process more efficient.

* The new editor is now the default for all Open edX sites. Previously, it was
  the default in Tutor-based sites, but the old editor was the default in
  non-Tutor sites. On all sites, site administrators can disable the new editor
  experience by enabling the course waffle flag
  ``legacy_studio.problem_editor``. In Ulmo, this option will be removed: only
  the new editor will be available.

Problem Editor Improvements
****************************

The new (React-based) editor now supports Markdown by default via course
waffle flag. Instance administrators can disable the Markdown editor by
creating a flag, ``contentstore.use_react_markdown_editor``, with the value "No".


Improvements to Common Cartridge Support
*****************************************

The Common Cartridge standard is now better integrated into the Open edX
platform. This makes it easier to migrate learning content created using Common
Cartridge into the Open edX olx format. This initiative includes enhancing the
existing ``cc2olx`` converter to improve its reliability and efficiency in
translating ``.imscc`` files into ``.tar.gz`` formats for import onto the Open edX
platform.

For more detail, see the `cc2olx documentation <https://github.com/openedx/cc2olx?tab=readme-ov-file#cc2olx>`_.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-05-08   | Product Working Group         | Teak           |  In Progress                   |
+--------------+-------------------------------+----------------+--------------------------------+