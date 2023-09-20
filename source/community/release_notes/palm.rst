.. _Open edX Palm Release:

Open edX Palm Release
#####################

These are the release notes for the Palm release, the 16th community release of the Open edX Platform, spanning changes from October 11, 2022, to April 11, 2023.  You can also review details about `earlier releases`_ or learn more about the `Open edX Platform`_.

.. _earlier releases: https://edx.readthedocs.io/projects/edx-developer-docs/en/latest/named_releases.html
.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
****************

Tutor minimum versions of Docker and Compose
============================================

In Palm, the minimum required versions will be `Docker v20.10.15 <https://docs.docker.com/engine/release-notes/20.10/#201015>`_ and Compose v2.0.0. These versions date back to May 2022, and not everyone can upgrade. We will do our best to keep backward compatibility with non-buildkit installations, but users will not have access to the fanciest features, such as build-time cache.

RateXBlock unsupported
======================

The RateXBlock has been deprecated and is now officially unsupported. `FeedbackXBlock 
<https://github.com/openedx/FeedbackXBlock>`_ is the recommended replacement.

Stripe API changes
==================

Ecommerce now supports the new Stripe Payment Intents API and no longer uses the Stripe Charges API. The legacy 
Stripe Charges ecommerce payment processor with a frontend in the ecommerce application is upgraded to a Stripe 
Payment Intents payment processor with a frontend in frontend-app-payment. See the discussion post, `Ecommerce: 
Changes to Stripe payment processor 
<https://discuss.openedx.org/t/ecommerce-changes-to-stripe-payment-processor/9457>`_ for more details. 

Ecommerce is still officially deprecated and we continue to work on the `Ecommerce Replacement Project 
<https://openedx.atlassian.net/wiki/spaces/AC/pages/3617849345/Ecommerce+Deprecation+and+Replacement+Project>`_.


Developer changes
=================

The old developer documentation site has been deprecated and removed. Please use `Open edX Developers - Latest 
Documentation <https://docs.openedx.org/en/latest/developers/index.html>`_  instead.

The modules :code:`tutor.hooks.actions`, :code:`tutor.hooks.filters`, and :code:`tutor.hooks.contexts` are no longer 
part of the Tutor API. This change should not affect most developers, who only use the :code:`Actions` and 
:code:`Filters` classes (notice the plural) from :code:`tutor.hooks`. If it does affect you, there are upgrade 
instructions in the discussion post, `Simplifying & documenting the Tutor Hooks API 
<https://discuss.openedx.org/t/simplifying-documenting-the-tutor-hooks-api/9258>`_

Learner Experiences
*******************

Discussions Improvements
========================

* The Posts page has been streamlined, allowing users to see more information at once.
* Post load faster 
* Comments and responses can now be sorted in reverse order.
* Filter by discussion with no responses. 

Android App updates
===================

* The Learner dashboard was updated. Profile was moved from the header to the footer. Learners can choose between viewing My Courses and My Programs. 
* The course header and course navigation have been updated
* Learners will see a course dates shift banner in the course header when the server returns that dates needs shifting, similar to behavior in the web browser. 

.. image:: /_images/community/release_notes/palm/android_shift_due_dates.png
    :width: 50%
    :alt: screenshot of Android banner for shifting due dates 

iOS App updates
===============

* Learners will see a course dates shift banner in the course header when the server returns that dates needs shifting, similar to behavior in the web browser. 

.. image:: /_images/community/release_notes/palm/ios_shift_due_dates.png
    :width: 50%
    :alt: screenshot of iOS banner for shifting due dates 


Other New Features
==================

* Support for Persian language (locale code :code:`fa_IR`) with 100% translate and reviewed.




Instructor Experiences
**********************

New Visual Problem Editor
=========================

The release includes an experimental improved problem-authoring experience with an interactive editor. When enabled, writing markdown 
code is no longer necessary. But, the advanced mode is still available, maintaining the ability to write and edit 
OLX XML.

The Open edX wiki page `[2U] New Visual Problem Editor <https://openedx.atlassian.net/wiki/spaces/OEPM/blog/2023/04/07/3724312593/2U+New+Visual+Problem+Editor>`_ 
provides a brief explanation of what has changed in the problem editor. Updated detailed instructions on writing 
problems can be found in section `8.4. Working with Problem Components <https://edx.readthedocs.io/projects/open-edx-building-and-running-a-course/en/latest/course_components/create_problem.html#working-with-problem-components>`_ of the Building and Running an edX Course documentation.

