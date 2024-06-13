Quick Reference: Writing RST
############################

RST is very powerful and flexible.  Below we provide a quick guide for how you
can use it to write Open edX documentation.

Headings
********

.. include:: ../references/rst_samples/headings.txt

.. tip::
   :class: dropdown
   
   Here's a way to remember the symbols for heading levels: ``#`` has four lines, ``*`` has three lines, ``=`` has two lines, ``-`` has one line, and ``~`` has zero lines.

.. note::
   :class: dropdown

   RST allows you to use almost any symbol to underline headings, as long as you're consistent between heading level. However, the way shown above is how headings should be defined in all Open edX documentation.


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

Learn More
**********

.. seealso::

   :download:`A one-page reference document <RST_quick_reference.pdf>` (PDF)
      This reference document summarizes the above rules in an easy to print reference guide

   `RST Primer`_
      The primer has a lot more detail about the concepts behind the markup.

   `RST Docs`_
      If you want even more details, check out full `RST Docs`_.


.. _RST Primer: https://docutils.sourceforge.io/docs/user/rst/quickstart.html
.. _RST Docs: https://docutils.sourceforge.io/rst.html


