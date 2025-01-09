.. _Working with Text Components:

.. tags:: educator, reference

.. this is the old name of this section, left here so that frozen Maple
    projects will resolve the reference:
.. _Working with HTML Components:

############################
About Text Components
############################

.. tags:: educator, reference

Text components are the basic building blocks of your course content. You use
Text components to add and format text, links, images, and more. You can work
with your Text components in a "visual" or WYSIWYG editor that hides the HTML
code details, or in a "raw" editor that requires you to mark up your content.

.. note::
 Review :ref:`Developing Your Course Outline` and :ref:`Best Practices for HTML
 Markup` before you start working with Text components.


.. _Options for Editing Text Components:

***********************************
Options for Editing Text Components
***********************************

You can use two different editing interfaces to work with a Text component.

* :ref:`The Visual Editor`

  With the visual editor you create, edit, and format content in a word
  processing-like interface, without using HTML markup directly. With the
  visual editor, you can more easily format your content, and add links and
  images.

  The visual editor includes an **HTML** option for you to review the
  HTML markup and make small formatting changes to your content. However, this
  HTML option does not provide the detailed control you can get with the raw
  HTML editor, nor does it support custom formatting or scripts.

  If you add a Text component and select **Text**, when you select **Edit**
  the visual editor opens by default.

* :ref:`The Raw HTML Editor`

  If you prefer to mark up your content directly with HTML markup, you can use
  the raw HTML editor. If you need to include custom formatting or scripts in
  your content, you must use the raw HTML editor.

  If you add a Text component and select **Raw HTML**, when you select
  **Edit** the raw HTML editor opens by default.

  There is no way to switch between the Visual Editor and the Raw HTML editor
  once one is selected.

.. note::
    If you copy text from another source and paste it into either the visual or
    raw HTML editor, be sure to proofread the result carefully. Some
    applications automatically change quotation marks and apostrophes from the
    "straight" version to the "smart" or "curly" version. Both editors require
    "straight" quotation marks and apostrophes.

.. _The Visual Editor:

=================
The Visual Editor
=================

The visual editor provides a "what you see is what you get" (WYSIWYG) interface
that allows you to format text by selecting options at the top
of the editor.

The following image shows callouts for the editing options and is followed by
descriptions.

.. image:: /_images/educator_references/HTML_VisualView_Toolbar.png
  :alt: An image of the visual editor toolbar, with numbers next to each of the
   formatting buttons.
  :width: 600

#. Arrows that perform undo/redo actions.

#. Select a formatting style for the selected text, such as paragraph,
   ``preformatted`` (monospace), or a heading level.

   .. note::
     The available heading levels in the Text component editor begin with
     heading 2 (``<h2>``). Text components are part of a complete page, and
     elements outside the Text component use heading level 1 by default.
     Because tools such as screen readers use heading levels to navigate
     through pages, using heading level 1 inside a Text component can
     interfere with the functionality of these tools.

#. Format the selected text in bold, or remove this formatting. The editor
   inserts ``<strong>`` tags around the selected text.

#. Format the selected text in italics, or remove this formatting. The editor
   inserts ``<em>`` tags around the selected text.

#. Underline the selected text, or remove this formatting. The editor encloses
   the selected text in the tag ``<span style="text-decoration: underline;">``.

#. Change the color of the selected text. The editor encloses the selected text
   in the tag ``<span style="color: color-hex-code;">``.

#. Change the background color of the selected text. The editor encloses the
   selected text in the tag ``<span style="background-color: color-hex-code;">``.

#. Align text and images to the left. The editor adds ``style="text-align:
   left;"`` to the ``<p>`` tags that surround the text.

#. Center text and images. The editor adds ``style="text-align: center;"`` to
   the ``<p>`` tags that surround the text.

#. Align text and images to the right. The editor adds ``style="text-align:
   right;"`` to the ``<p>`` tags that surround the text.

#. Justify text and images. The editor adds ``style="text-align: justify;"`` to
   the ``<p>`` tags that surround the text.

#. Create a bulleted list, or remove this formatting. The editor inserts
   ``<ul>`` tags around the selected text, and encloses each paragraph in
   ``<li>`` tags.

#. Create a numbered list, or remove this formatting. The editor inserts
   ``<ol>`` tags around the selected text, and encloses each paragraph in
   ``<li>`` tags.

#. Decrease and increase the indentation of the selected paragraph.

#. Insert an image at the cursor. For more information, see :ref:`Add an Image
   to a Text Component`.

#. Create a hypertext link from the selected text. For more information, see
   :ref:`Add a Link in a Text Component`.

#. Remove a hypertext link from the selected text.

#. Format the selected paragraph as a blockquote. The editor inserts
   ``<blockquote>`` tags around the selected text, which is then displayed as a
   separate indented paragraph.

#. Format the selected text as a code block, or remove this formatting. The
   editor inserts ``<code>`` tags around the selected text, which is then
   displayed in a monospace font.

#. The table toolbar icon lets you drop in a table component and selecting a
   given cell lets you create, remove, or adjust rows and columns.

#. You can easily add emoticons to your text content. This can be a way to break
   up long stretches of content.

#. We have introduced a way to to include special characters into your text
   content, including mathematical and symbolic elements.

#. Inject a horizontal line in the highlighted content.

#. Clear formatting button which removes all font formatting from the selected
   text.  This does not remove paragraph formatting (e.g. blockquote).

#. Review the HTML markup.

#. Accessibility Checker, which allows you to check HTML in the editor for various
   accessibility problems. For more information, see :ref:`Accessibility Checker`.


.. note::
  The visual editor is not available for :ref:`course handouts <Adding Course
  Updates and Handouts>`.

.. seealso::
 :class: dropdown

 :ref:`Create a Text Component` (how-to)

 :ref:`Paste without Formatting in a Text Component` (how-to)

 :ref:`Add an Image to a Text Component` (how-to)

 :ref:`Add Link to Website Course Unit or File` (how-to)

 :ref:`Work with HTML code` (how-to)

 :ref:`Work with Latex Code` (how-to)
