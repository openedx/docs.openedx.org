Sidebar Navigation Release Notes (Redwood)
##########################################

The Product, Design, and Engineering Teams at Western Governor's University,
Raccoon Gang, and Axim Collaborative are thrilled to offer users the opportunity
to try out a new method for navigating course content on the Open edX platform!
With the Redwood Release, site operators can choose to enable sidebar navigation
for courses on their instance, giving learners and course delivery teams a new
method for making their way through course content. Site operators should see
:ref:`redwood-enable-sidebar` for more detail.

While we're excited to share this new feature with the community, it's important
to note that this beta version contains a few known issues that we're actively
working to resolve in a future release. We encourage anyone who tries out
sidebar navigation to let us know if they discover any additional bugs while
using it. With the community's help, we can aim to make this the best navigation
experience it can be. 

.. note::

    Known issues with sidebar navigation include:
    
    * When a member of the course delivery team updates the name of a course
      unit, the unit name updates at the top of the unit page, but does not
      update in the sidebar navigation.
    * When using content groups in a course, the sidebar navigation does not
      hide hidden units when a staff user views the course as a content group
      using the masquerading feature. Content groups work as expected for real
      learners in content groups. Staff can masquerade as an individual user in
      a specific content group to view how a member of the content group
      actually sees the course and the sidebar.
    * Course sections, subsections, and unit names may appear as missing from
      the sidebar navigation in sections that include content that has yet to be
      published.


What is sidebar navigation?
***************************

Overview
========

The new navigation experience allows learners to navigate through course
material linearly or non-linearly via a new UI element on the side of the page
that displays the user's current course section, subsection, and unit.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot1.png
      :align: center

With sidebar navigation enabled, learners will still be able to navigate the
course linearly by using the Next or Previous buttons above and below course
content.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot2.png
      :align: center

Additionally, learners can easily navigate the course non-linearly without
having to go to the Course Outline page. Learners can click on any unit in the
sidebar to view that unit. The sidebar displays both the unit name and an icon
indicating the type of content in that unit. The idea is to give the learner a
fuller sense of what content exists where in the course, so that they can
navigate it in a way that makes sense for them.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot3.png
      :align: center
      :height: 350


Learners can explore the contents of a subsection by clicking on any collapsed
subsection heading to expand and view the units within.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot4.png
      :align: center
      :height: 350
      
The subsection heading expands when it is clicked to display its units.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot5.png
      :align: center
      :height: 450


If a learner wants to `view to a unit in another section of the course`_, they can
click on the back button in the upper corner of the sidebar to view all sections
in a course.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot6.png
      :align: center
      :height: 350

After, they will see all sections.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot7.png
      :align: center
      :height: 350

The learner can then click on any other section to view its contents.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot8.png
      :align: center
      :height: 350

Although the learner is not currently viewing a unit in this module, they are
still able to view its contents.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot9.png
      :align: center
      :height: 350


Collapsing and expanding the sidebar navigation
===============================================

The learner can easily collapse the sidebar navigation at any time to view the
course content in a full page format by clicking the collapse button in the
upper corner of the sidebar.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot10.png
      :align: center

The learner can revisit the sidebar navigation at any time by clicking the
expand button in the upper corner of the page.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot11.png
      :align: center

As the learner advances through the course, the expanded or collapsed state of
the sidebar remains the same until the learner changes it. See
:doc:`/educators/how-tos/sidebar_collapse_expand`.

Viewing completed and in-progress items
=======================================

When a learner completes a course unit, the icon next to the unit name in the
sidebar navigation updates to indicate that it was completed.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot12.png
      :align: center
      :height: 350

The icon next to the subsection name updates to a checkmark icon when a learner
has completed all units in a subsection.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot13.png
      :align: center
      :height: 350

Similar to a completed the subsection, the icon next to the section name updates
to a checkmark icon once the learner has completed all subsections in the
section.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot14.png
      :align: center
      :height: 450

In addition to completions, in-progress work is indicated on the sidebar
navigation for course sections and subsections. Once a unit is completed in a
section or subsection, the icon next to the section or subsection name is
updated to reflect the rough amount completed.

   .. image:: /_images/release_notes/redwood/LSN_Screenshot15.png
      :align: center
      :height: 450

These in-progress icons serve to convey to the learner what sections or
subsections they have in-progress as well as how much content they've completed
for each section or subsection at a glance.

.. _view to a unit in another section of the course: https://openedx.atlassian.net/wiki/spaces/OEPM/pages/4264263692/How-to+View+course+sections+from+the+navigation+sidebar
.. _collapse the sidebar navigation: https://openedx.atlassian.net/wiki/spaces/OEPM/pages/4264722448/How-to+Collapse+and+expand+the+navigation+sidebar