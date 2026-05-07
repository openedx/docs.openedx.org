.. _Using Open edX as an LTI Tool Provider:

Your instance as an LTI Tool Provider
######################################

.. tags:: educator, concept

Open edX platform can act as a Learning Tools Interoperability (LTI) tool provider, allowing you to deliver Open edX course content inside
another LMS such as Canvas, Blackboard or any system that supports LTI 1.1.

Setting this up involves 2 roles:

**Site operator**: Enables LTI provider functionality on the Open edX instance and creates LTI 1.1
credentials for external LMS. See :ref:`Configuring an edX Instance as an LTI Tool Provider` (site
operator docs).

**Educator**: Identifies the Open edX course content to share, constructs LTI URLs for that content,
and adds LTI 1.1 configuration along with those URLs to the external LMS.


Content You Can Deliver
=======================

The Open edX software lets you deliver specific parts of a course via LTI.
You can share a :ref:`subsection <About Course Subsections>`,
a :ref:`unit <About Course Units>`, or an individual :ref:`component <Add a Component>`.
:ref:`Sections <About Course Sections>` are not supported.

For details on which content types work well when delivered via LTI, see :ref:`Content Compatibility for LTI`.


Learner Authentication Options
==============================

The authentication mode affects how seamlessly learners can access your course content and what you
need to configure in your external LMS. Site operators can configure 3 authentication methods via
the LTI Consumer settings in Django admin:

#. **Anonymous (default)**: First time a learner accesses Open edX content from the external LMS, a user
   account is automatically created with a random username and a generated email address. No
   personally identifiable information is stored. This mode provides the most seamless experience
   and the learner may not even notice that your Open edX instance is involved.

#. **Auto-create with personal information**: When the "Use lti pii" option is enabled, a user account is
   created using the learner's email address from the LTI launch data. If a user with the same
   email already exists, the existing account is linked. This mode is useful when you need to identify
   learners or associate their LTI activity with an existing Open edX account.

   For this to work, configure your external LMS to include ``lis_person_contact_email_primary`` in
   the LTI launch request. Without it, your Open edX instance cannot identify the learner and will create an
   account using the LTI user ID instead. You can also send ``lis_person_name_full`` (or
   ``lis_person_name_given`` and ``lis_person_name_family``) to populate the learner's display name
   on the new account, but this is optional.

#. **Require existing account**: When the "Require user account" option is enabled, the learner must
   already be logged into your Open edX instance in the same browser, and their Open edX account email must match
   the email address the external LMS sends in the launch request. If either condition is not met,
   they see an error page with a link to the login page of your Open edX instance. After signing in with the matching
   account, they can return to the LTI content. This mode is useful when learners must have
   pre-existing accounts on your Open edX instance.

   For this to work, configure your external LMS to include ``lis_person_contact_email_primary`` in
   the LTI launch request. Without it, the email match fails and the learner sees the error
   page, regardless of whether they are signed in.

If both "Use lti pii" and "Require user account" are enabled, "Require user account" takes
precedence and "Use lti pii" is ignored.


Grading
=======

When you include problem components from a graded subsection in an external LMS, the Open edX software grades
the learner responses and transfers the scores back to the external LMS.

If the content is an individual problem component, the Open edX instance returns the grade for each learner
immediately after they submit an answer.

If the content is a unit or subsection, the Open edX instance aggregates the grades and returns them after a
configurable delay (15 minutes by default).

.. note::

   Your external LMS may have additional requirements for grading to work. For example, in Canvas,
   the LTI URL of a problem component must be added to the Assignments section of a course, or to
   a module item that points to an assignment.

   Or the user who launches the LTI material must be eligible to receive a grade (that is, a learner,
   not a TA or course designer).

What You Need from Your Site Operator
=====================================

Before you can configure your external LMS to consume Open edX content, you need the following
from your site operator:

#. Consumer key: A unique identifier for the external LMS. Your site operator creates this when
   configuring the LTI consumer in Django admin.

#. Consumer secret: A shared secret used to authenticate the LTI connection. Created alongside the
   consumer key.

You will enter these values into your external LMS when setting up the LTI integration. In
addition, you will need the LTI URL for each piece of Open edX content you want to deliver.
You'll need to construct these yourself using the course ID and usage ID. See :ref:`Determine Content Addresses`.


.. note::

   Not all Open edX content types work well when delivered via LTI. For details on which component types are
   compatible, see :ref:`Content Compatibility for LTI`.



.. seealso::

   :ref:`Content Compatibility for LTI`

   :ref:`Determine Content Addresses`

   :ref:`Configuring an edX Instance as an LTI Tool Provider` (site operator)



**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-06   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-06-04   | MITx                          | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+