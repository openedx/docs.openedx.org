How To Get Ready for Python Development
#######################################

.. How-tos should have a short introduction sentence that captures the user's goal and introduces the steps.

This how-to will help prepare your local system to start developing on a Python-based repository that is part of the Open edX Platform.

Assumptions
***********

.. This section should contain a bulleted list of assumptions you have of the
   person who is following the How-to.  The assumptions may link to other
   how-tos if possible.

* You have Git installed
* You have Python 3.8 installed

Steps
*****

.. note::

   These instructions will not work in all repositories. If they do not, check the repo's README for a Getting Started section for possible alternative instructions.

First-Time Setup
================

First, fork the repository, and then clone the forked repository with ``git clone <git_url>``. It's best to place all of your Open edX repositories in the same parent directory as each other, as a few of them assume that they will be arranged this way. (If you're not using devstack, this may not matter.)

After navigating to the new directory in your shell, you'll need to set up a virtualenv and install requirements.

A virtualenv contains a copy of your repo's Python dependencies. This avoids dependency version conflicts with your system packages and other repos.

The most basic way of creating a virtualenv is to use the builtin ``venv`` module in Python::

  python3.8 -m venv .venv

This example creates a virtualenv at ``./.venv/``. Each time you will be working with Python in the repo, you'll need to activate the virtualenv for that terminal session::

  source .venv/bin/activate

Once you have done this, any calls to ``python``, ``pip``, or other Python executables will refer to the ones managed by the virtualenv.

.. note::

   If you create virtualenvs inside repos, you'll need to tell git to ignore them. The easiest way to do this is to create a file called ``.gitignore-global`` in your home directory and add the line ``.venv/``. Alternatively, you can create the virtualenvs elsewhere in your filesystem.

.. note::

   Many developers use wrapper scripts (or write their own using shell aliases). One commonly used tool is `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/stable/>`_, which manages the virtualenv directories outside of repositories; this avoids several issues with git and other tools being able to see the virtualenv, but will require explicitly naming each virtualenv.

Working on a Repo
=================

#. Make sure you are on the default branch and have the latest version of the code::

     git checkout main
     git pull

   Some repos instead have ``master`` as their default branch.

#. Activate your virtualenv, as described above.
#. Install or update the Python requirements for the repo into your virtualenv::

     make requirements

   In a few repos, this might also install NodeJS requirements, or the Makefile target might have a different name.

#. Optionally, ensure you can run tests::

     make test

   Depending on the repository this might run not just unit tests, but also linters and other quality checks. The Makefile may also define ``make quality`` for code quality checks, or even a comprehensive ``test-all`` target.

#. Make a branch for your changes::

     git switch -c <your_github_username>/<short_descriptive_label>

#. As you change code and add tests, you can use ``make test`` to check if tests are still passing.
#. Run ``make test`` one more time and commit your changes with ``git add`` and ``git commit``. Follow the `conventional commits`_ documentation. Make sure your commit message is informative and describes why the change is being made. While the first line of the message should be terse, the body of the message has plenty of room for details.
#. Push your changes to GitHub with ``git push``.
#. In GitHub, open a pull request (PR). In the PR description, include anything that could help reviewers understand and test your change.

.. _conventional commits: https://open-edx-proposals.readthedocs.io/en/latest/best-practices/oep-0051-bp-conventional-commits.html
