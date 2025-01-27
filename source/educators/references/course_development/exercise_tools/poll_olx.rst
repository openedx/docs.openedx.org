.. _Poll Tool for OLX:

Poll Tool for OLX
##################

.. tags:: educator, reference

You can run polls in your course so that your students can share opinions on
different questions.

.. image:: /_images/educator_references/PollExample.png

.. note:: Creating a poll requires you to export your course, edit some of
 your course's XML files in a text editor, and then re-import your course. We
 recommend that you create a backup copy of your course before you create the
 poll. We also recommend that you only edit the files that will contain polls
 in the text editor if you are very familiar with editing XML.

**************
Terminology
**************

Sections, subsections, units, and components have different names in the
**Course Outline** view and in the list of files that you see after you
export your course and open the .xml files for editing. The following table
lists the names of these elements in the **Course Outline** view and in a list
of files.

.. list-table::
   :widths: 15 15
   :header-rows: 0

   * - Course Outline View
     - File List
   * - Section
     - Chapter
   * - Subsection
     - Sequential
   * - Unit
     - Vertical
   * - Component
     - Discussion, HTML, problem, or video

For example, when you want to find a specific section in your course, you
look in the **Chapter** folder when you open the list of files that your course
contains. To find a unit, you look in the **Vertical** folder.

*********************
Format description
*********************

The main tag of poll module input is:

.. code-block:: xml

    <poll_question> ... </poll_question>

``poll_question`` can include any number of the following tags:
any xml and ``answer`` tag. All inner xml, except for ``answer`` tags, we call "question".

==================
poll_question tag
==================

Xmodule for creating poll functionality - voting system. The following
attributes can be specified for this tag::

    name - Name of xmodule.
    [display_name| AUTOGENERATE] - Display name of xmodule. When this attribute is not defined - display name autogenerate with some hash.
    [reset | False] - Can reset/revote many time (value = True/False)

============
answer tag
============

Define one of the possible answer for poll module. The following attributes can
be specified for this tag::

    id - unique identifier (using to identify the different answers)

Inner text - Display text for answer choice.

***********
Example
***********

==================
Example of poll
==================

.. code-block:: xml

    <poll_question name="second_question" display_name="Second question">
        <h3>Age</h3>
        <p>How old are you?</p>
        <answer id="less18">&lt; 18</answer>
        <answer id="10_25">from 10 to 25</answer>
        <answer id="more25">&gt; 25</answer>
    </poll_question>

================================================
Example of poll with unable reset functionality
================================================

.. code-block:: xml

    <poll_question name="first_question_with_reset" display_name="First question with reset"
        reset="True">
        <h3>Your gender</h3>
        <p>You are man or woman?</p>
        <answer id="man">Man</answer>
        <answer id="woman">Woman</answer>
    </poll_question>

.. seealso::
 :class: dropdown
 
 :ref:`Create a Poll` (how to)
 
 :ref:`Poll Tool` (reference)

 :ref:`Add Poll` (how to)

 :ref:`Enable Poll in OLX` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
