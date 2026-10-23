.. _import-competency-taxonomy:

Import a Competency Taxonomy
############################

.. tags:: educator, how-to

This guide describes how to import a new taxonomy as a Competency taxonomy. For
an explanation of taxonomy types and when to use a Competency taxonomy, see
:ref:`about-competency-taxonomies`.

Before You Begin
****************

* You must be an organization-level or instance-level administrator to import
  a taxonomy.
* Prepare your taxonomy as a CSV or JSON file of up to 100 MB. Every row in the
  file needs an ``id`` and a ``value``, and a file with a row that lacks either
  is rejected. The ``value`` is the competency's name, and the ``id`` becomes the
  competency's Competency ID. For more information, see
  :ref:`about-competency-ids`. For how to build the file from a template,
  see :ref:`build-taxonomy-using-template`.
* Decide on the taxonomy type before you start. You can choose the type only
  during this import, and you cannot change it afterward.

Import the Taxonomy
*******************

#. From Studio Home, select the **Taxonomies** tab.

#. Select :guilabel:`Import`.

#. Drag your taxonomy file into the upload box, or click the box to choose the
   file from your computer. Then select :guilabel:`Continue`.

#. On the **Populate** step, enter a **Taxonomy Name** and a **Taxonomy
   Description**.

#. In the **Taxonomy Type** list, select **Competency**. The list is set to
   **Tags** by default, so if you leave it unchanged, the taxonomy is imported
   as a Tags taxonomy.

   .. Screenshot needed: taxonomies_import_taxonomy_type.png
      Alt text: A screenshot of the Populate step of the import wizard, with
      the Taxonomy Type list open and showing the Tags and Competency options.

#. Select :guilabel:`Import`.

When the import finishes, Studio shows a notification that the taxonomy was
imported, and the new taxonomy appears on the **Taxonomies** page. Its card
shows the Competency icon and an :guilabel:`Apply Competencies` button.

.. Screenshot needed: taxonomies_competency_card.png
   Alt text: A screenshot of a Competency taxonomy card on the Taxonomies page,
   showing the target icon next to the taxonomy name and the Apply Competencies
   button at the bottom of the card.

If the import fails, Studio shows an **Import error** message, and no taxonomy
is created. Fix the problem in your file and import it again.

.. note::

   You can also start this import from the Competency Management page of an
   existing Competency taxonomy by selecting
   :guilabel:`Import Competency Framework`. The wizard then has **Competency**
   selected as the taxonomy type.

.. seealso::

   :ref:`about-competency-taxonomies` (concept)

   :ref:`about-competency-ids` (concept)

   :ref:`open-competency-management-taxonomy-editing` (how-to)

   :ref:`build-taxonomy-using-template` (how-to)

   :ref:`import-export-taxonomy` (how-to)

   :ref:`Update/Re-import a taxonomy` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
