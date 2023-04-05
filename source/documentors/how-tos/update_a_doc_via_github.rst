Update An Existing Doc via GitHub
#################################

This how-to will take you through the process of submitting an update to a page
that you are looking at within the Open edX documentation.

Prerequisites
*************

* You're on the published documentation page at some address like ``docs.openedx.org/...`` and you want to make changes to it.

* You have a GitHub Account

  * If not `sign up here`_.

* In the GitHub UI, make any edits you need to make.

.. _sign up here: https://github.com/signup

1. Edit a file
**************

#. On the page you want to edit, find the ``suggest edit`` link.

   .. image:: /_images/documentors_howto_update_a_doc/suggest_edit_link.png

#. Make the necessary changes.

   Ensure you adhere to RST standards in the file.  See the :doc:`../references/quick_reference_rst` for a quick RST reference.

#. In the Commit Changes section at the bottom of the edit window:

   #. Add a descriptive comment about the changes you made.

   #. Click :guilabel:`Propose changes` to save these changes to your branch.

      .. image:: /_images/documentors_howto_update_a_doc/edit_in_github.png

2. Create a Pull Request
************************

When you are ready to have the Open edX team review your proposed documentation changes, you create a pull request.

#. Once you have clicked the :guilabel:`Propose changes` button, click :guilabel:`Create pull request`.

   .. image:: /_images/documentors_howto_update_a_doc/create_pr_screen1.png

#. On the next screen, give your pull request a unique, descriptive title and add a full description of your changes.

#. Click :guilabel:`Create pull request` button again to complete submitting your changes. Please make sure the "Allow edits by maintainers" checkbox is checked - this enables the Open edX team to rerun tests or make small changes, which will decrease the time for your changes to be accepted.

   .. image:: /_images/documentors_howto_update_a_doc/create_pr_screen2.png

The Open edX team will then review your changes. If they approve, they will merge the pull request, and you will see your changes in the latest documentation. The Open edX team may ask you to make further changes, to clarify the documentation or fix issues. See :doc:`make_changes_to_your_pull_request` if you'd like a refresher on how to make changes to your existing pull request.
