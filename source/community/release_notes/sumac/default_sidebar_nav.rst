Sidebar Navigation Release Notes (Sumac)
########################################

The Product, Design, and Engineering Teams at Western Governor's University,
Raccoon Gang, and Axim Collaborative are thrilled to offer a new method for
navigating course content on the Open edX platform! With the Sumac Release, the
sidebar navigation will be offered as the default course navigation experience,
giving learners and course delivery teams a new method for making their way
through course content. Site operators should see :doc:`dev_op_release_notes`
for more detail.

.. include:: ../redwood/sidebar_nav.rst
    :start-after: sidebar_nav_content_marker

.. note::

    Known issues with sidebar navigation include:
    
    * When a member of the course delivery team updates the name of a course
      unit, the unit name updates at the top of the unit page, but does not
      update in the sidebar navigation.
    * When using content groups in a course, the sidebar navigation does not
      hide hidden units when a staff user views the course as a content group
      using the masquerading feature. Content groups work as expected for real
      learners in content groups. Staff can masquerade as an individual user in
      a specific content group to view how a member of the content group
      actually sees the course and the sidebar.
    * Course sections, subsections, and unit names may appear as missing from
      the sidebar navigation in sections that include content that has yet to be
      published.
