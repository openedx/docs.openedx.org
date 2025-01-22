.. _SCORM XBlock:

SCORM
######

.. tags:: educator, how-to

This section describes how to include `SCORM <https://en.wikipedia.org/wiki/Sharable_Content_Object_Reference_Model>`_ content in your course.

Enable the SCORM XBlock
***********************

Before you can add SCORM content to your course, you must enable the SCORM XBlock.

To enable the SCORM XBlock in Studio, you add the ``"scorm"`` key to
the **Advanced Module List** on the **Advanced Settings** page. (Be sure to
include the quotation marks around the key value.) For more information, see
:ref:`Enable Additional Exercises and Tools`.

.. image:: /_images/educator_how_tos/AdvancedModuleListScorm.png
  :alt: Advanced Module List with "scorm" added.

Adding a SCORM component to a Unit
**********************************

#. In a unit where you want the SCORM content to display, click on the ``Advanced`` Icon.


  .. image:: /_images/educator_how_tos/AddNewAdvancedComponent.png
    :alt: Add New Advanced Component



#. Select ``Scorm module``


  .. image:: /_images/educator_how_tos/AddScormModule.png
    :alt: Select Scorm module


#. ``Scorm module`` selected

  .. image:: /_images/educator_how_tos/AddScormModuleSelected.png
    :alt: Selected Scorm module


#. The SCORM module component will be added. Click on the **EDIT** button.


  .. image:: /_images/educator_how_tos/ScormBlockStudio.png
    :alt: New SCORM Component in Studio



Uploading the SCORM content
***************************

.. image:: /_images/educator_how_tos/ScormStudioSettings.png
    :alt: Scorm Component settings in Studio



#. Choose the SCORM .zip package you want to upload.
#. If the SCORM content does not have any quizzes, set “Scored” to False.
#. If the "Scored" parameter is True, you must specify the weight of the quizzes' points.


.. note:: * Only 1 SCORM component per Unit may be used.
          * The SCORM component will be displayed under the **Unit** title in the LMS.
          * The **Display Name** is only used within Studio.


.. seealso::
 :class: dropdown

 :ref:`SCORM Overview` (reference)


