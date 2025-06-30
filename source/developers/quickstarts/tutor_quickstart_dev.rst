.. _Tutor QS (Dev):

Tutor Quickstart (Developer)
#############################

.. tags:: developer, quickstart

.. admonition:: tutor main vs tutor local

   ``tutor main`` should be used by developers when writing code for the
   master/main branches.

   ``tutor local`` should be used by site operators to deploy an Open edX
   instance. See :ref:`Tutor QS (Operator)` if you wish to deploy an Open edX
   instance.

   Also, it is helpful to first watch the video on the :ref:`Tutor Concept
   (Dev)` page before embarking on your Tutor journey.


Tutor was designed to make it easy for everyone to run the latest Open edX
release, either for development or production environments. In this Quickstart
we will walk you through how to set up Tutor Main for development on "master"
(the latest code being developed for the next named release). This Quickstart
walks through the basics of setting up Tutor for edx-platform development. For MFE development, you will want
to continue on to :ref:`Tutor for MFE QS`.

Requirements
*************

* Supported OS: Tutor runs on any 64-bit, UNIX-based OS. It has also been reported to
  work on Windows (with `WSL 2
  <https://docs.microsoft.com/en-us/windows/wsl/install>`__).
* Architecture: Both AMD64 and ARM64 are supported.
* Required software:

  * `Docker <https://docs.docker.com/engine/installation/>`__: v24.0.5+ (with BuildKit 0.11+)

  * `Docker Compose <https://docs.docker.com/compose/install/>`__: v2.0.0+ (installed by default with Docker Desktop)

.. warning::

    Do not attempt to simply run ``apt-get install docker docker-compose`` on older Ubuntu platforms,
    such as 16.04 (Xenial), as you will get older versions of these utilities.


* Hardware:

  * Minimum configuration: 4 GB RAM, 2 CPUs, 8 GB disk space
  *    Recommended configuration: 8 GB RAM, 4 CPUs, 25 GB disk space

.. note::

    On Mac OS, by default, containers are allocated 2 GB of RAM, which is not enough.
    You should follow `these instructions from the official Docker documentation <https://docs.docker.com/desktop/settings-and-maintenance/settings/#resources>`__
    to allocate at least 4-5 GB to the Docker daemon. If the deployment fails because
    of insufficient memory during database migrations, check the `relevant section in
    the troubleshooting guide <https://docs.tutor.edly.io/troubleshooting.html#migrations-killed>`_.

Set Up Tutor for Development
************************************


#. Fork the `edx-platform GitHub repo
   <https://github.com/openedx/edx-platform>`_ and clone it locally. Then run
   ``git switch master`` to ensure you are on the master branch. If you
   already have a fork, first sync it to the current upstream version.

#. Set up a `new virtual environment
   <https://docs.python.org/3/tutorial/venv.html>`_ for your Tutor environment
   and activate it:

   .. code-block:: bash

      python -m venv /path/to/new/virtual/environment
      source /path/to/new/virtual/environment/bin/activate

#. Follow the instructions to `install Tutor Main <https://docs.tutor.edly.io/tutorials/main.html>`_.

#. Follow the instructions to `have Tutor use your local fork
   <https://docs.tutor.edly.io/dev.html#first-time-setup>`_. Continue to follow
   the instructions to build the images and launch Tutor using ``tutor dev
   launch``.

#. Next, review the `common Tutor tasks
   <https://docs.tutor.edly.io/local.html#common-tasks>`_ for commands used to
   create superusers, import the "Open edX Demo Course", and set themes.

Congratulations! You are now running Tutor, on the master branch, in dev mode!

See the `Tutor tutorial about working on edx-platform`_ for more details on
what's going on behind the scenes.

.. seealso::

   :ref:`Tutor Concept (Dev)`

   :ref:`qs Dev First PR`

   `Tutor tutorial about working on edx-platform`_

   :ref:`Tutor for MFE QS`

.. _Tutor tutorial about working on edx-platform: https://docs.tutor.edly.io/tutorials/edx-platform.html

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+