.. _Quickstart Document Template:

Quickstart Document Template
############################

.. tags:: documentor, quickstart

What Is a Quickstart
********************
A quickstart is a brief, streamlined guide that helps users get up and running with a tool, project, or system as quickly as possible. Quickstarts focus on the essential steps to start working with a particular technology, often covering:

#. **Setup Requirements** – Prerequisites like software dependencies or configuration steps.

#. **Installation** – How to install the necessary files or dependencies.

#. **Primary Usage** – Commands or actions to perform basic operations.

#. **Testing and Verification** – Ways to ensure everything is working correctly.

#. **Common Next Steps** – Information on where to go next, often with links to detailed documentation.

A good quickstart is designed for users who want to dive in with minimal setup. For example, allowing developers to try out a tool or platform without wading through extensive documentation upfront, or empowering course authors to quickly get up and running with a complex area of Studio.

For this Quickstart template, we will go through the process of creating this document, including how to add or embed one document in another and the principal tools to guide a learner.

Because a Quickstart is usually composed of two or more How-tos and some concepts and references, it is essential to add a table of contents to guide the reader through the document. For example:

1. `What Is a Quickstart`_
2. `Prerequisites Example`_
3. `How To Embed One Document in Another`_
4. `How To Embed Only a Section`_
5. `Useful Resources`_

Prerequisites Example
**********************

- Outline required knowledge (e.g., familiarity with Open edX basics).
- List any tools or configurations needed (e.g., access to an Open edX instance, software, or plugins).

How To Embed One Document in Another
************************************

A Quickstart may be the union of different documents, such as how-tos, references, and concepts. To avoid duplicate documents, you can embed one document into another using the ``include`` directive. This directive allows you to include the content of another file located in the same repository. Here's how you can do it:

1. Copy the following code in the file to embed the other document.

.. code-block:: RST

	.. include:: path/to/other_file.rst

2. Replace the example path with the embedded document path. For example:

.. code-block:: RST

	include:: ../templates/doc_how_to_template.rst

How to Embed Only a Section
***************************

If you want to include or embed only certain sections of a document, you can follow these steps:

1.  Open the document you want to embed. Add ``.. START HERE`` at the beginning and ``.. END HERE`` at the end of the section you want to embed.

2. You will embed the other document in the document. Use the following code to the exact place where you want to add that particular section. Do not forget to edit the document link that you want to include in your Quickstart.

.. code-block:: RST


	.. include:: docs/section1.rst
  		:start-after: .. START HERE
   		:end-before: .. END HERE

The reader will see something like this:

How-To Document Template Section
================================

.. include:: ../templates/doc_how_to_template.rst
 	:start-after: .. START HERE
 	:end-before: .. END HERE

Useful Resources
****************

Here is a list of the most used resources to create a Quickstart:

Images
=======

