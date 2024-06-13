Quick Start: Update Existing Docs Through GitHub
################################################

.. sidebar:: Edit Documentation Video Demo

  |Video Sidebar Click|

  Video Will be Added Soon!

.. contents:: Steps to Edit Documentation
  :local:
  :class: no-bullets

**Prerequisites**

.. include:: ../how-tos/reusable_content/create_github_account.txt

.. include:: ../how-tos/reusable_content/sign_agreement.txt


Edit a Topic
************

Use the following instructions when you are viewing the published documentation on
``docs.openedx.org`` and you want to make changes to it.

#. On the page you want to edit, under the GitHub icon in the header, |GitHub Icon|, select :guilabel:`suggest edit`.

#. Make the necessary changes.

   Ensure you keep to RST standards in file.  See the :doc:`../references/quick_reference_rst` a quick reference to RST.

#. In the Commit Changes section at the bottom of the edit window:

   #. Add a descriptive comment about the changes you made.

   #. Click :guilabel:`Propose changes` to save these changes to your branch.

      .. image:: /_images/documentors_howto_update_a_doc/edit_in_github.png

GitHub then creates a *fork* of the repository that belongs to your account.  A fork is a complete copy of the repository, plus your changes. For more information, see `Github Forks`_.

GitHub then prompts you to create a pull request, which is a request for the Open edX team to integrate changes in your fork into the official repository.

Create a Pull Request for Your Change
**************************************

.. include:: ../how-tos/reusable_content/create_pull_request.txt

