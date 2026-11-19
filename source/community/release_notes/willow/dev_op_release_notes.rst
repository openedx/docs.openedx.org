.. _Willow Dev Notes:

Open edX Willow Developer & Operator Release Notes
#####################################################

*Releasing December, 2026!*

These are the developer & operator release notes for the Willow release, the 23rd
community release of the Open edX Platform, spanning changes from April 10,
2025 to December 9, 2026. You can also review details about :ref:`Open edX Release Notes` or
learn more about the `Open edX Platform`_.

To view the end-user facing docs, see the :ref:`Willow Product Notes`.

.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
****************

Deprecations & Removals
***********************

* **Removed the built-in XBlock implementations.** As announced in the
  :ref:`Verawood Dev Notes`, the deprecated built-in implementations of the
  following blocks have been removed from ``openedx-platform``. The extracted
  implementations from `xblocks-core <https://github.com/openedx/xblocks-core>`_
  are now always used:

  * Annotatable Block
  * Discussion Block
  * HTML Block
  * LTI Block
  * Poll Block
  * Problem Block
  * Video Block
  * Word Cloud Block

  The ``USE_EXTRACTED_*_BLOCK`` settings in ``openedx/envs/common.py`` (for
  example, ``USE_EXTRACTED_VIDEO_BLOCK``) are removed. Setting them has no
  effect, so there's no longer a way to fall back to the built-in blocks.

  The ``xblock.v1`` entry point names (for example, ``video`` and ``problem``)
  are unchanged and now point to the xblocks-core packages, so existing course
  content keeps working. Custom code that imports from the removed modules
  (for example, ``xmodule.video_block``, ``xmodule.capa_block`` or
  ``xmodule.word_cloud_block``) must import from the xblocks-core packages
  instead (``xblock_video``, ``xblock_problem``, ``xblock_word_cloud``, and so
  on). ``xmodule.html_block`` remains, because it still provides the About,
  Static Tab and Course Info blocks.

  See the `slash-n-burn epic <https://github.com/openedx/openedx-platform/issues/37819>`_.

Aspects Analytics
*****************************

Administrators & Operators
**************************

Settings and Toggles
********************

Developer Experience
********************

Known Issues
************

See the `Build Test Release project board <https://github.com/orgs/openedx/projects/28>`_ for known open issues.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
