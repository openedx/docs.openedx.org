# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import re
import sys
import urllib
from datetime import datetime

# -- Project information -----------------------------------------------------

project = ""
current_year = datetime.utcnow().year
copyright = f"{current_year}, Axim Collaborative"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.youtube",
    "sphinxcontrib.images",
    "sphinx_design",
    "sphinxcontrib.contentui",
    "sphinx_copybutton",
    "sphinx.ext.graphviz",
    "sphinxcontrib.mermaid",
    "sphinx.ext.intersphinx",
    "sphinxext.rediraffe",
]

# Extension Configuration
graphviz_output_format = "svg"

rediraffe_redirects = {
    "community/release_notes/latest.rst": "community/release_notes/palm.rst",
}

# Intersphinx Extension Configuration
DIGITS_ONLY = r"^\d+$"
rtd_language = os.environ.get("READTHEDOCS_LANGUAGE", "en")
rtd_version = os.environ.get("READTHEDOCS_VERSION", "latest")
if re.search(DIGITS_ONLY, rtd_version):
    # This is a PR build, use the latest versions of the other repos.
    rtd_version = "latest"

intersphinx_mapping = {
    "DoneXBlock": (
        f"https://docs.openedx.org/projects/donexblock/{rtd_language}/{rtd_version}",
        None,
    ),
    "openedx-proposals": (
        # Not setting the version on purpose because we always want the latest version
        # of OEPs
        f"https://docs.openedx.org/projects/openedx-proposals/{rtd_language}/latest",
        None,
    ),
    "openedx-aspects": (
        f"https://docs.openedx.org/projects/openedx-aspects/{rtd_language}"
        f"/{rtd_version}",
        None,
    ),
    "edx-installing-configuring-and-running": (
        f"https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/{rtd_language}/{rtd_version}",
        None,
    ),
    "edx-platform": (
        f"https://docs.openedx.org/projects/edx-platform/{rtd_language}/{rtd_version}",
        None,
    ),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'edx_theme'
# html_theme_path = [edx_theme.get_html_theme_path()]
# html_favicon = os.path.join(html_theme_path[0], 'edx_theme', 'static', 'css', 'favicon.ico')

html_theme = "sphinx_book_theme"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

images_config = {
    "default_image_width": "60%",
}

rst_epilog = """

.. raw:: html

  <hr/>

.. rst-class:: feedback

  :ref:`Feedback <Documentation Feedback Form>`

.. include:: /substitutions.txt
.. include:: /links.txt

"""


html_sidebars = {}

panels_add_bootstrap_css = False

# For custom styles

html_theme_options = {
    "repository_url": "https://github.com/openedx/docs.openedx.org",
    "repository_branch": "main",
    "path_to_docs": "source",
    "primary_sidebar_end": "primary_sidebar_end",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "navigation_with_keys": False,
    # "announcement": "",
}


html_logo = "_static/open-edx-logo-color.png"
html_favicon = "https://logos.openedx.org/open-edx-favicon.ico"
release = "Latest"

html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
]

html_js_files = [
    "_js/custom.js",
]

togglebutton_hint = "Show"
togglebutton_hint_hide = "Hide"
