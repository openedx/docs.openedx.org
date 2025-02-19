.. _Guide to Course About Page:

#########################################################   
Guide to Course About Page (Schedule & Details)
#########################################################

.. tags:: educator, reference

The course About page, sometimes called the course summary page, provides
information about your course to learners. Learners can see the About page
before they enroll in the course.

.. image:: /_images/educator_references/about_page.png
 :alt: A course About page, showing the course image, video, description, and
     additional information.
 :width: 600

You edit the contents of your course About page in Studio.

.. contents::
   :local:
   :depth: 2

.. _Course Pacing:

*************************
Course Pacing
*************************

When you create an Open edX course, you can set the schedule of the course,
including due dates for assignments or exams, or you can allow learners to work
at their own pace. Courses that follow a schedule that you set are known as
instructor- paced courses. Courses that offer suggested due dates for
assignment or exams based on the learner’s enrollment date and the expected
course duration are known as self-paced courses. These courses offer learners
flexibility to modify the assignment dates as needed.

An indicator for the pacing for your course appears on the **Course Outline**
page. By default, courses are instructor-paced.

.. image:: /_images/educator_references/Pacing_COIndicator.png
 :width: 600
 :alt: The Course Outline page with a call-out for the indicator that the
     course is instructor-paced.

.. note::
    You cannot change the course pacing after the course start date has passed.

========================================
Instructor-Paced and Self-Paced Courses
========================================

Instructor-paced courses progress at the pace that the course author sets. You
set release dates for content and due dates for assignments, and assignment due
dates are visible in the LMS. Learners cannot access course content before its
release date, and learners must complete assignments by their due dates.

In self-paced courses, learners can access all course materials when the
course begins, and assignment due dates follow a Personalized Learning Schedule (PLS)
by default. You do not have the option to set release dates for course content. Learners can
complete course material at any time before the course end date.

.. image:: /_images/educator_references/Pacing_SubSettingsWithCustomPacing.png
 :width: 500
 :alt: Side-by-side comparison of subsection settings for instructor-led and
     self-paced courses, showing release and due date options for the
     instructor-led course.

.. note:: If you set due dates for assignments or exams in an instructor-led
   course and later change the course to be self-paced, Studio stores the due
   dates that you previously set. If you change the course back to instructor-
   paced later, Studio restores the due dates.


.. _Personalized Learning Schedule:

========================================
Personalized Learning Schedule (PLS)
========================================

**Personalized Learning Schedule (PLS)** is a feature in self-paced courses that creates
a personalized schedule for learners by assigning suggested due dates to graded assignments.

A learner’s PLS is based on their enrollment date and can have two types of pacing:

* PLS’ **default pacing** automatically assigns due dates to graded subsections evenly throughout the course duration based on the total number of sections in the course.
* PLS’ **custom pacing** allows course authors to assign due dates to graded subsections manually throughout the course duration.

For example, if there are 4 sections, each of which has a graded assignment, in an 8-week course,
**default pacing** would assign due dates for every 2 weeks.

.. image:: /_images/educator_references/Pacing_DefaultPacing.png
 :width: 450
 :alt: Default Pacing Schedule for an 8-week course with 4 graded assignments.


**Custom pacing** allows for other relative due dates, such as setting an assignment to be due in
5 weeks instead of the 2 week interval.

.. image:: /_images/educator_references/Pacing_CustomPacing.png
 :width: 450
 :alt: Custom Pacing Schedule for an 8-week course with 4 graded assignments where 1 of which
     has a custom due date of 5 weeks.


Now, Personalized Learning Schedule can be adapted to have:

#. Default pacing
#. Custom pacing
#. A mix of default and custom pacing, where the user sets custom pacing to some, but not all, graded assignments in a course. The rest of the assignments that are not set have default pacing applied to them.

.. _Course Schedule:

****************************
Course Schedule
****************************

