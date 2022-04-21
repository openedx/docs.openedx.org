Topic Template
======================

This topic is meant as a template that you can copy from GitHub and use to develop new topics.

You can also copy RST code examples from this topic as needed. Just hover over the codeblock to see the copy button, and copy the RST as needed.

Replace "Topic Template" above with the topic title.

If this is a long topic with multiple sections, use the **contents** directive below:

.. contents:: Contents
  :local:

Ensure you use **======================** under the complete topic title.

*Copy the Topic Intruction*

.. code-block:: RST
  
	Topic Template
	======================

	This topic is meant as a template that you can copy from GitHub and use to develop new topics.

	Replace "Topic Template" above with the topic title.

	If this is a long topic with multiple sections, use the **contents** directive below:

	.. contents:: Contents
	  :local:

	Ensure you use **======================** under the complete topic title.


Develop Sections
**********************

You can nest sections in the topic as needed, to give it structure and break it up into discrete parts.

* Use **\*\*\*\*\*** under the 2nd level section titles

* Use **+++++++++++++++** under the 3rd level section titles

*Copy the Topic and Section Structure*

.. code-block:: RST
  
	Topic Title
	======================

	Introduce the topic

	If this is a long topic with multiple sections, use the **contents** directive below:

	.. contents:: Contents
	  :local:

	Section One
	*************

	Introduce Section One

	Subsection One
	++++++++++++++++++

	Content fo Subsection One

	Subsection Two
	++++++++++++++++

	Content for Subsection Two

	Section Two
	*************

	Introduce Section Two

	Subsection One
    ++++++++++++++++++

	Content fo Subsection One

	Subsection Two
	+++++++++++++++++++

	Content for Subsection Two


Create a How-to
*****************

*Copy this codeblock to start a new how-to*

.. code-block:: RST

	How-to Title
	=============

	Titles should be imperative. How-tos should have a short introduction sentence that captures the user's goal and introduces the steps.

	A task should have 3 - 7 steps.  Tasks with more should be broken down into digestible chunks.

	#. Step 1.

	#. Step 2.

	#. Step 3.

	Following the steps, you should add the result and any follow-up tasks needed.

	.. seealso::

	  Add links to related references and tasks

Create a Reference
*******************

*Copy this codeblock to start a new reference*

.. code-block:: RST

	Reference Title
	=================

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


