ReadMe
######

We're so happy you're here! We welcome contributions of all kinds, particularly issues and pull requests. Please read on for instructions on how to participate.

About This Repository
*********************

This repository contains source files for the `Open edX Documentation`_ site. This repository is managed by the Open edX documentation working group, and maintained by the ``docs-openedx-org-maintainers`` GitHub group.

The `Open edX Documentation`_ site contains documentation for:

* Educators
* Learners
* Site Operators
* Developers

Documentation for other components of the Open edX ecosystem is found in each component's repository.
When known, links to other documentation are provided in the `Open edX Documentation`_.

Submit Documentation Issues
***************************

We welcome input from the community on Open edX documentation.  You can report a problem or suggest an improvement to the documentation issues by `following the Report a Problem instructions <https://docs.openedx.org/en/latest/documentors/how-tos/report_problem_with_docs.html>`_.

Contribute to Open edX Documentation
************************************

You, the user community, can help update and revise Open edX documentation!

Open edX documentation is published from `RST`_ source files using `Sphinx`_.

Here are some resources for getting started:

* `First docs PR using the GitHub UI <https://docs.openedx.org/en/latest/documentors/quickstarts/first_documentation_pr.html>`_
* `Update existing docs through GitHub <https://docs.openedx.org/en/latest/documentors/quickstarts/update_doc_via_github.html>`_
* `Add new documentation through GitHub <https://docs.openedx.org/en/latest/documentors/quickstarts/quick_start_add_doc.html>`_
* More resources available at the `Documentors Homepage <https://docs.openedx.org/en/latest/documentors/index.html>`_

Propose Changes While Viewing Documentation
*******************************************

While viewing documentation, you can easily propose a change by selecting **suggest edit** from the menu under the GitHub icon.
The page you are viewing then opens in GitHub, in edit mode. When you save your edits, create a new branch, commit your changes,
and create a new Pull Request, to have your changes reviewed by the Open edX team.

Build and Test Documentation Locally
************************************

For developers comfortable pulling down the repository locally and making changes (see `GitHub Flow`_), you can build the documentation directly on your machine.

To build documentation, inside the root folder, run:

.. code-block:: bash

    make clean
    make html

Sphinx should build the HTML files locally. To serve the docs locally, run

.. code-block:: bash

    make serve_docs

This is a background process, and it will continue updating the docs as you edit them. However if you make substantive changes, you may need to kill the process and run ``make clean``/``make html`` again. Unfortuantely this is a big project and ``make html`` can take 3-4 minutes to run.

You should ensure the documentation builds with no errors or warnings when submitting a pull request.

.. _Open edX Documentation: https://docs.openedx.org/
.. _GitHub repository: https://github.com/openedx/docs.openedx.org
.. _RST: https://en.wikipedia.org/wiki/ReStructuredText
.. _Sphinx: https://www.sphinx-doc.org/
.. _GitHub Flow: https://docs.github.com/en/get-started/using-github/github-flow
