.. _Exporting and Importing a Library:

Exporting and Importing a Legacy Library
###########################################

.. tags:: educator, how-to

.. contents::
  :local:
  :depth: 1

.. warning::

   The Legacy Libraries feature will be supported through Teak, moving to
   unsupported in Ulmo. Teak will include a one-click migration feature that
   will make it easy to convert a Legacy Library into the new Library interface.

   See :doc:`/community/release_notes/sumac/content_libraries_redesign_beta` for
   more information.

You can :ref:`export<Export a Library>` and :ref:`import<Import a Library>` a
content library in Studio.

.. warning:: When you import a library, the imported library completely
  replaces the existing library and its contents. You cannot undo a library
  import. Before you proceed, we recommend that you export the current
  library, so that you have a backup copy of it.

.. _Export a Library:

Export a Legacy Library
************************

There are several reasons why you might want to export your library.

* To save your work in progress
* To edit the XML in your library directly
* To create a backup copy of your library
* To share with another course team member

When you export your library, Studio creates a **.tar.gz** file (that is, a
.tar file compressed using GNU Zip). This export file contains the problems in
the library, including any customizations you made in the library to problem
settings. The export does not include library settings such as user access
permissions.

To export a library, follow these steps.

#. In Studio, select the **Libraries** tab.

#. Locate the library that you want to export.

#. From the **Tools** menu, select **Export**.

#. Select **Export Library Content** and specify where you want the file to be
   saved.

When the export process finishes, you can access the .tar.gz file on your
computer.

.. _Import a Library:

Import a Legacy Library
*************************

You might want to import a library if you developed or updated library content
outside of Studio, or if you want to overwrite a problematic or outdated
version of the library.

.. warning:: When you import a library, the imported library completely
  replaces the existing library and its contents. You cannot undo a library
  import. Before you proceed, we recommend that you export the current
  library, so that you have a backup copy of it.

The library file that you import must be a .tar.gz file (that is, a .tar file
compressed using GNU Zip). This .tar.gz file must contain a library.xml file.

To import a library, follow these steps.

#. In Studio, select the **Libraries** tab.

#. Locate the library to which you want to import the new library content.

#. From the **Tools** menu, select **Import**.

#. Select **Choose a File to Import** and select the .tar.gz file that you want
   to import.

#. Select **Replace my library with the selected file**.

   .. warning:: The import process has five stages. During the first two stages
     (Uploading and Unpacking), do not navigate away from the
     **Library Import** page. Doing so causes the import process to end. You
     can leave the page only after the Unpacking stage completes. We recommend
     that you do not make important changes to the library until all stages of
     the import process have finished.

#. When the import process finishes, select **View Updated Library** to view
   the imported library.

.. note:: If your imported library includes changes to components that are in
   use in a course, the course does not reflect these library updates until you
   manually update the randomized content block in the course unit. For details
   about updating library components used in your course to match the latest
   version in the content library, see :ref:`Get the Latest Version of Library
   Content`.

.. seealso::
 :class: dropdown

 :doc:`/community/release_notes/sumac/content_libraries_redesign_beta`

 :ref:`Content Libraries Overview` (concept)

 :ref:`Create a New Library` (how to)

 :ref:`Give Other Users Access to Your Library` (how to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
