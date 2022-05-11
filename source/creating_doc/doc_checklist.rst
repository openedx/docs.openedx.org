Documentation Checklist
=============================

This page lists items you should check when you are creating new documentation. We recommend reviewing this list before you create a pull request.

.. contents:: Contents
  :local:
  :depth: 1

Your Audience
**************

Make sure your documentation is targeted to the right audience and organized under that audience's section of the documentation. Each topic in the documentation is for one of the following audiences:

* Educators
* Course Operators
* Site Operators
* Developers

Ensure that new topics are stored in the directory for the appropriate audience, under the ``source`` directory.

For more information, see :ref:`Audiences`.

Topic Types
************

Each topic in the documentation is one of three types:

* How to

* Reference

* Concepts

Ensure that you have clearly identified the types of new topics you have created, and have stored new files in the directory for that topic type.

For more information, see :ref:`Content Types`.


New Topics in TOCs
*******************

Every new topic must be added to a table of contents. Add each new topic to the audience home page in the appropriate place.


RST Standards
*******

Ensure that the new documentation adheres to RST standards and Open edX best practices. You should use :ref:`Documentation Templates` as much as possible, and review :ref:`New Documentation Guidelines`.


Images
********

All new images should be placed in the ``source/_images`` directory and referenced in the RST file as:

.. code-block:: RST

  Line of content, followed by a line with an image.

  .. image:: /_images/image-file-name

  Or, a line of content, followed by a clickable thumbnail of a large image.

  .. thumbnail:: /_images/image-file-name

External Links
***************

External links should be stored one in the ``source/links.txt`` file in the form:

.. code-block:: RST

  .. _Link Name: URL

Then referenced in topics as:

.. code-block:: RST

  `Link Name_`

.. note::  
 :class: dropdown

 Each ``Link Name`` in the entire documentation project must be unique.


Review Documentation in the Pull Request
*****************************************



Change Log
*************

Finally, ensure that you add a dated summary of your changes
in the ``source/change_log.rst`` file. Your summary should help others understand the purpose of the change.
