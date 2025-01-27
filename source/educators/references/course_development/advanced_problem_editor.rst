.. _Advanced Editor:


The Advanced Editor
####################

.. tags:: educator, reference

If the simple editor cannot fulfill your needs, you might turn your attention
to the Advanced Editor. This editor will allow you to directly edit the open
learning XML (OLX) of your problem. The Advanced Editor can be accessed in one of
two ways.

If you are creating a new problem, on the **Select problem type** screen,
select the **Advanced problem types**. This will bring you to a list of advanced
problems with varying levels of support. To create an advanced problem from
scratch, select **Blank advanced problem**.

If you are looking to turn your simple problem into an advanced problem, click
the **Switch to advanced editor** button, which can be found on the collapsible
settings to the right of the problem editor after clicking
**Show advanced settings**.

The Advanced Editor retains several settings from the simple editor such as
**Scoring**, **Show answer**, **Show reset option**, **Time between attempts**
and **MATLAB API Key** as well as introduces the **Randomization** setting.
While the other settings are not shown on the collapsible panes to the right of
the problem editor, they can be added via editing the OLX.

OLX specifications can be found under each problem type in
:ref:`Components and Activities TOC`.

.. note::
   If you have turned your problem into an advanced problem, it is possible to
   turn it back into a simple problem. When you edit a problem, as long as the
   problem editor can fully parse the OLX, the editor will open as the Simple
   Editor instead of the Advanced Editor.

.. _Advanced Editor Features:

***************************************************
Advanced Editor Features
***************************************************

Since the Advanced Editor allows you to edit the problem directly using the OLX,
there are many more ways to write a problem. Below are several features that the Advanced Editor is capable of:

.. contents::
 :local:
 :depth: 1

.. _Randomization:

===============
Randomization
===============

.. note::
   This Randomization setting serves a different purpose from “problem
   randomization”. This Randomization setting affects how numeric values are
   randomized within a single problem and requires the inclusion of a Python
   script. Problem randomization presents different problems or problem
   versions to different learners. For more information, see
   :ref:`Problem Randomization`.

This setting can be found in the collapsible settings to the right of the
problem editor. For problems that include a Python script to generate numbers
randomly, this setting specifies how frequently the values in the problem
change: each time a different learner accesses the problem, each time a single
learner tries to answer the problem, both, or never.

.. note::
   This setting should only be set to an option other than **Never** for
   problems that are configured to do random number generation.

For example, in this problem, the highlighted values change each time a
learner submits an answer to the problem.

.. image:: /_images/educator_references/Rerandomize.png
 :alt: An image of the same problem shown twice, with color highlighting on
   values that change.
 :width: 800

If you want to randomize numeric values in a problem, you must complete both of
these steps.

* Make sure that you edit your problem to include a Python script that randomly
  generates numbers.

* Select an option other than **Never** for the **Randomization** setting.

The Open edX Platform has a 20-seed maximum for randomization. This means that
learners see up to 20 different problem variants for every problem that has
**Randomization** set to an option other than **Never**. It also means that
every answer for the 20 different variants is reported by the Answer
Distribution report. Limiting the number of variants to a maximum of 20 allows
for better analysis of learner submissions by allowing you to detect common
incorrect answers and usage patterns for such answers.

.. important::
 Whenever you choose an option other than **Never** for a
 problem, the computations for the Answer Distribution report include up to 20
 variants for the problem, **even if the problem was not actually configured to
 include randomly generated values**. This can make data collected for problems
 that cannot include randomly generated values, (including, but not limited to,
 all single select, multi-select, dropdown, and text input problems), extremely
 difficult to interpret.

You can choose the following options for the **Randomization** setting.

.. list-table::
   :widths: 15 70
   :header-rows: 1

   * - Option
     - Description
   * - **Always**
     - Learners see a different version of the problem each time they select
       **Submit**.
   * - **On Reset**
     - Learners see a different version of the problem each time they select
       **Reset**.
   * - **Never**
     - All learners see the same version of the problem. For most courses, this
       option is supplied by default. Select this option for every problem in
       your course that does not include a Python script to generate random
       numbers.
   * - **Per Student**
     - Individual learners see the same version of the problem each time they
       look at it, but that version is different from the version that other
       learners see.