The Visual Problem Editor is hosted in the existing Course Authoring Micro-frontend. To enable the Visual Problem Editor, add the waffle flag 
:code:`new_core_editors.use_new_problem_editor` and set the value to “Yes” for all users.

New ORA Grading Experience
==========================

In this new on-platform grading experience one can easily preview common file types, assign rubric values, provide 
comments, and coordinate grading with all members of the course teams. Complete documentation is in section 
`10.26.4. Staff Grading for Open Response Assignments 
<https://edx.readthedocs.io/projects/edx-partner-course-staff/en/latest/exercises_tools/open_response_assessments/ORA_Staff_Grading.html#staff-grading-for-open-response-assignments>`_  of the Building and Running an edX Course documentation. 

The new ORA grading experience depends on the ORA Grading Micro-frontend, which was included as an experimental 
feature in Olive. To turn on the feature, add the feature flag :code:`openresponseassessment.enhanced_staff_grader`.

New Bulk Email Experience
=========================

The new bulk email experience for instructors is enabled automatically for any courses that are configured for sending bulk emails. See the Eucalyptus release notes for instructions on configuring bulk email. 

The instructor editing experience is largely the same, with choices of who to send the email to, and places to author the subject and body of the email:

.. image:: /_images/community/release_notes/palm/communications_send_an_email.png
    :alt: Send and Email interface for sending bulk emails 

The new experience also allows an experimental feature for instructors to schedule bulk emails, rather than sending them immediately. This feature requires a cron service which isn't currently included in Tutor. For more details see `Processing Scheduled Instructor Tasks <https://github.com/openedx/edx-platform/blob/b74138f2e67d9c636286f4e4633316aed051d21f/lms/djangoapps/instructor_task/docs/decisions/002-processing-scheduled-instructor-tasks.rst#L21>`_



Other Studio Updates
====================

* Using the setting, :code:`FEATURES['ENABLE_CREATOR_GROUP']`, users with CourseCreate permission can choose their organization from a drop-down in Studio. 
* Drag and Drop has been moved out of advanced problem types, and now appears along side other problems in Studio.  
* The "jump_to_id" hint in the Unit View will now pre-fill with the current location ID. This should avoid course authors copying and pasting the generic text. 


Administrators & Operators
**************************

Experimental New Learner Home Page 
==================================

The new Learner Home has many of the same features of the old learner dashboard, with some extended functionality and 
performance enhancements. Tutor operators can deploy the new Learner Home using the an `experimental learner-dashboard-mfe plugin <https://github.com/openedx/openedx-tutor-plugins/tree/main/plugins/tutor-contrib-learner-dashboard-mfe#learner-dashboard-mfe-plugin-for-tutor>`_  

* The Learner Home is now built with Paragon, the Open edX design pattern library. It is accessible and easy to style with brand colors. 
* Course cards show the course thumbnail, information about the course, and the ability to upgrade to a paid track or view/begin a course (if applicable). Further course actions (e.g. unenroll, email opt-out settings, and social media share) have been moved to the menu/triple dot icon on the course card.
* Clicking the “Refine” button opens options to filter by course status or sort either by most recent enrollment (default) or title.

.. image:: /_images/community/release_notes/palm/new_learner_home_filtering.png
    :alt: The Refine pop-up with Course State and Sort options

* All of a user’s courses are fetched on page load. To make the page manageable, we paginate that list, showing 25 courses at a time. To view other courses, a user should page through their list of courses using the pagination controls at the bottom of the course list.

.. image:: /_images/community/release_notes/palm/new_learner_home_pagination.png
    :alt: Next, previous and page number buttons appear below the list of courses

* Site staff can now masquerade as users on the platform by typing a username or email in the “View as” box and hitting submit. This is designed to be “view only” so change actions (e.g. enroll, unenroll, selecting a session) are blocked in this view.
* There is a complete list of changes in the `Open edX wiki <https://openedx.atlassian.net/wiki/spaces/OEPM/blog/2022/11/21/3584589831/2U+New+Learner+Home+Page#Comparison-with-old-experience>`_. 

Other Operator changes
======================

* Mongo is updated to v4.4. 
* Added a setting :code:`expiration_datetime_is_explicit` to the CourseMode model to override the default behavior of the Upgrade Deadline where it is set to be 10 days after the course start date. 
* Operators can now use a shared ElasticSearch installation for multiple OpenedX instances, using the setting :code:`ELASTIC_SEARCH_INDEX_PREFIX`. 
* the Micro-frontend (MFE) config setting `SUPPORT_URL` has been added to all MFEs. Use it to set the 

