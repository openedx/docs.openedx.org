.. _Ulmo LTI:

Reusable LTI Configurations
###########################

Ulmo supports an important platform improvement: centralized, reusable LTI
configurations powered by the new LTI Store.

.. image:: /_images/release_notes/ulmo/reusable_lti_configuration.png
   :alt: LTI component in editing mode, displaying the fields to be edited

This enhancement directly addresses a long-standing pain point: the repetitive,
error-prone process of entering LTI credentials (Client ID, Deployment ID, URLs,
keys, etc.) in every course and every LTI block. Now there's a cleaner, more
scalable way to manage these configurations across your instance.

Centralized LTI Store
*********************

Ulmo provides a reusable LTI store to centrally manage LTI tool credentials and
settings in Django Admin, which allows you to define LTI tool configurations
once, and reuse them anywhere across your Open edX instance.

.. note::

   Site operators will need to install the `ltistore plugin
   <https://github.com/openedx/openedx-tutor-plugins/tree/main/plugins/tutor-contrib-ltistore>`_
   to enable the reusable LTI store.

Reusable LTI Configurations in Studio
*************************************

Course authors can now add LTI tools in Studio using the LTI Consumer component
configured to reference a "reusable configuration" rather than requiring
credentials per course block.

See :ref:`Set up an LTI Consumer with Reusable LTI Configuration` for further
documentation.

.. note::

   In order to use the LTI Store, a site administrator will need to :ref:`Set up
   a Reusable LTI Store`.

Future Improvements for LTI
***************************

Building on the foundation laid in Ulmo, the LTI experience will continue to
improve with both short-term fixes and longer-term UX enhancements. For the
Verawood release, we will focus on high-impact technical fixes, including
ensuring configuration integrity when duplicating LTI blocks and improving
compatibility with Content Libraries. These updates enable reliable block-level
reusability and reduce the need for repeated configuration across courses.

Beyond Verawood, work will shift toward the redesigned LTI Consumer UX and
expanded support for global configurations at the course, organization, and site
levels. Some other lower-priority enhancements remain under consideration as the
new UX and structural improvements mature.

.. seealso::

   :ref:`About the LTI Component`

   :ref:`Set up an LTI Consumer with Reusable LTI Configuration`

   :ref:`Set up a Reusable LTI Store`

   :ref:`Ulmo LTI Certification`

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-12-11   | LTI WG                        | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+