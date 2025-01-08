.. _Reusing Course Content:

Reusing Course Content with LTI
###############################

.. tags:: educator, concept

When you use LTI to reuse your course content, learners who are already
familiar with an external learning management system or other consumer
application (external LMS) see content from your Open edX instance that is
seamlessly integrated into a familiar context. Only the content that you
specify from your Open edX instance appears in the external LMS, typically
within an iframe on a page.

For example, you can set up a course on an external LMS, such as Canvas, to
include a link to a problem component that is part of a course on your
instance. The problem is included as one of the course's assignments, and
appears in Canvas like other content.

.. image:: /_images/educator_concepts/lti_canvas_example.png
  :alt: An Open edX molecule builder problem shown as part of a course running
      on a Canvas system.

This section provides background information on different aspects of the
experience that learners and course team members have when interacting with
Open edX content in the context of an external LMS.

.. contents::
   :local:
   :depth: 1

For information about the content that you can include in an external LMS, see
:ref:`Planning for Content Reuse`.

Course Roster Management
************************

Course teams manage the course roster entirely on the external LMS, as you
would for other courses that run on that platform. Learners do not use the Open
edX LMS to enroll, and the course team does not complete any enrollment
activities in Studio or the Open edX LMS.

To obtain enrollment data for the course, you use the features available in
the external LMS.

Learner Identification and Single Sign On
*****************************************

Learners do not need to navigate to a different website, or sign in to any
other system (including your Open edX instance), to access content that
originates in an course in your instance. However, the first time a learner
views Open edX course content in the external LMS, she might have to re-enter
her credentials for the external LMS, even though she is already signed in to
the external LMS.

Internally, the Open edX instance associates a unique internal identifier to
each learner's credentials to allow for a streamlined, single sign in
experience in the future. However, this separate identifier can make
some content confusing for learners when viewed in the context of an
external LMS. For example, Open edX course discussions can identify
participants by these unique IDs instead of the usernames they would normally
see in the external LMS. As a result, some Open edX content is not currently
suitable for use in an external LMS.

For more information, see :ref:`Planning for Content Reuse`.

Learner Progress and Grades
***************************

Each learner's progress through the Open edX content is saved. Learners start,
stop, and resume work in the external LMS in the same way that they would in
the Open edX LMS.

Learner responses to Open edX problem components are graded by the Open edX
system, and then transferred automatically to the grade book in the external
LMS. For more information, see :ref:`Grading Remote Content`.

To obtain learner engagement and performance data, you use the features
available in the external LMS.

.. seealso::
 :class: dropdown

 :doc: `using_openedx_as_LTI_provider` (concept)

 :doc: `/how-tos/advanced_features/lti_prepare_content` (how-to)

 :doc: `/how-tos/advanced_features/lti_determine_content_address` (how-to)

 :doc: `/references/advanced_features/planning_content_reuse` (reference)

 :doc: `/references/advanced_features/lti_canvas_example` (reference)

 :doc: `/references/advanced_features/lti_blackboard_example` (reference)
