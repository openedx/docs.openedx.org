.. _Exporting and Importing a Legacy Library:

Exporting and Importing a Legacy Library
###########################################

.. tags:: educator, how-to

.. contents::
  :local:
  :depth: 1

.. warning::

   The Legacy Libraries feature will be supported through Ulmo, moving to
   unsupported in Verawood. Ulmo will include a one-click migration feature that
   will make it easy to convert a Legacy Library into the new Library interface.

   See :ref:`Content Libraries Redesign Teak` for more information.

You can :ref:`export<Export a Legacy Library>` and :ref:`import<Import a Legacy Library>` a legacy
content library in Studio.

.. warning:: When you import a legacy library, the imported legacy library completely
  replaces the existing legacy library and its contents. You cannot undo a legacy library
  import. Before you proceed, we recommend that you export the current
  legacy library, so that you have a backup copy of it.

.. _Export a Legacy Library:

Export a Legacy Library
************************

There are several reasons why you might want to export your legacy library.

* To save your work in progress
* To edit the XML in your legacy library directly
* To create a backup copy of your legacy library
* To share with another course team member

When you export your legacy library, Studio creates a **.tar.gz** file (that is, a
.tar file compressed using GNU Zip). This export file contains the problems in
the legacy library, including any customizations you made in the legacy library to problem
settings. The export does not include legacy library settings such as user access
permissions.

To export a legacy library, follow these steps.

#. In Studio, select the **Legacy Libraries** tab.

#. Locate the legacy library that you want to export.

#. From the **Tools** menu, select **Export**.

#. Select **Export Library Content** and specify where you want the file to be
   saved.

When the export process finishes, you can access the .tar.gz file on your
computer.

.. _Import a Legacy Library:

Import a Legacy Library
*************************

You might want to import a legacy library if you developed or updated legacy library content
outside of Studio, or if you want to overwrite a problematic or outdated
version of the legacy library.

.. warning:: When you import a legacy library, the imported legacy library completely
  replaces the existing legacy library and its contents. You cannot undo a legacy library
  import. Before you proceed, we recommend that you export the current
  legacy library, so that you have a backup copy of it.

The legacy library file that you import must be a .tar.gz file (that is, a .tar file
compressed using GNU Zip). This .tar.gz file must contain a library.xml file.

To import a legacy library, follow these steps.

#. In Studio, select the **Legacy Libraries** tab.

#. Locate the legacy library to which you want to import the new legacy library content.

#. From the **Tools** menu, select **Import**.

#. Select **Choose a File to Import** and select the .tar.gz file that you want
   to import.

#. Select **Replace my library with the selected file**.

   .. warning:: The import process has five stages. During the first two stages
     (Uploading and Unpacking), do not navigate away from the
     **Library Import** page. Doing so causes the import process to end. You
     can leave the page only after the Unpacking stage completes. We recommend
     that you do not make important changes to the legacy library until all stages of
     the import process have finished.

#. When the import process finishes, select **View Updated Library** to view
   the imported legacy library.

.. note:: If your imported legacy library includes changes to components that are in
   use in a course, the course does not reflect these legacy library updates until you
   manually update the randomized content block in the course unit. For details
   about updating legacy library components used in your course to match the latest
   version in the content legacy library, see :ref:`Get the Latest Version of legacy library
   Content`.

.. seealso::
 

 :ref:`Content Libraries Redesign Teak`

 :ref:`Legacy Content Libraries Overview` (concept)

 :ref:`Create a New Legacy Library` (how to)

 :ref:`Give Other Users Access to Your Legacy Library` (how to)

**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                 |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| 07/30/2025   | Sarina                        | Teak           |Deprecated                                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
