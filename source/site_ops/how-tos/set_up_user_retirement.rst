.. _Set Up User Retirement:

Set Up User Retirement
######################

.. tags:: site operator, how-to

This how-to walks through enabling the :ref:`user retirement <User Retirement Concept>`
feature so that your site can act on learner requests to delete their accounts.
For background on how retirement works, see :ref:`User Retirement Concept`.

Setting retirement up by hand involves creating a dedicated service user with
API credentials, loading your instance's specific pipeline states into the LMS,
and scheduling the driver scripts to run. The steps below use the
community-maintained
`tutor-contrib-retirement <https://github.com/cleura/tutor-contrib-retirement>`_
plugin, which automates that setup for Tutor deployments. If you do not use
Tutor, see :ref:`Configure retirement without Tutor` below.

.. note::

   This plugin is not an official part of an Open edX release and focuses on
   LMS retirement. If your site stores PII in other services (ex: analytics, A/B
   testing, 3rd party email, etc.) and you want to retire that data using this
   process, you will need to extend the pipeline yourself. See the reference docs
   linked under :ref:`See Also <User Retirement See Also>`.

Prerequisites
*************

* A working Tutor deployment that you can restart.
* Shell access to the host running Tutor.
* Permission to make LMS Django admin changes, which you will use to operate
  the feature after setup.

Enable the plugin with Tutor
****************************

#. **Choose a compatible plugin version.** The plugin is versioned to match
   Open edX and Tutor releases. Consult the `version compatibility matrix
   <https://github.com/cleura/tutor-contrib-retirement#version-compatibility-matrix>`_
   and pick the release (or branch) that matches the version you are deploying.

#. **Install the plugin**, substituting the version you selected above:

   .. code-block:: shell

      pip install git+https://github.com/cleura/tutor-contrib-retirement@v5.4.2

#. **Enable the plugin:**

   .. code-block:: shell

      tutor plugins enable retirement

#. **Build the retirement Docker image**, which packages the driver scripts:

   .. code-block:: shell

      tutor images build retirement

#. **Initialize your deployment** so the plugin can register the retirement
   service worker as an OAuth2 client in the LMS and populate the retirement
   pipeline stages:

   .. code-block:: shell

      # for a local deployment
      tutor local do init

      # for a Kubernetes deployment
      tutor k8s do init

Configure the cool-off period
*****************************

The *cool-off period* is the number of days an account waits in the
``PENDING`` state before it becomes eligible for retirement, giving learners a
window to rescind their request. It defaults to 30 days.

To change it (and any other setting), use ``tutor config save``:

.. code-block:: shell

   tutor config save --set RETIREMENT_COOL_OFF_DAYS=14

Rescinding a retirement during cool-off
***************************************

Generally to rescind a retirmement request (only during the cool-off period), the user
would contact the institution's support. In order for support to rescind a retirement
on behalf of a user they can use the management command:

.. code-block:: shell

    # for a local deployment
    tutor local run lms ./manage.py lms cancel_user_retirement_request <original_email_address>

The command takes the following steps:

#. Restores the user's email address back to the original.
#. Resets the password to a random 25-char value — so the learner must go through **password reset** to log back in.
#. Deletes the `UserRetirementStatus` row (the "permanent" retirement request record is cleaned up via a Django signal).

Retirement settings
*******************

The available settings and their defaults are:

- ``ENABLE_ACCOUNT_DELETION`` (default ``True``)
   Whether or not the learner facing "Delete My Account" flow is enabled.

- ``RETIREMENT_COOL_OFF_DAYS`` (default ``30``)
   Days an account must sit in ``PENDING`` before it is retired.

- ``RETIREMENT_EDX_OAUTH2_CLIENT_ID`` (default ``retirement_service_worker``)
   OAuth2 client ID registered for the retirement service worker.

- ``RETIREMENT_K8S_CRONJOB_SCHEDULE`` (default ``"0 0 * * *"``)
   Cron schedule for the Kubernetes retirement job (default: daily at midnight).

- ``RETIREMENT_K8S_CRONJOB_HISTORYLIMIT_SUCCESS`` (default ``3``)
   Number of successful job runs to retain in history.

- ``RETIREMENT_K8S_CRONJOB_HISTORYLIMIT_FAILURE`` (default ``1``)
   Number of failed job runs to retain in history.

After saving configuration (``tutor config save``), re-initialize the deployment (ex:
``tutor local do init``) so the new values take effect.

Run the retirement pipeline
***************************

Running the pipeline retires every learner whose cool-off period has elapsed,
walking each one through the pipeline stages.

For a **local** deployment, run it on demand:

.. code-block:: shell

   tutor local retire-users

To run it regularly, invoke that command from a cron job on the host, for
example once a day.

For a **Kubernetes** deployment, the plugin installs a ``CronJob`` that runs
the pipeline automatically on the schedule set by
``RETIREMENT_K8S_CRONJOB_SCHEDULE`` — no manual step is required.

Operate the feature
*******************

Day-to-day operation happens in the LMS Django admin, under the
``UserRetirementStatus`` section.

* **Confirm the deletion UI is available.** The learner-facing **Delete My
  Account** section is controlled by the ``ENABLE_ACCOUNT_DELETION`` feature in
  the LMS settings. It is enabled by default.

* **Cancel a request during cool-off.** If a learner asks to keep their
  account, cancel their request while it is still in the ``PENDING`` state. This
  moves the account to the ``ABORTED`` terminal state and restores it.

* **Recover from an error.** If a user lands in the ``ERRORED`` state, the
  ``UserRetirementStatus`` record shows the last state reached and the error.
  After resolving the underlying problem, set the user's state back to
  ``PENDING`` or to the ``_COMPLETE`` state of the last step that succeeded; the
  next run picks up from the following step.

.. important::

   Do not leave a user in a *working* state such as ``RETIRING_ENROLLMENTS``.
   The pipeline treats those users as "in progress" and skips them, so they stay
   partially retired until moved manually. Check periodically that no accounts
   are stuck in a working state.

.. _Configure retirement without Tutor:

Configure retirement without Tutor
**********************************

If you do not use Tutor, you must perform the same setup manually: create the
retirement service user and OAuth2 credentials, load the pipeline states into
the LMS, configure the driver scripts, and schedule them to run. The Open edX
reference documentation covers each of these steps in detail; see the links
below.

.. _User Retirement See Also:

.. seealso::

   :ref:`User Retirement Concept`
      Conceptual overview of how user retirement works.

   `Enabling the User Retirement Feature <https://docs.openedx.org/projects/edx-platform/en/latest/references/docs/scripts/user_retirement/docs/index.html>`_
      In-depth reference documentation on configuring the services, setting up
      the driver scripts, and extending the retirement pipeline.

   `tutor-contrib-retirement <https://github.com/cleura/tutor-contrib-retirement>`_
      Community-maintained Tutor plugin for deploying user retirement.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|   2026-07-28 | Ty Hob                        | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
