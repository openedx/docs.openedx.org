Open edX Documentation Writing Style Guide
##########################################

.. contents:: Contents
  :local:
  :depth: 2

Overview
********

This style guide exists to help Open edX document writers create their documents in a unified style that is easy to read, and that falls in line with the rest of the documentation. This document highlights the most important and relevant style guidelines, with examples specific to the Open edX platform.

Documentation Repository
************************

All Open edX documentation is managed in Github. To create one or more new pages, you’ll need to have a Github account and access, submit a pull request to have your content added. Please, follow these guidelines to start working in Github.

Document Writing Principles
***************************

Diataxis Organization
=====================

All Open edX documentation is organized based on the Diataxis framework [include link]. Such guide describes 4 types of documents which are the following:

- Quickstart
- How-to guides
- Reference
- Concepts

Apart from having the documents under such framework, when writing a new document, keep in mind these questions as a checklist:

Content
=======
* **Clear Purpose**: Is the purpose of the document well-defined?
* **Relevant Information**: Does it include all necessary information, and nothing extra that should go into a different guide?
* **Accuracy**: Are the facts and data correct?
* **Thoroughness**: Does it cover the topic comprehensively?

Structure
=========
* **Logical Organization**: Is the information presented in a logical order?
* **Headings and Subheadings**: Are they used effectively to guide the reader?
* **Sections and Paragraphs**: Are sections well-defined and paragraphs concise?

Clarity and Style
=================
* **Clear Language**: Is the language straightforward and easy to understand?
* **Consistent Tone**: Is the tone appropriate for the audience and consistent throughout?
* **Avoid Jargon**: Is jargon minimized or explained for clarity?
* **Voice**: Is the voice active? Are you using third person?

Visual Elements
===============
* **Formatting**: Is the document visually appealing with appropriate fonts and sizes?
* **Lists and Bullet Points**: Are they used to enhance readability?
* **Images and Graphs**: Are visuals used effectively to support the text?

Review and Edit
===============
* **Proofreading**: Is the document free of spelling and grammatical errors?
* **Feedback**: Has it been reviewed by someone else for clarity and effectiveness?
* **Revisions**: Have necessary changes been made based on feedback?

Accessibility
=============
- **Readable Layout**: Is the layout easy to navigate?
- **Accessibility Features**: Are there considerations for individuals with disabilities (e.g., alt text for images)?

Apart from answering those questions, our document needs to follow these principles:

- **Make it clear**: Is the purpose of the document well-defined? The best documentation doesn't try to sound fancy, complicated, or self-important. While what you are doing may be difficult, there is no reason to make it seem that way through documentation. Instead, focus on clarity and ease of reading. To this end:
    * Use simple language.
    * Keep sentences short.
    * Be direct.

- **Make it scannable**: Good documentation should allow users to scan through for just the information that they need. To this end:
    * Organize the information based on what is most important to your users. Thinking about things from the user's standpoint is a vital step to making the documentation accessible.
    * Use headings and subheadings strategically to separate the document into scannable sections.
    * Use stylistic elements strategically to help you organize your document and highlight the most critical information.
    * Use bolded text rather than capital letters to draw attention to key words and phrases.

    Use directives such as ``:info:``, ``:warning:``, and ``:guilabel:`` to draw attention to important text and button labels. For more information about this, please check this Quick Reference Directives.

- **Make it connect**: Good documentation connects to other resources. This connection helps users gain a firmer grasp on the material, adds credibility to your writing, and eliminates the need to "reinvent the wheel." To this end:
    * Link to other Open edX documentation that is relevant to your topic and audience.
    * Link to other external sites only if they provide information not contained in the first two sources. Use caution when connecting to external sites, as the content of those sites may unexpectedly change without warning.
    * All links should be written as text links in context. Your final document should not include full URLs written out.

Audience
========

Make sure your documentation is targeted to the right audience and organized under that audience’s section of the documentation. Each topic in the documentation is for one of the following audiences:


- Educators
- Site Operators
- Developers

Ensure that new topics are stored in the directory for the appropriate audience, under the source directory. For more information, see Documentation Audiences.

Languages
*********

Open edX documentation is written in American English.

Documentation Language
======================

The Open edX docs.openedx.org repository is using a documentation markup language called reStructured Text language (RST) which is very similar to Markdown. You can check this guide which is helpful to learn how to implement such language: RST Guide.

Migrating Docs Checklist
************************

Some checklist items are specific to migrating 2U/Edx.org legacy docs into Open edX® Docs. During migration, documentors are using this Open edX Doc Migration Tracking sheet.

* **Remove or modify references that are specific to 2U/EdX.org**: When migrating legacy documentation from 2U/EdX.org, remove references that are applicable only to the 2U or EdX.org users.
* **Modify references that may have come from 2U/EdX.org but are also applicable to Open edX® LMS users**.

Clear any .. only:: formatting
==============================

