.. _Palm Editor Improvements:

A New Problem Editor Experience (Palm)
######################################


In the latest Open edX release, Palm, the Problem Editor has been enhanced to
provide a smoother editing experience for Studio authors.

.. contents::
  :local:
  :depth: 2

What has changed?
*****************

In Studio, selecting :guilabel:`Problem` from the component selection widget:

   .. image:: /_images/release_notes/palm/ped1.png

brings you to a full page where you can select which problem type you can use:

   .. image:: /_images/release_notes/palm/ped2.png


The right side of the page visually shows an example of what the problem type
looks like, as well as a link to documentation.

Selecting a problem type brings you to a full-page editing screen, where you can
easily input the question, an explanation of the answer, the answer choices,
scores & attempts, and hints.

   .. image:: /_images/release_notes/palm/ped3.png


The problem renders in the LMS as usual:

   .. image:: /_images/release_notes/palm/ped4.png


For authors who prefer to customize problems using OLX, the new editing
experience retains this function by clicking on “Switch to Advanced Editor”
(nested under “Advanced Settings” on the right sidebar). It's worth noting that
once a problem has been converted to OLX via the Advanced Editor, it's not
possible to revert to the Visual Editor.

   .. image:: /_images/release_notes/palm/ped5.png


For a description of all the visual editor capabilities, plus more on raw OLX
editing, see the end of this article.

Author Impact
*************

Previously, the Problem Editor rendered in a small pop-up and required course
authors to understand a technical language called Markdown to define problems.
Changing the problem weight or maximum attempts required accessing a Settings
menu.

With a new, full-screen editing experience that provides a visual editor that
can be typed directly in without use of Markdown, course authors can focus on
what they do best: authoring courses. With the settings displayed right next to
the problem editor itself, authors do not need to switch between two screens to
update problem weight and other settings.

Advanced Problems Advanced Problems also take advantage of the new full-screen
editor. Selecting an advanced problem, such as Custom Javascript display and
grading, brings you to a full screen display where you can edit the component in
its raw form:

   .. image:: /_images/release_notes/palm/ped6.png


How can I get the new editor experience?
****************************************

The editor experience is available as of the Open edX Palm release. `Upgrading
your local installation to Palm
<https://docs.tutor.edly.io/install.html#upgrading>`_ will guarantee that your
system is up-to-date with the latest features, including this editor.

Once you've upgraded to Palm, you'll need a system administrator to perform the
following steps:

#. Enable the Course Authoring MFE feature flag
#. Add the ``new_core_editors.use_new_problem_editor`` waffleflag to the CMS
   Django Admin
#. Set the value of the waffleflag to “Yes” for everyone

Visual Editor Features: What's New
**********************************

Select Problem Type
===================

* On click of the “problem” button under the “Add New Component” section in
  Studio, the user is brought to a new page where they can select one of several
  problem types (select problem type page below).

  * Each problem type, when selected on the select problem type page, reveals a
    preview on the right hand side of the page.

* Advanced Problem Types Selector: A user can select an advanced problem type
  and be taken to the raw editor. Selecting the problem type:

     .. image:: /_images/release_notes/palm/ped7.png

  Then, advanced problem type can be selected:

   .. image:: /_images/release_notes/palm/ped8.png


Visual Editor
=============

* Problem types are changed using the “Type” setting to the right of the editor

* Multi-select questions were previously called checkbox questions

* Single select questions were previously called multiple choice questions

* Hints and feedback can still be used with the same problem types as before,
  but these configurable settings now exist as editable widgets for greater ease
  of use

* Content previously written in markdown will now present/render in the visual
  editor, and will be preserved safely

* Questions are entered in the provided question field with TinyMCE tools for
  improved styling

* Editing tools include a button to label the question for screen readers for
  improved accessibility

* Course authors can specify correct answers using checkboxes and radio buttons
  instead of manually specifying these using markdown

* Adding and deleting answer choices, answer-specific feedback, group feedback,
  and hints can all be edited visually using buttons and text fields in the UI

* Problem settings, which previously lived on a separate screen, have been
  included in the main editing experience and can be configured side by side and
  in-context with the problem authoring experience

* Settings with a pre-set default value now include links to the advanced
  settings page where the default value can be configured

* Below the question field is an explanation field in which an explanation for
  the correct answer can be provided. The TinyMCE toolbar is included here as
  well. There is a tolerance setting widget and an answer range option on
  Numerical Input Problems:

     .. image:: /_images/release_notes/palm/ped9.png


Raw OLX Editor
==============

* When selecting “advanced problem types” within the “select problem type” page,
  user is sent to raw editor

* Inside the visual editor, there is a “show advanced settings” button which
  shows additional settings and a link to get to the advanced editor. That link
  takes you to the advanced editor

* A course author will be taken to the advanced editor page if the parser cannot
  render the problem options in the visual editor experience

* Raw OLX Editing Capacity: the Code Editor is inside the raw editor. The
  block's OLX can be edited there.

* It uses xml syntax highlighting (not HTML)

*Note: the Raw Text Editor still works for HTML editing*

**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-04-28    | Docs WG                       | Teak           | Deprecated: This is no longer the current release |
+--------------+-------------------------------+----------------+---------------------------------------------------+

