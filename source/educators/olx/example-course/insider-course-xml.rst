.. _The olx-example course.xml File:

###################################
The olx-example ``course.xml`` File
###################################

.. tags:: educator, reference

The `olx-example`_ course is a sample course that was originally developed for edX.org.

The courseware for `olx-example`_ is defined in the `course.xml`_ file and
follows the organization described in :ref:`The Courseware Structure`.

.. contents::
  :local:
  :depth: 1

*****************************
olx-example Course Hierarchy
*****************************

The olx-example courseware is organized into chapters, sequentials, and
verticals.

For example, the following XML defines the first chapter, sequential, and
vertical in the course.

.. code-block:: xml

  <chapter display_name="Pedagogical Foundations: Constructive Learning"
      url_name="Week_2_Technology_enabled_constructive_learning">
      <sequential format="Learning Sequence" graded="true"
          display_name="Overview (go here first)"
          url_name="Overview_go_here_first">
          <vertical display_name="Week's overview" url_name="Week_s_overview">
              <html display_name="Week overview" filename="Week_overview"
                  url_name="Week_overview"/>
	          <done display_name="Read week overview"
	              url_name="Read_week_overview" align="right"/>


The vertical ``Week's Overview`` contains an HTML component that references the
file ``Week_overview`` in the ``HTML`` directory.

Learners see this content in the Learning Management System as follows.

.. Image:: /_images/olx-example-images/Insider-first-image.png
 :alt: The HTML component as a learner sees it.


*********************************
Sequentials that Contain XBlocks
*********************************

One advantage of OLX (open learning XML) is the flexibility it allows in how
you organize your course. For example, olx-example demonstrates that you can
nest XBlocks and problems directly in a sequential, without the need for a
vertical. This streamlines the course creation process while maintaining
consistency in how students interact with courseware.

The following example XML defines a sequential that has, as children, an HTML
XBlock, a reference to a vertical that is defined in another file, and a
reference to a problem defined in another file.

.. code-block:: xml

    <sequential display_name="In-class exercise" url_name="in_class">
        <html display_name="Overview" url_name="overview">
	        <p>In the on-line portion, . . . </p>
	        <table border="0">
	            <tr>
	                <td align="right">3pm-3:10pm</td><td>Welcome!</td>
	            </tr>
	            . . .
	        </table>
        </html>
        <vertical url_name="in_class_ora"></vertical>
        <problem url_name="res_survey" filename="res_survey"
            display_name="Survey: What next?">
        </problem>
    </sequential>

The learner sees this sequential as follows.

.. Image:: /_images/olx-example-images/Insider-first-sequential.png
 :alt: The sequential as a learner sees it.

.. seealso::

  :ref:`What is Open Learning XML?` (concept)

  :ref:`OLX Components` (reference)

  :ref:`OLX Exercises, Tools, and Problem Types` (reference)
  
  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)

  :ref:`Example of OLX for a Studio Course` (reference)

  :ref:`The Courseware Structure` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
| Review Date  | Reviewer                      |   Release      |    Test situation                                                                                                  |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
| 2025-04-11   | Sarina Canelake               | Sumac          |`Fail <https://github.com/openedx/docs.openedx.org/issues/998>`_                                                    |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+

