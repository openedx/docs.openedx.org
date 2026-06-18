.. _Manage LTI PII Sharing for a Course:

Manage LTI PII Sharing for a Course
###################################

.. tags:: site operator, how-to

Some LTI tools require personally identifiable information (PII), such as a
learner's username, full name, or email address. Site operators can enable the
course-level LTI PII sharing flag for a specific course in Django Admin.

Use this guide when a course team needs to configure an LTI Consumer XBlock to
share learner information with an external LTI tool.

.. warning::

   Share only the learner information required by the LTI tool. Follow your
   organization's privacy and data governance policies before you enable the
   course-level LTI PII sharing flag.

Before You Start
****************

Before enabling the course-level LTI PII sharing flag, make sure that you have
the following information.

* Access to Studio Django Admin with permission to manage
  ``CourseAllowPIISharingInLTIFlag`` records.
* The course ID for the course that needs LTI PII sharing.
* Confirmation from the course team about which LTI tool needs learner
  information.
* Confirmation that sharing learner information with the tool is allowed by
  your organization's privacy and data governance policies.

What the Course-Level Flag Allows
*********************************

The course-level LTI PII sharing flag allows course teams to edit PII sharing
fields in Studio. After you enable the flag, course teams can configure LTI
Consumer XBlocks in the course to share learner information with an LTI tool.

Course teams decide which LTI component settings to use for the tool. For more
information, see :ref:`Allow sharing PII to LTI Components`.

Enable the Course-Level LTI PII Sharing Flag
********************************************

#. With a system administrator account, open Studio Django Admin.
#. Find :guilabel:`Course allow pii sharing in lti flags`.
#. Open the list of flags.

   .. image:: /_images/site_ops_how_tos/lti_pii_sharing_admin_1.png
      :alt: Django Admin menu showing the Course allow pii sharing in lti
         flags item.

#. Select :guilabel:`Add course allow pii sharing in lti flag`.

   .. image:: /_images/site_ops_how_tos/lti_pii_sharing_admin_2.png
      :alt: Django Admin page showing the button to add a course allow pii
         sharing in lti flag.

#. In the new flag form, enter the course ID for the course where course teams
   need LTI PII sharing.
#. Select :guilabel:`Enabled`.

   .. image:: /_images/site_ops_how_tos/lti_pii_sharing_admin_3.png
      :alt: Django Admin form for enabling PII sharing for an Open edX course.

#. Select :guilabel:`Save`.

After the flag is enabled, tell the course team that they can configure the LTI
Consumer XBlock to share only the learner information required by the tool.

Disable the Course-Level LTI PII Sharing Flag
*********************************************

To stop allowing course teams to edit LTI PII sharing fields in Studio, return
to :guilabel:`Course allow pii sharing in lti flags`, open the course flag,
clear :guilabel:`Enabled`, and save the record.

Before or after disabling the flag, ask the course team to review any LTI
Consumer XBlocks in the course that previously shared learner information.
They should clear any component-level PII sharing settings that should no
longer apply.

Next Steps
**********

Ask the course team to configure the LTI Consumer XBlock settings for the tool.
For more information, see :ref:`Allow sharing PII to LTI Components`.

.. seealso::

   :ref:`Allow sharing PII to LTI Components` (reference)

   :ref:`About the LTI Component` (concept)

   :ref:`Learner Data` (concept)

   :ref:`Set up an LTI 1_1 component` (how-to)

   :ref:`Set up an LTI 1_3 component` (how-to)

   :ref:`Configure an LTI Tool Using Reusable Configuration` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
