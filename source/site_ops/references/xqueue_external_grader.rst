.. _XQueue Reference:

XQueue Reference
############################

.. tags:: site operator, reference

This reference describes the interface between the LMS and an external
grader: the HTTP endpoints the grader calls and the JSON exchanged. The LMS
serves this API itself; see :ref:`Enable XQueue` for setting it up. The name
"XQueue" is kept for compatibility with the retired XQueue service and with
`xqueue-watcher`_, which implements the grader side.

.. contents::
  :local:
  :depth: 1

Once properly set up, an :ref:`OLX definition <OLX Definition>` for the external grader can be defined in Studio.

.. _External Grader Requirements:

External Grader Requirements
============================

When you build your external grader, keep the following requirements in mind.

* The grader must accept and return JSON objects. For more information, see
  :ref:`XQueue JSON Objects`.

* The grader must actively retrieve, or pull, submissions from the LMS
  through the endpoints below at regular intervals. The LMS does not push
  submissions to graders.

* The grader must be scalable. Many learners might submit responses at one
  time, such as shortly before an exam is due. The grader must be able to
  process many submissions in a limited time, without failure or unexpected
  delays.

* The grader must post a result for every submission it pulls. A submission
  that is pulled and not answered is offered to graders again after five
  minutes.

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
  whether the problem is with your grader or the LMS.

  If you know the grader will be unavailable at a certain time for maintenance,
  you might consider contacting course teams so they can :ref:`add a course update <Add a Course Update>`.

.. _XQueue Endpoints:

Endpoints
=========

All endpoints are relative to the LMS root URL. Every response body is
``{"return_code": 0, "content": ...}`` on success and
``{"return_code": 1, "content": "<message>"}`` on failure, with an HTTP status
that matches the outcome.

.. list-table::
   :header-rows: 1
   :widths: 30 10 60

   * - Endpoint
     - Method
     - Purpose
   * - ``/xqueue/login/``
     - GET, POST
     - GET sets the CSRF cookie. POST ``username`` and ``password`` to open a
       session. The user must be in the ``xqueue`` group for every other
       endpoint.
   * - ``/xqueue/logout/``
     - POST
     - End the session.
   * - ``/xqueue/get_submission/``
     - GET
     - ``?queue_name=<name>``. Returns the oldest waiting submission in that
       queue and marks it pulled. ``content`` is the submission JSON below, as a
       string. An empty queue returns ``return_code`` 1 with HTTP 200.
   * - ``/xqueue/put_result/``
     - POST
     - Post the grader response below. Requires the ``submission_key`` that
       came with the submission. Returns 403 for a wrong key, 404 for an
       unknown submission, 409 if another grader is posting for the same
       submission.
   * - ``/xqueue/status/``
     - POST
     - Liveness check.

Mutating requests after login need the ``X-CSRFToken`` header set from the
``csrftoken`` cookie. xqueue-watcher handles this.

.. _XQueue JSON Objects:

XQueue JSON Objects
===================

Both the learner submission that the LMS sends to the grader, and the response
that the grader sends back, are JSON objects. Each of the three top-level
values is itself a JSON-encoded string.

.. note::
  The LMS does not send the learner ID to the external grader. Your grader
  cannot access IDs or associate learner IDs with submissions.

.. _XQueue Learner Submissions:

Learner Submissions
*******************

The grader receives a JSON object with the following keys.

* ``xqueue_header``: Identifies the submission. Return it unchanged in the
  ``xqueue_header`` of the grader response.

  * ``submission_id``: The submission's integer ID.

  * ``submission_key``: A secret issued when the submission was pulled. Only
    the grader that holds it can post the result.

* ``xqueue_files``: A dictionary that maps each file name the learner
  submitted to a URL from which the grader can download it. Empty unless the
  problem uses ``<filesubmission>``.

* ``xqueue_body``: The submission.

  * ``student_info``: Information about the learner in relation to this
    submission.

    * ``anonymous_student_id``: An anonymized identifier of the learner.

    * ``submission_time``: A Unix timestamp, in seconds, as a string.

    * ``random_seed``: Always ``1``.

  * ``student_response``: The learner's code, entered in the LMS or read from
    an attached file.

  * ``grader_payload``: A JSON string containing only the ``grader`` key from
    the problem's ``<grader_payload>`` element. Other keys in the element are
    not forwarded. For more information, see
    :ref:`Add an External Grader Problem`.

An example learner submission follows, shown with each value decoded. On the
wire, ``xqueue_header``, ``xqueue_files`` and ``xqueue_body`` are each a
JSON-encoded string, and ``student_info`` and ``grader_payload`` inside the
body are JSON-encoded strings too.

::

  {
    "xqueue_header": {
      "submission_id": 72,
      "submission_key": "ffcd933556c926a307c45e0af5131995"
    },
    "xqueue_files": {
      "helloworld.c": "https://storage.example.com/my_course_queue/0f1e2d3c"
    },
    "xqueue_body": {
      "student_info": {
        "anonymous_student_id": "106ecd878f4148a5cabb6bbb0979b730",
        "submission_time": "1711276541",
        "random_seed": 1
      },
      "student_response": "def double(x):\n return 2*x\n",
      "grader_payload": {"grader": "problem_2/grade.py"}
    }
  }

.. _XQueue External Grader Responses:

External Grader Responses
*************************

After the grader runs tests and records the results for a submission, the
grader posts a JSON response to ``/xqueue/put_result/``. It contains the
header it received and a body with the following keys.

* ``correct``: Whether the submission was correct.
* ``score``: A number from 0 to 1. The LMS multiplies it by the problem's
  possible points and rounds to the nearest integer.
* ``msg``: HTML shown to the learner under **See full output**.

In the following example external grader response, the learner's submission was
correct, the score was 1, and the tests created a brief message. As with the
submission, both values are sent as JSON-encoded strings.

::

  {
    "xqueue_header": {
      "submission_id": 72,
      "submission_key": "ffcd933556c926a307c45e0af5131995"
    },
    "xqueue_body": {
      "correct": true,
      "score": 1,
      "msg": "<p>The code passed all tests.</p>"
    }
  }

.. _XQueue Submission Lifecycle:

Submission Lifecycle
====================

Each submission has a status, visible in Django admin under **Submissions >
External grader details**.

* ``pending``: Waiting for a grader.
* ``pulled``: Handed to a grader. Offered again after five minutes without a
  result.
* ``retired``: Graded. The score is recorded and the learner's problem is
  updated.
* ``retry``: Recording the score failed. The submission is offered again.
* ``failed``: Recording the score failed five times. An admin action resets
  ``failed`` submissions to ``pending``.

.. seealso::

 :ref:`Enable XQueue` (how-to)

 :ref:`Migrate from XQueue` (how-to)

 :ref:`XQueue Custom Watcher` (reference)

 :ref:`About External Grader Problems` (concept)

 :ref:`Add an External Grader Problem` (how-to)

.. _xqueue-watcher: https://github.com/openedx/xqueue-watcher

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-03-25   |  Usama S                      |  Verawood      |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
