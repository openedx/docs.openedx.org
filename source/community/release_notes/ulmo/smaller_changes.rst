.. _Ulmo Potpourri:

Smaller Changes (Potpourri)
############################

.. contents::
  :local:
  :depth: 1

.. _Ulmo Problem Visibility:

New Problem Visibility Setting
******************************

With the new :ref:`problem visibility option <Problem Results Visibility>`,
**Never show individual assessment results, but show overall assessment results
after due date**, learners do not see question-level correctness or scores
before *or* after the due date. However, once the due date passes, they can see
their overall score for the subsection on the Progress page.

If *either* "Show When Subsection is Past Due" or "Never show individual
assessment results, but show overall assessment results after due date" has been
selected, and the due date is in the future, a banner message will appear on the
progress page with the message "Some assignment scores are not yet included in
your total grade. These grades will be released by {dueDate}."

.. image:: /_images/educator_references/progress_page_assessment_before_due.png
   :alt: The banner appears at the top of the learner's progress page, directly below the banner that indicates whether or not the learner is currently passing the course.

.. _Forums Spam Prevention:

Forum Moderation & Spam Prevention Features
*******************************************

In the Ulmo release, five new features to remediate forums spam and abuse have
been introduced.

1. A tooltip has been added when hovering over any Forums username, which shows
   their role in the course. This helps learners identify official posts and
   reduces the effect of fake authority names.

   The tooltips say:

   * "Learner - Taking the course just like you" displays for all learners
   * "Staff - Part of the team that runs this course" displays for all course staff
   * "Moderator - Part of the team that runs this course" displays for all course moderators

   .. figure:: /_images/release_notes/ulmo/forums_role_tooltips.png
      :scale: 40

      Mouse-over on usernames shows tooltips that explains their role

.. note::

   The following four features are *not* enabled by default. Site operators should see the
   :ref:`Configuring Forums Spam` section of the Operators Release Notes to
   learn more.

2. Preventing harmful content from being viewed: A configurable feature was
   added that replaces content containing certain strings with a custom message.

3. reCAPTCHA was added to the forum content creation API to prevent automated
   posting. It does not apply to users who have a course or forum role, or whose
   accounts are more than one month old.

4. A rate limit was added to forums content creation, to limit the number of
   posts a single author can add within a set period of time.

5. Given almost all spam accounts use unverified or random email addresses, a
   feature was built to limit forums posts to only those with verified accounts.

   Turning this on runs the risk of reducing engagement by adding friction for
   genuine learners, and it has been seen that spammers can work around this
   limitation.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|2025-12-18    | Product WG                    | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+