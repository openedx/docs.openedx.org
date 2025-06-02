.. _Git workflow:

Open edX Git Workflows
######################

The Open edX project is available on GitHub, which uses the Git system for version control.

When contributing to a new repo, contributors should use a `personal fork <Using
A Personal Fork>`_, follow
:doc:`openedx-proposals:best-practices/oep-0051-bp-conventional-commits`, squash
changes into logical commits, and rebase branches before requesting reviews.
This page will describe how to do all of these things!

Once you've set up your flow, follow the instructions on :ref:`Landing Your Work`.

.. _Using A Personal Fork:

Using A Personal Fork
*********************

Personal forks are a standard open source tool for making pull requests against
repos where you don't have write access.  It's a little more complicated than
working directly in the repo, but it's not difficult.

There are many Git tools, and styles of working. These instructions focus on the
Git command line tool (``git``).  There are other ways to accomplish the same workflow,
including more GitHub GUI-centered, or the gh GitHub command-line tool. We
welcome improvements to this page.

Terminology
===========

**Fork**: on GitHub, a fork is a copy of a repo in your own account so
that you have write permissions to push commits and branches to it.  This is
different than the broader open source term of forking a project because of a
disagreement about direction.  We are talking about the gentle GitHub term, not
the aggressive governance term.

**Upstream**: the repo you are ultimately contributing to.  In our world, this is
likely in the ``openedx`` GitHub organization.

**Remote**: a server copy of a repo.  A local repo on your machine can have a number
of different remotes, and pull from them separately.  Each remote has a name and
a URL.  The default remote is called "origin". You can see your remotes' names
and URLs with ``git remote -v``.

The Ideal State 
================
You will have a local repo with two remotes: "origin" will point
to your fork in your account, and "upstream" will point to the repo in the
openedx org.  Very briefly, the normal flow will be:

#. Pull from the upstream into your fork to get the latest code.

#. Make a feature branch in your repo.

#. Make your changes, and commit them.

#. Push your branch to your fork (origin).

#. Make a pull request against upstream.

Once the review is complete, the owning team will approve and merge the pull
request.

Creating a fork
================

Creating a fork is easy:

#. Visit the repo on GitHub.

#. In the upper-right corner is a Fork button. Click it:

   .. image:: /_images/developers_references/gh_fork_button.png
       :alt: The "Fork" button at the top right of the screen

#. On the next screen, you'll be asked to choose which GitHub account the repository should be forked to — this is shown as the Owner field.
   Choose your own personal account (the default choice):

   .. image:: /_images/developers_references/gh_new_fork_screen.png
       :alt: The screen allowing you to pick which GitHub account to fork to

#. If you have permissions to fork into your company's organization, you should
   check carefully with your process owners to see if you should.

   * The downsides to forking into your organization:

     * Now there will appear to be two sources of truth: ``openedx/repo`` and
       ``myorg/repo``.  Developers will have to be careful about which to clone,
       and which to merge into.
     * There's now a shared task of keeping the two repos in sync.

Getting the fork locally
=========================

How you get the fork locally depends on whether you already have a local repo
copy that you want to keep.  If you have a local copy but don't need it, you can
delete the repo directory and use the "I do not have a local copy" section below.

I do not have a local copy
--------------------------

#. Clone the repo locally: ``git clone https://github.com/USER/REPO.git``

#. Change to the new repo directory: ``cd REPO``

#. Add a new remote for upstream: ``git remote add upstream https://github.com/openedx/REPO.git``

I have a local copy I want to keep
-------------------------------------

.. warning::

   The rename will change the remote of all your branches to upstream, which is
   not what you want. So, it is probably best to complete your work, remove
   the old copy, and then follow the steps in "I do not have a local copy."

#. Rename the existing remote:

   * Use ``git remote -v`` to check that the openedx repo is named "origin"
   * Rename the remote to "upstream": ``git remote rename origin upstream``.

#. Add a new remote for your fork: ``git remote add origin https://github.com/USER/REPO.git``

.. _sync fork:

Keeping your fork up to date
=============================

You now have two remotes: your fork called ``origin`` and the openedx core repo
called ``upstream``.  Before beginning work on a change, you will want to get the
latest code from upstream into your fork.  Keep in mind that some repos use a
``master`` branch, others use ``main``.

