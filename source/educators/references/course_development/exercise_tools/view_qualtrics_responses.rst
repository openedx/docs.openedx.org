.. _View Qualtrics Responses: 

*******************************
View Survey Responses
*******************************

.. tags:: educator, reference

You can view both overall survey responses and responses for individual
learners.

=======================
View Overall Responses
=======================

To view your overall survey results and analyze data, open your survey on the
`Qualtrics website <http://www.qualtrics.com>`_.

=========================================================
View Survey Responses for an Individual Learner
=========================================================

To view a specific learner's survey responses, you must download data both
from the Insructor Dashboard and from Qualtrics, and then review the data.

Download Data from the Instructor Dashboard
**********************************************

#. In the LMS, select **Instructor**.
#. Select **Data Download**.
#. Under **Data Download**, select **Get Student Anonymized IDs CSV**. If you
   receive a prompt, specify the location where you want to save the file.

   The .csv file is saved to your computer. The file has the following name.

   ``<course name>_<course number>_<year>_<term>_anon-ids.csv``

   For more information about anonymized student IDs, see
   :ref:`Access_anonymized`.

#. Under **Reports**, select **Download profile information as a CSV**.
#. When the profile information report appears in the list under **Reports
   Available for Download**, select the report to download the .csv file to
   your computer. The file has the following name.

   ``<course name>_<course number>_<year>_<term>_student_profile_info_<date and time>.csv``

For more information about accessing learner data, see :ref:`Learner Data`.

Download Data from Qualtrics
*******************************

.. note:: Because Qualtrics is a third-party tool, the following steps might
 change without notice. See the `Qualtrics website
 <http://www.qualtrics.com>`_ for the most up-to-date Qualtrics documentation.

#. In Qualtrics, select the **View Results** tab.
#. On the page that opens, select **Download Data** in the upper left corner
   of the page.
#. On the page that opens, clear the **Compress the desired format into a .zip
   file before downloading** check box. Accept all the other default values.
#. Under **Format**, select the **This is a Comma
   Separated Values format...** link to download the .csv file.

Review the Data
******************

To associate learners' responses with their learner profiles, open the three
.csv files that you have downloaded in a program such as Microsoft Excel.

* The Qualtrics file has a **uid** column that contains each learner's
  anonymized ID, as well as columns that contain each learner's answers to the
  survey.

* The anonymized user ID file (``<course name>_<course number>_<year>_<term
  >_anon-ids.csv``) contains each learner's anonymized ID and the learner's
  edX user ID.

* The student profile data file (``<course name>_<course
  number>_<year>_<term>_student_profile_info_<date and time>.csv``) contains
  each learner's edX user ID and profile information, such as user name and
  real name.

To merge the data in the three spreadsheets so that you can see a learner’s
edX user ID, profile information, and survey responses in one place, you can
use functions such as VLOOKUP in Microsoft Excel.

.. seealso::
 :class: dropdown
