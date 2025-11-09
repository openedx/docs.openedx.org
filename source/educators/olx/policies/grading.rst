.. _Grading Policy:

#################################
Create OLX Grading Policy
#################################

.. tags:: educator, how-to

You create a grading policy file to specify how problems are graded in your
course.

.. contents::
  :local:
  :depth: 1

*******************************
Create the Grading Policy File
*******************************

You define policies for your course in the ``grading_policy.json`` file.

Save the ``grading_policy.json`` file in the ``policy/<course-name>``
directory.

The ``<course-name>`` directory must match the value of the ``url_name``
attribute in the ``course.xml`` file.

************************************
Course Policy JSON Objects
************************************

  .. list-table::
     :widths: 10 80
     :header-rows: 0

     * - ``GRADE_CUTOFFS``
       - The minimal grade for passing the course, and receiving a certificate
         if offered.
     * - ``GRADER``
       - For each assignment type:

         * ``drop_count``: The number of assignments of this type that can be
           dropped when calculating the final grade.
         * ``min_count``: TBD
         * ``short_label``: The label for the assignment type shown on the
           student's Progress page.
         * ``type``: The name of the assignment type.
         * ``weight``: The percentage of the total grade determined by
            assignments of this type (for example, ``0.5`` for 50%).
            The total value for all assignment types must equal 1.0.


*******************************
Example Grading Policy File
*******************************

.. code-block:: json

  {
      "GRADER": [
          {
              "drop_count": 2,
              "min_count": 1,
              "short_label": "HW",
              "type": "Homework",
              "weight": 0.3
          },
          {
              "drop_count": 0,
              "min_count": 1,
              "short_label": "Midterm",
              "type": "Midterm Exam",
              "weight": 0.3
          },
          {
              "drop_count": 0,
              "min_count": 1,
              "short_label": "Final",
              "type": "Final Exam",
              "weight": 0.4
          }
      ],
      "GRADE_CUTOFFS": {
          "Pass": 0.41
      }
  }


.. seealso::

  :ref:`About Graded Subsections` (concept)

  :ref:`What is Open Learning XML?` (concept)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
