######################################################
Overview of Review Process for Community Contributions
######################################################

Community contributions, in the form of pull requests, go through a process
shepherded by the `Community Contribution Project Managers`_. These
contributions are sometimes referred to as "OSPRs" (open source pull requests).

See the :doc:`pull-request-statuses` if you're looking for more information about
what the various statuses and labels of your pull request (PR) mean.

.. contents::
 :local:
 :depth: 1

=======================================
Community Contribution Project Managers
=======================================

The main goal of the `Community Contribution Project Managers`_ is to triage all
pull requests that come in from contributors across the community, and help
those PRs get through to being merged. During the triage and review process, the
Community PMs are responsible for:

* Welcoming new contributors to the community

* Triaging community pull requests in a timely manner

* For new contributors, ensuring they submit a CLA form (if contributing as an
  individual), or get added to their organization's entity agreement (if
  contributing on behalf of their organization)

* Ensuring the correct amount of detail is provided for the requested change(s)
  (e.g. if there is not context or description for your contribution, we'll ask
  you to provide one)

* Making sure checks are able to run on the pull request

* Routing pull requests to the appropriate reviewers / `maintainers`_, and
  making sure they're addressed in a timely manner

* Connecting contributors with the appropriate people if troubleshooting is
  needed, or if there are technical questions

* Helping to get the pull request merged once everything is approved

At a high level, the pull request process is as follows:

#. Initial triage on a new pull request is done by the Community PMs within a few days

   #. Note: some pull requests require review by our Product team. Please see
      :doc:`contributor` for requirements needed for the Product team to
      properly review your contribution. Ideally, this would be done before code
      is written.

#. If checks need to be enabled, or a CLA form needs to be submitted, the
   Community PMs will help get checks running and help with any questions
   regarding the CLA

   .. image:: /_images/devguide_workflow_approval.png

   .. image:: /_images/devguide_failed_cla_check.png

#. If there are checks failing on your pull request, you'll need to look into
   what's causing the issue. The Community PM can direct you to someone to help
   if needed.

   #. Note: please see :doc:`../../running_pr_tests` that outlines common issues
      that pop up while running tests

#. Once everything is up and running, the Community PMs are available to help
   with any questions that come up while product and/or engineering review is
   in-progress

#. If the pull request review process takes a bit longer than expected, you may
   notice the following alerts pop up, and the Community Project Managers might
   ask you to take some action:

   #. **“This branch is out-of-date with the base branch”** which means you'll
      need to rebase your changes.

      .. image:: /_images/devguide_out_of_date_branch.png

   #. **“This branch has conflicts that must be resolved”** which means someone
      has changed information in the same file on the target branch of the PR
      (which is usually the master). You will need to reconcile those changes
      with your own.

      .. image:: /_images/devguide_branch_conflicts.png

#. When all checks are green, tests are passing, there are no conflicts, and the
   work is ready for engineering review, the Community PMs will assign the
   appropriate reviewer / maintainer to take a look

   .. image:: /_images/devguide_passing_checks.png

#. During review, you may receive feedback or change requests that require
   action on your part.

#. Once all feedback and changes have been incorporated, the pull request will
   be able to be merged by the reviewer / maintainer.

As pull requests move through the process, the Community Project Managers update
the PR's status, and use labels to denote different aspects / states of the PR.
This helps reviewers better understand what action(s) are needed, and by who.

A breakdown of these statuses and labels can be found at the
:doc:`pull-request-statuses` for reference (though, PR authors are not
responsible for updating PR status or labels).

On the right-hand side of the PR, you'll be able to see the status of your pull
request, the Community PM responsible for the PR, and the last date the
Community PM checked in on it. To do this, find the "Projects" section, and
click on the "⌄" caret in the top right corner next to "Contributions" to see a
display like this:

.. image:: /_images/devguide_pr_status.png

============================
FAQs about your Pull Request
============================

**My pull request has been waiting for review for a few weeks, is something
wrong?**

No! We receive hundreds of pull requests from the community (which is awesome!),
but that means sometimes the process to get PRs through the review process and
merged might take a bit of time due to things like:

* The reviewing team is at capacity and needs to review the pull request during a later sprint
* Related work or dependencies may be blocking a PR's ability to be merged

The Community PMs will do our best to make sure all updates related to delays
are communicated within the PR. Additionally, if the reviewing team needs
additional information or context for your contribution, they will ask within
the PR.

**There haven't been any updates in my PR in a few weeks. How do you handle
stalled PRs?**

The Community Project Managers proactively stay on top of pull requests, and
will ping reviewers for updates, actions, etc. when things seem stalled. If you
have any questions, you can tag the assigned Community PM for help / updates in
the PR at any time.

**I submitted a PR a while ago, something came up, and I am not able to work on
it for the foreseeable future. What happens now?**

If a PR is stalled on the author's side, the Community PMs will ping the author
a few times before labeling the PR as “inactive” after a month or so.

* If you want to pursue the PR, but don't have capacity at the moment, please
  let us know directly in the PR if possible. At that point we can leave it as a
  draft, or we can close it if needed, and can reopen it at a later time if
  you're able to pursue it.
* If an author is unresponsive for a month or more, or hasn't had capacity to
  come back to check on the PR, the Community PMs may need to close the PR due
  to inactivity (though, again, it can be reopened at a later time if needed).

**My PR was labeled as “blocked” - what does that mean?**

Occasionally, a pull request may get blocked by other on-going or related work.
The Community PMs will stay on top of it to make sure it gets unblocked as soon
as possible, but note that it may take a bit depending on what's blocking it.
Updates from the Community PMs and reviewing team should be made in the PR so
you have updated information.

**My PR was closed and not merged - why?**

There may be times where a pull request is closed (instead of merged) by an
owning team because the update may no longer be needed, it's duplicative of
other work, or other reasons. The reason for closing the pull request should be
made clear to you in the PR, and if it's not, the Community PM assigned to your
pull request can help you get that information.



.. _Community Contribution Project Managers: https://openedx.atlassian.net/wiki/spaces/COMM/pages/3548807177/Community+Contributions+Project+Manager
.. _maintainers: https://openedx.atlassian.net/wiki/spaces/COMM/pages/3426844690/Maintainership+Pilot


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
