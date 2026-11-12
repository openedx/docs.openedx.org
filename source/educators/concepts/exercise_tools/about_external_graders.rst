.. _About External Grader Problems:

About External Grader Problems
##############################

.. tags:: educator, concept

An external grader is a service that receives learner responses to a
problem, processes those responses, and returns feedback and a problem
grade to the platform. Course teams build and deploy a grader on an
external platform, such as Amazon Web Services (AWS) or Azure, and the
grader connects to the LMS through an interface called XQueue. XQueue is a
Representational State Transfer (RESTful) interface that uses JavaScript
Object Notation (JSON) objects. Most course teams run their grader with
`xqueue-watcher`_, which implements that interface.

For more information, see the following sections.

.. contents::
  :local:
  :depth: 1

.. _External Grader Workflow:

External Grader Workflow
************************

External grader problems use the following workflow.

#. In the learning management system (LMS), the learner either enters code or
   attaches a file for a problem, then selects **Submit**.
#. The LMS places the submission in the queue named by the problem.
#. The external grader actively retrieves, or pulls, the submission from the
   LMS.
#. The external grader runs the tests that you created on the code.
#. The external grader returns the grade for the submission, as well as any
   messaging in a JSON, to the LMS.
#. In the LMS, the learner sees the problem results and the grade.

Your site operations team runs the grader and tells you the queue name to use
in your problems. For the interface, see :ref:`XQueue Reference`.

.. _External Grader Example:

External Grader Example
***********************

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


External Grader Requirements
============================

Your site operations team :ref:`builds and deploys the external grader <Enable XQueue>`.


.. seealso::

 :ref:`Add an External Grader Problem` (how-to)

 :ref:`Enable XQueue` (site operators how-to)

 :ref:`XQueue Reference` (site operators reference)

.. _xqueue-watcher: https://github.com/openedx/xqueue-watcher

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
