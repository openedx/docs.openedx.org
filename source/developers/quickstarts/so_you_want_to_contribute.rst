.. _qs Dev Contributing:

Quick Start: So You Want to Contribute to Open edX
##################################################

.. tags:: developer, quickstart

So you have gone through :ref:`qs Dev First PR`, and you are ready to make a
substantive contribution to Open edX. What is next?

.. contents::
 :local:
 :depth: 1

.. _Signing CLA:

Start Here!
************

Before we can merge your contribution you will need to sign a Contributor
License Agreement (CLA).  We suggest starting that process sooner rather than
later.

#. If you are contributing as an individual go ahead and sign the `Individual
   Contributor Agreement <Open edX CLA_>`_.

#. If your work will be contributed as part of a company or institution, have
   your team or company lead email ``legal@axim.org`` with your information.


Process Overview
**************************

Open edX follows a standard pull request review process, entirely using GitHub.
Here is a simplified version of the PR process:

.. graphviz::

   digraph G {
     "Pull Request Opened" [shape=box];
     "Needs Product Review" [shape=box, style=rounded];
     "Does this Contribution\n change user experience?" [shape=diamond];
     "Is this contribution \nrelated to groomed work\n from the public road map?" [shape=diamond];
     "Ready for Engineering \nReview" [shape=box, style=rounded];
     
     
     "Pull Request Opened" -> "Does this Contribution\n change user experience?";
     "Does this Contribution\n change user experience?" ->   "Is this contribution \nrelated to groomed work\n from the public road map?" [label="Yes"];
     "Is this contribution \nrelated to groomed work\n from the public road map?" -> "Needs Product Review" [label="No"];
     "Does this Contribution\n change user experience?" ->   "Ready for Engineering \nReview" [label="No"];
     "Is this contribution \nrelated to groomed work\n from the public road map?" -> "Ready for Engineering \nReview" [label="Yes"]
   
   }

See the :ref:`Process for Contributing Code` document for more details.

See the :ref:`Pull Request Status Guide` if you're looking for more information about
what the various statuses and labels of your pull request (PR) mean.

Finding Something To Work On
******************************

One source of candidates is this `list of issues labeled “help wanted”
<https://github.com/search?q=org%3Aopenedx%20is%3Aopen%20is%3Aissue%20label%3A%22help%20wanted%22%20&type=issues>`_.
Some maintainers also label issues with the `"good first issue" label
<https://github.com/search?q=org%3Aopenedx+is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22+&type=issues>`_.
We also encourage you to check out our `Working groups
<https://openedx.atlassian.net/wiki/spaces/COMM/pages/46793351>`_! There are a
few working groups that may have some work they can help guide you through as a
new contributor to the project. Particularly:

* The `Build-Test-Release (BTR) Working Group
  <https://openedx.atlassian.net/wiki/spaces/COMM/pages/1022099494/Build-Test-Release+BTR+Working+Group>`_:
  they manage our named releases, which come out each June and December. They
  particularly need help from mid-February through June and again from mid-August through
  December.

* The `Frontend Working Group
  <https://openedx.atlassian.net/wiki/spaces/COMM/pages/3090056949/Frontend+Working+Group>`_:
  they manage the state of our frontend, including both new features and
  upgrades. They would love more people to join them!

* The `Deprecation (DEPR) Working Group
  <https://openedx.atlassian.net/wiki/spaces/COMM/pages/825983190/Deprecation+Working+Group>`_:
  they work on deprecating various aspects of the Open edX platform. Some
  deprecations are pretty approachable, others are rather complex. Reach out to
  them to see if they have anything you might be able to work on.

* The `Documentation Working Group
  <https://openedx.atlassian.net/wiki/spaces/COMM/pages/4360732679/Documentation+Working+Group>`_
  is developing, migrating, and improving documentation for the Open edX
  Platform. This is a good first task that is non-technical, and open to anyone who
  builds on the platform. To learn more about helping with this, reach out in
  the `#wg-documentation Slack channel <https://openedx.slack.com/archives/C1LM7G955>`_
  and let the group know you are interested.

* The `Product Working Group
  <https://openedx.atlassian.net/wiki/spaces/COMM/pages/3449028609/Product+Working+Group>`_
  reviews and approves new feature proposals. On their `Github project board
  <https://github.com/orgs/openedx/projects/4>`_ there is a column titled
  "Backlog - Not resourced, can be picked up" which contains larger projects you
  or your team may be able to tackle. Reach out in `#wg-product-core
  <https://openedx.slack.com/archives/C057J2D1WU9>`_ if you're interested in
  tackling one of these issues, to ensure no one else is working on it.

The other working groups are very interesting (and worth attending!) but don't
have a backlog of work.

Do you have an idea of what to work on? That's awesome! We encourage you to post
your ideas on the `Open edX forums`_ to get feedback on your idea and
get connected to others that can help you out. Please clearly state your idea,
what you plan to do, link to any relevant code/screenshots, and ask
specifically for what type of feedback or help you are looking for.

Development Environment
**************************

