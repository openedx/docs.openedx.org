.. _How to Read the Roadmap:

How to Read the Product Roadmap
###############################

.. tags:: community, how-to

The `Open edX Product Roadmap`_ is the way in which the Open edX community comes together to collaboratively develop and advance the Open edX platform.

.. contents::
 :depth: 1
 :local:

What is the Product Roadmap?
************************************

The Roadmap is a Kanban-style board, organized into 7 main status categories nested within swimlanes.

See the :ref:`What is the Roadmap` concept guide for more information.

Status Columns
******************

**Ideation**: A collection of early-stage ideas for possible contributions to the Open edX platform. Ideation tickets consist of simple opportunity briefs outlining the reason behind the idea and the basic value-add. There is no guarantee that the work outlined ideation tickets will be completed. It is a responsibility of the `Product Working Group`_ to create a framework for assessing and prioritizing ideation tickets in alignment with overall product strategies.

**Prioritized**: Subset of ideation tickets that have been identified by the Product Working Group for further discovery.

**Backlog - Is Resourced**: Initiatives that are intended for contribution, that are in the backlog at any organization in the community. A ticket enters the backlog after it has been approved by the Product Working Group.

**Backlog - Is Not Resourced**: Initiatives that have been approved by the Product Working Group, but that are not in the backlog of any organization in the community. This work is available to be picked up.

**In-progress**: Initiatives that are intended for contribution that are in-flight. In-progress tickets must contain information about: the initiative goal; context; scope and approach; value and impact.

**Done: To Ship in a Future Named Release**: Work on an Initiative is complete and it may be live for Provider partners, but the Initiative has not yet been shipped in an Open edX Named Release.

**To Ship in [Named Release]** or **Shipped in [Named Release]**: Work on an Initiative is included in a specific Named Release.

Swimlanes
*************
The Roadmap is grouped into a set of “swimlanes” - horizontal lines that split a kanban board into sections. We use them to visually separate different work types on the same board and organize homogenous tasks together. The following swimlanes are represented on the board:

Content Core
=============

Roadmap items specifically related to the core authoring and/or learning experience. Examples include the Copy-Paste feature in Studio, Libraries, LMS navigation improvements, improvements to the LMS Progress page, and content tagging.

Platform Core
==============

Platform Core roadmap items relate to enhancements and improvements within core platform code (generally referring to the `edx-platform`_ repository). Examples include new platform APIs; features involving authentication or user profile information; integrations such as Credly, Salesforce, or Ecommerce; and new frontend plugin slots.

Data and Analytics
===================

Roadmap items relating to advancing the state of data analytics within the platform. These items generally focus on efforts within the :ref:`openedx-aspects:Aspects Home` project.

Maintenance
============

Roadmap items related to platform maintenance, for example, major package upgrades (Python, node, React, etc) and technical backend-focused projects (migrating forums from Ruby to Python, migrating from MongoDB to MySQL, etc).

Not all technical projects fall into this category. For example, MFE conversions often fall into “Content Core” (Studio or Learning MFE conversions) or “Platform Core” (Authentication MFE conversion). Improvements to Paragon components would likely fall under “Content Core”. Major infrastructure projects might fit into any category - for example, Design Tokens (comprehensive theming) and Role-Based Access Control fall under “Platform Core”.

Potpourri
==========

Important efforts that don't fit cleanly into any of the above categories.

Tabbed Views
****************

Additionally, the Roadmap contains varied views that narrow the scope to certain areas of the platform. For example, a view for the end-to-end landscape of investments and ideas for investment in the Studio Authoring experience. Roadmap views are a current work-in-progress and are expected to change over time.

The Product Working Group triages incoming proposals using the `Product Review Tracking view <https://github.com/orgs/openedx/projects/4/views/20>`_. This view shows newly filed proposals in the “No Status” column, and as the proposals are triaged, assigned a Coordinator, and progress through the `Product Review Process`_, this view represents the status of the proposal throughout this process.

Projects Not On The Product Roadmap
***********************************************

Not all projects need to be represented on the Product Roadmap. For example, plugins such as Frontend Plugins or XBlocks can be developed and published outside of the Open edX core codebase by any organization. In the future, the `Extensions Catalog <https://openedx.atlassian.net/wiki/spaces/COMM/pages/4411195427/Community+Proposal+Open+edX+Extensions+Marketplace>`_ will be an authoritative source of all plugins developed and published by members of the Open edX community.

How Can I Add to the Product Roadmap?
*************************************************

We need your participation in order to make the Roadmap a successful and meaningful artifact. Please follow the `Product Review Process`_ to submit your product proposal - whether it’s a rough idea or an initiative your team is planning to complete - to the roadmap.


.. seealso::

   :ref:`What is the Roadmap`

.. include:: /links.txt

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|2025-04-01    | Sarina Canelake               |  Sumac         | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