After you determine scheduling for your course run, you enter this
information in Studio before the course run begins. For more information,
see :ref:`Edit the Course About Page`.

.. _Guidelines for Start and End Dates:

========================================
Guidelines for Start and End Dates
========================================

The start and end dates you set for your course are important for prospective
and current learners. Current learners see your course start or end date on
their dashboards. You should consider your course dates carefully.

--------------------------------
Course Start Date and Time
--------------------------------

.. sidebar:: Course Schedule and Details

  Click the image to see where to set the course schedule.

    .. thumbnail:: /_images/Educators_course_schedule.png

The course start date and time specify when learners can access published
course content. By default, the course start date and time are set to
**01/01/2030** at **00:00 UTC** to ensure that your course does not start
before you intend it to.

The following guidelines can help you determine a course start date.

* Start on a Tuesday, Wednesday, or Thursday.
* Avoid major public holidays.
* Specify a month, day, and year. If you are unsure of the exact date, specify
  a day that is close to the estimated start date. For example, if your course
  will start near the end of March, specify March 31.
* Set the start time of your course early in the day, generally 00:00
  Coordinated Universal Time (UTC) or earlier. Learners often expect the course
  to be available on the start date in their own time zones and try to access
  course content during the day. If you do not specify a start time for your
  course, the course starts at 00:00 UTC.

Although learners cannot access any part of your course before the course
start date, course team members who are enrolled in the course and who have
the staff, admin, or beta tester role can see published content in the course
before the course start date. For information about testing your course
content before the course start date, see :ref:`About Course Beta Testing`.

.. note::
  You can set a different advertised start date for your course. You might do
  this if the exact start date is uncertain. For example, you could advertise
  the start date as "Coming Soon". For more information, see
  :ref:`Advertise a Different Start Date <Advertise a Different Start Date>`.

--------------------------------
Course End Date and Time
--------------------------------

The course end date and time specify when learners can no longer earn credit
toward certificates. Learners can continue to complete available coursework,
but cannot earn credit after the course ends. Learners who have earned
certificates can view the certificates soon after the course end date.

In self-paced courses, course teams can make certain course components
unavailable based on the course end date. For example, course teams can make a
final exam unavailable after the end date for a self-paced course. For more
details, see :ref:`Hide a Subsection After its Due Date <Hide a Subsection After its Due Date>`.

.. important::
  If you do not set a course end date, learners cannot access earned
  certificates.

--------------------------------
Enrollment Start Date and Time
--------------------------------

As soon as enrollment starts, prospective learners can see your course in the
course catalog, view the course **About** page, and enroll in the course.

The enrollment start date and time specify when learners can start to enroll
in the course. Ensure that the enrollment start date is early enough to allow
learners to both enroll in and prepare for the course. The enrollment start date and time must be before the course start date and time.

.. _Enrollment End Date and Time:

--------------------------------
Enrollment End Date and Time
--------------------------------

The enrollment end date and time specify when learners can no longer enroll
in the course. Ensure that the enrollment end date is late enough to allow
learners adequate time to enroll. The enrollment end date cannot be later
than the course end date.


.. _View Start and End Dates:

================================================
The Learner's View of Course Start and End Dates
================================================

When learners browse courses, the start date for each course is visible in the
course catalog and in the course's About page.

.. image:: /_images/educator_references/course_dates.png
 :alt: Course cards in the course catalog, showing each course's start date.
 :width: 800

.. image:: /_images/educator_references/about-page-course-start.png
 :alt: The course About page, showing the start date.
 :width: 800


To find the URL of your course's **About** page in Studio, select
**Settings**, and then select **Schedule & Details**.

After learners enroll in courses, the courses appear on their course
dashboards. To access the dashboard, learners select their usernames and then
select **Dashboard**. For a course that is in progress or has not yet started,
the start date is visible. For a course that has ended, the course end date is
visible.

