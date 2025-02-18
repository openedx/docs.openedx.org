.. _Assign Learners to Cohort Groups by uploading CSV:

Assign Learners to Cohorts by Uploading a .csv File
######################################################

.. tags:: educator, how-to

Uploading a .csv file containing a list of learners and the cohorts that you
want to assign them to is another way of assigning learners to cohorts
manually. For details about the other manual assignment method, see
:ref:`Assign Learners to Cohorts Manually`.

Any assignments to cohorts that you specify in the .csv files you upload will
overwrite or change existing cohort assignments. The configuration of your
cohorts should be complete and stable before your course begins. You should
complete manual cohort assignments as soon as possible after any learner
enrolls, especially for enrollments that occur after your course has started.
To understand the effects of changing cohort assignments after your course has
started, see :ref:`Altering Cohort Configuration`.

.. note:: Be aware that the contents of the .csv file are processed row by
   row, from top to bottom, and each row is treated independently. If the same
   learner is assigned to different cohorts in different rows in the
   spreadsheet, the last assignment to be performed is that learner's final
   assignment.

    For example, if in your .csv file Learner A is first assigned to Cohort 1,
    then later in the spreadsheet is assigned to Cohort 2, the end result of
    your .csv upload is that Learner A is assigned to Cohort 2. However, the
    upload results file will include Learner A twice in the "Learners Added"
    count: once when they are added to Cohort 1, and again when they are added
    to Cohort 2. Before submitting a file for upload, check it carefully for
    duplicated learners and other errors.

    If the same learner is assigned to a cohort that they already belong to,
    they are not included in the count of "Learners Added".


The requirements for the .csv file are summarized in this table.

.. list-table::
    :widths: 15 30

    * - **Requirement**
      - **Notes**
    * - Valid .csv file

      - The file must be a properly formatted comma-separated values file:

        * The file extension is .csv.
        * Every row must have the same number of commas, whether or not there
          are values in each cell.

    * - File size
      - The file size of .csv files for upload is limited to a maximum of 2MB.

    * - UTF-8 encoded
      - You must save the file with UTF-8 encoding so that Unicode characters
        display correctly.

        See :ref:`Creating a Unicode Encoded CSV File`.

    * - Header row
      - You must include a header row, with column names that exactly match
        those specified in "Columns" below.

    * - One or two columns identifying learners
      - You must include at least one column identifying learners:
        either "email" or "username", or both.

        To preassign learners who do not yet have accounts in your Open edX instance, you must
        provide their email addresses in an "email" column.

        If both the username and an email address are provided for a learner,
        the email address has precedence. In other words, if an email address
        is present, an incorrect or unrecognized username is ignored.

    * - One column identifying the cohort
      - You must include one column named "cohort" to identify the cohort
        to which you are assigning each learner.

        The specified cohorts must already exist in Studio.

    * -
      - Columns with headings other than "email", "username" and "cohort" are
        ignored.


To manually add learners to cohorts by uploading a .csv file, follow these
steps.

.. note:: To add learners who do not yet have accounts in your Open edX instance to cohorts using a
   .csv file upload, you must provide their email addresses in a column with
   the heading "email". Learners without accounts are "preassigned" to
   cohorts; they are not included in the count of learners "added" to cohorts.

#. View the live version of your course. For example, in Studio, select **View
   Live**.

#. Select **Instructor**, then select **Cohorts**.

#. From the **Select a cohort** list, select the cohort to which you are adding
   students.

#. Select **Assign students to cohorts by uploading a CSV file**, then select
   **Browse** to navigate to the .csv file you want to upload.

#. Select **Upload File and Assign Students**. A status message is displayed
   above the **Browse** button.

#. Verify your upload results on the **Data Download** page.

   Under **Reports Available for Download**, locate the link to a .csv file
   with "cohort_results" and the date and time of your upload in the filename.
   The list of available reports is sorted chronologically, with the most
   recently generated files at the top.

The results file provides the following information:

.. list-table::
    :widths: 15 30

    * - **Column**
      - **Description**

    * - Cohort
      - The name of the cohort to which you are assigning learners.

    * - Exists
      - Whether the cohort was found in the system. TRUE/FALSE.

        If the cohort was not found (value is FALSE), no action is taken for
        learners who you assigned to that cohort in the .csv file.

    * - Learners Added
      - The number of learners added to the cohort during the row by row
        processing of the .csv file. This number does not include learners who
        are not enrolled in the course.

    * - Learners Not Found
      - A list of the usernames of learners that could not be matched and who
        were therefore not added to the cohort.

    * - Invalid Email Addresses
      - A list of email addresses that were not valid. These learners could
        not be added to the cohort.

    * - Preassigned Learners
      - The email addresses of learners who do not yet have an account in your Open edX instance but
        who you have preassigned to a cohort using their email addresses.
        These learners are not included in the count of "Learners Added". When
        these preassigned learners create an account and enroll in your
        course, they are automatically added to the cohorts that you
        preassigned them to.


For a report that includes the cohort assignment for every enrolled learner,
review the learner profile information for your course. See :ref:`View Learner Data`.


.. _Creating a Unicode Encoded CSV File:

Creating a Unicode-encoded .csv File
*************************************

Make sure the .csv files that you upload are encoded as UTF-8, so that any
Unicode characters are correctly saved and displayed.

.. note:: Some spreadsheet applications (for example, MS Excel) do not allow
   you to specify encoding when you save a spreadsheet as a .csv file. To
   ensure that you are able to create a .csv file that is UTF-8 encoded, use a
   spreadsheet application such as Google Sheets, LibreOffice, or Apache
   OpenOffice.



.. seealso::
 

 :ref:`Cohorts Overview` (concept)

 :ref:`Manage Course Cohorts` (how-to)

 :ref:`Enable Cohorts` (how-to)

 :ref:`Add Cohorts` (how-to)
 
 :ref:`Assign Learners to Cohorts Manually` (how-to)
 
 :ref:`Changing Student Cohort Assignments` (how-to)
 
 :ref:`Renaming a Cohort` (how-to)
 
 :ref:`Changing the Assignment Method of a Cohort` (how-to)
 
 :ref:`Disabling the Cohort Feature` (how-to)

 :ref:`Create Cohort Specific Course Content` (how-to)

 :ref:`About Divided Discussions` (concept)

 :ref:`Managing Divided Discussion Topics` (concept)

 :ref:`Moderating_discussions` (concept)

 :ref:`Setting Up Divided Discussions` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
