How to Set Up Github Action to Monitor Python Coverage
######################################################

Most of our public repos use `CodeCov`_ to track our coverage, which is a separate service that can show how a particular commit changes the impact of an individual PR on the overall coverage of a repository. But sometimes, we do not want to use a separate service, because the particular repository is private or for some other reason.

For Python repositories in these cases, we recommend using a GitHub action called `python-coverage-comment`_.


.. _CodeCov: https://codecov.io
.. _python-coverage-comment: https://github.com/py-cov-action/python-coverage-comment-action


Features of the Action
**********************

This action will add a comment to PRs indicating how the current PR will affect coverage and how much of the current PR's lines have been covered.

It will also create a branch to track the coverage of the default branch over time. This branch will also contain generated coverage HTML reports of the default branch.

Setting Up a Repository
***********************

To enable this action you will need to do a few steps:

1. Add the ``coverage`` library as a dependency to ``ci.in``. By default, we do not install this via cookiecutters.
2. Add the setting ``relative_files = True`` to ``.coveragerc``
3. Replace the ``codecov`` action in the ``ci.yml`` workflow, following `the GitHub action's README`_ for details on how to do the setup.
   a. Ensure that the permissions for the ``ci.yml`` workflow are correct.
4. Follow the README's instructions to add a ``coverage.yml`` workflow next.


More information and details can be found in `the GitHub action's README`_.

.. _the GitHub action's README: https://github.com/py-cov-action/python-coverage-comment-action/blob/v3/README.md
