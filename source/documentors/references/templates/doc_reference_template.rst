Reference Document Template
###########################

Reference material is information-oriented. Regarding software, reference guides describe the software - APIs, classes, functions, etc. In the context of the Open edX® Docs, reference docs are often in the form of informational lists (e.g., Resources for Students) and tables (e.g., Course Access Roles and Privileges).

Reference material is like a map. A map tells you what you need to know about the territory without having to go out and check it for yourself; a reference guide serves the same purpose for the product and its internal machinery. For example, this part works as the introduction to the article and as a description of the product of what this document is about. (Replace this text with your content.)

The purpose of this document is to be as straightforward as possible. In addition to an accurate and precise description of the product you’re referencing, use examples of the uses and functions of the product to make it more comprehensive.
For example, list details or a product glossary that the reader could need to use. (Replace this text with your content.)

Example Lists
=============

As mentioned, a reference document can contain lists detailing different elements, like a glossary or a list of resources to consult. Those lists could have different formats depending on their purpose. For example,

**Ordered Lists**
#. Reference A
#. Reference B
#. Reference C

Or

**Unordered Lists**
- Reference A
- Reference B
- Reference C


Table Example
=============

Another vital resource you can use to create a reference document is a table. For example:

+------------------+--------------------------------------------------------------+
| Example #        | 01                                                           |
+------------------+--------------------------------------------------------------+
| Title            | Table Example                                                |
+------------------+--------------------------------------------------------------+
| Last-Modified    | MM-DD-YYYY                                                   |
+------------------+--------------------------------------------------------------+
| Documents        | - Document 1                                                 |
|                  | - Document 2                                                 |
|                  | - Document 3                                                 |
+------------------+--------------------------------------------------------------+

Reference Links
===============
In this type of document, links are usually added to refer to other sources that may interest the reader, such as GitHub repositories or documents from this same repository.

External Links
--------------

You can have `inline links <https://docs.openedx.org/en/latest/documentors/references/quick_reference_rst.html#linking>`_ and `indirect links`_, that are useful if you want to link to the same thing multiple times, or if the URL is really long and you want things to read more cleanly.

.. _Indirect links: https://docs.openedx.org/en/latest/documentors/references/quick_reference_rst.html#linking

Internal Links
--------------

Link to :doc:`doc_how_to_template` in the same folder or :doc:`../quick_reference_rst` in a different
folder.

By default, it will use the title of the doc as the link text but you can override that with :doc:`other text <doc_how_to_template>` if you want.

RST Template
************

.. code-block:: RST

	Reference material is information-oriented. Regarding software, reference guides describe the software - APIs, classes, functions, etc. In the context of the Open edX® Docs, reference docs are often in the form of informational lists (e.g., Resources for Students) and tables (e.g., Course Access Roles and Privileges).

	Reference material is like a map. A map tells you what you need to know about the territory without having to go out and check it for yourself; a reference guide serves the same purpose for the product and its internal machinery. For example, this part works as the introduction to the article and as a description of the product of what this document is about. (Replace this text with your content.)

	The purpose of this document is to be as straightforward as possible. In addition to an accurate and precise description of the product you’re referencing, use examples of the uses and functions of the product to make it more comprehensive.
	For example, list details or a product glossary that the reader could need to use. (Replace this text with your content.)

	Example Lists
	=============

	As mentioned, a reference document can contain lists detailing different elements, like a glossary or a list of resources to consult. Those lists could have different formats depending on their purpose. For example,

	**Ordered Lists**

	#. Reference A
	#. Reference B
	#. Reference C

	Or

	**Unordered Lists**

	- Reference A
	- Reference B
	- Reference C


	Table Example
	=============

	Another vital resource you can use to create a reference document is a table. For example:

	+------------------+--------------------------------------------------------------+
	| Example #        | 01                                                           |
	+------------------+--------------------------------------------------------------+
	| Title            | Table Example                                                |
	+------------------+--------------------------------------------------------------+
	| Last-Modified    | MM-DD-YYYY                                                   |
	+------------------+--------------------------------------------------------------+
	| Documents        | - Document 1                                                 |
	|                  | - Document 2                                                 |
	|                  | - Document 3                                                 |
	+------------------+--------------------------------------------------------------+

	Reference Links
	===============
	In this type of document, links are usually added to refer to other sources that may interest the reader, such as GitHub repositories or documents from this same repository.

	External Links
	--------------

	You can have `inline links <https://docs.openedx.org/en/latest/documentors/references/quick_reference_rst.html#linking>`_ and `indirect links`_, that are useful if you want to link to the same thing multiple times, or if the URL is really long and you want things to read more cleanly.

	.. _Indirect links: https://docs.openedx.org/en/latest/documentors/references/quick_reference_rst.html#linking

	Internal Links
	--------------

	Link to :doc:`doc_how_to_template` in the same folder or :doc:`../quick_reference_rst` in a different folder.

	By default, it will use the title of the doc as the link text but you can override that with :doc:`other text </doc_how_to_template>` if you want.
