.. _qs Dev First PR:

Quick Start: First Open edX Pull Request
########################################

.. tags:: developer, quickstart

.. contents:: Steps to Making your First Pull Request
   :local:
   :class: no-bullets

Welcome to the Quickstart guide for new Open edX contributors. 

This tutorial is focused on teaching you how to make a noticeable
change to the platform equivalent to a "hello world" exercise.

By the end of this tutorial, you will have completed all the steps
necessary to begin contributing to the Open edX project.

These include:

* Setting up your development environment;
* Making your first commit;
* Submitting your first pull request (PR);
* :ref:`Signing your Contributor License Agreement (CLA) <Signing CLA>`

We assume you are comfortable with the command line, and understand the basics
of using Git, GitHub, Docker, and python basics.

.. This Quickstart is written for first-time contributors to the Open edX project.
   If you are a plug-in developer or a frontend developer, please see our
   :doc:`Quickstart guide for plug-in developers <setup_a_plugin_dev_environment>`
   or our :doc:`Quickstart for frontend developers <setup_an_mfe_dev_environment>`.

.. contents::
 :local:
 :depth: 1

Before you start
****************

.. admonition:: System Requirements

   For the smoothest experience, we recommend that your computer has at least
   **16 GB of RAM, 2 CPUs, and at least 50 GB of Free disk space**.

This tutorial is written for users of macOS or Linux.
It has been tested with both common 64-bit processor families:
x86-64 (a.k.a. Intel-64) and ARM-64 (used in newer Apple laptops, including M1, M2, etc.).
Additionally,
you will need to have the following installed or configured, and know at least
the basics of using them, before proceeding:

* Git (see `GitHub's set up Git guide
  <https://help.github.com/en/github/getting-started-with-github/set-up-git>`_)

* A `GitHub account <https://github.com/signup>`_

  * Additionally, we strongly recommend setting up 2-factor authentication.

* `Python 3.11 <https://www.python.org/downloads/>`_

* Your favorite code editor (our team uses
  `VSCode <https://code.visualstudio.com/download>`_,
  `Emacs for Mac OS X <https://emacsformacosx.com/>`_,
  `NeoVim <https://neovim.io/>`_,
  `MacVim <https://github.com/macvim-dev/macvim>`_,
  and others)

.. _homebrew: https://brew.sh

Install Docker
**************

Install `Docker Desktop <https://docs.docker.com/desktop/>`_ and launch
it. You can check that it is running correctly with::

    docker run --rm hello-world

You should see a message that starts with the following::

   Hello from Docker!
   This message shows that your installation appears to be working correctly.

On macOS, by default, Docker allocates at most 2 GB of RAM to containers; the
Open edX software requires at least 8 GB. macOS users should follow these instructions
from the `official Docker documentation
<https://docs.docker.com/docker-for-mac/#advanced>`_ to allocate at least 8 GB
to the Docker daemon.


Installing Tutor Main
************************

Tutor main is the best solution for using Tutor as your development
environment and tracking the bleeding edge of the Open edX platform
code.

Follow the official instructions for installing Tutor Main.

.. admonition:: Use Virtual Environments

   The Tutor documents will recommend this as well, but please do
   yourself the favor of using python virtual enviroments.  Doing so
   will make managing multiple repositories and dependency versions
   much easier.

`Official Tutor tutorial <https://docs.tutor.edly.io/tutorials/main.html#running-open-edx-on-the-master-branch-tutor-main>`_


Working with a fork
*******************

At this point you should have a Tutor installation that is suitable for
development, but you're still missing a practical way to edit the code, test
it locally, and then contribute it back.

