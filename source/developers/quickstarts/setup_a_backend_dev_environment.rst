Quick Start: First Open edX Pull Request
########################################

Welcome to the Quickstart guide for new Open edX contributors. By the end of this tutorial, you will have completed all the steps necessary to begin contributing to the Open edX project. 

These include: 

* Setting up your development environment; 
* Making your first commit; 
* Submitting your first pull request (PR); 
* Signing your Contributor License Agreement (CLA). 

We assume you are comfortable with the command line, and understand the basics of using Git, GitHub, and so forth.

This Quickstart is written for first-time contributors to the Open edX project. If you are a plug-in developer or a developer, please see our Quickstart guide for plug-in developers <link coming soon> or our Quickstart for developers <link coming soon>.

System Requirements
*******************

For the smoothest experience, we recommend that your computer has at least 16 GB of RAM.

Before you start 
****************

This tutorial is written for users of Mac OS, either with an Intel or an Arm (Apple Silicone) processor. Additionally, you will need to have the following installed or configured, and know at least the basics of using them, before proceeding:

* Git & a GitHub account (see `GitHub's set up Git guide <https://help.github.com/en/github/getting-started-with-github/set-up-git>`_)

  * Additionally, we strongly recommend setting up 2-factor authentication

* SSH, so that you can provide your public key to a server (`GitHub's guides to setting up SSH <https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh>`_)
* Pip, the `Python Package Installer <https://pip.pypa.io/en/stable/installing/>`_ 
* venv, the `Python virtual environment system <https://docs.python.org/3/library/venv.html>`_
* Your favorite code editor (our team uses `VSCode <https://code.visualstudio.com/download>`_, Emacs `<https://emacsformacosx.com/>`_ or via homebrew, `Vim <https://github.com/macvim-dev/macvim>`_ or via homebrew, and others)

This tutorial assumes you have some experience with Python, and you are comfortable with using the command line.

Install Docker
**************

Install `Docker for Mac <https://docs.docker.com/docker-for-mac/>`_ and launch it. You can check that it is running correctly with::

    docker run --rm busybox true

On macOS, by default, Docker allocates at most 2 GB of RAM to containers; the Open edX software requires at least 8 GB. You should follow these instructions from the `official Docker documentation <https://docs.docker.com/docker-for-mac/#advanced>`_ to allocate at least 8 GB to the Docker daemon.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
END OF SARINA & JENNA'S SECTION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. contents:: Steps to Making your First Pull Request
   :local:
   :class: no-bullets


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

Get Tutor Working: `Tutor Developer Quickstart`_.

Because this was a practice PR, it will be closed without the changes being
accepted.  This is so others can continue to go through the same quickstart.

However for any real changes you make in the future, you can expect that the
reviewers will review your changes and may ask for changes or accept your
changes as is and merge them.

.. note::
   .. include:: /documentors/how-tos/reusable_content/sign_agreement.txt

If you need more help or run into issues, check out the :doc:`/other/getting_help`
section of the documentation for links to some places where you could get help.

Related Docs
************

.. _Tutor Developer Quickstart: https://docs.tutor.overhang.io/tutor.html
