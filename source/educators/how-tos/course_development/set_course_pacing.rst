.. _Set Course Pacing: 

###########################
Set Course Pacing
###########################

.. tags:: educator, how-to

.. sidebar:: Course Schedule and Details

  Click the image to see where to set the course pacing.

    .. thumbnail:: /_images/Educators_course_pacing.png


You can set a schedule for your course, including when content is released and due dates for assignments. You can allow learners to work at their own pace, as long as they complete the course within the course run time period.

************************
Instructor-Paced Courses
************************

Courses that follow a schedule that you set are known as instructor-paced courses. Select :guilabel:`Instructor-Paced` in the Course Schedule and Details screen.

******************
Self-Paced Courses
******************

Courses that allow learners to work at their own pace, as long as they are finished by the time the course ends, are known as self-paced courses. These courses offer learners flexibility to modify the assignment dates as needed. Select :guilabel:`Self-Paced` in the Course Schedule and Details screen.

************************************
Set Course Pacing in Studio
************************************

Before you can use this feature to set up a self-paced course, it must be
enabled using the Open edX Django admin panel. Follow these steps, or
contact your Open edX site administrator for assistance.

   #. Log in to your Open edX Django Admin panel.
   #. In the **Self_Paced** section, locate **Self paced configurations**, and
       then select **Add**.
   #. Select the **Enabled** and **Enable course home page improvements**
       checkboxes.
   #. Select **Save**.

To set the pacing for your course, follow these steps.

.. note::
 You cannot change the course pacing after the course start date has passed.

#. On the **Settings** menu, select **Schedule & Details**.
#. Scroll down to the **Course Pacing** section.
#. Under **Course Pacing**, select either **Instructor-Paced** or
   **Self-Paced**.
#. Select **Save Changes**.

********************************************************
Set Custom Pacing in Personalized Learning Schedules
********************************************************

For more information about Personalized Learning Schedules, see :ref:`Personalized Learning Schedule`.

Once you have created a graded assignment in your self-paced course, the assignment is eligible to be included in
a learner’s Personalized Learning Schedule (PLS), and it will automatically inherit default pacing.
Follow these steps to override the course’s default pacing, and enable custom pacing:

1. Click on the subsection’s configuration setting

.. image:: /_images/educator_references/Pacing_StepOne.png
    :width: 500
    :alt: Subsection in the course outlines.

2. Type the number of weeks you would like the assignment to be due in starting from the learner’s enrollment date.
   (Note: Leaving this field empty will cause the assignment to inherit default pacing)

.. image:: /_images/educator_references/Pacing_StepTwo.png
    :width: 500
    :alt: Subsection's configuration modal with grading type options.

3. Click “Save”

The relative due date you saved will now be published for all enrolled learners.

.. seealso::

  :ref:`Guide to Basic Course Details` (reference)

  :ref:`Edit Basic Course Details` (how-to)

  :ref:`Guide to Course About Page` (reference)

  :ref:`Edit the Course About Page` (how-to)

  :ref:`Set Course Schedule` (how-to)



**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
