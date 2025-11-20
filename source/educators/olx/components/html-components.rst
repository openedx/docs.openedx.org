.. _HTML Components:

#################################
HTML Components in OLX
#################################

.. tags:: educator, reference

.. contents::
   :local:
   :depth: 1

*********************************************
Create the HTML Component
*********************************************

To add an HTML component to your course, split it up into 2 files: The HTML
configuration into an .xml file in the html directory and an additional .html
file in the same directory.

.. caution::
  
  If you are including HTML that is not valid HTML, you must break out HTML content in a separate file.


*********************************************
Example of XML & HTML Files
*********************************************

You create an XML file in the ``html`` directory for the content that you
choose to break out into separate HTML files.

The name of the XML file must match the value of the @url_name attribute of the
``html`` element in the vertical XML file.

For example, the ``vertical/unit_1_what_is_olx.xml`` file contains the following
``url_name``.

.. code-block:: xml

  <vertical display_name="Unit 1: What is OLX?">
    <html url_name="what_is_olx"/>
    . . .
  </vertical>

This references the file ``html/what_is_olx.xml`` to define the HTML component.

*************************************
Example HTML Component XML File
*************************************

The following example shows the ``html/what_is_olx.xml`` file for an HTML component.

.. code-block:: xml

  <html filename="what_is_olx" display_name="What is OLX?"/>

*************************************
``html`` Element Attributes
*************************************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``display_name``
     - Required. The value that is displayed to learners as the name of the
       HTML component. If you do not supply a ``display_name`` value, "html" is
       supplied for you.
   * - ``filename``
     - The name of the HTML file that contains the content for the HTML
       component, without the ``.HTML`` extension.


*************************************
HTML Component XML File Elements
*************************************

The root element of the XML file for the HTML component is file is ``html``.

In this case, the ``html`` element contains no children.

*************************************
Example HTML Component Content
*************************************

In the component's HTML file, you add valid HTML to represent the content you
want to be displayed to learners. For example, the following is from an HTML
file from the olx_example_course:

.. code-block:: html

  <p><span style="font-size: 1em;">OLX (open learning XML) is the XML-based standard used to build courses for the Open edX Platform.</span></p>
  <p><span style="font-size: 1em;">With OLX, you can:</span></p>
  <ul>
  <li>Move content between Open edX instances.</li>
  <li>Create course content outside of Open edX Studio, including by conversion from other content formats.</li>
  <li>Ensure content remains free of proprietary encoding and allow portability.</li>
  </ul>


.. seealso::

  :ref:`What is Open Learning XML?` (concept)

  :ref:`About Text Components` (concept)
  
  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
