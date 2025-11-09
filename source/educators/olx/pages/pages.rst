.. _Course Tabs:

########################################
Create Course Tabs in OLX
#########################################

.. tags:: educator, how-to

You can add custom tabs, or pages, to your course. Each page appears in your course's
navigation bar.

*********************************************
Create the Tab File
*********************************************

For each page you want your course to offer, you create an HTML file in the
``tabs`` directory. It can be as simple as this:

*Contents of* ``html_custom_tab.html``:

.. code-block:: html

  <h1>Welcome to the OLX Example Course!</h1>

  <p>This is a custom HTML page added as a custom tab to the course.</p>

You can add any text and HTML markup to the page. Pages can also be links or
other types of content. One design pattern is to link a tab to a chromeless
XBlock in the courseware, which allows for top-level interactive course
content.

Ensure you place the custom tab properly in the ``policy.json`` file as detailed
in :ref:`Course Policies`.

.. code-block:: json

  {
    "course/2025": {
    ...

      {
          "course_staff_only": false,
          "name": "HTML Custom Tab",
          "type": "static_tab",
          "url_slug": "html_custom_tab"
      }
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
