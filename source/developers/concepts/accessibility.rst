###############################
Open edX Accessibility Concepts
###############################

The Open edX project measures and evaluates accessibility using the World Wide Web Consortium's
`Web Content Accessibility Guidelines (WCAG) 2.2 <https://www.w3.org/TR/WCAG22/>`_
(20 July 2023). All features that you merge into edX repositories are expected
to `conform <https://www.w3.org/TR/WCAG22/#conformance>`_ to `Level AA
<https://www.w3.org/TR/WCAG22/#cc1>`_ of this specification and to satisfy the
requirements outlined in the edx.org `Website Accessibility Policy
<http://www.edx.org/accessibility>`_. The **edx.org Accessibility Guidelines**
are intended to extend the guidance available in WCAG 2.2, with a focus on features
frequently found in the Open edX platform as well as in Learning and Content
Management Systems in general.

.. contents::
 :local:
 :depth: 2

============
Introduction
============

Accessibility, often abbreviated "a11y" ("a" followed by 11 letters followed
by "y"), is the practice of creating technologies in a way that all users can use.
The core mission of the Open edX project is to expand access to education for everyone. We expect
any user interfaces that are developed for the Open edX platform to be usable by
everyone, regardless of any physical limitations that they might have. The Open
edX platform is used every day by people who might not be able to see or hear,
or who might not be able to use traditional modes of computer interaction such
as the mouse or keyboard.

Understanding a few core concepts about how people with disabilities use the web
and web applications should give you more context for applying the guidance in
this document.

* People without vision, as well as those with neurological conditions that
  prevent precise hand-eye coordination, cannot use a mouse. Therefore, all interactive content must be usable by keyboard alone.

* People with mobility impairments might use custom keyboards, keyboard
  emulators, or voice input programs.

* Some people rely on speech to interact with web applications and need to be
  able to address interactive elements by speaking their accessible names. Any visible labels should be a part of the control's accessible name.

* People who cannot hear, or cannot hear well, require visible text captions (or an
  equivalent visual cue) for any audible content.  This includes recorded audio and video, but also includes audible UI feedback.

* Many people with disabilities use "`assistive technologies
  <http://www.w3.org/TR/WCAG20/#atdef>`_" (such as screen readers) to interact
  with their computers, web browsers, and web applications.

* Some of the most commonly used assistive technologies are browser plugins.  Common examples include Reader Mode (for text reflow), Speech output for text when selected or on mouse hover, and thesaurus and grammar checkers for people with dyslexia.

* Learners might customize their operating system, browser, or web page display properties to make
  web applications easier for them to use. For example, they might increase the
  font size in their displays, reverse or increase contrast, or remove images.

* To allow assistive technologies to provide the maximum information to users,
  anything in a user interface that is conveyed visually (such as the element
  with focus, an element's role, its current state, and other properties) must
  also be conveyed programmatically. This information is often included automatically when you
  use native HTML5 elements or `Paragon <https://github.com/openedx/paragon>`_` components.

Keep these core concepts in mind when you develop user interfaces so that they
can truly be used by everyone. More information is available from the W3C's Web
Accessibility Initiative's publication `How People with Disabilities Use the
Web: Overview <http://www.w3.org/WAI/intro/people-use-web/Overview.html>`_.


============================
Accessibility Best Practices
============================

The following sections cover some best practices and tips to keep in mind as you
develop user interfaces that are WCAG 2.0 compliant.

* Use semantic markup
* Make images accessible
* Avoid using CSS to add content
* Include title attributes for all iframe elements
* Make sure form elements have labels
* Include link and control labels that make sense out of context
* Use WAI ARIA to create accessible widgets
* Manage focus for popups
* Inform users when content changes dynamically
* Hide or expose content to targeted audiences
* Choose colors that meet minimum contrast ratios
* Test your code for accessibility

For more on how to code for accessibility, see :doc:`../references/a11y-ref`.
