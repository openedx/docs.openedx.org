.. _Documentation Syntax Reference:

Quick Reference: Writing RST and Markdown
##########################################

.. tags:: documentor, reference

RST and MyST Markdown are both powerful and flexible. Below, we provide a quick guide for how you
can use them to write Open edX documentation.

Headings
********

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

         Heading 1
         #########

         There should be only 1 Heading 1 per topic, as the topic title.
         The underline must match the length of the text above it.

         Heading 2
         *********

         Heading 2s denote the main sections of a topic.

         Heading 3
         =========

         Heading 3s denote subsections under Heading 2s.

         Heading 4
         ---------

         Heading 4s denote subsections under Heading 3s.

         Heading 5
         ~~~~~~~~~

         Heading 5s denote subsections under Heading 4s.
         If you are this deep, consider splitting your document into multiple topics.

   .. tab-item:: Markdown

      .. code-block:: markdown

         # Heading 1

         There should be only 1 Heading 1 per topic, as the topic title.

         ## Heading 2

         Heading 2s denote the main sections of a topic.

         ### Heading 3

         Heading 3s denote subsections under Heading 2s.

         #### Heading 4

         Heading 4s denote subsections under Heading 3s.

         ##### Heading 5

         Heading 5s denote subsections under Heading 4s.
         If you are this deep, consider splitting your document into multiple topics.

.. tip::
   

   **RST**: Here's a way to remember the symbols for heading levels: ``#`` has four lines, ``*`` has three lines, ``=`` has two lines, ``-`` has one line, and ``~`` has zero lines.

.. note::
   

   **RST**: RST allows you to use almost any symbol to underline headings as long as you're consistent between heading levels. However, the abovementioned way is how headings should be defined in all Open edX documentation.
   
   **Markdown**: Markdown uses 1-6 ``#`` symbols for heading levels 1-6.

How To Use Sections Effectively
*******************************

You can nest sections in the topic as needed to structure it and break it into discrete parts.

Copy the Topic and Section Structure below as needed.

.. tab-set::

   .. tab-item:: RST

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

   .. tab-item:: Markdown

      .. code-block:: markdown

         # Topic Title

         Introduce the topic

         If this is a long topic with multiple sections, use the **contents** directive below:

         ```{contents} Contents
         :depth: 1
         :local:
         ```

         ## Section 1

         Introduce Section One

         ### Subsection 1

         Content for Section 1/Subsection 1

         ### Subsection 2

         Content for Section 1/Subsection 2

         ## Section 2

         Introduce Section Two

         ### Subsection 1

         Content for Section 2/Subsection 1

         ### Subsection 2

         Content for Section 2/Subsection 2


Inline Markup
*************

Both RST and MyST Markdown support **bold**, *italic*, and ``mono-spaced`` characters.

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

         Use double asterisks for **bold** text.

         Use single asterisks for *italic* text.

         Use double backticks for ``mono-spaced`` text.

         Use the guilabel role for :guilabel:`GUI elements`

   .. tab-item:: Markdown

      .. code-block:: markdown

         Use double asterisks for **bold** text.

         Use single asterisks for *italic* text.

         Use single backticks for `mono-spaced` text.

         Use the guilabel role for {guilabel}`GUI elements`

Lists
*****

You can make numbered and bulleted lists that can nest arbitrarily.

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

         #. Item 1
                                 # Need this blank line between items and sub-items
            * Sub-item 1         # Sub-items of ordered lists need to be indented by
            * Sub-item 2         # 3 spaces

         #. Item 2

         * Item 1

           #. Sub-item 1         # Sub-items of unordered lists need to be indented
           #. Sub-item 2         # by exactly 2 spaces

         * Item 2

   .. tab-item:: Markdown

      .. code-block:: markdown

         1. Item 1

            * Sub-item 1
            * Sub-item 2

         2. Item 2

         * Item 1

           1. Sub-item 1
           2. Sub-item 2

         * Item 2