.. _Multiple Problems in One Component:

============================================================
Including Multiple Questions in One Component
============================================================

In some cases, you might want to design an assessment that combines multiple
questions in a single problem component. For example, you might want learners
to demonstrate mastery of a concept by providing the correct responses to
several questions, and only giving them credit for a problem if all of the
answers are correct.

Another example involves learners who have slow or intermittent internet
connections. When every problem appears on a separately loaded web page, these
learners can find the amount of time it takes to complete an assignment or exam
discouraging. For these learners, grouping several questions together can
promote increased engagement with course assignments.

When you add multiple questions to a single problem component, the settings
that you define, including the display name and whether to show the **Reset**
button, apply to all of the questions in that component. The answers to all of
the questions are submitted when learners select **Submit**, and the correct
answers for all of the questions appear when learners select **Show Answer**.
By default, learners receive one point for each question they answer correctly.
For more information about changing the default problem points and other
settings, see :ref:`Problem Settings`.

.. important::
  To assure that the data collected for learner interactions with
  your problem components is complete and accurate, include a maximum of 10
  questions in a single problem component.

-------------------------------------------------
Adding Multiple Questions to a Problem Component
-------------------------------------------------

To design an assignment that includes several questions, you add one problem
component and then edit it to add every question and its answer options, one
after the other, in that component. Be sure to identify the text of every
question or prompt with the appropriate OLX ``<label>`` element, and include
all of the other required elements for each question.

* Each question and its answer options are enclosed by the element that
  identifies the type of problem, such as
  ``<multiplechoiceresponse>`` for a single select question or
  ``<formularesponse>`` for a math expression input question.

* You can provide a different explanation for each question with the
  OLX ``<solution>`` element.

As a best practice, avoid including unformatted
paragraph text between the questions. Screen readers can skip over text that is
inserted among multiple questions.

The questions that you include can all be of the same problem type, such as a
series of text input questions, or you can include questions that use different
problem types, such as both numerical input and math expression input.

.. note::
  You cannot use a :ref:`Custom JavaScript` in a problem component that
  contains more than one question. Each custom JavaScript problem must be in
  its own component.

An example of a problem component that includes a text input question and a
numerical input question follows.

.. code-block:: xml

  <problem>
    <stringresponse answer="Caesar Cardini" type="ci">
      <label>Who invented the Caesar salad?</label>
      <description>Be sure to check your spelling.</description>
      <textline size="20"/>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>Caesar Cardini is credited with inventing this salad and received
           a U.S. trademark for his salad dressing recipe.</p>
        </div>
      </solution>
    </stringresponse>

    <numericalresponse answer="1924">
      <label>In what year?</label>
      <formulaequationinput/>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>Cardini invented the dish at his restaurant on 4 July 1924 after
           the rush of holiday business left the kitchen with fewer supplies
           than usual.</p>
        </div>
      </solution>
    </numericalresponse>
  </problem>


.. _Problem Randomization:

***********************
Problem Randomization
***********************

Presenting different learners with different problems or with different
versions of the same problem is referred to as "problem randomization".

You can provide different learners with different problems by using randomized
content blocks, which randomly draw problems from pools of problems stored in
content libraries. For more information, see :ref:`Randomized Content Blocks`.

.. note::
   Problem randomization is different from the **Randomization** setting
   that you define in Studio. Problem randomization presents different problems
   or problem versions to different learners, while the **Randomization**
   setting controls when a Python script randomizes the variables within a
   single problem. For more information about the **Randomization** setting,
   see :ref:`Randomization`.

.. _Create Randomized Problems:

Creating randomized problems by exporting your course and editing some of your
course's XML files is no longer supported.

.. seealso::
 

 :ref:`Working with Problem Components` (reference)

 :ref:`Modifying a Released Problem` (reference)

 :ref:`Problem Settings` (reference)

 :ref:`Feedback Best Practices` (concept)

 :ref:`Learner View of Problems` (reference)

 :ref:`Partial Credit` (reference)

 :ref:`Adding Tooltips` (reference)



**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
