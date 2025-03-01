.. _Manage Content Experiments:

Manage Content Experiments
#############################################

.. tags:: educator, how-to

.. contents::
  :local:
  :depth: 2  

This how-to provides instructions for configuring your course to enable
:ref:`content experiments<Overview of Content Experiments>`. 

.. _Enable Content Experiments:

*********************************
Enable Content Experiments
*********************************

To enable content experiments in your course, you must add ``split_test`` to the
**Advanced Module List** in Advanced Settings. To do it, follow the next steps:

.. note:: ``split_test`` is the internal name for a content experiment.

#. From the **Settings** menu, select **Advanced Settings**.

#. On the **Advanced Settings** page, locate **Advanced Module List**.

#. In the **Advanced Module List** field, add ``"split_test"``. Be sure that
   you include the double quotation marks.

   If you have multiple values, ensure that they are separated by commas
   (``,``).

   For example, the text in the **Advanced Module List** field may resemble
   the following:

   .. code-block:: none

     [
       "lti_consumer",
       "word_cloud",
       "split_test"
     ]

#. Select **Save Changes**.


.. _Set up Group Configurations in Studio:

#. To set up group configurations, on the **Settings** menu, select **Group
Configurations**. The **Group Configurations** page opens.

#. From this page you can :ref:`create<Create a Group Configuration>`,
:ref:`edit<Edit a Group Configuration>`, and :ref:`delete<Delete a Group
Configuration>` group configurations. You can also :ref:`view content
experiments that use a group configuration<View Experiments that Use a Group
Configuration>`.

.. _Create a Group Configuration:

*****************************
Create a Group Configuration
*****************************

You can create a group configuration at any time and used to creat :ref: content experiments in your courses <Manage Content Experiments>

#. On the **Group Configurations** page, under **Experiment Groups**, select
   **New Experiment Group**. The following page opens:

   .. image:: /_images/educator_how_tos/create-group-config.png
    :width: 800
    :align: center
    :alt: An image of the Create a New Group Configuration page in Studio.

#. Enter a name in the **Group Configuration Name** field. Use a meaningful
   name, because you will select from group configuration names when you create
   content experiments. Learners do not see the group configuration name.

#. Optionally, enter a description for the new group configuration.

#. By default, a new configuration already contains two groups. Modify the
   groups or add and delete groups as needed. A group configuration must have
   at least one group.

   * Modify group names as needed. You see group names in the unit page in
     Studio, but group names are not visible to learners.
   * Select **Add another group** to include another group as part of the
     configuration.
   * Select the **X** to the right of an existing group to remove it from the
     configuration. A group configuration must have at least one group.

#. Select **Create** to save the new group configuration.

The group configuration is then listed in the page. You can see the number of
groups that the configuration contains, as well as whether the configuration is
in use in the course:

.. image:: /_images/educator_how_tos/group_configurations_one_listed.png
    :width: 800
    :align: center
    :alt: The Group Configurations page with one group configuration listed.

.. _Create a Content Experiment:

*****************************
Create a Content Experiment
*****************************

Before you add content experiments to your course, ensure that you have
completed the following tasks.

* :ref:`Enable Content Experiments`

#. On the unit page, under **Add New Component**, select **Advanced**.

#. Select **Content Experiment**.

   A new content experiment is added to the unit.

   .. image:: /_images/educator_how_tos/content_experiment_block.png
    :width: 600
    :alt: An image showing the content experiment component in a unit page in
        Studio.

   The content experiment includes a container for each group that is defined
   in the group configuration you selected. You create content for each
   experiment group as you do any other component. For more information, see
   :ref:`Add a Component`.

#. Select either **Select a Group Configuration** or **Edit** to open the
   content experiment component.

   .. image:: /_images/educator_how_tos/content_experiment_editor.png
    :alt: An image of the content experiment editor in Studio.
    :width: 600

#. For **Group Configuration**, select a group configuration.

#. In the **Display Name** field, enter the name of the component. The display
   name is only used in Studio; learners do not see this value.

#. Select **Save**.

The content experiment is displayed as a component that contains other
components. For more information, see :ref:`Components that Contain Other
Components`.

You can now create content for the groups in the experiment.

.. warning::

   Do not create new content experiments by duplicating configured content
   experiments. Duplicating content experiments after you have configured them
   is not supported.

.. _Create Content for Content Experiment Groups:

*****************************************************
Create Content for Groups in the Content Experiment
*****************************************************

Before you add content experiments to your course, ensure that you have
completed the following tasks.

* :ref:`Enable Content Experiments`

#. After you select a group configuration in the content experiment component,
select **View**.

#. The content experiment page that opens automatically includes a container for
each group that is defined in the group configuration you selected. For
example, if you select a group configuration that defines two groups, Group A
and Group B, you see the following page.

.. image:: /_images/educator_how_tos/content_experiment_container.png
 :alt: An image of the content experiment page in Studio, with two groups.
 :width: 600

