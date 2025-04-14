Choosing RST
############

Status
******

**Provisional**

A major concern with accepting this decision is whether we can overcome the RST
and GitHub barrier to entry by investing in training and proper documentation.
This decision should be re-evaluated once we've put the relevant quickstarts,
how-tos and references through their paces.

Context
*******

Now that we agree on the doc:`general goal <0001-purpose-of-this-repo>` of a
root documentation site, we need to figure out how we will write the words for
the site.  Per `OEP-19`_ developer documentation is written in RST.  However
since the audience for all documentation is not developers it is worth
re-considering and reviewing the alternatives and actively make a decision here
rather than passively choose what already exists.


Decision
********

We will use `Sphinx-flavored`_ RST for the root `docs.openedx.org`_ site and any
documentation that is written within the repositories where the relevant
features exist.  In particular we will use the `Sphinx`_ tool to manage our RST
content and publish it using ReadTheDocs.org

.. _Sphinx-flavored: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html

Nuance
======

This does not mean that all documentation needs to live in repositories nor
that all of it must be RST.  There are many good reasons to write documentation
on the wiki, in GitHub Issues, or as discussion forum posts.  Especially early
on when there might be a lot of iteration.

Summary of Findings
===================

Markdown often looks like the right choice when looking at it from the
perspective of individual documents but quickly stops being a good solution as
we expand the scope of what we're trying to solve for in a larger project.  For
this reason, Markdown is often going to come up as a suggested replacement for
Sphinx Flavored RST.  However, while it has a pretty low barrier to entry, it's
overall capabilities are not yet mature enough to be a good replacement for a
project as large and as complex as the Open edX Platform.

We choose Sphinx RST as our tooling of choice because:

* It allows us to easily write words while spending minimal effort writing basic
  markup.

* It has tooling to help us build translations for documentation.

* It lets us use more advanced components using a straight forward directive
  syntax that's consistent and can be extended to add more features.

* It can be deployed easily using off the shelf tools like readthedocs.org

* It can be stored in version control which gives us the ability to build review
  and preview process around changes to the documentation.

* It allows us to deploy multiple versions of the documentation so that it's easy
  to access documentation for previous named releases.

* RST allows for easy componentization of documents so that they can be re-used.
  This is especially useful for user facing How-Tos.  For example, we often need
  to do the same initial steps to setup a course.  Making this re-usable allows
  us reduce boilerplate in our documentation and ease updates.

* `Developer documentation`_ is in RST already, choosing a different technology
  requires us to revisit that decision as well which may be more costly.

.. _Developer documentation: https://open-edx-proposals.readthedocs.io/en/latest/best-practices/oep-0019-bp-developer-documentation.html#decisions

Concerns Considered
===================

These were some notes on specific concerns we considered when making our
decision.  For each concern, we provide some notes on how we will address them.

* Git and GitHub are a barrier to entry for non-technical writers.

   * We acknowledge that we will have to do training and write good
     documentation to mitigate this for less technical users in our community.

     Investments by GitHub as well as effort we'll be making in terms of
     quickstarts and how-tos will help

* RST is a barrier to entry.

   * While RST can become very complicated, the basics of it are not much
     different from Markdown and other simple markup languages.  A small
     opinionated :doc:`quickreference <../references/quick_reference_rst>`
     should help mitigate the major issues.

* Translating RST docs is difficult.

   * The process and tooling around translations is not robust, the translations
     working group has had issues getting everything to work as expected.
     However, in spite of this Sphinx seems to be more mature than the
     alternatives we looked at.


Rejected Alternatives
*********************

.. _Basic Markdown:

Basic Markdown
==============

The basics of Markdown are extremely simple and easy to learn.  Because Markdown
was built for the web, it's often supported in web based editors and many people
are already quite familiar with it from other uses.

However, there are currently `over 30 implementations`_ of the original Markdown
reference specification.  The basic specification does not meet the needs of our
project as it lacks many of the capabilities that we would want to build a large
documentation project.

   * It doesn't allow for relative document links, which makes it difficult to
     have multiple builds (local development vs production) of the same docs and
     have the links point to local files locally and remote files when deployed.

   * Complex items such as videos, panels/cards, and generated documentation
     from other sources such as code must be added manually using raw HTML.
     This means we lose Markdown's advantage when we want to do anything more
     advanced than raw text and images.

.. _over 30 implementations: https://github.com/commonmark/commonmark-spec/wiki/Markdown-Flavors

Basic RST
=========

The basic RST specification has many of the same problems as the basic Markdown
specification.

   * Like basic Markdown, basic RST also doesn't allow for relative document
     links.

   * Basic RST also lacks support for complex items such as videos, panels/cards
     and other ways of generating documentation from code.

We reject this for much the same reason as we reject basic Markdown.


MkDocs Flavored Markdown
========================

The `MkDocs`_ tool powered by the `Python-Markdown`_ flavor of Markdown solves
many of the problems with pure Markdown by introducing the ability to add
extensions that add more functionality.  Both the issues noted above in the
:ref:`Basic Markdown <Basic Markdown>`
are solved via extensions in MkDocs.  However, the extension mechanism is not
consistent so each extension essentially adds its own new syntax to learn in
order to make use of the new capabilities.

Sphinx has similar extension capabilities but provides a much more consistent
syntax with which to make use of complex capabilities in the form of
`directives`_.

So while there are ways to overcome the shortcomings of basic Markdown, they add
undesired complexity which reduces flavored Markdown's advantage over flavored
RST.

Other reasons that we reject this option:

* Currently no good translations tooling exists to ease the process of
  translating the Markdown content.

.. _directives: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
.. _Python-Markdown: https://python-Markdown.github.io
.. _MkDocs: https://www.mkdocs.org/


MDX Flavored Markdown
=====================

Another popular way of writing Markdown is `MDX`_, a flavor of Markdown that
combines Markdown syntax with `JSX`_ syntax to let you write React web pages.
While it is possible to create a documentation site this way, we do not believe
it is the right tool for the audience as it adds even further barriers to entry
for non-technical documentation writers.

Other reasons that we reject this option:

* Requires us to re-develop many capabilities that the other options already
  have available.  From basic things like Admonitions to more complex things
  like code and video blocks.

* Currently no good translations tooling exists to ease the process of
  translating the Markdown content.

* Increased development and maintenance burden as we would have to deploy the
  site ourselves rather than using an existing industry standard tool such as
  ReadTheDocs.org

* No good tooling exists to deploy and maintain multiple versions of the same
  documentation.

.. _MDX: https://mdxjs.com/
.. _JSX: https://facebook.github.io/jsx/

Confluence Wiki
===============

One of the major drawbacks of both the RST and Markdown approaches is that both
require us to use git and GitHub to coordinate and make
changes. We currently believe that this is a barrier that can be overcome with
sufficient guidance and documentation for newcomers.  However an alternative
that was considered was to use the existing Confluence wiki as the root
documentation site.

We rejected this option for the following reasons:

* It introduces a much more complex permissioning system for who can edit what
  documentation.

* It lacks a good search mechanism which can't easily be replaced with standard
  search engines because of its complex permissioning system.

* It is harder to guard against malicious changes since Confluence does not
  provide a review workflow for content changes.

* Keeping multiple versions of documentation available is not easily possible.

* There is no workflow for maintaining translations of documentation.

.. _OEP-19: https://open-edx-proposals.readthedocs.io/en/latest/best-practices/oep-0019-bp-developer-documentation.html
.. _docs.openedx.org: https://docs.openedx.org
