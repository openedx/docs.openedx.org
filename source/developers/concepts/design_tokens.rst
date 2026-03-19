.. _Design Tokens:

Design Tokens
#############

What are Design Tokens?
***********************

Design tokens are all the values needed to build and maintain a design system —
spacing, color, typography, object styles, etc. They can represent anything
defined by the design: color as an RGB value, opacity as a number, spacing as a
REM value. They are used instead of hard-coded values to provide flexibility and
uniformity across the application.

By defining style properties as tokens, we can transform the styles into various
implementations compatible with different platforms or formats (e.g.,
transforming tokens to CSS variables, CSS utility classes, and eventually
mobile).

Paragon uses `style-dictionary <https://github.com/style-dictionary/style-dictionary>`_ to build design tokens into CSS variables.

Background & Motivation
***********************

Design tokens debuted as the primary theming mechanism in the Ulmo release (January 2026), and was available for beta testing in the Open edX Teak release (June 2025).

.. warning::
   
   There will be no overlap between the old SCSS-variable theming system and Design Tokens. Site operators must prepare migration strategies in advance.

**Background reading:**

* `Scaling Paragon's styles architecture with design tokens (Confluence) <https://openedx.atlassian.net/wiki/spaces/BPL/pages/3630923811/Scaling+Paragon+s+styles+architecture+with+design+tokens>`_
* `ADR: design tokens implementation in Paragon <https://github.com/openedx/paragon/blob/master/docs/decisions/0019-scaling-styles-with-design-tokens.rst>`_
* `November 2024 Open edX meetup presentation slides <https://docs.google.com/presentation/d/1FOSbTUTbbzaBoIDYMa5s32in1uFoYWdoQ-GjKk5IRBo/edit?usp=sharing>`_
* `Teak design tokens wiki (includes test branches) <https://openedx.atlassian.net/wiki/spaces/BPL/pages/5050499077/Using+Teak+Design+Tokens+branches>`_

Reference Links
***************

* :ref:`Release note (Ulmo) <Ulmo Design Tokens>`
* `Paragon tokens source (release-23.x) <https://github.com/openedx/paragon/tree/release-23.x/tokens>`_
* `Paragon README: Design Tokens section <https://github.com/openedx/paragon/tree/release-23.x?tab=readme-ov-file#design-tokens>`_
* `brand-openedx (interface definition) <https://github.com/openedx/brand-openedx>`_
* `brand-openedx: design tokens how-to <https://github.com/openedx/brand-openedx/blob/main/docs/how-to/design-tokens-support.rst>`_
* `sample-plugin/brand (purple example) <https://github.com/openedx/sample-plugin/tree/main/brand>`_
* `elm-theme (production example) <https://github.com/edx/elm-theme>`_
* `tutor-contrib-paragon <https://github.com/openedx/openedx-tutor-plugins/tree/main/plugins/tutor-contrib-paragon>`_
* `frontend-platform theming docs <https://github.com/openedx/frontend-platform/blob/master/docs/how_tos/theming.md>`_
* :ref:`OEP-0048: Brand Customization <openedx-proposals:OEP-48 Brand Customization>`
* `style-dictionary docs <https://amzn.github.io/style-dictionary/#/>`_
* `W3C Design Tokens Community Group spec <https://tr.designtokens.org/format/#abstract>`_
* `Confluence: Background/motivation <https://openedx.atlassian.net/wiki/spaces/BPL/pages/3630923811/Scaling+Paragon+s+styles+architecture+with+design+tokens>`_
* `Confluence: Teak test branches <https://openedx.atlassian.net/wiki/spaces/BPL/pages/5050499077/Using+Teak+Design+Tokens+branches>`_
* `Paragon design tokens issues <https://github.com/openedx/paragon/issues?q=design+tokens>`_
* `Paragon CLI issues <https://github.com/openedx/paragon/issues?q=%5BCLI%5D>`_


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-03-20   |  Frontend WG                  | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+