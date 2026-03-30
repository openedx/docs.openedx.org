.. _Add an External Grader Problem:

Add an External Grader Problem in Studio
###########################################

.. tags:: educator, how-to

To create a code response problem in Studio, follow these steps.

#. In the unit where you want to add the code response problem, select
   **Problem** under **Add New Component**.

#. In the list that opens, select the **Advanced** tab, and then select **Blank
   Advanced Problem**. The :ref:`advanced editor <Advanced Editor>` opens.

#. In the new component, select **Edit**.

#. In the problem editor, enter the :ref:`online learning XML (OLX) definition <OLX Definition>` for
   the problem that you created.

#. Select **Save**.

#. Test the problem in the LMS.

.. note::

   To validate your external grader and test a problem, you must view the
   component in a published unit in the LMS. If you test a problem in Studio,
   you receive an “Error: No grader has been set up for this problem” message.

.. _OLX Definition:

OLX Definition
==============

To create an external grader problem in Studio, you create an Open Learning XML
(OLX) definition of the problem, and then add the code to a problem component.

.. note::

   Your site operations team will need to first :ref:`Enable XQueue`, and then give you the ``queuename`` to use in your problem.

The OLX definition of a problem contains the following information.

* A ``queuename`` attribute that specifies the name of the XQueue that your site operations team
  created.

* A ``<label>`` element that contains the instructions for the problem.

* The type of input that the problem accepts, specified as one of two elements.

  * ``<textbox>``: The learner enters code in a browser field while the learner
    views the course unit.

  * ``<filesubmission>``: The learner  attaches and submits a code file in the
    unit.

* (optional) An element that contains a JSON object that you send to the
  external grader. For example, you can use the ``<grader_payload>`` element to
  tell the grader which tests to run for a problem.

The following example shows the OLX definition of a problem that uses an
external grader.

::

  <problem>
    <coderesponse queuename="my_course_queue">
      <label>Write a program that prints "hello world".</label>
      <textbox rows="10" cols="80" mode="python" tabsize="4"/>
      <codeparam>
        <initial_display>
          # students write your program here
          print ""
        </initial_display>
        <answer_display>
          print "hello world"
        </answer_display>
        <grader_payload>
          {"output": "hello world", "max_length": 2}
        </grader_payload>
      </codeparam>
    </coderesponse>
  </problem>

.. _Testing the Grader:

Testing the Grader
==================

You must test the grader thoroughly, via the LMS interface, before your course
starts. Be sure to test incorrect code as well as correct code to ensure that
the grader responds with appropriate scores and messages.

If you know the grader will be unavailable at a certain time for maintenance,
you might consider :ref:`adding a course update <Add a Course Update>`.


.. seealso::

 :ref:`About External Grader Problems` (concept)

 :ref:`Enable XQueue` (site operators how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 07/03/2025   | Leira (Curricu.me)            | Sumac          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
