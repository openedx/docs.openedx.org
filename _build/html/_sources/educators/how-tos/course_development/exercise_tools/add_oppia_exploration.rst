.. _Enable the Oppia Exploration Tool:

Enable the Oppia Exploration Tool
#################################

.. tags:: educator, how-to

Before you can add an Oppia exploration to your course, you must enable this
tool in Studio.

To enable the Oppia exploration tool in Studio, you add the ``"oppia"`` key to
the **Advanced Module List** on the **Advanced Settings** page. (Be sure to
include the quotation marks around the key value.) For more information, see
:ref:`Enable Additional Exercises and Tools`.

***********************************
Add an Oppia Exploration in Studio
***********************************

You must :ref:`enable the Oppia exploration tool <Enable the Oppia Exploration
Tool>` before you add a component with an exploration to your course. You must
also select the Oppia exploration that you want to add, and obtain both the URL
of the website that hosts that exploration and its ID.

#. On the **Course Outline** page, open the unit in an ungraded subsection
   where you want to add the exploration.

#. Under **Add New Component**, select **Advanced**, and then select **Oppia
   Exploration**. The new component is added to the unit.

#. In the new component, select **Edit**.

   .. image:: /_images/educator_references/oppia_studio.png
     :alt: The Edit component dialog box for an Oppia exploration in Studio.
     :width: 600

#. In the **Component Display Name** field, enter an identifying name for the
   component. In the LMS, this name appears as a heading above the exploration.

#. In the **Oppia Exploration ID** field, enter the identifier assigned to the
   exploration you want to add. For example, ``qG6kclSxlWZn`` or
   ``gC4_ggkWar-L``.

#. In the **Oppia Server URL** field, enter the host site of the exploration
   you want to add. For example, ``www.oppia.org``.

#. Select **Save**.

   Studio does not show the exploration on the unit page. To verify your work,
   select **Preview**, or publish the unit and then select **View Live**.

.. seealso::
 .. class::dropdown

 :ref:`Enable Additional Exercises and Tools` (how-to)

 :ref:`Oppia Exploration Tool` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
