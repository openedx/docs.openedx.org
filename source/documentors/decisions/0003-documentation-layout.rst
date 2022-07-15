Documentation Layout
####################

Status
******

**Accepted**

Context
*******

As multiple people were working with writing documentation for different
`personas`_, the directory structure underneath each persona started diverging.
This made it harder for someone to easily jump between work on different
`personas`_ and easily locate documents and orient themselves.

.. _personas: https://en.wikipedia.org/wiki/Persona_(user_experience)

Decision
********

* The ``source`` folder MUST be the root for all docs.

* For each top-level persona that we have, there MUST be a separate folder whose
  name closely matches the name of the persona (no caps, underscores instead of
  spaces).

  * Examples

    * Course Operators -> course_ops

    * Software Developers -> developers

* Each persona folder MUST contain a folder for each :doc:`documentation
  type<../concepts/content_types>` (``concepts``, ``how-tos``, ``quickstarts``
  and ``references``).

* Each folder MUST have an ``index.rst`` file that is the root document for that
  folder.

  * The index.rst file MUST contain a ``toc_tree`` that connects all content
    in that folder and sub-folders.

Visually this would look something like:

.. code-block:: bash

   persona
   ├── concepts
   │   ├── index.rst
   │   └── some-concept.rst
   ├── how-tos
   │   ├── index.rst
   │   └── how-to-something.rst
   ├── quickstarts
   │   └── index.rst
   ├── references
   │   └── index.rst
   └── index.rst

Consequences
************

Having a consistent layout should make it easier for documentors to be able to
navigate the repository and quickly switch between `personas`_ and know where to
put new documentation and where to find the roots for each sub-area of a persona.
