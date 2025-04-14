.. _Create a Duplicate Course for LTI use:

Create a Duplicate Course for LTI use
######################################

.. tags:: educator, how-to

.. warning:: This feature was a closed pilot experiment. This feature is poorly documented and may not work properly.

Before you create a duplicate course, be sure to check with your DevOps team
to determine the website that hosts your organization's courses for LTI use.

To create the duplicate course, follow these steps.

#. In Studio, export the original course. For more information, see
   :ref:`Export a Course`.

#. In Studio on your organization's host site for LTI courses, create a course.
   This is the duplicate course.

   .. note:: If your organization uses the same site as the host for both the
    original course and for LTI courses, be sure to give the duplicate course a
    different name or run.

#. In the duplicate course, import the tar.gz file you exported in step 1.
   For more information, see :ref:`Import a Course`.

.. future: add re-run as an option for sites that host courses for LTI on the same instance (edit from Mark, Phil says re-run should work). - Alison 1 Sep 2015


Verify Content Status
*******************************

Only the published course content from your Open edX instance appears in an external LMS.

.. note:: The **Hide from students** setting for sections, subsections,
 and units does not affect the visibility of content in an external LMS. Only
 the publication status of a unit can prevent content from being included.

To verify that all of the content in your course is published, follow these
steps.

#. In Studio, from the **Content** menu select **Outline**. The **Course
   Outline** page opens.

#. Expand each section and subsection.

#. Locate units with *Unpublished units will not be released* or *Unpublished
   changes to live content* below the unit name.

#. For each unpublished unit, make any changes that are necessary to prepare
   the content for publication. Alternatively, delete the unit.

#. Publish the unit. For more information, see :ref:`Publish a Unit`.

.. seealso::
 

 :ref:`Using Open edX as an LTI Tool Provider` (concept)

 :ref:`Determine Content Addresses when using Open edX as an LTI Provider<Determine Content Addresses>` (how-to)

 :ref:`Planning for Content Reuse (LTI)<Planning for Content Reuse>` (reference)

 :ref:`Open edX as an LTI Provider to Canvas` (how-to)

 :ref:`Open edX as an LTI Provider to Blackboard` (how-to)




**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