Settings and Toggles
====================

New Features/Toggles added since the Olive release:

* `DISABLE_JWT_FOR_MOBILE <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/openedx/core/djangoapps/oauth_dispatch/toggles.py#L10>`_
* `DISABLE_ADVANCED_SETTINGS <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/cms/envs/common.py#L520>`_
* `DISABLE_ALLOWED_ENROLLMENT_IF_ENROLLMENT_CLOSED <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/lms/envs/common.py#L1022>`_
* `ENABLE_SEND_XBLOCK_EVENTS_OVER_BUS <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/cms/envs/devstack.py#L303>`_
* `JWT_AUTH_FORCE_CREATE_ASYMMETRIC <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/openedx/core/djangoapps/oauth_dispatch/jwt.py#L198>`_
* `instructor_task.use_on_disk_grade_reporting <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/lms/djangoapps/instructor_task/config/waffle.py#L27>`_
* `learner_home_mfe.enabled <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/lms/djangoapps/learner_home/waffle.py#L13>`_
* `learner_home_mfe.enable_learner_home_amplitude_recommendations <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/lms/djangoapps/learner_home/recommendations/waffle.py#L10>`_
* `learner_recommendations.enable_course_about_page_recommendations <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/lms/djangoapps/learner_recommendations/toggles.py#L10>`_
* `learner_recommendations.enable_dashboard_recommendations <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/lms/djangoapps/learner_recommendations/toggles.py#L24>`_
* `student.enable_enrollment_confirmation_email <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/common/djangoapps/student/toggles.py#L61>`_
* `student.enable_fallback_recommendations <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/common/djangoapps/student/toggles.py#L26>`_
* `third_party_auth.apple_user_migration <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/common/djangoapps/third_party_auth/toggles.py#L9>`_
* `video_config.public_video_share <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/openedx/core/djangoapps/video_config/toggles.py#L8>`_

The following Features/Toggles were removed:

* `block_structure.raise_error_when_not_found <https://github.com/openedx/edx-platform/blob/db111c05f6d8172c5629e9d723844565ac657476/openedx/core/djangoapps/content/block_structure/config/__init__.py#L51>`_
* `credentials.use_learner_record_mfe <https://github.com/openedx/edx-platform/blob/db111c05f6d8172c5629e9d723844565ac657476/openedx/core/djangoapps/credentials/config.py#L10>`_

The following new settings were added:

* `SECURITY_PAGE_URL <https://github.com/openedx/edx-platform/blob/8e6e2997151e010276f5d76db7269c1f1d2af702/lms/envs/common.py#L3355)>`_

The following settings were removed:

* `LEARNER_RECORD_MFE_URL <https://github.com/openedx/edx-platform/blob/db111c05f6d8172c5629e9d723844565ac657476/lms/envs/common.py#L4894>`_
* `XBLOCK_SELECT_FUNCTION <https://github.com/openedx/edx-platform/blob/db111c05f6d8172c5629e9d723844565ac657476/lms/envs/common.py#L1531>`_



Deprecations & Removals
***********************

* The Django setting :code:`JWT_AUTH.JWT_PRIVATE_SIGNING_JWK` can be removed from CMS configs if it is still present, as it has only been used by the LMS for some time now.
* Most of the viewing code for PDF certificates was removed in previous releases. In the Palm release, we closed out this work with an ADR (Architecture Decision Record) on `Leaving PDF Certificate Fields in Certificates Model <https://github.com/openedx/edx-platform/blob/open-release/palm.master/lms/djangoapps/certificates/docs/decisions/008-certificate-model-remnants.rst>`_. 


Developer Experience
********************

API changes
===========

* Filter by active courses in the course listing API.
* Added :code:`certificate_available_date` to course detail API.

New filters and hook events
===========================

* Added :code:`VerticalBlockChildRenderStarted` and :code:`VerticalBlockRenderCompleted` filters that will be called at the start of rendering a vertical and after rendering is completed.
* Added :code:`AccountSettingsRenderStarted` filter which passes the account settings context before is rendered.
* Added events :code:`XBLOCK_PUBLISHED`, :code:`XBLOCK_DELETED`, and :code:`XBLOCK_DUPLICATED` to signal changes to xblocks in taxonomy-connector/course-discovery.


Researcher & Data Experiences
*****************************

* Tracking events have been added for reporting of threads, responses and comments, and for marking responses as endorsed. 


Known Issues
************

* There are no known issues at this time. 
