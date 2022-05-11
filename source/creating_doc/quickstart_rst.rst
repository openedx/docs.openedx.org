Quick Start: Writing RST
########################

RST is very powerful, and flexible.  Below we provide a quick guide for how you
can use it to write Open edX documentation.

For more details check out the `RST Primer`_

.. _RST Primer: https://docutils.sourceforge.io/docs/user/rst/quickstart.html

Headings
********

.. code-block:: RST

   Heading 1
   #########

   Heading 2
   *********

   Heading 3
   =========

   Heading 4
   ---------

.. note::
   :class: dropdown

   RST is very flexible: it will allow you to use almost any symbol to underline headings, as long as you're consistent between heading level. However, the way shown above is how headings should be defined in all Open edX documentation. 

Text Markup
***********

RST supports **bold**, *italic*, and ``mono-spaced`` characters. You can also make GUI elements appear as :guilabel:`GUI elements`.

.. code-block:: RST

   Use double asterisks for **bold** text.

   Use single asterisks for *italic* text.

   Use double backticks for ``mono-spaced`` text.

   Use the guilabel role for :guilabel:`GUI elements`

Lists
*****

You can make numbered, and bulleted lists that can nest arbitrarily.

#. Item 1

   * Sub-item 1
   * Sub-item 2
#. Item 2

.. code-block:: RST

   #. Item 1
                           # Need this blank line between items and sub-items
      * Sub-item 1
      * Sub-item 2
   #. Item 2

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

   .. some_location:

   Some text at this location.


   Some other stuff that links back to :ref:`some_location`.


Links between rst documents
===========================

.. code-block:: RST

   Link to :doc:`file_b` in the same folder or :doc:`../file_c` in a different
   folder or doc:`/file_d` relative to the root of the project.

   By default it will use the title of the doc as the link text but you can
   override that with doc:`other text </file_d>` if you want.
   which


Directives
**********

RST can do a lot of things via `directives`_. Here are the most useful ones:

.. _directives: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives

.. code-block:: RST

   .. warning::  This is a warning.

      It will be styled to stand-out in the documentation.

   .. note:: This is a note.

      It will stand-out but not as much as a warning.

   .. image:: path/to/image.png
      :alt: Alternative text for accessibility.

Learn More
**********

The `RST Primer`_ has a lot more detail about the concepts behind the markup and
if you want even more details, check out full `RST Docs`_.

.. _RST Docs: https://docutils.sourceforge.io/rst.html