Both examples above produce the following published list:

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

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

         You can have `inline links <https://example.com>`_

         `Indirect links`_ can be useful if you want to link to the same thing
         multiple times, or if the url is really long and you want things to read more
         cleanly.

         .. _Indirect links: http://example.com/?lorem=Lorem%20ipsum%20dolor%20sit

   .. tab-item:: Markdown

      .. code-block:: markdown

         You can have [inline links](https://example.com)

         [Indirect links] can be useful if you want to link to the same thing
         multiple times, or if the url is really long and you want things to read more
         cleanly.

         [Indirect links]: http://example.com/?lorem=Lorem%20ipsum%20dolor%20sit


Links within a document
=======================

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

         .. _some_location:

         New Subsection Title
         --------------------

         Some text at this location.


         Some other stuff that links back to :ref:`some_location`.

   .. tab-item:: Markdown

      .. code-block:: markdown

         (some_location)=
         ## New Subsection Title

         Some text at this location.

         Some other stuff that links back to {ref}`some_location`.


Links between documents
=======================

.. warning::

   Previously, we recommended using the ``:doc:`` directive to link between
   documents. However, ``:doc:`` is fragile, and can break when files are
   reorganized and renamed, whereas references generally follow the text to
   other files as reorganization happens. Thus it is strongly recommended to use
   ``:ref:`` only to cross-link between documents, even those in other docs
   projects.

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

         Link to :ref:`reference in another file`, where another file has a location marked as such:

         .. _reference to another file:

         Link to :ref:`openedx-proposals:OEP-51 Conventional Commits` to link to
         a reference in another "book" (Open edX documentation project). The
         full list of available books can be found in the root file conf.py, in
         the "intersphinx_mapping" section, for example, "openedx-events" or "openedx-aspects".

   .. tab-item:: Markdown

      .. code-block:: markdown

         Link to {ref}`reference in another file`, where another file has a location marked as such:

         .. _reference to another file:

         Link to {ref}`openedx-proposals:OEP-51 Conventional Commits` to link to
         a reference in another "book" (Open edX documentation project). The
         full list of available books can be found in the root file conf.py, in
         the "intersphinx_mapping" section, for example, "openedx-events" or "openedx-aspects".


.. _RST Directives:

Directives
**********

Both RST and MyST Markdown can do a lot of things via `directives`_. Here are some common ones:

.. _directives: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives

.. tab-set::

   .. tab-item:: RST

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

   .. tab-item:: Markdown

      .. code-block:: markdown

         ```{warning}
         This is a warning.

         It will be styled to stand-out in the documentation.
         ```

         ```{note}
         This is a note.

         It will stand-out but not as much as a warning.
         ```

         ```{image} path/to/image.png
         :alt: Alternative text for accessibility.
         ```

         ```python
         Some python code.
         ```

         ```{seealso}
         [Link to a thing](https://example.com)
         : A brief description of the thing

         [Link to another thing](https://example.com/other)
         : A brief description of another thing.
         ```

      .. tip::
      
         **MyST Nesting**: When nesting directives in MyST Markdown, use more backticks for outer directives than inner ones:
         
         .. code-block:: markdown
         
            ````{note}
            This is an outer note.
            
            ```{warning}
            This warning is nested inside the note.
            ```
            ````

Tables
******

To add a table like the following example:

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

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

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

   .. tab-item:: Markdown

      .. code-block:: markdown

         | Code Number   | #1                                                           |
         |---------------|--------------------------------------------------------------|
         | Title         | Table Example                                                |
         | Last-Modified | 2024-11-08                                                   |
         | Documents     | - Open edX Documentors Style Guide<br>- Open edX Diataxis Criteria<br>- Example 3<br>- Example 4<br>- Example 5 |

.. seealso:: To see alternative ways of defining tables, visit the `RST documentation about this topic <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/#tables>`_.

Add a Substitution
******************

A *substitution* serves as a variable which you can set a value for once, then use repeatedly. This is useful for words or phrases that are used often, as it enables you to edit the value once and change it everywhere.

Substitutions are all kept in the source/substitutions.txt file in the documentation project on GitHub.

Copy the format for the substitution as needed.

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

        .. |variable name| replace:: value

        .. |Platform name| replace:: Open edX

      You then add the *variable name* inline in the topic.

      .. code-block:: RST

        A line of text with an |variable name| inserted.

   .. tab-item:: Markdown

      MyST Markdown substitutions work the same way as RST:

      .. code-block:: markdown

        .. |variable name| replace:: value

        .. |Platform name| replace:: Open edX

      You then add the *variable name* inline in the topic.

      .. code-block:: markdown

        A line of text with an |variable name| inserted.


Add a Sidebar
*************

You can add any content in a sidebar. Open edX documentation uses sidebars for image thumbnails, videos, and other notes.

The sidebar must come directly after a heading.

Copy this codeblock to add a new sidebar topic.

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

        .. sidebar:: Sample Sidebar

          Any content, typically an image, video, or note.

   .. tab-item:: Markdown

      .. code-block:: markdown

        ```{sidebar} Sample Sidebar
        Any content, typically an image, video, or note.
        ```

Add an Image to a Topic
***********************

You can add an image on its separate line, inline, or in a sidebar.

You can also add an image directly or add a thumbnail of a larger image, which, when clicked on, will open the full image.

You must save images in the ``source/_images`` directory before adding a reference to it in a topic. 

Add an Image on its Own Line
============================

Copy this codeblock to an image on its own line.

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

        Line of content, followed by a line with an image.

        .. image:: /_images/image-file-name

        Or, a line of content, followed by a clickable thumbnail of a large image.

        .. thumbnail:: /_images/image-file-name

   .. tab-item:: Markdown

      .. code-block:: markdown

        Line of content, followed by a line with an image.

        ```{image} /_images/image-file-name
        ```

        Or, a line of content, followed by a clickable thumbnail of a large image.

        ```{thumbnail} /_images/image-file-name
        ```

Add an Image Inline
===================

To add an image inline, you must first create a substitution for the image in the substitutions.txt file.

Copy the format for the substitution as needed.

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

        .. |variable name| image:: /_images/image-file-name

      You then add the *variable name* inline in the topic.

      .. code-block:: RST

        A line of text with an |variable name| inserted.

   .. tab-item:: Markdown

      .. code-block:: markdown

        .. |variable name| image:: /_images/image-file-name

      You then add the *variable name* inline in the topic.

      .. code-block:: markdown

        A line of text with an |variable name| inserted.

Add a Thumbnail in a Sidebar
============================

You can add a thumbnail in a sidebar, a common practice for How-to topics.

The sidebar must come directly after a heading.

Copy this codeblock to add a new sidebar with a thumbnail.

.. tab-set::

   .. tab-item:: RST

      .. code-block:: RST

        .. sidebar:: Sample Sidebar with a thumbnail

          .. thumbnail:: _images/image-file-name

   .. tab-item:: Markdown

      .. code-block:: markdown

        ```{sidebar} Sample Sidebar with a thumbnail
        ```{thumbnail} _images/image-file-name
        ```

Learn More
**********

.. seealso::

   **RST Resources:**

   :download:`A one-page RST reference document <RST_quick_reference.pdf>` (PDF)
      This reference document summarizes the RST rules in an easy-to-print reference guide.

   `RST Primer`_
      The primer has a lot more detail about the concepts behind RST markup.

   `RST Docs`_
      If you want even more details about RST, check out the full RST documentation.

   **MyST Markdown Resources:**

   :ref:`MyST Markdown Syntax Sample`
      A complete sample page written in MyST Markdown demonstrating all the syntax examples.

   `MyST Parser Documentation`_
      Complete documentation for MyST Markdown syntax and features.

   `MyST Syntax Guide`_
      A comprehensive guide to MyST Markdown syntax.


.. _RST Primer: https://docutils.sourceforge.io/docs/user/rst/quickstart.html
.. _RST Docs: https://docutils.sourceforge.io/rst.html
.. _MyST Parser Documentation: https://myst-parser.readthedocs.io/
.. _MyST Syntax Guide: https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html


.. seealso::

   :ref:`About Open edX Documentation Standards` (concept)

   :ref:`Documentor Guidelines` (reference)

   :ref:`Documentation Maintenance Process` (reference)

   :ref:`Guidelines for Writing Global English` (reference)

   :ref:`Open edX Documentation Writing Style Guide` (reference)

   :ref:`Documentation Templates` (reference)

   :ref:`Documentation Audiences` (concept)

   :ref:`Update An Existing Doc via GitHub` (how-to)

   :ref:`Add New Documentation via GitHub` (how-to)

   :ref:`Report a problem with the docs` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
