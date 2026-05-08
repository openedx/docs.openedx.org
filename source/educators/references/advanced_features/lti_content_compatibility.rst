.. _Content Compatibility for LTI:

Content Compatibility for LTI
##############################

.. tags:: educator, reference

Not all Open edX content types and features work well when delivered via Learning Tools Interoperability (LTI) to an external
LMS. This table summarizes compatibility.

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

When selecting content to deliver via LTI, keep these points in mind:

* Only published content appears in an external LMS.

* Content appears in the external LMS regardless of the start, end, or enrollment dates
  defined in the Open edX course. This ensures uninterrupted availability.

* The external LMS does not respect the "Hide from students" visibility setting. If it is selected,
  the content will not appear in the learner view of your Open edX instance. However, it will be
  visible to learners accessing the content via the external LMS.

* Problem components work only when opened in a new window, not in an iframe. If your external LMS
  embeds LTI content in an iframe by default, learners will not be able to interact with problem
  components. Check your external LMS settings for an option to open LTI content in a new window.

* Discussion components can be confusing for learners in an LTI context because learners may be
  identified by internally assigned IDs rather than their usernames. Consider using the discussion
  features in your external LMS instead.

* Features that create groups of learners based on their IDs, such as content experiments and
  cohorts, are not designed for external use. Set up these features in your external LMS if you
  need them.



.. seealso::

   :ref:`Using Open edX as an LTI Tool Provider` (concept)

   :ref:`Determine Content Addresses` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-06   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-06-04   | MITx                          | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+