For the purposes of this tutorial, you'll be modifying code in the
``edx-platform`` repository, where the Open edX backend code lives.  Let's
start by creating your own personal "fork" of it. A "fork" is essentially your
own copy of the repository. `See here <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_ to learn more about forks.

Forking edx-platform
====================

Assuming you're logged in to GitHub, forking a repository is easy.  Visit the
``edx-platform`` repository at this URL:

https://github.com/openedx/edx-platform

Now, click the :guilabel:`Fork` button on the top right, and in the next
screen, select your personal account as the owner.  After you click the
:guilabel:`Create fork` button, you'll be taken to your own version of the
``edx-platform`` repository.

Cloning your fork
=================

Your ``edx-platform`` currently only exists on the GitHub servers.  You'll now
create a local copy of it (a "clone").

First, fetch the git URL of your fork.  Navigate to its web page (to which you
were taken after creation), click on the :guilabel:`Code` button, select
the **HTTPS** tab, and copy the URL given.  It should look like this::

   https://github.com:<your_github_username>/edx-platform.git

Now, from the same top level directory you created above, clone the repository
as follows:

.. code-block:: bash

   cd ~/openedx
   git clone  https://github.com:<your_github_username>/edx-platform.git

You'll now have an ``edx-platform`` directory containing a local clone of your
fork.  It is not yet wired into your Tutor development environment, though.
This is what you'll do next.

Mounting edx-platform
=====================

To have Tutor run your local fork of edx-platform, you have to tell it to do so
on start up.  It is a simple CLI parameter that points Tutor to the directory where
the code lives.

To set up your local enviroment to update edx-platform, follow the
`official instructions
<https://docs.tutor.edly.io/tutorials/edx-platform.html>`_

From this point on, whatever changes you make to the code in your clone should
be visible in your local LMS instance immediately.

Working with an MFE
===================

Most of the Open edX platform's frontends have migrated from backend
Django templates to microfrontends based on the React framework
(MFEs).  If you are interested in updating frontend code, MFEs are
probably where you want to focus.  There are different ways of
configuring your development environment, but a common one is to use
Tutor to serve the backend services and run your MFE locally using npm
dev start.

To run MFEs in Tutor requires enabling a plugin, Tutor MFE.

Start by verifying that the mfe plugin is installed and enabled

.. code-block:: bash

   (tutor-main) $ tutor plugins list
   
   NAME         STATUS          VERSION
   discovery    installed       19.0.0
   forum        installed       19.0.0
   indigo       ✅ enabled      19.0.1
   jupyter      installed       19.0.0
   mfe          ✅ enabled      19.0.0

If ``mfe`` isn't enabled run the following command to do so

.. code-block:: bash

   (tutor-main) $ tutor plugins enable mfe
   (tutor-main) $ tutor dev stop
   (tutor-main) $ tutor dev launch

Once Tutor has restarted with the ``mfe`` plugin enabled you will see a few more URLs listed.

.. code-block:: bash

   http://apps.local.openedx.io:1984/communications
   http://apps.local.openedx.io:1990/learner-record
   http://apps.local.openedx.io:1993/ora-grading
   http://apps.local.openedx.io:1994/gradebook
   http://apps.local.openedx.io:1995/profile
   http://apps.local.openedx.io:1996/learner-dashboard
   http://apps.local.openedx.io:1997/account
   http://apps.local.openedx.io:2000/learning
   http://apps.local.openedx.io:2002/discussions

These ports and paths are to specific MFEs made available via the MFE plugin.

In order to develop locally, you will need to fork and clone the MFE
repository as you did for edx-platform, bind mount the directory, stop
the Tutor-hosted MFE and start a local npm dev server.  Let's do so
with the Learner Dashboard MFE.

First, you should verify that the learner dashboard is working
correctly after you have installed the MFE plugin.  Assuming
everything is configured in the standard way, your URL should be
``http://apps.local.openedx.io:1996/learner-dashboard/``

Follow the same, fork, clone workflow described above and clone the
learner-dashboard
``https://github.com/openedx/frontend-app-learner-dashboard``
repository locally.

Add a tutor mount for your cloned directory.

.. code-block:: bash

   (tutor-main) $ tutor mounts add /home/git/frontend-app-learner-dashboard

Next, ensure that the learner-dashboard MFE is stopped

.. code-block:: bash

   (tutor-main) $ tutor dev stop learner-dashboard

Reloading the learner dashboard page in the browser should now yield an error.

Now its time to replace the default Tutor-hosted learner-dashboard with a
local version.  That version will use a dev config file to connect to
the Tutor-hosted backend and to bind to the expected port.

.. admonition:: Local MFE Support and npm dev Profiles

   Not every MFE currently has an ``npm run dev`` command that will
   work with Tutor, though it is possible to create one if that is the
   case for the MFE you are developing, , using `an existing one
   <https://github.com/openedx/frontend-app-learner-dashboard/pull/530/files>`_
   as a template.

From the directory containing the local copy of the learner-dashboard
repository start the npm dev server.

.. code-block:: bash

   (tutor-main) $ npm run dev

Exercise: Update the Learner Dashboard
**************************************

The Learner Dashboard is the first page that students will see after they log
into Open edX.

