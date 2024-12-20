.. _Adding Pages to a Course:

##################################
Managing the Pages in Your Course
##################################

.. tags:: educator, how-to

This topic describes the applications and resources that your course experience
has enabled outside of the core content experience and how you can modify these
tools to fit your course needs.


.. contents::
  :local:
  :depth: 2

.. _Default Pages:

*******************************
Working with the Default Pages
*******************************

By default, every new course has the following key areas enabled:

* Course
* Progress
* Date
* Discussion


In the learner experience, these will be shown in the primary navigation bar at the top of every page,
consistently in this order for all courses.

.. image:: /_images/educator_how_tos/page_bar_lms_orig.png
 :alt: The navigation bar in the LMS, showing the default pages.

As a course team member with the **Staff** or **Admin** role, you also see the Instructor
option in the navigation bar, shown at the end of the list of pages.
Learners do not see the Instructor option.

    .. note::
        The progress page can be disabled and thus hidden from the learner experience,
        though this is not commonly done and is not recommended. The information on
        the Progress page is critical for motivating learners, particularly in courses
        that include graded subsections, but also for courses that include only ungraded
        exercises. Before choosing to hide the Progress page for your course, consider
        the possible effect on learner engagement.

.. _Enable Additional Resource:

********************************************
Enabling Additional Applications & Resources
********************************************

Additional applications and resources can be enabled depending on your course needs, including:

* Notes
* Teams
* Wiki
* Calculator
* Textbooks
* Custom Pages

.. _Enable Notes:

==============================
Enabling the Notes Application
==============================

The notes application can be optionally enabled to allow learners to easily create organized
text notes for any text, problem, or video transcript content within a course. These notes are
then centrally stored for review in the Notes area of the course

To disable or enable the Notes application, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.

#. Click the gear icon on the **Notes** card shown on this page.

#. From the **Configure notes** modal, select the toggle to enable or disable the notes application.

#. Select **Apply** to save your configuration changes.

.. _Enable Teams:

==============================
Enabling the Teams Application
==============================

When you create a course, the teams application can be optionally enabled to provide a
mechanism for instructor and learner-driven team formation or assignment.

To disable or enable the Teams application, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.

#. Click the gear icon on the **Teams** card shown on this page.

#. From the **Configure teams** modal, select the toggle to enable or disable the teams application.

#. Select **Apply** to save your configuration changes.

Additional configuration for the Teams application can be found at :ref:`11.3.3.3 Configuring the Teams application<Teams Configuration>`


.. _Enable Wiki:

=============================
Enabling the Wiki Application
=============================

When you create a course, a wiki can be optionally enabled to create and share resources that can be edited and updated by any course team member or learner.

To disable or enable the Wiki application, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.

#. Click the gear icon on the **Wiki** card shown on this page.

#. From the **Configure Wiki** modal, select the toggle to enable or disable the wiki.

#. Select **Apply** to save your configuration changes.

When you disable the wiki application in your course, any existing articles remain in the edX- wide wiki, but the Wiki page is removed from your course pages.

Additional details for configuring the wiki application can be found at :ref:`11.3.3.2 Configuring the wiki application<Wiki Configuration>`.

.. _Enable Calculator:

================================
Enabling the Calculator Resource
================================
Courses can optionally render a calculator resource that helps learners use an in-platform
tool for mathematical operations and computations.

To disable or enable the Calculator resource, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.

#. Click the gear icon on the **Calculator** card shown on this page.

#. From the **Configure calculator** modal, select the toggle to enable or disable the calculator.

#. Select **Apply** to save your configuration changes.

.. _Add Page:

.. _Add Custom Page:

============================
Adding Custom Page Resources
============================

You can customize your course by adding pages. Each page that you add appears in the navigation
bar for your course. When you add a page, you also add its content using an HTML editor.
The following example shows the navigation bar for a course that has added a custom page named Syllabus.

    .. image:: /_images/educator_how_tos/lms_navigation_bar.png
     :width: 500
     :alt: The navigation bar in the LMS, showing a custom page named Syllabus.

When you add a page, you can specify whether it and its content are visible only to course team
members who have the Admin or Staff role, or to all enrolled learners as well as the course team.
For more information about assigning course team roles, see :ref:`Course_Staffing`.

If you add a custom page to a course after its start date, and have specified that the page should
be visible to learners, the page is visible in the LMS as soon as you save your work.

