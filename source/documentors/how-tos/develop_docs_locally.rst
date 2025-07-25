.. _Develop Docs Locally:

Develop Docs Locally
########################

.. tags:: documentor, how-to


If you are familiar with the basics of a local development environment, you can
set one up to develop documentation locally - that is, on your machine rather
than waiting for the automated build on GitHub.

Prerequisites
**************

In this How-To guide, we assume that you have the following:

* A Mac or Linux environment
* Familiarity with the command line (terminal application), or the desire to learn!

Set Up Your Environment
*************************

#. On a Mac, first install `homebrew <https://brew.sh/>`_ using the command line ("Terminal" application on a Mac)::

	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

#. Install Python, using the version specified in `.readthedocs.yaml <https://github.com/openedx/docs.openedx.org/blob/main/.readthedocs.yaml>`_::

	# On Mac
	brew install python3.12 # Insert proper version here

#. Install Git::

	# On Mac
	brew install git

#. Create a directory to hold your openedx code (I call it ``openedx`` but you
   can call it anything) and switch to that directory::

	mkdir openedx
	cd openedx

#. Create a new Virtualenv for docs development (I call it "vdocs.openedx.org",
   but you can use any name that makes sense to you)::

	python3.12 -m venv vdocs.openedx.org # Use proper Python version here
			
#. Activate the virtual environment::

	source vdocs.openedx.org/bin/activate

Writing Documentation Locally
******************************

#. Set up a local code editor. `VS code (download link)
   <https://code.visualstudio.com/download>`_ is recommended as it is easy to
   use.

#. Using the command line, clone the repo locally, into a directory you use to
   write Open edX code (for example, a directory called ``openedx``)::

	git clone git@github.com:openedx/docs.openedx.org.git

#. Set up your code editor to read from your ``openedx`` folder.

#. Write some docs!!

Build and Test Documentation Locally
************************************

#. First, ensure you are working within your docs virtual environment, and run the requirements script::

	  cd openedx # or the folder where you cloned the docs.openedx.org repo
     source vdocs.openedx.org/bin/activate
	  cd docs.openedx.org
	  make requirements


#. To build documentation, inside the root folder, run::

	make clean
	make html

#. Sphinx should build the HTML files locally. If there are errors, you will
   need to address them. Once the HTML successfully builds ("The HTML pages are
   in build/html."), To serve the docs locally, run::

		make serve_docs

Once this process is running, you can view the docs in your browser by
navigating to http://127.0.0.1:8000

Note: This is a background process, and it will continue updating the docs as you edit
them. However if you make substantive changes, you may need to kill the process
and run ``make clean``/ ``make html`` again. We're fortunate to have a lot of
docs - but this means that ``make html`` can take 3-4 minutes to run.

You should ensure the documentation builds with no errors or warnings when
submitting a pull request.

Making a Pull Request
**********************

Follow the :ref:`Process for Contributing Code`.

The `gh CLI tool <https://cli.github.com/>`_ is a great way to interact with
GitHub on the command line. You can also interact with GitHub via your code
editor (for example, `Using Git with VS Code
<https://code.visualstudio.com/docs/sourcecontrol/overview>`_).


.. seealso::

   :ref:`About Open edX Documentation Standards` (concept)

   :ref:`Add New Documentation via GitHub` (how-to)

   :ref:`Update an Existing Doc via GitHub` (how-to)

   :ref:`Make Changes to your Pull Request` (how-to)	

   :ref:`FAQ PR Process` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
