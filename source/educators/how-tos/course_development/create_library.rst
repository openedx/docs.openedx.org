.. :diataxis-type: how-to

.. _Create a New Library:

********************
Create a New Library
********************

Use :ref:`content libraries<Content Libraries>` to build a pool of components
that can be used in randomized assignments in your courses.

To create a new library, follow these steps.

#. Log in to Studio.

#. Select **New Library**.

#. Enter the required information for your new library, then select **Create**.

   .. note:: Enter new library information carefully. The values in these
      fields become part of the URL for your library, therefore the total
      number of characters in the **Library Name**, **Organization**, and
      **Library Code** fields must be 65 or fewer.

   .. image:: /_images/educator_how_tos/ContentLibrary_NewCL.png
      :alt: Image of the library creation page.
      :width: 600

  - For **Library Name**, enter the public display name for your library.
    Choose a meaningful name that will help you and other course team members
    to identify the library. For example, "Level 200 Math Problems". When you
    add a randomized content block to a course unit, you use the library name
    to specify this library as a source for the randomized assignment.

  - For **Organization**, enter the identifier for your university. For
    example, enter HarvardX or MITx. Do not include spaces or special
    characters.

  - For **Library Code**, enter an identifier for your library that is unique
    within your organization. This code becomes part of the URL for your
    library, so do not include spaces or special characters in the code.

4. Select **Create**.

You see the new library, to which you can now add components. For information
about adding components to a library, see :ref:`Add Components to a Library`.

After you create a library, you are automatically assigned an **Admin** role
for the library. For information about adding other users to a library after
you create it, see :ref:`Give Other Users Access to Your Library`.


.. _Edit a Library:

**************
Edit a Library
**************

After you create a library, the only change you can make to the initial library
information is to the name. However, at any time, you can make changes to the
components in your library, including adding or deleting components or editing
the settings of components. For details about editing the contents of a
library, see :ref:`Edit Components in a Library` and :ref:`Add Components to a
Library`.

To change the name of a library, follow these steps.

#. Log in to Studio.

#. Select **Libraries**, then select the library whose name you want to edit.

#. Select the **Edit** icon next to the library name.

   The library name field becomes editable.

   .. image:: /_images/educator_how_tos/ContentLibrary_EditName.png
     :alt: The Edit icon to the right of the Library Name.
     :width: 300

#. In the library name field, make edits or enter a new library name.

#. Select anywhere outside the library name field to save your changes.

For details about giving other users access to the library, see :ref:`Give
Other Users Access to Your Library`.

.. _Add Components to a Library:

****************************
Add Components to a Library
****************************

To add new :ref:`components<Developing Course Components>` to your library,
follow these steps.

#. Log in to Studio.

#. Select **Libraries**, then select the library that you want to add
   components to.

#. Select **Add Component**, then select the component type that you want to
   add under **Add New Component**.

For more information about the types of components you can add to a library,
see these topics.

* :ref:`Working with Text Components<working with text components>`
* :ref:`Working with Problem Components`
* :ref:`Working with Video Components`

After you add a component to a library, you can edit its settings. These
settings are retained when the component is selected from the library and used
in a course.

When a component from the library is used in a randomized content block, you
can further edit the component as it exists in the unit, without affecting the
original version in the library. For details, refer to :ref:`Edit Components in
a Library` and :ref:`Get the Latest Version of Library Content <Get the Latest Version of Library Content>`.

.. _View the Contents of a Library:

******************************
View the Contents of a Library
******************************

To view the entire contents of a library in Studio, follow these steps.

#. Log in to Studio.

#. Select **Libraries**, then select the library whose components you want to
   view.

#. Optionally, select **Hide Previews** at the top right of the library page to
   collapse the component previews and see only the list of component display
   names. To return to the full preview of components in the library, select
   **Show Previews**.

The components in the library are shown in the order in which they were added,
with the most recently added at the bottom. If your library has more than 10
components, additional components are shown on other pages.

The range of the components shown on the current page, and the total number of
components, are shown at the top of the page.

You can navigate through the pages in the following ways.

* Use the **<** and **>** buttons at the top and bottom of the list to navigate
  to the previous and next pages.

* At the bottom of the page, you can edit the first number in the page range.
  Select the number to place your cursor in the field, then enter the page
  number you want to jump to.

  .. image:: /_images/educator_how_tos/file_pagination.png
     :alt: Image showing a pair of page numbers with the first number circled.
     :width: 300

To view the list of matching components in the library, see :ref:`View the
Matching Components in a Randomized Content Block`.

To view the randomized content that was assigned to a specific learner, see
:ref:`Specific Student View`.


.. _Edit Components in a Library:

****************************
Edit Components in a Library
****************************

After you have added components to a library, you can edit, duplicate, or
delete them.

For step-by-step instructions for editing, duplicating, or deleting components,
refer to the following topics.

* :ref:`Edit a Component`
* :ref:`Duplicate a Component`
* :ref:`Delete a Component`

.. note:: If you modify components in your library that are in use in a course,
   these updates in the "source" library are not reflected in the course unless
   you manually update the randomized content block in the course unit. For
   details about updating library components used in your course to match the
   latest version in the library, see :ref:`Get the Latest Version of Library
   Content`.

.. _Delete a Library:

*****************
Delete a Library
*****************

You cannot delete a library. Instead, you can discontinue use of an unwanted
library. To do so, first make sure that none of its components are in use in
any courses, then delete all components in the library. You can also :ref:`edit
the name of the library<Edit a Library>` to make it clear to other course team
members that the library should not be used as a source of randomized
assignment content in courses.

For details about deleting components in a library, see :ref:`Edit Components
in a Library`.


.. seealso::
 :class: dropdown

  :ref:`Content Libraries Overview` (concept)
  :ref:`Give Other Users Access to Your Library` (how to)
  :ref:`Exporting and Importing a Library` (how to)
