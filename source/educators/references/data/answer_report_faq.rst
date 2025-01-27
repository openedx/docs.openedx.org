.. _Answer_Report_FAQ:

########################################################################
Frequently Asked Questions about the Student Answer Distribution Report
########################################################################

.. tags:: educator, reference

Answers to questions about the student answer distribution report follow.

**My course doesn't have a student answer distribution report. How can I
generate it?**

Student answer distribution reports are generated automatically and refreshed
several times each day. The ``{course_id}_answer_distribution.csv`` file
displays after all of the ``{course_id}_grade_report_{date}.csv`` files. Be
sure to scroll to the end of the list of available reports.

**Why are some problems missing from this report? The ones that are missing do
have the problem types listed under** :ref:`Review_Answers`.

This report includes only problems that at least one learner has answered since
early March 2014. For those problems, this report only includes activity that
occurred after October 2013.

**Why don't I see an AnswerValue for some of my problems?**

For checkboxes and multiple choice problems, the answer choices actually
selected by a learner after early March 2014 display as described in the
previous answer. Answer choices selected by at least one learner after October
2013, but not selected since early March 2014, are included on the report but
do not include an **AnswerValue**. The **ValueID** does display the internal
identifiers, such as choice_1 and choice_2, for those answers.

**Why don't I see a Question for some of my problems?**

The value in the **Question** column is the question text that you identified
for the problem with the accessible label formatting. If you did not identify the
question text for the problem, you will not see a question. For more
information about how to set up accessible labels for problems, see
:ref:`Simple Editor`.

Also, for problems that use the **Randomization** setting in Studio, if a
particular answer has not been selected since early March 2014, the
**Question** is blank for that answer.

**My learners are saying that they answered a question, but it isn't showing up
in the report. How can that be?**

Only questions that have a **Maximum Attempts** setting of 1 or higher are
included in the report.

**I made a correction to a problem after it was released. How can I tell which
learners tried to answer it before I made the change?**

Problem **Count** values reflect the entire problem history. If you change a
problem after it is released, it may not be possible for you to determine which
answers were given before and after you made the change.

**Why is the same answer showing up in two different rows when I view the
report in a spreadsheet?**

Some spreadsheet applications can alter the data in the .csv report for display
purposes. For example, for different learner answers of "0.5" and ".5" Excel
correctly includes the two different lines from the .csv, but displays the
**AnswerValue** on both of them as "0.5". If you notice answers that appear to
be the same on separate lines with separate counts, you can review the actual,
unaltered data by opening the .csv file in a text editor.

**Why are there strange characters in the report when I view it in a
spreadsheet?**

The .csv file is UTF-8 encoded, but not all spreadsheet applications interpret
and render UTF-8 encoded characters correctly. For example, a student answer
distribution report with answer values in French displays differently in
Microsoft Excel for Mac than in OpenOffice Calc.

  Answer Values in Microsoft Excel for Mac:

   .. image:: /_images/educator_references/student_answer_excel.png
     :alt: A spreadsheet that replaces accented French characters with
      underscores.

  Answer Values in OpenOffice Calc:

   .. image:: /_images/educator_references/student_answer_calc.png
     :alt: A spreadsheet that displays accented French characters correctly.

If you notice characters that do not display as expected in a spreadsheet, try
a different spreadsheet application such as LibreOffice or Apache OpenOffice to
open the .csv file.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
