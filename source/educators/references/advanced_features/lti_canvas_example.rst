.. _edX as an LTI Provider to Canvas:

##########################################
Example: edX as an LTI Provider to Canvas
##########################################

.. tags:: educator, reference

.. note:: This feature was a closed pilot experiment. This feature is not
 supported for new users.

To use edX course content in the Canvas LMS, you add a new app to the course and then add external tool module items.

.. note:: This example relies on the use of a third-party tool. Because this
  tool is subject to change by its owner, the steps and illustrations provided
  here are intended as guidelines and not as exact procedures.

#. In Canvas, select your course. In **Settings**, select **Add New App**.

   .. image:: /_images/educator_references/lti_edit_external_app_Canvas.png
     :alt: The Canvas page where you enter identifying values for the edX host
         site as a LTI tool provider.

#. In **Modules**, add a new **External Tool** item. The **URL** is the LTI
   URL that you determined for the edX course content, such as
   ``https://edx-lti.org/lti_provider/courses/course-v1:edX+DemoX+2014/block-v1:edX+DemoX+Demo_Course+type@problem+block@d2e35c1d294b4ba0b3b1048615605d2a``.

   .. image:: /_images/educator_references/lti_edit_problem_Canvas.png
     :alt: The Canvas page where you add an external tool and supply the LTI
         URL.

   For more information, see :ref:`Determining Content Addresses`.

#. Review the content to verify that it appears as you expect.

   .. image:: /_images/educator_references/lti_canvas_example2.png
     :alt: An edX drag and drop problem shown as part of a course running on a
      Canvas system.

.. seealso::
 :class: dropdown

 :ref:`Using Open edX as an LTI Tool Provider` (concept)

 :ref:`Create a Duplicate Course for LTI use` (how-to)

 :ref:`Determine Content Addresses when using Open edX as an LTI Provider<Determine Content Addresses>` (how-to)

 :ref:`Planning for Content Reuse (LTI)<Planning for Content Reuse>` (reference)

 :ref:`Example: edX as an LTI Provider to Blackboard<edX as an LTI Provider to Blackboard>` (reference)