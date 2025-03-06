.. _Writing RST:

Quick Reference: Writing RST
############################

.. tags:: documentor, reference

RST is very powerful and flexible.  Below, we provide a quick guide for how you
can use it to write Open edX documentation.

Headings
********

.. include:: ../references/rst_samples/headings.txt

.. tip::
   

   Here's a way to remember the symbols for heading levels: ``#`` has four lines, ``*`` has three lines, ``=`` has two lines, ``-`` has one line, and ``~`` has zero lines.

.. note::
   

   RST allows you to use almost any symbol to underline headings as long as you're consistent between heading levels. However, the abovementioned way is how headings should be defined in all Open edX documentation.

How To Use Sections Effectively
*******************************

You can nest sections in the topic as needed to structure it and break it into discrete parts.

Copy the Topic and Section Structure below as needed.

.. code-block:: RST

   Topic Title
   ###########

   Introduce the topic

   If this is a long topic with multiple sections, use the **contents** directive below:

   .. contents:: Contents
      :depth: 1
      :local:

   Section 1
   *********

   Introduce Section One

   Subsection 1
   ++++++++++++

   Content for Section 1/Subsection 1

   Subsection 2
   ++++++++++++

   Content for Section 1/Subsection 2

   Section 2
   *********

   Introduce Section Two

   Subsection 1
   ++++++++++++

   Content for Section 2/Subsection 1

   Subsection 2
   ++++++++++++

   Content for Section 2/Subsection 2


Inline Markup
*************

RST supports **bold**, *italic*, and ``mono-spaced`` characters. You can also make GUI elements appear as :guilabel:`GUI elements`.

.. include:: ../references/rst_samples/inline.txt

Lists
*****

You can make numbered, and bulleted lists that can nest arbitrarily, using the **#** symbol for ordered lists and **\*** for unordered lists.


.. include:: ../references/rst_samples/nested_lists.txt


This codeblock is used for the following published list:

#. Item 1

   * Sub-item 1
   * Sub-item 2

#. Item 2

* Item 1

  #. Sub-item 1
  #. Sub-item 2

* Item 2

See the `RST guide on lists <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/lists.html>`_ for more detail.

Linking
*******

Links off-site
==============

.. code-block:: RST

   You can have `inline links <https://example.com>`_

   `Indirect links`_ can be useful if you want to link to the same thing
   multiple times, or if the url is really long and you want things to read more
   cleanly.

   .. _Indirect links: http://example.com/?lorem=Lorem%20ipsum%20dolor%20sit


Links within a document
=======================

.. code-block:: RST

   .. _some_location:

   New Subsection Title
   --------------------

   Some text at this location.


   Some other stuff that links back to :ref:`some_location`.


Links between rst documents
===========================

.. code-block:: RST

   Link to :doc:`file_b` in the same folder or :doc:`../file_c` in a different
   folder or doc:`/file_d` relative to the root of the project.

   By default it will use the title of the doc as the link text but you can
   override that with doc:`other text </file_d>` if you want.


.. _RST Directives:

Directives
**********

RST can do a lot of things via `directives`_. Here are some common ones:

.. _directives: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives

.. code-block:: RST

   .. warning::  This is a warning.

      It will be styled to stand-out in the documentation.

   .. note:: This is a note.

      It will stand-out but not as much as a warning.

   .. image:: path/to/image.png
      :alt: Alternative text for accessibility.

   .. code-block:: python

      Some python code.

   .. seealso::

      `Link to a thing <https://example.com>`_
         A brief description of the thing

      `Link to another thing <https://example.com/other>`_
         A brief description of another thing.

Tables
******

To add a table in RST like the following example:

+---------------+--------------------------------------------------------------+
| Code Number   | #1                                                           |
+---------------+--------------------------------------------------------------+
| Title         | Table Example                                                |
+---------------+--------------------------------------------------------------+
| Last-Modified | 2024-11-08                                                   |
+---------------+--------------------------------------------------------------+
| Documents     | - Open edX Documentors Style Guide                           |
|               | - Open edX Diataxis Criteria                                 |
|               | - Example 3                                                  |
|               | - Example 4                                                  |
|               | - Example 5                                                  |
+---------------+--------------------------------------------------------------+

Use the following code:

.. code-block::

   +---------------+--------------------------------------------------------------+
   | Code Number   | #1                                                           |
   +---------------+--------------------------------------------------------------+
   | Title         | Table Example                                                |
   +---------------+--------------------------------------------------------------+
   | Last-Modified | 2024-11-08                                                   |
   +---------------+--------------------------------------------------------------+
   | Documents     | - Open edX Documentors Style Guide                           |
   |               | - Open edX Diataxis Criteria                                 |
   |               | - Example 3                                                  |
   |               | - Example 4                                                  |
   |               | - Example 5                                                  |
   +---------------+--------------------------------------------------------------+

.. seealso:: To see alternative ways of defining tables, visit the `RST documentation about this topic <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/#tables>`_.

Add a Substitution
******************

In RST, a *substitution* serves as a variable which you can set a value for once, then use repeatedly. This is useful for words or phrases that are used often, as it enables you to edit the value once and change it everywhere.

You also need to use substitutions for inline images, as explained below.

Substitutions are all kept in the source/substitutions.txt file in the documentation project on GitHub.

Copy the format for the substitution as needed.

.. code-block:: RST

  .. |variable name| replace:: value

  .. |Platform name| replace:: Open edX

You then add the *variable name* inline in the topic.

.. code-block:: RST

  A line of text with an |variable name| inserted.


Add a Sidebar
*************

You can add any content in a sidebar. Open edX documentation uses sidebars for image thumbnails, videos, and other notes.

The sidebar must come directly after a heading.

Copy this codeblock to add a new sidebar topic.

.. code-block:: RST

  .. sidebar:: Sample Sidebar

    Any content, typically an image, video, or note.

Add an Image to a Topic
***********************

You can add an image on its separate line, inline, or in a sidebar.

You can also add an image directly or add a thumbnail of a larger image, which, when clicked on, will open the full image.

You must save images in the ``source/_images`` directory before adding a reference to it in a topic. 

Add an Image on its Own Line
============================

Copy this codeblock to an image on its own line.

.. code-block:: RST

  Line of content, followed by a line with an image.

  .. image:: /_images/image-file-name

  Or, a line of content, followed by a clickable thumbnail of a large image.

  .. thumbnail:: /_images/image-file-name

Add an Image Inline
===================

To add an image inline, you must first create a substitution for the image in the substitutions.txt file.

Copy the format for the substitution as needed.

.. code-block:: RST

  .. |variable name| image:: /_images/image-file-name

You then add the *variable name* inline in the topic.

.. code-block:: RST

  A line of text with an |variable name| inserted.

Add a Thumbnail in a Sidebar
============================

You can add a thumbnail in a sidebar, a common practice for How-to topics.

The sidebar must come directly after a heading.

Copy this codeblock to add a new sidebar with a thumbnail.

.. code-block:: RST

  .. sidebar:: Sample Sidebar with a thumbnail

    .. thumbnail:: _images/image-file-name

Learn More
**********

.. seealso::

   :download:`A one-page reference document <RST_quick_reference.pdf>` (PDF)
      This reference document summarizes the above rules in an easy-to-print reference guide.

   `RST Primer`_
      The primer has a lot more detail about the concepts behind the markup.

   `RST Docs`_
      If you want even more details, check out full `RST Docs`_.


.. _RST Primer: https://docutils.sourceforge.io/docs/user/rst/quickstart.html
.. _RST Docs: https://docutils.sourceforge.io/rst.html


