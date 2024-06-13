Maintainers Home
################

.. grid:: 1 2 2 2
   :gutter: 3
   :padding: 0

   .. grid-item-card:: How-tos
      :class-card: sd-shadow-md sd-p-2
      :class-footer: sd-border-0

      * :doc:`how-tos/maintain-a-repo`
      * :doc:`how-tos/ongoing-maintainers-tasks`

   .. grid-item-card:: References
      :class-card: sd-shadow-md sd-p-2
      :class-footer: sd-border-0

      * :doc:`references/tools_for_maintainers`
      * `Maintainers Slack Channel`_
      
   .. grid-item-card:: Process Documentation 
      :class-card: sd-shadow-md sd-p-2
      :class-footer: sd-border-0

      * `Maintainership Wiki Space`_
      * `Maintainers Scrum of Scrums Notes`_
      * `Maintainers Office Hours Notes`_

Concepts Documentation
**********************

* :doc:`openedx-proposals:processes/oep-0055-proc-project-maintainers` - The
  OEP that kicked off the maintainership program.

* `Community Contributions Project Manager`_ - The role definition for the
  Community Project Managers.  They help triage community PRs and coordinate
  reviews from subject matter experts.

High Level Contribution Process
===============================

.. graphviz::

   digraph G {
     "Pull Request Opened" [shape=box];
     "Needs Product Review" [shape=box, style=rounded];
     "Does this Contribution\n change user experience?" [shape=diamond];
     "Is this contribution \nrelated to groomed work\n from the public road map?" [shape=diamond];
     "Ready for Engineering \nReview" [shape=box, style=rounded];
     
     
     "Pull Request Opened" -> "Does this Contribution\n change user experience?";
     "Does this Contribution\n change user experience?" ->   "Is this contribution \nrelated to groomed work\n from the public road map?" [label="Yes"];
     "Is this contribution \nrelated to groomed work\n from the public road map?" -> "Needs Product Review" [label="No"];
     "Does this Contribution\n change user experience?" ->   "Ready for Engineering \nReview" [label="No"];
     "Is this contribution \nrelated to groomed work\n from the public road map?" -> "Ready for Engineering \nReview" [label="Yes"]
   
   }

.. graphviz::

   digraph G {
       rankdir="LR";
       
       "PR Opened" [shape=none];
       "Ready for\n Review" [shape=none];
       "Scheduled for\n Review" [shape=none];
       "In Review" [shape=none];
       "Merged" [shape=none];
       
       open_day [label="Day 1", shape=none];
       ready_for_review_day [label="Day 2", shape=none];
       scheduled_for_review_day [label="Day 3", shape=none];
       in_review_day [label="Day 4", shape=none];
       merge_day [label="Day 5", shape=none];
       
       { rank=same; open_day, "PR Opened" };
       { rank=same; ready_for_review_day, "Ready for\n Review" };
       { rank=same; scheduled_for_review_day, "Scheduled for\n Review" };
       { rank=same; in_review_day, "In Review" };
       { rank=same; merge_day, "Merged" };
       
       open_day -> ready_for_review_day -> scheduled_for_review_day -> in_review_day -> merge_day [style="invis"];
       "PR Opened" -> "Ready for\n Review" -> "Scheduled for\n Review" -> "In Review" -> "Merged";
       
       open_day -> "PR Opened" [arrowhead=none]
       ready_for_review_day -> "Ready for\n Review" [arrowhead=none];
       scheduled_for_review_day -> "Scheduled for\n Review" [arrowhead=none];
       in_review_day -> "In Review" [arrowhead=none];
       merge_day -> "Merged" [arrowhead=none];
       
   }

.. _Maintainers Slack Channel: https://openedx.slack.com/archives/C03R320AFJP

.. _Maintainers Office Hours Notes:  https://openedx.atlassian.net/wiki/spaces/COMM/pages/3603791889/Office+Hours+Notes

.. _Maintainers Scrum of Scrums Notes: https://openedx.atlassian.net/wiki/spaces/COMM/pages/3507027983/Maintainers+Scrum+of+Scrums

.. _Maintainership Wiki Space: https://openedx.atlassian.net/wiki/spaces/COMM/pages/3426844690/Maintainership+Pilot

.. _Community Contributions Project Manager: https://openedx.atlassian.net/wiki/spaces/COMM/pages/3548807177/Community+Contributions+Project+Manager

