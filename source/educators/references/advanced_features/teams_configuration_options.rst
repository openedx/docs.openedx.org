.. _Teams Configuration Options:


Teams Configuration Options
###########################

.. tags:: educator, reference

There are several configuration options available to the Teams application.
Many basic configuration options are provided within Studio’s **Pages & Resources** area,
and course management capabilities are available to instructors directly from the Teams application.
Included below are details about both the configuration options and management tools.

Default Team Size
*****************

This specifies the maximum number of learners that can join a team, a default value for all teams in your course.
This default value can be overridden for a specific team group as well. This value has a hard limit and cannot exceed 500,
but in practice, this should be significantly lower. Teams should rarely have many learners in them at all.
If you have a use case where a large number of users need to be in a team, consider using discussions rather than teams.

Team Groups:
************

Each team group is a grouping for multiple learner teams. To start, each of these team groups must be given a
unique name, and optionally a description can also be set.

These names and descriptions are visible to learners in the Teams application as shown in the visual below.

    .. image:: /_images/educator_references/teams_application_screen.png
     :alt: The navigation bar in the LMS, showing the default pages.


.. note::  Do not delete topics once your course is
   running, if learners might have already joined teams within topics. If
   you delete a topic from the **Teams Configuration** policy key, that topic
   is no longer visible in the LMS, and learners will not be able to leave
   teams associated with the deleted topic.

Types of Team Groups
********************

There are several types of team group that can be created, each of which behaves
differently for both instructors and learners.

* **Open** sets up a team group where learner can create, join, leave, and see all teams within the group
* **Public managed** allows only course staff to control team creation and membership.
  Learners can see other teams but cannot join or leave their team.
* **Private managed** allows only course staff to control team creation and membership.
  Additionally, learners can only see the teams they are members of, unlike other options
  that give them visibility into other teams. This type is helpful in particular if team
  assignments are being used in a course.

.. note:: If you do not see all team group type options, check with your platform administrator
   to see if the relevant teams application features have been enabled.

Team Group Size Override
************************

Separate from the team maximum size setting, it is possible to override the specific team size for
a given team group, allowing you to adjust team sizes to fit your course needs.

.. seealso::
 

 :ref:`Teams Overview <CA_Teams_Overview>` (concept)

 :ref:`Managing Team Discussions <Teams Discussions>` (concept)

 :ref:`Enable and Configure Teams` (how-to)

 :ref:`The Learner's Experience of Teams <CA Learner Experience of Teams>` (concept)

 :ref:`Managing Teams via CSV Upload` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
