.. _competency-ids-rest-api:

Competency IDs in the REST API
##############################

.. tags:: developer, reference

A Competency ID is the identifier of a competency in a Competency taxonomy,
usually the code that the competency has assigned in its source framework, such as
``HS.N-RN.A.1``. For what a Competency ID is and how course teams use it, see
:ref:`about-competency-ids`.

This page describes how Competency IDs are exposed through the Studio REST API.
The endpoints below are relative to ``/api/content_tagging/v1/``.

In the API, a Competency ID is the tag's ``external_id`` field, and the taxonomy
type is the taxonomy's ``taxonomy_type`` field.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Endpoint
     - Competency and Competency ID fields
   * - ``POST taxonomies/import/``
     - Creates a taxonomy from an uploaded file. Send ``taxonomy_type`` as
       ``competency`` or ``tags`` in the form data. The default is ``tags``.
       The ``id`` of each row in the file is stored as that tag's
       ``external_id``.
   * - ``GET taxonomies/`` and ``GET taxonomies/{id}/``
     - Each taxonomy includes ``taxonomy_type``, with the value ``competency``
       or ``tags``.
   * - ``GET taxonomies/{id}/tags/``
     - Each tag includes ``external_id``. The value is always present; a tag
       created without one has an ``external_id`` generated from its name.
   * - ``POST taxonomies/{id}/tags/``
     - Creates a tag. The optional ``external_id`` field sets its Competency ID.
       When it is omitted, the ID is generated from the tag's ``value``.
   * - ``PUT taxonomies/{id}/tags/import/``
     - Re-imports a taxonomy from a file. Tags are matched to existing tags by
       ``external_id``. A row with a ``previous_id`` column renames the matched
       tag's ``external_id`` to the row's ``id``. The taxonomy type is not
       changed.

A re-import with ``previous_id`` is the way to change a tag's ``external_id``
after the tag is created.

.. seealso::

   :ref:`about-competency-ids` (concept)

   :ref:`about-competency-taxonomies` (concept)

   :ref:`tag-ids-for-taxonomy-import` (concept)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
