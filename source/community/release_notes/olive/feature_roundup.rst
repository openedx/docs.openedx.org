Olive Feature Roundup
#####################

The Olive release contains many features, enhancements, and improvements. Some
are the subject of their own blog posts: :doc:`olive_discussions` and :doc:`olive_studio_editor`.
In this post we'll run through a number of other interesting
additions to the platform, with brief descriptions of what they are.

.. contents::
  :local:
  :depth: 1

Resets for Randomized Content Blocks
************************************

Randomized content blocks now have a “Reset” option, allowing learners to
prepare themselves for exams by answering a series of questions at random from a
predetermined problem bank (similar to flashcards). `This video demo of the
feature <https://www.loom.com/share/91b7224cb8a74cf2891a240b6e4fb8c6>`_ shows
the learner experience of being able to answer some questions within the Open
edX LMS and then clicking a “Reset” option to get a new set of unanswered
questions.

      .. image:: /_images/release_notes/olive/roundup1.png


To enable this feature, create a Randomized Content Block in Studio and set the
:guilabel:`Show Reset Button`` option to True.

      .. image:: /_images/release_notes/olive/roundup2.png


Note: before you can add randomized content blocks to your course, you must add
a Content Library in Studio. Once you've done that, you can add the randomized
content block by clicking the “Library Content” button when adding a new
Component to a Unit. See the next section for instructions on how to get a test
library.

Open edX Test Course & Test Library
***********************************

The Open edX project now provides a `testing course & testing library
<https://github.com/openedx/openedx-test-course/tree/master/dist>`_ with the aim
of exposing as many Open edX Studio & courseware features as possible. The test
course provides example usages of various block types and by enabling various
features through Advanced Settings, and also exposes usage of the test Content
Library. You are free to use these in your installation; it is useful both to
see how a problem type behaves in the LMS as well as how to set it up in Studio.

      .. image:: /_images/release_notes/olive/roundup3.png


Install the course or library by creating a new, blank course or library in
Studio. Then, from the Tools menu, select :guilabel:`Import`. Upload the correct file
(``test-course.tar.gz`` or ``test-problem-bank.tar.gz``), and you will be all set.

This course is new as of the Maple (June 2022) release, and is tested to work on
both Maple and Nutmeg; it's a bit sparse at the moment, but will be continually
updated over time. Currently, the test course contains at least one usage of all
advanced block types that come pre-installed in the Open edX release. Some of
the block usages aren't yet configured; for example, the LTI Consumer block
usage exists with instructions on how to use it, but it isn't actually set up to
consume an LTI tool yet.

We are looking for contributions to make this course better! If you're
interested in contributing, here are some things we're looking for:

* Actual tool launches for various configurations of lti and lti_consumer blocks.
* Use of content groups for units and sequences. Currently, content groups are only tested at the component (sub-unit) level.
* Use of custom Python in Advanced LONCAPA problems. 
* Examples usages of start/end dates, beta-released content, etc.
* Handouts, static tabs, and other advanced uses of the Course Home.

If you want to help out but don't know where to start, visit us on the
`Discussion Forums <http://discuss.openedx.org>`_. Instructions for contributing
are also available `on GitHub <https://github.com/openedx/openedx-test-course#contributing>`_.

Pages and Resources View
************************

Olive contains a new micro front-end (MFE) called course authoring, which
enables an overhaul of the Pages and Resources view. This is a page within your
course's configuration in Studio that allows you to easily turn features on and
off; applications and tools that previously required fiddling with advanced
course settings can now be set up in a few clicks using the Course Authoring
MFE.

      .. image:: /_images/release_notes/olive/roundup4.png


Clicking the gear icon on “Progress”, “Wiki”, and “Calculator” creates a pop-up
that allows you to quickly enable or disable the feature for the course. We'll
cover the various options available when choosing the Discussion option in a
future post.

Authentication Micro-frontend (MFE)
***********************************

A new MFE has been added in this release, known as the `Authentication (or
“Authn”) MFE <https://github.com/openedx/frontend-app-authn/>`_. This provides a
streamlined registration, sign in, and Forgot Password experience. During the
registration process, a set of available usernames are suggested, based on the
full name entered.

      .. image:: /_images/release_notes/olive/roundup5.png

If an entered username already exists, the user is notified and given some similar, available suggestions.

      .. image:: /_images/release_notes/olive/roundup6.png


Some brief operator notes: you can set the `LOGO_URL MFE setting
<https://github.com/openedx/frontend-app-authn/blob/master/src/base-component/AuthLargeLayout.jsx#L14>`_
(which you should be able to do `via dynamic configuration
<https://github.com/openedx/edx-platform/blob/open-release/olive.master/lms/djangoapps/mfe_config_api/docs/decisions/0001-mfe-config-api.rst>`_
in Olive) to add your logo to this page. There are also instructions for
installing a custom brand package in an MFE in the `tutor-mfe README
<https://github.com/overhangio/tutor-mfe#customising-mfes>`_. If you'd like to
revert to the legacy experience, running ``tutor config save --set
MFE_AUTHN_MFE_APP=null`` would be the simplest possible way, as instructed in
the `tutor-mfe README
<https://github.com/overhangio/tutor-mfe#customising-mfes>`_.

Other Small/Operational Changes
*******************************

* The `Molecular Structure Problem type
  <https://github.com/openedx/public-engineering/issues/14>`_ was removed.
* The Learning Micro front-end is now required and the legacy learner view has
  been deprecated. This means that if your instance hasn't been using the
  Learning MFE, it will now, and you may notice some slight visual changes.
* Grades are now persistent, meaning that they are stored in MySQL database
  tables for fast access and improved performance anywhere grades information
  exists. This has been optional since Hawthorn but is now required. For
  technical information about the upgrade, `visit this wiki page
  <https://openedx.atlassian.net/wiki/spaces/AC/pages/755171487/Migrating+to+Persistent+Grading>`_.
* Android app support is currently limited to `Release 3.0.2
  <https://github.com/openedx/edx-app-android/releases/tag/release%2F3.0.2https://github.com/openedx/edx-app-android/releases/tag/release%2F3.0.2>`_
  of the ``edx-android-app`` codebase. The only noticeable impact here is that
  there may be new features in the iOS app that are not in the older version of
  the Android release.
