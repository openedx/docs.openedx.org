.. _Problem Settings:

Defining Settings for Problem Components
########################################

.. tags:: educator, reference

In addition to the text of the problem and its formatting or OLX
markup, you define the following settings for problem components. To access
these settings, edit the problem. With the exception of **Display Name**,
you can find all of these settings on the right side of your problem. Click
on **Show advanced settings** to view additional options such as
**Show Answer**, **Show reset option** and **Time between attempts**.

.. contents::
  :local:
  :depth: 2

If you do not edit these settings, default values are supplied for your
problems.

.. note::
  If you want to temporarily or permanently hide problem results from learners,
  you use the subsection-level **Results Visibility** setting. You cannot
  change the visibility of individual problems. For more information,
  see :ref:`Problem Results Visibility`.


Display Name
************

This required setting provides an identifying name for the problem. The display
name appears as a heading above the problem in the LMS, and it identifies the
problem for you in reporting and analytics systems. Be sure to add unique,
descriptive display names so that you, and your learners, can identify specific
problems quickly and accurately.

You can find the display name setting at the top of your problem. To edit,
click the pen symbol to the right of the field and enter the desired text.

The following illustration shows the display name of a problem in Studio, and
in the LMS.

.. image:: /_images/educator_how_tos/display_names_problem.png
 :alt: The identifying display name for a problem in Studio, and the LMS.
 :width: 800

.. _Problem Type:


Type
****

You can change the problem type after your initial selection. The current
problem type is shown with a check mark. Selecting any other problem type will
change your problem to that type while carrying over the content you have already
prepared. Please check your selection for correct answers as these may not carry
over when changing problem types.

.. note:: If you would like to convert your problem into an advanced problem,
  scroll down to the bottom of the settings, click **Show advanced settings**
  and then click **Switch to advanced editor**.

.. _Problem Scoring:


Scoring
********

These settings allow you to change the amount of points your problem is worth
and the number of attempts a student has for answering it.


Problem Points
==============

This setting specifies the total number of points possible for the problem.
This defaults to 1 point. In the LMS, the number of points a problem is worth
appears near the problem's display name.

.. note::
  The LMS scores all problems. However, only scores for problem
  components that are in graded subsections count toward a learner's final
  grade.


Attempts
********

This setting specifies the number of times that a learner is allowed to try
to answer this problem correctly. You can define a different **Attempts**
value for each problem. Setting the Attempts value to empty means that learners
have an unlimited number of attempts.

A course-wide **Maximum Attempts** setting defines the default value for this
problem-specific setting. Initially, the value for the course-wide setting is
null, meaning that learners can try to answer problems an unlimited number of
times. You can change the course-wide default by selecting **Settings** and
then **Advanced Settings**. Note that if you change the course-wide default
from null to a specific number, you can no longer change the problem-specific
**Attempts** value to unlimited.

Only problems that have an **Attempts** setting of 1 or higher are included in
the answer distribution computations used in the Student Answer Distribution
report.

.. note::
   The recomendation is to set **Maximum Attempts** to unlimited or a
   large number when possible. Problems that allow unlimited attempts encourage
   risk taking and experimentation, both of which lead to improved learning
   outcomes. However, allowing for unlimited attempts might not be feasible in
   some courses, such as those that use primarily single select or dropdown
   problems in graded subsections.

.. _Show Answer Number of Attempts:


Number of Attempts
==================

This setting appears under the Show answer dropdown when the
**After some number of attempts**, **After all attempts** or
**After all attempts or correct** option is selected. This limits when
learners can select the **Show Answer** option for a problem. Learners must
submit at least the specified number of attempted answers for the problem
before the **Show Answer** option is available to them.

.. _Time Between Attempts:

Time Between Attempts
=======================

This setting can be found on the collapsible settings to the right of the
problem editor after clicking **Show advanced settings**. It specifies the
number of seconds that a learner must wait between submissions for a problem
that allows multiple attempts. If the value is 0, the learner can attempt the
problem again immediately after an incorrect attempt.

Adding required wait time between attempts can help to prevent learners from
simply guessing when multiple attempts are allowed.

If a learner attempts a problem again before the required time has elapsed, they
see a message below the problem indicating the remaining wait time. The format
of the message is, "You must wait at least {n} seconds between submissions. {n}
seconds remaining."

.. _Hints:

Hints
******

