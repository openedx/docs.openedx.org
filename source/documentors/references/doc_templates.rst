Documentation Templates
#########################

This page contains templates that you can copy directly and use to develop new topics.

To copy RST code examples from this topic, just hover over the codeblock to see the copy button, and copy the RST as needed.

.. contents:: Contents
  :local:
  :depth: 1



Topic Titles
***************

Open edX Documentation uses hierarchical titles, indicated by the special characters underneath each title.

Copy the following titles as needed.

.. include:: ../references/rst_samples/headings.txt

.. note::
 :class: dropdown

 It is a rule of RST that the line of underline characters must be as long as or longer than the title; if the line is shorter than the title, the documentation will not build.

Content Links at the top of a Topic
*************************************

If you have a long topic with meaning Heading 2s, you can use the **contents** directive at the top of the topic to provide links to the different sections (as shown at the top of this topic).


Copy the contents directive as needed.

.. code-block:: RST

	Topic Title
	###########

	An introductory sentence for the topic, followed by the contents directive, which will create the links to subsections.

	.. contents:: Contents
	  :local:
	  :depth: 1

	First Heading 2
	****************


Develop Sections
**********************

You can nest sections in the topic as needed, to give it structure and break it up into discrete parts.

Copy the Topic and Section Structure as needed

.. code-block:: RST

	Topic Title
	###########

	Introduce the topic

	If this is a long topic with multiple sections, use the **contents** directive below:

	.. contents:: Contents
	:local:

	Section 1
	**********

	Introduce Section One

	Subsection 1
	+++++++++++++

	Content for Section 1/Subsection 1

	Subsection 2
	+++++++++++++

	Content for Section 1/Subsection 2

	Section 2
	**********

	Introduce Section Two

	Subsection 1
	+++++++++++++

	Content for Section 2/Subsection 1

	Subsection 2
	+++++++++++++

	Content for Section 2/Subsection 2

Create a How-to
*****************

Copy this codeblock to start a new how-to topic.

.. code-block:: RST

   How-to Title
   ############

   .. Titles should be imperative. https://www.grammarly.com/blog/imperative-sentences/

   .. How-tos should have a short introduction sentence that captures the user's goal and introduces the steps.

   This how-to will help you accomplish task X.

   Assumptions
   ***********

   .. This section should contain a bulleted list of assumptions you have of the
      person who is following the How-to.  The assumptions may link to other
      how-tos if possible.

   * You know how to use Git

   * You know how to create an empty course.

   Steps
   *****

   .. A task should have 3 - 7 steps.  Tasks with more should be broken down into digestible chunks.

   #. Step 1.

   #. Step 2.

   #. Step 3.

   .. Following the steps, you should add the result and any follow-up tasks needed.

   .. seealso::

     :ref:`title to link to`


Add an Ordered List
*********************

Copy this codeblock to start an ordered (numbered) list.

.. include:: ../references/rst_samples/ordered_lists.txt

Add an Unordered List
*********************

Copy this codeblock to start an unordered (bulleted) list.

.. include:: ../references/rst_samples/ordered_lists.txt

Nested Lists
*************

You can nest arbitrarily, using the **#** symbol for ordered lists and **\*** for unordered lists.


.. include:: ../references/rst_samples/nested_lists.txt


Create a Reference
*******************

Copy this codeblock to start a new reference topic.

.. code-block:: RST

	Reference Title
	###############

	The reference title should just name the object or subject. Such as *Course Section* or *Course Dates*.

	Provide a high-level overview of topic.

	What is it?
	************

	Provide a high-level view of what you are documenting - what it is and why one would care.

	Complex topics may contain 2 or more subsections.

	What is <part of subject> ?
	++++++++++++++++++++++++++++++

	When you need to break down a subject, you can break it down into subsections (H3s). Typically you would have 0 H3s, or 2+ H3s.

	What is <part of subject> ?
	+++++++++++++++++++++++++++++++

	When you need to break down a subject, you can break it down into subsections (H3s)

	Aspects of the Subject
	***************************

	Create sections for different aspects of the subject; for example, for problem types, you would have a section on all the settings and a section on the XML representation of the problem.

Add a Substitution
********************

In RST, a *substitution* serves as a variable which you can set a value for once, then use repeatedly. This is useful for words or phrases that are used often, as it enables you to edit the value once and change it everywhere.

You also need to use substitutions for inline images, as explained below.

Substitutions are all kept in the source/substitutions.txt file in the documenation project on GitHub.

Copy the format for the substitution as needed.

.. code-block:: RST

  .. |variable name| replace:: value

  .. |Platform name| replace:: Open edX

You then add the *variable name* inline in the topic.

.. code-block:: RST

  A line of text with an |variable name| inserted.


Add a Sidebar
**************

You can add any content in a sidebar. Open edX uses sidebars for image thumbnails, videos, and other notes.

The sidebar must come directly after a heading.

Copy this codeblock to add a new sidebar topic.

.. code-block:: RST

  .. sidebar:: Sample Sidebar

    Any content, typically an image, video, or note.

Add an Image to a Topic
************************

You can add an on its own separate line, inline, or in a sidebar.

You can also add an image directly, or add a thumbnail of an larger image, which when clicked on will open the full image.

You must save images in the ``source/_images`` directory before adding a reference to it in a topic.

Add an Image on its Own Line
=============================

Copy this codeblock to an iamge on its own line.

.. code-block:: RST

  Line of content, followed by a line with an image.

  .. image:: /_images/image-file-name

  Or, a line of content, followed by a clickable thumbnail of a large image.

  .. thumbnail:: /_images/image-file-name

Add an Image Inline
====================

To add an image inline, you must first create a substitution for the image in the subsitutions.txt file.

Copy the format for the substitution as needed.

.. code-block:: RST

  .. |variable name| image:: /_images/image-file-name

You then add the *variable name* inline in the topic.

.. code-block:: RST

  A line of text with an |variable name| inserted.

Add an Thumbnail in a Sidebar
==============================

You can add a thumbnail in a sidebar, a common practice for How-to topics.

The sidebar must come directly after a heading.

Copy this codeblock to add a new sidebar with a thumbnail.

.. code-block:: RST

  .. sidebar:: Sample Sidebar with a thumbnail

    .. thumbnail:: _images/image-file-name

Use Inline Formatting
************************

RST supports **bold**, *italic*, and ``mono-spaced`` characters. You can also make GUI elements appear as :guilabel:`objects`.

Copy this codeblock for inline formatting as needed.

.. include:: ../references/rst_samples/inline.txt

