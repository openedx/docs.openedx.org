Add New Documentation via GitHub
################################

.. sidebar:: Add Documentation Video Demo

  |Video Sidebar Click|

  Video Will be Added Soon!

.. contents:: Steps to Add Documentation
  :local:
  :class: no-bullets

.. note::

   These instructions are for adding new documentation directly on GitHub. You can create documentation on your computer then synch it to GitHub, if you are familiar with the GitHub client software.

**Prerequisite**

.. include:: ../how-tos/reusable_content/create_github_account.txt



1. Find Where To Add a New Document
***********************************

The latest documentation is in the **main** branch of the `Open edX Documentation GitHub repository`_.

Review the :doc:`../concepts/doc_audiences` and :doc:`../concepts/content_types` sections to determine where you addition should be located.

#. Navigate to the folder where you want to create the new document.

#. Ensure the **main** branch is selected.

#. In the GitHub repository, click the branch drop-down.

#. Type the name of the branch, in the form of:

   ``your_github_username-type_of_change``

#. Click :guilabel:`Create branch`.

The branch you created becomes active; you can now create or edit documentation.


2. Create the New Document
***************************

In some cases (for example, with a brand new feature), you may want to create a new document to describe the feature.

With your new branch active:

#. Find the location where you should put the new document. Consider the audience and type of topic for the new content.

#. In the :guilabel:`Add New File` drop-down, select :guilabel:`Create New File`. You will see the following screen:

   .. image:: /_images/github_create_topic.png

#. At the top of the screen, give the file a name and the ``.rst`` extension.

#. Add content to the topic as needed.

   Ensure you keep to RST standards in file.  See the :doc:`../references/doc_checklist` for guidelines, and copy RST code as needed from :doc:`../references/doc_templates`.

#. In the Commit Changes section at the bottom of the edit window:

   #. Add a comment about the addition you made.

   #. Choose to commit directly to the branch you created in Step 1.

   #. Click :guilabel:`Propose new file` to save these changes to your branch.

#. Repeat these steps for all topics you need to create.

#. Every new topic must be added to a table of contents. Add each new topic to the audience home page in the appropriate place.



3. Create a Pull Request
************************

.. include:: ../how-tos/reusable_content/create_pull_request.txt
