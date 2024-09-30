.. _Understanding the Progress Page:

================================
Understanding the Progress Page
================================

.. _course_completion:

Course Completion
*****************

This chart represents how much of the course content learner’s have completed.
All units that can be completed are accounted for in this chart, including readings, videos,
graded assignments, practice assignments, and assignments with future scheduled release dates.

The :ref:`Subsection Visibility Setting<Content Hidden from Students>` in Studio impacts what content is represented in the Course Completion chart.

* Course content with a **Subsection Visibility Setting** of “Entirely Hide Subsection” will not appear in the chart.

* Course content in self-paced courses with a **Subsection Visibility Setting** of “Hide content after course end date” will not appear in the chart once the course has ended.

* Course content in instructor-paced courses with a **Subsection Visibility Setting** of “Hide content after due date” will not appear in the chart once the assignment’s due date has passed.

   .. image:: /_images/educator_references/Progress_CompletionChart.png
     :alt: Pie chart representing how much course content has been completed.

.. _grades_chart:

Grades
*****************

This feature displays the minimum passing grade in the course against the learner's current grade.
The :ref:`Assessment Visibility Setting<Problem Results Visibility>` in Studio impacts the grade calculation on the **Progress** page. Different settings
determine whether a graded assignment is considered when calculating the grade to display to the learner.

* If “Always Show Results” has been selected, the assignment will be factored into this grade.

* If “Never Show Results” has been selected, the assignment will not be factored into this grade. This does not change the learner’s grade within Gradebook. This also does not impact the learner’s eligibility for a certificate.

* If “Show When Subsection is Past Due” has been selected, the assignment will only be factored into this grade when the assignment due date has passed.

Regardless of which **Assessment Visibility Setting** is selected, it will not impact the grade within the **Gradebook** of the **Student Admin** tab.
A learner's certificate eligibility is based on the grade in the **Gradebook**.

Additionally, the Grades display includes a description of the :ref:`grade range<Set the Grade Range>` set for the course. The default grade range for a course is a binary Pass/Fail.
If your course has additional ranges, they will be displayed here.

   .. image:: /_images/educator_references/Progress_Grades.png
     :alt: Example of the Grades feature where the learner's current grade is not above the minimum passing grade.

.. _grade_summary:

Grade Summary
*************

The Grade Summary table breaks down each :ref:`assignment type<Configure the Assignment Types>` available in the course and the learner's performance in each type.
The grades displayed in this section follow the same calculation criteria as the :ref:`Grades<grades_chart>` feature. To recap, an assignment will be factored into
this grade calculation if its :ref:`Assessment Visibility Setting<Problem Results Visibility>` has been set to "Always Show Results" or "Show When Subsection is Past Due".

   .. image:: /_images/educator_references/Progress_GradeSummary.png
     :alt: Grade Summary table displaying assignment types and weighted grades.

.. _detailed_grades:

Detailed Grades
***************

The Detailed Grades section is a list of all graded assignments in a course. Both the overall subsection grade
and the individual problem scores are included in this list. Assignments will not appear in this display if any of the following criteria are true:

* The assignment has its :ref:`Subsection Visibility Setting<Content Hidden from Students>` set to "Entirely Hide Subsection".

* The assignment has a future scheduled release date.

* The assignment is not graded.

   .. image:: /_images/educator_references/Progress_DetailedGrades.png
     :alt: Detailed Grades feature that displays subsection scores.

.. _certificate_status:

Certificate Status
******************

Certificate Status will only be displayed if your course has a certificate option.
If your course is eligible, this feature will describe which of the following states the learner is in:

* **Passing**, where the learner has earned the minimum grade required to earn a certificate.

* **Not passing**, where the learner has not earned the minimum grade required to earn a certificate.

* **Audit learner**, where the learner is in an audit track and does not qualify for a certificate.

* **Certificate not yet available**, where the course is instructor-paced, and the certificate will not be available until after the course end date.

* **ID not verified**, where the learner has not completed their ID verification.

* **Can request certificate**, where the learner has earned a certificate, but the certificate has yet to be generated. In this case, the learner can request a certificate.

   .. image:: /_images/educator_references/Progress_CertificateStatus.png
     :alt: Certificate Status feature describing the learner has passed and can view their certificate.
