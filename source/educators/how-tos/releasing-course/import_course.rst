.. _Import a Course:

###############
Import a Course
###############

.. tags:: educator, how-to

.. youtube:: q8QJB5KVKbw

When you have released your course, you can use the course export and import
tools in Studio to save a backup copy of the course, and optionally re-import
your course for editing. For more information, see :ref:`Export a Course` and
:ref:`Import a Course` through Studio.

When you import and export a course, you work with :ref:`.tar.gz files <Work
with the targz file>`.

To duplicate an existing course for a new run, course creators can use the
course re-run option. See :ref:`Rerun a Course`.

.. caution::
  Before exporting and importing a course, ensure that links in the course to
  other course content use the ``/jump_to_id/<unit identifier>`` syntax. If a
  link does not use the ``/jump_to_id/<unit identifier>`` syntax, the link will
  be broken if you export then import the course. For more information, see
  :ref:`Add a Link to a Course Unit`.

.. warning::
	Content of the imported course replaces all the content of this course.
	**You cannot undo a course import**. We recommend that you first export the
	current course, so you have a backup copy of it.

There are several reasons you may want to import a course. Some examples
follow.

* To load a course you developed outside of Studio.
* To run a new version of a course that was not created in Studio.
* To prepare course content for reuse in another learning system.

The course that you import must be in a ``.tar.gz`` file (that is, a .tar file
compressed with GNU Zip). This ``.tar.gz`` file must contain a ``course.xml`` file in a
course data directory. The ``tar.gz`` file must have the same name as the course
data directory. It may also contain other files.  For more information, see
:ref:`Work with the targz file`.

If your course uses legacy layout structures, you may not be able to edit the
course in Studio. To make sure that your course is completely editable, ensure
that all components are embedded in a unit.

The import process has five stages. During the first two stages, you must stay
on the Course Import page. You can leave this page after the Unpacking stage
has completed. Open edX community recommends, however, that you don't make important changes
to your course until the import operation has completed.

To import a course, follow these steps.

#. From the **Tools** menu, select **Import**.
#. Select **Choose a File to Import**.
#. Locate the file that you want, and then Select **Open**.

.. image:: /_images/educator_how_tos/course_import_page.png
 :width: 600
 :alt: an image of the Import page in which you can select a ``.tar.gz`` file to
  replace your course content.

.. note::
 When you import a course, important dates, such as the course start date and
 time, are overwritten. After the import is complete, you should check dates to
 ensure they are set as intended. For more information, see
 :ref:`Set Course Schedule`.

.. seealso::
 

 :ref:`Export a Course` (how-to)

 :ref:`Course Export File Terminology` (reference)

 :ref:`Work with the targz File` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
