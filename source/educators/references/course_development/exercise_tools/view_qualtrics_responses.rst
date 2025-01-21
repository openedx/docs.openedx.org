.. _View Qualtrics Responses: 

View Survey Responses
######################

.. tags:: educator, reference

You can view both overall survey responses and responses for individual
learners.


View Overall Responses
***********************

To view your overall survey results and analyze data, open your survey on the
`Qualtrics website <http://www.qualtrics.com>`_.


View Survey Responses for an Individual Learner
=========================================================

To view a specific learner's survey responses, you must download data both
from the Insructor Dashboard and from Qualtrics, and then review the data.

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

 :ref:`Poll Tool for OLX` (reference)

 :ref:`Qualtrics Survey` (how to)
