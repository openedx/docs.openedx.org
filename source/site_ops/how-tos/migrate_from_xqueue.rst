.. _Migrate from XQueue:

Migrate from the XQueue Service
###############################

.. tags:: site operator, how-to

The XQueue service is deprecated and its repository is archived
(`DEPR: XQueue`_). The LMS now queues external grader submissions itself,
through `edx-submissions`_, and serves the API that graders poll. From Willow
onward the LMS can no longer send submissions to the XQueue service or receive
its results. This guide moves a deployment that runs the XQueue service onto
the in-platform queue, on Verawood or Willow.

On Verawood you can move one course at a time and roll back, using a course
waffle flag. That is the path in Steps 1 to 5, and it is the safer one:
migrate before you upgrade to Willow. If you are already upgrading, see
`Migrating During a Willow Upgrade`_. Teak and Ulmo do not serve the API the
grader polls, so upgrade to Verawood first or migrate during the Willow
upgrade.

.. contents:: Contents
  :local:
  :depth: 1

What Changes and What Does Not
******************************

Little changes for course teams. Existing ``<coderesponse>`` problems keep
working with the same ``queuename`` values, and the JSON exchanged with the
grader keeps the same shape. The one exception is ``<grader_payload>``: on
Willow only its ``grader``, ``skip_grader``, ``hide_output`` and ``lang`` keys
reach the grader, and on Verawood only ``grader``. A problem that passed other
keys, such as an expected output or a list of tests, needs its own grader file
instead.

Nothing changes in `xqueue-watcher`_'s code. It needs new configuration: the
LMS URL instead of the XQueue URL, and an LMS account instead of an XQueue
account.

What goes away is the XQueue service itself: its database, its S3 bucket, the
``lms`` user inside it, and the ``XQUEUE_INTERFACE`` settings that told the LMS
where it was. Willow removes ``XQUEUE_INTERFACE`` and the ``xqueue_callback``
URL from the LMS.

Before You Start
****************

* Upgrade to Open edX Verawood or newer.
* List the queue names in use. They are the keys of your xqueue-watcher
  ``conf.d`` files and the ``queuename`` attributes in course problems.
* If any problem uses ``<filesubmission>``, decide where the LMS will store
  uploaded files. See Step 2 of :ref:`Enable XQueue`.
* Search course exports for ``<grader_payload>`` elements with keys other than
  ``grader``, ``skip_grader``, ``hide_output`` and ``lang``. Move per-problem
  configuration into a grader file per problem. See
  :ref:`Add an External Grader Problem`.

Step 1: Create the Grader Account on the LMS
********************************************

Follow Step 1 of :ref:`Enable XQueue`: a Django user in the ``xqueue`` group,
exempted from ``PREVENT_CONCURRENT_LOGINS``. The XQueue service's own user
database is not consulted, so reuse the username if you like, but create it
on the LMS.

Verawood has no ``SINGLE_LOGIN_EXEMPT_GROUPS`` setting, so the account cannot
be exempted and every login evicts the account's other sessions. Give each
watcher connection its own account: set ``CONNECTIONS`` to 1 and use a
separate account for each queue entry and each watcher process. After the
Willow upgrade you can exempt the accounts and share one.

Step 2: Enable the Flag for a Pilot Course
******************************************

This step and Step 4 apply to releases before Willow. Willow removed the flag.

Turn on ``send_to_submission_course.enable`` for one course: in Django admin
under **Waffle_utils > Waffle flag course overrides**, add a row with the flag
name, the course ID and **Override choice: Force On**, and check **Enabled**.
A row without **Enabled** checked has no effect. Submissions
from that course now go to edx-submissions; every other course still goes to
the XQueue service.

Step 3: Run a Watcher Against the LMS
*************************************

Start a second xqueue-watcher instance, or a second queue entry, whose
``SERVER`` is the LMS root URL and whose ``AUTH`` is the account from Step 1.
Copy ``HANDLERS`` from the queue's existing entry; the graders themselves do
not change. Keep the existing watcher running against the XQueue service so it
drains whatever is already queued there.

.. code-block:: json

   {
       "my_course_queue": {
           "SERVER": "https://lms.example.com",
           "AUTH": ["xqueue_watcher", "choose-a-strong-password"],
           "CONNECTIONS": 1,
           "HANDLERS": [
               {
                   "HANDLER": "xqueue_watcher.containergrader.ContainerGrader",
                   "KWARGS": {
                       "grader_root": "/graders/",
                       "image": "registry.example.com/my-course-grader:latest",
                       "backend": "docker"
                   }
               }
           ]
       }
   }

