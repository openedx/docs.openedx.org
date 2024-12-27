.. _Working with Problem Components:

################################
Working with Problem Components
################################

.. tags:: educator, reference

This section introduces the core set of problem types that course teams can add
to any course by using the problem component. It also describes editing options
and settings for problem components.

.. contents::
 :local:
 :depth: 1

For information about specific problem types, and the other exercises and tools
that you can add to your course, see :ref:`Create Exercises`.

.. _Adding a Problem:

****************
Adding a Problem
****************

To add interactive problems to a course in Studio, in the course outline, at
the :ref:`unit<The Unit Workflow>` level, you select **Problem**. You then
choose the type of problem that you want to build on the Problem Type Selection
page.

The simple problem types include relatively straightforward CAPA problems such
as single select and text or numeric input. The advanced problem types can be
more complex to set up, such as math expression input, open response
assessment, or custom JavaScript problems.

=====================================
Adding Graded or Ungraded Problems
=====================================

When you :ref:`establish the grading policy<Set the Grade Range>` for your course,
you define the assignment types that count toward learners' grades: for
example, homework, labs, midterm, final, and participation. You specify
one of these assignment types for each of the subsections in your course.

As you develop your course, you can add problem components to a unit in any
subsection. The problem components that you add automatically inherit the
assignment type that is defined at the subsection level. For example, all of
the problem components that you add to a unit in the midterm
subsection are graded.

For more information, see :ref:`Set the Assignment Type and Due Date for a
Subsection`.

.. _Problem Studio View:

*****************************
Editing a Problem in Studio
*****************************

When you select **Problem**, Studio adds a blank problem to the unit and brings
you to the problem editor. From here, you can select 1 of 5 **simple problem
types** or select Advanced problem types for a list of **advanced problem types**.

* For simple problem types, the :ref:`simple editor<Simple Editor>` opens. In
  this editor, you can quickly create problems with question and answer formats.
  Options for scoring, hints, feedback, and more can be entered.

* For advanced problem types, the :ref:`advanced editor<Advanced Editor>` opens.
  In this editor, you use `EdX Open Learning XML Guide`_.
  elements and attributes to identify the elements of the problem. Options for scoring,
  feedback and more can be entered.

* For open response assessment problem types, you define the problem elements and
  options by using a graphical user interface. For more information, see
  :ref:`PA Create an ORA Assignment`.

* For drag-and-drop problem types, you build an interactive assessment in a
  customized interface in which you define areas that learners can drag into target
  zones on a background image. For more information, see
  :ref:`Creating a Drag and Drop Problem`.

You can switch from the simple editor to the advanced editor at any time by
selecting the **Switch to advanced editor** from the simple editor's settings.

.. note::
 After you save a problem in the advanced editor with complex OLX, you may not
 be able to open it again in the simple editor.

.. _Simple Editor:

==================
The Simple Editor
==================

When you select one of the **simple problem types**, you will be directed to
the simple editor.

*  :ref:`Single Select<Single Select>`

*  :ref:`Multi-select<multi select>`

*  :ref:`Dropdown<Dropdown>`

*  :ref:`Numerical Input<Numerical Input>`

*  :ref:`Text Input<Text Input>`

.. _Question and Explanation Fields:

================================
Question and Explanation Fields
================================

The question and explanation fields (and other text fields as well) offer a
number of formatting tools to craft your problem.

.. image:: /_images/educator_references/problem_editor_question_box.png
 :alt: an image of the Problem Editor toolbar and a number associated with
  each icon in the toolbar.
 :width: 800

#. **Undo/Redo**: Undo or redo changes made to the text field.

#. **HTML Tags**: Applies HTML tags to the selected block of text.

#. **Label**: Applies a “Question” label to the selected text which is picked
   up by screen readers. Screen readers read all of the text that you supply
   for the problem, and then repeat the text that is identified by this label
   immediately before reading the answer choices for the problem. This label
   can be removed by selecting the block of text and clicking this button
   again.

#. **Formatting**: Applies various formatting to the selected text such as
   bold, italicize, underline, color, text alignment, bullet points and
   indentation.

