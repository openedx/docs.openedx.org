.. _Add New Documentation Through GitHub:

Quick Start: Add New Documentation Through GitHub
#################################################

.. tags:: documentor, quickstart

.. sidebar:: Add Documentation Video Demo

  |Video Sidebar Click|

  Video Will be Added Soon!

.. contents:: Steps to Add Documentation
  :local:
  :class: no-bullets


**Prerequisites**

.. include:: ../how-tos/reusable_content/create_github_account.txt

.. include:: ../how-tos/reusable_content/sign_agreement.txt


Find Where to Add a New Topic
*****************************

The latest documentation is in the **main** branch of the `Open edX Documentation GitHub repository`_.

Review the :ref:`Documentation Audiences` and :ref:`About Open edX Documentation Standards` sections to determine where your addition should be located.

#. Navigate to the folder where you want to create the new topic.

#. Ensure the **main** branch is selected.


Create the New Topic
********************

In the location where you should create the new topic:, with the **main** branch selected:

#. In the :guilabel:`Add New File` drop-down, select :guilabel:`Create New File`.

   You receive the following message:

   .. image:: /_images/documentors_fork_message.png
    :width: 80%

   Followed by the interface for creating a new topic:

   .. image:: /_images/github_create_topic.png

#. At the top of the screen, give the file a name and the ``.rst`` extension.

#. Add content to the topic as needed.

   Ensure you keep to RST standards in file.  See the :ref:`Documentation Checklist` for guidelines, and copy RST code as needed from :ref:`Documentation Templates`.

#. In the **Propose New File** section at the bottom of the edit window:

   #. Add a comment about the addition you made.

   #. Optionally, add a longer description.

   #. Click :guilabel:`Propose new file` to save these changes to your fork.

GitHub then creates a *fork* of the repository that belongs to your account.  A fork is a complete copy of the repository, plus your changes. For more information, see `Github Forks`_.

GitHub then prompts you to create a pull request, which is a request for the Open edX team to integrate changes in your fork into the official repository.

.. thumbnail:: /_images/github_new_pr_fork.png

Create a Pull Request for the New Topic
***************************************

.. include:: ../how-tos/reusable_content/create_pull_request.txt

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+