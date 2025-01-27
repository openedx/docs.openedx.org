.. _SCORM Overview:

SCORM Overview
###############

********
Overview
********

.. tags:: educator, reference

The :ref:`SCORM XBlock` provides the ability to display SCORM content within the Open edX LMS and Studio.
It can save a learners state and report scores to the progress tab of the course.
It currently supports SCORM 1.2 and SCORM 2004 standard.

***************************
SCORM Content best practice
***************************

To ensure the best experience for learners it is recommend that you keep your SCORM packages small. (1MB - 15MB)
A larger package has a longer load time and can cause a bad learner experience.

Following the rule of 1 SCORM component per unit, it is recommended that you break your content up into unit sized chunks.
This will help maintain the smaller package size.

Try to limit the SCORM package to 1 quiz or scored component.

*********************
Technical information
*********************

There are 2 events a SCORM package can emit in order to communicate with the Open edX platform.

* For a SCORM module to set the Unit as complete (trigger the completion event of Open edX), the following event needs to be emitted:
    ``scorm_set_values`` with the following key/name pair.

    * **name**: ``cmi.completion_status``
    * **value**: ``completed, incomplete, not attempted, unknown`` **(only 1)**

* For a SCORM module to send grading back to the Open edX platform, the following event need to be emitted:
    ``scorm_set_values`` with the following key/name pair.

    * **name**: ``cmi.score.raw``
    * **value**: A number that reflects the performance of the learner relative to the range bounded by the values of min and max [e.g. if the quiz is out of 10, a number between 0 and 10. The maximum being the ``Weight`` you set in for the SCORM settings above.]

.. seealso::
 :class: dropdown

 :ref:`SCORM XBlock` (how to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
