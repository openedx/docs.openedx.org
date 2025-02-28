.. _External Grader Problem Requirements:

External Grader Problem Requirements
####################################

.. tags:: educator, reference

An external grader problem in Studio must have the following requirements.

* A :ref:`GNU PG key <GPG Key>`.
* An :ref:`XQueue name <XQueue Name>`.
* :ref:`XQueue JSON objects <XQueue JSON Objects>`.
* An :ref:`external grader <External Grader Requirements>` that meets platform
  requirements.
* An :ref:`OLX definition <OLX Definition>` for the external grader.

.. _GPG Key:

GPG Key
*******

Before you can add an external grader problem, you must obtain a public GNU
Privacy Guard (GPG) key. For information about how to obtain a GPG key, see the
`GnuPG website`_.

.. _XQueue Name:

XQueue Name
***********

The external grader problems in your course must use a specific XQueue name.
You create the name for the XQueue that your course uses when you request
account credentials.

To request account credentials, contact the system administrator for your
instance of the Open edX platform.


.. _Testing the XQueue Credentials:

Testing Your XQueue Credentials
*******************************

We strongly recommend that you test your XQueue credentials when you receive
them. To test your XQueue credentials, run the following commands at a command
prompt. Replace the placeholder values with the values for your credentials.

::

  curl -v -d "username=&password=" "https://xqueue.edx.org/xqueue/login/"
  curl -v -b "sessionid=returnedbylogin"   "https://xqueue.edx.org/xqueue/get_queuelen/?queue_name=your_q"

  curl -v -d "username=&password=" "https://xqueue.edx.org/xqueue/login/"
  curl -v -b "sessionid=returnedbylogin"   "https://xqueue.edx.org/xqueue/get_queuelen/?queue_name=your_queue_name"

.. _XQueue JSON Objects:

===================
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

In the following example external grader response, the learner’s submission was
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

.. _OLX Definition:

==============
OLX Definition
==============

To create an external grader problem in Studio, you create an Open Learning XML
(OLX) definition of the problem, and then add the code to a problem component.

The OLX definition of a problem contains the following information.

* A ``queuename`` attribute that specifies the name of the XQueue that you
  created. For more information, see :ref:`XQueue Name`.

* A ``<label>`` element that contains the instructions for the problem.

* The type of input that the problem accepts, specified as one of two elements.

  * ``<textbox>``: The learner enters code in a browser field while the learner
    views the course unit.

  * ``<filesubmission>``: The learner  attaches and submits a code file in the
    unit.

* (optional) An element that contains a JSON object that you send to the
  external grader. For example, you can use the ``<grader_payload>`` element to
  tell the grader which tests to run for a problem.

The following example shows the OLX definition of a problem that uses an
external grader.

::

  <problem>
    <coderesponse queuename="my_course_queue">
      <label>Write a program that prints "hello world".</label>
      <textbox rows="10" cols="80" mode="python" tabsize="4"/>
      <codeparam>
        <initial_display>
          # students write your program here
          print ""
        </initial_display>
        <answer_display>
          print "hello world"
        </answer_display>
        <grader_payload>
          {"output": "hello world", "max_length": 2}
        </grader_payload>
      </codeparam>
    </coderesponse>
  </problem>

.. seealso::
 

 :ref:`About External Grader Problems` (concept)

 :ref:`Add an External Grader Problem` (how-to)





**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
