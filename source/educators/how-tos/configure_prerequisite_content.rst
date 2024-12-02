.. _configuring_prerequisite_content:

################################
Prerequisite Course Subsections
################################

.. tags:: educator, how-to

You can lock subsections of your course until learners complete other,
prerequisite subsections. If a subsection has a prerequisite, it is displayed
in the course outline with a lock icon, and learners cannot view the subsection
content until they have earned a minimum score in the prerequisite subsection.

.. note::
   You must first :ref:`Enable Course Prerequisites` before
   prerequisite course subsections can be used.

.. _enabling_subsection_gating:

********************************
Enable Subsection Prerequisites
********************************

To enable prerequisite subsections in a course, follow these steps.

#. From the **Settings** menu, select **Advanced Settings**.

#. In the **Enable Subsection Prerequisites** field, enter ``true``.

#. Select **Save Changes**.

.. _creating_a_prerequisite_subsection:

********************************
Create a Prerequisite Subsection
********************************

To prevent learners from seeing a subsection of your course until they have
earned a minimum score or completed a minimum portion in a prerequisite
subsection, follow these steps.

.. note::
    Make sure that you configure subsection prerequisites in the order that you
    intend for learners to encounter them in the course content. The
    prerequisite configuration controls do not prevent you from creating a
    circular chain of prerequisites that will permanently hide them from
    learners.

.. note::
    You cannot use :ref:`open response assessments<Open Response Assessments
    Two>` that have a point value of 0 as the prerequisite for other course
    subsections.

#. Enable subsection prerequisites for your course. For more information, see
   :ref:`enabling_subsection_gating`.

#. Select the **Configure** icon for the subsection that must be completed
   first. This is the prerequisite subsection.

   .. image:: /_images/educator_how_tos/subsections-settings-icon.png
     :alt: A subsection in the course outline with the configure icon
      indicated.
     :width: 600

#. Select the **Advanced** tab.

#. Under **Use as a Prerequisite**, select **Make this subsection available as
   a prerequisite to other content**.

#. Select **Save**.

#. Select the **Configure** icon for the subsection that
   will be hidden until the prerequisite is met.

#. Select the **Advanced** tab, and then locate the **Limit Access** section.

#. In the **Prerequisite** list, select the name of the subsection you want to
   specify as the prerequisite.

      .. image:: /_images/educator_how_tos/prerequisite-percent-complete.png
       :alt: The Limit Access section in the Advanced settings, showing the
           Prerequisite, Minimum Score, and Minimum Completion Percentage
           controls.

#. To require that learners achieve a minimum score in the prerequisite
   subsection before the current subsection opens, enter the percent of the
   total score that learners must earn in the **Minimum Score** field. If
   the prerequisite section is not a problem set, set **Minimum Score** to
   ``0`` and set **Minimum Completion Percentage** to a value greater than
   zero.

   For example, if the prerequisite subsection includes four problems and each
   problem is worth the same number of points, set the **Minimum Score** to
   ``75`` to require at least three correct answers.

   To require that learners complete a minimum portion of the prerequisite
   subsection before the current subsection opens, enter the percent of the
   prerequisite subsection that learners must complete in the **Minimum
   Completion Percentage** field.

   If you set both the **Minimum Score** field and the **Minimum Completion
   Percentage** field to a value greater than zero, then learners must satisfy
   both conditions in the prerequisite section before they can view the
   current subsection. The default value for both the **Minimum Score** field
   and the **Minimum Completion Percentage** field is ``100``.

#. Select **Save**.

#. In the course outline, if a subsection has a prerequisite, the prerequisite
   name appears under the subsection name.

   .. image:: /_images/educator_how_tos/studio-locked-content.png
     :alt: A subsection in the course outline with a prerequsitie indicated.
     :width: 600

  .. note:: Prerequisite course subsection settings are not retained when
     you :ref:`export or import a course<Exporting and Importing a Course>`, or
     when you :ref:`re-run a course<Rerun a Course>`.