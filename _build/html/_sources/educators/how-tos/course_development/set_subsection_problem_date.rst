.. _Set the Assignment Type and Due Date for a Subsection:

********************************************************
Set the Assignment Type and Due Date for a Subsection
********************************************************

.. tags:: educator, how-to

You set the assignment type for problems at the subsection level.

When you set the assignment type for a subsection, all problems in the
subsection are graded and weighted as a single type. For example, if you
designate the assignment type for a subsection as **Homework**, then all
problem types in that subsection are graded as homework.

.. note::
   Unlike other problem types, by default, ORA assignments are not governed by the
   subsection due date, but are instead set in the assignment's settings. There
   is, however, a setting that allow ORAs to instead use the subsection due date.
   For details, see :ref:`PA ORA Assignment Schedule`.

To set the assignment type and due date for a subsection, follow these steps.

#. Select the **Configure** icon in the subsection box.

   The subsection settings dialog box opens.

#. On the **Basic** tab, locate the **Grading** section.
#. In the **Grade as** list, select the assignment type for this subsection.

#. For **Due Date** and **Due Time in UTC**, enter or select a due date and
   time for problems in this subsection.

   .. note:: The time that you set is in Coordinated Universal Time (UTC). You
      might want to verify that you have specified the time that you intend by
      using a time zone converter such as `Time and Date Time Zone Converter`_.

      Learners who have specified a time zone in their account settings see
      course dates and times converted to their specified time zone. Learners
      who have not specified a time zone in their account settings see course
      dates and times on their dashboards, in the body of the course, and on
      their **Progress** pages in the time zone that their browsers specify.
      Learners see other course dates and times in UTC.

#. Optionally, for a course that has the timed exam feature enabled, select the
   **Advanced** tab to set the subsection to be :ref:`timed<Timed Exams>`.

#. Select **Save**.

.. _Problem Results Visibility:

*********************************
Set Problem Results Visibility
*********************************

By default, when learners submit answers to problems, they immediately receive
the results of the problem: whether they answered the problem correctly, as
well as their scores. However, you might want to temporarily hide problem
results from learners when you run an exam, or permanently hide results when
you administer a survey. You can do this by using the **Assessment Results
Visibility** setting.

.. note::
 The **Assessment Results Visibility** setting is a subsection setting. You
 cannot change the visibility of individual problems. The **Assessment Results
 Visibility** subsection setting overrides the **Show Answer** setting for
 individual problems. Answers to problems are not visible when results are hidden.

The **Assessment Results Visibility** setting can be used with the following
common problem types.

* :ref:`Dropdown`
* :ref:`Multi select`
* :ref:`About Numerical Input`
* :ref:`Single Select`
* :ref:`Text Input`

The **Assessment Results Visibility** setting can be used with the following
advanced problem types.

* :ref:`Annotation`
* :ref:`Circuit Schematic Builder`
* :ref:`Custom JavaScript Display and Grading<Guide to Custom JavaScript Display and Grading Problem>`
* :ref:`Custom Python-Evaluated Input<About Custom Python-Evaluated Input Problem>`
* :ref:`Image Mapped Input<About Image Mapped Input Problem>`
* :ref:`Math Expression Input`
* :ref:`Problem Written in LaTeX`
* :ref:`Problem with Adaptive Hint`

To change the results visibility for your subsection, follow these steps.

#. Select the **Configure** icon in the subsection box.

   The **Settings** dialog box opens.

#. Select the **Visibility** tab, and locate **Assessment Results Visibility**.

#. Select one of the available options.

   * **Always show results**: This is the default setting. Problem results and
     subsection scores are visible immediately when learners and staff submit
     answers.
   * **Never show results**: Subsection scores are visible, but problem results
     are never visible to learners or to course staff.
   * **Show results when subsection is past due**: For learners, results are
     not visible until the subsection due date (for instructor-paced courses)
     or the course end date (for self-paced courses) has passed. For course
     staff, results are always visible unless the staff member is
     :ref:`previewing or viewing the course as a learner<Roles for
     Viewing Course Content>`.

     .. note::
      If the subsection does not have a due date, or the course does not have
      an end date, results are always visible.

#. Select **Save**.


.. seealso::
 
   :ref:`About Problems Exercises and Tools` (concept)

   :ref:`Core Problem Types` (reference)

   :ref:`Working with Problem Components` (reference)

   :ref:`Guide to Problem Settings` (reference)

   :ref:`Gradebook Assignment Types` (reference)

   :ref:`Feedback Best Practices` (concept)

   :ref:`Adding Feedback and Hints to a Problem` (reference)

   :ref:`Configure Hint` (how-to)

   :ref:`Partial Credit` (reference)

   :ref:`Set the Assignment Type and Due Date for a Subsection` (how-to)

   :ref:`Adding Tooltips` (reference)

   :ref:`Learner View of Problems` (reference)

   :ref:`Advanced Editor` (reference)

   :ref:`Add Hints via the Advanced Editor` (how-to)

   :ref:`Modifying a Released Problem` (reference)

:ref:`Add Unsupported Exercises Problems` (how-to)



**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
