.. _UBC Peer Instruction:

##########################
Peer Instruction Tool
##########################

.. tags:: educator, concept

The Peer Instruction learning system provides students with in class
opportunities to discuss questions and arrive at a deeper understanding of
concepts. The peer instruction tool emulates this classroom experience for the
learners in an online course.

.. contents::
  :local:
  :depth: 2

For more information about the Peer Instruction learning system, consult the
`Turn to Your Neighbor` blog.

*********************
Assignment Overview
*********************

Assignments created with the peer instruction tool present learners with a
single select question, and then guide the learners through these stages of
the exercise.

#. An initial response, which includes both an answer choice and a written
   explanation for that choice.

#. Review of responses submitted by several other course participants.

#. A final response, which also includes an answer choice and revised
   explanation.

Learners also receive an explanation for the correct answer choice. After 10
learners complete the assignment, class breakdown histograms show the
percentage of responding learners who selected each of the answer choices, both
initially and after reviewing peer responses.

.. _Designing a Peer Instruction Assignment:

===============================================
Designing an Online Peer Instruction Assignment
===============================================

Before you use the peer instruction tool in Studio, you design the assignment.
You prepare the assignment question and its answer choices in the same way that
you would for classroom students. The question and the answer choices can
include text, images, or both.

For your online learners, you also prepare the following additional elements
for the exercise.

* A text explanation of the correct answer choice.

* An example text explanation for each answer choice.

  These example explanations ensure that all learners, including the first few
  to attempt the assignment, have other responses to review in the second stage
  of the exercise. As the number of responses received from learners increases,
  the likelihood that your examples will be shown to any given learner
  decreases.

* The number of responses for learners to review in the second stage of the
  exercise.

* The logic for selecting the responses to show.

  * The random algorithm presents the specified number of responses without
    regard to the associated answer choices. The responses shown to a learner
    might include explanations for each of the answer choices, or it might
    include several explanations for one choice and none for another choice.

  * The simple algorithm includes an additional step to minimize repeated and
    missed responses for the different answer choices. Explanations are
    presented for as many different answer choices as possible for the number
    of responses specified.

After your design is complete, you use Studio to add the assignment to your
course.

.. note:: You might consider including a Text component before the peer
 instruction component to describe the workflow that learners will experience
 in this assessment type. You might also consider including a content-specific
 discussion component after the peer instruction component to give learners an
 opportunity to continue the conversation.

.. _Enable the Peer Instruction Tool:

==================================
Enable the Peer Instruction Tool
==================================

Before you can add a component to your course structure for a peer instruction
assignment, you must enable the peer instruction tool for your course.

To enable the peer instruction tool in Studio, you add the ``"ubcpi"`` key to
the **Advanced Module List** on the **Advanced Settings** page. Be sure to
include quotation marks around the key value. For more information, see
:ref:`Enable Additional Exercises and Tools`.

.. note:: This tool was developed and contributed to the Open edX platform by the
 University of British Columbia.

.. seealso::
 

 :ref:`Add Peer Instruction Assignment` (how to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