.. image:: /_images/educator_references/dashboard-course-start-and-end.png
 :alt: The learner dashboard with a course in progress, one that has ended, one
  that is self-paced and can be started any time, and one that has not
  started.
 :width: 800

.. _Language Guidelines:

*******************
Language Guidelines
*******************

You are required to specify a language or languages for the following content.

* Course content, including text
* Video transcripts

Optionally, you can also specify additional languages for course videos.

.. _Course Description:

********************************
Course Description
********************************

Descriptive course information includes information such as the course short
and long descriptions, as well as information about what learners will learn,
the subject, and the difficulty level.

.. _Course Short Description Guidelines:

========================================
Course Short Description Guidelines
========================================

An effective short description follows these guidelines.

* Contains 25–50 words.
* Functions as a tagline.
* Conveys compelling reasons to take the course.
* Follows search engine optimization (SEO) guidelines.
* Targets a global audience.


--------------------------------
Example Short Description
--------------------------------

**Course Name:** The Science of Happiness 

**Course Description:** The first MOOC to teach positive psychology. Learn science-based principles and
practices for a happy, meaningful life.

.. _Course Long Description Guidelines:

========================================
Course Long Description Guidelines
========================================

Given the diversity of online learners, be sure to review your course
description to ensure that it clearly communicates the target audience, level,
and prerequisites for your course. Use concrete, unambiguous phrasing, such as
a prerequisite of "understand eigenvalue decomposition" rather than
"intermediate linear algebra".

An effective long description follows these guidelines.

* Contains 150–300 words.
* Is easy to skim.
* Uses bullet points instead of dense text paragraphs.
* Follows SEO guidelines.
* Targets a global audience.


--------------------------------
Example Long Descriptions
--------------------------------

The following long description is a content-based example.

  Want to learn computer programming, but unsure where to begin? This is the
  course for you! Scratch is the computer programming language that makes it
  easy and fun to create interactive stories, games and animations and share
  them online.

  This course is an introduction to computer science using the programming
  language Scratch, developed by MIT. Starting with the basics of using
  Scratch, the course will stretch your mind and challenge you. You will learn
  how to create amazing games, animated images and songs in just minutes with a
  simple “drag and drop” interface.

  No previous programming knowledge needed. Join us as you start your computer
  science journey.

The following long description is a skills-based example.

  Taught by instructors with decades of experience on Wall Street, this M&A
  course will equip analysts and associates with the skills they need to rise
  to employment in the M&A field. Additionally, directors and managers who have
  transitioned, or hope to transition, to M&A from other areas such as equities
  or fixed income can use this course to eliminate skill gaps.

.. _Learning Outcome Guidelines:

========================================
Learning Outcome Guidelines
========================================

It is good practice to include a list of learning outcomes describing the skills and knowledge
learners will acquire in the course in an itemized list. It is recommended that
you format each item as a short bullet item.


--------------------------------
Example Learning Outcomes
--------------------------------

* Write basic R scripts to manipulate and visualize data.
* Apply linear and logistic regression techniques to analyze real-world datasets and interpret the results.
* Apply text analytics techniques to extract insights from a given dataset and present their findings.
* Formulate and solve linear and integer optimization problems


.. _Course and Program Images and Videos:

************************************************
Images and Videos for a Course or Program
************************************************

The About page for a course or program includes both a representative image and
a short About video. The course or program image also appears in places such as
learner dashboards and search engine results.

For information about how to add your course title and number, see
:ref:`Creating a New Course <Create a New Course>`.

.. _Course and Program Image Guidelines:

========================================
Representative Image Guidelines
========================================

A representative image is an eye-catching, colorful image that captures the
essence of a course or program. These images are visible in the following
locations.


* The About page.
* The learner dashboard.
* Search engine results.

When you create a course or program image, keep the following guidelines in
mind.

* The image must not include text or headlines.
* You must have permission to use the image. Possible image sources include
  Flickr Creative Commons, Stock Vault, Stock XCHNG, and iStock Photo.
