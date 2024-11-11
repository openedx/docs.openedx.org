.. :diataxis-type: how-to

.. _Hide a Subsection from Students:

***********************************
Hiding a Subsection from Learners
***********************************

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

========================================
Entirely Hide a Subsection from Learners
========================================

You can completely hide a subsection and its content from learners, regardless
of the status of units within the section. Subsections hidden in this way are
not shown in the course navigation, and are not included when grades are
calculated.

To entirely hide a subsection from learners, follow these steps.

#. Select the **Configure** icon in the subsection box.

   .. image:: /_images/educator_how_tos/subsections-settings-icon.png
     :alt: A subsection in the course outline with an arrow pointing to the
        configure icon.
     :width: 500

   The subsection settings dialog box opens.

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

========================================
Hide a Subsection Based on Date
========================================

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

#. Select the **Configure** icon in the subsection box.

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
