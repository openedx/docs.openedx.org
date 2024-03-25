*****************
Landing Your Work
*****************

Once you're ready to submit your code changes in a pull request, check the following
requirements to be sure that your pull request is ready to be reviewed:

---------------------
Describe your changes
---------------------

Prepare a detailed pull request description. Most repositories have a template
to be followed when you open the PR in the GitHub UI. Please fill out that template
with as much detail as possible, including links to any roadmap tickets or
forum discussions as well as screenshots or screencasts (not everyone reviewing
your changes is a developer).

The code should be clear and understandable. Comments in code, detailed
docstrings, and good variable naming conventions are expected. See the
:doc:`../style_guides/index` for more details.

Commit messages should conform to `OEP-51: Conventional Commits`_.
This style categorizes commits to make them easier to understand.

----------------
Limit your scope
----------------

The pull request should be as small as possible. Each pull request should
encompass only one idea: one bug fix, one feature, etc. Multiple features
(or multiple bug fixes) should not be bundled into one pull request. A
handful of small pull requests is much better than one large pull request.

Structure your pull request into logical commits. “Fixup” commits
should be squashed together. The best pull requests contain only a
single, logical change - which means only a single, logical
commit. You can squash your own commits, or the person merging the
pull request may choose to squash them.
They will do so by using the Squash and merge button of
the GitHub interface to preserve the logical commits in the pull
request, for forensic purposes when trying to diagnose a regression
or understand a bug.

The pull request should integrate with existing infrastructure as much as
possible, rather than reinventing the wheel. In a project as large as ours,
there are many foundational components that might be hard to find.
It is important not to duplicate functionality, even if small, that already
exists. Posting in the `forums`_ is an easy way to find out if functionality
you're looking for already exists.

---------
Licensing
---------

All code in the pull request must be compatible with the Open edX project's
AGPL license.  This means that the author of the pull request must sign a
`contributor's agreement`_ (or be covered by their employer's agreement),
and all libraries included or referenced in the pull request must have
`compatible licenses`_.

-------
Testing
-------

All of the tests must pass. You'll see the checks that are being run on the
bottom of your PR; they must be green. More information can be found on the
:doc:`/developers/references/running_pr_tests` page.

If a pull request contains a new feature, it
should also contain new tests for that feature. If the pull request fixes a
bug, it should also contain tests for that bug to be sure that it stays
fixed. GitHub actions will verify this for your pull request, and point out
any failing tests.

The author of the pull request should provide a test plan for manually
verifying the change in this pull request. The test plan should include
details of what should be checked, how to check it, and what the correct
behavior should be. When it makes sense to do so, a good test plan includes
a tarball of a small test course that has a unit which triggers the bug
or illustrates the new feature.

For pull requests that make changes to the user interface, please include
screenshots of what you changed. GitHub will allow you to upload images
directly from your computer. Changes should only use elements from the
`Paragon pattern library`_.

-----------
Code Review
-----------

The author of the pull request should be receptive to feedback and
constructive criticism. The pull request will not be accepted until all
feedback from reviewers is addressed. Once a core committer has reviewed a
pull request from a contributor, no further review is required from the core
committer until the contributor has addressed all of the core committer's
feedback: either making changes to the pull request, or adding another
comment explaining why the contributor has chosen not make any change based
on that feedback.

While your pull request is open, you may have questions about how things are
going, or how to check in on the progress of your review. We've prepared a
:doc:`FAQ-about-pull-requests` that should answer most of your questions.

It's also important to realize that you and the core committers may have
different ideas of what is important in the codebase. The power and freedom of
open source software comes from the fact that you can fork our software and
make any modifications that you like without permission from us. However, the
core contributors are similarly empowered and free to decide what modifications
to pull in from other contributors, and what not to pull in. While your code
might work great for you on your installation, it might not work as well on
a large installation, have problems with performance or security, not be
compatible with internationalization or accessibility guidelines, and so on.
There are many, many reasons why the core committers may decide not to accept
your pull request, even for reasons that are unrelated to the quality of your
code change. However, if we do reject your pull request, we will explain why we
aren't taking it, and try to suggest other ways that you can accomplish the
same result in a way that we will accept.

Further Information
-------------------

For further information on the pull request requirements, please see the
following links:

* :doc:`code-considerations`
* :doc:`../testing/github-actions`
* :doc:`../testing/code-coverage`
* :doc:`../testing/code-quality`
* :doc:`../style_guides/python-guidelines`
* :doc:`../style_guides/javascript-guidelines`
* :doc:`../style_guides/sass-guidelines`

.. _contributor's agreement: http://openedx.org/cla
.. _compatible licenses: https://openedx.org/open-edx-licensing
.. _OEP-51\: Conventional Commits: https://open-edx-proposals.readthedocs.io/en/latest/best-practices/oep-0051-bp-conventional-commits.html
.. _Paragon pattern library: https://paragon-openedx.netlify.app/
.. _forums: https://discuss.openedx.org/
