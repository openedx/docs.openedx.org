.. _Enabling and using LTI Advantage features:

Use and Verify LTI Advantage Features
#####################################

.. tags:: educator, how-to

This guide shows you how to use and verify LTI Advantage services after they
have been configured for an LTI 1.3 tool.

Use this guide after you complete the LTI 1.3 setup workflow. For more
information about configuring LTI Advantage settings, see :ref:`Set up an LTI
1_3 component`.

LTI Advantage services are not available for LTI 1.1/1.2 tools.

The Open edX platform supports these LTI Advantage services.

* :ref:`Assignments and Grades Services <Verifying LTI Assignments and Grades Services>`
* :ref:`Deep Linking <Enabling and using LTI Deep Linking>`
* :ref:`Names and Roles Provisioning Service <Verifying LTI Names and Roles Provisioning Service>`

.. contents:: Contents
   :local:
   :depth: 1


.. note::

   If the component uses an *Existing* reusable configuration, site operators
   manage LTI Advantage settings in LTI Store. If those settings need to change,
   contact your site operator.

.. _Verifying LTI Assignments and Grades Services:

Verify Grade Return
*******************

The LTI Assignments and Grades service (LTI-AGS) allows LTI tools to send and
manage learner grades in the Open edX gradebook.

To test grade return, follow these steps.

#. In Studio, open the LTI Consumer XBlock.
#. On the *Review Options* tab, confirm that *This activity is graded* is set to
   *Graded*.
#. Confirm that the unit is in a graded subsection.
#. Publish the unit.
#. Open the unit in the LMS as a learner.
#. Launch the tool.
#. Complete a gradable activity in the tool.
#. Confirm that the score appears in the Open edX gradebook.

If the score does not return to the Open edX platform, check these items.

* Confirm that *Assignment and Grades* is not set to *Disabled*.
* Confirm that the external tool sends scores for the selected activity.
* Confirm that the tool registration uses the correct Open edX platform values.
* Confirm that *Accept grades after due date* is set correctly for the activity.

.. TODO: Add a figure that shows a returned LTI score in the gradebook or
   learner progress view. Suggested file:
   /_images/educator_how_tos/lti_advantage_ags_grade_return.png

..
   .. figure:: /_images/educator_how_tos/lti_advantage_ags_grade_return.png
      :alt: Returned score from an LTI tool shown in the Open edX gradebook.
      :width: 100%

      After the learner completes the activity, confirm that the score returns
      to the Open edX platform.

.. _Enabling and using LTI Deep Linking:

Use Deep Linking
****************

Deep Linking allows course teams to select and configure tool content from
Studio instead of manually entering all content parameters.

To select tool content with Deep Linking, follow these steps.

#. Publish the unit that contains the LTI Consumer XBlock.
#. In Studio, open the LTI Consumer XBlock.
#. Select the *Deep Linking Launch - Configure tool* link.
#. Select the content in the external tool.
#. When the tool redirects back to Studio, confirm that the selected content is
   configured for the XBlock.
#. Select :guilabel:`Save` if Studio shows unsaved changes.
#. Publish the unit again if Studio shows unpublished changes.
#. Open the unit in the LMS and confirm that the selected content appears.

.. note::

   LTI 1.3 launches work only with published blocks. Publish the unit before
   launching or testing Deep Linking.

.. TODO: Add a figure that shows the Deep Linking Launch - Configure tool link
   in Studio. Suggested file:
   /_images/educator_how_tos/lti_advantage_deep_linking_configure_tool.png

..
   .. figure:: /_images/educator_how_tos/lti_advantage_deep_linking_configure_tool.png
      :alt: Deep Linking Launch - Configure tool link in the LTI Consumer
         XBlock.
      :width: 100%

      Use the configure tool link to launch the external tool's content
      selection workflow.

.. TODO: Add a figure that shows selected Deep Linking content configured in
   the LTI Consumer XBlock or displayed in the LMS. Suggested file:
   /_images/educator_how_tos/lti_advantage_deep_linking_selected_content.png

..
   .. figure:: /_images/educator_how_tos/lti_advantage_deep_linking_selected_content.png
      :alt: Selected Deep Linking content displayed in an Open edX course unit.
      :width: 100%

      Confirm that the selected tool content appears in the course unit.

.. _Verifying LTI Names and Roles Provisioning Service:

Verify Names and Roles Provisioning Service
*******************************************

The Names and Roles Provisioning Service (LTI-NRPS) allows a tool to retrieve
course membership and role information from the Open edX platform. Depending on
the tool and the information-sharing settings, this can include limited
personal information such as full name, email, or username.

To verify NRPS, follow the external tool's instructions for checking roster or
membership access. In most tools, a successful verification shows the course
members or confirms that the tool can retrieve the course membership service.

If the tool does not receive expected course membership information, check
these items.

* Confirm that *Names & Roles (NRPS)* is enabled for the component or reusable
  configuration.
* Confirm that the course has no more than the supported number of active
  enrollments.
* Confirm that the tool registration uses the correct Open edX platform values.
* If the tool needs username, full name, or email address, confirm the course
  PII sharing settings and the information sharing settings on the LTI Consumer
  XBlock. For more information, see :ref:`Allow sharing PII to LTI Components`.

.. TODO: Add a figure that shows a successful roster or membership check in the
   external tool. Suggested file:
   /_images/educator_how_tos/lti_advantage_nrps_roster_check.png

..
   .. figure:: /_images/educator_how_tos/lti_advantage_nrps_roster_check.png
      :alt: External LTI tool showing a successful course membership check.
      :width: 100%

      Confirm NRPS access in the external tool.

.. note::

   Due to performance concerns, LTI-NRPS information is available by default
   only on courses with up to 1000 users. Site operators may adjust this
   limit using the `LTI_NRPS_ACTIVE_ENROLLMENT_LIMIT setting`_.

.. seealso::
 
 :ref:`About the LTI Component` (concept)

 :ref:`Set up an LTI 1_3 component` (how-to)

 :ref:`Configure an LTI Tool Using Reusable Configuration` (how-to)

 :ref:`Allow sharing PII to LTI Components` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