When you add hints, the **Hint** button is automatically displayed to learners.
Learners can access the hints by selecting **Hint** beneath the problem.  A
learner can view multiple hints by selecting **Hint** multiple times.

For example, in the following single select problem, the learner selects
**Hint** after having made one incorrect attempt.

.. image:: /_images/educator_references/multiple_choice_hint.png
 :alt: Image of a single select problem with the first hint.
 :width: 600

The hint text indicates that it is the first of two hints. After the learner
selects **Next Hint**, both of the available hints appear. When all hints have
been used, the **Hint** or **Next Hint** option is no longer available.

.. image:: /_images/educator_references/multiple_choice_hint2.png
 :alt: Image of a single select problem with the second hint.
 :width: 600

.. seealso::
 :class: dropdown

 :ref:`Configure Hint` (how-to)



Best Practices for Providing Hints
==================================

To ensure that your hints can assist learners with varying backgrounds and
levels of understanding, you should provide multiple hints with different
levels of detail.

For example, the first hint can orient the learner to the problem and help
those struggling to better understand what is being asked.

The second hint can then take the learner further towards the answer.

In problems that are not graded, the third and final hint can explain the
solution for learners who are still confused.

.. _Show Answer:

Show Answer
***********

This setting can be found on the collapsible settings to the right of the
problem editor after clicking Show advanced settings. This will add a
**Show Answer** option to the problem for the learner. The following
options define when the answer is shown to learners.

.. list-table::
   :widths: 15 70

   * - **After All Attempts**
     - Learners will be able to **Show Answer** after they have used all of
       their attempts. Requires max attempts to be set on the problem.

   * - **After All Attempts or Correct**
     - Learners will be able to **Show Answer** after they have used all of
       their attempts or have correctly answered the question. If max attempts
       are not set, the learner will need to answer correctly before they can
       **Show Answer**.

   * - **After Some Number of Attempts**
     - Learners will be able to **Show Answer** after they have attempted the
       problem a minimum number of times (this value is set by the course team
       in Studio).

   * - **Always**
     - Always present the **Show Answer** option.

       Note: If you specify **Always**, learners can submit a response even
       after they select **Show Answer** to see the correct answer.

   * - **Answered**
     - Learners will be able to **Show Answer** after they have correctly
       answered the problem.

   * - **Attempted**
     - Learners will be able to **Show Answer** after they have made at least
       1 attempt on the problem.

       If the problem can be, and is, reset, the answer continues to show.
       (When a learner answers a problem, the problem is considered to be both
       attempted and answered. When the problem is reset, the problem is still
       considered to have been attempted, but is not considered to be
       answered.)

   * - **Attempted or Past Due**
     - Learners will be able to **Show Answer** after they have made at least
       1 attempt on the problem or the problem’s due date is in the past.

   * - **Closed**
     - Learners will be able to **Show Answer** after they have used all
       attempts on the problem or the due date for the problem is in the past.

   * - **Correct or Past Due**
     - Learners will be able to **Show Answer** after they have correctly
       answered the problem or the due date for the problem is in the past.

   * - **Finished**
     - Learners will be able to **Show Answer** after they have used all
       attempts on the problem or the due date for the problem is in the past
       or they have correctly answered the problem.

   * - **Never**
     - Learners and Staff will never be able to **Show Answer**.

   * - **Past Due**
     - Learners will be able to **Show Answer** after the due date for the
       problem is in the past.

An explanation for the correct answer can be entered below. This explanation
is displayed when the learner presses the Show answer option.

.. _Show Reset Button:


Show Reset Button
*****************

This setting can be found on the collapsible settings to the right of the
problem editor after clicking **Show advanced settings**. It defines whether a
**Reset** option is available for the problem.

Learners can select **Reset** to clear any input that has not yet been
submitted, and try again to answer the problem.

If the learner has already submitted an answer, selecting **Reset** clears the
submission and, if the problem contains randomized variables and randomization
is set to **On Reset**, changes the values in the problem.

If the number of Maximum Attempts that was set for this problem has been
reached, the **Reset** option is not visible.

This problem-level setting overrides the course-level **Show Reset Button for
Problems** advanced setting.


.. seealso::
 :class: dropdown

 :ref:`Working with Problem Components` (reference)

 :ref:`Modifying a Released Problem` (reference)

 :ref:`Advanced Editor` (reference)

 :ref:`Feedback Best Practices` (concept)

 :ref:`Learner View of Problems` (reference)

 :ref:`Configure Hint` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
