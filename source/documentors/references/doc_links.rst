Add Links in a Topic
#####################

You can include links to other locations in the same document, to locations in other documents and to external websites.

For more information about creating links using RST and Sphinx, see `Sphinx Hyperlinks_`.

Links to Sections in the Same Document
****************************************************

You can link from text to a heading in any other part of the document by using the ``:ref:`` command with the target heading text as the parameter. For example, this text in another part of this document would link to this section:

.. code-block:: RST

  :ref:`Cross-References to Locations in the Same Document`

The heading text is printed as the link text.

.. note:: The heading text in the link must match the heading exactly.

Use Custom Link Text
=======================

For internal links that use text other than the heading for the section that you're linking to, use ``:ref:`custom text<Heading Text>``` syntax, as in the following example.

.. code-block:: RST

  Learn how to :ref:`link to a different section<Cross-References to Locations in the Same Document>`.

.. note:: Do not include a space between the last word of the link text and the opening angle bracket for the anchor text.

In this example, **link to a different section** is the link text, and **Cross-References to Locations in the Same Document** is the heading text.

Use a Custom Anchor
====================

When you have two sections with the same title in a project, you will get build errors when you have a link to either section, because Sphinx does not know which section to link to.

In this case, you can create a custom *anchor* directly above the title and link to it, instead of the title itself. For example, if you have a section called **Overview** in each part of your document, you should add a more specific anchor above the section heading.

.. code-block:: RST

  .. _RST Overview:

  Overview
  **********

  RST Overview content


  .. _Sphinx Overview:

  Overview
  *********

  Sphinx Overview content

In a ``:ref:`` command, you then use the anchor text. For example:

.. code-block:: RST

  This is a link to the RST Overview: :ref:`RST Overview`

  This is a link to the Sphinx Overview: :ref:`Sphinx Overview`

In both cases, the link text is the section title, **Overview**, unless you `Use Custom Link Text`_.

Links to External Web Pages
*****************************************

To link to an external web page, use the following syntax:

.. code-block:: RST

  `Link text <link URL>`_

For example:

.. code-block:: RST

  `CNN <http://cnn.com>`_

You can also separate the link and the target definition. For example:

.. code-block:: RST

  Get the latest news at `CNN`_.

  .. _CNN: http://cnn.com/

As a best practice, to avoid duplication, in Open edX documentation, all links are listed together in the ``source/links.txt`` file, which is included in every page during the build process.


TO VERIFY

Test External Links
=========================

You can use the built-in Sphinx command, ``checklinks`` to test all external
links in your document. The command checks that a working web page is accessed
at the given URL and reports any errors.

Add the following code to the project ``Makefile``:

.. code-block:: bash

  LINKCHECKDIR  = build/linkcheck

  .PHONY: checklinks
    checklinks:
    $(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(LINKCHECKDIR)
    @echo
    @echo "Check finished. Report is in $(LINKCHECKDIR)."

Then, from the command window, enter:

.. code-block:: bash

  make checklinks

Sphinx compiles the document and tests all links. It shows the results in the
command window, and writes results to the file ``output.txt`` in the build
directory.

