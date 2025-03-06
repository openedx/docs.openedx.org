.. _Open edX Diataxis Guide:

Open edX Diataxis Guide
#######################

.. tags:: documentor, concept

.. contents:: 
  :local:
  :depth: 1

Diataxis Definition
*******************

The `Diataxis framework <https://diataxis.fr/>`_ is an approach to quality in technical documentation and creates a systematic organization. Diataxis identifies four modes of documentation:

* `Quickstart`_
* `How-to`_
* `Reference`_
* `Concept`_

Using Diataxis, documentation can be organized to meet diverse user needs, making it easier to find relevant information based on the user’s situation or goal. This structure enhances usability and comprehension, allowing users to navigate documentation more effectively.

For each type of document, you will find the explanation, the technical guidelines, and a matrix of criteria that will allow you to identify whether or not a document complies with the parameters of the Diataxis used in the Open edX repositories. 

.. _Quickstart:

Quickstart
**********

A Quickstart is a lesson that guides the reader through **practical steps** to complete a stated goal. It is **learning-oriented**. In other words, it is a lesson and a learning experience. For example, creating a virtual course can be a Quickstart because it’s a practical skill. A Quickstart may comprise the contents of multiple How-To guides.

Although Quickstart topics may seem similar to How-Tos, they focus differently. Quickstarts are specifically built for beginners and are meant to help them gain experience with the product.

How to Write a Good Quickstart:
===============================
#. **Learning objectives.** Describe what the learner will accomplish.

	E.g., *“In this quickstart, you will…”* 

#. **Clear learning path.** Describe the topics, the order, and the activities your learner will follow to accomplish the learning objectives.

	E.g., *“To accomplish that, you will learn how to …” “You will create …”*

#. **Step-by-step process** explanation with just the necessary amount of explanation. Link to a more detailed explanation.

	E.g., *“Step 0: First, do x.”*
	E.g., *“Note: For more information about migration, click here.”*

#. **Output examples:** Give your learner clear expectations.

	E.g., *“The output should look like this: (add image).”*

#. **Accomplishment description:**

	E.g., *“You have successfully created your first course.”*

Technical Guidelines:
=====================
By following these recommendations, you will be able to write a good-quality Quickstart:

- Add the Quickstart to the title to guide the reader.
- Teach by doing.
- Use a friendly and professional tone.
- The learning objective should be apparent from the beginning. Setting expectations from the start allows the learners to see themselves building towards the completed goal as they work.
- Do not omit the “obvious.” Your learners follow the quickstart because they do not know about that topic or product.
- Every step the learner follows should produce an understandable result, however small.
- Your Quickstart should work for all users every time. This means you must consider different types of devices and software and test your Quickstart once a year to ensure it is updated.
- Be specific about actions and outcomes.
- Explain what’s necessary and nothing more. Your guidance must remain focused on achieving the stated learning objective. 

Criteria of a Good Quickstart:
==============================
.. list-table::
   :widths: 15 40 40
   :header-rows: 1

   * - 
     - **Criteria**
     - 

   * - 
     - **Objectives: Learning Oriented**
     - **Technical guidelines: Practical steps**

   * - **Perfect**
     - - The learning objective of the quickstart is evident from the beginning and is coherent throughout the whole document.
       - As a learner, you achieve the learning goals of the Quickstart.
       - The document has a clear learning path.
     - - The precise activities, explanations, and steps guide the learner toward the quickstart's objective.
       - The document is easy for the learner to follow.

   * - **Very accurate**
     - Document shares features of Perfect and Acceptable.
     - 

   * - **Acceptable**
     - - The learning objective must be clarified from the Quickstart beginning, but the Quickstart is coherent.
       - As a learner, you complete most of the learning goals of the Quickstart.
       - The learning path in the document is confusing at some point.
     - - The activities, explanations, and steps guide the learner to achieve most of the quickstart's objectives but have one or two details that may confuse them.
       - The document can confuse the learner at specific points.

   * - **Needs corrections**
     - Document shares features of Acceptable and Not acceptable.
     - 

   * - **Not acceptable**
     - - It's unclear what the quickstart's learning objective and purpose are.
       - As a learner, you can't achieve the learning goals of the Quickstart.
       - The learning path is not clear.
     - - The activities, explanations, and steps fail to guide the learner in accomplishing the quickstart's objective.
       - The document is not easy to follow and can confuse the learner.

 
.. _How To:

How-To
******

