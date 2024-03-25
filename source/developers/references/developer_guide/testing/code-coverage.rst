*************
Code Coverage
*************

We use a coverage tool to test on your pull request whether or not your changed
lines of code are _covered_ by unit tests. That means, for each line, is there a
unit test that tests out that line?

Unit testing is a software testing method where “units” — the individual
components of software—are tested. Developers write unit tests for their code to
make sure that the code works correctly. This helps to detect and protect
against bugs in the future.

The main objective of unit testing is to isolate written code to test and
determine if it works as intended. Unit testing is an important step in the
development process. If done correctly, unit tests can detect early flaws in
code and prevent future developers from breaking your feature by enforcing its
correct behavior.

In ``edx-platform``, coverage is run via `CodeCov
<https://about.codecov.io/resource/what-is-code-coverage/>`_ and you can see the
results of your Codecov by viewing the coverage builds:

.. image:: /_images/devguide_coverage_builds.png

Other repositories may use CodeCov or other coverage tools; check the builds on
your pull request, the repo's Makefile, or the repo's README for more detail. It
is your responsibility to make sure you provide adequete test coverage for all
changes you make.


