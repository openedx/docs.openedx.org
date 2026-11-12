.. _Migrate from XQueue:

Migrate from the XQueue Service
###############################

.. tags:: site operator, how-to

The XQueue service is deprecated and its repository is archived
(`DEPR: XQueue`_). It is not part of Open edX releases from Willow onward.
The LMS now queues external grader submissions itself, through
`edx-submissions`_, and serves the API that graders poll. This guide moves a
deployment that runs the XQueue service onto the in-platform queue.

.. contents:: Contents
  :local:
  :depth: 1

What Changes and What Does Not
******************************

Nothing changes for course teams. Existing ``<coderesponse>`` problems keep
working with the same ``queuename`` values, and the JSON exchanged with the
grader keeps the same shape.

Nothing changes in `xqueue-watcher`_'s code. It needs new configuration: the
LMS URL instead of the XQueue URL, and an LMS account instead of an XQueue
account.

What goes away is the XQueue service itself: its database, its S3 bucket, the
``lms`` user inside it, and the ``XQUEUE_INTERFACE`` settings that told the LMS
where it was.

Before You Start
****************

* Upgrade to Open edX Teak or newer.
* List the queue names in use. They are the keys of your xqueue-watcher
  ``conf.d`` files and the ``queuename`` attributes in course problems.
* If any problem uses ``<filesubmission>``, decide where the LMS will store
  uploaded files. See Step 3 of :ref:`Enable XQueue`.

Step 1: Create the Grader Account on the LMS
********************************************

Follow Step 2 of :ref:`Enable XQueue`: a Django user in the ``xqueue`` group,
exempted from ``PREVENT_CONCURRENT_LOGINS``. The XQueue service's own user
database is not consulted, so reuse the username if you like, but create it
on the LMS.

Step 2: Enable the Flag for a Pilot Course
******************************************

Turn on ``send_to_submission_course.enable`` for one course through
**Waffle_utils > Waffle flag course overrides** in Django admin. Submissions
from that course now go to edx-submissions; every other course still goes to
the XQueue service.

Step 3: Run a Watcher Against the LMS
*************************************

Start a second xqueue-watcher instance, or a second queue entry, whose
``SERVER`` is the LMS root URL and whose ``AUTH`` is the account from Step 1.
Keep the existing watcher running against the XQueue service so it drains
whatever is already queued there.

.. code-block:: json

   {
       "my_course_queue": {
           "SERVER": "https://lms.example.com",
           "AUTH": ["xqueue_watcher", "choose-a-strong-password"],
           "CONNECTIONS": 2,
           "HANDLERS": [
               {
                   "HANDLER": "xqueue_watcher.grader.Grader",
                   "KWARGS": {"grader_root": "/path/to/graders/"}
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
#. Remove ``XQUEUE_INTERFACE`` from your LMS settings. The default value is
   harmless, and the setting is slated for removal.
#. With Tutor, disable the plugin and rebuild the configuration:

   .. code-block:: shell

      tutor plugins disable xqueue
      tutor config save

Differences to Expect
*********************

The LMS API is compatible with xqueue-watcher, but it is not byte-for-byte
XQueue. If you run a custom grader, check these points against
:ref:`XQueue Reference`.

* Errors return HTTP 400, 401, 403, 404 or 409 with the usual
  ``{"return_code": 1, "content": ...}`` body. XQueue returned 200 for
  everything.
* There is no ``/xqueue/get_queuelen/`` endpoint. xqueue-watcher does not use
  it.
* ``grader_payload`` reaching the grader contains only the ``grader`` key from
  the problem's ``<grader_payload>``. Other keys are not forwarded.
* ``student_info.submission_time`` is a Unix timestamp in seconds, not
  ``YYYYMMDDHHMMSS``, and ``random_seed`` is always ``1``.
* A submission a grader pulled but never answered is offered again after five
  minutes. XQueue used ``SUBMISSION_PROCESSING_DELAY``.
* Push (passive) graders, which XQueue called with the submission, are not
  supported. The LMS only serves pull graders.
* Results reach the problem in-process. ``XQUEUE_INTERFACE["callback_url"]``
  is no longer used.

Rolling Back
************

Turning the flag off for a course sends that course's new submissions to the
XQueue service again. Submissions already queued in edx-submissions stay
there until a watcher pointed at the LMS grades them, so keep that watcher
running while you roll back.

.. seealso::

 :ref:`Enable XQueue` (how-to)

 :ref:`XQueue Reference` (reference)

 :ref:`About External Grader Problems` (concept)

.. _DEPR\: XQueue: https://github.com/openedx/public-engineering/issues/286
.. _edx-submissions: https://github.com/openedx/edx-submissions
.. _xqueue-watcher: https://github.com/openedx/xqueue-watcher

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