The dashboard page will either be provided by a legacy server side template or by the learner-dashboard MFE.  Working with the MFE is usually the best choice.  Note that this tutorial is simplistic and appropriate to get started.  However, we don't recommend forking an MFE to customize it.  For extensive modifications, that might be necessary, but for simple things using design tokens and frontend plugin slots will be a much better alternative.

Working with the Learner Dashboard MFE
======================================



Working with the Legacy Learner Dashboard
=========================================
On our Tutor dev environment, it is located at
``http://local.openedx.io:8000/dashboard``

.. image:: /_images/developers_quickstarts/learner_dashboard_before.png
   :alt: Learner Dashboard page without any of our changes.

As an exercise, you're going to make a small edit to the top of this page. This
is not a change that will be merged upstream, but it will demonstrate the
steps you will have to go through to make a real change.

Edit the Template
-----------------

The template file for this page is at ``lms/templates/dashboard.html``. We're
going to add a simple welcome message to the ``dashboard-notifications`` div::

    <div class="dashboard-notifications" tabindex="-1">
        <!-- start new content -->

        Welcome to your dashboard!

        <!-- end new content -->

Feel free to replace the welcome text with any message you'd like and save the
file. When you reload it in your browser, you should see something like this:

.. image:: /_images/developers_quickstarts/learner_dashboard_after.png
   :alt: Learner Dashboard page after we add the welcome message.

Standard Operating Procedure For Backend or Frontend Changes
============================================================

Make a Commit
-------------

Now that you've saved your changes, you can make a commit. First make a new
branch with the name ``developer_quickstart``::

    git checkout -b developer_quickstart

Then we can create the actual commit. Note that Open edX commit messages should
follow :doc:`openedx-proposals:best-practices/oep-0051-bp-conventional-commits`
practices. In our case, we're making a new feature, so our commit message must
be prefixed with "feat:" like so::

    commit -a -m "feat: add welcome message to learner dashboard"

Push the Commit to Your Fork
----------------------------

Now push your changes to a new branch in your fork::

    git push --set-upstream origin developer_quickstart

If you get a ``fatal: Authentication failed`` error, authenticate Git Hub by running::

   gh auth login

`Learn more about authentication <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github#about-authentication-to-github>`_.


Create A Pull Request
---------------------

Go to your fork.

``https://github.com/<your_github_username>/edx-platform``

At the top of the page you'll see a section that will suggest that you make a
new pull request.  Go ahead and click the big green button.

.. image:: /_images/developers_quickstarts/new_pull_request_suggestion.png
   :alt: Screenshot of the Review and Create Pull Request button.

This will bring up a form which you don't need to make any changes in for now.
Go ahead hit "Create Pull Request" again.

.. image:: /_images/developers_quickstarts/pull_request_form.png
   :alt: Screenshot of the Pull Request Form with "Create Pull Request" highlighted.

Congratulations, you have made a new pull request for a change against the
Open edX project!

.. image:: /_images/animated_confetti.gif
   :alt: Animated confetti.
   :target: https://commons.wikimedia.org/wiki/File:Wikipedia20_animated_Confetti.gif


Because this was a practice PR, it will be closed without the changes being
accepted.  This is so others can continue to go through the same quickstart.

However for any real changes you make in the future, you can expect that the
reviewers will review your changes and may ask for changes or accept your
changes as is and merge them.

.. note::
   .. include:: /documentors/how-tos/reusable_content/sign_agreement.txt

If you are now looking for something to work on, please see :ref:`qs Dev Contributing`.

If you need more help or run into issues, check out the :ref:`Getting Help with Open edX`
section of the documentation for links to some places where you could get help.

.. seealso::

   :ref:`qs Dev Contributing` (Quickstart)

   :ref:`Open edX Developer's Guide` (Reference)

   `Intro to the Open edX Project & Contributing <https://training.openedx.io/courses/course-v1:OpenedX+OEX101+2023/about>`_ (Training Course)

   `Open edX Developer Onboarding <https://training.openedx.io/courses/course-v1:OpenedX+OEX-Dev101+2024/about>`_ (Training Course)

**Maintenance Chart**

+--------------+-------------------------------+-----------------------------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release                         |Test situation                  |
+--------------+-------------------------------+-----------------------------------+--------------------------------+
| 2025-03-19   | e0d (Ed Zarecor)              | master/main, on Tutor dev locally | Pass                           |
+--------------+-------------------------------+-----------------------------------+--------------------------------+
