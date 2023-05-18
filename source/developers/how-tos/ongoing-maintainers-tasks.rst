Ongoing Maintainer's Tasks
##########################

..
  Much of the TBD content in this document should be answered when we come
  to consensus on https://openedx.atlassian.net/wiki/spaces/COMM/pages/3545726977/Maintainer+Outstanding+Questions+9+14+meeting


This How-to will explain the ongoing tasks that Maintainers are expected to
perform, once their repositories are up to Open edX project standards (see
:doc:`maintain-a-repo`). These actions are performed periodically - some more
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
  documentation in a consistent format with the rest of the project.

GitHub Notifications
********************

TBD: How to set up a group, what the notification settings should look like for that group

Responding to Issues
********************

TBD: Explain what a maintainer's responsibilities are around issue response time

Responding to PRs
*****************

Our goal for PR response time is that they are "triaged" within a week of receipt. This does not mean that review happens within a week, but that the PR is acknowledged and scheduled for review in line with the maintainer's other priorities.  This response time goal is ongoing.  So when an author responds to feedback, the goal is the same.

One of the scarcest resources of an open-source project is contributor and maintainer time.  It is ideal that once a review starts, that it can be finalized as a single piece of work, say within the boundaries of a single sprint.

As a maintainer, your goal should be keeping the time to review and finalize a PR predictable and as short as reasonable.  Finalizing a PR can mean rejecting it. For a contributor, knowing that a PR won't be accepted and why provides them appropriate feedback and lets them decide what to do next.

If your team schedules reviews for future sprints, providing that information to the author is helpful to set their expectations and plan accordingly. Leave a comment indicating when you expect the review to occur and ensure that the status on the contributions board is "Scheduled for Eng Review."

When reviewing a PR, we want to focus on reducing the back-and-forth that increases lead time.  In our globally distributed project, a comment and response cycle can easily take 24 hours.  Ideally, both contributor and reviewer can both focus their attention on finalizing a PR at the same time.

It is recommended that reviewers approve the GitHub actions if approval is required.  Github requires approval from new contributors to any repository, so even folks who have contributed to the project, but not the particular repository, require approval.

When GitHub detects that the PR branch is out of date with the base, it is recommended that the reviewer update the branch using a merge commit.  This keeps the history clear and reduces days of lead time over pushing this back to the original author.  However, reviewers may ask authors to resolve any conflicts between their branch and the base.

Managing Upgrade PRs
********************

TBD: Explain SLAs for responding to python-upgrade-bot, Renovate, or any other automatic upgrade tool

Participating in Forum Discussions
**********************************

TBD: Explain what a maintainer's responsibilities are around participating in the forums

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


