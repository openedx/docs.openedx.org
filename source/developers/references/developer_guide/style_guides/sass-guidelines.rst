..  _edx_sass_guidelines:

#########################
Open edX Sass Style Guide
#########################

This section describes the requirements and conventions used to contribute
Sass stylesheets to the Open edX platform.

.. warning:: Please note that the project is currently in the process of
   transitioning to `Design Tokens`_, a better alternative to Sass.  At the
   time of writing there is no official deprecation plan, but the goal is to
   eventually remove Sass altogether from the codebase.  The linked document
   describes the reasons why.

.. contents::
 :local:
 :depth: 2

.. highlight:: none

**********
Code Style
**********

In order to standardize and enforce the Open edX project's Sass coding style across
multiple codebases, the project uses `Stylelint`_ which is a widely adopted CSS linter
written in JavaScript. In particular, Open edX provides the `Open edX Stylelint Config`_
which is an npm package that defines the rule set to be used to validate Sass.

The Open edX project generally adopts the standard Stylelint rule set:

* `CSS Rules`_
* `SCSS-Specific Rules`_

If you are interested in the exceptions, see the `Open edX Stylelint Config README`_.

*************
Use Variables
*************

It is strongly recommended to avoid hard-coding values such as colors and fonts.
Using hard-coded values makes it difficult to change the value in the future as
it may have been used in many stylesheets. Using variables also allows themes
to simply override the value in one place.

Before defining a new variable, see if you can reuse an existing one. If you
need to create a new one, be sure to use the ``!default`` flag. This allows
themes to provide a different value for this variable if they choose. See the
Sass documentation for `default flag`_ for more details.

For example, here is an example of a hard-coded style::

    .my-element {
      color: #0000ff;
    }

This should instead be written as::

    $my-custom-color: #0000ff !default;

    .my-element {
      color: $my-custom-color;
    }

.. _Design Tokens: https://github.com/openedx/paragon/blob/master/docs/decisions/0019-scaling-styles-with-design-tokens.rst
.. _CSS Rules: https://github.com/stylelint/stylelint/blob/master/docs/user-guide/rules.md
.. _default flag: https://sass-lang.com/documentation/variables/#default-values
.. _Open edX Stylelint Config: https://github.com/openedx/stylelint-config-edx
.. _Open edX Stylelint Config README: https://github.com/openedx/stylelint-config-edx#sass-style-guide
.. _SCSS-Specific Rules: https://www.npmjs.com/package/stylelint-scss#list-of-rules
.. _Stylelint: https://stylelint.io/
