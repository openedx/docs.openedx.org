.. _Generate a Report for ORA File Submissions and Attachments:

Generate a Report for ORA File Submissions and Attachments
###########################################################

.. tags:: educator, how-to

To generate a report containing details of the ORA assignments in the course,
follow these steps.

#. View the live version of your course.

#. Select **Instructor**, and then select **Data Download**.

#. In the **Reports** section, select **Generate ORA Submission Files Archive**.

   A status message indicates that the ORA data report is being generated. This
   process might take some time to complete, but you can navigate away from this
   page and do other work while it runs.

   To check the progress of the report generation, reload the page in your
   browser and scroll down to the **Pending Tasks** section. The table shows
   the status of active tasks.

   When the report is complete, a linked .zip file name becomes available above
   the **Pending Tasks** section. File names are in the format
   ``{course_id}_submission_files_{datetime}.csv``. The most recently generated
   reports appear at the top of the list.

#. To open or save the generated ORA submission files archive, locate and select
   the link for the archive you requested.

   You can open .zip files using your computer and navigate the student's
   submissions from your file explorer.


.. _Interpret the ORA Submission Files Archive:

Interpret the ORA Submission Files Archive
*******************************************

The ORA submission files archive for your course is a zipped folder that contains
both a time-stamped .csv file listing out all included submissions as well as
folder directories with the contents of these submissions for each ORA problem
contained in your course.

This zipped directory contains a ``downloads.csv`` file which lists all available submissions,
their location, the content of any text submissions and file IDs for any attached
files included in the submission. Missing or corrupted files will be annotated with
``False`` in the ``file_found`` column of this document but will not be included in the
zipped file archive.

Inside the zipped directory there's a folder for each unit that contains an ORA
problem in the course named using the following format: ``[section_index] Section
title, [subsection_index] Subsection name, [unit_index] Unit name``.
Example: ``[1] First section, [2] Second subsection, [3] Unit name``.

Each of the folders mentioned above contain the text submissions for all students
in .txt format along with any attached files in that submission if applicable. The
filename indicates the ORA index, username (or partner ID if available) and
prompt index for a given ORA. When responses are file uploads, the name will also
include the original filename.
Example: ``[1] - john_doe - prompt_0.txt``.

.. seealso::
 

 :ref:`Open Response Assessments` (concept)

 :ref:`Accessing ORA Assignment Information` (reference)

 :ref:`List and manage students waiting in peer step` (how-to)

 :ref:`View Metrics for All ORA Assignments` (how-to)

 :ref:`PA View Metrics for Individual Steps` (how-to)

 :ref:`Generate ORA Report` (how-to)

 :ref:`PA Create an ORA Assignment` (how to)

 :ref:`Managing ORA Assignments` (how to)

 :ref:`ORA Staff Grading` (reference)

