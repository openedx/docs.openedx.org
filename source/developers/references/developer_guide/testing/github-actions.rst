GitHub Actions
##############

This page explains GitHub Actions, how we use them in the Open edX project, and
some tips on troubleshooting.

What Is GitHub Actions?
***********************

`GitHub Actions`_ is a continuous integration and continuous delivery (CI/CD)
platform that allows you to automate your build, test, and deployment pipeline.
You can create workflows that build and test every pull request to your
repository, or deploy merged pull requests to production.

GitHub Actions goes beyond just DevOps and lets you run workflows when other
events happen in your repository. For example, you can run a workflow to
automatically add the appropriate labels whenever someone creates a new issue in
your repository.

How Does the Open edX Project Use Them?
***************************************

The Open edX project uses Actions to automate test builds on pull requests, as
well as to create other types of automations beyond testing. Once such workflow
is the `fix Transifex resource names`_ workflow in the openedx-translation repo.
hat runs every time the ``transifex.yml`` or ``extract-translation-source-files.yml``
files are updated on the main branch, on `workflow dispatch`_ (when triggered
manually), and on the first of every month. We also use Actions to ensure
everyone is covered by a CLA, to allow anyone to assign an Issue to themselves
by commenting ``assign me`` in a comment, linting commit messages, ensuring our
requirements are up to date, and in many other creative ways.

You can check out the workflows available to all Open edX repositories in the
`.github repo`_; many repos define their own workflows in their
``.github/workflows`` directory.

Understanding and Troubleshooting Builds
****************************************

A "build" is a name for a collection of GitHub actions that run on a single
commit. These "builds" typically consist of multiple GitHub actions: one or more
test runners, a CLA check, commitlint, possibly a ReadTheDocs build for repos
with documentation, and various other types depending on the repo's purpose and
primary language.

Reading Build Statuses
======================

At the bottom of your pull request, there will be one or more builds run and a
widget that displays the status of the run:

.. image:: /_images/devguide_pr_build.png

Clicking the "Details" link on the right of each build will give you some more
context as to why it failed.

If the "openedx/cla" check fails, you'll need to either sign the `Open edX CLA`_
or have your employer add you to their entity CLA agreement. Please talk to your
employer for guidance if you're unsure.

If the "Lint Commit Messages" check fails, you need to rewrite your commit
message using Conventional Commits (see :doc:`openedx-proposals:best-practices/oep-0051-bp-conventional-commits`).

Failed Builds
=============

Click on an individual failed Action (red X) to be brought to the build page.

Kicking Off Builds
==================

Actions run automatically on a pull request when a new commit is pushed to the
branch, or the branch is rebased. Sometimes Actions get stuck (a yellow circle
that never goes away) or fail when you think it should pass - in this case, you
have a few options:

* If possible, rebase the branch atop master/main and force-push to generate a
  new build

* If you have permissions, you can visit the build page for a failed build and
  click the "Re-run jobs" button in the top right corner

  .. image:: /_images/devguide_rerun_actions.png

* Push an empty commit to trigger a new build (but rebase it away before merging)::

   git commit --allow-empty -m "Empty-Commit"

* Try closing and re-opening the pull request to trigger a new build.

Please do not close your PR and open a new one in an attempt to get a build to
pass, unless asked to do so. This removes a lot of history from the new PR,
making it challenging to understand the previous review history and requested
changes.


.. _GitHub Actions: https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions
.. _.github repo: https://github.com/openedx/.github/tree/master/.github/workflows
.. _fix Transifex resource names: https://github.com/openedx/openedx-translations/blob/main/.github/workflows/fix-transifex-resource-names.yml
.. _workflow dispatch: https://github.com/openedx/openedx-translations/blob/cf313a06ebf8c3a792e67174dfcba7607da2d61f/.github/workflows/fix-transifex-resource-names.yml#L5-L13
.. include:: /links.txt