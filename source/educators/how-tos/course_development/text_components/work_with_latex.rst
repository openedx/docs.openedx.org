.. :diataxis-type: how-to

.. _Work with Latex Code:

#############################################
Work with LaTeX Code
#############################################


JRistau (26 Sept 2022) - LaTeX editor support was removed with the rollout of
the new Course Authoring based Text Editor.  Coursegraph shows ~100 active
courses that have enabled the LaTeX advanced module, and we have had no
issues reported since rollout of the new text editor.  The LaTeX component
is listed as “Unsupported” in studio (TNL-9993).  For these reasons, edX PM
has decided to remove this section of our support documentation.



.. ==========================
.. Enable the LaTeX Processor
.. ==========================

.. The LaTeX processor is not enabled by default. To enable it, you have to change
.. the advanced settings in your course.

.. #. In Studio, select **Settings**, and then select **Advanced Settings**.

.. #. In the field for the **Enable LaTeX Compiler** policy key, change **false**
   to **true**.

.. #. At the bottom of the page, select **Save Changes**.

.. ==============================================
.. Add a Text Component that Contains LaTeX Code
.. ==============================================

.. When the LaTeX processor is enabled, you can create a Text component that
.. contains LaTeX code.

.. #. In the unit where you want to create the component, select **Text** under
   **Add New Component**, and then select **E-text Written in LaTeX**. The new
   component is added to the unit.

.. #. Select **Edit** to open the new component.

.. #. At the bottom of the component editor, select **Launch Latex Source
   Compiler**.

   The LaTeX editor opens.

   .. image:: ../images/HTML_LaTeXEditor.png
    :alt: The LaTeX editor.
    :width: 500

.. #. Add your LaTeX code. To do this, complete either of the following
   procedures.

   * In the **High Level Source Editing** field, add your LaTeX code.

   * To upload a LaTeX file from your computer, select **Upload**.

.. #. Select **Save & Compile to edX XML**.

.. #. On the unit page, select **Preview** to verify that your content looks
   correct in the LMS.

   If you see errors, go back to the unit page. Select **Edit** to open the
   component again, and then select **Launch Latex Source Compiler** to edit
   the LaTeX code.

.. _import latex code:

.. ****************************************
.. Import LaTeX Code into a Text Component
.. ****************************************

.. You can import LaTeX code into a Text component. You might do this, for
.. example, if you want to create "beautiful math" such as the math in the
.. following image.

.. .. image:: ../images/HTML_LaTeX_LMS.png
 :alt: Math formulas created with LaTeX in a Text component.

.. .. warning::
 The LaTeX processor that Studio uses to convert LaTeX code to XML is a third
 party tool. We recommend that you use this feature with caution. If you use
 the tool, make sure that you work with your partner manager.

.. seealso::
 :class: dropdown

  :ref:`Working with Text Components` (reference)
  :ref:`Create a Text Component` (how-to)
  :ref:`Paste without Formatting in a Text Component` (how-to)
  :ref:`Add an Image to a Text Component` (how-to)
  :ref:`Add Link to Website Course Unit or File` (how-to)
  :ref:`Work with HTML code` (how-to)

