ReadMe
######

This repository contains source files for the `Open edX Documentation`_ site. This repository is managed by the Open edX team.

The `Open edX Documentation`_ site contains complete documentation for:

* Educators
* Site Operators
* Developers

Documentation for other components of the Open edX ecosystem is found in each component's repository.
When known, links to other documentation are provided in the `Open edX Documentation`_.

Submit Documentation Issues
***************************

We welcome input from the community on Open edX documentation.  You can submit documentation issues in the `GitHub repository`_.

Contribute to Open edX Documentation
************************************

You, the user community, can help update and revise Open edX documentation.

Open edX documentation is published from `RST`_ source files using `Sphinx`_.

To suggest a revision, create a new branch, make changes, and submit a pull request: this is known as the `GitHub Flow`_.

Propose Changes While Viewing Documentation
*******************************************

While viewing documentation, you can easily propose a change by selecting **suggest edit** from the menu under the GitHub icon.
The page you are viewing then opens in GitHub, in edit mode. When you save your edits, create a new branch, commit your changes,
and create a new Pull Request, to have your changes reviewed by the Open edX team.

Build and Test Documentation
****************************

To build documentation, inside the root folder, run:

.. code-block:: bash

    make html

Sphinx should build the HTML files locally.

You should ensure the documentation builds with no errors or warnings when submitting a pull request.

.. _Open edX Documentation: https://docs.openedx.org/
.. _GitHub repository: https://github.com/openedx/docs.openedx.org
.. _RST: https://en.wikipedia.org/wiki/ReStructuredText
.. _Sphinx: https://www.sphinx-doc.org/
.. _GitHub Flow: https://docs.github.com/get-started/quickstart/github-flow
