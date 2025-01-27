.. _Email Task History Report:

Use the Email Task History Report
###########################################

.. tags:: educator, how-to

The Email Task History report can help you keep track of who sent messages,
when, to which groups, and how many messages were successfully sent. For each
message sent, the report includes the username of the requester, the date and
time it was submitted, the duration and state of the entire task, the task
status, and the task progress.

You can use this history to investigate questions relating to bulk email
messages that have been sent, such as these examples.

* How frequently learners are sent course-related email messages.
* Whether a message was sent successfully.
* The change in the number of people who were sent course-related messages over
  time.

To produce the Email Task History report, follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Email**.

#. In the **Email Task History** section of the page, select **Show Email Task
   History**. A report like the following example displays on the instructor
   dashboard.

.. image:: /_images/educator_how_tos/Bulk_email_history.png
       :alt: A tabular report with a row for each message sent and columns for
             requester, date and time submitted, duration, state, task status,
             and task progress.


Review Email Task History
***************************

For tasks with a **State** of Success, the **Task Progress** column shows an
informational message. These messages can have a format such as "Message
successfully emailed for 13457 recipients (skipping 29) (out of 13486)". To
interpret this message, note that:

* The first number ("recipients") indicates the number of messages sent to the
  selected recipients.

* The second number ("skipping") indicates the number of enrolled and activated
  users who were not sent the message. This count is of learners who have opted
  not to receive course email messages.

* The final number ("out of") indicates the number of users in the set of
  recipients you selected who were enrolled in the course (and had activated
  their user accounts) when you sent the email message.

If the "recipients" and "out of" numbers are the same, the message reads
"Message successfully emailed for 13457 recipients" instead.

Other **Task Progress** messages for tasks with a **State** of Success indicate
that some or all of the emailing subtasks did not successfully send email:

* "Message emailed for {number succeeded} of {number attempted} recipients"
* "Message failed to be emailed for any of {number attempted} recipients"
* "Unable to find any recipients to be emailed"

No **Task Progress** messages display for tasks that have a **State** of
Failure.

.. seealso::
 

 :ref:`Bulk Email` (reference)

 :ref:`Send_Bulk_Email` (how-to)

 :ref:`Review Sent Messages` (how-to)

 :ref:`Example Messages to Students` (reference)

 :ref:`Options for Email Message Text` (reference)
  
  


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
