.. _Manage Course Sections:

#########################
Manage Course Sections
#########################

.. tags:: educator, how-to

.. contents::
  :local:
  :depth: 1

.. _Create a Section:

********************************
Create a Section
********************************

To create a new section, follow these steps.

.. START CREATE A SECTION

#. Open the course outline in Studio.

#. Click :guilabel:`New Section`.

   A new section is created at the end of the course content, with the section name selected.

#. Enter the name for the new section. A descriptive name can help learners
   locate content in the course. It can also help you select content when
   you analyze performance in reporting or analytics systems.

#. :ref:`Add subsections<Create a Subsection>` to the new section as needed.

.. END CREATE A SECTION

If you do not change the :ref:`course start date<Set Start and End Dates>`
default value, ``1/1/2030``, when you create a new section, its release date
will be ``Unscheduled``.

If you have modified the course start date, when you create a new section, the
default release date is the course start date.

.. caution::
 If the course start date is in the past, newly created sections are
 immediately visible to learners.

It is recommended that you :ref:`test course content <Testing Your Course
Content>` as you create new sections.

********************************
Change a Section Name
********************************

To edit a section name, move your cursor over the section name to show the
**Edit** icon.

.. image:: /_images/educator_how_tos/section-edit-icon.png
  :alt: The Edit Section Name icon.
  :width: 500

Select the **Edit** icon next to the section name. The name field becomes
editable. Enter the new name, and then tab or click outside of the field to
save the name.

.. _Set a Section Release Date:

********************************
Set a Section Release Date
********************************

To set the section release date, follow these steps.

#. Select the **Configure** option from the kebab menu in the section box.

   .. image:: /_images/educator_how_tos/section-settings-box.png
    :alt: The section settings icon circled.
    

   The **Settings** dialog box opens.

#. Enter the release date and time for the section.

   .. note::
      The time that you set is in Coordinated Universal Time (UTC). You might want
      to verify that you have specified the time that you intend by using a time
      zone converter such as `Time and Date Time Zone Converter`_.

#. Select **Save**.

For more information, see :ref:`Release Dates`.


.. _Publish all Units in a Section:

********************************
Publish All Units in a Section
********************************

To publish all new and changed units in a section, select the **Publish** option
in the kebab menu for the section.

.. image:: /_images/educator_how_tos/outline-publish-icon-section.png
 :alt: Publishing icon for a section.

.. note::
 The **Publish** icon only appears when there is new or changed content within
 the section.

For more information about statuses and visibility to learners, see :ref:`Unit
Publishing Status`.

.. _Hide a Section from Students:

********************************
Hide a Section from Learners
********************************

You can hide all content in a section from learners, regardless of the status
of subsections and units within the section.

For more information, see :ref:`Content Hidden from Students`.

To hide a section from learners, follow these steps.

#. Select the **Configure** icon in the section box.

   .. image:: /_images/educator_how_tos/section-settings-box.png
    :alt: The section settings icon circled.
    :width: 500

   The **Settings** dialog box opens.

#. In the **Section Visibility** section, select **Hide from learners**.

#. Select **Save**.

Now, none of the content in the section is visible to learners.

To make the section visible to learners, repeat these steps and deselect **Hide
from learners**.

.. warning::  When you deselect **Hide from learners** for a section, not all
   content in the section is necessarily made visible to learners. If you
   explicitly set a subsection or unit to be hidden from learners, it remains
   hidden from learners. Unpublished units remain unpublished, and changes to
   published units remain unpublished.


********************************
Delete a Section
********************************

When you delete a section, you delete all subsections and units within the
section.

.. warning::
 You cannot restore course content after you delete it. To ensure you do not
 delete content you may need later, you can move any unused content to a
 section in your course that you set to never release.

To delete a section, follow these steps.

#. Select the **Delete** option from the kebab menu of the section that you want to delete.

  .. image:: /_images/educator_how_tos/section-delete.png
   :alt: The section with Delete button highlighted.
   :width: 500

2. When you receive the confirmation prompt, select **Delete** to confirm the deletion.


.. seealso::

  :ref:`Guide to Course Content Development` (reference)

  :ref:`Create a New Course` (how-to)

  :ref:`About the Course Outline` (concept)

  :ref:`Manage Course Outline` (how-to)

  :ref:`Modify Settings for Objects in the Course Outline` (how-to)

  :ref:`Publish Content from the Course Outline` (how-to)

  :ref:`About Course Sections` (concept)

  :ref:`About Course Subsections` (concept)

  :ref:`About Course Units` (concept)

  :ref:`Manage Course Subsections` (how-to)

  :ref:`Manage Course Units` (how-to)

  :ref:`View as Learner` (how-to)
 

**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                 |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| 07/07/2025   | Leira (Curricu.me)            |  Sumac         | Pass                                                          |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| 03/05/2025   | Leira (Curricu.me)            |  Sumac         |Fail (https://github.com/openedx/docs.openedx.org/issues/862)  |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
