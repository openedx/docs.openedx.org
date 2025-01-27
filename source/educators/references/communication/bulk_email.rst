.. _Bulk Email:

Bulk Email Messages from the Course Team
########################################

.. tags:: educator, reference

For courses on an Open edX instance, you can send bulk email messages to course participants
directly from the instructor dashboard: in the LMS, select **Instructor**, and
then select **Email**.

Your messages can use HTML styling, and can include links to videos, social
media pages for the course, and other material. All course team members who
have the Staff or Admin role can use bulk email messages to communicate with
course participants before, during, and after the course run.

Learners are less likely to read and respond to email messages from courses
when they receive too many of them. As a best practice, do not send more than
one email message per week to course participants, unless there is good reason
to do so.

.. note:: Some courses use third party services such as MailChimp to send bulk
   email. Do not use both a third party service and the Open edX bulk email
   service. If you use more than one service to send email message, your
   messages are more likely to be marked as spam, and learners might not read
   them.

This section contains the following topics.

.. contents::
  :local:
  :depth: 1

.. _bulk_email_message_addressing:

Message Addressing
*************************

When you send a bulk email message from the instructor dashboard, you choose
its recipients by selecting a **Send to** option. You can select one or more
recipient groups for each message. For details about who is included in each
of the preset recipient groups, see :ref:`Bulk Email Who Is Included or
Excluded`

When you send a message to more than one recipient group, duplicate recipients
are filtered out, so that someone who belongs to more than one of the recipient
groups only receives one copy of the message. For example, if you address an
email message to learners in a particular cohort as well as to learners in the
Verified enrollment track, a learner who is in the cohort AND is in the Verified
enrollment track will only receive one email message.

The following preset recipient groups are available.

* **Myself**. Send an email message only to yourself, to test and review the
  message before sending it to a larger group.

* **Staff and Administrators**. Send an email message to members of the course
  team who have Staff or Admin privileges. For information about course
  team member privileges, see :ref:`Course_Staffing`.

* **All Learners**. Send an email message to all currently enrolled learners.
  This group does not include learners who have not activated their accounts,
  or who have opted out of receiving email communications. This group does not
  include course team members, even if they are enrolled in the course.

If you have more than one enrollment track in your course, each enrollment
track is available as a separate recipient group. For more information, see
:ref:`Enrollment Track Recipient Groups`.

If you have cohorts enabled in your course, each cohort is available as a
separate recipient group. For more information, see :ref:`Bulk Email Cohorts`.


.. _Bulk Email Who Is Included or Excluded:

Who Is Included in Each Recipient Group?
=========================================

When you send a bulk email message to one of the preset recipient groups, you
should be aware of who is included in each group.

.. note:: It is considered good practice to only send messages to active and
   engaged learners. For this reason, regardless of the recipient groups
   selected, the Open edX platform will only send email messages to learners in a course run who
   have logged in within the last 18 months. This helps reduce the risk of
   messages being marked as spam (or bouncing) and helps ensure the continued
   delivery of bulk course email messages through your instance's email providers.

.. list-table::
   :widths: 30 40 40
   :header-rows: 1

   * - Recipient Group
     - Includes
     - Does Not Include

   * - Staff and Administrators
     - * Any course team member who has the **Staff** role.
       * Any course team member who has the **Admin** role.
     - * Beta testers who do not also have the **Staff** or **Admin** role.
       * Discussion moderators who do not also have the **Staff** or **Admin**
         role.
       * Discussion administrators who do not also have the **Staff** or
         **Admin** role.
       * Learners who have the Community TA or Group Community TA discussion
         moderator roles.

   * - All Learners
     - * All currently enrolled learners in your course, including those who
         have enrolled but have not yet accessed the course.
     - * Learners who have not replied to the account activation email message
         that they received when they registered on your Open edX instance.
       * Learners who have opted out of receiving email messages through the
         **Email Settings** link for the course on the learner's dashboard.
       * Course team members, regardless of whether they are enrolled in the
         course.


.. _Enrollment Track Recipient Groups:

==================================================================
Sending Email Messages to Learners in Different Enrollment Tracks
==================================================================

