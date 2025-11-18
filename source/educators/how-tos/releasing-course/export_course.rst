.. _Export a Course:

###############
Export a Course
###############

.. tags:: educator, how-to

When you have released your course, you can use the course export and import
tools in Studio to save a backup copy of the course, and optionally re-import
your course for editing. For more information, see :ref:`Export a Course` and
:ref:`Import a Course` through Studio.

When you import and export a course, you work with :ref:`.tar.gz files <Work
with the targz file>`.

To duplicate an existing course for a new run, course creators can use the
course re-run option. See :ref:`Re Run a Course`.

.. caution::
  Before exporting and importing a course, ensure that links in the course to
  other course content use the ``/jump_to_id/<unit identifier>`` syntax. If a
  link does not use the ``/jump_to_id/<unit identifier>`` syntax, the link will
  be broken if you export then import the course. For more information, see
  :ref:`Add a Link to a Course Unit`.

There are several reasons you might want to export your course. Examples
follow.

* To save your work.
* To edit the XML in your course directly.
* To create a backup copy of your course, which you can import if you want to
  revert the course back to a previous state.
* To share with the team members of another course.
* To create a copy of your course that you can later import into another course
  instance and customize.

When you export your course, Studio creates a ``.tar.gz`` file that includes
the following course data.

* Course content (all Sections, Subsections, and Units)
* Course structure
* Individual problems
* Pages
* Course assets
* Course settings
* Prerequisite course subsection settings

The following data is not exported with your course.

* User data
* Course team data
* Discussion data
* Certificates

To export your course, follow these steps.

#. From the **Tools** menu in the header, select **Export**.

   .. image:: /_images/educator_how_tos/tools_menu_export_course.png
    :width: 600
    :alt: Selecting the "Export Course" option from the Tools menu in the page header.

#. Select **Export Course Content**.

   .. image:: /_images/educator_how_tos/course_export_page.png
    :width: 600
    :alt: an image of the Export page in which you can export courses and edit them outside of Studio.

#. When the export is complete, click **Download Exported Course**.

   .. image:: /_images/educator_how_tos/download_exported_course.png
    :width: 600
    :alt: an image of the Export page when the export is complete, showing the Download Exported Course button

When the export completes and is downloaded, you can then access the ``.tar.gz`` file on your
computer.

.. seealso::
 

 :ref:`Import a Course` (how-to)

 :ref:`Course Export File Terminology` (reference)

 :ref:`Work with the targz File` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+-----------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                   |
+--------------+-------------------------------+----------------+-----------------------------------------------------------------+
| 2025-04-13   | sarina                        | Sumac          | Pass                                                            |
+--------------+-------------------------------+----------------+-----------------------------------------------------------------+
| 2025-03-07   | Docs WG                       | Sumac          | `Fail <https://github.com/openedx/docs.openedx.org/issues/954>`_|
+--------------+-------------------------------+----------------+-----------------------------------------------------------------+
