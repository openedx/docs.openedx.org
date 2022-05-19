Quick Start: Add Documentation via Github
=========================================

.. sidebar:: Add Documentation Video Demo

  |Video Sidebar Click|

  Video TBP

.. contents:: Steps to Add Documentation
  :local:
  :class: no-bullets

.. note::
 :class: dropdown

 These instructions are for adding new documentation directly on GitHub.


1. Find the area where you want to add a new document
*****************************************************

The latest documentation is in the **main** branch of the `Open edX Documentation GitHub repository`_.

#. Navigate to the folder where you want to create the new document.

#. Ensure the **main** branch is selected.

#. In the GitHub repository, click the branch drop-down.

#. Type the name of the branch, in the form of:

   ``your_github_username-type_of_change``

#. Click :guilabel:`Create branch`.

The branch you created becomes active; you can now create or edit documentation.


2. Add a New Document
*********************

.. sidebar:: Create a Topic in GitHub

  .. thumbnail:: /_images/github_create_topic.png

In some cases (for example, with a brand new feature), you may want to create a new document to describe the feature.

With your new branch active:

#. Find the location where you should put the new document. Consider the audience and type of topic for the new content.

#. In the :guilabel:`Add New File` drop-down, select :guilabel:`Create New File`.

#. At the top of the screen, give the file a name and the ``.rst`` extension.

#. Add content to the topic as needed.

   Ensure you keep to RST standards in file.  See the :ref:`Documentation Checklist` for guidelines, and copy RST code as needed from :ref:`Documentation Templates`.

#. In the Commit Changes section at the bottom of the edit window:

   #. Add a comment about the addition you made.

   #. Choose to commit directly to the branch you created in Step 1.

   #. Click :guilabel:`Commit new file` to save these changes to your branch.

#. Repeat these steps for all topics you need to create.

#. Every new topic must be added to a table of contents. Add each new topic to the audience home page in the appropriate place.



3. Create a Pull Request
**********************************

.. sidebar:: Create a Pull Request in GitHub

  .. thumbnail:: /_images/github_pr_tab.png

When you are ready to have the Open edX team review your proposed documentation changes, you create a pull request.

#. In the GitHub repository, open the Pull requests tab.

#. Click :guilabel:`New pull request`.

#. In the right-hand drop-down field, select the branch on which you made changes. Keep *main* selected for the left-hand drop-down field.

   This indicates that you want to merge your branch into the *main* branch (the latest published documentation.)

   Below the drop-down fields, GitHub shows the changes in your branch, compared to the *main* branch.

#. Click :guilabel:`Create pull request`.

#. In the pull request, add a description of your changes.

The Open edX team will then review your changes. If they approve, they will merge the pull request, and you will see your changes in the latest documentation. The Open edX team may ask you to make further changes, to clarify the documentation or fix issues.
