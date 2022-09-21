Platform Overview
#################

The Open edX Platform is made up of multiple web services that work together to
provide all the tools you might need to build and run courses online.

Tech Stack
**********

While there are a few exceptions for the most part the technology stack for the
Open edX Platform is based on `Django`_ based backend servers and `React`_ based
frontend apps.  There are multiple frontend apps which are usually referred to as
MFEs(Micro-FrontEnds) within the ecosystem and community.

The core code base lives on GitHub in the `openedx`_ organization.

Platform Layout
***************

While the platform contains many services, MFEs and libraries the core of the
platform lives in the `edx-platform`_ and `frontend-platform` repositories.

* edx-platform - This was the first service created in the Open edX ecosystem and
  contains the legacy monolith application. That application currently can run
  in two modes.

  As the LMS(Learning Management System) it serves as the backend
  for learner data as they go through courses, programs, and serves some legacy
  UI elements.

  As the CMS(Content Management System) it serves as the place where instructors
  and course authors can build the course content that learners will consume.

* frontend-platform - This is a newer core system meant to ease the creation of
  multiple small frontend applications(MFEs) by bundling together many common
  utilities that all frontends need.  This includes things like auth workflows,
  logging, monitoring and translations related tooling.

Along with these two core systems, there exist a number of other `backend
services`_ and `MFEs`_ which you can find on GitHub.

Libraries
=========

In addition to the backends and front-ends mentioned above, the platform is made
of numerous 1st party libraries, that live in the `openedx`_ organization.
These libraries accomplish a variety of different tasks, and you can find more
details about what they do in their READMEs.

Exceptions
**********
While the above summary covers most of the system, there are a few exceptions to
be aware of.


Non-Django Backends
===================
The `cs_comments_service`_ which provides discussion forum capability within the
platform is a legacy application that is written in Ruby, using the Sinatra
framework.

Non-React Frontends
===================
The Open edX Platform is currently still in the process of moving to React based
MFEs.  Previously front-end content used to be served by the Django services.
This means that there are still many parts of the system that use `Django
Template`_ based rendering pipelines to serve frontend content to users.

.. note::

   An exception to the expception.  In edx-platform rather than using the
   default Django templates, django is setup to use `Mako`_ based templates.

.. _Django: https://www.djangoproject.com/
.. _React: https://reactjs.org/
.. _openedx: https://github.com/openedx/
.. _edx-platform: https://github.com/openedx/edx-platform
.. _frontend-platform: https://github.com/openedx/frontend-platform
.. _backend services: https://github.com/orgs/openedx/repositories?q=topic%3Abackend-service&type=all&language=&sort=
.. _MFEs: https://github.com/orgs/openedx/repositories?q=frontend-app&type=all&language=&sort=
.. _cs_comments_service: https://github.com/openedx/cs_comments_service
.. _Django Template:
.. _Mako: https://www.makotemplates.org/