As a best practice, be sure the following aspects of your page design are ready before you add a page
in Studio.

* The content for the page, which can include HTML markup.
* The name of the page.
* The audience for the page (everyone, or course team members with the Admin or Staff roles only).

To add a custom page and its content to your course, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.
#. Select the **Custom Pages** card on this page.
#. Click **New Page**, which prompts the system to add a page named **Empty** to the end of the list.
#. In the row for the new page, select **Edit**. The :ref:`visual editor<The Visual Editor>` opens.
#. Enter the content for your page.

    To add HTML tags to your content, select HTML to open the :ref:`the raw HTML editor<The Raw HTML Editor>`.
    For more information about entering content, see :ref:`Options for Editing Text Components`.

    .. note:: If you copy text from another source and paste it into the visual editor,be sure to proofread the result carefully. Some applications automatically change quotation marks and apostrophes from the “straight” version to the “smart” or “curly” version. The raw HTML editor requires “straight” quotation marks and apostrophes.

#. To rename the page, select Settings, and then enter a Display Name. The display name is the label that course participants use in the course navigation bar.
#. To hide the page from learners, select **Settings**, and then select true for **Hide Page from Learners**. By default, pages are visible to learners.
#. Select **Save**.

The new page is immediately available to the specified audience if the course has started.

For details on reordering course pages, see additional detail in :ref:`11.3.4. Reordering and Deleting Custom Pages<Reordering and deleting custom pages>`.

.. _Enable Textbook:

================================
Enabling the Textbooks Resources
================================

You can add textbooks in PDF format to your course using the Textbooks resource area. Each textbook that
you add is displayed to learners as a page, or tab, in the course navigation bar.

 .. note:: Do not use image files (for example, .png files) as textbooks for your course, because they are not accessible to learners who use screen readers. For more information, review :ref:`Creating Accessible PDFs`.

To add a textbook resource to your course, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.
#. Select the **Textbooks** card on this page.
#. Select either **Add your first textbook** or **New Textbook**.
#. On the page that opens, enter the **Textbook Name**.
#. Enter the **Chapter Name**.
#. Next to **Chapter Asset**, select **Upload PDF** to upload a PDF from your computer, and then follow the prompts to upload your file.
#. To add more chapters, select **Add a Chapter** and repeat steps 5 and 6.
#. Select **Save**.

 .. note:: When you add a textbook to your course, Studio automatically adds each PDF file that you upload to the Files & Uploads page. EdX recommends that you upload a separate PDF for each chapter of your textbook. When learners open the textbook page in the course, they can navigate the textbook by chapter.

You can delete a custom textbook from your course using the delete icon shown on each textbook from the Textbooks
Studio page. It is also possible to delete a specific chapter from a textbook when editing a textbook using
the close icon to the right of each listed chapter.

 .. note:: After you delete your textbook on the Textbooks page, edX strongly recommends that you :ref:`lock <Lock a File>` or :ref:`delete <Delete a File>` the PDF files for the textbook on the Files & Uploads page to avoid copyright issues.


.. _Reordering and deleting custom pages:

************************************
Reordering and Deleting Custom Pages
************************************

For instructions on how to add custom pages see :ref:`11.3.2.5 Adding Custom Page Resources<Add Custom Page>`.

You can reorder the custom pages in your course in the same way that you :ref:`reorganize the course outline<Reorganize the Course Outline>`:
you drag a page to a different location in the list of pages and drop it there.

.. note:: All default course pages (Course, Progress, Dates, Discussion) and optional course applications (Notes, Teams, Wiki) appear in the navigation before any configured custom page resources. If you have configured any textbook resources, these are listed after custom pages.

To reorder the pages, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.
#. Select the **Custom Pages** card on this page.
#. On the list of pages, each page that you can move includes a Drag to reorder icon.
#. Move your pointer over the Drag to reorder icon for the page. Your pointer changes to a four-headed arrow.
#. Click and drag the page to the new location, and then release.

You can also delete a custom page from your course using the delete icon shown on each custom page from the **Custom Pages** Studio page.
If you delete a page after the course start date, note that the visibility of the page in the learner experience changes immediately.

.. seealso::
 :class: dropdown

 :ref:`Configure Resources` (how to)

 :ref:`Adding Textbooks` (how to)
