Purpose of This Repo
####################

.. note::

   This is mostly a copy of the summary and recommendation sections of the
   `original product discovery documentation`_.  That document will have more
   information about the exact work that went into developing the
   recommendation.

   This document serves as a confirmation that we are accepting the
   recommendation that came out of the discovery work.


Status
******

**Accepted**

Context
*******

Over the years of its existence, the documentation to support Open edX has grown
and evolved organically. Without a clear end-to-end information strategy to
guide the creation and organization of the documentation, and without a clear
definition of users’ end goals, a number of problems have arisen:

#. The Open edX project documents things in many places, including repos, RTDs,
   the wiki, the Open edX website. It's messy, without a clear strategy for what
   types of docs should live where and why, and for whom docs are intended.

#. It's not clear to end-users where to look for the right documentation to
   address their questions or to learn the platform. It's also not clear to
   contributors where to put new documentation, or how to improve current
   documentation.

#. Information is often out of date.

#. https://docs.edx.org is specific to https://edx.org. With the split of edX
   from Open edX, it's necessary to design a documentation strategy that speaks
   specifically to Open edX user needs, pain points and expectations, and that
   removes edX specific needs, pain points and expectations.

#. Documentation is less developed, or not organized in the most appropriate
   way, for certain types of users, for example faculty/course authors. One
   Instance administrator noted that some `Open edX Documentation
   <https://edx.readthedocs.io/projects/open-edx-building-and-running-a-course/en/latest/index.html>`__
   is actually a barrier of entry for faculty, rather than a facilitator to
   entry, because 1) the documentation is too dense; 2) there's not a clear path
   through the documentation to connect the faculty with their need; 3) it's
   overwhelming at first sight.

The above issues make it difficult for users to engage with the Open edX
platform, whether they’re a software developer looking for documentation for new
feature flags or a faculty member looking for instructions to quickly build a
new course.

.. _original product discovery documentation: https://openedx.atlassian.net/wiki/spaces/OEPM/pages/3389849714/Discovery+Proposal+Open+edX+Documentation+Restructure

Decision
********

Given the above context and learnings from the `original product discovery`_ we
make the following decisions.


#. `docs.openedx.org`_ will exist and serve as the root site for all Open edX
   documentation.

   Its goal is to make the organization of documentation clear and make it easy
   to find the right kind of information based on a user's needs. It is
   essentially an index that helps to orient users and way find to the right
   document for their needs.

#. `docs.openedx.org`_ will be organized by persona, such that each persona
   has a clear entry point into the documents relevant to their needs.

   We will start with the following personae and expect this list to expand:

   * Site Operators: Set up/upgrade and run an Open edX instance

   * Educators: Build an Open edX course

   * Course Operators: Run an Open edX course

   * Software Developers: Customize an Open edX course

   * Documenters: Anyone looking to create or update Open edX documentation

#. We will organize the documentation for each persona around the
   `documentation quadrant approach`_.  Thus all personae must have the
   following four document types/categories:

   * Quickstart guides

   * How-TOs

   * References

   * Explanation/Concepts

.. _original product discovery: https://openedx.atlassian.net/wiki/spaces/OEPM/pages/3389849714/Discovery+Proposal+Open+edX+Documentation+Restructure
.. _docs.openedx.org: https://docs.openedx.org
.. _documentation quadrant approach: https://documentation.divio.com/

Consequences
************

#. `docs.openedx.org`_ exists.

#. There will be a period of time where both `docs.openedx.org`_ and
   `docs.edx.org`_ exist.  `docs.edx.org`_ has historically been the location to
   find Open edX docs.  It contains a lot of good information but suffers from
   the issues outlined above in the `Context`_ section.

   * As documentation is created or migrated to the new site, we will need to
     deprecate the old documentation.  We'll need a process for this that
     doesn't necessarily delete the old docs but routes people to the relevant
     new docs where it makes sense.

#. `OEP-19`_ will need to be updated to align developer documentation with the
   high level documentation with the decisions made here.

.. _OEP-19: https://open-edx-proposals--340.org.readthedocs.build/en/340/best-practices/oep-0019-bp-developer-documentation.html
.. _docs.edx.org: https://docs.edx.org
