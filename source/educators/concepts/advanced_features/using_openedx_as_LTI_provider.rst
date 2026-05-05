.. _Using Open edX as an LTI Tool Provider:

Using Open edX as an LTI Tool Provider
######################################

.. tags:: educator, concept

Open edX can act as an LTI tool provider, allowing you to deliver Open edX course content inside
another LMS such as Canvas, Blackboard or any system that supports the LTI 1.1.

Setting this up involves 2 roles:

1. Site operator: Enables LTI provider functionality on the Open edX instance and creates LTI 1.1
credentials for external LMS. See Configuring an Open edX Instance as an LTI Tool Provider (site
operator docs).

2. Educator: Identifies the Open edX course content to share, constructs LTI URLs for that content,
and adds LTI 1.1 configuration along with those URLs to the external LMS.

Learner Authentication Options
==============================

Site operator can configure 3 authentication methods via the LTI Consumer settings in Django admin:

1. Anonymous (default): First time a learner accesses Open edX content from the external LMS, Open
edX automatically creates a user account with a random username and a generated email address. No
personally identifiable information is stored. This mode provides the most seamless experience and learner may not even notice that Open edX is
involved.

2. Auto-create with personal information: When the "Use lti pii" option is enabled, Open edX creates
a user account using the learner's real name and email address from the LTI launch data. If a user
with the same email already exists, the existing account is linked. This mode is useful when you need to identify learners or associate their LTI activity with an
existing Open edX account.

3. Require existing account: When the "Require user account" option is enabled, the learner must
already be logged into Open edX in the same browser. If the learner is not logged in, they see an
error page with a link to the Open edX login page. After signing in, they can return to the LTI
content. This mode is useful when learners must have pre-existing accounts on the Open edX system.

If both "Use lti pii" and "Require user account" are enabled, "Require user account" takes
precedence and "Use lti pii" is ignored.

Grading
=======

When you include problem components from a graded subsection in an external LMS, Open edX grades
the learner responses and transfers the scores back to the external LMS.

If the content is an individual problem component, Open edX returns the grade for each learner
immediately after they submit an answer.

If the content is a unit or subsection, Open edX aggregates the grades and returns them after a
configurable delay (15 minutes by default).

Note the following requirements for grading to work:

1. The problem component must be in a graded subsection of your Open edX course.

2. Your external LMS may have additional requirements. For example, in Canvas, the LTI URL of a
problem component must be added to the Assignments section of a course, or to a module item that
points to an assignment. The user who launches the LTI material must be eligible to receive a
grade (that is, a learner, not a TA or course designer).

What You Need from Your Site Operator
=====================================

Before you can configure your external LMS to consume Open edX content, you need the following
from your site operator:

1. Consumer key: A unique identifier for the external LMS. Your site operator creates this when
configuring the LTI consumer in Django admin.

2. Consumer secret: A shared secret used to authenticate the LTI connection. Created alongside the
consumer key.

You will enter these values into your external LMS when setting up the LTI integration. In
addition, you will need the LTI URL for each piece of Open edX content you want to deliver.
You'll need to construct these yourself using the course ID and usage ID. See :ref:`Determine Content Addresses`.


.. note::

   Not all Open edX content types work well when delivered via LTI. For details on which component types are
   compatible, see :ref:`Content Compatibility for LTI`.



.. seealso::

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-05   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+