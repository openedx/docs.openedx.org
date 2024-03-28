#########################
Pull Request Status Guide
#########################

***************************
Contribution Board Statuses
***************************

.. list-table:: Title
   :widths: 30 70
   :header-rows: 1

   * - **Status**
     - **Description(s)**

   * - **Needs Triage**
     - A bot automatically places open-source contributions in this status and
       labels them as such. The Community Project Managers triage PRs from here
   * - **Needs Tests Run, or CLA Signed**
     -
         * If the author has never contributed to a particular repo, they need
           authorization to run tests on the pull request [enabling tests is
           currently handled by Axim].
         * If the author has never contributed to the Open edX project before,
           they need to fill out a CLA form.
   * - **Product Review**
     - Actively being reviewed by Product (only applies to PRs labeled as
       needing product review) - pull requests needing product review must have
       product approval before continuing through the process
   * - **Waiting for Author**
     -
         * The PR is actively in progress
         * The author needs to address questions, feedback, rebase, etc.
         * The PR is still in a draft state

   * - **Blocked**
     - Blocked by other pull requests / work. There should be context within the
       PR for why it's blocked
   * - **Ready for Review**
     -
         * Ready for review by maintainer or repo owner
         * All checks have passed and are green (including CLA)
         * The owning / maintaining team has been asked to review

   * - **Scheduled for Eng Review**
     - The reviewing team has scheduled to review this in an upcoming sprint,
       has assigned themselves to review

   * - **In Eng Review**
     - Actively being reviewed by Engineering.

   * - **Ready to Merge**
     -
         * Reviews are complete
         * Tests are green
         * No conflicts, and branch is not out-of-date
         * Changes and feedback have been addressed
         * Reviewer has approved

   * - **Done**
     - Merged/Closed

*************************
Contribution Board Labels
*************************

**Note**: Depending on the situation, more than one of these labels may be on a
pull request at the same time. Though some may seem repetitive of the status
columns, the PRs might have several things going on simultaneously, so these
labels compliment the above board statuses.

For example, a pull request could be “In Eng Review” on the Contributions board,
but be tagged with the “Waiting for Author” and/or “Changes Requested” label if
the author needs to take actions related to feedback.

.. list-table:: Title
   :widths: 30 70
   :header-rows: 1

   * - **Label**
     - **Description**

   * - .. image:: /_images/pr_label_open-source-contribution.png
     - Automatically added by a bot to PRs coming from the community (not from Axim or 2U).

   * - .. image:: /_images/pr_label_backport.png
     - Denotes that the PR backports a change from main to a named release.

   * - .. image:: /_images/pr_label_blocked_by_other_work.png
     - Another way to notate that the PR is blocked. It should say in the PR why
       the work is blocked.
   * - .. image:: /_images/pr_label_changes_requested.png
     - The reviewer(s) have taken a look at the PR and requested the author make changes.

   * - .. image:: /_images/pr_label_closed-inactivity.png
     - Closed due to PR being abandoned.

   * - .. image:: /_images/pr_label_core_contributor.png
     - Denotes that a :doc:`Core Contributor <core-contributors>` is the author
       of the pull request.

   * - .. image:: /_images/pr_label_inactive.png
     - Used when the author has been unresponsive for an extended period of
       time. The Community Project Managers will typically give a final comment
       to the author alerting them the pull request may need to be closed due to
       inactivity. If there is still no response from the author, the PR will be
       closed shortly after.

   * - .. image:: /_images/pr_label_needs_test_run.png
     - This means an author has not contributed to a particular repo before and
       needs authorization to be able to run tests on the PR. Currently, test
       authorization is handled by Axim.

   * - .. image:: /_images/pr_label_product_review.png
     - Indicates that a PR requires Product Review. Product review is done
       either before code is written, or before Engineering review if the PR is
       already in-progress.

   * - .. image:: /_images/pr_label_waiting_for_eng_review.png
       .. image:: /_images/pr_label_needs_maintainer_attention.png
     - Used to alert reviewers / maintainers that a PR is waiting for their review.

   * - .. image:: /_images/pr_label_waiting_on_author.png
     - Waiting for the author to respond to change requests, feedback, failing
       tests, etc. Usually this label is used for PRs in board statuses other
       than “Waiting for Author”.

   * - .. image:: /_images/pr_label_duplicate.png
     - This issue or pull request already exists elsewhere.