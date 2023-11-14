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

* `Internationalization Coding Guidelines`_
* `RTL UI Best Practices`_
* `Accessibility Guidelines`_
* `Analytics Guidelines`_
* `Eventing Design and Review Process`_

.. _Contributing to the Documentation for your Open Source Feature:

=====================
Feature Documentation
=====================

Documentation can occur in multiple places - in code, in decision records, or in
formal feature documentation.

`OEP-19 Developer Documentation`_ describes the various ways to provide
documentation of your code and features to a developer audience. This includes
API documentation, decision records (ADRs and OEPs), and README files. Of
course, you should always provide detailed, informative comments within your
code and excellent docstrings for your functions and classes!

If you have developed a new feature, created an XBlock, or otherwise see that a
topic is missing in this documentation, you can create one or more new pages in
this document and submit a pull request to have the content added. Follow the
guidelines in :doc:`../../../../documentors/references/doc_guidelines`.

Additionally, please see the section on :ref:`Named Release documentation` -
consider documenting your change for the upcoming Named Release.

========================
Feature Rollout Concerns
========================

When writing your feature, consider the ways in which your code might be rolled
out on various Open edX instances. `OEP-17 Feature Toggles`_ describes the many
reasons why you might use a feature toggle, including releasing incrementally,
beta testing, and providing one Open edX release where the feature is optional
before making it the default. Utilizing various `Waffle`_ flags, you can gate
your feature using an on/off switch. Within ``edx-platform``, you can also
utilize ``CourseWaffleFlag``, a toggle that allows you to gate a feature
per-course.

Waffle flags should be well-documented when they are used. Some of the Waffle
flags used in ``edx-platform``, as well as how they are documented, can be seen
in the `lms/djangoapps/courseware/toggles.py`_ file. (As a note, you can view
all Waffle flags in edx-platform here: :doc:`edx-platform:references/featuretoggles`,
and please be sure to document any Django settings you define as well - those
are documented here: :doc:`edx-platform:references/settings`.)

.. _lms/djangoapps/courseware/toggles.py: https://github.com/openedx/edx-platform/blob/master/lms/djangoapps/courseware/toggles.py

=============================
Operational Impact on edx.org
=============================

The edx.org website continuously deploys the latest version of the Open edX code
directly onto its site. This means that, for most repos, once your code is
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


.. include:: ../links.rst
