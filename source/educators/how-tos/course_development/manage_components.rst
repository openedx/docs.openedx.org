.. _Manage Course Components:

#########################
Manage Course Components
#########################

.. tags:: educator, how-to

.. contents::
  :local:
  :depth: 2

.. _Add a Component:

***************************
Add a Component
***************************

To add a component to the unit, follow these steps.

#. In Studio, open the page for the unit.
#. Under **Add New Component**, select a component type. The default component
   types are discussion, HTML, problem, and video.

For more information, see the documentation for the specific component type
that you want to work with.

- :ref:`Configure Open edX Discussions Legacy`
- :ref:`About Text Components <About Text Components>`
- :ref:`Working with Problem Components`
- :ref:`Working with Video Components`

After you add a component, it is not visible to learners until you
:ref:`publish the unit<Publish a Unit>`.

.. _Edit a Component:

*****************
Edit a Component
*****************

To edit a component, you select **Edit** in the component's title bar in
Studio.

.. image:: /_images/educator_how_tos/unit-edit.png
  :alt: A component with the Edit icon indicated in the toolbar.
  :width: 400

Then, follow instructions for the type of component you are editing.

After you edit a component, the changes are not visible to learners until you
:ref:`publish the unit<Publish a Unit>`.

.. _Set the Display Name for a Component:

************************************
Set the Display Name for a Component
************************************

The display name identifies the component. This name appears as a heading
above the component in the LMS, and it identifies the component for you in
reporting and analytics systems.

The following illustration shows the display name of a problem in Studio and in
the LMS.

.. image:: /_images/educator_how_tos/display_names_problem.png
 :alt: The identifying display name for a problem in Studio, and the LMS.
 :width: 800

Unique, descriptive display names help you and your learners identify
components quickly and accurately.

To set the display name for a component, follow these steps.

#. Edit the component; a dialog box opens.

   * For a discussion or video component, the dialog box opens to the list of
     settings, including the **Display Name** field.

   * For an HTML or problem component, the dialog box opens to an editing view.
     Select **Settings** to show the list of settings, including the **Display
     Name** field.

#. Edit the **Display Name** field.

   .. image:: /_images/educator_how_tos/display-name.png
    :alt: The settings dialog box for a problem component.
    :width: 500

#. Select **Save**.

Different types of components have different fields in the **Settings** dialog
box, but all of them have a **Display Name** field.

.. _Reorganize a Component:

**********************************
Reorganize a Component
**********************************

You can drag and drop components to a new position within their current unit,
or you can move components from one unit to another unit.

=====================================
Reorganize Components Within a Unit
=====================================

To reorganize components within their current unit, you drag and drop
components like you can drag and drop units, subsections, and
sections on the **Course Outline** page. For more information, see
:ref:`Reorganize the Course Outline`.

For components that consist of nested components (for example, a content
experiment), you can also use drag and drop to move a child component into a
different parent component, if both parents are expanded. For example, you can
select the video component that is in Child Component A and drag it into Child
Component B. Select the video component, and as you drag it into Child
Component B, release the mouse button when a dashed outline of the component
you are moving appears in the new location.

.. image:: /_images/educator_how_tos/drag_child_component.png
 :alt: A child component being dragged to a new location in a different parent
       component.
 :width: 400

You can also drag a child component outside of a parent, so that the child
moves to the same level as the parent.

=====================================
Move Components to Other Units
=====================================

Follow these steps to move components to another unit in the course outline.

#. Select the **Move** icon for the component that you want to move.

   .. image:: /_images/educator_how_tos/component_move_icon.png
      :alt: The action icons for components, with the Move icon highlighted.

   A dialog box appears that displays your course outline tree, starting at the
   section level.

#. In the **Move** dialog box, navigate to the location where you want to move
   the component by selecting the section, the subsection, and then the unit.

   .. image:: /_images/educator_how_tos/component_move_navigation.png
      :alt: The Move dialog box displays your course outline tree for
        navigating to the unit you want to move your component to.
      :width: 380

   The **Move** button is enabled only when your selected location is a valid
   level and location for moving your component. For example, when you move a
   component, the **Move** button is enabled only when you have navigated to
   a unit to which the component can be moved.

#. Select **Move**.

   The component moves to the new location. A success message appears that
   provides options to go to the new location or to undo the move.

   .. note::

       If the old and new locations of the component you moved were
       previously published, your changes are not reflected in the learner's
       view of the course until you republish the affected units.

.. _Duplicate a Component:

**********************
Duplicate a Component
**********************

When you duplicate a component, a new copy of that component is added directly
beneath the first component. You can then modify the duplicate. In many cases,
duplicating a component and editing the copy is a faster way to create new
content.

To duplicate a component, select the **Duplicate** icon in the component
header.

.. image:: /_images/educator_how_tos/unit-dup.png
  :alt: A unit with the Duplicate icon selected and highlighted.

Then, follow instructions for the type of component you are editing.

After you duplicate a component, the new component is not visible to learners
until you :ref:`publish the unit<Publish a Unit>`.

.. note::  Duplicating content experiments after you have configured them is not
   supported.

.. _Delete a Component:

*******************
Delete a Component
*******************

.. caution::
 Be sure you want to delete the component. You cannot undo the deletion.

To delete a component, follow these steps.

#. Select the **Delete** icon in the component header.

.. image:: /_images/educator_how_tos/unit-delete.png
  :alt: A unit with the Delete icon circled.

2. When you receive the confirmation prompt, select **Yes, delete this
   component**.

After you delete a component in Studio, the component remains visible to
learners until you :ref:`publish the unit<Publish a Unit>`.

.. seealso::

 :ref:`About Course Components` (concept)

 :ref:`Restrict Access to a Component` (how-to)

 :ref:`Components that Contain Other Components` (reference)  


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 06/26/2025   | Leira (Curricu.me)            | Sumac          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
