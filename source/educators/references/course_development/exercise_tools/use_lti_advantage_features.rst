.. _Enabling and using LTI Advantage features:
.. _LTI Advantage Services:

LTI Advantage Services
######################

.. tags:: educator, reference

LTI Advantage services extend LTI 1.3 tools beyond basic launch. This reference
describes how each service behaves in an Open edX course, the conditions
required for each service, and what course teams can expect after a service is
enabled.

LTI Advantage services are available only for LTI 1.3 tools. The external tool
must support each service that you want to use. For information about
configuring an LTI 1.3 tool, see :ref:`Set up an LTI 1_3 tool`.

.. note::

   If the component uses an *Existing* reusable configuration, the site
   operator manages LTI Advantage settings in LTI Store. If a service needs to
   be enabled, disabled, or changed, contact your site operator.


.. _Verifying LTI Assignments and Grades Services:
.. _LTI Assignment and Grade Services:

Assignment and Grade Services
*****************************

With Assignment and Grade Services (AGS), a tool can send scores to line
items in the Open edX platform. A tool can also read grade results for line
items that belong to that tool.

A line item is the AGS object that receives scores for an activity in a course.
When a tool posts a score to a line item, the Open edX platform maps that score
to the gradebook column for the corresponding LTI Consumer XBlock.

The *Assignment and Grades* setting controls how the tool works with line items.

* *Declarative* is the default mode. The Open edX platform creates one line
  item for the LTI Consumer XBlock and shares it with the tool during launch.
* *Programmatic* allows the tool to create, read, update, and remove line items
  through AGS. Use this mode only when the tool needs to manage its own line
  items, such as when one launch can contain multiple graded activities.

Open edX can receive and store a score for the LTI Consumer XBlock only when
*This activity is graded* is set to *Graded*. For the stored score to
contribute to the learner's course grade, the unit must also be part of a
graded subsection.

If a tool's score is missing, check these conditions.

* The tool supports AGS and is configured to send scores.
* *Assignment and Grades* is set to the mode required by the tool.
* The unit is published before the learner launches the tool from the LMS.
* *This activity is graded* is set to *Graded* on the *Review Options* tab.
* The unit is part of a graded subsection if the score should contribute to
  the learner's course grade.
* *Accept grades after due date* allows the timing of the grade return.
* The learner has completed the steps that the tool requires before sending a
  score.


.. _Enabling and using LTI Deep Linking:
.. _LTI Deep Linking:

Deep Linking
************

Deep Linking allows course teams to select tool content from Studio.

After Deep Linking is enabled and the LTI Consumer XBlock is saved, Studio
shows a *Deep Linking Launch - Configure tool* link on the XBlock. Selecting
that link opens the tool's content selection workflow. After the course team
selects content, the tool redirects back to Studio and updates the XBlock with
the selected content.

Some tools allow course teams to select more than one content item. When the
LTI Consumer XBlock includes multiple selected items, users see all returned
links during launch and choose which item to open.

If the *Deep Linking Launch - Configure tool* link does not appear on the XBlock
in Studio, or if Deep Linking does not work as expected, check these conditions.

* The tool supports Deep Linking.
* *Deep linking* is enabled on the *Advantage Settings* tab.
* *Deep Linking Launch URL* contains the launch URL provided by the tool for
  the content selection workflow.
* The tool is registered with the correct Open edX platform values.


.. figure:: /_images/educator_how_tos/lti_xblock_deeplink_success.png
  :alt: LTI Consumer XBlock in Studio showing saved Deep Linking content and
     the Deep Linking Launch - Configure tool link.
  :width: 80%

  After Deep Linking succeeds, Studio displays the selected content
  configuration on the LTI Consumer XBlock.


.. _Verifying LTI Names and Roles Provisioning Service:
.. _LTI Names and Role Provisioning Services:

Names and Role Provisioning Services
************************************

With Names and Role Provisioning Services (NRPS), a tool can retrieve course
membership and role information from the Open edX platform.

By default, NRPS information is available only for courses with up to 1000
active enrollments. Site operators can adjust this limit with the
``COURSE_MEMBER_API_ENROLLMENT_LIMIT`` setting.


.. seealso::

 :ref:`About the LTI Component` (concept)

 :ref:`Set up an LTI 1_3 tool` (how-to)

 :ref:`Set up an LTI tool using a reusable configuration` (how-to)

 :ref:`Allow sharing PII to LTI Components` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
