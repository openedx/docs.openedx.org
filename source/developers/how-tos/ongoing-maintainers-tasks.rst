Ongoing Maintainer's Tasks
##########################

..
  Much of the TBD content in this document should be answered when we come
  to consensus on https://openedx.atlassian.net/wiki/spaces/COMM/pages/3545726977/Maintainer+Outstanding+Questions+9+14+meeting


This How-to will explain the ongoing tasks that Maintainers are expected to
perform, once their repositories are up to Open edX project standards (see
:doc:`maintain-a-repo`). These actions are performed **periodically** - some more
frequently than others - and are done to ensure your repository is consistently
up to date with the latest security fixes and the rest of the project's codebase.
Additionally, maintainers have a responsibility to the community to develop
transparently, respond to requests for help, and respond to proposals/PRs for
changes to the codebase.

To learn more about the Maintainer's Program, see `OEP-55`_.

.. _OEP-55: https://open-edx-proposals.readthedocs.io/en/latest/processes/oep-0055-proc-project-maintainers.html


Assumptions
***********

This How-to assumes the following:

* You are a repository maintainer.

* You have followed the instructions in :doc:`maintain-a-repo` to get your repo's
  documentation and tooling in alignment with the standards of the project.

Hold Yourself to Community Standards
************************************

A prerequisite for a Maintainer is to be a Core Contributor.  Part of what this
means is that you must hold yourself to the same standards as any CC - any
contributor, really - in your repository.  You are still a member of the
community, after all!

Here are a few rules-of-thumb to keep in mind:

* Participate!  Make yourself available in the several community communication
  channels - the `Open edX discussion forums`_, `Slack`_, `working group meetings`_,
  and, of course, `Github issues`_ - to discuss matters related to your
  maintenance role publicly.  Don't restrict yourself to private conversation
  channels: this would make for an opaque project.

.. _Open edX discussion forums: https://discuss.openedx.org/

.. _Slack: https://openedx.slack.com/

.. _working group meetings: https://openedx.atlassian.net/wiki/spaces/COMM/pages/3707371565/Active+Working+Groups#Joining-Working-Group-Meetings

.. _GitHub issues: https://github.com/openedx

* Treat any change you or your organization want to make to the codebase as an
  open source contribution.  This means that any and all PRs must be properly
  reviewed by somebody other than the submitter.  And if the change is
  user-facing, it must necessarily undergo the public `Product Review Process`_.


.. important::

   Adding a feature toggle around a piece of code does not exempt it from being
   put through the Product Review Process!  Even experiments must be approved
   beforehand, for even if a feature is not shown by default, the code that
   builds it must still be dealt with by the community as part of the
   maintenance, testing, and release processes.

* Please do not use the main branch as a way to debug your deployments.
  Commits to ``main`` or ``master`` should not contain debugging code unless
  there's value in it staying there permanently (in which case it would likely
  have to sit behind a runtime ``DEBUG`` toggle).

* Your own PRs should have full descriptions, including testing instructions
  and screenshots: anybody should be able to understand not only the How, but
  the Why.  Descriptions consisting solely of a link to a private page are a
  big no-no! Hint: Try viewing your link in an incognito browser to see if it
  is publicly available.

* Just because you've been entrusted with write access doesn't mean you should
  use the repository as you would a personal one:

  * Always consult the community with respect to important changes.  Possibly
    even small ones!  When in doubt, go public.

  * Unless there's communal value in creating a new public git branch (such as
    feature branches, for instance), you should prefer to create PR branches on
    personal or organizational Github forks.  It is just as easy to issue PRs
    from them, and it avoids branch pollution in the main repository.  Plus,
    it's what regular community members have to do to contribute: it's an
    opportunity to lead by example!

* If the repository you maintain is an official part of the Open edX release,
  make sure any and all incoming changes are developed with the next one in
  mind.  In other words, even if they come from your own team, and even if your
  organization's deployment method is far from standard, PRs must, among other
  things:

  * Work with the current officially recommended installation method, which at
    the time of writing is `Tutor`_;

  * Not contain strings that are not properly internationalized;

  * Not contain code, strings, variable names, or feature flags that are
    organization- or site-specific.

.. note::

   Changes to MFEs must futher conform to the `Requirements for an MFE`_ as
   established by the Build Test Release Working Group.  Failing to do so would
   make the MFE in question ineligible for release.

.. _Requirements for an MFE: https://openedx.atlassian.net/wiki/spaces/COMM/pages/3561521275/Requirements+for+an+MFE

GitHub Notifications
********************

GitHub provides a lot of individual control over how you receive notifications when you or teams you are on are mentioned in issues or pull requests on Github.com

You can learn more about how to configure your notifications settings on `GitHub's notifications documentation`_

