.. _Manage Course Cohorts:

Manage Course Cohorts
#######################

.. tags:: educator, how-to

To use cohorts in your course, you must select a strategy for assigning
your learners to cohorts: automated assignment, manual assignment, or a hybrid
approach. For more information, see :ref:`Options for Assigning Learners to
Cohorts`.

.. note:: Although you can change the assignment method for cohorts at any
  time, you should have a strategy in mind as you design your course, and only
  make changes to cohorts while the course is running if absolutely necessary.

.. contents::
  :local:
  :depth: 1

You must also decide whether course-wide and content-specific discussion topics
should be divided by cohort or unified for all learners.

After you decide on a cohort strategy for your course, complete these
configuration steps (as applicable).

#. :ref:`Enable cohorts<Enable Cohorts>`.

#. Determine the method you want to use to assign learners to cohorts.

  * :ref:`Implement an automated assignment strategy<Implementing the Automated
    Assignment Strategy>`

  * :ref:`Implement a manual assignment strategy<Implementing the Manual
    Assignment Strategy>` and :ref:`manually assign enrolled learners <Assign
    Learners to Cohorts Manually>` to the cohorts that you create

  * :ref:`Use a combination of automated and manual assignment<Hybrid
    Assignment>`

3. Optionally, identify the discussion topics that you want to be divided by
   cohort.

   For information about divided discussions, see :ref:`About Divided
   Discussions`.

You complete these procedures on the **Cohorts** and **Discussions** tabs on
the Instructor Dashboard.

.. note:: On the **Cohorts** tab, the number of learners shown next to each
   cohort name in the **Select a cohort** list includes only learners who are
   enrolled in the course. The number does not include preassigned learners
   who either do not yet have an edX account or are not enrolled in your
   course.

For an optimal learner experience, you should make sure that configuration of
the cohort feature is as complete as possible before the start date of your
course. If you need to make changes to the way you have configured cohorts
while your course is running, be aware of the implications of your changes. For
more information, see :ref:`Altering Cohort Configuration`.

.. _Implementing the Automated Assignment Strategy:

***************************************************
Implementing an Automated Assignment Strategy
***************************************************

To implement an automated assignment strategy of learners to cohorts, you
:ref:`enable the cohort feature<Enable Cohorts>` for your course, and
:ref:`create cohorts<Add Cohorts>` that have the **Automatic**
:ref:`assignment method<Changing the Assignment Method of a Cohort>`. To add
learners to these cohorts, you do not need to take any action: the system
automatically and randomly assigns learners to the available automatic cohorts
when they first access any course content or divided discussions. Learners who
access the **Course** page or other course pages such as a **Textbook** page
do not receive a cohort assignment until they view course content or divided
discussions.

.. note:: You can :ref:`add learners manually<Assign Learners to Cohorts Manually>`
    to any cohort, whether it was created as an automated cohort or a
    manual cohort.

For a scenario using an automated assignment strategy, see :ref:`All Automated
Assignment`. For a scenario using a combination of automated and manual
assignment to cohorts, see :ref:`Hybrid Assignment`.

.. _About Auto Cohorts:

=================
Automated Cohorts
=================

The first time a learner views course content on the **Course** or
**Discussion** page, if she is not already assigned to a cohort, she is
randomly assigned to one of the automated cohorts. If no automated cohorts
exist, the system creates a :ref:`default cohort <Default Cohort Group>` and
assigns the learner to this cohort.

.. note:: The default cohort is created to ensure that every learner is
   assigned to a cohort. To avoid having to re-assign learners from the default
   cohort to other cohorts, make sure you create the automated cohorts that you
   want before the course starts.

.. _Implementing the Manual Assignment Strategy:

***************************************************
Implementing a Manual Assignment Strategy
***************************************************

To implement a manual assignment strategy of learners to cohorts, you
:ref:`enable the cohort feature<Enable Cohorts>` for your course, and
:ref:`create cohorts<Add Cohorts>` that have the **Manual** :ref:`assignment
method<Changing the Assignment Method of a Cohort>`. Then, you manually assign
enrolled learners to the appropriate cohorts.

.. note:: It is not a requirement that learners have enrolled in your course
   or registered on edx.org for you to add them to a cohort. For learners who
   have not yet created an edx.org account, you must provide a valid email
   address. For learners who have an edx.org account but have not yet enrolled
   in your course, you can provide either a valid email address or a
   recognized edx.org username.

Manual assignments should be as complete as possible before your course starts.
If learners enroll after your course starts, you should assign new learners to
cohorts as soon as possible. If you need to make changes to the way you have
configured cohorts while your course is running, see :ref:`Altering Cohort
Configuration`.

For a scenario using a manual assignment strategy, see :ref:`All Manual
Assignment`. For a scenario using a combination of automated and manual
assignment to cohorts, see :ref:`Hybrid Assignment`.

.. _Altering Cohort Configuration:

*************************************************
Altering Cohort Configuration in a Running Course
*************************************************

The configuration of cohorts should be complete and stable before your course
begins. Manual cohort assignments should be completed as soon as possible after
any learner enrolls, including any enrollments that occur while your course is
running.

If you decide that you must alter cohort configuration after your course starts
and activity in the course discussion begins, be sure that you understand the
consequences of these actions.

* :ref:`Changing Student Cohort Assignments`
* :ref:`Renaming a Cohort`
* :ref:`Deleting a Cohort`
* :ref:`Changing the Assignment Method of a Cohort`
* :ref:`Disabling the Cohort Feature`


.. seealso::
 

 :ref:`Cohorts Overview` (concept)

 :ref:`Enable Cohorts` (how-to)

 :ref:`Add Cohorts` (how-to)
 
 :ref:`Assign Learners to Cohorts Manually` (how-to)
 
 :ref:`Assign Learners to Cohort Groups by uploading CSV` (how-to)
 
 :ref:`Changing Student Cohort Assignments` (how-to)
 
 :ref:`Renaming a Cohort` (how-to)
 
 :ref:`Changing the Assignment Method of a Cohort` (how-to)
 
 :ref:`Disabling the Cohort Feature` (how-to)

 :ref:`Create Cohort Specific Course Content` (how-to)

 :ref:`About Divided Discussions` (concept)

 :ref:`Managing Divided Discussion Topics` (concept)

 :ref:`Best Practices for Moderating Course Discussions` (concept)

 :ref:`Set Up Divided Discussions` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
