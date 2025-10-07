.. _Set up an LTI Consumer with Reusable LTI Configuration:


Set up an LTI Consumer with Reusable LTI Configuration
######################################################

.. tags:: educator, how-to


Overview
********

Reusable LTI configurations are created once by an administrator in Django Admin (LTI Store) and identified by a filter key.  
In Studio, you can point an LTI Consumer component to that reusable configuration, avoiding repeated copy/paste of credentials.


Before you start
****************

* An administrator has created a reusable LTI 1.3 configuration in Django Admin.  
* You have the reusable configuration’s filter key. It may be shared as a value like ``lti_store:reference_tool``  
* You have edit access to the course in Studio.

.. note::
   The following steps correspond to an **LTI 1.3 configuration**.


Add the LTI Consumer component
******************************

#. Open your course in Studio.  
#. Navigate to the unit where you want to add the tool.  
#. Add Component → Advanced → LTI Consumer.

.. image:: /_images/educator_how_tos/add_lti_component.png
   :alt: 'Add advanced component' dialog box displaying the LTI component as selected

Configure the LTI Consumer to use the reusable configuration
************************************************************

#. Open the component’s settings (Edit).  
#. Set **Configuration type** to *Reusable configuration*.  
#. Set **LTI version** to *LTI 1.3*.  
#. Set **Reusable configuration ID**:  

   * Enter the filter key for the reusable configuration, typically the slug value prefixed as shown in your instance (for example, ``lti_store:reference_tool``).  

#. (Optional) Update the **Display name** and any course-facing settings as needed.  
#. Save.

.. image:: /_images/educator_how_tos/edit_lti_component.png
   :alt: LTI component in editing mode, displaying the fields to be edited

Publish and test
****************

* Publish the unit.  
* In the LMS, open the unit and launch the LTI tool to verify it loads as expected.


What changes compared to on-block configuration
***********************************************

* No tool credentials are entered on the block.  
* Updates to the centralized configuration in Django Admin apply to all blocks that reference it.


.. seealso::

 :ref:`Set up a Reusable LTI Store` (how-to)

 :ref:`LTI Component Settings` (reference)

 :ref:`Set up an LTI 1_3 component` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        | Release        | Test situation                 |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               | Ulmo           | Draft                          |
+--------------+-------------------------------+----------------+--------------------------------+