How-to guides take the reader through the **steps to solve a real-world problem**. This documentation is **goal-oriented** and similar to recipes, with directions that guide the reader through the steps to **achieve a specific end**. For example, “how to import a course” is a problem with a particular resolution.

What Is the Difference between a How-to and a Quickstart?
=========================================================
The main difference between a Quickstart and a How-To is that a How-To focuses on completing one specific task, while a Quickstart guides you through a series of tasks to achieve a larger goal. Essentially, a Quickstart consists of two or more How-Tos that work together towards a broader concept. However, Quickstart seeks to be as straightforward as possible in its teaching processes since it is often designed to guide beginners through complex processes. In the case of a How-to, you can include more details and options for performing a specific task because it is focused content and can cover broader levels of expertise.

A How-to Guide Must Have:
=========================

#. **Problem description:** Describe clearly the problem or task and show the user how to solve it.

	E.g., *“This guide shows you how to…”*

#. **Step-by-step process:** Indicates the order of the steps to make the process compelling.

	E.g., *“Step 1; Step 2” or “ 1. , 2.”*

#. **Visual supports:** Accompany the steps with images, videos, or graphics to guide the person following the process.

#. **Reference links:** 

	E.g., *“To learn more about x, visit our documentation”*

Technical Guidelines:
=====================
By following these recommendations, you will be able to write good quality how-to guides:

- Describe a sequence of actions. A how-to guide contains a sequence of actions that have an order.
- Solve a particular task. The problem or task is the concern of a how-to guide: stick to that practical goal.
- Do not explain concepts—link to other documents for further explanation.
- Omit the unnecessary. Practical usability is more helpful than completeness.
- Pay attention to naming. Choose action-based titles that say precisely what the how-to guide shows, such as “Import A Course” or “Copy And Paste Course Content.”

Criteria of the How-To Guide:
=============================

.. list-table::
   :widths: 15 40 40
   :header-rows: 1

   * - 
     - **Criteria**
     - 

   * - 
     - **Objective: Task-Oriented**  
       - Serves to work
     - **Technical guidelines: Practical steps**

   * - **Perfect**
     - - The guide is goal-oriented and helps to resolve a specific problem.
       - The title says clearly what the how-to guide is about.
     - - The sequence of steps is clear and easy to follow.
       - The document has the necessary visual accompaniments and follows the appropriate parameters.
       - The document is easy for the reader to follow.

   * - **Very accurate**
     - Document shares features of Perfect and Acceptable.
     - 

   * - **Acceptable**
     - - The guide structure is broad but helps to resolve a specific problem.
       - The title could be more explicit or related to the guide's topic.
     - - Two or three (2-3) of the steps in the sequence need to be clarified or made easier to follow.
       - The document is missing one or two (1-2) necessary visual accompaniments, or they need to follow the appropriate parameters.
       - The document can confuse the reader at specific points.

   * - **Needs corrections**
     - Document shares features of Acceptable and Not Acceptable.
     - 

   * - **Not acceptable**
     - - The guide doesn't help resolve the task.
       - The guide covers two or more discrete goals.
       - The document's structure could be more organized and easier to follow.
       - The title needs to be more specific or is unrelated to the guide's topic.
     - - The step sequence is unclear and difficult to follow.
       - It doesn't have visual accompaniments.
       - The document is not easy to follow and needs to be clarified for the reader.


.. _Reference:

Reference
*********

Reference material is **information-oriented**. It can easily relate to **technical descriptions and factual information** about the system, APIs, parameters, etc. For example, “The Open edX Problem Types” or “The Open edX User Roles” would be good reference guides, as they are used by someone already familiar with the product and need to look up all the options it provides. 

Reference material is like a map and details a function or feature of the Open edX platform. A map tells you what you need to know about the territory without having to go out and check it for yourself; a reference guide serves the same purpose for the product and its internal machinery.
For example, many details about course subsections, such as the different publication states, grading configuration, and visibility, are not included in the how-to topic Create a Subsection but are fully described in the reference topic Course Subsections. These two topics are linked in the See Also sections.

Reference Material Must Have:
=============================

#. **An accurate and precise description** of the product you’re referencing.

#. **Provide examples of the uses and functions** of the product to make it more comprehensive.

#. Generally, a reference **lists details or provides a glossary** of aspects of the product that the reader needs. (For example: definitions, commands, options, operations, features, flags, limitations, error messages, etc.)

#. Provide **warnings** where appropriate.

