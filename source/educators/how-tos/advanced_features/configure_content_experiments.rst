.. _Configure Your Course for Content Experiments:

Configure Your Course for Content Experiments
#############################################

.. tags:: educator, how-to

This how-to provides instructions for configuring your course to enable
:ref:`content experiments<Overview of Content Experiments>`. 

To enable content experiments in your course, you must add ``split_test`` to the
**Advanced Module List** in Advanced Settings. To do it, follow the next steps:

.. note:: ``split_test`` is the internal name for a content experiment.

.. _Enable Content Experiments:

*********************************
Enable Content Experiments
*********************************

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



.. seealso::
 

 :ref:`Offering Differentiated Content` (concept)

 :ref:`Overview of Content Experiments` (concept)

 :ref:`Experiment Group Configurations` (reference)

 :ref:`Guidelines for Modifying Group Configurations` (concept)

 :ref:`Create a Group Configuration` (how-to)

 :ref:`Edit a Group Configuration` (how-to)

 :ref:`Delete a Group Configuration` (how to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2024/12      | Documentation WG - Ana Gomez  |Redwood         |Pass.                           |
+--------------+-------------------------------+----------------+--------------------------------+