* Each course in a sequence or program must have a unique image.



.. _Image Size Guidelines:

--------------------------------
Image Size Guidelines
--------------------------------

Images must follow specific size guidelines.

--------------------------------
Course Image Size
--------------------------------

The course image that you add in Studio appears on the About page for the
course and on the learner dashboard. It must be a minimum of 378 pixels in
width by 225 pixels in height, and in .jpg or .png format. Make sure the
image that you upload maintains the aspect ratio of those dimensions so that
the image appears correctly on the dashboard.

.. _Course About Video Guidelines:

========================================
Course About Video Guidelines
========================================

.. tags:: educator, reference

The course About video should excite and entice potential learners to enroll,
and reveal some of the personality that the course team brings to the course.

This video should answer these key questions.

* Who is teaching the course?
* What university or institution is the course affiliated with?
* What topics and concepts are covered in your course?
* Why should a learner enroll in your course?

This video should deliver your message as concisely as possible and have a run
time of less than two minutes.

Before you upload a course About video, make sure that it follows the
same :ref:`video guidelines <Video Compression Specifications>`
as your course content videos.

.. note::

  * If you upload both a course image and a course About video, the course
    image appears on learner dashboards with a **play** icon superimposed on
    it. If you upload only a course video, the first frame of the video
    file appears with the **play** icon.

  * The process for adding a course about video is different than the process
    for including videos as part of the content of your course. For more
    information about including video content, see :ref:`Introduction to Video`.

For information about how to add an About video to your course About page, see
:ref:`Add an About Video <Add an About Video>`.

.. _Additional Course Information:

************************************************
Additional Course Information
************************************************

You can add these optional items to your course About page. For more
information, see :ref:`Edit the Course About Page`.

.. _Effort Guidelines:

========================================
Effort Guidelines
========================================

Effort indicates the number of hours each week you expect learners to work on
your course, rounded to the nearest whole number.


.. _Set Course Prerequisites:

========================================
Skill and Knowledge Prerequisites
========================================

You might want to make sure your learners have a specific set of skills
and knowledge before they take your course. This information appears on the
course About page.


Optionally, you can also require that learners complete a specific course
before they enroll in your course, or that learners complete an entrance exam
before they access course content. This information also appears on the About
page, but you specify these prerequisites on the **Schedule & Details** page
in Studio. For more information, see :ref:`Require a Prerequisite Course` and
:ref:`Require an Entrance Exam`.

You add skill and knowledge prerequisites in Studio. For more information,
see :ref:`Edit the Course About Page`.

------------------------------------------
Example Skill and Knowledge Prerequisites
------------------------------------------

* Secondary school (high school) algebra; basic mathematics concepts
* Graduate-level understanding of Keynesian economics
* Basic algebra
* Familiarity with eigenvalue decomposition

.. _Prerequisite Courses:

========================================
Prerequisite Courses
========================================

When you require your learners pass a particular course before they
enroll in your course, learners see information about course prerequisites on
the course **About** page.

.. image:: /_images/educator_references/PrereqAboutPage.png
  :width: 500
  :alt: A course About page with prerequisite course information circled.

If learners have not completed the prerequisite course, they can enroll in
your course and then see your course on their learner dashboards. However,
unlike with other courses, the dashboard does not provide a link to the
course content. The dashboard includes a link to the **About** page for the
prerequisite course. Learners can enroll in the prerequisite course from the
**About** page.

.. image:: /_images/educator_references/Prereq_StudentDashboard.png
  :width: 500
  :alt: The learner dashboard with an available course and a course that is
      unavailable because it has a prerequisite.

You enter this information in Studio. For more information, see :ref:`Require a Prerequisite Course`.

.. _Entrance Exam Prerequisite:

========================================
Entrance Exam
========================================