`Tutor`_ is the official Docker-based Open edX distribution, both for production
and local development. There is a `Tutor Topic on the discussion forums
<https://discuss.openedx.org/c/operators/tutor/41>`_ to get help specifically on
Tutor or you can post in the `Development category on the Open edX forum
<https://discuss.openedx.org/c/development/11>`_ if you have questions about
set-up or development. 

Getting Support
**************************

Please use the `Open edX forums`_ to ask for help. First, search for your
question/issue/stack trace before asking a question, as it may already be
answered! We recommend first posting in the forums, *then* cross-posting the
link to your forums post in Slack if you want to draw more attention to your
post.

Why? The Slack history is deleted after 6 months but the forums history is
never deleted, so your questions there will be displayed to people searching for
similar questions in the future.

Making Your First Pull Request
*******************************

Follow the :ref:`Git workflow`, and the instructions for :ref:`Landing Your Work`.

#. Don't forget about :ref:`signing your CLA <Signing CLA>`!

#. When you are :ref:`ready to submit changes <Contributing Code>`, create a Pull Request.

#. Be sure to `reference which ticket your code is resolving
   <https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests#linking-a-pull-request-to-an-issue>`_.

#. Please read the bot's comment on your PR carefully, and ensure you have done
   everything that is asked for.

#. If you did work for a working group, post your pull request in the
   appropriate WG Slack channel.

#. Once your code has begun to be reviewed, communicate with the reviewer about
   the code and respond to feedback promptly. Note that it may take a week or
   two for a review to begin on your PR. If after that time your PR still
   doesn't have any attention, feel free to ping the maintainer mentioned in the
   bot's message for attention.

#. Once your PR is approved it will be merged by the reviewer.

#. Celebrate 🎉!!!

How To Streamline Getting Your Contribution Merged
***************************************************

When pull requests come in they need to be reviewed by team that maintains the
repository.  Depending upon that team's priorities, it may take some time to get
your review scheduled.  We aim at having predicable lead times and transparency
about what is happening and when.  There are things that you can do as a
contributor to help.

#. If your change in still in progress or experimental, please **open the pull
   request as a draft**.  We won't focus on reviews until the code is ready and
   this will reduce wasted attention on both sides.

#. Make sure that you **describe the purpose of the change** that you are
   proposing clearly in the description of the pull request and why the change
   is valuable.

#. **Read the bot messages** on your PR carefully.

#. Follow the :ref:`Landing Your Work` instructions carefully, including using
   Conventional Commits, considering internationalization/performance/security,
   and more.

#. `Allow admins to push commits onto your branch
   <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork>`_.
   GitHub has settings that allow reviewers to push commits onto your branch.
   This feature is valuable when the branch is out of date with the base.
   Reviewers can update your branch from the base with a merge commit that will
   isolate those changes. This decreases the back-and-forth, which can add days to
   review times.

#. **Mention related pull requests** in the PR description so reviewers can review
   them as a single body of work and avoid context shifts.

#. **Check the checks**. GitHub requires that the Open edX team run checks manually
   for new contributors. When there are failures, please review them and
   address them quickly to ensure a timely completion of your review.  Failures
   you may see include linting errors, test failures, failures related to
   decreased test coverage, etc. On occasion failures may not be related to
   your change, but can be fixed by merging in updates on the base branch. If
   you believe this is the case, please update your branch.

Working with GitHub Issues
**************************

Work on Open edX is often tracked on GitHub issues, which are organized on
`GitHub project boards <https://github.com/orgs/openedx/projects>`_.

Anyone with a GitHub account can interact with our GitHub issues in some basic
ways using `issue commands
<https://openedx.atlassian.net/wiki/spaces/COMM/pages/3536815057/Working+group+issue+commands>`_.
For example, if you would like to work on an issue, let everyone know by simply
commenting ``assign me``!

Once you have established yourself as involved in a working group or some other
project, feel free to request “Triage” access to our repositories. Open an `Axim
Request`_ using the “Onboarding” template, and specify that you would like
Triage access in order to be more involved in the project. Provide a link to
what you are working on, and ``@``-mention another GitHub user who you have been
working with who can vouch for you. If Axim grants the request, then you will
find that you are now able to manage assignees, labels, and handful of other
aspects of Open edX GitHub issues.

Once you have Triage access, you can also ask project leaders to give you access
to individual project boards that you want to help manage, which will let you
change status and other metadata on project issues.

Giving Feedback
**************************

We are always looking to improve this process and make it easier for people to
contribute to the platform.  Your feedback is a very important part of that
process.

If you have specific praise, or constructive criticism you think the community
could benefit from, please post on the `Open edX forums`_. 

.. seealso::

   :ref:`Process for Contributing Code` (Reference)

   :ref:`Contributing Code` (Reference)

   :ref:`Landing Your Work` (Reference)

   :ref:`Git workflow` (Reference)

   :ref:`Open edX Style Guidelines` (Reference)

   :ref:`Testing` (Reference)

   :ref:`Open edX Developer's Guide` (Reference)

   `Intro to the Open edX Project & Contributing <https://training.openedx.io/courses/course-v1:OpenedX+OEX101+2023/about>`_ (Training Course)

   `Open edX Developer Onboarding <https://training.openedx.io/courses/course-v1:OpenedX+OEX-Dev101+2024/about>`_ (Training Course)


.. include:: /links.txt


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
