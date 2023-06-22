How to Switch to the sphinx-book-theme for Documentation
########################################################

This how-to will help you switch from your existing Sphinx theme to the
sphinx-book-theme for a sphinx documentation project.

Assumptions
***********

.. This section should contain a bulleted list of assumptions you have of the
   person who is following the How-to.  The assumptions may link to other
   how-tos if possible.

* You already have a Sphinx documentation project.

* You know how to work with Python code.

Steps
*****

.. A task should have 3 - 7 steps.  Tasks with more should be broken down into digestible chunks.

#. Update and rebuild your requirements.

   #. Find the requirements file that has your documentation requirements in it.

      For most projects there will be a ``requirements/docs.in`` file which will
      contain your theme as a Python requirement.  For example if you are using
      the deprecated ``edx-sphinx-theme``, you'll see a line with that package
      name on it.

   #. Remove your old theme (for example, ``edx-sphinx-theme``) and add a line for the
      ``sphinx-book-theme``.

      .. code::

         - edx-sphinx-theme
         + sphinx-book-theme

   #. Run ``make upgrade``

   #. Install your doc requirements.

      .. code::

         pip install -r requirements/docs.txt # in most cases

#. Update conf.py

   Add or update the following
   .. code::

      import os

      html_theme_options = {

          "repository_url": TODO: Add a github URL Here, for example https://github.com/openedx/repo-name,
          "repository_branch": TODO: Add the correct branch, for example 'main',
          "path_to_docs": "docs/",
          "use_repository_button": True,
          "use_issues_button": True,
          "use_edit_page_button": True,
          # Please don't change unless you know what you're doing.
          "extra_footer": """
              <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">
                  <img
                      alt="Creative Commons License"
                      style="border-width:0"
                      src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png"/>
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
      # Only if your project has a dependency on Django
      if not os.environ.get('DJANGO_SETTINGS_MODULE'):
         # If you do depend on django you'll need a settings file that you can
         # use when building docs.  This will allow you to pull docstrings from
         # your code.
         os.environ['DJANGO_SETTINGS_MODULE'] = 'test_utils.test_settings'

#. Re-build your project and fix any errors.

   .. code::

      make html # and fix errors until there are no errors.

Once everything is building correctly without errors you should be all set to
make a pull request with your changes!

.. Following the steps, you should add the result and any follow-up tasks needed.

.. seealso::

  :doc:`add-sphinx-docs-to-a-repo`
