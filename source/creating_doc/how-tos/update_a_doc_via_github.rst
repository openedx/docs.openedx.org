How-To: Update A Doc via GitHub
###############################

This how-to will take you through the process of submitting an update to a page
that you are looking at within the Open edX documnetation.

Prerequisites
*************

* You're on the published documentation page at some address like
  ``docs.openedx.org/...`` and you want to make changes to it.

* You have a GitHub Account
   * If not `sign up here`_.

.. _sign up here: https://github.com/signup

2. In the github UI, make any edits you need to make.

1. Edit a file
*****************

.. sidebar:: Edit a Topic in GitHub

  .. thumbnail:: ../_images/github_edit_topic.png

#. On the page you want to edit, find the ``suggest edit`` link.

   #TODO: Add a picture.

#. Make the necessary changes.

   Ensure you keep to RST standards in file.  See the :doc:`../quickstart_rst` a quick reference to RST.

#. In the Commit Changes section at the bottom of the edit window:

   #. Add a comment about the changes you made.

   #. Click :guilabel:`Commit changes` to save these changes to your branch.

2. Create a Pull Request
**********************************

.. sidebar:: Create a Pull Request in GitHub

  .. thumbnail:: ../_images/github_pr_tab.png

When you are ready to have the Open edX team review your proposed documentation changes, you create a pull request.

#. Once you have clicked the :guilabel:`Commit changes` button

#. Click :guilabel:`Create pull request`.

#. In the pull request, add a description of your changes.

#. Click :guilabel:`Create pull request` button again to complete submitting your changes.

The Open edX team will then review your changes. If they approve, they will merge the pull request, and you will see your changes in the latest documentation. The Open edX team may ask you to make further changes, to clarify the documentation or fix issues.
