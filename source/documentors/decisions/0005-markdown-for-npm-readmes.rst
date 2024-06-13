Use Markdown READMEs for repos published to npm
###############################################

Status
******

**Accepted**

Context
*******

As documented in :doc:`0002-choosing-rst`, we use RST for the majority of Open edX documentation. 
This includes README files in Open edX project repositories.

When browsing packages on https://www.npmjs.com/, however, RST READMEs are not rendered.
This results in a "This package does not have a README." message appearing for packages with RST READMEs.

The `npm documentation for README files`_ mentions Markdown exclusively.

Decision
********

Markdown must be used for Open edX project repositories that publish packages to npm. 

Rejected Alternatives
*********************

* Adding RST to Markdown conversion for the README into the build/publish process.
  It is quite likely that formatting would be lost/broken in the conversion process.
  This would require README authors to verify their RST changes work post-conversion,
  adding complexity to the README writing process.

* Using a placeholder README file that links to the GitHub repository README. This would
  require either having both a Markdown and RST README in each repository, or implementing
  Markdown readme generation into the build/publish process. It would also result in a 
  sub-par experience when browsing Open edX published packages on npmjs.com.


Consequences
************

* The READMEs for npm packages published as a part of the Open edX project will be fully rendered on npmjs.com.
* Any existing RST READMEs in Open edX repositories that publish packages to npm will need to be rewritten in Markdown.

.. _npm documentation for README files: https://docs.npmjs.com/about-package-readme-files