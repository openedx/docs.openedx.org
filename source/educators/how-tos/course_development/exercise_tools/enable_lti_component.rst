.. _enable_lti_components:

Find the LTI Consumer Component
################################

.. tags:: educator, how-to

Use the *LTI Consumer* component to add an external LTI tool to a course unit.

#. In Studio, open the course unit where you want to add the external tool.
#. In the *Add New Component* area, select *Advanced*.
#. Select *LTI Consumer*.

.. note::

   For Teak and later releases, the *LTI Consumer* component is visible by
   default. If you do not see *LTI Consumer* in Studio, you can enable it by
   adding ``"lti_consumer"`` to the *Advanced Module List* on the *Advanced
   Settings* page. If the list already includes other tools, separate each value
   with a comma.


.. note::

   If both *LTI Consumer* and the older *LTI* XBlocks appear in Studio, select
   *LTI Consumer*.

   *LTI Consumer* XBlock includes all the functionality of the *LTI* XBlock and
   it supports `LTI 1.3`_ and `LTI Advantage`_. Some courses may already contain
   the *LTI* XBlock in their content. They will continue to work, but use
   *LTI Consumer* for new LTI integrations.


.. seealso::
 
 :ref:`About the LTI Component` (concept)

 :ref:`Set up an LTI 1_1 component` (how-to)

 :ref:`Set up an LTI 1_3 component` (how-to)

 :ref:`Set up an LTI Consumer with Reusable LTI Configuration` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)

 :ref:`LTI Component Settings` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-03-19   |   Documentation WG            |     Sumac      |      Pass                      |
+--------------+-------------------------------+----------------+--------------------------------+
