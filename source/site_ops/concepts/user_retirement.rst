.. _User Retirement Concept:

What is User Retirement?
########################

.. tags:: site operator, concept

**User retirement** is the Open edX toolset for handling requests to delete a
user account and to remove or obfuscate that user's Personally Identifiable
Information (PII) from the platform. A learner can request that their account
be deleted, and site operators can then run a process that erases or scrambles
that learner's PII across the services that make up a particular Open edX site
(the LMS, forums, credentials, and others).

.. important::

   User retirement is **not** a compliance guarantee. It makes no claim of
   satisfying any law or regulation. It is a configurable toolset that site
   operators can use to help meet the obligations apply to them specifically.
   Custom code, configuration, plugins, packages, or XBlocks on your site may
   store PII that this feature does not know about and will not clean up.
   Deciding what data must be removed, and confirming that it has been,
   remains the operator's responsibility.

Why it works the way it does
****************************

PII about a single user can live in many places: the LMS database, the
discussion forums, the credentials service, and potentially external systems
such as third-party marketing or email tools. There is no single "delete user"
button that can reach all of those places at once. Instead, user retirement is
built as a *configurable pipeline* of small steps, each of which retires some
of the user's data in one system. Operators can add, remove, or reorder
steps to match the services their site actually uses.

The main pieces
***************

User retirement is made up of a few moving parts that work together.

The account deletion UI
=======================

The learner-facing entry point is a **Delete My Account** section on the
learner's Account page. When a learner confirms deletion (by entering their
password), three things happen immediately:

* All of the learner's browser sessions are logged out and the account is
  disabled, so the learner can no longer sign in.
* A row is created in the LMS database (the ``UserRetirementStatus`` record)
  that marks the account as awaiting retirement.
* A confirmation email is sent to the learner.

At this point the account is **deactivated but not yet retired** — no PII has
been erased. Whether this UI is shown is controlled by the
``ENABLE_ACCOUNT_DELETION`` feature setting in the LMS.

The cool-off period
===================

After a deletion request, the account sits in a waiting state (called
``PENDING``) for a configurable number of *cool-off days*. During this window a
learner who changed their mind can contact the site's support or operator and
have the request cancelled, restoring the account. Only once an account has
been in the ``PENDING`` state longer than the cool-off period is it considered
ready for actual retirement. This gives operators a safety margin against
accidental or regretted deletions.

The retirement process
======================

The retirement process is the batch job that actually carries out deletions.
It is driven by a set of Python scripts (the *driver* scripts) that typically
run on a schedule, for example once a day:

#. One script asks the LMS for the list of learners whose cool-off period has
   elapsed and who are therefore ready to retire.
#. A second script then walks each of those learners, one at a time, through
   the retirement pipeline.

Retirement is modeled as a **state machine**. The LMS is the authoritative
record of where every user is in the process, tracking each user's current
state (such as ``PENDING``, ``RETIRING_ENROLLMENTS``, ``ENROLLMENTS_COMPLETE``,
and so on) and moving them forward one step at a time. The list of possible
states is stored in the LMS database rather than hard-coded, so operators can
tailor the pipeline to their needs.

Every user's journey ends in one of a few **terminal states**:

``COMPLETE``
   The user was retired successfully and their record can be cleaned up.
``ABORTED``
   The request was cancelled during the cool-off period.
``ERRORED``
   A step failed and needs an operator to investigate and resolve it.

Each step has a "working" state such as ``RETIRING_ENROLLMENTS`` and a "complete"
state such as ``ENROLLMENTS_COMPLETE``. The first indicates that the step is in
progress, while the second indicates that it has completed successfully and the
user can move on to the next step.

Because the pipeline is linear and re-runnable, a run that fails partway through
can be safely restarted by changing the user's state manually in the LMS Django
admin's ``UserRetirementStatus`` section. This area also shows any errors
from the previous run, and the last state that a user was in before a failure.

If a users's ``UserRetirementStatus`` row is set to ``PENDING`` or any
``_COMPLETE`` state (ex: ``ENROLLMENTS_COMPLETE``), the pipeline will pick
up from the *following* step on the next pipeine run.

.. important::

   Setting a user's state to any **working** state (ex: ``RETIRING_ENROLLMENTS``)
   will cause the user to be seen as "in progress" by the pipeline and ignored.
   They will be stuck in a partially retired state until manually moved. It
   is important to occasionally check that no users have been left in a working
   state for too long.

The retirement APIs
===================

Each step in the pipeline calls an API in one of the platform's services. Most
of these live in the LMS and do the real work of forgetting a user such as
unenrolling them from courses, scrubbing their forum posts, and scrambling their
username and email so that neither can be reused. The retirement pipeline
configuration maps each step to the specific service and API method it should
call, which is how operators extend the process to cover additional services or
custom data.

Deploying user retirement with Tutor
************************************

Setting up user retirement by hand involves several steps: creating a dedicated
service user with API credentials, loading the pipeline states into the LMS,
and scheduling the scripts to run.

For sites deployed with Tutor, the community-maintained
`tutor-contrib-retirement <https://github.com/cleura/tutor-contrib-retirement>`_
plugin automates most of this. It registers the OAuth2 credentials for the
retirement service worker, populates the pipeline states in the LMS, and
provides a command (and, on Kubernetes, a scheduled job) to run the retirement
process on a regular cadence with a configurable cool-off period. While not an
official part of an Open edX release, it is well maintained.

.. seealso::

   `Enabling the User Retirement Feature <https://docs.openedx.org/projects/edx-platform/en/latest/references/docs/scripts/user_retirement/docs/index.html>`_
      In-depth reference documentation on configuring the services, setting up
      the driver scripts, and extending the retirement pipeline.

   `tutor-contrib-retirement <https://github.com/cleura/tutor-contrib-retirement>`_
      Community-maintained Tutor plugin for deploying user retirement.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
