.. _How To Document Template:

How-To Document Template
########################

.. tags:: documentor, how-to

A How-To guide document guides the reader through the steps to solve a real-world problem. This documentation is goal-oriented and similar to recipes, with directions that guide the reader through the steps to achieve a specific end.

For example, following the steps in this How-To guide, you can create a how-to document for any repository for the Open edX platform.

.. START HERE

1. Copy this document into a new file to edit as needed. At the bottom, you will find a template in RST to make this process easier.

2. Edit the title according to the topic you are working on. Adding the how-to is unnecessary, but the matter should be clear from this point on.

3. Edit the description with relevant information to introduce the reader to the topic and the problem you will teach them how to solve.

4. Start creating the step-by-step the reader should follow to solve the problem. Please don't ignore any step, even if it is evident. 

5. Add the images and audiovisual resources you think could be necessary to clarify the process. Remember that  the callouts should be in Open edX red ``(#d23228)`` and round-edged rectangles. Also, save images as .png  or .jpg files for upload. For example:

.. image:: /_images/documentors_howto/image_example.png
	:width: 500px
	:align: center
	:alt: This image example shows how to access the GitHub repository from the Open edX documentation repository.

6. If the solution requires code, add the reference the person should use. For example, the following case is an HTML code.

.. code-block:: HTML

  <h1 class="title">Title</h1>

.. seealso:: To learn more about how to add a code block, visit the `Code blocks documentation <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/#code-blocks>`_.

7. Add any reference that could be important for someone to understand the topic. For example, here is additional information about `how to style for Read the Docs <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/>`_.

Now, you have a how-to document. Congratulations! 

.. END HERE

.. note:: To upload your document to RTD, you can review the `Documentors Quickstarts <https://docs.openedx.org/en/latest/documentors/quickstarts/index.html#>`_.

..  see also:: Review the Style Guide to learn more about directives and other resources to create your documentation.

RST Template
************

.. code-block:: RST

	How-To Document Template
	########################

	A How-To guide document guides the reader through the steps to solve a real-world problem. This documentation is goal-oriented and similar to recipes, with directions that guide the reader through the steps to achieve a specific end.

	For example, following the steps in this How-To guide, you can create a how-to document for any repository for the Open edX platform.

	1. Copy this document into a new file to edit as needed. At the bottom, you will find a template in RST to make this process easier.

	2. Edit the title according to the topic you are working on. Adding the how-to is unnecessary, but the matter should be clear from this point on.

	3. Edit the description with relevant information to introduce the reader to the topic and the problem you will teach them how to solve.

	4. Start creating the step-by-step the reader should follow to solve the problem. Please don't ignore any step, even if it is evident. 

	5. Add the images and audiovisual resources you think could be necessary to clarify the process. Remember that  the callouts should be in Open edX red ``(#d23228)`` and round-edged rectangles. Also, save images as .png  or .jpg files for upload. For example:

	.. image:: /_image/documentors_howto/image_example.png
		:width: 500px
		:align: center
		:alt: This image example shows how to access the GitHub repository from the Open edX documentation repository.

	6. If the solution requires code, add the reference the person should use. For example, the following case is an HTML code.

	.. code-block:: HTML

  		<h1 class="title">Title</h1>


	.. seealso:: To learn more about how to add a code block, visit the `Code blocks documentation <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/#code-blocks>`_.

	7. Add any reference that could be important for someone to understand the topic. For example, here is additional information about `how to style for Read the Docs <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/>`_.

	Now, you have a how-to document. Congratulations! 

	.. note:: To upload your document to RTD, you can review the `Documentors Quickstarts <https://docs.openedx.org/en/latest/documentors/quickstarts/index.html#>`_.

	..  see also:: Review the Open edX Documentation Writing Style Guide to learn more about directives and other resources for creating your documentation.
		
.. seealso::

   :ref:`About Open edX Documentation Standards` (concept)

   :ref:`Concept Document Template` (reference)

   :ref:`Reference Document Template` (reference)

   :ref:`Quickstart Document Template` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
