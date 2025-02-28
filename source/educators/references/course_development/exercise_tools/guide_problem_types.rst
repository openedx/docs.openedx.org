.. _Core Problem Types:

Guide to Problem Types
######################

.. tags:: educator, reference

The problem types that you can include in any course, without taking any
other steps to identify or enable additional exercises or tools, are the core
problem types. When you add a problem component in Studio, the core problem
types are classified as either **Simple Problem Types** or **Advanced**.

.. contents::
  :local:
  :depth: 2


Simple Problem Types
*********************

When you create a problem in Studio, the editor opens with options for the
following problem types. When you select any of the simple problem types, the
:ref:`simple editor<Simple Editor>` opens.

.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Problem Type
     - Description
     - Support
   * - :ref:`Single Select`
     - In single select problems, learners select one answer from a set of
       possible answers, which are visible directly below the question.
     - Full support; mobile-ready
   * - :ref:`Multi select`
     - In multi-select problems, learners select one or more options from a list of
       possible answers. To answer the problem correctly, a learner must select
       all of the options that are correct answers, and none of the options
       that are incorrect.
     - Full support; mobile-ready
   * - :ref:`Dropdown`
     - In dropdown problems, learners choose one answer from a set of possible
       answers, which are presented in a dropdown list after the learner
       selects the dropdown arrow.
     - Full support; mobile-ready
   * - :ref:`Numerical Input`
     - In numerical input problems, learners enter numbers or specific and
       relatively simple mathematical expressions to answer a question. These
       problems allow only integers and a few select constants. You can specify
       a margin of error, and you can specify a correct answer either
       explicitly or by using a Python script.
     - Full support; mobile-ready
   * - :ref:`Text Input`
     - In text input problems, learners enter text into a response field. The
       response can include numbers, letters, and special characters such as
       punctuation marks.
     - Full support; mobile-ready

By adding hints, feedback, or both, you can give learners guidance and help
when they work on a problem. When you choose one of the simple problem types,
the editor interface provides additional guidance and text fields for entering
these options. All of these problem types also have full support and are
mobile-ready.


Advanced Problem Types
***********************

If none of the simple problem types fit what you need, the editor's problem type
select page has an option for **Advanced problem types**. Selecting this option
will bring you to a list of advanced problems. When you select any of the
advanced problem types, the :ref:`advanced editor<Advanced Editor>` opens.

* If you choose the **Blank Advanced Problem** option, the editor opens without
  providing a template or example for you to follow. You can begin to add OLX
  markup and the text for required and optional problem elements immediately.

* If you choose one of the following problem types, a template appears in the
  editor with guidance for adding all of that problem type's required elements,
  as well as several optional elements.

.. note:: Some advanced problem types are **unsupported**
   and are not available in the list of problem types unless you
   enable a setting in Studio. For more information, see :ref:`Unsupported
   Advanced Problem Types` and :ref:`Add Unsupported Exercises Problems`.


.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support

   * - :ref:`Custom JavaScript Display and Grading<Guide to Custom JavaScript Display and Grading Problem>`
     - Custom JavaScript display and grading problems (also called custom
       JavaScript problems or JS input problems) allow you to create a custom
       problem or tool that uses JavaScript and then add the problem or tool
       directly into Studio.
     - Full support
   * - :ref:`Custom Python-evaluated Input <About Custom Python-Evaluated Input Problem>`
     - In custom Python-evaluated input (also called "write-your-own-grader")
       problems, the grader uses a Python script that you create and embed in
       the problem to evaluate a learner's response or provide hints. These
       problems can be any type.
     - Provisional support
   * - :ref:`Math Expression Input`
     - Learners enter mathematical expressions to answer a question. These
       problems can include unknown variables and more complex symbolic
       expressions. You can specify a correct answer either explicitly or by
       using a Python script.
     - Full support; mobile-ready

.. _Unsupported Advanced Problem Types:


Unsupported Advanced Problem Types
===================================

The following advanced problem types are **not supported**
by the Open edX Platform. You can enable an option to make unsupported problem types
available in Studio. For more information, see
:ref:`Add Unsupported Exercises Problems`.

