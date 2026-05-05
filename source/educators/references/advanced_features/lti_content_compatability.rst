.. _Content Compatibility for LTI:

Content Compatibility for LTI
##############################

.. tags:: educator, reference

Not all Open edX content types and features work well when delivered via LTI to an external
LMS. The following table summarizes compatibility.

.. list-table::
   :widths: 45 45
   :header-rows: 1

   * - Course Content or Feature
     - Works Well with LTI?
   * - Problem Components
     - Yes (in new window, not in iframe)
   * - Text Components
     - Yes
   * - Video Components
     - Yes
   * - Annotation Problem Components
     - No
   * - Cohorts
     - No
   * - Content Experiment Components
     - No
   * - Course-wide Discussions
     - No
   * - Discussion Components
     - No
   * - Internal Links
     - No
   * - Randomized Content Block Problem Components
     - No

Considerations
**************

When selecting content to deliver via LTI, keep the following in mind:

* Discussion components can be confusing for learners in an LTI context because learners may be
  identified by internally assigned IDs rather than their usernames. Consider using the discussion
  features in your external LMS instead.

* Features that create groups of learners based on their IDs, such as content experiments and
  cohorts, are not designed for external use. Set up these features in your external LMS if you
  need them.

* Course content appears in the external LMS regardless of the start, end, or enrollment dates
  defined in the Open edX course. This ensures uninterrupted availability.

* Only published content appears in an external LMS. The "Hide from students" visibility setting
  for sections, subsections, and units does not affect LTI visibility.

.. seealso::

 :ref:`Using Open edX as an LTI Tool Provider` (concept)

 :ref:`Determine Content Addresses` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-05   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+