.. _OLX Completion: 

########################################
Add the Completion Tool to an OLX Course
########################################

.. tags:: educator, how-to

To add the completion tool to a unit in an OLX (open learning XML) course, it
is sufficient to add the ``<done>`` tag to the OLX.

It is recommended that you also explicitly specify a ``url_name`` within the
``<done>`` tag, as shown in the following example. If you do not explicitly
specify a ``url_name``, a value is automatically assigned, which can be
problematic if the same course is imported several times. For example, if the
``url_name`` value is automatically generated each time you import your
course, and if you import your course more than once, the learner state for
the associated problems is lost each time a new ``url_name`` value is assigned.

 .. code-block:: xml

    <done url_name="video_3_completion"/>

.. seealso::
 

 :ref:`About the Completion Tool` (reference)

 :ref:`Enable Completion` (how to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