Add the images and audiovisual resources you think could be necessary to clarify the process. Remember that the callouts should be in Open edX red ``(#d23228)`` and round-edged rectangles.

.. code-block:: RST

	.. image:: /_images/documentors_howto/image_example.png
		:width: 500px
		:align: center
		:alt: This image example shows how to access the GitHub repository from the Open edX documentation repository.

.. image:: /_images/documentors_howto/image_example.png
		:width: 500px
		:align: center
		:alt: This image example shows how to access the GitHub repository from the Open edX documentation repository.

Links
======

External Links
--------------

You can use `inline links <https://docs.openedx.org/en/latest/documentors/references/quick_reference.html#linking>`_ or `indirect links`_. Indirect links are useful if you want to link to the same thing multiple times, or if the URL is really long and you want the raw RST to read more cleanly.

.. _Indirect links: https://docs.openedx.org/en/latest/documentors/references/quick_reference.html#linking

Directives:
===========

Usually, for this type of document, you can use different directives like ``warning``, ``note``,  and ``see also``, among others.

..  see also:: Review the Open edX Documentation Writing Style Guide to learn more about directives and other resources for creating your documentation.


RST Template
************

.. code-block:: RST

	Quickstrat Document Template
	############################

	What Is a Quickstart
	********************
	A quickstart is a brief, streamlined guide that helps users get up and running with a tool, project, or system as quickly as possible. Quickstarts focus on the essential steps to start working with a particular technology, often covering:

	#. **Setup Requirements** – Prerequisites like software dependencies or configuration steps.

	#. **Installation** – How to install the necessary files or dependencies.

	#. **Primary Usage** – Commands or actions to perform basic operations.

	#. **Testing and Verification** – Ways to ensure everything is working correctly.

	#. **Common Next Steps** – Information on where to go next, often with links to detailed documentation.

	A good quickstart is designed for users who want to dive in with minimal setup. It benefits developers, allowing them to try out a tool or platform without wading through extensive documentation upfront.

	For this Quickstart template, we will go through the process of creating this document, including how to add or embed one document in another and the principal tools to guide a learner.

	Because a Quickstart is usually composed of two or more How-tos and some concepts and references, it is essential to add a table of contents to guide the reader through the document. For example:

	1. `What Is a Quickstart`_
	2. `Prerequisites Example`_
	3. `How To Embed One Document in Another`_
	4. `How To Embed Only a Section`_
	5. `Useful Resources`_

	Prerequisites Example
	**********************

	- Outline required knowledge (e.g., familiarity with Open edX basics).
	- List any tools or configurations needed (e.g., access to an Open edX instance, software, or plugins).

	How To Embed One Document in Another
	************************************

	A Quickstart may be the union of different documents, such as how-tos, references, and concepts. To avoid duplicate documents, you can embed one document into another using the ``include`` directive. This directive allows you to include the content of another file located in the same repository. Here's how you can do it:

	1. Copy the following code in the file to embed the other document.

	.. code-block:: RST

		.. include:: path/to/other_file.rst

	2. Replace the example path with the embedded document path. For example:

	.. code-block:: RST

		include:: ../templates/doc_how_to_template.rst

	How to Embed Only a Section
	***************************

	If you want to include or embed only certain sections of a document, you can follow these steps:

	1.  Open the document you want to embed. Add ``.. START HERE`` at the beginning and ``.. END HERE`` at the end of the section you want to embed.

	2. You will embed the other document in the document. Use the following code to the exact place where you want to add that particular section. Do not forget to edit the document link that you want to include in your Quickstart.

	.. code-block:: RST


		.. include:: docs/section1.rst
	  	:start-after: .. START HERE
	   	:end-before: .. END HERE

	The reader will see something like this:

	How-To Document Template Section
	--------------------------------

	.. include:: ../templates/doc_how_to_template.rst
	 	:start-after: .. START HERE
	 	:end-before: .. END HERE

	Useful Resources
	****************

	Here is a list of the most used resources to create a Quickstart

	Images
	======

	Add the images and audiovisual resources you think could be necessary to clarify the process. Remember that the callouts should be in Open edX red ``(#d23228)`` and round-edged rectangles.

	.. code-block:: RST

		.. image:: /_images/documentors_howto/image_example.png
			:width: 500px
			:align: center
			:alt: This image example shows how to access the GitHub repository from the Open edX documentation repository.

	.. image:: /_images/documentors_howto/image_example.png
			:width: 500px
			:align: center
			:alt: This image example shows how to access the GitHub repository from the Open edX documentation repository.

	Links:
	======

	External Links
	--------------

	You can use `inline links <https://docs.openedx.org/en/latest/documentors/references/quick_reference.html#linking>`_ or `indirect links`_. Indirect links are useful if you want to link to the same thing multiple times, or if the URL is really long and you want the raw RST to read more cleanly.

	.. _Indirect links: https://docs.openedx.org/en/latest/documentors/references/quick_reference.html#linking

	Directives:
	===========

	Usually, for this type of document, you can use different directives like ``warning``, ``note``,  and ``see also``, among others.

	..  see also:: Review the Open edX Documentation Writing Style Guide to learn more about directives and other resources for creating your documentation.

.. seealso::

   :ref:`About Open edX Documentation Standards` (concept)

   :ref:`Concept Document Template` (reference)

   :ref:`Reference Document Template` (reference)

   :ref:`How To Document Template` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