.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support
   * - :ref:`Circuit Schematic Builder`
     - Learners arrange circuit elements such as voltage sources, capacitors,
       resistors, and MOSFETs on an interactive grid. They then submit a DC,
       AC, or transient analysis of their circuits to the system for grading.
     - Not supported
   * - :ref:`Image Mapped Input`
     - Learners answer prompts by selecting a defined area in an image. You
       define the area by including coordinates in the body of the problem.
     - Not supported
   * - :ref:`Problem with Adaptive Hint`
     - A problem with an adaptive hint evaluates a learner's response, then
       gives the learner feedback or a hint based on that response so that the
       learner is more likely to answer correctly on the next attempt. These
       problems can be text input or single select problems.
     - Not supported

******************************
Additional Exercises and Tools
******************************

This table lists the fully or provisionally supported additional exercises and
tools that you can add to your course.

.. note:: Some additional exercises and tools are **not supported**
   by the Open edX Platform. You can enable an option to make unsupported exercises
   and tools available in Studio. For more information, see :ref:`Unsupported
   Additional Exercises and Tools` and
   :ref:`Add Unsupported Exercises Problems`.

.. to come: revise to eliminate entries with no support. Add pointer (at least for Open edX) to all of the XBlocks that are available.


.. note:: In addition to the following exercises and tools, the Open edX platform offers
   the :ref:`Notes tool<Notes Tool>`. The Notes tool allows learners to
   highlight and make notes about what they read in the course. T

.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support

   * - :ref:`Calculator`
     - Learners can enter input that includes Greek letters, trigonometric
       functions, and scientific or ``e`` notation in addition to common
       operators. The calculator tool is available for every course through the
       course advanced settings. When the calculator tool is enabled, it
       appears on every unit page.
     - Provisional support
   * - :ref:`Conditional Module`
     - You can create a conditional module to control versions of content that
       groups of learners see. For example, learners who answer "Yes" to a poll
       question then see a different block of text from the learners who answer
       "No" to that question.
     - Provisional support
   * - :ref:`Drag and Drop Problem<About the Drag and Drop Problem>`
     - Learners respond to a question by dragging text or objects to a specific
       location on an image.
     - Full support; mobile-ready
   * - :ref:`Guide to the Drag and Drop Problem`
     - Learners respond to a question by dragging text or objects to a specific
       location on an image. This version of the drag and drop problem type is
       deprecated and should not be added to a course. For more information
       about the fully supported drag and drop problem type, see
       :ref:`About the Drag and Drop Problem`.
     - Not supported
   * - :ref:`External Grader`
     - An external grader is a service that receives learner responses to a
       problem, processes those responses, and returns feedback and a problem
       grade to the Open edX platform. You build and deploy an external grader
       separately from the Open edX platform. An external grader is particularly
       useful for software programming courses where learners are asked to
       submit complex code.
     - Provisional support
   * - :ref:`Google Calendar Tool`
     - Learners see a Google calendar embedded in your course. You can use a
       Google calendar to share quiz dates, office hours, or other schedules of
       interest to learners.
     - Provisional support
   * - :ref:`Google Drive Files Tool`
     - Learners see a Google Drive file, such as a document, spreadsheet, or
       image, embedded in your course.
     - Provisional support
   * - :ref:`IFrame`
     - With the iframe tool, you can integrate ungraded exercises and tools
       from any Internet site into a Text component in your course.
     - Provisional support
   * - :ref:`LTI Component`
     - LTI components allow you to add an external learning application or non-
       PDF textbook to Studio.
     - Full support
   * - :ref:`Open Response Assessments`
     - Learners receive feedback on responses that they submit and give
       feedback to other course participants. Open response assessments include
       self assessment, peer assessment, and optionally, staff assessment.
     - Full support
   * - :ref:`Oppia Exploration Tool`
     - You can embed Oppia explorations in your course so that learners can
       interact with them directly in the course body.
     - Provisional support
   * - :ref:`UBC Peer Instruction`
     - This type of exercise offers the experience of the Peer Instruction
       learning system within your online course.
     - Full support
   * - :ref:`Poll Tool`
     - You can include polls in your course to gather learners' opinions on
       various questions. You can use the Poll Tool in Studio.
     - Full support
   * - :ref:`Survey Tool <Manage Survey Tool>`
     - You can include surveys in your course to collect learner responses to
       multiple questions.
     - Full support
   * - :ref:`Word Cloud <Manage Word Cloud Tool>`
     - Word clouds arrange text that learners enter in response to a question
       into a colorful graphic.
     - Provisional support



.. _Unsupported Additional Exercises and Tools:

==========================================
Unsupported Additional Exercises and Tools
==========================================

