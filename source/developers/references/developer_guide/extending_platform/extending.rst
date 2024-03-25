
.. _Options for Extending the Open edX Platform:

###########################################
Options for Extending the Open edX Platform
###########################################

There are several options for extending the Open edX Platform to provide useful
and innovative educational content in your courses.

This section of the developers' documentation lists and explains the different
ways to extend the platform, starting with the following table.

.. |br| raw:: html

  <br />

.. list-table::
   :widths: 10 10 10 10 10 10
   :header-rows: 1

   * -
     - Custom |br|
       JavaScript |br|
       Applications
     - LTI
     - External |br|
       Graders
     - XBlocks
     - Platform |br|
       Customization
   * - Development Cost
     - Low
     - Low
     - Medium
     - Medium
     - High
   * - Language
     - JavaScript
     - Any
     - Any
     - Python
     - Python
   * - Development Environment Needed
     - No
     - No
     - Yes
     - Yes
     - Yes
   * - Self-hosting Needed
     - No
     - Yes, if building a new LTI unit. Many LTI tools are hosted elsewhere.
     - Yes
     - No
     - No
   * - Requires Sysadmin Installation on Your Open edX Instance
     - No
     - No
     - Yes
     - Yes
     - Yes
   * - Clean UI Integration
     - Yes
     - No (see :doc:`openedx-building-and-running-a-course:exercises_tools/lti_component`)
     - Yes
     - Yes
     - Yes
   * - Mobile enabled
     - Possibly
     - Possibly
     - Yes
     - Yes
     - Yes
   * - Server Side Grading
     - Possibly (See :doc:`openedx-building-and-running-a-course:exercises_tools/custom_javascript`)
     - Yes
     - Yes
     - Yes
     - Yes
   * - Usage Data
     - No (See :doc:`openedx-building-and-running-a-course:exercises_tools/custom_javascript`)
     - No
     - Limited
     - Yes
     - Yes
   * - Provision in Studio
     - No
     - No
     - No
     - Yes
     - No
   * - Learner Data Privacy Loss?
     - No
     - Possibly (Depends on LTI tool used)
     - Possibly (Depends on external grader implementation)
     - No
     - No
