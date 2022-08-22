Quick Start: First Open edX Pull Request
########################################

.. contents:: Steps to Making your First Pull Request
   :local:
   :class: no-bullets

Welcome to the Quickstart guide for new Open edX contributors. By the end of
this tutorial, you will have completed all the steps necessary to begin
contributing to the Open edX project.

These include: 

* Setting up your development environment; 
* Making your first commit; 
* Submitting your first pull request (PR); 
* Signing your Contributor License Agreement (CLA). 

We assume you are comfortable with the command line, and understand the basics
of using Git, GitHub, and so forth.

This Quickstart is written for first-time contributors to the Open edX project.
If you are a plug-in developer or a frontend developer, please see our
Quickstart guide for plug-in developers <link coming soon> or our Quickstart for
frontend developers <link coming soon>.

System Requirements
*******************

For the smoothest experience, we recommend that your computer has at least 16 GB
of RAM, 2 CPUs, and a disk image of 96 GB.

Before you start 
****************

This tutorial is written for users of Mac OS, either with an Intel or an Arm
(Apple Silicone) processor. Additionally, you will need to have the following
installed or configured, and know at least the basics of using them, before
proceeding:

* A `GitHub account <https://github.com/signup>`_
* Git (see `GitHub's set up Git guide
  <https://help.github.com/en/github/getting-started-with-github/set-up-git>`_)

  * Additionally, we strongly recommend setting up 2-factor authentication

* SSH, so that you can provide your public key to a server (`GitHub's guides to
  setting up SSH
  <https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh>`_)
* Pip, the `Python Package Installer
  <https://pip.pypa.io/en/stable/installing/>`_
* venv, the `Python virtual environment system
  <https://docs.python.org/3/library/venv.html>`_
* Your favorite code editor (our team uses `VSCode
  <https://code.visualstudio.com/download>`_, Emacs
  `<https://emacsformacosx.com/>`_ or via `homebrew <https://brew.sh/>`_, `Vim
  <https://github.com/macvim-dev/macvim>`_ or via homebrew, and others)

This tutorial assumes you have some experience with Python, and you are
comfortable with using the command line.

Install Docker
**************

Install `Docker for Mac <https://docs.docker.com/docker-for-mac/>`_ and launch
it. You can check that it is running correctly with::

    docker run --rm busybox true

On macOS, by default, Docker allocates at most 2 GB of RAM to containers; the
Open edX software requires at least 8 GB. You should follow these instructions
from the `official Docker documentation
<https://docs.docker.com/docker-for-mac/#advanced>`_ to allocate at least 8 GB
to the Docker daemon.


Installing Tutor Nightly
************************

Navigate into a folder to hold your Open edX repositories.
We will assume you're using ``~/openedx``, but you can choose any folder.

.. code-block:: bash

  mkdir -p ~/openedx
  cd ~/openedx

