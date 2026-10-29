.. _about-competency-taxonomies:

About Competency Taxonomies
###########################

.. tags:: educator, concept

Every taxonomy in Studio has a type: **Tags** or **Competency**. The type is
chosen during the import of a new taxonomy. The type controls what can be done
with the taxonomy after it is imported.

Taxonomy Types
**************

The following table describes the two taxonomy types.

.. list-table::
   :header-rows: 1
   :widths: 15 40 45

   * - Type
     - What the taxonomy contains
     - What it is used for
   * - Tags
     - Labels that describe content, such as subject, difficulty, or format.
     - Tagging courses, course content, and library content to have the ability to
       organize, filter, and search for that content. Tags is the default type.
   * - Competency
     - Competencies, which are the skills or knowledge that a learner is
       expected to demonstrate. The competencies often come from an existing
       competency framework.
     - Defining competency criteria. A competency criterion connects a
       competency to graded course content, and sets what a learner must
       achieve on that content to demonstrate mastery of the competency.

A Competency taxonomy is built and edited the same way a Tags taxonomy is built and edited. The tags in a Competency taxonomy are its competencies. The
difference between the two types is that only the competencies in a Competency
taxonomy can be connected to graded course content through competency criteria,
and used to track what a learner has mastered.

When to Use a Competency Taxonomy
*********************************

Import a taxonomy as a Competency taxonomy when both of the following are true.

* Each entry in the taxonomy is a competency that learners must demonstrate.
* Learner mastery of those competencies is tracked against graded work
  in courses.

Import a taxonomy as a Tags taxonomy when its entries only describe or
categorize content.

The Taxonomy Type Is Permanent
******************************

A taxonomy's type is chosen only when it is imported as a new taxonomy.
Re-importing a taxonomy replaces its tags but keeps its type, and Studio does
not currently provide a way to change the type later. To use the same entries
as a different type, import the file again as a new taxonomy and choose the
other type.

How a Competency Taxonomy Appears in Studio
*******************************************

A Competency taxonomy differs from a Tags taxonomy on the **Taxonomies** page
in the following ways.

* **Type icon.** Each taxonomy card shows one icon to the left of the taxonomy
  name. A target icon marks a Competency taxonomy, and a tag icon marks a Tags
  taxonomy. Screen readers announce the icons as "Competency taxonomy" and
  "Tags taxonomy".
* **Apply Competencies.** A Competency taxonomy card has an
  :guilabel:`Apply Competencies` button at the bottom of the card, and an
  :guilabel:`Apply Competencies` item in the card's three-dot menu. Both open
  the Competency Management page for that taxonomy. Tags taxonomy cards have
  neither of these.

.. image:: /_images/educator_concepts/taxonomies_type_icons.png
   :alt: A screenshot of the Taxonomies page showing a Competency taxonomy
         card with a target icon and an Apply Competencies button, next to a
         Tags taxonomy card with a tag icon.

Editing a Competency taxonomy and applying its competencies are separate
workflows on separate pages. For how to open each page, see
:ref:`open-competency-management-taxonomy-editing`.

Each competency in a Competency taxonomy has a Competency ID, which comes from
the imported file or is generated from the competency's name. For more
information, see :ref:`about-competency-ids`.

.. seealso::

   :ref:`import-competency-taxonomy` (how-to)

   :ref:`open-competency-management-taxonomy-editing` (how-to)

   :ref:`about-competency-ids` (concept)

   :ref:`import-export-taxonomy` (how-to)

   :ref:`manage-taxonomy-tags` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
