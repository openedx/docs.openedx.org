Quick Start: First Documentation PR
###################################

.. sidebar:: First Docs PR Walkthrough

   |Video Sidebar Click|

   Video Will be Added Soon!

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


Fork the repository (repo)
**************************

If you have never made a pull request to this repo, you'll be asked to fork the
repo.  A "fork" is essentially your own copy of the repository.

Go ahead and click the big green button!

.. image:: /_images/documentors_quickstart_first_pr/fork_this_repository.png
   :alt: A screenshot of the github page for forking a repository. With the "Fork this Repository" button highlighted.

Make your fixes
***************

Once you've clicked the fork button, you're ready to make your update in the
web editor.

.. image:: /_images/documentors_quickstart_first_pr/github_rst_editor.png
   :alt: A screenshot of the github editor with the contents of the doc_with_errors.rst file.

Go to line 11 and fix the spelling error.

While we're here let's also highlight some text we want to emphasize on this
page. You can bold text by adding ``**`` before and after the text you want to bold.
Go ahead and do that now around the sentence ``Small changes add up!``

It should end up looking something like::

    I really want to emphasize the following: **Small changes add up!**

The format that the documentation is using is called reStructuredText or RST for
short.  If you want to learn more about what RST can do, check out the RST Quick
Reference :doc:`../references/quick_reference_rst`


Preview your changes
********************

Click on the "Preview" tab to see what your changes look like. You can click this tab whenever
you want to take a look at your work.

.. image:: /_images/documentors_quickstart_first_pr/preview_rst.png
   :alt: A screenshot of the GitHub RST visual preview.

.. note::

   The GitHub "Preview" tab will not always show, or *render*, everything perfectly.
   As you can see, both the "Note" box and the part that starts with ``:doc:``, which
   display correctly on docs.openedx.org, do not render correctly in the GitHub preview.

   Solutions to this problem are to install a local development environment (How-To
   article TBD), or rely on the "pull request build", discussed below.


Save your changes
*****************

Now that you've made the change, scroll down and add some notes about the change
and get it ready for review by a project maintainer.

To help the maintainers review the change, let's add a small description that
gives them context about what we changed and why.

.. image:: /_images/documentors_quickstart_first_pr/propose_change_with_a_comment.png
   :alt: A screenshot of the "Propose Changes" form with the suggested text. The
         subject is the same but the description has two bullet items to indicate that
         we've fixed the spelling and have emphasized some text.

Once you've added a description, go ahead and hit the :guilabel:`Propose Changes`
button. This will save your changes to your fork and allow you to make a pull
request that (more on that shortly.)

.. image:: /_images/documentors_quickstart_first_pr/propose_change_highlight_button.png
   :alt: A screenshot of the "Propose Changes" form with the "Propose changes"
         button highlighted.

Making a pull request
*********************

The next page will give you a chance to review your changes before you ask
others to do the same.

By making a pull request you will notify the maintainers about the change
and officially request that they review the changes and accept them.

Go ahead and hit the :guilabel:`Create Pull Request` button.

.. image:: /_images/documentors_quickstart_first_pr/create_pull_request_first_button.png
   :alt: A screenshot of the github page comparing changes with the "Create pull
         request" button highlighted.

This will bring up a form which you don't need to make any changes in for now.

.. image:: /_images/documentors_quickstart_first_pr/create_pull_request_first_button.png
   :alt: A screenshot of the github PR form with the "Create pull request" button highlighted.

Click the ``Create pull request`` button again and you will have a published
Pull request!

.. image:: /_images/documentors_quickstart_first_pr/published_pr.png
   :alt: A screenshot of a submitted github PR.

Congratulations, you have made a new pull request for a change against the
Open edX documentation!

.. image:: /_images/animated_confetti.gif
   :alt: Animated confetti.
   :target: https://commons.wikimedia.org/wiki/File:Wikipedia20_animated_Confetti.gif

Because this was a practice PR, it will be closed without the changes being
accepted.  This is so others can continue to go through the same quickstart.

However for any real changes you make in the future, you can expect that the
reviewers will review your changes and may ask for changes or accept your
changes as is and merge them.


Viewing the pull request build
******************************

As mentioned above, sometimes you can't use the Preview to see everything rendering properly.
Thus, you can use the *build* on your pull request. At the bottom of your pull request, there
is a section that show you the checks on your pull request. If the Docs build is successful,
you'll see it with a green checkmark:

.. image:: /_images/documentors_quickstart_first_pr/green_docs_build.png
   :alt: A picture of the GitHub user interface showing a successful build has a green checkmark

If you click the "Details" link, you'll be brought to this page:

.. image:: /_images/documentors_quickstart_first_pr/readthedocs_build_page.png
   :alt: The page that shows the build artifacts on the Read the Docs website

Click the "View docs" link, *NOT* the button, to see the build - that is, the set of documentation
generated by your changes.

You'll be brought to a site that looks exactly like docs.openedx.org, but you'll see the URL looks
different and a warning box shows. This is a special site made just for your changes! Navigate to
page(s) you've changed to double-check your changes look right.

.. image:: /_images/documentors_quickstart_first_pr/pr_generated_page.png
   :alt: A version of the docs.openedx.org page updated with our changes, visible at a unique URL.

.. note::
   .. include:: ../how-tos/reusable_content/sign_agreement.txt

If you need more help or run into issues, check out the :doc:`/other/getting_help`
section of the documentation for links to some places where you could get help.