#. You add content for both groups as needed, just as you would add content to
any container page. For more information, see :ref:`Components that Contain
Other Components`.

For example, you can add a Text component and a video to Group A.

.. image:: /_images/educator_how_tos/a_b_test_child_expanded.png
 :alt: An image of an expanded content experiment component with an HTML and
     video component.
 :width: 600

.. note::   It is valid, and can be useful, to have no content for a group in
   a content experiment. For example, if one group has a video and another
   group has no content, you can analyze the effect of the video on learner
   performance.

.. _Change Group Configuration for a Content Experiment:

*******************************************************
Change the Group Configuration for a Content Experiment
*******************************************************

You can change the group configuration for a content experiment. When you
change the group configuration, you edit the content for any additional groups
in the group configuration. You can use the components from the previous
groups, as well as create new components.

.. warning::   Changing the group configuration of a learner-visible content
   experiment will affect the experiment data.

#. Open the unit that contains the content experiment.

#. In the content experiment component, select **Edit**.

   .. image:: /_images/educator_how_tos/content_experiment_editor_group2.png
    :alt: An image of the content experiment editor in Studio, with a group
        configuration selected.
    :width: 600

#. Select a different group configuration.

#. Select **Save**.

#. You must now add components to the new groups in the experiment. Select
   **View** to open the content experiment.

   You see that groups for the new configuration are empty, and any components
   that you had added to groups in the previous configuration are now moved to
   a section called **Inactive Groups**.

   .. image:: /_images/educator_how_tos/inactive_groups.png
    :alt: An image of a content experiment in Studio, with components in an
        inactive group.
    :width: 600

#. Drag and drop components from the **Inactive Groups** section into the new
   groups. You can also create new components in the new groups.


.. _Edit a Group Configuration:

*****************************
Edit a Group Configuration
*****************************

.. important:: You can change the name of a group configuration at any time.
   However, before you modify any other characteristics of a group
   configuration that is currently used in a running course, review :ref:`Guidelines for Modifying Group Configurations`.

#. On the **Group Configurations** page, hover over the group configuration and
   select **Edit**.

   .. image:: /_images/educator_how_tos/group_configurations_edit.png
    :width: 800
    :align: center
    :alt: An image of the Group Configurations page with the Edit button
        highlighted.

   The following page opens:

   .. image:: /_images/educator_how_tos/save-group-config.png
    :width: 800
    :align: center
    :alt: An image of the Edit a Group Configuration page.

#. On the **Edit a Group Configuration** page, modify the name and description as
   needed.

#. Modify groups in the configuration as needed. See :ref:`Create a Group
   Configuration` for details.

#. Select **Save** to save your changes.

.. _View Experiments that Use a Group Configuration:

================================================
View Experiments that Use a Group Configuration
================================================

You can view the content experiments that use each of your group
configurations.

On the **Group Configurations** page, select the name of a group to see its
details. You see links to the content experiments that use this group
configuration.

.. image:: /_images/educator_how_tos/group_configurations_experiments.png
 :alt: An image of a group configuration with the content experiments using the
     configuration circled.
 :width: 800

Select a link to go to the unit that contains the content experiment.

================================================
View a Group Configuration from an Experiment
================================================

When working with a content experiment, you can view details about the group
configuration used by that experiment in two ways.

* In a unit that contains a content experiment, the content experiment
  block, select the name of the group configuration.

  .. image:: /_images/educator_how_tos/content_experiment_group_config_link.png
   :alt: An image of the content experiment on the unit page with the group
     configuration link circled
   :width: 800

* At the top of the content experiment page, select the name of the group
  configuration.

  .. image:: /_images/educator_how_tos/content_experiment_page_group_config_link.png
   :alt: An image of the content experiment page with the group configuration
       link circled.
   :width: 800

In both cases, the group configuration opens.

.. image:: /_images/educator_how_tos/group_configurations_experiments.png
 :alt: An image of the Group Configuration page with the experiments using it
     circled.
 :width: 800

You can use the link in the group configuration to return to the unit that
contains the content experiment.

.. _Delete a Group Configuration:

*****************************************************
Delete a Group Configuration
*****************************************************

.. note::
 You can only delete a group configuration not currently used in a
 content experiment. You cannot delete a group configuration used in a
 content experiment.

#. On the **Group Configurations** page, hover over the group configuration and
   select the Delete icon.

   .. image:: /_images/educator_how_tos/group-configuration-delete.png
    :alt: The Delete icon circled for a group configuration.
    :width: 800

#. When prompted to confirm the deletion, select **Delete**.

.. seealso::
 
 :ref:`About Content Experiments` (concept)

 :ref:`Guidelines for Modifying Group Configurations` (reference)

 :ref:`Add a Content Experiment in OLX` (how-to)

 :ref:`Test Content Experiments` (how-to)

 :ref:`Experiment Group Configurations` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2024/12      | Documentation WG - Ana Gomez  |Redwood         |Pass.                           |
+--------------+-------------------------------+----------------+--------------------------------+