This type of formatting is left over from legacy documentation and won’t render in Open edX® Docs. It is typically seen as `.. only:: Open_edX` or `.. only:: Partners` followed by intended text.

    Example:
    ```rst
    .. only:: Open_edX
    Here some text only intended for Open edX users.
    ```

    To clear it, remove the `.. only::` line and unindent the text. For 2U/Edx.org specific text, see point above.

* **Verify All Links**: Some legacy documents are many years old. Links may no longer be working or accurate, even if they are not throwing an error in the Sphinx Docs build process. All links (internal and external) should be verified manually.

Elements
********

Elements are non-textual components of your document. The following elements add clarity to complicated sections, highlight important information, and create clear distinctions between different types of information.

* Code
* Headings
* Images
* Links
* Lists
* Notes
* Block Quotes
* Table of Contents
* Tables
* Tags
* Info and Warning boxes

Code
====

Occasionally you will need to post snippets of code in your documents. Since code regularly uses the same symbols as our documentation language reStructuredText (RST), you will need to mark it properly so that RST does not confuse your code with the RST language surrounding it.


**Code Samples** 

You can use ``backticks`` for showing ``highlighted`` code.
If you want to make sure that text is shown in monospaced fonts for code examples or concepts, use double backticks (``) around it. (``)


Sections
========

At this point you have probably noticed the document-level navigation panel to the right of each document on the Open edX documentation sites. It displays all of the sections in the document, and allows users easy access to those contents. Because headings have a navigational component, it is especially important to use headings strategically and word them in a clear and accessible manner.

* Use title case for all headings.
* For a top level section heading and for topics that introduce concepts, use a verb in gerund form to start the title.
* For topics that describe a procedure, use an imperative verb to start the title.

Example:

* "Adding Course Updates and Handouts"
* "Adding a Course Update"
* "Identify a Course Handout"

**Additional Tips**

* Headings should be first-letter capitalized.
* Headings should not be bolded or italicized.
* Headings should not use end punctuation.

Images
======

Images should be used to explain complex processes. They are a quick solution to explain the location of an object on a page or to demonstrate the flow of information. However, be judicious and avoid using numerous large screenshots when a sentence can provide the user with sufficient guidance.

To add an image to an Open edX document, use the following RST format, which has all the necessary parameters included:

.. code-block::

    .. image:: _assets/example_image_2.png
        :width: 500px
        :align: center
        :alt: Alternative text. This is important for accessibility

You can modify the width if the image size needs to be adjusted to be more apparent or visible to the reader.

An image's alt text must be descriptive and clear to facilitate the use of different accessibility tools, such as screen readers. This practice also helps the web repository's SEO positioning.

Lists
=====

Introduce a list with a complete sentence that ends in a period. Do not use “the following” as a noun or to introduce a list. Instead, include the noun. For example, “The .csv file includes the following columns.” or “When pretty printed, this comment has the following format.”

Numbered lists
--------------

Numbered, or Ordered lists should be used to express processes.

Example:

1. Open Studio at the URL provided by your administrator.
2. Click New Course. The Create a New Course screen opens.
3. Enter information for the new course:
    - Course Name: The public display name of the course. You can override the name later in the Advanced Settings.
    - Organization: Your school or organization. This value becomes part of the course URL and cannot be changed. You can override how the organization is displayed to learners in Advanced Settings.
    - Course Number: The unique number that identifies your course. Note: This value becomes part of the course URL and cannot be changed. No spaces or special characters are allowed.
    - Course Run: The term or unique run of the course. This value part of your course URL, so no spaces or special characters are allowed and it cannot be changed.
4. Click Create.

.. note:: 
    Numbered lists should not be extended over headings. If you use a heading, you should restart your numbered list.

Bulleted lists
--------------

Bulleted, or Unordered lists display information in a compact and highly visible format. For usage rules, see the example below:

- Complete sentences should start with a capital letter, and should end with end punctuation.
- Some items
- May contain
    - sub-items.
- Sentences that are
    - broken over multiple lines
    - do not need to have end punctuation
    - until that sentence ends.
- Single
- Items
- Need
- No
- Punctuation

For information on entering unordered lists in RST, see the list-table section on the RST guide.

Links
=====

To have more interactive documents, always try to include hyperlinks to help readers quickly access relevant additional documentation and resources. Open edX documentation should not include full URLs written out. For information on entering links in RST, review the hyperlinks (internal or external) section from the RST guide.

For adding links to other locations in the same document, to locations in other documents and to external websites, please check this document.

Types of Call-Out Boxes
=======================

Notes
-----

Notes (using the `.. note::` directive) should be used to highlight the most valuable information in a section. Notes are considered to be more important than information that is bold. Notes are highly visible, and as such should be used sparingly.

Example:

.. note:: 
    Notes stand out from other texts. They allow you to insert information that is directly relevant to the last paragraph, but may not fit with the tone of that section. To enter Notes using RST, please, check this section of the guide.

