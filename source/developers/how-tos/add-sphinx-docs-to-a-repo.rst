How To Add Sphinx Docs to a Repo
#################################

.. How-tos should have a short introduction sentence that captures the user's goal and introduces the steps.

This how-to will help you setup the basic skeleton for sphinx docs in your repo
in a manner that is standard to the Open edX Project.

Assumptions
***********

.. This section should contain a bulleted list of assumptions you have of the
   person who is following the How-to.  The assumptions may link to other
   how-tos if possible.

* You know how to use Git

* You are familiar enough with `make`_ to use it.

* You are familiar with `basic python development`_ (pip, virtualenvs, etc.)

.. _make: https://www.gnu.org/software/make/manual/html_node/index.html

.. _basic python development: https://docs.python.org/3/tutorial/index.html

Steps
*****

.. A task should have 3 - 7 steps.  Tasks with more should be broken down into digestible chunks.

#. Add a ``docs.in`` file in the ``requirements`` folder with the following content.


   .. code::

      # Requirements to build the documentation.
      -c constraints.txt

      sphinx
      sphinx-book-theme
      sphinx-copybutton
      sphinx-autobuild
      sphinxcontrib-mermaid
      sphinxcontrib-contentui

#. Add ``docs.in`` to the ``upgrade`` command in your ``Makefile``

#. Run ``make upgrade`` to generate ``requirements/docs.txt``

#. ``pip install -r requirements/docs.txt``

#. Make a ``docs`` folder at the root of your repo and ``cd`` into it.

   .. note::

      If you already have a docs repo with RST, move it aside for now, and you
      can move the RST files into the newly generated sphinx project once it has
      been setup.

   .. code::

      mkdir docs
      cd docs

#. Generate a basic sphinx doc skeleton.

   .. code::

      sphinx-quickstart --no-batchfile --extensions sphinxcontrib.contentui --extensions sphinx_copybutton --extensions sphinx.ext.graphviz --extensions sphinxcontrib.mermaid --no-sep -a "Open edX Community" -l "en" --release latest

#. Make sure the build works.

   .. code::

      make html

   This should generate an html file at ``_build/html/index.html``

#. Update the following settings in ``docs/conf.py``

   .. code::

      html_theme = 'sphinx_book_theme'

#. Add the following settings to ``docs/conf.py``

   .. note::

      You'll have to update at least the ``repository_url`` and
      ``repository_branch`` settings in ``html_theme_options`` but you should
      review the rest of the settings as well.


   .. code::

      import os

      html_theme_options = {

          "repository_url": TODO: Add a URL Here,
          "repository_branch": TODO: Add the correct branch here,
          "path_to_docs": "docs/",
          "use_repository_button": True,
          "use_issues_button": True,
          "use_edit_page_button": True,
          "extra_footer": """
              <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">
                  <img
                      alt="Creative Commons License"
                      style="border-width:0"
                      src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png">
              </a>
              <br>
              These works by
                  <a
                      xmlns:cc="https://creativecommons.org/ns#"
                      href="https://openedx.org"
                      property="cc:attributionName"
                      rel="cc:attributionURL"
                  >Axim Collaborative</a>
              are licensed under a
                  <a
                      rel="license"
                      href="https://creativecommons.org/licenses/by-sa/4.0/"
                  >Creative Commons Attribution-ShareAlike 4.0 International License</a>.
          """
      }

      # Note the logo won't show up properly yet because there is an upstream
      # bug in the theme that needs to be fixed first.
      # If you'd like you can temporarily copy the logo file to your `_static`
      # directory.
      html_logo = "https://logos.openedx.org/open-edx-logo-color.png"
      html_favicon = "https://logos.openedx.org/open-edx-favicon.ico"

      # Set the DJANGO_SETTINGS_MODULE if it's not set.
      if not os.environ.get('DJANGO_SETTINGS_MODULE'):
         os.environ['DJANGO_SETTINGS_MODULE'] = 'test_utils.test_settings'

#. Run the build again to make sure youve got the standard logos and footers
   setup.

   .. code::

      make html

#. Now that the basic build works you're ready to create the skeleton for
   documentation based on `diataxis`_.

   .. code::

      cd docs/
      mkdir -p {concepts,how-tos,quickstarts,references,decisions}
      touch {concepts,how-tos,quickstarts,references,decisions}/index.rst

#. Add a title to each index.rst

#. Start wiriting documentation!

.. seealso::

   :doc:`/documentors/references/quick_reference_rst`
      Basic syntax guidance for RST.

   `Diataxis`_
      The conceptual documentation system we're trying to follow.

   :doc:`/documentors/concepts/content_types`
      A quick summary on the different types of documents.

   :doc:`/developers/how-tos/get-your-project-docs-on-rtd`
      Once your docs are building, setup publishing and PR builds.

.. _diataxis: https://diataxis.fr
