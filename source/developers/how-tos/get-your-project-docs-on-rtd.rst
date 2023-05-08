How-to get your repository docs on docs.openedx.org
###################################################

This how-to will help you publish the documentation for your Open edX Library or Service to ReadTheDocs.org under the https://docs.openedx.org domain.

Assumptions
***********

* You know how to build your repo's documentation locally. If not, see :doc:`/developers/how-tos/add-sphinx-docs-to-a-repo`

* Your repo's documentation is built using Sphinx

Steps
*****

.. A task should have 3 - 7 steps.  Tasks with more should be broken down into digestible chunks.

#. Add a .readthedocs.yml file in your repository that looks like the following.

   .. code-block:: yaml

      # .readthedocs.yml
      # Read the Docs configuration file
      # See https://docs.readthedocs.io/en/stable/config-file/v2.html for details
      
      # Required: the version of this file's schema.
      version: 2
      
      # Build documentation in the docs/ directory with Sphinx
      sphinx:
        configuration: docs/conf.py
        fail_on_warning: true
      
      # Set the version of python needed to build these docs.
      build:
        os: "ubuntu-22.04"
        tools:
          python: "3.8"
   
      # Optionally install extra requirements required to build your docs
      python:
        install:
        - requirements: requirements/doc.txt
   
#. File an `Axim Request <https://github.com/openedx/axim-engineering/issues/new/choose>`_ to add your docs to docs.openedx.org

   Sample request text:

   .. code-block:: text

      I'd like to have the documentation for the <url_to_repo> repository published 
      under docs.openedx.org.  Please enable publishing the docs as well as running
      test builds on pull requests for this repository.

#. Once the documentation is published you should update any READMEs and other
   links that need to point to this documentation. The new documetation will be
   published at a url like ``https://docs.openedx.org/projects/<repo_name>/``

.. Following the steps, you should add the result and any follow-up tasks needed.

.. seealso::

  `Debuging/Fixig Docs Builds <https://openedx.atlassian.net/wiki/spaces/DOC/pages/3014852990/Debugging+Fixing+Docs+and+Adding+Docs+CI>`_
        A guide to help you fix issues you might run into while setting documentation CI.

  :doc:`/developers/how-tos/add-sphinx-docs-to-a-repo`
        Add sphinx to a repository that doesn't already have it.
