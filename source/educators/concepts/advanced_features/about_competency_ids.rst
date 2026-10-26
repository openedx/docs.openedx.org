.. _about-competency-ids:

About Competency IDs
####################

.. tags:: educator, concept

A Competency ID is the identifier of a competency in a Competency taxonomy.
Every competency has one. It is usually the code that the competency is assigned in
its source framework, such as ``HS.N-RN.A.1``, which is set in the file that
is imported. Studio shows the Competency ID next
to the competency's name to identify which framework entry a
competency matches, even when two competencies have similar names.

Where a Competency ID Comes From
********************************

A Competency IDs is assigned in the file that is imported to create or update a
Competency taxonomy. The ``id`` column of a CSV file, or the ``id`` field of
each tag in a JSON file, holds the Competency ID. The ``value`` column or field
holds the competency's name.

The following example shows a CSV file with two competencies. The second
competency is nested under the first one.

.. code-block:: text

   id,value,parent_id
   HS.N-RN.A,Extend the properties of exponents to rational exponents,
   HS.N-RN.A.1,Explain how the definition of rational exponents follows from integer exponents,HS.N-RN.A

A Competency ID must follow these rules.

* Every row in the import file requires a Competency ID.
* Each Competency ID must be unique within a taxonomy. Studio does not
  distinguish uppercase from lowercase letters when it compares IDs, so
  ``ABC-1`` and ``abc-1`` are viewed as the same ID.
* A Competency ID can be up to 255 characters long and cannot contain a TAB
  character. Spaces at the start or end of the ID are removed during import.

Who Uses a Competency ID
************************

* **Administrators** assign Competency IDs in the file used for
  importing a Competency taxonomy.
* **Course authors** see Competency IDs on the Competency Management page,
  where the IDs help in the selection of the correct competency.

Where a Competency ID Appears
*****************************

Competency IDs appear only on the Competency Management page. Each one is shown
as a blue badge in the following places:

* In the competency tree, at the right end of each competency's row.
* Next to the **Demonstrate Mastery For** line, after selecting a competency.

Screen readers announce each badge as "Competency ID:" followed by the ID.

..  image:: /_images/educator_concepts/taxonomies_competency_id_badges.png
  :alt: A screenshot of the Competency Management page with a competency
   selected, showing Competency ID badges in the competency tree and next to
   the Demonstrate Mastery For line.

The taxonomy editing page does not show Competency IDs.

Changing a Competency ID
************************

The Competency ID is not viewable or editable on the taxonomy editing page. The Competency IDs is set
and changed by importing a CSV or JSON file.

When re-importing a taxonomy, Studio uses the Competency ID to match each row
in the new file to an existing competency. If a row's Competency ID matches an
existing competency, Studio updates that competency, for example by renaming
it. For more information about how IDs work during import, see
:ref:`tag-ids-for-taxonomy-import`.

To change a competency's Competency ID, add a ``previous_id`` column to the
import file. Put the current ID in ``previous_id`` and the new ID in ``id``.
Studio renames the ID in place, and the competency keeps its competency
criteria. The ``previous_id`` column is used only during import, exported files
do not include it.

A competency added on the taxonomy editing page, or that an import file
lists without an ``id``, gets a Competency ID generated from its name. If that
ID is already taken in the taxonomy, Studio adds a suffix such as ``-2`` to it. When 
the taxonomy is exported, the ``id`` column holds that generated ID. To replace it with the
competency's real code, re-import the file with the generated ID in
``previous_id`` and the real code in ``id``.

Competency IDs in the REST API
******************************

Developers who work with taxonomies through the Studio REST API read and set
Competency IDs through the ``external_id`` field of a tag. For the endpoints
involved and how each one handles Competency IDs, see
:ref:`competency-ids-rest-api`.

.. seealso::

   :ref:`about-competency-taxonomies` (concept)

   :ref:`import-competency-taxonomy` (how-to)

   :ref:`open-competency-management-taxonomy-editing` (how-to)

   :ref:`tag-ids-for-taxonomy-import` (concept)

   :ref:`Update/Re-import a taxonomy` (how-to)

   :ref:`competency-ids-rest-api` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
