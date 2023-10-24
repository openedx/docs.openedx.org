************
Contributing
************

Contributing your custom code to the Open edX project is a two-step process:
review of your idea by the product team (the Product Review Process),
followed by a review of your code by the project's core committers.
We describe this process on this page.

Note::

   By and large, bug fixes do not require the Product Review Process.
   However, if your bug fix will change user facing behavior, you should
   check with the Product Working Group on the best way to land your fix.

----------------------------------------
Product Review Process & Product Roadmap
----------------------------------------

New features added to the Open edX project go through a Product Review
Process, lead by the Open edX Product Working Group. If you're interested
in adding new features, we ask that you undergo the product review process
_before_ you begin coding your feature. This allows the project to get
alignment on new features and help guide you to implement the feature in
a way that works with the overall platform. Additionally, there might well
be someone else already working on the same change you want to make,
and it's much better to collaborate than to submit incompatible pull requests.

If you open up your feature request with a solid description, the product owners
will be able to quickly understand your change and prioritize it for
review. However, they may have some questions about your intention, need,
and/or approach that they will ask about.

To read more about the product review process and how to submit your idea,
**TODO: Visit This Content (wiki?).**

Features that the project wants, as well as ones being currently worked on
by community members, are represented on the `Product Roadmap`_. This
kanban-style board represents units of work on individual cards. Check
out the tickets on the far left for help reading the board. The tabs at
the top will allow you to drill into roadmap tickets by platform area.

If you're interested in contributing to the Open edX project but don't know
what to contribute, check out the roadmap! If you're interested in picking
up or collaborating on a ticket, join the conversation by adding a comment
on the ticket.

.. _Product Roadmap: https://github.com/orgs/openedx/projects/4

----------------------------
Getting Preliminary Feedback
----------------------------

It is sometimes useful to submit a pull request even before the code is
working properly, to make it easier to collect early feedback on your
implementation. To indicate to others that your pull request is not yet in a
functional state, just prefix the pull request title with "(WIP)" (Work In
Progress), and start the pull request as a draft on GitHub. 

Please include a link to your roadmap ticket in the PR description, and add a
link to a WIP pull request in any discussion threads you start.

-----------------
Landing Your Work
-----------------

Once you're ready to submit your code changes in a pull request, check the following
list of requirements to be sure that your pull request is ready to be reviewed:

#. Prepare a detailed pull request description. Most repositories have a template
   to be followed when you open the PR in the GitHub UI. Please fill out that template
   with as much detail as possible, including links to any roadmap tickets or
   forum discussions as well as screenshots or screencasts.

#. The code should be clear and understandable. Comments in code, detailed
   docstrings, and good variable naming conventions are expected. See the
   :doc:`../style_guides/index` for more details.

#. Commit messages should conform to `OEP-51: Conventional Commits`_.
   This style categorizes commits to make them easier to understand.

#. The pull request should be as small as possible. Each pull request should
   encompass only one idea: one bug fix, one feature, etc. Multiple features
   (or multiple bug fixes) should not be bundled into one pull request. A
   handful of small pull requests is much better than one large pull request.

#. Structure your pull request into logical commits. "Fixup" commits
   should be squashed together. The best pull requests contain only a
   single, logical change -- which means only a single, logical
   commit. You can squash your own commits, or the person merging the
   pull request may choose to squash them.
   They will do so by using the `Squash and merge` button of
   the GitHub interface to preserve the logical commits in the pull
   request, for forensic purposes when trying to diagnose a regression
   or understand a bug.

#. All code in the pull request must be compatible with the Open edX project's AGPL
   license.  This means that the author of the pull request must sign a
   `contributor's agreement`_, and all libraries included or
   referenced in the pull request must have `compatible licenses`_.

#. All of the tests must pass. You'll see the checks that are being run on the
   bottom of your PR; they must be green.

#. If a pull request contains a new feature, it
   should also contain new tests for that feature. If the pull request fixes a
   bug, it should also contain tests for that bug to be sure that it stays
   fixed. GitHub actions will verify this for your pull request, and point out
   any failing tests.

#. The author of the pull request should provide a test plan for manually
   verifying the change in this pull request. The test plan should include
   details of what should be checked, how to check it, and what the correct
   behavior should be. When it makes sense to do so, a good test plan includes
   a tarball of a small test course that has a unit which triggers the bug
   or illustrates the new feature.

#. For pull requests that make changes to the user interface, please include
   screenshots of what you changed. GitHub will allow you to upload images
   directly from your computer. Changes should only use elements from the
   `Paragon pattern library`_.

#. The pull request should contain some documentation for the feature or bug
   fix. A well-written description for the pull request is often sufficient.

#. The pull request should integrate with existing infrastructure as much as
   possible, rather than reinventing the wheel.  In a project as large as ours,
   there are many foundational components that might be hard to find.
   It is important not to duplicate functionality, even if small, that already
   exists. Posting in the `forums`_ is an easy way to find out if functionality
   you're looking for already exists.

#. The author of the pull request should be receptive to feedback and
   constructive criticism. The pull request will not be accepted until all
   feedback from reviewers is addressed. Once a core committer has reviewed a
   pull request from a contributor, no further review is required from the core
   committer until the contributor has addressed all of the core committer's
   feedback: either making changes to the pull request, or adding another
   comment explaining why the contributor has chosen not make any change based
   on that feedback.

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
* :doc:`../testing/jenkins`
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
