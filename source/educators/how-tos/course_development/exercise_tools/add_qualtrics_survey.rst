.. :diataxis-type: how to
.. _Qualtrics Survey:

#########################
Qualtrics Survey Tool
#########################

You can administer Qualtrics surveys to your learners in your edX course. The
Qualtrics survey appears in an iframe inside the course.

.. image:: /_images/educator_how_tos/Qualtrics.png
  :width: 500
  :alt: A Qualtrics survey with several responses filled in.

Course staff can view the overall results of the survey as well as responses
from individual learners.

.. note:: To use a Qualtrics survey, you must have a Qualtrics license.
 Qualtrics licenses are available for a fee at the `Qualtrics website
 <http://www.qualtrics.com>`_. If you want to include a survey but you do not
 have a Qualtrics license, you can use the :ref:`edX survey tool<Survey Tool>`
 or a :ref:`Google form<Google Drive Files Tool>`.

For more information, see the following sections.

.. contents::
  :local:
  :depth: 1

Be sure to review all supplemental materials to make sure that they are
accessible before making them available through your course. For more
information, see
:ref:`Accessibility Best Practices for Course Content Development`.

*************************************
Add a Qualtrics Survey to Your Course
*************************************

To add a Qualtrics survey to your course, you must :ref:`create the survey in
Qualtrics <Create the Qualtrics Survey>`, and then :ref:`create a Text
component in Studio <Create the Text Component in Studio>`.

.. _Create the Qualtrics Survey:

==============================
Create the Qualtrics Survey
==============================

.. note:: Because Qualtrics is a third-party tool, the following steps might
 change without notice. See the `Qualtrics website
 <http://www.qualtrics.com>`_ for the most up-to-date Qualtrics documentation.

#. Using your Qualtrics account, create your survey.
#. Add the statements and options that you want the survey to include.
#. Add the **user ID** element. This element imports data from your course
   into Qualtrics.

   #. At the top of the page, make sure the **Edit Survey** tab is selected,
      and then select **Survey Flow**.
   #. In the upper left corner, select **Add a New Element Here**.
   #. Select **Embedded Data**.
   #. Under **Set Embedded Data**, replace **Enter Embedded Data Field Name
      Here** with ``uid``.
   #. Select **Save Flow**.

#. At the top of the page, make sure **Edit Survey** is selected, and then
   select **Launch Survey**.
#. On the page that opens, select **Activate Survey** in the upper right
   corner.
#. On the page that opens, locate the URL that is listed under **Your
   Anonymous Survey Link**. You will add this URL to the Text component for
   your survey in Studio.

   .. note:: If you need to find this URL in the future, open your survey
    in Qualtrics, and then select the **Distribute Survey** tab at the top of
    the page.

.. _Create the Text Component in Studio:

=====================================
Create the Text Component in Studio
=====================================

#. Open the unit where you want the survey to appear.
#. Under **Add New Component**, select **Text**, and then select **IFrame
   Tool**.
#. Select **Edit** to open the component editor, and then select **HTML** in
   the menu bar.
#. At the end of the instructions, locate the example iframe element, and
   replace the placeholder values with the values for your survey. The iframe
   element starts with the following text.

   ``<iframe title="Euler Line Demo"``

  * In the ``title`` attribute, replace ``Euler Line Demo`` with the title of
    your survey.
  * In the ``src`` attribute, replace the placeholder URL with the URL from
    step 6 in :ref:`Create the Qualtrics Survey`.
  * In the ``src`` attribute, add the following value to the end of the URL.

    ``?uid=%%USER_ID%%``

    The resulting ``src`` attribute resembles the following example.

    ``src="https://qtrial2015az1.az1.qualtrics.com/SE/?SID=SV_9N27VuruRdNcpHT?uid=%%USER_ID%%"``

  * Replace the values in the ``width`` and ``height`` attributes with values
    that allow your survey to appear the way you want it to. For example, you
    might change ``width`` to 800 and ``height`` to 1000.
  * (Optional) If your survey might be taller than the value that you set for
    ``height``, in the ``scrolling`` attribute, change the value to ``yes``.
    If you do not change the value to ``yes`` and your survey is taller than
    the ``height`` value, learners cannot scroll down to respond to all the
    survey statements.
  * Leave the other default values, and then select **OK** at the bottom
    of the HTML source code editor to return to the component editor.

#. In the component editor, delete all of the default instructional text, or
   replace it with introductory text for your Qualtrics survey.
#. Select **Save**.

.. seealso::
 :class: dropdown

 :ref:`View Qualtrics Responses` (reference)