**************
GitHub Actions
**************

`GitHub Actions`_ is a continuous integration and continuous delivery (CI/CD)
platform that allows you to automate your build, test, and deployment pipeline.
You can create workflows that build and test every pull request to your
repository, or deploy merged pull requests to production.

The Open edX project uses Actions to automate test builds on pull requests, as
well as to create other types of automations. You can check out the workflows
available to all Open edX repositories in the `.github repo`_; many repos define
their own workflows in their ``.github/workflows`` directory.

Reading Builds
==============

At the bottom of your pull request, there will be one or more builds run and a
widget that displays the status of the run:

.. image:: /_images/devguide_pr_build.png

Clicking the "Details" link on the right of each build will give you some more
context as to why it failed.

If the "openedx/cla" check fails, you'll need to either sign the `Open edX CLA`_
or have your employer add you to their entity CLA agreement. Please talk to your
employer for guidance if you're unsure.

If the "Lint Commit Messages" check fails, you need to rewrite your commit
message using `Conventional Commits`_.

Failed Builds
=============

Click on the build to be brought to the build page.

Kicking Off Builds
==================

Actions run automatically on a pull request when a new commit is pushed to the
branch, or the branch is rebased. Sometimes Actions get stuck or fail when you
think it should pass - in this case, you have a few options:

* If possible, rebase the branch atop master/main and force-push to generate a
  new build

* If you have permissions, you can visit the build page for a failed build and
  click the "Re-run jobs" button in the top right corner

  .. image:: /_images/devguide_rerun_actions.png

* Try closing and re-opening the pull request to trigger a new build.

* Push an empty commit to trigger a new build (but rebase it away before merging)::

   git commit --allow-empty -m "Empty-Commit"



.. _GitHub Actions: https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions
.. _.github repo: https://github.com/openedx/.github/tree/master/.github/workflows
.. include:: ../links.rst