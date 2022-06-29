Quick Start: First Documentation PR
###################################

.. sidebar:: First Docs PR Walkthrough

   |Video Sidebar Click|

   Video TBP

This quickstart will walk you through the process of making an update to a piece
of documentation on docs.openedx.org.

**Prerequisites**

.. important::

   .. include:: ../how-tos/reusable_content/create_github_account.txt

.. Leave the CLA stuff for later don't mention it here to reduce the number of
   steps before we're making a change.

.. contents:: Steps to Making your First Documentation PR
   :local:
   :class: no-bullets


Login to GitHub
***************

Go to https://github.com/login

If you are not already logged in, go ahead and login. If you are already logged
in, GitHub will redirect you to the homepage https://github.com

Find a Page to Update
*********************

First let's find a page in the documentation that needs to be updated.

Go to the :doc:`../references/doc_with_errors`

This page has a spelling error that we want to fix, let's go to the source and
make a change.

.. image:: /_images/documentors_quickstart_first_pr/bad_spelling.png
   :alt: A screenshot of the bad spelling of the word spelling on the sample page.


Suggest an edit
***************

Click the :guilabel:`suggest edit` button to begin the process of changing the text.

.. image:: /_images/documentors_quickstart_first_pr/suggest_edit.png
   :alt: A screenshot of the sample page with the 'suggest edit' link highlighted.


Fork the repository(repo)
*************************

If you have never made a pull request to this repo, you'll be asked to fork the
repo.

Go ahead and click the big green button!

   TODO: Add a picture and highlight the fork button. Need to merge the basic PR
   with the sample document before we can take this picture.

Make your fixes
***************
Once you've clicked the fork button, you're ready to make your update in the
web editor.

   TODO: Add a picture of the web editor.

Go to line 11 and fix the spelling error.

While we're here let's also highlight some text we want to emphasize on this
page. You can bold text by adding ``**`` before and after the text you want to bold.
Go ahead and do that now around the sentence ``Small changes add up!``

It should end up looking something like::

    I really want to emphasize the following: **Small changes add up!**

The format that the documentation is using is called reStructuredText or RST for
short.  If you want to learn more about what RST can do, check out the RST Quick
Reference :doc:`../references/quick_reference_rst`


Save your changes
*****************

Now that you've made the change, let's add some notes about the change and
get it ready for review by a project maintainer.

To help the maintainers review the change, let's add a small description that
gives them context about what we changed and why.

   TODO: Picture of the propose changes section with a useful comment.

Once you've added a description, go ahead and hit the :guilabel:`Propose Changes`
button. This will save your changes to your fork and allow you to make a pull
request that (more on that shortly.)

   TODO: Picture with button highlighted.

Making a pull request
*********************

The next page will give you a chance to review your changes before you ask
others to do the same.

By making a pull request you will notify the maintainers about the change
and officially request that they review the changes and accept them.

Go ahead and hit the :guilabel:`Create Pull Request` button.  This will bring
up a form which you don't need to make any changes in for now.

   TODO A picture of the form.

Click the ``Create pull request`` button again.

   TODO A picture for after you click the button.


Congratulations, you have made a new pull request for a change against the
Open edX documentation!

   TODO: Celebration Picture

Because this was a practice PR, it will be closed without the changes being
accepted.  This is so others can continue to go through the same quickstart.

However for any real changes you make in the future, you can expect that the
reviewers will review your changes and may ask for changes or accept your
changes as is and merge them.

.. note::
   .. include:: ../how-tos/reusable_content/sign_agreement.txt

If you need more help with the future, check out the getting help section of
the documentation.

   TODO Link to the getting help section once that exists.

