.. _Course Overview:

#################################
Create Course Overview in OLX
#################################

.. tags:: educator, how-to

.. note::

  This page describes how to create the Course Overview section for
  a course, provided the Open edX instance the course is hosted on is using the default
  Open edX course catalog. Some Open edX instances might utilize a different
  way of publishing and advertising courses.

Each course must have an overview page. Learners see the overview page when
searching and registering for the course.

*********************************************
Create the Overview File
*********************************************

In the ``about`` directory, create an HTML file called
``overview.html``.

*********************************************
Overview Sections
*********************************************

The ``overview.html`` contains specific sections. The default Open edX course
catalog does not style the Overview page based on most of these HTML classes,
however, other course catalogs may (and Open edX Studio will export with these
classes).

Each section is wrapped in ``section`` tags. The value of the ``class``
attribute specifies what the section is for and how it is displayed to
learners. Within the ``section`` tags, use valid HTML.

The overview may contain section(s) with the following names.

* ``about``
* ``prerequisites``
* ``course-staff``
* ``teacher``
* ``faq``


.. _A Template For Course Overview:

************************************************
A Template For A Course Overview
************************************************

Replace the placeholders in the following template with relevant course information.

.. code-block:: html

  <section class="about">
    <h2>About This Course</h2>
    <p>Include your long course description here. The long course description
      should contain 150-400 words.</p>
    <p>This is paragraph 2 of the long course description. Add more paragraphs
      as needed. Make sure to enclose them in paragraph tags.</p>
  <section>
  <section class="prerequisites">
    <h2>Prerequisites</h2>
    <p>Add information about class prerequisites here.</p>
  </section>
  <section class="course-staff">
    <h2>Course Team</h2>
    <article class="teacher">
      <div class="teacher-image">
        <!-- Replace the path below with the path to your faculty image. -->
        <img src="/c4x/edX/edX101/asset/Placeholder_FacultyImage.jpg"
          align="left" style="margin:0 20 px 0"/>
      </div>
      <h3>Team Member</h3>
      <p>Biography of course team member</p>
    </article>
    <article class="teacher">
      <div class="teacher-image">
        <img src="/c4x/edX/edX101/asset/Placeholder_FalcutyImage.jpg"/>
      </div>
      <h3>Team Member Name</h3>
      <p>Biography of course team member</p>
    </article>
  </section>
  <section class="faq">
    <section class="responses">
      <h2>Frequently Asked Questions</h2>
      <article class="response">
        <h3>What web browser should I use?</h3>
        <p>The Open edX platform works best with the current versions of Chrome, Firefox, Safari, and Microsoft Edge.</p>
        <p>See our :ref:`list of supported browsers<Browsers>` for the most up-to-date information.</p>
      </article>
      <article class="response">
        <h3>Question 2?</h3>
        <p>Answer 2.</p>
      </article>
    </section>
  </section>

.. seealso::

  :ref:`What is Open Learning XML?` (concept)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