The following additional exercises and tools are **not supported** by the Open edX Platform. You can enable an option to make unsupported exercises and
tools available in Studio. For more information, see
:ref:`Add Unsupported Exercises Problems`.


.. list-table::
   :widths: 25 60 20
   :header-rows: 1

   * - Type
     - Description
     - Support
   * - :ref:`Annotation`
     - Learners respond to questions about a specific block of text. The
       question appears above the text so that learners can think about the
       question as they read.
     - Not supported
   * - :ref:`Chemical Equation`
     - Learners enter a value that represents a chemical equation into a text
       box. The grader uses Python script that you create and embed in the
       problem to evaluate learner responses.
     - Not supported
   * - :ref:`Completion Tool<About the Completion Tool>`
     - Learners mark sections of course content as completed. This tool helps
       learners track their progress through sections of the course (including
       ungraded activities such as reading text, watching videos, or
       participating in course discussions), and gives them a way to indicate
       to both themselves and course staff that they completed an activity.
     - Not supported
   * - :ref:`Full Screen Image<Manage the Full Screen Image Tool>`
     - Learners can enlarge an image in the entire browser window. This tool is
       useful for detailed images that are easier to view when enlarged.
     - Not supported
   * - :ref:`Gene Explorer`
     - The gene explorer (GeneX) simulates the transcription, splicing,
       processing, and translation of a small hypothetical eukaryotic gene.
       Learners make specific mutations in a gene sequence, and this tool
       calculates and displays the effects of the mutations on the mRNA and
       protein.
     - Not supported
   * - :ref:`Periodic Table`
     - An interactive periodic table of the elements that shows detailed
       information about each element when learners move the pointer over each
       element.
     - Not supported
   * - :ref:`Poll Tool via OLX <Guide to the Poll Tool via OLX>`
     - You can run polls in your course so that your learners can share
       opinions on different questions. You can only add this type of poll to a
       course by using OLX (open learning XML). Support for this tool in Studio
       is not available. For more information, see the :ref:`Set Up Group Configuration for OLX Courses`.
     - Not supported
   * - :ref:`Problem Written in LaTeX`
     - If you have a problem that is already written in LaTeX, you can use this
       problem type to convert your code into XML.
     - Not supported
   * - :ref:`Protein Builder`
     - Learners create specified protein shapes by stringing together amino
       acids.
     - Not supported
   * - :ref:`RecommenderXBlock`
     - RecommenderXBlock can hold a list of resources for misconception
       remediation, additional reading, and so on. This tool allows the course
       team and learners to work together to maintain the list of resources.
       For example, team members and learners can suggest new resources, vote
       for useful ones, or flag abuse and spam.
     - Not supported
   * - :ref:`Single Select and Numerical Input`
     - Learners not only choose one answer from a set of possible options, they
       are also prompted to provide more specific information, if necessary.
     - Not supported
   * - :ref:`Zooming Image`
     - Learners can view sections of an image in detail. You specify the
       sections in an image that can be enlarged.
     - Not supported

.. _Mobile Ready Problem Types:

**************************
Mobile-Ready Problem Types
**************************

Learners can read and submit answers for the following types of problems while
they use the Open edX mobile app.

* :ref:`Drag and Drop Problem<About the Drag and Drop Problem>`
* :ref:`Dropdown`
* :ref:`Math Expression Input`
* :ref:`Multi select`
* :ref:`Numerical Input`
* :ref:`Single Select`
* :ref:`Text Input`

Questions that have other problem types do not appear in the Open edX mobile app.
Instead, a message appears with a link to open the applicable problem component
in a web browser.


.. seealso::

  :ref:`About Problems Exercises and Tools` (concept)

  :ref:`Working with Problem Components` (reference)

  :ref:`Guide to Problem Settings` (reference)

  :ref:`Gradebook Assignment Types` (reference)

  :ref:`Feedback Best Practices` (concept)

  :ref:`Adding Feedback and Hints to a Problem` (reference)

  :ref:`Configure Hint` (how-to)

  :ref:`Partial Credit` (reference)

  :ref:`Set the Assignment Type and Due Date for a Subsection` (how-to)

  :ref:`Adding Tooltips` (reference)

  :ref:`Learner View of Problems` (reference)

  :ref:`Advanced Editor` (reference)

  :ref:`Add Hints via the Advanced Editor` (how-to)

  :ref:`Modifying a Released Problem` (reference)

  :ref:`Add Unsupported Exercises Problems` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
