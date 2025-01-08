.. _Set Access Restrictions For a Component:

#######################################
Set Access Restrictions for a Component
#######################################

.. tags:: educator, how-to

If you have more than one enrollment track in your course, or if you have
enabled cohorts, you can limit a component's availability to specific groups of
learners. For information about offering different content to different learner
groups, see :ref:`Offering Differentiated Content`.

.. note:: Components inherit any group access restrictions that are set for
   their parent unit. If you set additional group access restrictions for a
   component, make sure the component access settings do not contradict the
   unit access settings. For example, you cannot give Group A of learners
   access to a component if Group A does not have access to the unit that
   contains the component.

To specify a component's access settings, follow these steps.

#. In Studio, select **Content**, and then select **Outline**.

#. On a unit page, for each component for which you want to restrict access to,
   select the **Access Settings** icon.

   .. image:: /_images/educator_how_tos/component_access_settings.png
    :alt: The access settings icon for a component on a Studio unit page
    :width: 500

#. In the **Editing access** dialog box, for the **Restrict access to** option,
   select the group type by which you want to restrict access.

   .. note::  The **Enrollment Track Groups** option is available only if your
       course has more than one :ref:`enrollment track<enrollment_track_g>`.
       The **Content Groups** option is available only if you have created
       :ref:`content groups<About Content Groups>` for use with cohorts.

   .. image:: /_images/educator_how_tos/component_access_select_grouptype.png
    :alt: The access settings dialog for a component, with a dropdown list for
       selecting the type of learner group you will use for restricting access.
    :width: 300

   After you have selected a group type, you see a list of the groups that
   exist for that group type.

#. Select the checkbox for each group for which you want the current component to be available.

#. Select **Save**.

   The groups which have access to the component are listed under the
   component title in the Studio course outline.

   .. image:: /_images/educator_how_tos/component_access_indicator.png
    :alt: When a component has restricted access, a message listing the groups
      which have access to the component appears under the component title in
      the Studio course outline.
    :width: 500

   In addition, on the unit page in Studio, a message in the publishing status
   bar indicates that some content in the unit is restricted to specific groups of learners.


   .. image:: /_images/educator_how_tos/components_restricted_access_indicator.png
    :alt: When any component in a unit has restricted access, a message
      appears in the unit's publishing status bar.
    :width: 250