Create a Python 3.8 virtual environment (we'll call it ``tutor-venv``) and activate it:

.. code-block:: bash

  python3.8 -m venv tutor-venv
  . tutor-venv/bin/activate

Install Tutor. This is a tool that helps you run Open edX.
We will install the "Nightly" version of Tutor, which means it will run the latest
version of Open edX (as opposed to the stable version of Open edX):

.. code-block:: bash

  git clone --branch=nightly https://github.com/overhangio/tutor.git
  pip install -e "./tutor[full]"

If you are using ARM-64, then install this extra plugin and enable it
(if you're not, then skip this step):

.. code-block:: bash

  pip install git+https://github.com/open-craft/tutor-contrib-arm64
  tutor plugins enable arm64
  tutor config save

Finally, let's configure and provision your Open edX instance!
You will be asked a couple questions.
Answer them however you like, although the default answers will work fine.

.. code-block:: bash

  tutor dev quickstart

Depending on your system and your Internet connection speed,
this could take anywhere from five minutes to over an hour,
so go get a coffee and come back for the next part.


Working with a fork
*******************

At this point you should have a Tutor installation that is suitable for
development, but you're still missing a practical way to edit the code, test
it locally, and then contribute it back.

For the purposes of this tutorial, you'll be modifying code in the
``_edx-platform`` repository, where the Open edX backend code lives.  Let's
start by creating your own personal "fork" of it.

**What's a fork?**

In GitHub terminology, a fork is is simply a copy of the original repository,
but one that you can make changes to without affecting the original codebase.
The point is to be free to make and save changes at your leisure, until they're
ready for contribution.

Open edX will accept contributions that use a specific Github fork workflow.
You will need to:

1. Fork the original repository (in this case, ``edx-platform``) into your
   personal Github account;
2. Clone the forked repository locally;
3. Create a new git branch for the change you'll be making (also known as a
   "feature branch");
4. Create, test and commit your changes to this branch locally;
5. Push the local branch to your forked repository on Github;
6. Make a pull request ("PR") against the original repository, or "upstream",
   from the feature branch on your fork.

The maintainer team responsible for the repository can then review your PR, and
then either accept it outright, or request you make changes to it.

**Forking edx-platform**

Assuming you're logged in to Github, forking a repository is easy.  Visit the
``edx-platform`` repository at this URL:

https://github.com/openedx/edx-platform

Now, click the :guilabel:`Fork` button on the top right, and in the next
screen, select your personal account as the owner.  After you click the
:guilabel:`Create fork` button, you'll be taken to your own version of the
``edx-platform`` repository.

**Cloning your fork**

Your ``edx-platform`` currently only exists in the Github servers.  You'll now
create a local copy of it (a "clone").

First, fetch the git URL of your fork.  Navigate to its web page (to which you
were taken after creation), click on the :guilabel:`Code` button, select
the **SSH** tab, and copy the URL given.  It should look like this:

``git@github.com:<your_github_username>/edx-platform.git``

Now, from the same top level directory you created above, clone the repository
as follows:

.. code-block:: bash

   cd ~/openedx
   git clone git@github.com:<your_github_username>/edx-platform.git

You'll now have an ``edx-platform`` directory containing a local clone of your
fork.  It is not yet wired into your Tutor development environment, though.
This is what you'll do next.

**Mounting edx-platform**

To have Tutor run your local fork of edx-platform, you have to tell it to do so
on start up.  It is a simple CLI parameter that points Tutor to the directory where
the code lives.  First, make sure to stop the running dev environment, though:

.. code-block:: bash

   tutor dev stop
   tutor dev start --mount=~/openedx/edx-platform lms

From this point on, whatever changes you make to the code in your clone
should be visible in your local instance.

Exercise: Update the Learner Dashboard
**************************************

The Learner Dashboard is the first page that students will see when they log
into Open edX. On our Tutor dev environment, it is located at
``http://local.overhang.io:8000/dashboard``

.. image:: /_images/developers_quickstart_first_pr/learner_dashboard_before.png
   :alt: Learner Dashboard page without any of our changes.

As an exercise, we're going to make a small edit to the top of this page. This
is not a change that we'd really merge, but it will demonstrate the steps we'd
have to go through to make a real change.

Edit the Template
=================

The template file for this page is at ``lms/templates/dashboard.html``. We're
going to add a simple welcome message to the ``dashboard-notifications`` div::

    <div class="dashboard-notifications" tabindex="-1">
        <!-- start new content -->
        
        Welcome to your dashboard!
        
        <!-- end new content -->

Feel free to replace the welcome text with any message you'd like and save the
file. When you reload it in your browser, you should see something like this:

.. image:: /_images/developers_quickstart_first_pr/learner_dashboard_after.png
   :alt: Learner Dashboard page without any of our changes.

Make a Commit
=============

Now that you've saved your changes, you can make a commit. Open edX commit
messages should follow our `conventional commit <https://open-edx-proposals.readthedocs.io/en/latest/best-practices/oep-0051-bp-conventional-commits.html>`_
practices. In our case, we're making a new feature, so our commit message must
be prefixed with "feat:" like so::

    commit -a -m "feat: add welcome message to learner dashboard"

Push the Commit to Your Fork
============================

Now push your changes to a new branch in your fork::

    git push --set-upstream origin <github_username>/quickstart

Create A Pull Request
*********************

Branch Name: <github_username>/quickstart

# Go to your fork.

``https://github.com/<your_github_username>/edx-platform``

At the top of the page you'll see a section that will suggest that you make a
new pull request.  Go ahead an click the big green button.

.. Screenshot of the root page with make a PR highlighted.

This will bring up a form which you don't need to make any changes in for now.
Go ahead hit "Create Pull Request" again.

.. Screenshot of the Create PR Page

Congratulations, you have made a new pull request for a change against the
Open edX documentation!

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

If you need more help or run into issues, check out the :doc:`/other/getting_help`
section of the documentation for links to some places where you could get help.