Tip
---

Tips are another specialized block quote that will appear in a special way on the documentation site. Tips should be used to highlight useful methods of performing an action.

Example:

.. tip:: 
    Tips allow you to provide useful information for procedures. Tips can be entered in RST, so check this section of the RST guide.

Important
---------

Important blocks are specialized block quotes that will appear in a special way on the documentation site. They should be used to convey information that cannot be ignored.

Example:

.. important:: 
    Vital information that should not be ignored. Highlights critical information that the reader should pay special attention to, but may not necessarily indicate a risk. Important notes can be entered in RST.

Warning
-------

Warning blocks are specialized block quotes that will appear in a special way on the documentation site. They should be used to convey information that, if ignored, may do one of the following:
- Endanger the user's data or their solution.
- Lead to inappropriate, undesired, or unexpected results within the user's solution.
- Expose the user or their solution to risk.

Example:

.. warning:: Vital information that should not be ignored. The user incurs risk if this information is not followed. Please, check this section of the RST guide to know how to include them.

See also
--------

This directive is useful for referencing other documents related to the topic that may be of interest to the reader.

.. seealso:: Here goes the reference to another document.

Additionally, “See Also Tables” is an important way for users to find documents related to the topic they are exploring. Good docs will have thorough, accurate, and relevant links in the See Also section through this syntax.

.. seealso::
    :class: dropdown

    :ref:`Offering Differentiated Content` (concept)
    
    :ref:`Configure Your Course for Content Experiments` (how-to)

Table of contents
=================

The table of contents is the navigation section to the left of your document. Clicking entries on the table of contents will open that document. The table of contents is consistent across all documents on docs.openedx.org. Every document must belong to at least one table of contents. In other words, you cannot create “orphan” documents that are not reachable to users via standard navigation.

As an example, if a new file ``build_a_course.rst`` is created, then it would need to be appended to an existing table of contents, as shown in the example below. 

You can learn more about adding your document to a table of contents by following this guide.

Also, you can do a :glob: `*` on an index page, meaning in some cases, documents in a page tree are automatically added to the ToC. In the following example, any file contained in the same folder will automatically be added to the table of contents. It is a quick way to set up a table of contents so that new documents are automatically picked up, but it reduces the control you have on the order of your documents in the TOC:

.. code-block::

    .. toctree::
       :maxdepth: 1
       :glob:

       *

Tables
======

When you include a table, be sure to include a heading row. In addition, consider whether a stub column is appropriate. The heading row and stub column provide useful context for users of screen readers.

Tables should be used to compile complicated data and indicate its relationships. In Open edX documentation, tables look like this:

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3

• When the information is significantly complicated.
• When the information repeats at least one element more than twice.
• When the information does not benefit from being compressed.

When not to use a table:
• If that information could be better written in a sentence.
• The information is important but not sufficiently complicated.

For information on entering tables in RST, see the RST guide.

Tags
====

Tags appear as links (e.g. #Administrator) at the top of the article. If you click on the tag, it will take you to a page listing all files with that tag. This allows users to search for documents with a particular tag. A typical document should have at least two tags:
- One or more persona tags: The document is tagged with the intended reader persona type. If the document is relevant to more than one audience, then you may use more than one tag. Educator, developer, site operator, community, documentor, translator.
- One (and only one) diataxis tag: The document is tagged with the diataxis type it belongs to. Concept, reference, quick-start, how-to.

The syntax of tags is as follows:

.. tags:: educator, reference

NOTE: Tags should be placed after the first heading in the document.

Use of Abbreviations
====================

The first time you want to use an abbreviation, spell it out. For example:

The Open edX ``docs.openedx.org`` repository is using a documentation markup language called reStructuredText (RST) which is very similar to Markdown. The following guide is helpful to refer to as you produce RST documentation: RST Guide.

Punctuation
===========

Punctuation is the primary example of a convention. For specifics on punctuation use, see https://draft-edx-style-guide.readthedocs.io/en/latest/global_English.html#.

Quotation Marks
===============

Quotation marks are commonly used incorrectly by newer documentation writers. Follow this short list to ensure that you use quotation marks correctly.

• Quotation marks should only be used for direct quotations.
• If you want to emphasize text, you should use italic text.
• If you want to draw attention to a specific word, you should use bolded text.
• If you want to ensure that code appears correctly, you should use code notation.
• Use the `` :guilabel:`` directive to highlight the text of a button.

• Quotation marks should always use the double quotes ("), unless you are quoting inside a quotation. Under those conditions, you can use the single quote (').

Italic Text
===========

*Italic* text can be used to add emphasis to a word, phrase or sentence. As italic text is slightly more difficult to read, it should be used sparingly. Instead, we recommend using bolded text. 

Bolded Text 
===========

Using **bold type** for emphasis serves to draw the reader's attention to specific words or phrases that are particularly important or impactful.