Technical Guidelines:
=====================
By following these recommendations, you will be able to write a good quality reference material:

- Do nothing but describe. References have one job: **to explain** and do that **accurately and comprehensively**.
- **Be accurate.** These descriptions must be accurate and kept up-to-date.
- **Provide examples.** It is a valuable way of providing illustrations that help readers understand the references without becoming distracted from the job of describing them.
- **The documentation structure should mirror the product's structure** so the user can work their way through it simultaneously. It doesn’t mean forcing the documentation into an unnatural structure. What’s important is that the documentation should help make sense of the product.
- **Be consistent** in structure, language, terminology, and tone.

Criteria of a Reference Document:
=================================

.. list-table::
   :widths: 15 40 40
   :header-rows: 1

   * - 
     - **Criteria**
     - 

   * - 
     - **Objective: Information Oriented**  
       - Serve to Work
     - **Technical guidelines: Theoretical Knowledge**

   * - **Perfect**
     - - The document describes the topic clearly, accurately, and comprehensively.
       - The document is structured according to the structure of the product itself.
     - - The document style is consistent, neutral, and objective.
       - The document descriptions are comprehensive.

   * - **Very accurate**
     - Document shares features of Perfect and Acceptable.
     - 

   * - **Acceptable**
     - - The document describes the content, but one (1) of the descriptions is unclear.
       - The document follows the product's structure but omits one or two (1-2) essential points.
     - - The document style can be more consistent, neutral, and objective.
       - The document has one or two elements that need to be clarified.

   * - **Needs corrections**
     - Document shares features of Acceptable and Not acceptable.
     - 

   * - **Not acceptable**
     - - Two (2) or more descriptions are not clear or accurate.
       - The document focuses on describing a task or concept; a reference doesn't have a specific objective. It only exists to describe.
     - - The document needs to describe the product consistently or objectively.
       - The document descriptions could be more precise.


.. _Concept:

Concept
*******

Concept documentation **clarifies and illuminates** a particular topic. It is **understanding-oriented**and could be considered a **conceptual guide**. Concept topics provide best practices or other Open edX platform guidelines. 

A Good Concept Must Have:
=========================

#. A **clear title** about the topic.

	E.g., *“About XBlocks and Their Uses in Course Creation” or “What are Learning Taxonomies?”*

#. An explanation that **answers a why question**. It could be descriptive, historical, or even propose different alternatives to explain the bigger picture and give context.

	E.g., *“What is an XBlock? The Open edX platform provides different components, called XBlocks, that can work to create a course, like text, video, assessment, and discussions.”*

Technical Guidelines:
=====================
By following these recommendations, you will be able to write a good quality concept guide:

- **Make connections to other things**, even to things outside the immediate topic, if that helps to clarify the subject you are explaining.
- Provide **background and context** in your explanation: explain why things are so.
- **Concept guides are about a topic.** You should be able to place an implicit (or even explicit) *"About"* before each title—for example, “(About) Instructional Design.” Also, concept document names should use nouns or noun phrases that indicate theoretical or conceptual topics.

Criteria of a Concept Document:
===============================

.. list-table::
   :widths: 15 40 40
   :header-rows: 1

   * - 
     - **Criteria**
     - 

   * - 
     - **Understanding oriented**
     - **Theoretical Knowledge**

   * - **Perfect**
     - - The document explains and clarifies the subject.
       - The document’s title is indicative of the subject of the concept.
     - - The document style is consistent, neutral, and objective.
       - The document is clear and precise about the topic.

   * - **Very accurate**
     - Document shares features of Perfect and Acceptable.
     - 

   * - **Acceptable**
     - - The document manages to explain part of the topic and shed light on it, although it omits particular contents that could better contextualize the reader.
       - The title is related to the topic of the concept but could be more explicit.
     - - The document style can be more consistent, neutral, and objective.
       - Certain text parts need to be clarified.

   * - **Needs corrections**
     - Document shares features of Acceptable and Not acceptable.
     - 

   * - **Not acceptable**
     - - The document needs to explain the topic and ensure the reader understands.
       - The guide doesn’t connect the concept with how it relates to the Open edX product.
       - The document's title does not reflect the subject of the concept.
     - - The document needs to describe the product consistently or objectively.
       - The document's topic needs to be clarified.


.. Note:: To learn more about the Diataxis framework, visit `the Diataxis homepage <https://diataxis.fr/>`_. The Open edX community adapted the framework according to the platform's needs.

