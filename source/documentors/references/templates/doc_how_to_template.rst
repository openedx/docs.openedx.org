.. _How To:

How-To Document Template
########################

A How-To guide document guides the reader through the steps to solve a real-world problem. This documentation is goal-oriented and similar to recipes, with directions that guide the reader through the steps to achieve a specific end.

For example, following the steps in this How-To guide, you can create a how-to document for any repository for the Open edX platform. (Description)

#. Copy this document in a new file to edit it as needed. At the bottom, you will find a template in RST to make this process easier.

#. Edit the title according to the topic you are working on. Adding the how-to is unnecessary, but the matter should be clear from this point on.

#. Edit the description with relevant information to introduce the reader to the topic and the problem you will teach them how to solve.

#. Start creating the step-by-step the reader should follow to solve the problem. Please do not omit any step, even if it is evident. 

#. Add the images and audiovisual resources you think could be necessary to clarify the process.
To do it, follow these parameters: 

	- Callouts are ``red (#d23228)`` round-edged rectangles. 3pt edges
	- Save images as .png  or .jpg files for upload.

	For example:

	.. image:: ../../_image/documentors_howto/image_example.png
	   :width: 500px
	   :align: center
	   :alt: This image example shows how to access the GitHub repository from the Open edX documentation repository.



#. If the solution requires code, add the reference the person should use. For example, the following case is an HTML code.

.. code-block:: HTML
	:linenos:

	<h1>HTMLcode block example</h1>

.. seealso:: To learn more about how to add a code, visit the `Code blocks documentation <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/#code-blocks>`_.

#. Add any reference that could be important for someone to understand the topic. For example, here is additional information about `how to style for Read the Docs <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/>`_

Now, you have a how-to document. ¡Congratulations! 

.. note:: To upload your document to RTD, you can review the `Documentors Quickstarts <https://docs.openedx.org/en/latest/documentors/quickstarts/index.html#>`_.

RST Template
************

.. code-block:: RST

		A How-To guide document guides the reader through the steps to solve a real-world problem. This documentation is goal-oriented and similar to recipes, with directions that guide the reader through the steps to achieve a specific end.

		For example, following the steps in this How-To guide, you can create a how-to document for any repository for the Open edX platform. (Description)

		#. Copy this document in a new file to edit it as needed. At the bottom, you will find a template in RST to make this process easier.

		#. Edit the title according to the topic you are working on. Adding the how-to is unnecessary, but the matter should be clear from this point on.

		#. Edit the description with relevant information to introduce the reader to the topic and the problem you will teach them how to solve.

		#. Start creating the step-by-step the reader should follow to solve the problem. Please do not omit any step, even if it is evident. 

		#. Add the images and audiovisual resources you think could be necessary to clarify the process. To do it, follow these parameters: 

			- Callouts are ``red (#d23228)`` round-edged rectangles. 3pt edges
			- Save images as .png  or .jpg files for upload.

			For example:

			.. image:: ../../../_image/documentors_howto/image_example.png
			   :width: 500px
			   :align: center
			   :alt: This image example shows how to access the GitHub repository from the Open edX documentation repository.



		#. If the solution requires code, add the reference the person should use. For example, the following case is an HTML code.

			.. code-block:: HTML
				:linenos:

				<h1>HTMLcode block example</h1>

		.. seealso:: To learn more about how to add a code, visit the `Code blocks documentation <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/#code-blocks>`_.

		#. Add any reference that could be important for someone to understand the topic. For example, here is additional information about `how to style for Read the Docs <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/>`_

		Now, you have a how-to document. ¡Congratulations! 

		.. note:: To upload your document to RTD, you can review the `Documentors Quickstarts <https://docs.openedx.org/en/latest/documentors/quickstarts/index.html#>`_.

