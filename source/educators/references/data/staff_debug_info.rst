.. _Guide to Staff Debug Info:

#############################
Guide to Staff Debug Info
#############################

.. tags:: educator, reference

The platform keeps track of learners' progress through a course -- recording
when the learner watches videos, responds to problems, and so on. If you are a
member of a course team, some of that data is visible to you for debugging
purposes. Under every problem is a **Staff Debug Info** button: selecting this
button opens a window with information about the problem.

None of this information should be necessary for day-to-day usage of your Open edX® LMS,
but for the sake of clarity, some of these fields are documented here.

``is_released``
  Indicates whether the problem is visible to learners.

``location``
  An internal unique identifier that corresponds to this problem.

``markdown``
  The text of the problem, in Markdown format. This is often written using
  Studio. Markdown is no longer supported with the release of the visual editors.

``display_name``
  The name of the problem, as shown to the learner.

``max_attempts``
  The maximum number of times that a learner can attempt to answer the problem
  correctly.

``attempts``
  The number of times that the currently logged-in learner has
  attempted to answer the problem correctly, so far. Every time this learner
  attempts to answer this question, this number will go up, until it reaches
  ``max_attempts``.

``parent``
  An internal unique identifier that corresponds to the unit that
  contains this problem.

.. seealso::
 
 :ref:`Learner Data` (concept)

 :ref:`View learner data` (how-to)

 :ref:`View Anonymized Learner IDs` (how-to)

 :ref:`Guide to the Student Profile Report` (reference)

 :ref:`Manage Learner Grades <Grades>` (how-to) 

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