Submit a problem in the pilot course and confirm it is graded. **Submissions >
External grader details** in Django admin shows each submission's status.

Step 4: Switch Every Course
***************************

Enable the flag for everyone:

.. code-block:: shell

   ./manage.py lms waffle_flag send_to_submission_course.enable --everyone --create

From this point the LMS no longer sends anything to the XQueue service.
Submissions already in XQueue are still graded by the old watcher and still
reach the LMS through the callback URL, so leave both running until the old
queues are empty.

Step 5: Decommission XQueue
***************************

#. Stop the old watcher instance, or remove the old queue entries.
#. Stop the XQueue service and delete its database and bucket.
#. Remove your ``XQUEUE_INTERFACE`` override from the LMS settings. Verawood
   still reads the default value, so remove the override rather than setting
   it to an empty value.
#. On Verawood, leave the ``send_to_submission_course.enable`` flag on:
   turning it off sends submissions back to the XQueue service. Delete it
   after the Willow upgrade, which removed the flag.
#. With Tutor, disable the plugin and rebuild the configuration:

   .. code-block:: shell

      tutor plugins disable xqueue
      tutor config save

Differences to Expect
*********************

The LMS API is compatible with xqueue-watcher, but it is not byte-for-byte
XQueue. If you run a custom grader, check these points against
:ref:`XQueue Reference`.

* Errors return HTTP 400, 401, 403, 404, 409 or 500 with the usual
  ``{"return_code": 1, "content": ...}`` body. XQueue returned 200 for
  everything.
* There is no ``/xqueue/get_queuelen/`` endpoint. xqueue-watcher does not use
  it.
* ``grader_payload`` reaching the grader contains the ``grader``,
  ``skip_grader``, ``hide_output`` and ``lang`` keys from the problem's
  ``<grader_payload>``. Other keys are not forwarded. Releases before Willow
  forward only ``grader``.
* ``student_info`` has no ``random_seed``. XQueue sent the problem's seed;
  xqueue-watcher does not read it. Releases before Willow send ``1``, and send
  ``submission_time`` as a Unix timestamp instead of ``YYYYMMDDHHMMSS``.
* A submission a grader pulled but never answered is offered again once five
  minutes have passed. XQueue used ``SUBMISSION_PROCESSING_DELAY``.
* Push (passive) graders, which XQueue called with the submission, are not
  supported. The LMS only serves pull graders.
* Results reach the problem in-process. There is no callback URL, and Willow
  removed the ``xqueue_callback`` view.
* ``<matlabinput>`` problems no longer queue anything. The MATLAB integration
  only worked through the XQueue service and was removed in Willow
  (`DEPR: MATLAB`_). The problems keep their scores, and a new submission is
  refused with "MATLAB problems can no longer be graded."

Migrating During a Willow Upgrade
*********************************

A Willow LMS sends every course's submissions to edx-submissions as soon as
it starts. It has no callback URL, so it cannot receive results for anything
still queued in the XQueue service.

#. Before the upgrade, let the old queues empty. Learners whose submissions
   are still queued in the XQueue service when the LMS is upgraded have to
   submit again.
#. During the upgrade, create the grader account (Step 1) and start a watcher
   pointed at the LMS (Step 3). Skip Steps 2 and 4.
#. After the upgrade, decommission XQueue (Step 5).

Rolling Back
************

Releases before Willow only. Turning the flag off for a course sends that
course's new submissions to the XQueue service again. Submissions already
queued in edx-submissions stay there until a watcher pointed at the LMS grades
them, so keep that watcher running while you roll back.

From Willow onward there is no XQueue path to roll back to.

.. seealso::

 :ref:`Enable XQueue` (how-to)

 :ref:`XQueue Reference` (reference)

 :ref:`About External Grader Problems` (concept)

.. _DEPR\: XQueue: https://github.com/openedx/public-engineering/issues/286
.. _DEPR\: MATLAB: https://github.com/openedx/public-engineering/issues/192
.. _edx-submissions: https://github.com/openedx/edx-submissions
.. _xqueue-watcher: https://github.com/openedx/xqueue-watcher

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