One simple way to keep your fork up to date is to visit the GitHub page for your
fork (``https://github.com/MYUSERNAME/REPO``) and click the "Sync Fork" button.
Then locally, you can pull down the changes on the ``master`` or ``main`` branch.

To do this via the command line follow these instruction. If you are in a ``main``
repo, replace ``master`` with ``main``:

#. Switch the current branch to master: ``git switch master``.

#. Pull down the changes from upstream and update your master branch: ``git pull upstream master --ff-only``

#. If everything has been done right, this will be a fast-forward merge, with no
   explicit merge commit.  You shouldn't have changes on your master, but if you
   do, the ``git pull`` command will fail with "fatal: Not possible to
   fast-forward, aborting."  If this happens, you will need to fix your master
   branch before continuing. One way is to make a branch off your master branch
   with your changes, then switch back to the master branch and remove your
   commits with an interactive rebase or by using ``git reset --hard <commit>``.

#. Push the changes to your fork to keep it up to date: ``git push``.

Now your master branch is in sync with upstream, both locally and in your fork
on GitHub.

Making a pull request
======================

Making a pull request is very similar to the simple one-remote workflow:

#. Create a branch locally: ``git switch -c user/description``.

#. Make your changes and commit them.

#. Push your branch to your fork: ``git push -u origin @`` (``@`` is shorthand for ``HEAD``, i.e., your current branch).

#. Make a pull request on GitHub.  The base repository should automatically
   choose the upstream repo.

#. Review and work on the pull request as usual.  You can push new commits to
   your branch as usual.

#. Ask the owning team to approve and merge your pull request.

Once your code has been merged, the steps in "Keeping your fork up to date" will
get you ready for the next iteration of work.  You can also use those steps if
you need to rebase your pull request to base it on the latest changes on master.

.. _Squashing Changes:

Squashing Changes
*****************

When merging commits to upstream ``master`` and ``main`` branches, we prefer
tidiness over historical accuracy. In other words, we would prefer that you
merge in a small number of well-documented, individually-coherent commits rather
than a large number of commits that detail all your intermediate development
states and bugfixes. We achieve this via *squashing*, which means combining
multiple git commits into a single commit with the same cumulative changeset.

As a PR author, you can help us keep the upstream git history tidy in two ways:

* Before submitting your PR for review, perform an `interactive rebase`_, and
  squash away any commits which will not be useful to other developers.
* During your PR review, as you edit your code in response to feedback, name
  your new commits using the special git `squash! <https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-code--squashltcommitgtcode>`_ or `fixup! <https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-code--fixupamendrewordltcommitgtcode>`_ prefixes. This will indicate to the
  repository's core contributors that these commits should be squashed away as
  part of the final merge to ``main`` or ``master``. It will also allow the core contributors to auto-squash your commits more easily.

As a core contributor, when you are ready to merge a PR, take a look at the
commit log. How many commits are there to merge *excluding* ones that need to be
squashed away? If there is only one non-squashable commit, then you can simply
press the "Squash and Merge" button, which will open a visual interface
allowing you to squash all the commits into one (but please edit the message to
something useful rather than using the default one). If there are multiple
non-squashable commits, then you can pull the branch down and perform an
`interactive rebase`_ to revise the commit list. You'll then need to force-push
and select "Rebase and Merge" on GitHub.

.. _interactive rebase: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History

See also the `git-scm book section on squashing changes
<https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#_squashing>`_.

.. _Rebasing:

Rebasing Your Branch
********************

It is best practice to *rebase* your branch atop a repo's ``main`` or ``master``
branches before requesting a review. This ensures your branch is up to date with
the repo's latest changes, preventing conflicts.

.. admonition:: Heads Up!

   It is strongly recommended to :ref:`squash your changes <Squashing Changes>`
   before rebasing. Otherwise, you may end up having to resolve similar
   conflicts over and over.

Rebasing can be complicated, but the happy-path is as follows:

#. Switch to the ``master`` or ``main`` branch of the repo, and :ref:`sync upstream changes <sync fork>`.

#. Switch back to your working branch.

#. Run the rebase command: ``git rebase master`` or ``git rebase main``

#. If there are no conflicts, you will see your branch rebased successfully. You'll now need to force-push your changes: ``git push -f`` or ``git push --force-with-lease``.

If there are conflicts, the rebase will stop on the conflicting commit and wait
for you to `resolve the conflict
<https://docs.github.com/en/get-started/using-git/resolving-merge-conflicts-after-a-git-rebase>`_.
Once the conflict is resolved, you can continue the rebase with ``git rebase
--continue``.

See the `git-scm book section on rebasing
<https://git-scm.com/book/en/v2/Git-Branching-Rebasing>`_ for more technical
details on rebasing.

Further Git Resources
**********************

The Open edX community has found the following resources helpful in their
journey to becoming Git experts:

* `An interactive way of understanding branching and rebasing <https://learngitbranching.js.org/>`_
* `A technical git tutorial <https://www.cduan.com/technical/git/>`_
* `A user reference for git <https://git-scm.com/book/en/v2>`_
* `GitHub Standard Fork and PR Workflow <https://gist.github.com/Chaser324/ce0505fbed06b947d962>`_.
* `Working with Forks <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks>`_.