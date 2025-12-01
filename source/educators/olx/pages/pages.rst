.. _Course Tabs OLX:

########################################
Create Course Tabs in OLX
########################################

.. tags:: educator, how-to

Authors can add custom tabs, or pages, to a course. Each page appears in the course's
navigation bar.

*********************************************
Create the Tab File
*********************************************

For each custom page in the course, create an HTML file in the
``tabs`` directory. It can be as simple as this:

*Contents of* ``html_custom_tab.html``:

.. code-block:: html

  <h1>Welcome to the OLX Example Course!</h1>

  <p>This is a custom HTML page added as a custom tab to the course.</p>

Any text and HTML markup can be added to the page. Pages can also be links or
other types of content. One design pattern is to link a tab to a chromeless
XBlock in the courseware, which allows for top-level interactive course
content.

Ensure the custom tab is placed properly in the ``policy.json`` file as detailed
in :ref:`Course Policies`.

.. code-block:: json

  {
    "course/2025": {
    {
        "course_staff_only": false,
        "name": "HTML Custom Tab",
        "type": "static_tab",
        "url_slug": "html_custom_tab"
    },
  }



.. seealso::

  :ref:`What is Open Learning XML?` (concept)

  :ref:`Course Policies` (reference)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
