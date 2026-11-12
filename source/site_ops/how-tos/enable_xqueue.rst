.. _Enable XQueue:

Enable External Grading
#######################

.. tags:: site operator, how-to

External grader problems (``<coderesponse>`` in OLX) send learner submissions
to a grader that runs outside the LMS. The LMS queues those submissions itself,
using the `edx-submissions`_ app, and exposes the same REST API that the retired
XQueue service used to. `xqueue-watcher`_, or any grader that speaks the XQueue
API, polls the LMS directly. No separate XQueue service is needed.

If you run the XQueue service today, see :ref:`Migrate from XQueue` first.

.. contents:: Contents
  :local:
  :depth: 1

How It Works
************

#. A learner submits a response to a ``<coderesponse>`` problem.
#. The LMS stores the submission in edx-submissions, in the queue named by the
   problem's ``queuename`` attribute. A problem without a ``queuename`` uses
   ``<org>-<course>`` from the course key.
#. The grader logs in to the LMS as a dedicated user and polls
   ``/xqueue/get_submission/`` for its queue.
#. The grader posts its result to ``/xqueue/put_result/``. The LMS records the
   score and updates the learner's problem.

Prerequisites
*************

* Open edX Teak or newer.
* A grader. `xqueue-watcher`_ is the maintained reference implementation; see
  its operator guide for installing it. :ref:`XQueue Reference` describes the
  JSON that any other grader must accept and return.

Step 1: Enable the Submissions Backend
**************************************

The course waffle flag ``send_to_submission_course.enable`` routes submissions
to edx-submissions. While it is off for a course, the LMS posts that course's
submissions to the XQueue service configured in ``XQUEUE_INTERFACE`` instead.

To enable it for every course, create the flag with ``--everyone``:

.. code-block:: shell

   ./manage.py lms waffle_flag send_to_submission_course.enable --everyone --create

With Tutor:

.. code-block:: shell

   tutor local run lms ./manage.py lms waffle_flag send_to_submission_course.enable --everyone --create

To enable it for one course only, add a row in Django admin under
**Waffle_utils > Waffle flag course overrides** with the flag name, the course
ID and **Override choice: Force On**.

Step 2: Create the Grader Account
*********************************

The grader authenticates to the LMS with the username and password of a Django
user. That user must belong to a group named ``xqueue``. It does not need to be
staff or a superuser; use a dedicated service account, not a person's login.

.. code-block:: shell

   ./manage.py lms shell

.. code-block:: python

   from django.contrib.auth import get_user_model
   from django.contrib.auth.models import Group

   User = get_user_model()
   user, _ = User.objects.get_or_create(
       username="xqueue_watcher", defaults={"email": "xqueue_watcher@example.com"}
   )
   user.set_password("choose-a-strong-password")
   user.save()
   group, _ = Group.objects.get_or_create(name="xqueue")
   user.groups.add(group)

``PREVENT_CONCURRENT_LOGINS`` is on by default and keeps one session per user.
Each xqueue-watcher connection logs in as the same user, so they would evict
each other. Exempt the grader account in your LMS settings:

.. code-block:: python

   SINGLE_LOGIN_EXEMPT_GROUPS = ["xqueue"]

Step 3: Configure File Storage (File Submissions Only)
*******************************************************

For ``<filesubmission>`` problems the LMS stores the uploaded file and passes
its URL to the grader in ``xqueue_files``. Files go to Django's default storage
unless you configure a dedicated backend:

.. code-block:: python

   EDX_SUBMISSIONS = {
       "MEDIA": {
           "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
           "OPTIONS": {"bucket_name": "my-submissions-bucket"},
       }
   }

The grader must be able to fetch the URL that storage produces. Use a backend
that returns absolute, reachable URLs when the grader runs on another host.

Step 4: Point the Grader at the LMS
***********************************

In the xqueue-watcher queue configuration, set ``SERVER`` to the LMS root URL
(no ``/xqueue`` suffix) and ``AUTH`` to the account from Step 2. The key is the
queue name used by the problems' ``queuename`` attribute.

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

See the `xqueue-watcher operator guide`_ for ``SERVER_REF``, container graders
and the rest of its configuration.

Step 5: Test a Problem
**********************

#. In Studio, :ref:`add an external grader problem <Add an External Grader Problem>`
   whose ``queuename`` matches the watcher configuration, then publish the unit.
#. Start the watcher. Its log shows a successful login and polling.
#. Open the unit in the LMS as a learner and submit a response. The problem
   reports that the submission is queued, then shows the score once the grader
   replies.
#. In Django admin, open **Submissions > External grader details**. The
   submission moves from ``pending`` to ``pulled`` to ``retired``.

Troubleshooting
***************

* **The grader gets 403 Forbidden.** The account is not in the ``xqueue``
  group.
* **The grader logs in repeatedly.** ``PREVENT_CONCURRENT_LOGINS`` is evicting
  its sessions. See Step 2.
* **Submissions stay ``pending``.** No grader is polling that queue name. Check
  the problem's ``queuename`` against the watcher configuration.
* **Submissions stay ``pulled``.** The grader took the submission but never
  posted a result. The LMS offers a ``pulled`` submission to graders again
  after five minutes.
* **Submissions end up ``failed``.** Recording the score failed five times.
  Fix the cause (usually a grader reply the LMS cannot parse), then use the
  **Reset failed submissions to pending** action in the admin.
* **"No grader has been set up for this problem".** The problem was tested in
  Studio preview. External graders only run in the LMS.
* **Submissions go to the old XQueue service.** The waffle flag is off for that
  course.

Related Settings
****************

* ``XQUEUE_WAITTIME_BETWEEN_REQUESTS``: minimum seconds between two
  submissions by the same learner to the same problem. Default 5.
* ``XQUEUE_INTERFACE``: only used for courses where the flag is off. It is
  slated for removal with the rest of the XQueue service support.
* ``EDX_SUBMISSIONS["MEDIA"]``: storage for submitted files (Step 3).
* ``SINGLE_LOGIN_EXEMPT_GROUPS`` and ``SINGLE_LOGIN_EXEMPT_USERNAMES``:
  accounts exempt from single-session enforcement (Step 2).

.. seealso::

 :ref:`Migrate from XQueue` (how-to)

 :ref:`XQueue Reference` (reference)

 :ref:`XQueue Custom Watcher` (reference)

 :ref:`About External Grader Problems` (concept)

 :ref:`Add an External Grader Problem` (how-to)

.. _edx-submissions: https://github.com/openedx/edx-submissions
.. _xqueue-watcher: https://github.com/openedx/xqueue-watcher
.. _xqueue-watcher operator guide: https://github.com/openedx/xqueue-watcher/blob/master/docs/operators.md

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-03-25   |  Usama S                      |  Verawood      |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
