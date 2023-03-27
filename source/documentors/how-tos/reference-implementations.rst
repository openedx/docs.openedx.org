Heading 1
#########

There should be only 1 Heading 1 per topic, as the topic title.

Heading 2
*********

Heading 2s denote the main sections of a topic.

Heading 3
=========

Heading 3s denote subsections under Heading 2s

Heading 4
---------

Heading 4s denote subsections under Heading 3s


Inline Markup
=============

Use double asterisks for **bold** text.

Use single asterisks for *italic* text.

Use double backticks for ``mono-spaced`` text.

Use the guilabel role for :guilabel:`GUI elements`


Lists
=====

#. Item 1
#. Item 2


* Item 1
* Item 2

.. code-block:: RST

   #. Item 1
   #. Item 2


.. code-block:: RST

   * Item 1
   * Item 2


#. Item 1

   * Sub-item 1
   * Sub-item 2

#. Item 2




Links offsite
=============

You can have `inline links <https://example.com>`_

`Indirect links`_ can be useful if you want to link to the same thing
multiple times, or if the url is really long and you want things to read more
cleanly.

.. _Indirect links: http://example.com/?lorem=Lorem%20ipsum%20dolor%20sit

Links within
============



Some text at this location.





Links between
=============

Link to ``file_b`` in the same folder or ``file_c`` in a different
folder or ``/file_d`` relative to the root of the project.

By default it will use the title of the doc as the link text but you can
override that with ``other text`` if you want.
which


Directives
==========

.. warning::  This is a warning.

   It will be styled to stand-out in the documentation.

.. note:: This is a note.

   It will stand-out but not as much as a warning.


Tip: Use ``:height:`` or ``:width:`` to scale your image!

.. image:: ../../_images/documentors_howto/make_changes_to_pr/gnu_wizard.svg
   :height: 200
   :alt: Alternative text for accessibility.

.. code-block::python

   Some python code.

.. seealso::

   `Link to a thing <https://example.com>`_
      A brief description of the thing

   `Link to another thing <https://example.com/other>`_
      A brief description of another thing.