If you have more than one enrollment track in your course, each enrollment
track is available as a separate recipient group. If your course includes only
a single enrollment track, you will not have a track-based recipient group.

For example, if your course includes an audit track and a verified certificate
track, you have two additional recipient groups: **Learners in the Audit
Track** and **Learners in the Verified Certificate Track**.


.. _Bulk Email Cohorts:

===================================================
Sending Email Messages to Learners in Cohorts
===================================================

If you enable cohorts in your course, each cohort is available as a separate
recipient group. The recipient groups for individual cohorts only include
enrolled learners who have been assigned to a cohort, whether they were
automatically assigned when they accessed the course or manually assigned to a
cohort by a member of the course team.

The recipient groups for cohorts do not include enrolled learners who have not
been added to a cohort. This might be the case if they have not accessed the
course or have not been manually added to a cohort by a member of the course
team. To make sure such learners are included in email messages that are
intended for all enrolled learners, select the **All Learners** recipient
group instead of selecting all of the cohort recipient groups.

If a default cohort exists in your course, a recipient group named **Cohort:
Default Group** is also available.

.. note:: The default cohort is created only if you have not created at least
   one automated assignment cohort in your course by the time the first
   learner accesses course content. If learners access the course before you
   have created any automated cohorts, they are automatically placed in the
   default cohort, to ensure that all learners in the course belong to a
   cohort. You can manually reassign learners from the default cohort to
   another cohort. For more information, see :ref:`Default Cohort Group`.

Managing Scheduled Email Messages
**********************************

Once a message has been scheduled it will appear in the **Scheduled emails**
table. Each entry will describe *when* the message will be sent (in local time),
the *recipient groups* selected, the *subject* of the message, and the *author*
of the message.

.. image:: /_images/educator_how_tos/Bulk_email_scheduled_emails_table.png
       :alt: A tabular list of scheduled email messages, with columns for
             *send date*, *send to*, *subject*, *author*, and *action*.

Each scheduled email entry in this table will support the following actions:

* The *View* button will open a modal that allows you to view the contents of
  this message.
* The *Delete* button will cancel the scheduled bulk email task and the message
  will **not** be sent. This sets the bulk email task's status to **REVOKED**.
* The *Edit* button will allow you to edit the bulk email message. You will be
  able to adjust the recipients, subject, message contents, and/or the date and
  time the message should be sent.


.. _Email_queuing:

Message Workflow States
****************************

When you select **Send Email** for a message, the server begins to process a
bulk email task. The server assigns a series of different workflow states to
the task.

When you select **Schedule Email** for a message, the server creates a bulk
email task and sets it to the **SCHEDULED** state. This task will remain in this
state until it is ready to be processed.

.. image:: /_images/educator_how_tos/Bulk_email_states.png
       :alt: Flowchart of the possible states of a bulk email task.

Bulk email tasks can have the following workflow states.

* Queuing: The bulk email task is created and being queued for background
  processing.
* Pending: The task is queued and is waiting to run.
* Scheduled: The task has been created and is scheduled to run at a future date
  and time.
* Started: Background processing is in progress to create emailing subtasks.
* Progress: The emailing subtasks are in progress.
* Success: All emailing subtasks are complete. Note that the bulk email task
  can be in this state even if some or all of its emailing subtasks failed.
* Failure: An error occurred and task processing did not complete successfully.
* Revoked: The task was cancelled before it was processed.

While the bulk email task is in progress, you can find out what stage it has
reached in the workflow by checking the **Pending Tasks** section on the
**Course Info** page of the Instructor Dashboard.

.. image:: /_images/educator_how_tos/Bulk_email_pending.png
      :alt: Information about an email message, including who submitted it
            and when, in tabular format

When the bulk email task is complete, you can find its final state by checking
the Email Task History report. For more information, see :ref:`Email Task
History Report`.

.. seealso::
 :class: dropdown

 :ref:`Send_Bulk_Email` (how-to)

 :ref:`Review Sent Messages` (how-to)

 :ref:`Email Task History Report` (how-to)

 :ref:`Example Messages to Students` (reference)

 :ref:`Options for Email Message Text` (reference)

  
  

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
