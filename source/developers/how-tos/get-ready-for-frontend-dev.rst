How To Get Ready for Frontend Development
#########################################

.. How-tos should have a short introduction sentence that captures the user's goal and introduces the steps.

This how-to will help prepare your local system to start developing on an
:term:`MFE` that is part of the front-end of the Open edX Platform.

Assumptions
***********

.. This section should contain a bulleted list of assumptions you have of the
   person who is following the How-to.  The assumptions may link to other
   how-tos if possible.

* You know how to use Git
* You have the Open edX Legacy Devstack_ setup and the LMS is running.
* You are running Node 16.x.x

Steps
*****

.. note::

   Most :term:`MFEs<MFE>` will follow the steps defined here but we always recommend
   reviewing the README of an MFE as it will have more detailed instructions
   that are specific to the project.

#. Clone the repository locally.

   .. code-block::

      git clone <git_url>

#. Install the Node dependencies

   .. code-block::

      cd <repo_dir> && npm clean-install

#. Start the dev server

   .. code-block::

      npm start

.. seealso::

  :doc:`/developers/concepts/platform_overview`

.. _Devstack: https://edx.readthedocs.io/projects/open-edx-devstack/en/latest/
