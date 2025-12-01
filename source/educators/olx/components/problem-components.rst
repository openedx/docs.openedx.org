.. _Problem Components:

#################################
Problem Components in OLX
#################################

.. tags:: educator, reference

The problem component allows authors to add interactive exercises to the units
in a course. Many different types of exercises and problems can be added.
This section covers the basics of problem components: what they look like to
authors and learners, and the options that every problem component has.

.. contents::
   :local:
   :depth: 1

*********************************************
Problem Component Overview
*********************************************

The format for Open edX problems is based on the `LON-CAPA XML format`_, although
the two are not quite compatible. In the Open edX variant, problems are composed of
various *input types*, such as ``numericalresponse`` or ``stringresponse``.

Standard HTML tags are used for formatting.

OLX is designed to allow mixing and matching of input types and response types.
For example, a numerical grader could match 7+-0.1%. Ideally, this grader could
be used with any input type that returns numbers as its output, including a text
box, equation input, slider, or multiple choice question. In practice, this does
not always work. For example, a multiple choice question would not give an
output in a format a numerical grader could handle.

In addition, in many cases, there is a 1:1 mapping between graders and inputs.
For some types of inputs (especially discipline-specific specialized ones),
only one grader is needed.

The most general grader is ``customresponse``. This grader uses Python code to
evaluate the input. By design, this ought to work with any input type, although
this is not guaranteed to render or work properly in the Open edX Studio or LMS
environments.

Like LON-CAPA, OLX allows embedding of code to generate parameterized problems.
Unlike LON-CAPA, Open edX supports Python (and not Perl). Otherwise, the syntax for
parameterizing problems is approximately identical.

=====================================
Creating Graded or Ungraded Problems
=====================================

All problems receive a point score. However, when a grading policy is
established for a course, the assignment types that will count toward learners'
grades are defined; for example, homework, lab, midterm, and final.

As a course is developed, problem components can be added to the units in any
subsection. The problem components that are added automatically inherit the
assignment type that is defined at the subsection level. Assignment types can
only be set at the subsection level, not at the unit or individual component
level.

For more information, see :ref:`Grading Policy`.

.. _Problem Student View:

.. include:: /educators/references/course_development/learner_problem_view.rst
  :start-after: .. START LEARNER VIEW OF PROBLEM
  :end-before: .. END LEARNER VIEW OF PROBLEM

=====================================
Example OLX - Single Select Problem
=====================================

See the `single select problem <https://github.com/openedx/training-courses/blob/main/olx_example_course/course/problem/single_select.xml>`_
in the ``olx_example_course``; it is replicated here:

.. code-block:: xml

  <problem display_name="Single select" show_reset_button="false" showanswer="finished" weight="2.0">
    <multiplechoiceresponse>
      <div>What is the correct answer?</div>
      <choicegroup>
        <choice correct="false">
          <div>Incorrect</div>
        </choice>
        <choice correct="false">
          <div>Incorrect</div>
        </choice>
        <choice correct="true">
          <div>Correct</div>
        </choice>
      </choicegroup>
      <solution>
        <div class="detailed-solution">
          <p>Explanation</p>
          <p>The correct answer is called "Correct"</p>
        </div>
      </solution>
    </multiplechoiceresponse>
  </problem>  

******************
Problem Settings
******************

In addition to the text of the problem, problems have the following settings.

.. contents::
  :local:
  :depth: 1

This section describes the OLX elements and attributes that can be defined for the
problem settings. For a detailed description of each setting, see
:ref:`Guide to Problem Settings`.

===============
Display Name
===============

Using OLX, set the display name as an attribute of the ``<problem>``
element.

.. code-block:: xml

  <problem display_name="Geography Homework"></problem>

==============================
Maximum Attempts
==============================

Using OLX, set the maximum attempts as an attribute of the ``<problem>``
element.

.. code-block:: xml

  <problem max_attempts="3"></problem>


.. _Problem Weight:

==============================
Problem Weight
==============================

Using OLX, set the score of the component as an attribute of the ``<problem>``
element.

.. code-block:: xml

  <problem weight="2.0"></problem>

.. _Randomization OLX:

===============
Randomization
===============

Using OLX, set value randomization as an attribute of the ``<problem>``
element.

.. code-block:: xml

  <problem rerandomize="always"></problem>

The following values can be set for this attribute:

* always
* on_reset
* never
* per_student

.. _Show Answer OLX:

===============
Show Answer
===============

Using OLX, set set the show answer preference as an attribute of the
``<problem>`` element.