You can require your learners to pass an entrance exam before they access
your course materials. If you include an entrance exam, learners who enroll
in your course can access only the **Entrance Exam** page until they pass the
exam. After learners pass the exam, they can access all released materials in
your course.

You enter this information in Studio. For more information, see :ref:`Require
an Entrance Exam <Require an Entrance Exam>`.

---------------------------------
Best Practices for Entrance Exams
---------------------------------

We strongly recommend you follow several guidelines to help you and your
learners have a positive experience with entrance exams.

* Make sure your beta testers include the entrance exam when they test
  your other course content.

* Make sure you mention the entrance exam in the course description on
  your course **About** page. Otherwise, learners will not know about the
  entrance exam before they enroll in your course and try to access course
  content.

* Add an announcement to the **Course Updates & News** page that contains
  information and instructions for learners who need to take the exam. When
  learners first try to access content in a course that has an entrance exam,
  they see the **Course Updates & News** page. We suggest you include
  the following information.

  * To begin the course entrance exam, learners select **Entrance Exam**.

  * After learners complete the entrance exam, they must select **Entrance
    Exam** again or refresh the page in their browsers. After the page
    refreshes, learners can access all currently available course content.

.. _Syllabus Guidelines:

========================================
Syllabus Guidelines
========================================

A syllabus is a review of content covered in your course, organized by week or
module. To create an effective syllabus, keep the following guidelines in mind.

* Focus on topics and content.
* Do not include detailed information about course logistics, such as grading,
  communication policies, and reading lists.
* Format items as either paragraphs or a bulleted list.


You can add the syllabus to your course About page. For more information, see
:ref:`Edit the Course About Page`.

You can also add a syllabus to your course in Studio by creating a custom page
or a handout. For more information, see :ref:`Add Page <Adding Pages to a Course>` and :ref:`Add Course
Handouts <Add Course Handouts>`.

--------------------------------
Example Syllabus
--------------------------------

**Week 1: From Calculator to Computer**

Introduction to basic programming concepts, such as values and expressions, as
well as making decisions when implementing algorithms and developing programs.

**Week 2: State Transformation**

Introduction to state transformation, including representation of data and
programs as well as conditional repetition.

.. _FAQ Guidelines:

========================================
FAQ Guidelines
========================================

To help prospective learners, you can add any frequently asked questions (FAQ)
and the answers to those questions to your About page.


You can add the FAQ to your course About page. For more information, see
:ref:`Edit the Course About Page`.

--------------------------------
Example FAQ
--------------------------------

**Q: Is the textbook required?**

A: No, the textbook is not required. However, you will find that it more
completely explains some of the concepts that we cover quickly in the course,
and will add depth to your understanding.

**Q: How much is the final exam worth?**

A: The final exam is worth 30% of the total grade. You can find more
information about the value of each assignment on your **Progress** page.

.. _Learner Testimonial Guidelines:

========================================
Learner Testimonial Guidelines
========================================

A learner testimonial is a quote from a learner in the course, demonstrating
the value of taking the course.

To be effective, a testimonial should contain no more than 25-50 words.


You can add the learner testimonial to your course About page. For more
information, see :ref:`Edit the Course About Page`.



.. _Course Metadata:

========================================
Course Metadata
========================================

You may need to be able to make certain custom information about your course
available to entities such as customer relationship management (CRM)
software, a marketing site, or other external systems. This information is
not visible to learners.

For example, you might want to make the following information available.

* The course difficulty
* The course ID in an external system
* Course prerequisites

You add this information as a JSON dictionary in Studio. For more
information, see :ref:`Add Course Metadata <Add Course Metadata>`.

.. seealso::

  :ref:`Guide to Basic Course Details` (reference)

  :ref:`Edit Basic Course Details` (how-to)

  :ref:`Edit the Course About Page` (how-to)

  :ref:`Set Course Pacing` (how-to)

  :ref:`Set Course Schedule` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+