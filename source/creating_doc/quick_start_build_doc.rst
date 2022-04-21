Quick Start: Add Documentation
===============================

.. sidebar:: Add Documentation Video Demo

  |Video Sidebar Click|

  Video TBP

.. contents:: Steps to Add Documentation
  :local:
  :class: no-bullets

.. note:: 
 :class: dropdown

 These instructions are for adding and editing documentation directly on GitHub. You can also work with documentation on your computer, which requires setting up Sphinx, an editor, and GitHub tools.

1. Create a new branch in the documentation repository
*******************************************************

.. sidebar:: GitHub Branches drop-down

  .. thumbnail:: ../_images/github_repo_branches.png

The latest documentation is in the **main** branch of the `Open edX Documentation GitHub repository`_.

You cannot edit the **main** branch directly. Instead, you must create your own branch in which to make changes.  

#. Ensure the **main** branch is selected.

#. In the GitHub repository, click the branch drop-down.

#. Type the name of the branch, in the form of:

   ``your_github_username-type_of_change``

#. Click :guilabel:`Create branch`.

The branch you created becomes active; you can now create or edit documentation.


2. Edit a file
*****************

.. sidebar:: Edit a Topic in GitHub

  .. thumbnail:: ../_images/github_edit_topic.png

With your new branch active:

#. Find the topic you need to edit.

#. Click the pencil icon (|GitHub Pencil|).

   The topic opens in edit mode.

#. Make the necessary changes.  

   Ensure you keep to RST standards in file.  See the :ref:`Documentation Checklist` for guidelines, and copy RST code as needed from :ref:`Topic Templates`.

#. In the Commit Changes section at the bottom of the edit window:

   #. Add a comment about the changes you made.

   #. Choose to commit directly to the branch you created in Step 1.

   #. Click :guilabel:`Commit changes` to save these changes to your branch.

#. Repeat these steps for all topics you need to edit.


3. Add a New Topic
*********************

.. sidebar:: Create a Topic in GitHub

  .. thumbnail:: ../_images/github_create_topic.png

In some cases (for example, with a brand new feature), you will need to create a new topic.

With your new branch active:

#. Find the topic you should put the new topic in. Consider the audience and type of topic for the new content.

#. In the :guilabel:`Add New File` drop-down, select :guilabel:`Create New File`.

#. At the top of the screen, give the file a name and the ``.rst`` extension.

#. Add content to the topic as needed.  

   Ensure you keep to RST standards in file.  See the :ref:`Documentation Checklist` for guidelines, and copy RST code as needed from :ref:`Topic Templates`.

#. In the Commit Changes section at the bottom of the edit window:

   #. Add a comment about the addition you made.

   #. Choose to commit directly to the branch you created in Step 1.

   #. Click :guilabel:`Commit new file` to save these changes to your branch.

#. Repeat these steps for all topics you need to create.



4. Create a Pull Request
**********************************

5. Test the Publication of your branch on ReadTheDocs
******************************************************

6. Edit Topics if Neded
***************************

7. Tag the OpenedX Team in the Pull Request
*********************************************


The Open edX team will review your changes and may make recommendations. When ready, they will merge it.















