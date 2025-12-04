.. _DemoX Quince:

Introducing the New DemoX Course (Quince)
#########################################

In 2013, just as the Open edX® platform was starting to take off, the “edX
Demonstration Course”, or DemoX, was created and bundled with each new Open edX®
installation. To many, this is a familiar thumbnail on a fresh new installation
of Open edX®:

   .. image:: /_images/release_notes/quince/demox_post_1.png

In the 10 years since the original DemoX, the Open edX® platform and the online
education landscape overall have evolved significantly.

* The number of people taking courses online has increased dramatically.
* Conservatively, the number of learners reached by MOOCs increased by 73,000%
  from 2011 to 2021 [`source <https://www.edsurge.com/news/2021-12-28-a-decade-of-moocs-a-review-of-stats-and-trends-for-large-scale-online-courses-in-2021>`_]
* The Open edX platform has evolved from a mainly MOOC platform to one that
  supports blended learning, fully online degrees, micro-credentials, and more.
* The tools and approaches used to build courses have evolved and expanded.
* The Open edX project has spun out of edX.org and is now supported by a
  community of largely volunteers.

In short, by 2023, the original DemoX was already long overdue for a
re-imagining. A new course needed to inspire the newer generation of Open edX
users. It needed to demonstrate practical, reusable examples of what can now be
done in an Open edX course. And so DemoX v2 was born:

.. youtube:: lVPPPpyUOR4

The new DemoX course is available now. There are five modules that advance from
general to specific knowledge and provide reusable blocks that you can repurpose
for your own courses. 

Module 1: Dive into the Open edX Platform
*****************************************

A general overview of the purpose and structure of the Open edX® platform.

   .. image:: /_images/release_notes/quince/demox_post_2.png


Module 2: Crafting Captivating Content
**************************************

Demos and best practices for crafting fundamental learning content (text,
images, video) as well as tools like Libraries, conditionals, and custom
styling.

   .. image:: /_images/release_notes/quince/demox_post_3.png

Module 3: Ace the Assessments
*****************************

An overview and re-usable practical example for many of the assessment tools
offered by the Open edX platform:

   .. image:: /_images/release_notes/quince/demox_post_4.png

Module 4: Social Learning: Engaging through Interaction
*******************************************************

An updated overview of how to incorporate the Open edX platform's social tools
like discussions, polls, surveys, teams, and cohorts into your course.

   .. image:: /_images/release_notes/quince/demox_post_5.png

Module 5: Your Open edX Community
*********************************

A brand new module about how to find support and get involved in the Open edX
community.

   .. image:: /_images/release_notes/quince/demox_post_6.png


Using the New DemoX Course
**************************

If you'd like to start using the Open edX DemoX course on your instance, getting
started is easy. If you are running a Tutor-based installation version ``quince.2``
or higher, you can run the following commands to import both the course and the
demo library:: 

   $ tutor local importdemocourse --version master
   $ tutor local do importdemolibraries --version master admin

If you are on a different version, or would prefer to install it manually, then
you can follow the instructions in the `DemoX github repository`_ to import the
library and course ``.tar.gz`` files into your instance. 

The course content is released under the `Creative Commons BY-NC-SA 3.0 US
License`_, so you are free to re-use as you like for your own organization as
long as you follow the terms of the license. In addition, this course collects
feedback for continuous improvement. As you go through the course, you are
encouraged to leave quick feedback on any unit you like with the feedback widget
at the bottom of each page. Feedback is anonymous and will be secured by Axim
Collaborative and periodically reviewed for course improvement.

   .. image:: /_images/release_notes/quince/demox_post_7.png


About John Swope: John Swope is the architect for the new DemoX course, and the
founder of Curricu.me who specializes in Open edX® course development and custom
games and interactives for the platform. He is extremely grateful for the many
contributions from the Open edX® community that made this course possible. 

.. _DemoX github repository: https://github.com/openedx/openedx-demo-course
.. _Creative Commons BY-NC-SA 3.0 US License: http://creativecommons.org/licenses/by-nc-sa/3.0/us/

**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-04-28    | Docs WG                       | Teak           | Deprecated: This is no longer the current release |
+--------------+-------------------------------+----------------+---------------------------------------------------+

