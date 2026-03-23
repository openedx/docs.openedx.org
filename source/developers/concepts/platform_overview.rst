Platform Overview
#################

.. tags:: developer, concept

The Open edX Platform is made up of multiple web services that work together to
provide all the tools you might need to build and run courses online.

Tech Stack
**********

While there are a few exceptions, for the most part the technology stack for the
Open edX Platform uses `Django`_ for backend services and `React`_ for the frontend.
The frontend consists of multiple frontend apps which are usually referred to as
MFEs (Micro-FrontEnds) within the ecosystem and community.

The core code base lives on GitHub in the `openedx`_ organization.

If you want more details about the tech stack, check out this video:

.. youtube:: LlpdOUnymAQ

Platform Layout
***************

While the platform contains many services such as MFEs and libraries, the
core of the platform lives in the `openedx-platform`_ and `frontend-platform`_
repositories.

* openedx-platform - This was the first service created in the Open edX ecosystem and
  contains the legacy monolith application. That application currently can run
  in two modes: LMS and Studio.

  As the LMS (Learning Management System), it acts as the backend
  for learners' data as they go through courses and programs, and it serves some
  legacy UI elements.

  As Studio, it is the CMS (Content Management System) where instructors and
  course authors can build the course content that learners will consume.


* frontend-platform - This is a newer core system meant to ease the creation of
  multiple MFEs by bundling together many common utilities that all frontends
  need.  This includes things like authentication workflows, logging,
  monitoring and translations related tooling.

Along with these two core systems, there exist a number of other `backend
services`_ and `MFEs`_ which can be found on GitHub.

Libraries
=========

In addition to the backends and frontends mentioned above, the platform is made
of numerous libraries that live in the `openedx`_ organization.
These libraries accomplish a variety of different tasks. More details about
what they do can be found in their READMEs.

Exceptions
**********
While the above summary covers most of the system, there are a few exceptions.

Non-React Frontends
===================
The Open edX Platform is currently still in the process of `moving to React based
MFEs`_.  Previously frontend content used to be served by the Django services.
This means that there are still many parts of the system that use `Django
Template`_ based rendering pipelines to serve frontend content to users.

.. note::

   An exception to the exception.  In openedx-platform rather than using the
   default Django templates, django is setup to use `Mako`_ based templates.

.. _Django: https://www.djangoproject.com/
.. _React: https://reactjs.org/
.. _openedx: https://github.com/openedx/
.. _openedx-platform: https://github.com/openedx/openedx-platform
.. _frontend-platform: https://github.com/openedx/frontend-platform
.. _backend services: https://github.com/orgs/openedx/repositories?q=topic%3Abackend-service&type=all&language=&sort=
.. _MFEs: https://github.com/orgs/openedx/repositories?q=frontend-app&type=all&language=&sort=
.. _moving to React based MFEs: https://github.com/openedx/openedx-platform/issues/31620
.. _Django Template: https://docs.djangoproject.com/en/6.0/topics/templates/
.. _Mako: https://www.makotemplates.org/

Adding new Features to the Open edX Platform
********************************************

If you're looking to add new features to the Open edX Platform, we recommend
extending the platform rather than trying to make changes to the core.

The modular Open edX platform provides many extension points that don't require modification to the core codebase or review from the Open edX community. These include:

* :ref:`Frontend plugin "slots" <Use A Frontend Plugin Framework Slot>` for UI customization
* :ref:`XBlocks <xblock:Open edX XBlock Tutorial>`, a composable framework to enable rapid development and pluggability of new content types
* :ref:`Hooks Extension Framework` for modifying the platform's functionality and flows
* :ref:`Design tokens <Design Tokens>` for theming customization

Check out the `Sample Plugin <https://github.com/openedx/sample-plugin>`_ for documentation and examples of leveraging the various Open edX extension points.

New update to the core platform
===============================

If we don't have extension points for the kind of change you want to make, you might need to make a change to the core source.
This can be complex and we encourage you to `reach out to us`_ to talk about the kind of changes you want to make.

.. _reach out to us: https://open.edx.org/community/connect/

Two quickstarts are provided for developers looking to jump in and contribute to
the open-source Open edX project. The :ref:`Pull Request Quickstart <qs Dev
First PR>` goes through the GitHub “pull request” workflow all developers who
contribute must follow. You'll learn how to set up a development environment and
at the end will have made your first pull request to the project.

The :ref:`Contributing Quickstart <qs Dev Contributing>` builds on the Pull
Request Quickstart to guide you through the process of making a more substantial
change to the platform. It discusses both technical and product considerations.

The `Open edX contribution course
<https://apps.training.openedx.io/catalog/courses/course-v1:OpenedX+OEX101+2023/about>`_
and the `Developer onboarding course
<https://apps.training.openedx.io/catalog/courses/course-v1:OpenedX+OEX-Dev101+2024/about>`_
are additional, helpful resources.


.. seealso::

   - `Open edX Platform Architecture Introduction <https://www.youtube.com/watch?v=LlpdOUnymAQ&list=PL87xhvJSz2W4Pn4dpmxT9goqhGicqg2-5&index=4>`_



**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|  2025-03-25  |    sarina                     |   Ulmo         |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
