.. _Concept Document Template:

Concept Document Template
#########################

.. tags:: documentor, reference

A concept is a document that clarifies and illuminates a particular topic. It is understanding-oriented. It could be considered a conceptual guide. This type of document answers a why question. It could be descriptive, historical, or even propose different alternatives to explain the bigger picture and give context.

For example, “What is an XBlock? The Open edX platform provides different components, called XBlocks, that can work to create a course, like text, video, assessment, and discussions”.

Since this type of document seeks to explain a topic, you will likely need to add images to illustrate the topic you are talking about. For example:


.. image:: /_images/documentors_howto/xblock_example.png
	:width: 500px
	:align: center
	:alt: This image shows the Advance Module List, where the XBlocks are added to the platform.

External Links
--------------

You can use `inline links <https://docs.openedx.org/en/latest/documentors/references/quick_reference.html#linking>`_ or `indirect links`_. Indirect links are useful if you want to link to the same thing multiple times, or if the URL is really long and you want the raw RST to read more cleanly.

.. _Indirect links: https://docs.openedx.org/en/latest/documentors/references/quick_reference.html#linking

Internal Links
--------------

Link to :doc:`doc_how_to_template` in the same folder or :ref:`Documentation Syntax Reference` in a different
folder.

By default, it will use the title of the doc as the link text but you can override that with :doc:`other text <doc_how_to_template>` if you want.

..  see also:: Review the Open edX Documentation Writing Style Guide to learn more about directives and other resources for creating your documentation.

RST Template
************

.. code-block:: RST

	Concept Document Template
	#########################

	A concept is a document that clarifies and illuminates a particular topic. It is understanding-oriented. It could be considered a conceptual guide. This type of document answers a why question. It could be descriptive, historical, or even propose different alternatives to explain the bigger picture and give context.

	For example, “What is an XBlock? The Open edX platform provides different components, called XBlocks, that can work to create a course, like text, video, assessment, and discussions.”

	Since this type of document seeks to explain a topic, you will likely need to add images to exemplify the topic you are talking about. For example:


	.. image:: /_images/documentors_howto/xblock_example.png
		:width: 500px
		:align: center
		:alt: This image shows the Advance Module List, where the XBlocks are added to the platform.

	External Links
	--------------

   .. warning::
      Usage of ``:doc:`` is an antipattern. It is fragile and prone to breaking cross references when docs are moved or renamed.

      Adding in ``.. _reference:`` syntax to files and headings means cross-references can instead be made with the ``:ref:`` directive, which will be more robust to docs refactorings.
	
	You can use `inline links <https://docs.openedx.org/en/latest/documentors/references/quick_reference.html#linking>`_ or `indirect links`_. Indirect links are useful if you want to link to the same thing multiple times, or if the URL is really long and you want the raw RST to read more cleanly.

	.. _Indirect links: https://docs.openedx.org/en/latest/documentors/references/quick_reference.html#linking

	Internal Links
	--------------

	Link to :doc:`doc_how_to_template` in the same folder or :ref:`Documentation Syntax Reference` in a different
	folder.

	By default, it will use the title of the doc as the link text but you can override that with :doc:`other text <doc_how_to_template>` if you want.

	..  see also:: Review the Open edX Documentation Writing Style Guide to learn more about directives and other resources for creating your documentation.


.. seealso::

   :ref:`About Open edX Documentation Standards` (concept)

   :ref:`Reference Document Template` (reference)

   :ref:`Quickstart Document Template` (reference)

   :ref:`How To Document Template` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
