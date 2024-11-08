.. :diataxis-type: concept
.. _External Grader:

###########################
External Grader
###########################

An external grader is a service that receives learner responses to a
problem, processes those responses, and returns feedback and a problem
grade to the platform. Course teams build and deploy a grader on an
external platform, such as Amazon Web Services (AWS) or Azure, and then
link their external grader to the platform using an interface called
XQueue. XQueue is a Representational State Transfer (RESTful) interface
that uses JavaScript Object Notation (JSON) objects.

For more information, see the following sections.

.. contents::
  :local:
  :depth: 1

.. _External Grader Workflow:

**************************
External Grader Workflow
**************************

XQueue uses the following workflow for external grader problems.

#. In the learning management system (LMS), the learner either enters code or
   attaches a file for a problem, then selects **Submit**.
#. The LMS sends the learner's code to XQueue.
#. The external grader actively retrieves, or pulls, the code from XQueue.
#. The external grader runs the tests that you created on the code.
#. The external grader returns the grade for the submission, as well as any
   messaging in a JSON, to XQueue.
#. The XQueue delivers the results to the LMS.
#. In the LMS, the learner sees the problem results and the grade.

For the code for the XQueue interface, see the ``urls.py`` file in the `edX
XQueue repository`_.

.. _External Grader Example:

***************************
External Grader Example
***************************

An external grader is particularly useful for software programming courses
where learners are asked to submit complex code. The grader can run tests that
you define on that code and return results to a learner.

For example, you define a problem that requires learners to submit Python code,
and create a set of tests that an external grader can run to verify the
submissions. When a learner enters Python code for the problem and selects
**Submit**, the LMS sends the code to the grader for testing. If the code
passes all tests, the grader returns the score and a message indicating that
the solution is correct. The learner can see the message by selecting **See
full output**. A message can be useful when the learner's solution is not
correct and you want to return information about the failed tests, as in the
following example.


.. image:: /_images/educator_concepts/external-grader.png
 :alt: A learner's view of a programming problem that uses an external grader,
     with an incorrect result.


.. _External Grader Requirements:

============================
External Grader Requirements
============================

The course team builds and deploys the external grader.

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
  you should :ref:`add a course update <Add a Course Update>`.

* You must test the grader thoroughly before your course starts. Be sure to
  test incorrect code as well as correct code to ensure that the grader
  responds with appropriate scores and messages.

.. seealso::
 :class: dropdown

 :ref:`External Grader Problem Requirements` (reference)

 :ref:`Create an External Grader Problem in Studio` (how-to)
