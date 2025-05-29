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

* The new (React-based) editor now provisionally supports Markdown via course
  waffle flag. Instance administrators can enable the Markdown editor by
  enabling the ``contentstore.use_react_markdown_editor`` feature flag.
  (NOTE: Change this if https://github.com/openedx/edx-platform/pull/36602 is merged.)

* Similar to the old editor, the new editor now floats on top of unit page
  instead of taking up the entire screen.

* The new editor is now the default for all Open edX sites. Previously, it was
  the default in Tutor-based sites, but the old editor was the default in
  non-Tutor sites. On all sites, site administrators can disable the new editor
  experience by enabling the course waffle flag
  ``legacy_studio.problem_editor``. In Ulmo, this option will be removed: only
  the new editor will be available.

Libraries v1 Migrations
************************

Kyle to write.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-05-08   | Product Working Group         | Teak           |  In Progress                   |
+--------------+-------------------------------+----------------+--------------------------------+