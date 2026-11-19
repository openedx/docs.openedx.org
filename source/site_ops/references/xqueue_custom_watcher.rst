.. _XQueue Custom Watcher:

XQueue Custom Watcher Script
############################

.. tags:: site operator, reference

`xqueue-watcher`_'s built-in graders cover most courses. If you need your own
grading logic, the smallest option is a script that uses its ``XQueueClient``
and registers a handler. The script below accepts every submission; replace
``always_ok_handler`` with real grading. See :ref:`Enable XQueue` for the
LMS side and :ref:`XQueue Reference` for the JSON it receives and returns.


.. code-block:: python

   '''
   Minimal xqueue-watcher client that accepts every submission.

   Run it from a checkout of xqueue-watcher, with its requirements installed.
   '''
   import json
   import logging

   from xqueue_watcher.client import XQueueClient

   logging.basicConfig(
      level=logging.INFO,
      format="%(asctime)s %(levelname)s %(name)s: %(message)s"
   )
   log = logging.getLogger("mini-watcher")

   def always_ok_handler(content: dict) -> dict:
      """
      content structure (from /xqueue/get_submission/):
         {
         "xqueue_body": "<json str>",
         "xqueue_header": "<json str>",
         "xqueue_files": "<json str>"
         }

      We ignore everything and return a valid result body the LMS understands.
      """
      try:
         body = json.loads(content.get("xqueue_body", "{}"))
         # Optional: peek at what student sent
         student_response = body.get("student_response")
         log.info("Grading submission_id=%s (dummy OK). student_response=%r",
                  json.loads(content["xqueue_header"]).get("submission_id"), student_response)
      except Exception:
         pass

      # This dict becomes the JSON sent as 'xqueue_body' to /xqueue/put_result/
      return {
         "correct": True,
         "score": 1.0,
         "msg": "<div class='result-output result-correct'><h4>Graded OK</h4>"
                  "<pre>Minimal watcher: accepted.</pre></div>"
      }

   def main():
      # Adjust to your values
      QUEUE_NAME = "my_course_queue"               # the problem's queuename
      XQUEUE_URL = "http://local.openedx.io:8000"  # the LMS root URL
      XQUEUE_AUTH = ("xqueue_watcher", "password")  # a user in the xqueue group

      client = XQueueClient(
         queue_name=QUEUE_NAME,
         xqueue_server=XQUEUE_URL,
         xqueue_auth=XQUEUE_AUTH,
         http_basic_auth=None,
         requests_timeout=5,
         poll_interval=1,
         login_poll_interval=5,
         follow_client_redirects=False,
      )

      # register our trivial handler
      client.add_handler(always_ok_handler)

      # run forever (Ctrl+C to stop)
      client.run()

   if __name__ == "__main__":
      main()

.. seealso::
 
 :ref:`Enable XQueue` (how-to)

 :ref:`XQueue Reference` (reference)

 :ref:`About External Grader Problems` (concept)

 :ref:`Add an External Grader Problem` (how-to)

.. _xqueue-watcher: https://github.com/openedx/xqueue-watcher

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-03-25   |  Usama S                      |  Verawood      |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+