.. note::

   Expectations for how quickly you respond to issues or pull requests are detailed in the sections below.


.. _GitHub's notifications documentation: https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications

Responding to Issues
********************

Issues may come in the form of bug reports or feature requests. In any case, the issues should be **"triaged" within a week of receipt**.  This does not mean agreeing to the request in the issue or fixing it, but simply acknowledging it and scheduling time to respond to the requests in a timely manner.  Sometimes the issues will require further discussion but if you see issues that you are unlikely to resolve, it is better to provide that feedback quickly rather than leaving the issue open and unanswered.

Responding to PRs
*****************

Our goal for PR response time is that they are **"triaged" within a week of receipt**. This does not mean that review happens within a week, but that the PR is acknowledged and scheduled for review in line with the maintainer's other priorities.  This response time goal is ongoing.  So when an author responds to feedback, the goal is the same.

One of the scarcest resources of an open-source project is contributor and maintainer time.  It is ideal that once a review starts, that it can be finalized as a single piece of work, say within the boundaries of a single sprint.

As a maintainer, your goal should be keeping the time to review and finalize a PR as predictable and as short as is reasonable.  Finalizing a PR can mean rejecting it. For a contributor, knowing that a PR won't be accepted and why provides them appropriate feedback and lets them decide what to do next.

If your team schedules reviews for future sprints, providing that information to the author is helpful to set their expectations and plan accordingly. Leave a comment indicating when you expect the review to occur and ensure that the status on the contributions board is "Scheduled for Eng Review."

When reviewing a PR, we want to focus on reducing the back-and-forth that increases lead time.  In our globally distributed project, a comment and response cycle can easily take 24 hours.  Ideally, both contributor and reviewer can both focus their attention on finalizing a PR at the same time.

It is recommended that reviewers approve the GitHub actions if approval is required.  GitHub requires approval from new contributors to any repository, so even folks who have contributed to the project, but not the particular repository, require approval.

When GitHub detects that the PR branch is out of date with the base, it is recommended that the reviewer update the branch using a merge commit.  This keeps the history clear and reduces days of lead time over pushing this back to the original author.  However, reviewers may ask authors to resolve any conflicts between their branch and the base.

Managing Upgrade PRs
********************

As a part of bringing your repository into alignment with the standards of the project, you have setup automation that will create new PRs when packages you depend on have newer versions available.

Keeping your dependencies up-to-date on a regular basis is both lest costly and more secure than waiting a long time between package updates.  It is recommended that you **apply all security fix on packages you depend on within weekly**.  For automated PRs that don't contain security updates to dependent packages it is still recommended that you triage them on a weekly basis. Schedule any complex upgrades in a timely manner - you don't want to be in a situation where it becomes an emergency to land them (whether to get new features or apply a major security fix).

Approving GitHub Actions for new committer PRs
**********************************************

.. note::

   This process is only for contributors that already have passed the CLA check, for those that haven’t please follow the normal process for helping the contributor onboard.

When a user opens their first PR in a repository you maintain it is likely that they will need to be approved before some Github Actions, such as tests, will run. This is to protect us all from having malicious code run in our account as part of our test suite.

When this occurs the orange “Approve and run“ will appear for the PR.

The current process for this is to:

1. Look over the PR to make sure that it is legitimate and there are no malicious changes.

   a. In the event of a questionable or malicious looking change, please notify #maintainers-pilot in Slack to warn other maintainers and allow us to take appropriate action.

2. Any maintainer or Axim employee with write permissions on the repository can approve the PR after step 1 has been completed. This should only need to be done once per contributor per repository.

3. Once the PR is unblocked, the rest of the approval process should work as normal.

Participating in Forum Discussions
**********************************

As a maintainer you are expected to participate in the `Open edX discussion forums`_  The discussion forums use `Discourse <https://discourse.org>`_ under the hood and you can fine a lot more information about how discourse notifications work in their `Notifications Primer`_

Discourse allows you a **lot** of control over which categories and sub-categories you actually get notified about.  We recommend that you make use of this to only subscribe to the categories that are relevant to your work as well as any posts that mention you directly.


.. tip::

   You can reduce noise by simply watching categories for the "first-post" so you are notified of all new topics (Discourse's term for threads).

   If a topic interests you, you can always go to the link provided in the notification to subscribe to all future updates to that topic.

.. _Notifications Primer: https://meta.discourse.org/t/notifications-primer/228439

Transparent Development Expectations
************************************

TBD: Explain what transparent development means to our project - public roadmaps,
public architecture, etc

Adding a Maintainer
*******************

TBD: Explain the process for adding a maintainer to a repo

Stepping Down as Maintainer
***************************

TBD: Explain the process for stepping down


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
