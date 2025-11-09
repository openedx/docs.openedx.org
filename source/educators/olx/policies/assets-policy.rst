.. _Course Asset Policy:

#####################################################
Create Course Assets and Textbooks in OLX
#####################################################

.. tags:: educator, how-to

You create an asset policy file to provide details of the assets used in your
course. Assets can include image files, textbooks, and handouts.

.. contents::
  :local:
  :depth: 1

You must enter policy details for each asset you add to the ``static``
directory. For more information, see :ref:`Course Assets`.

*******************************
Create the Asset Policy File
*******************************

You define policies for your assets in the ``assets.json`` file.

Save the ``assets.json`` file in the ``policy`` directory. You use one
``assets.json`` file for all of the courses you might have in your directory
structure.

************************************
Asset Policy JSON Objects
************************************

For each asset, the following fields must be provided in a JSON dict for that asset:

.. list-table::
    :widths: 10 80
    :header-rows: 0

    * - ``contentType``
      - The MIME type of the file.
    * - ``content_son``
      - A collection that contains:
         * ``category``:  Equal to ``asset``.
         * ``course``: The course number.
         * ``name``: The file name.
         * ``tag``:
         * ``org``: The organization that created the course.
         * ``revision``
    * - ``displayname``
      - The file name.
    * - ``filename``
      - The full path and name of the file in the Open edX Platform.
    * - ``import_path``
      - ``null`` (TBD - why?)
    * - ``locked``
      - ``true`` if users can only access the file from within your course.
        ``false`` if users can access the file from outside of your course.      
    * - ``thumbnail_location``
      - Either ``null`` (for assets without a thumbnail type, such as PDFs), or, an array containing:
         * ``c4x``
         * The organization.
         * The course number.
         * ``thumbnail``
         * The filename for the thumbnail.
         * ``null`` (TBD - why?)


*******************************
Example Asset Policy File
*******************************

The following example shows the JSON policy for an image file and a PDF textbook.

.. code-block:: json

  {
      "Education_for_a_Digital_World.pdf": {
          "contentType": "application/pdf",
          "content_son": {
              "category": "asset",
              "course": "OLXex",
              "name": "Education_for_a_Digital_World.pdf",
              "org": "OpenedX",
              "revision": null,
              "run": "2025",
              "tag": "c4x"
          },
          "custom_md5": "be2c4a1483397675d7bd124c100d02f9",
          "displayname": "Education_for_a_Digital_World.pdf",
          "filename": "asset-v1:OpenedX+OLXex+2025+type@asset+block@Education_for_a_Digital_World.pdf",
          "import_path": null,
          "locked": false,
          "thumbnail_location": null
      },
      "Intro_to_OLX_course_card.png": {
          "contentType": "image/png",
          "content_son": {
              "category": "asset",
              "course": "OLXex",
              "name": "Intro_to_OLX_course_card.png",
              "org": "OpenedX",
              "revision": null,
              "run": "2025",
              "tag": "c4x"
          },
          "custom_md5": "f007dbebf9fb14d666a01614b97a860e",
          "displayname": "Intro to OLX course card.png",
          "filename": "asset-v1:OpenedX+OLXex+2025+type@asset+block@Intro_to_OLX_course_card.png",
          "import_path": null,
          "locked": false,
          "thumbnail_location": [
              "c4x",
              "OpenedX",
              "OLXex",
              "thumbnail",
              "Intro_to_OLX_course_card-png.jpg",
              null
          ]
      },
    }

.. _Course Textbooks OLX:

*********************************************
Create Textbooks
*********************************************

As described above, first upload a textbook asset to
your course in the ``static`` directory.

.. admonition:: Accessibility concerns

  See the notes in the :ref:`Add Course Textbooks` article around accessibility - namely, that
  PDF textbooks are accessible whereas PNG/image files are not.

Then, as described above, link it in your ``assets.json`` file.

Finally, update the ``policy.json`` file (described in :ref:`Course Policies`)
with information in the ``pdf_textbooks`` key:

.. code-block:: json

  {
    "course/2025": {
      ...
      "pdf_textbooks": [
          {
              "chapters": [
                  {
                      "title": "Full Book",
                      "url": "/asset-v1:OpenedX+OLXex+2025+type@asset+block@Education_for_a_Digital_World.pdf"
                  }
              ],
              "id": "6Education_for_a_Digital_World",
              "tab_title": "Education for a Digital World: Advice, Guidelines and Effective Practice from Around Globe"
          }
      ],
      ...
  }      

.. seealso::

  :ref:`Add Course Assets` (reference)

  :ref:`Course Assets in OLX <Course Assets>` (how-to) 

  :ref:`What is Open Learning XML?` (concept)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