.. code-block:: xml

  <problem showanswer="correct_or_past_due"></problem>

The following values can be set for this attribute:

* "always"
* "answered"
* "attempted"
* "closed"
* "finished"
* "past_due"
* "correct_or_past_due"
* "after_all_attempts"
* "after_all_attempts_or_correct"
* "attempted_no_past_due"
* "never"

.. _Show Reset Button OLX:

=================
Show Reset Button
=================

Using OLX, set the show reset button preference as an attribute of the
``<problem>`` element.

.. code-block:: xml

  <problem show_reset_button="true"></problem>

.. _Modifying a Released Problem OLX:

*********************************
Modifying a Released Problem
*********************************

.. warning:: Be careful when modifying problems after they have been
 released! Changes that are made to published problems can affect the learner
 experience in the course and analysis of course data.

After a learner submits a response to a problem, the LMS stores the learner's
response, the score that the learner received, and the maximum score for the
problem. For problems with a **Maximum Attempts** setting greater than 1, the
LMS updates these values each time the learner submits a new response to a
problem. However, if a problem or its attributes are changed, existing learner
information for that problem is not automatically updated.

For example, a problem might be released with the answer specified as "3". After
some learners have submitted responses, the course team notices that the answer
should be 2 instead of 3. When the problem is updated with the correct answer,
the LMS does not update scores for learners who answered 2 for the original
problem and thus received the wrong score.

For another example, the number of response fields is changed fom two to three.
Learners who submitted answers before the change have a score of 0, 1, or 2 out
of 2.0 for that problem. Learners who submitted answers after the change have
scores of 0, 1, 2, or 3 out of 3.0 for the same problem.

If the weight setting for the problem in Studio is changed, however, existing
learner scores update when the learner's **Progress** page is refreshed. In a
live section, learners will see the effect of these changes.

===============
Workarounds
===============

The Instructor Dashboard allows rescoring existing submissions for either a
specific learner, or all learners in the course. However, this may not be ideal
in the situation that the problem itself has changed.

If a released problem has to be modifyed in a way that affects grading, there are
two options within Studio to assure that every learner has the opportunity to
submit a new response and be regraded. Note that both options require the course
team to ask their learners to go back and resubmit answers to a problem.

*  In the problem component that was changed, increase the number of attempts
   for the problem. Then ask all learners to redo the problem.

*  Delete the entire Problem component in Studio and create a new Problem
   component with the correct content and settings. (If the revisions needed are
   minor, duplicate the problem component before it is deleted and revise the
   copy.) Then ask all learners to complete the new problem.

****************************************************
Adding Feedback and Hints to a Problem
****************************************************

.. include:: /educators/references/course_development/exercise_tools/adding_hints.rst
  :start-after: .. START ADDING FEEDBACK AND HINTS
  :end-before: .. END ADDING FEEDBACK AND HINTS

**************************
Awarding Partial Credit
**************************

.. include:: /educators/references/course_development/awarding_partial_credit.rst
  :start-after: .. START PARTIAL CREDIT
  :end-before: .. END PARTIAL CREDIT

.. _Problem Randomization OLX:

***********************************
Problem Randomization
***********************************

Presenting different learners with different problems or with different
versions of the same problem is referred to as "problem randomization".

ifferent learners can be provided with with different problems by using
randomized content blocks, which randomly draw problems from pools of problems
stored in content libraries. For more information, see :ref:`Randomized Content
Blocks`.

.. note:: Problem randomization is different from the **Randomization** setting
   in Studio. Problem randomization offers different problems or problem
   versions to different learners, whereas the **Randomization** setting
   controls when a Python script randomizes the variables within a single
   problem. For more information about the **Randomization** setting, see
   :ref:`Randomization`.


.. _Create Randomized Problems OLX:

====================================
Create Randomized Problems
====================================

.. note:: Creating randomized problems by exporting a course and editing
   some of the course's XML files is no longer supported.

Different learners can be provided with with different problems by using
randomized content blocks, which randomly draw problems from pools of problems
stored in content libraries. For more information, see :ref:`Randomized Content
Blocks`.

**************************
Tooltips
**************************

.. include:: /educators/references/course_development/adding_tooltips.rst
  :start-after: .. START ADDING TOOLTIPS
  :end-before: .. END ADDING TOOLTIPS

.. seealso::

  :ref:`What is Open Learning XML?` (concept)

  :ref:`Multipart Components OLX` (reference)

  :ref:`Components and Activities TOC` (reference)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
