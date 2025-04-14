.. _Manage Course Subsections:

###########################
Manage Course Subsections
###########################

.. tags:: educator, how-to

.. contents::
  :local:
  :depth: 1

.. _Create a Subsection:

********************************
Create a Subsection
********************************

.. START CREATE A SUBSECTION

To create a new subsection, follow these steps.

#. In the outline, expand the section in which you want to create a new
   subsection.
#. Select **New Subsection** at the bottom of the expanded section. A new
   subsection appears at the end of the section, with the subsection name
   selected.
#. Enter the name for the new subsection. A descriptive name can help learners
   locate content in the course. It can also help you select content when you
   analyze performance in reporting and analytics systems.
#. :ref:`Add units<Manage Course Units>` to the new subsection as needed.

.. END CREATE A SUBSECTION

It is recommended that you :ref:`test course content <Testing Your Course
Content>` as you create new subsections.

********************************
Change a Subsection Name
********************************

To change a subsection name, select the **Edit** icon next to the subsection
name. The name field becomes editable. Enter the new name, and then tab or
click outside of the field to save the name.

.. _Set a Subsection Release Date:

********************************
Set a Subsection Release Date
********************************

If the subsection should release at a later time than the containing section, set the release date. To set the subsection release date, follow these steps.

#. Select the **Configure** option from the kebab menu in the subsection box.

   .. image:: /_images/educator_how_tos/subsections-settings-icon.png
    :alt: A subsection in the course outline with the configure option highlighted.

   The subsection settings dialog box opens.

#. On the **Basic** tab, under **Release Date and Time**, enter the release
   date and time for the subsection.

   .. note:: The time that you set is in Coordinated Universal Time (UTC). You
      might want to verify that you have specified the time that you intend by
      using a time zone converter such as `Time and Date Time Zone Converter`_.

      Learners who have specified a time zone in their account settings see
      course dates and times converted to their specified time zone. Learners
      who have not specified a time zone in their account settings see course
      dates and times on their dashboards, in the body of the course, and on
      their **Progress** pages in the time zone that their browsers specify.
      Learners see other course dates and times in UTC.

   .. image:: /_images/Educators_subsection_settings_basic.png
    :alt: Subsection Settings Basics tab with the Release Date and Grade As fields

#. Select **Save**.

For more information, see :ref:`Release Dates`.

.. _Hide a Subsection from Students:

********************************************
Hide a Subsection from Learners
********************************************

You can hide a subsection from learners in the following ways.

* :ref:`Entirely hide the subsection <Entirely Hide a Subsection>` so that it
  does not appear in course navigation. Subsections that are hidden in this
  way are not included when grades are calculated.

* :ref:`Prevent learners from accessing <Hide a Subsection After its Due
  Date>` a subsection's contents after its due date (for instructor-led
  courses) or the course end date (for self-paced courses) has passed, but
  keep the subsection visible in course navigation. Subsections that are
  hidden based on date remain included when grades are calculated.

You can also hide just the answers to problems in the subsection, leaving the
problems visible. For more information, see :ref:`Problem Results Visibility`.

For more information, see :ref:`Content Hidden from Students`.


.. _Entirely Hide a Subsection:

==========================================
Entirely Hide a Subsection from Learners
==========================================

You can completely hide a subsection and its content from learners, regardless
of the status of units within the section. Subsections hidden in this way are
not shown in the course navigation, and are not included when grades are
calculated.

To entirely hide a subsection from learners, follow these steps.

#. Select the **Configure** option from the kebab menu in the subsection box.

   .. image:: /_images/educator_how_tos/subsections-settings-icon.png
     :alt: A subsection in the course outline with the configure option highlighted.

   The subsection settings dialog box opens.

   .. image:: /_images/Educators_subsection_settings_visibility.png
      :alt: Subsection Settings Visibility tab with the Show entire subsection option selected.
      :width: 500

#. On the **Visibility** tab, locate **Subsection Visibility**, and then select
   **Hide entire subsection**.


#. Select **Save**.

None of the content in the subsection is visible to learners. In the course
outline, the subsection is shown with a lock icon, indicating that it is
available only to course staff.

To make the subsection visible to learners, repeat these steps and select
**Show entire subsection**.

.. warning::  When you make a previously hidden subsection visible, not all
   content in the subsection is necessarily made visible to learners. Units
   that were explicitly hidden from learners remain hidden.


.. _Hide a Subsection After its Due Date:

==========================================
Hide a Subsection Based on Date
==========================================

You can make a subsection's content unavailable based on date. For example, you
might want to make exam questions unavailable after a certain date. For
instructor-led courses, this option uses the subsection's due date. For self-
paced courses, this option uses the course's end date.

Subsections that are hidden in this way remain visible in the course
navigation, and are included when grades are calculated. However, learners can
no longer access the subsection's content after the due date or the course end
date.

.. note::
  If you want to continue to show a subsection's content, but hide learners'
  results for problems in the subsection, see :ref:`Problem Results
  Visibility`.

To hide a subsection based on date, follow these steps.

#. Select the **Configure** option from the kebab menu in the subsection box.

   The subsection settings dialog box opens.

#. On the **Visibility** tab, locate **Subsection Visibility**, and then select
   the appropriate option.

   * In instructor-led courses, select **Hide content after due date**.

   * In self-paced courses, select **Hide content after course end date**.

#. Select **Save**.

Learners who access the subsection after the due date or course end date has
passed are shown a message indicating that the subsection is no longer
available because the due date (or course end date) has passed.

In the course outline in Studio, the subsection is shown with an icon and a
"Subsection is hidden after due date" or "Subsection is hidden after course
end date" message under the subsection's display name.


.. _Publish all Units in a Subsection:

**********************************
Publish All Units in a Subsection
**********************************

To publish all new and changed units in a subsection, select the **Publish**
icon in the box for the subsection.

.. image:: /_images/educator_how_tos/outline-publish-icon-subsection.png
 :alt: Part of a course outline with the publishing icon for a subsection
     circled.
 

See :ref:`Unit Publishing Status` for information about statuses and visibility
to learners.


.. _Delete a Subsection:

********************************
Delete a Subsection
********************************

When you delete a subsection, you delete all units within the subsection.

.. warning::
 You cannot restore course content after you delete it. To ensure you do not
 delete content that you might need later, you can move any unused content to a
 section in your course that you set to never release.

To delete a subsection, follow these steps.

#. In the subsection that you want to delete, select the **Delete** option from the kebab menu.

  .. image:: /_images/educator_how_tos/subsection-delete.png
   :alt: Part of a course outline showing a subsection with the Delete icon
       circled.

#. When the confirmation prompt appears, select **delete** to confirm.

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

  :ref:`Manage Course Sections` (how-to)

  :ref:`Manage Course Units` (how-to)

  :ref:`View as Learner` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                 |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| 03/19/2025   | John (Curricu.me)            | Sumac           |Pass                                                           |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
| 03/05/2025   | Leira (Curricu.me)            | Sumac          |Fail (https://github.com/openedx/docs.openedx.org/issues/863   |
+--------------+-------------------------------+----------------+---------------------------------------------------------------+
