.. _Components that Contain Other Components:

Components that Contain Other Components
#########################################

.. tags:: educator, reference

For specific use cases, you configure course content so that components contain
other components. For example, if you want to include conditional components or
content experiments, you have to create components inside components. See
:ref:`Add Content Experiments to Your Course` for more information.

The component that contains other components is referred to as the *parent*;
the contained components are referred to as child components, or children.

On a unit page, a parent component appears with its display name and a
**View** link.

.. image:: /_images/educator_references/component_container.png
 :alt: A unit page with a parent component.
 :width: 500



Edit a Parent Component
*************************

A parent component does not directly contain content. Content such as HTML,
videos, or problems are in the child components.

A parent component has a display name. When the unit is private or in draft,
select **Edit** in the parent component to change the display name.

.. note::
  Parent components of a specific type, such as content experiments, have
  additional attributes that you edit.



View Child Components
**********************

When you select **View** in the parent component, the parent component page
opens, showing all child components. In this example, Child Component A
contains a Text component and a video.

.. image:: /_images/educator_references/child-components-a.png
 :alt: An expanded child component.
 :width: 400

Select the arrow next to a child component name to collapse it and hide the
component's contents. Select the arrow again to expand the component.

For more information, see the following topics.

* :ref:`Edit a Component`
* :ref:`Set the Display Name for a Component`
* :ref:`Duplicate a Component`
* :ref:`Delete a Component`


Add a Child Component
**********************

If the containing unit is private or in draft, you can add a child component in
its parent component.

To add a child component, open and expand the parent component. Then, select
the component type that you want under **Add New Component** within the parent
component.

For more information, see the section for the specific component type that you
want.

- :ref:`Working with Discussion Components`
- :ref:`Working with Text Components`
- :ref:`Working with Problem Components`
- :ref:`Working with Video Components`



XML for Parent and Child Components
************************************

You develop parent and child components in XML, then import the XML course into
Studio to verify that the structure is as you intended.

For more information about working with your course's XML files, including
information about terminology, see the `EdX Open Learning XML Guide <https://edx.readthedocs.io/projects/edx-open-learning-xml/en/latest/index.html>`.

The following examples show the XML used to create the unit and components
shown in Studio above.

The XML for the unit is as follows.

.. code-block:: xml

    <vertical display_name="Unit 1">
        <html url_name="6a5cf0ea41a54b209e0815147896d1b2"/>
        <vertical url_name="131a499ddaa3474194c1aa2eced34455"/>
    </vertical>

The ``<vertical url_name="131a499ddaa3474194c1aa2eced34455"/>`` element above
references the parent component file that contains the child components.

.. code-block:: xml

    <vertical display_name="Parent Component">
        <vertical url_name="2758bbc495dd40d59050da15b40bd9a5"/>
        <vertical url_name="c5c8b27c2c5546e784432f3b2b6cf2ea"/>
    </vertical>

The two verticals referenced by the parent component refer to the child
components, which contain the actual content of your course.

.. code-block:: xml

    <vertical display_name="Child Component A">
        <html url_name="4471618afafb45bfb86cbe511973e225"/>
        <video url_name="fbd800d0bdbd4cb69ac70c47c9f699e1"/>
    </vertical>

.. code-block:: xml

    <vertical display_name="Child Component B">
        <html url_name="dd6ef295fda74a639842e1a49c66b2c7"/>
        <problem url_name="b40ecbe4ed1b4280ae93e2a158edae6f"/>
    </vertical>

Theoretically, there is no limit to the levels of component nesting you can use
in your course.



The Learner View of Nested Components
**************************************

For learners, all parent and child components appear on the unit page.

.. note::
 The visibility of nested components depends on the visibility of the parent
 unit. The parent unit must be public for learners to see nested components.
 For more information, see :ref:`Unit States and Visibility to Students`.

The following example shows the learner view of the unit described above.

.. image:: /_images/educator_references/nested_components_student_view.png
 :alt: The learner's view of nested components.
 :width: 400

.. seealso::
 :class:dropdown

 :ref:`Unit States and Visibility to Students` (reference)

 :ref:`Working with Discussion Components` (reference)
 
 :ref:`Working with Text Components` (reference)
 
 :ref:`Working with Problem Components` (reference)
 
 :ref:`Working with Video Components` (reference)