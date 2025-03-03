.. _Set Access Restrictions For a Unit:

***********************************
Set Access Restrictions For a Unit
***********************************

.. tags:: educator, how-to

If you have more than one enrollment track in your course, or if you have
enabled cohorts, you can limit a unit's availability to specific groups of
learners. For information about offering different content to different learner
groups, see :ref:`Offering Differentiated Content`.

.. note:: A unit's group access settings are inherited by components in the
   unit. If you set additional group access restrictions for a component, make
   sure the component access settings do not contradict the unit access
   settings. For example, you cannot give Group A of learners access to a
   component if Group A does not have access to the unit that contains the
   component.

Tp specify a unit's access settings, follow these steps.

#. In Studio, select **Content**, and then select **Outline**.

#. For the unit that you want to restrict access to, select the **vertical dots**
   icon, then select **Configure** to bring up the unit's configuration menu.

   .. image:: /_images/educator_how_tos/unit-configure-icon.png
    :alt: The vertical dots icon and configure option highlightedin a unit's toolbar in the Studio course outline.
    :width: 500

   You can also access the **Restrict access to** option from the gear icon
   next to a unit's name on a unit page in Studio.


   .. image:: /_images/educator_how_tos/unit-access-settings-gear-icon.png
    :alt: The gear icon next to a unit's title on the unit page in Studio is
       another way to launch the unit access settings dialog.
    :width: 400


#. In the unit's **Settings** dialog box, for the **Restrict access to**
   option, select the group type by which you want to restrict access.

   The **Enrollment Track Groups** option is available only if your course has
   more than one :ref:`enrollment track<enrollment_track_g>`. The **Content
   Groups** option is available only if you have created :ref:`content
   groups<About Content Groups>` for use with cohorts.


   .. image:: /_images/educator_how_tos/unit-access-settings.png
    :alt: The visibility and access settings dialog for a unit, with a
    :width: 200

   After you select a group type, you see a list of the groups that exist for
   that group type.


4. Select the checkbox for each group for which you want the current unit to
   be available.

   .. image:: /_images/educator_how_tos/unit-access-groupselected.png
    :alt: The visibility and access settings dialog for a unit, with
       enrollment track groups selected, and two enrollment tracks available for
       selecting.
    :width: 500

#. Select **Save**.

   The groups which have access to the unit are listed under the unit title in
   the Studio course outline, as well as under the unit title on the unit page
   in Studio.

   .. image:: /_images/educator_how_tos/unit-access-indicator.png
    :alt: When a unit has restricted access, a message listing the groups
       which have access to a unit appears under the unit title in the Studio
       course outline.
    :width: 500

.. seealso::
 
 :ref:`About Course Units` (concept)

 :ref:`Manage Course Units` (how-to)

 :ref:`Copy and Paste Course Units <Copy and Paste Course Units>` (how-to)

 :ref:`Hide a Unit from Learners <Hide a Unit from Students>` (how-to)

 :ref:`Copy and Paste Course Components <Copy and Paste Course Components>` (how-to)

 :ref:`Manage Course Units` (how-to)

 :ref:`The Unit Workflow` (reference)   

**Maintenance chart**

+--------------+-------------------------+----------+-------------------------------------------------------------------+
| Review Date  | Working Group Reviewer  | Release  | Test situation                                                    |
+--------------+-------------------------+----------+-------------------------------------------------------------------+
| 2025-01      | Educators WG - J Swope  | Redwood  | `Fail <https://github.com/openedx/docs.openedx.org/issues/812>`_  |
+--------------+-------------------------+----------+-------------------------------------------------------------------+
