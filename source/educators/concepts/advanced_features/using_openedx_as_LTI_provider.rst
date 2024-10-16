.. :diataxis-type: concept

.. _Using Open edX as an LTI Tool Provider:

#######################################
Using Open edX as an LTI Tool Provider
#######################################

.. note:: This feature was a closed pilot experiment. This feature is not
 supported for new users.

An experimental feature enabled the edX Edge site to be configured  to be a
learning tool interoperability (LTI) provider to other systems and  applications
that partner institutions use. After initial configuration and testing between
Edge and your system or application is complete, course teams could use this
feature to reuse Edge course content, including advanced problem types and
videos, in an on campus or in house learning management system. Examples
currently include courses running on Canvas and Blackboard.

You can also include content from an LTI provider in your edX courses. For
more information, see :ref:`LTI Component`.

.. _Reusing Course Content:

**********************************
Reusing Course Content with LTI
**********************************

.. note:: This feature was a closed pilot experiment. This feature is not
 supported for new users.

When you use LTI to reuse edX course content, learners who are already familiar
with an external learning management system or other consumer application
(external LMS) see content from edX that is seamlessly integrated into a
familiar context. Only the content that you specify from edX appears in the
external LMS, typically within an iframe on a page.

For example, you can set up a course on an external LMS, such as Canvas, to
include a link to a problem component that is part of an edX course. The
problem is included as one of the course's assignments, and appears in Canvas
like other content.

.. image:: /_images/educator_concepts/lti_canvas_example.png
  :alt: An edX molecule builder problem shown as part of a course running on a
      Canvas system.

This section provides background information on different aspects of the
experience that learners and course team members have when interacting with edX
content in the context of an external LMS.

.. contents::
   :local:
   :depth: 1

For information about the content that you can include in an external LMS, see
:ref:`Preparing Content`.

**********************************
Course Roster Management
**********************************

Course teams manage the course roster entirely on the external LMS, as you
would for other courses that run on that platform. Learners do not use the edX
LMS to enroll, and the course team does not complete any enrollment activities
in Studio or the edX LMS.

To obtain enrollment data for the course, you use the features available in
the external LMS.

******************************************
Learner Identification and Single Sign On
******************************************

.. only:: Partners

  .. note:: Different configuration options are available for how an external
   LMS and edX Edge authenticate users. Your DevOps team is likely to have
   additional information about the specific authentication process used by
   your institution.

Learners do not need to navigate to a different website, or sign in to any
other system (including edX), to access content that originates in an edX
course. However, the first time a learner views edX course content in the
external LMS, she might have to re-enter her credentials for the external LMS,
even though she is already signed in to the external LMS.

Internally, the edX instance associates a unique internal identifier to each
learner's credentials to allow for a streamlined, single sign in experience in
the future. However, this separate edX identifier can make some edX content
confusing for learners when viewed in the context of an external LMS. For
example, edX course discussions can identify participants by their edX IDs
instead of the usernames they would normally see in the external LMS. As a
result, some edX content is not currently suitable for use in an external LMS.

For more information, see :ref:`Preparing Content`.

******************************
Learner Progress and Grades
******************************

Each learner's progress through the edX content is saved. Learners start, stop,
and resume work in the external LMS in the same way that they would in the edX
LMS.

Learner responses to edX problem components are graded by the edX system, and
then transferred automatically to the grade book in the external LMS. For more
information, see :ref:`Grading Remote Content`.

To obtain learner engagement and performance data, you use the features
available in the external LMS.

.. _Grading Remote Content:

******************************
Grading Remote Content
******************************

.. note:: This feature was a closed pilot experiment. This feature is not
 supported for new users.

When you include the problem components in a graded edX subsection in an
external LMS, the edX system grades the learner responses to those problems.
The edX system then transfers the learner scores back to the external LMS. This
exchange between an external LMS, the edX system, and the external LMS again is
near real time. It can take a few moments to complete this exchange for a
single problem component, and up to several minutes to return aggregated scores
of all of the problems in a unit or subsection.

When you include edX problem components in an external LMS, note the following
requirements.

* The edX problem component must be in one of the graded subsections in your
  course.

* Your external LMS might also require that you use a specific part of the
  course for graded content. For example, in Canvas, you must add the LTI URL
  of a problem component to the "Assignments" section of a course, or to a
  module item that points to an assignment. In addition, the user who launches
  the LTI material must be eligible to get a grade for the assignment; that is,
  a learner and not a TA or course designer.

For more information about constructing an LTI URL for a course component, see
:ref:`Determining Content Addresses`.

.. seealso::
 :class: dropdown

  :ref:`Create a Duplicate Course for LTI use` (how-to)
  :ref:`Determine Content Addresses when using Open edX as an LTI Provider<Determine Content Addresses>` (how-to)
  :ref:`Planning for Content Reuse (LTI)<Planning for Content Reuse>` (reference)
  :ref:`Example: edX as an LTI Provider to Canvas<edX as an LTI Provider to Canvas>` (reference)
  :ref:`Example: edX as an LTI Provider to Blackboard<edX as an LTI Provider to Blackboard>` (reference)