Aspects Release Notes (Redwood)
###############################

The Product and Engineering Teams from eduNEXT and Axim Collaborative are
thrilled to introduce Aspects Reports for course delivery teams and site
operators! Operators can learn more about enabling Aspects on their
installations by reviewing the :doc:`dev_op_release_notes`.

What are Aspects Reports?
*************************

Aspects Reports provide access to near real-time course and instance data
through dashboards with interactive tables and charts.

IMAGE 1

How can I find Aspects Reports?
*******************************

Accessing course-level dashboards from the LMS
==============================================

Once Aspects has been installed, users can easily `access Aspects Reports
<https://openedx.atlassian.net/wiki/x/CIBJ-Q>`_ for a
course directly from the Open edX LMS by clicking on a new Reports link on the
Instructor Dashboard. There's no need to navigate elsewhere to gain valuable
insight into exactly what's going on in a course.

IMAGE 2

On the Reports tab in the LMS, users can navigate between three new dashboards:
a `course dashboard <https://openedx.atlassian.net/wiki/x/FIBI-Q>`_, `at-risk
learners dashboard <https://openedx.atlassian.net/wiki/x/EQBD-Q>`_, and `individual learner
dashboard <https://openedx.atlassian.net/wiki/x/CoBE-Q>`_. These dashboards were
designed specifically for course authors and course teams looking to access
quick and easy-to-glean engagement, enrollment, and performance data from their
courses.

IMAGE 3

Accessing all Aspects has to offer from Superset
================================================

Course delivery team members who plan to view information for one course and
then another may chose to `navigate to Superset
<https://openedx.atlassian.net/l/cp/c1n0h2AD>`_, a third-party data
visualization tool used to create and display Aspects dashboards and charts.
This will allow these users to easily view the three out-of-the-box course-level
dashboards for one of their courses and followed by another and another.

Site operators and superusers can view data about any course on their Open edX
instance or their whole Open edX instance in Superset. `Users can access Superset
directly via a link from the Aspects Reports in the LMS
<https://openedx.atlassian.net/wiki/spaces/OEPM/pages/4248666119/How-to+Navigate+to+Superset>`_
using single sign-on authorization via their LMS account credentials.

IMAGE 4 Go to superset

Using single sign-on allows users to access Superset directly using their LMS
account without having to create and log-in with a separate Superset account.

IMAGE 5 Authorize

IMAGE 6 Sign In

Once in Superset, site operators can view a course dashboard, at-risk learner
dashboard, individual dashboard for any course on their instance as well as an
operator dashboard that displays information about their entire Open edX
instance.

IMAGE 7 operator dashboard

Site operators can even use Aspects to create and share custom dashboards and
charts in Superset beyond what is provided out of the box with the plugin.

Course-level dashboard highlights
*********************************

Course Dashboard
================

The Course Dashboard displays enrollment, engagement, and performance
information for all learners in a course.

Because this dashboard displays unit page, video, and problem engagement
information for a course, the charts and tables in this dashboard give users a
glimpse into how their course content is performing.

For example, when unit page engagement is plotted sequentially across the whole
course, course delivery teams may be able to better identify key points in the
course where learner engagement drops off.

IMAGE 8 green bars red circles

When `cross-filtered <https://openedx.atlassian.net/wiki/x/KABN-Q>`_ by a single
course video, the Watched Video Segment graphs can help course authors and teams
pinpoint potentially unclear video timestamp ranges.

IMAGE 9 Yellow bars

With a benchmark percent correct figure in mind, users can identify problems
that may be too easy or too difficult by sorting the Problem Results table by
percentage of attempts correct or incorrect.

IMAGE 10 Problem results


Individual and At-Risk Learner Dashboards
=========================================

In addition to course-wide data, Aspects Reports surface course activity data
for `individual learners <https://openedx.atlassian.net/wiki/x/CoBE-Q>`_ and
`learners that may be at-risk of not completing the course
<https://openedx.atlassian.net/wiki/x/EQBD-Q>`_ based on a set of predefined
risk factors. The at-risk learner group is made up of learners that have
enrolled in the course, done something in the course other than visit the course
outline page, have not yet passed the course, and have not visited the course in
seven or more days.

When installing the plugin, site operators can choose whether or not to show
limited personally identifiable information (PII) to course delivery teams. On
Open edX instances that show limited PII to course delivery teams, staff and
admin users can see and `download
<https://openedx.atlassian.net/wiki/x/GwBI-Q>`_ the names, usernames, and email
addresses of individual and at-risk learners making targeted communication and
learner intervention possible.

Key dashboard functionality
***************************

Hover to view more detail
=========================

Users can hover over any element in a table or chart in an Aspects dashboard to
view detailed information.

IMAGE 11 cumulative enrollemnts by track

Add filters to a dashboard
==========================

Users can `add filters <https://openedx.atlassian.net/wiki/x/G4BC-Q>`_ to an
Aspects dashboard using the filters panel on the side of each dashboard. Hover
over the filter icon on the upper corner of a table or chart to view what
filters were applied to create the data visualization on any dashboard.

IMAGE 12 watched video segments

Dive deeper into the data with interactive charts that can be cross-filtered
============================================================================

All Aspects Dashboards allow users to dig deeper into their data through
`cross-filters <https://openedx.atlassian.net/wiki/x/KABN-Q>`_. With
cross-filters, a user can apply the same filter to multiple charts and tables in
a dashboard at once. For example, if a user adds a cross-filter for a single
video on the Video Engagement tab of the Course Dashboard, all applicable video
tables and charts will update to show data only for that video.

IMAGE 13 video views by section/subsection

Download tables and images from Aspects dashboards
==================================================

Users can easily `download the data used to create any chart or table in an
Aspects dashboard in tabular format as a CSV or Excel file
<https://openedx.atlassian.net/wiki/x/GwBI-Q>`_ or `download the table or chart
as an image <https://openedx.atlassian.net/wiki/x/JQBJ-Q>`_ for use in their own
documents, presentations, or reports.

IMAGE 14 cumulative enrollments by track

