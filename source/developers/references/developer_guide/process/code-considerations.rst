*******************
Code Considerations
*******************

This is a checklist of all of the things that we expect developers to consider
as they are building new, or modifying existing, functionality.

.. contents::
   :local:
   :depth: 1

==================
Basic Code Quality
==================

As described in :doc:`overview`, your code should meet basic Open edX project
standards: it should be accessible, internationalized, and meet the concerns of
analytics.

* :ref:`i18n`
* `RTL UI Best Practices`_ (Here, RTL stands for "Right To Left", for languages
  like Arabic who read from the right side of the page to the left)
* :ref:`Accessibility Guidelines`
* :ref:`analytics`
* Use :doc:`openedx-proposals:best-practices/oep-0051-bp-conventional-commits`
* Basic security best practices. The Open Web Application Security Project
  provides a great set of `security-related cheatsheets
  <https://cheatsheetseries.owasp.org/>`_ to help address common software
  security issues.
* Basic performance concerns. The Open edX project currently does not run a
  performance sandbox, but attention should be paid to basic performance issues
  that may hurt large instances, such as expensive database queries and database
  migrations. See the `Django documentation on performance
  <https://docs.djangoproject.com/en/4.2/topics/performance/>`_ for some tips
  around creating performant Django sites.

.. _Contributing to the Documentation for your Open Source Feature:

=====================
Feature Documentation
=====================

Documentation can occur in multiple places - in code, in decision records, or in
formal feature documentation.

:doc:`openedx-proposals:best-practices/oep-0019-bp-developer-documentation` describes the various ways to provide
documentation of your code and features to a developer audience. This includes
API documentation, decision records (ADRs and OEPs), and README files. Of
course, you should always provide detailed, informative comments within your
code and excellent docstrings for your functions and classes!

If you have developed a new feature, created an XBlock, or otherwise see that a
topic is missing in this documentation, you can create one or more new pages in
this document and submit a pull request to have the content added. Follow the
guidelines in :ref:`Documentor Guidelines`.

Additionally, please see the section on :ref:`Named Release documentation` -
consider documenting your change for the upcoming Named Release.

========================
Feature Rollout Concerns
========================

When writing your feature, consider the ways in which your code might be rolled
out on various Open edX instances. :doc:`openedx-proposals:best-practices/oep-0017-bp-feature-toggles` describes the many
reasons why you might use a feature toggle, including releasing incrementally,
beta testing, and providing one Open edX release where the feature is optional
before making it the default. Utilizing various `Waffle`_ flags, you can gate
your feature using an on/off switch. Within ``edx-platform``, you can also
utilize ``CourseWaffleFlag``, a toggle that allows you to gate a feature
per-course.

Waffle flags should be well-documented when they are used. Some of the Waffle
flags used in ``edx-platform``, as well as how they are documented, can be seen
in the `lms/djangoapps/courseware/toggles.py`_ file. (As a note, you can view
all Waffle flags in edx-platform here: :ref:`edx-platform:featuretoggles`,
and please be sure to document any Django settings you define as well - those
are documented here: :doc:`edx-platform:references/settings`.)

.. _lms/djangoapps/courseware/toggles.py: https://github.com/openedx/edx-platform/blob/master/lms/djangoapps/courseware/toggles.py

=====================================
Operational Impact on Early Deployers
=====================================

Some sites (like edx.org) continuously deploy the latest version of the Open edX code
directly onto their site. This means that, for most repos, once your code is
merged to master/main it will be deployed live on edx.org within a few hours.
This is very cool - your changes are live, immediately! - and it also means that
edx.org does the community a large service of testing our code in advanced of
the next named release.

However, this also means that if your code causes a problem on edx.org, your
pull request may get reverted. Please pay attention to PRs that are especially
prone to problems (for example, database migrations) and be prepared to answer
questions posted to your PR for the day or so after it merges.

.. _Named Release documentation:

=======================
Open edX Named Releases
=======================

Open edX Named Releases come out every six months. They are cut in early April
and early October, tested for two months, and released in June and December. If
you are introducing breaking changes, complicated migrations, deprecations, or
anything else of note, please note your changes on the appropriate release page
of the `Open edX Release Planning`_ wiki page. Especially important is
information that system installers or operators will need to know. Please
include your name when you add an item, so that the release coordinators can get
back to you with questions.

.. _Open edX Release Planning: https://openedx.atlassian.net/wiki/spaces/COMM/pages/13205845/Open+edX+Release+Planning


.. include:: /links.txt


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
