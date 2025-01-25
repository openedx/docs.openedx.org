.. _Work with HTML code:

Work with HTML Code in the Text Component
#############################################

.. tags:: educator, how-to

HTML, or HyperText Markup Language, is the standard markup language used to
create web pages. Web browsers present HTML code in a more readable format.

When students see text and images in your course, they are seeing HTML code
that is formatted and presented by their browsers. For more information about
HTML, see `Wikipedia <https://en.wikipedia.org/wiki/HTML>`_.

Review HTML Markup in the Visual Editor
***************************************

#. To review the HTML markup added to content in the visual editor, select
**HTML** from the visual editor's toolbar. The HTML source code editor opens.

    .. image:: /_images/educator_how_tos/HTML_source_code.png
     :alt: The HTML source code editor for the visual editor in Studio, showing
         HTML with markup.
     :width: 600

#. You can edit text and the HTML markup in this editor. However, you cannot add
custom styles or scripts in this editor. To do this, you must use the
:ref:`raw HTML editor<The Raw HTML Editor>` instead.

#. Select **Save** to return to the visual editor. The visual editor attempts to
correct any problems with the markup you entered. For example, if you do
not provide a close paragraph tag, the editor adds the tag for you.

#. You can then continue working in the visual editor.

.. warning::
 Selecting **OK** in the source code editor does not save your changes to the
 Text component. To save your changes and close the component, select **Save**
 in the visual editor. If you select **Cancel**, the changes you made in the
 HTML source code editor are discarded.

.. _The Raw HTML Editor:

The Raw HTML Editor
********************

The raw HTML editor is a text editor. It does not offer a toolbar with
formatting options.

.. image:: /_images/educator_how_tos/raw_html_editor.png
 :alt: The raw HTML editor, showing example HTML.
 :width: 600

When you use this editor, you must supply valid HTML. The raw HTML editor does
not validate your HTML code. If you use this editor, you should thoroughly test
the HTML content in your course.

.. important::
 When you add a heading to a Text component, make sure you use only
 heading level 2 ``<h2>`` through heading level 6 ``<h6>``. Text components are
 part of a complete page, and elements outside the Text component use heading
 level 1 by default. Because tools such as screen readers use heading
 levels to navigate through pages, using heading level 1 inside a Text
 component can interfere with the functionality of these tools.


.. seealso::
 

 :ref:`Working with Text Components` (reference)

 :ref:`Create a Text Component` (how-to)

 :ref:`Paste without Formatting in a Text Component` (how-to)

 :ref:`Add an Image to a Text Component` (how-to)

 :ref:`Add Link to Website Course Unit or File` (how-to)

 :ref:`Work with Latex Code` (how-to)
