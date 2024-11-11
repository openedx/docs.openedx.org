.. _Interpret the Problem Grade Report:

########################################
Interpreting the Problem Grade Report
########################################

.. tags:: educator, reference

A problem grade report for your course is a time-stamped .csv file that
identifies each learner by ID, email address, and username, and provides a
snapshot of earned scores compared with the possible scores for each problem.

The problem grade report includes two columns for every problem that is
included in your grading configuration. For each homework, lab, midterm, or
final exam problem, there is one column for earned points, and one column for
possible points. In addition, the report shows the final grade score for each
learner, expressed as a decimal.

.. image:: /_images/educator_references/Problem_Grade_Report_Example.png
  :alt: An example problem grade report shown in Excel, showing the decimal
    final grade for learners as well as the earned vs possible points that they
    each achieved on several quiz assignments. A column for a midterm is only
    partially visible.

The .csv file contains one row of data for each learner, and columns that
provide the following information.

* Learner identifiers, including an internal **Student ID**, **Email** address,
  and **Username**.

* The **Grade** column shows the total score that a learner has currently
  attained in the course. This value is expressed as a decimal: a learner with
  a grade of 0.65 has earned 65% of the credit in the course, and a learner
  with a grade of 1 has earned 100%.

* For each problem (identified by assignment, subsection, and problem name), a
  column showing the number of points actually earned by each learner. If the
  learner did not attempt the assignment, the value is "Not Attempted". If the
  assignment is not available to the learner, the value in this column is "Not
  Available".

* For each problem (identified by assignment, subsection, and problem name), a
  column showing the number of points that it is possible to earn for the
  problem. If the assignment is not available to the learner, the value in
  this column is "Not Available".

.. seealso::
 :class: dropdown

 :ref:`problem_report` (how-to)