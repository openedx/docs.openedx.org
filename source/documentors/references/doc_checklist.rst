Documentation Checklist
#############################

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

For more information, see :doc:`../concepts/doc_audiences`.

Topic Types
************

Each topic in the documentation is one of four types:

* How to

* Reference

* Concepts

* Quickstarts

Ensure that you have clearly identified the types of new topics you have created, and have stored new files in the directory for that topic type.

For more information, see :doc:`../concepts/content_types`.


New Topics in TOCs
*******************

Every new topic must be added to a table of contents. Add each new topic to the audience home page in the appropriate place.


RST Standards
**************

Ensure that the new documentation adheres to RST standards and Open edX best practices. You should use :doc:`../references/doc_templates` as much as possible, and review :doc:`../references/doc_guidelines`.


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

When you create a pull request, a version of the documentation with your changes is automatically built, as a website that matches ``https://docs.openedx.org`` except for your changes.  You can tell that the site built for your pull request is different than the main Open edX documentation because the URL includes your pull request number, and because the following warning appears at the top of each page:

.. image:: /_images/pr_doc_warning.png

You must ensure that the documentation for the pull request  builds successfully, with no errors or warnings. You can access documentation build information in the pull request. The following example shows a successful documentation build:

.. image:: /_images/pr_doc_link.png


In the pull request, click **Details** to see the documentation with your changes. Ensure the changes are published in the way you expect.

If there is an error when building the documentation, the pull request will indicate that checks failed, and the **Details** link will take you to the error message. If you are able to fix the issue indicated by the error message, do so; if not, contact the Open edX team for assistance.


