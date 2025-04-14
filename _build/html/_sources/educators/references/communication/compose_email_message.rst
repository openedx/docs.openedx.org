.. _Guide to Composing Email Messages:

Guide to Composing Email Messages
###################################

.. tags:: educator, reference

When you compose an email message, you can use the following options.

.. contents::
  :local:
  :depth: 2


Styling
*********

Messages can include HTML styling, including text formatting and links.

For more information, see :ref:`About Text Components<About Text Components>`.

Restricted HTML Content
========================

The Bulk Course Email tool restricts the use of specific HTML elements from being
used in messages. The following HTML elements may not be used in messages
authored with this tool:

* iframe
* svg
* form
* script

.. note:: If a message contains restricted HTML content, it will **not** be
   stripped from the message. The HTML code will be converted to plain text. You
   should send a test message to yourself before sending it to larger groups
   to ensure message content is displayed as desired.


Images
********

Messages can include images. You must first add the file
to your course on the **Files & Uploads** page to include an image. For an email message, you copy
the **Web** URL that the system assigns to the image. Then, in the email
message editor, you select the **Insert/edit image** icon to add the web URL.

.. note:: Scalable Vector Graphic (SVG) images are restricted from use in
   messages authored with the Bulk Course Email tool. Please see the above note
   in the *Restricted HTML Content* section.

To ensure your course assets are transmitted securely, add the
``https://`` preface to the web URL. An example follows.

::

    https://courses.myinstance.com/asset-v1:{course}.x+{run}+type@asset+block@{image}.jpg

For more information, see :ref:`Add Course Files`.


Keywords
*********

Messages can include variables representing values specific to each
recipient, such as learner name or user ID. The LMS substitutes these
variables, called keywords, with actual values when it sends a message.


.. _Use Keywords in Messages:

Use Keywords in Messages
========================

You can include keywords in your messages. A keyword is a variable: when you
send the message, a value specific to each recipient is substituted
for the keyword. For example, when you use the ``%%USER_FULLNAME%%`` keyword,
each message contains the recipient's name.

.. note::
  Do not use keywords in the Subject line of a message. The keyword in the
  subject will not be assigned a value, and the recipient will see the keyword
  text.


Supported Keywords
===================

You can use the following keywords in your messages.

* ``%%USER_ID%%`` - the anonymous user ID of the message recipient
* ``%%USER_FULLNAME%%`` - the full name of the message recipient
* ``%%COURSE_DISPLAY_NAME%%`` - the display name of the course
* ``%%COURSE_END_DATE%%`` - the end date of the course


Keyword Formatting
===================

You format keywords as: ``%%Keyword%%``.  You can include keywords in any HTML
tags in an email message. An example follows.

::

  <h2>%%COURSE_DISPLAY_NAME%% Updates</h2>

  <p>Dear %%USER_FULLNAME%%, this is a reminder that the last day of the course
     is <b>%%COURSE_END_DATE%%</b></p>
  . . .


.. seealso::
 

 :ref:`Guide to Bulk Email Messages` (reference)

 :ref:`Send an Email Message to Course Participants` (how-to)

 :ref:`Review Sent Messages` (how-to)

 :ref:`View Email Task History Report` (how-to)

 :ref:`Example Messages to Students` (reference)
  


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
