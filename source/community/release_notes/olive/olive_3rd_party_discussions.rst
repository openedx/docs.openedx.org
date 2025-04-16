Configuring 3rd Party Discussion Experiences (Olive)
####################################################

The Olive release includes the ability to configure a 3rd party discussion
provider for your course's discussion experience. This configuration is done
within Studio. Read on for more details.

.. contents::
  :local:
  :depth: 2

Setup Discussions Prior to Course Start
***************************************

The Olive release includes the ability to configure a 3rd party discussion
provider for your course's discussion experience. This must be done prior to a
course's start date. To do this, first navigate to the Pages and Resources view:

      .. image:: /_images/release_notes/olive/discussC1.png


Clicking on the “Discussion” gear icon brings you to a landing page where you
can pick from various discussion provider options for your course:

      .. image:: /_images/release_notes/olive/discussC2.png


The options include descriptions, and a checklist below the options compare the
benefits of the various types of providers. Note that only the “edX” option is
included with the Olive release. Configuring one of the other providers
(Yellowdig, InScribe, Piazza, or Ed Discussion) requires you to have a
subscription at that site. These external providers may charge for their
services.

Enabling a Third-Party Discussions Provider
*******************************************

Your instance administrator will help you configure the new discussions provider
for your course. Note that you'll need your course to allow PII sharing with the
discussions provider. You should ensure you understand the implications of this,
which may include sending learner usernames, email addresses, and/or full names
to the third party provider, and may not be allowed in your jurisdiction.

First, reach out to your chosen provider and get a course set up. You will need
them to send you the following LTI launch info: Consumer Key, Consumer Secret,
and Launch URL. Once you have that, your instance administrator will take the
following steps:

#. To turn on PII sharing, your instance administrator will visit the admin page
   for PII sharing at
   ``[your-site-url]/admin/lti_consumer/courseallowpiisharinginltiflag`` and
   enable the option using your course's course key.

#. Once that is done, the instance administrator will be able to set up the LTI
   integration by visiting the course's Pages & Resources view in Studio,
   clicking on the preferred discussion provider, and filling in the LTI launch
   info:

         .. image:: /_images/release_notes/olive/discussC3.png



We'll now take a short look at the four available discussion providers and let
you know how to get started with each of them.

Ed Discussion
=============

`Ed Discussion <https://edstem.org/>`_ helps scale class communication in an
intuitive interface to facilitate Q&A and quality discussion, provide course
information and more. Moderation tools are robust, and instructors can access an
analytics page which shows trends in participation, views, answers, and top
contributors across a variety of metrics. Functionality includes automation,
advanced LaTeX, image annotation, live interpreters to help learners write and
execute code directly, and much more for STEM, CS, business and many other
disciplines.

Complementing Ed Discussion are `Ed Lessons <https://edstem.org/lessons>`_ and
`Ed Workspaces <https://edstem.org/workspaces>`_ for interactive content to
learn and practice skills like programming, bash scripts, HTML pages,
collaborative JuPyter notebooks, and much more.

      .. image:: /_images/release_notes/olive/discussC4.png
 
For more information or to get started with Ed Discussion visit `edstem.org
<edstem.org>`_ or contact team@edstem.org.

*Note: the above screenshot was provided by edX. The tCRIL team has been unable
to confirm that the iframe view of Ed Discussions works in Olive; for us, Ed
Discussions opened full screen rather than embedded in the LMS.*

Yellowdig
=========

`Yellowdig <https://www.yellowdig.co/>`_ is a community-focused platform aiming
to turn your course into an active learning community through its
research-driven, hyper-interactive, Yellowdig Engage platform. This platform was
built upon principles of Agency, Mastery, and Connectedness. Yellowdig is unique
in providing a graded discussions experience which is cumulative over the span
of your course, encouraging repeated and active participation in the discussions
forums.

      .. image:: /_images/release_notes/olive/discussC5.png



To learn more about Yellowdig, check out their `Resources page
<https://www.yellowdig.co/resources>`_, take their `introductory instructor and
design courses <https://learn.yellowdig.co/>`_, or email
learnmore@yellowdig.com.

Note: In the Olive release, the grade passback functionality is not implemented
in the Discussions MFE integration. To enable grades from Yellowdig in your
platform, we recommend that you `manually export grades from Yellowdig
<https://help.yellowdig.co/kb/en/article/exporting-grades-manual-grade-passback>`_
and input the scores directly into your course.

InScribe
========

InScribe is a learning support tool built on a community model. With InScribe,
learners and moderators can create conversations that can be collaboratively
answered and endorsed by moderators.Conversations are organized into topics,
which make it easier to navigate content. You can also copy your term into a new
course, to preserve useful content for future learners.

      .. image:: /_images/release_notes/olive/discussC6.png



To get a peek into how a community can be used as a knowledge repository as well
as a place to get accurate information, ask questions, and connect with peers,
visit `InScribe's Get to Know Us Page
<https://inscribe.education/main/inscribe/6754110229500853/compositions/6749461749594201>`_
and their `tips for a thriving community
<https://inscribe.education/main/inscribe/6754110229500853/compositions/6749461749594195>`_.
To get started with InScribe, reach out to hello@inscribeapp.com.

Piazza
======

`Piazza <https://piazza.com/>`_ is an engaging question and answer tool that
focuses on features such as wiki-style collaborative answers to questions,
support for mathematical-based courses in LaTeX, real-time updating, and
effective moderation tools such as instructor-endorsed answers. Instructors can
view engagement reports that give insight into individual participation levels
and allow you to pinpoint when your class is asking the highest volume of
questions.

      .. image:: /_images/release_notes/olive/discussC7.png

To get started with Piazza, reach out to team@piazza.com. 


**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-04-28    | Docs WG                       | Teak           | Deprecated: This is no longer the current release |
+--------------+-------------------------------+----------------+---------------------------------------------------+
