Setup a BackEnd Dev Environment
###############################

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
   .. include:: ../how-tos/reusable_content/sign_agreement.txt

If you need more help or run into issues, check out the :doc:`/other/getting_help`
section of the documentation for links to some places where you could get help.
=======
===============================



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

.. code-bash:: bash

  pip install git+https://github.com/open-craft/tutor-contrib-arm64
  tutor plugins enable arm64
  tutor config save

Finally, let's configure and provision your Open edX instance!
You will be asked a couple questions.
Answer them however you like, although the default answers will work fine.

.. code-bash:: bash

  tutor dev quickstart

Depending on your system and your Internet connection speed,
this could take anywhere from five minutes to over an hour,
so go get a coffee and come back for the next part.