#. **Add Image and Links**: Allows you to add images and links to your text
   field.

#. **Blockquote and Code**: Applies blockquote or code formatting to the
   selected text. This can be removed by selecting the text and clicking this
   button again.

#. **Various Inserts**: Insert tables, emoticons, special characters and page
   breaks using these buttons.

#. **Clear Formatting**: Clears all formatting applied to the selected text.

#. **Accessibility Checker**: allows you to check HTML in the editor for
   various accessibility problems.

#. **More**: Depending on page size, some of the toolbar may not show. Click
   this button to expand or shrink the toolbar.

The explanation field is almost identical to the question field, only missing
the Label button for marking questions.

.. _Answer Fields:

==============
Answer Fields
==============

Enter your answers below in this section. While what you see below is the
general layout of the answer fields, there are some minor differences between
problem types.

.. image:: /_images/educator_references/problem_editor_answer_box.png
 :alt: An example answer field in the simple editor.
 :width: 600

#. **Correct Answer**: The selected or checked answer(s) are the correct answers.
   Due to the nature of dropdowns only allowing a single selection, the dropdown
   problem type has radio buttons which allow you to select only one correct
   answer. As you cannot enter incorrect answers for numeric input problems,
   the numeric input problem type automatically comes with checked answers.
   The other problem types allow you to select any number of correct answers.

#. **Answer Feedback**: Opens up the feedback panel for an answer option. For
   more information, see the following **Adding Feedback** section.

#. **Delete Answer**: Removes the corresponding line of answer buttons and
   fields.

#. **Add Answer**: Adds a new line of answer buttons and fields.

.. _Adding Feedback:

================
Adding Feedback
================

You can add feedback that displays to learners after they submit an answer. See :ref:`best practices for feedback<Feedback Best Practices>`. 

For example, the following single select problem provides feedback in
response to the selected option when the learner selects **Submit**. In this
case, feedback is given for an incorrect answer.

.. image:: /_images/educator_references/multiple_choice_feedback.png
 :alt: Image of a single select problem with feedback.
 :width: 600

While editing a problem block, you can apply **Answer-specific feedback**
for all problem types. **Group feedback** can only be applied to
**multi-select** problems.

**Answer-specific feedback** can be added under each answer by pressing
the feedback icon to the right of the answer text. Feedback entered in
these fields are given when the learner selects that answer or when the
learner does not select that answer.

.. image:: /_images/educator_references/problem_editor_feedback_box.png
 :alt: Image of the answer-specific feedback settings.
 :width: 600

.. note::
   The “is not selected” feedback field shown above is only available
   for the **multi-select** problem type.

**Group Feedback** can be found on the collapsible settings to the right of
the problem editor. Feedback entered in this field will display if and
only if the learner selects all of the checked answers. Click the
**Add group feedback** button to add additional feedback for different
groups of checked answers. **Group feedback** can only be applied for
the **multi-select** problem type.

.. image:: /_images/educator_references/problem_editor_group_feedback_box.png
 :alt: Image of the group feedback settings.
 :width: 300

.. note::
   Feedback for incorrect answers in the **numerical input** problem type
   is not supported.


.. _Adding Mathematics:

===================
Adding Mathematics
===================

To add mathematics, you can use LaTeX, MathML, or AsciiMath notation. Studio
uses MathJax to render equations. For more information, see :ref:`MathJax in
Studio`.

============
Power Paste
============

Many course authoring teams rely on copying and pasting content from documents
such as Google Docs or Microsoft Word. Correct formatting in Studio and the LMS
can be most easily realized through Power Paste. To learn how to use Power
Paste, see :ref:`Paste without Formatting in a Text Component`.

.. seealso::
 :class: dropdown

 :ref:`Modifying a Released Problem` (reference)

 :ref:`Advanced Editor` (reference)

 :ref:`Problem Settings` (reference)

 :ref:`Feedback Best Practices` (concept)

 :ref:`Learner View of Problems` (reference)

 :ref:`Partial Credit` (reference)

 :ref:`Configure Hint` (how to)

