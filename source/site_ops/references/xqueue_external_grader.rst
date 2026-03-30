.. _XQueue Reference:

XQueue Reference
############################

.. tags:: site operator, how-to

An external grader problem requires :ref:`Enable XQueue` before it can be defined and published in Studio.

This reference guide details external grader requirements and technical specifications of XQueue submissions.

.. contents:: 
  :local:
  :depth: 1

Once properly set up, an :ref:`OLX definition <OLX Definition>` for the external grader can be defined in Studio.

.. _External Grader Requirements:

External Grader Requirements
============================

When you build your external grader, keep the following requirements in mind.

* To communicate with XQueue, the grader must accept and return JSON objects.
  For more information, see :ref:`XQueue JSON Objects`.

* The external grader must actively retrieve, or pull, submissions from the
  XQueue through a RESTful interface at regular intervals.

* The grader must be scalable. Many learners might submit responses at one
  time, such as shortly before an exam is due. The grader must be able to
  process many submissions in a limited time, without failure or unexpected
  delays.

* The grader must not constantly send queries unless the grader detects that
  the ``queuelen`` value is growing. If XQueue receives too many requests from
  a grader, the XQueue system administrator may apply throttling to the grader.

* The grader must implement security features.

  You are responsible for the server that runs the code that learners submit.
  Your system must protect against learners who might submit malicious code and
  ensure that the external grader runs only code that is relevant to the course
  problems. Your specific security implementation depends on the programming
  language that you are using and your deployment architecture. You must ensure
  that malicious code will not damage your server.


* You must have a plan to immediately notify the team that operates your
  grader, as well as your Open edX system administrator, if the grader fails.
  You must also have a process to quickly identify the cause of the failure,
  whether the problem is with your grader or XQueue.

  If you know the grader will be unavailable at a certain time for maintenance,
  you might consider contacting course teams so they can :ref:`add a course update <Add a Course Update>`.

.. _XQueue JSON Objects:

XQueue JSON Objects
===================

Both the learner submission that XQueue sends to the grader, and the response
that the grader sends to XQueue, are JSON objects.

.. note::
  XQueue does not send the learner ID to the external grader. Your grader
  cannot access IDs or associate learner IDs with submissions.

.. _XQueue Learner Submissions:

Learner Submissions
*******************

The grader must receive a JSON object as a learner submission. The JSON object
has the following keys.

* ``xqueue_header``: A dictionary that the grader uses to identify the
  submission when the grader returns the submission to XQueue. Do not edit this
  dictionary. Return this dictionary to XQueue in the same ``xqueue_header``
  part of the JSON object.

* ``xqueue_files``: A dictionary of key/value pairs that contains a list of
  files that the learner submitted. In this dictionary, each key is a file
  name, and each value is the location of the file.

* ``xqueue_body``: A dictionary that contains the actual submission as JSON.

  * ``student_info``: A dictionary that contains the following information
    about the student in relation to this submission.

    * ``anonymous_student_id``: A string that contains an anonymized identifier
      of the student.

    * ``submission_time``: A string that contains a timestamp with the time of
      submission in ``YYYYMMDDHHMMSS`` format.

    * ``random_seed``: If a randomization script is attached to the problem,
      ``random_seed`` is an integer that contains the seed that initializes the
      randomization script.

  * ``student_response``: A string that contains the learner’s code submission.
    A learner can submit code by entering a string in the LMS or by attaching a
    file. XQueue stores files that learners upload in ``xqueue_files``.

  * ``grader_payload``: An optional string that you can specify when you create
    the problem. For more information, see :ref:`Add an External Grader Problem`.

An example JSON object for a learner submission follows.

::

  {
    "xqueue_header": {
      "submission_id": 72,
      "submission_key": "ffcd933556c926a307c45e0af5131995"
    }
    "xqueue_files": {
      "helloworld.c": "http://download.location.com/helloworld.c"
    }
    "xqueue_body":
    "{
      "student_info": {
        "anonymous_student_id": "106ecd878f4148a5cabb6bbb0979b730",
        "submission_time": "20160324104521",
        "random_seed": 334
      },
      "student_response": "def double(x):\n return 2*x\n",
      "grader_payload": "problem_2"
     }"
  }


.. _XQueue External Grader Responses:

External Grader Responses
*************************

After the grader runs tests and records the results for a submission, the
grader must return information by posting a JSON response. The JSON string
contains a value that indicates the following information.

* Whether the submission was correct.
* The score for the problem.
* Any message that the tests create.

In the following example external grader response, the learner's submission was
correct, the score was 1, and the tests created a brief message.

::

  {
  “xqueue_header”: {
    Identical to what was received from the xqueue
  },
  “xqueue_body”: {
      "correct": true,
      "score": 1,
      "msg": "<p>The code passed all tests.</p>"
   }
  }


.. seealso::
 
 :ref:`Enable XQueue`

 :ref:`About External Grader Problems` (concept)

 :ref:`Add an External Grader Problem` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-03-25   |  Usama S                      |  Verawood      |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+