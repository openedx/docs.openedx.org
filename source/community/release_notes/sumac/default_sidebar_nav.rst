Sidebar Navigation Release Notes (Sumac)
########################################

The Product, Design, and Engineering Teams at Western Governor's University,
Raccoon Gang, and Axim Collaborative are thrilled to offer a new method for
navigating course content on the Open edX platform! With the Sumac Release, the
sidebar navigation will be offered as the default course navigation experience,
giving learners and course delivery teams a new method for making their way
through course content. Site operators should see :doc:`dev_op_release_notes`
for more detail.

.. note::

    There is one breaking issue with sidebar navigation:

    * Site operators using brand packages that override the ``max-width`` for ``.container-xl`` have reported an issue with sidebar navigation taking up half of the page and making course content 
      appear narrower than it should be when the sidebar is expanded. The default ``max-width`` is ``1600px`` and accommodates the space needed by the sidebar. As a result, the fix for this breaking 
      change is to make sure your brand package values are wide enough.

.. include:: ../redwood/sidebar_nav.rst
    :start-after: sidebar_nav_content_marker

.. include:: ../redwood/sidebar_nav.rst
    :start-after: sidebar_nav_issues_marker
    :end-before: sidebar_nav_content_marker