*******
Testing
*******

Testing is something that we take very seriously within the Open edX project. We
maintain two kinds of tests: unit tests and integration tests.

Overall, you want to write the tests that maximize coverage while minimizing
maintenance. In practice, this usually means investing heavily in unit tests,
which tend to be the most robust to changes in the code base. Integration
tests, being more expensive to write and run, should be used more sparingly.

Different repositories may have different ways of defining and/or running tests.
Check out the repo documentation for more information.

.. toctree::
    :maxdepth: 2

    browsers
    github-actions
    code-coverage
    code-quality
