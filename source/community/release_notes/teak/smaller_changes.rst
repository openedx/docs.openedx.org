Smaller Changes (Potpourri)
############################

Remove Before Publish
**********************

https://openedx.atlassian.net/wiki/spaces/OEPM/pages/4913561601/Potpourri+Product+Facing+for+Teak

.. contents::
  :local:
  :depth: 1

Preview Button Improvement
****************************

The “Preview” button in Studio now uses the Learning MFE rather than the legacy
experience. This will improve your ability to understand how the content you
author will be seen by learners in your course.

Problem Editor Improvements
****************************

* Similar to the old editor, when course authors add new components to their
  course outlines, the component editors (text editor, video editor, etc) float
  in context above the course outline. This ensures that authors can maintain
  their place within the course structure when creating new content, rather than
  navigating away from the outline. This reduces the chance of error and makes
  the authoring process more efficient.

* The new (React-based) editor now provisionally supports Markdown via course
  waffle flag. Instance administrators can enable the Markdown editor by
  enabling the ``contentstore.use_react_markdown_editor`` feature flag.
  (NOTE: Change this if https://github.com/openedx/edx-platform/pull/36602 is merged.)

* The new editor is now the default for all Open edX sites. Previously, it was
  the default in Tutor-based sites, but the old editor was the default in
  non-Tutor sites. On all sites, site administrators can disable the new editor
  experience by enabling the course waffle flag
  ``legacy_studio.problem_editor``. In Ulmo, this option will be removed: only
  the new editor will be available.

Improvements to Common Cartridge Support
*****************************************

The Common Cartridge standard is now better integrated into the Open edX
platform. This makes it easier to migrate learning content created using Common
Cartridge into the Open edX olx format. This initiative includes enhancing the
existing ``cc2olx`` converter to improve its reliability and efficiency in
translating ``.imscc`` files into ``.tar.gz`` formats for import onto the Open edX
platform.

Link to RG docs when available.

Libraries v1 Migrations
************************

Kyle to write.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-05-08   | Product Working Group         | Teak           |  In Progress                   |
+--------------+-------------------------------+----------------+--------------------------------+