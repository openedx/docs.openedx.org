.. _Guidelines for Writing Global English:

Guidelines for Writing Global English
#####################################

.. tags:: documentor, reference

.. contents::
  :local:
  :depth: 1

***************
Global Examples
***************

In addition to writing so that the text can be easily translated, remember that the Open edX audience is global, and ensure this is reflected in the examples we use to illustrate concepts in the documentation. Use situations that people can relate to regardless of their culture, and use example names and email addresses that represent diverse ethnicities.

***************
Short Sentences
***************

Write short sentences when possible. Long sentences can include problems...

* complex grammar
* complex use of tenses
* ambiguous pronouns
* long clauses
* complex modifier strings

Try to limit sentences to 20-30 words. Rule of thumb: if you run out of breath when you read a sentence aloud, it is too long.

However!

* Do not damage clarity.
* Do not sacrifice the syntactic cues provided by definite and indefinite articles.
* Do not omit important information. Be explicit.

Example:

"Create course content" could mean completely different things once a preposition is inserted. Compare "Create course content for the new program." to "Create course content about the new program."


******************************
Active Voice and Active Verbs
******************************

Use the active voice.

Use active verbs. Avoid nominalizations (nouns made from verbs or adjectives) as they disguise the actors.

  Example nominalizations:

  utilization, operation, facilitation, activation, completion, reaction, improvement, movement, discovery, difficulty

Here's an example of a sentence drafted in the passive voice and how it was rewritten in the active voice.

  Passive: This method is typically applied to free text fields, including discussion posts and wiki articles.

  Active: The Open edX community writers typically apply this method to free text fields, including discussion posts and wiki articles.


**************
Bulleted Lists
**************

- Write bulleted lists so that they are translatable.

- Introduce the list with a complete sentence.

- Please don't use the bulleted points to complete an introductory sentence.

- Make sure each bulleted point can stand alone.

This approach might increase word count, but it decreases translation costs.

*********
Pronouns
*********

Avoid ambiguous pronouns, particularly impersonal pronouns.  All kinds of words can sneak into use as pronouns.

  Examples:

  all, another, any, each, either, few, following, many, neither, none, one, other, rest, same, several, some, such, that, them, these, those

Ask "of what?", "of which?" or "as what?" when you use these words.

  Example:

  To sterilize a reusable product using an autoclave, it must first be properly cleaned and disinfected.

  What must be cleaned and disinfected?

Avoid broad-reference pronouns.

  Example:

  Our new monitor has virtually no background noise, which should substantially reduce the number of false positives.

****
Mood
****

Avoid the subjunctive mood. Native English speakers have trouble with it. Prefer the indicative and imperative moods.

***************
Provide Context
***************

Be sensitive to words that are used as both nouns and verbs and provide context for them.

  Examples:

  Display it on the screen.

  Change the scroll rate on the display.

***********
Word Choice
***********

Avoid jargon.

Avoid colloquialisms.

Avoid humor.

Eliminate unusual non-technical words.

  Examples:

  and so forth, albeit, heretofore, whilst, ...

Use nouns as nouns and verbs as verbs. (More on that elsewhere!)

Beware of commonly used constructions that introduce ambiguity.

  Examples:

  Replace "For more information on..." with "For more information about..."

  Replace "When the process completes, you can..." with "After the process completes..."

*****************************
Use (and Add to) the Glossary
*****************************

Use and maintain our :ref:`glossary <Glossary>`. Be consistent in the terms used.

  Example:

  top, cap, and cover are translated and understood as three different things, not as the same thing.

*************
Contractions
*************

Avoid contractions. They introduce ambiguity, particularly 'd and 's. Use other means to convey a friendly, informal tone.

***********
White Space
***********

Plan for expanded text. An expansion of 25% is common, so incorporate white space in flowcharts, blocks of text, and UI strings.

***********
Punctuation
***********

Avoid slashes. They introduce ambiguity.

Avoid em dashes. Putting non-restrictive relative clauses into separate sentences lead to simpler, clearer writing.

Do not use smart quotes or smart apostrophes. Prefer the straight versions.

*************
Abbreviations
*************

Avoid clipped terms.

  Examples:

  stat, spec, app, quotes, rep

  Exception:

  "The mobile app" is the correct term.

Avoid acronyms.

Do not use Latin abbreviations.

Do not use non-technical abbreviations.

***************
Preferred Usage
***************

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Term
     - Usage
   * - Can, Might, and May
     - Use the verb “can” to describe ability, capability, or capacity. Use “might” to describe possibility or eventuality. Because “may” implies permission, the Open edX documentation team prefers to use one of        the other two verbs.
   * - Capitalization
     - Use title capitalization for headings. When discussing elements in the user interface, please follow the capitalization used in the labels or text. Refrain from capitalizing on job titles like professor,         instructor, or program manager. Please don't capitalize terms unless they are trademarks so that you can refer to the instructor dashboard or a course about video rather than the Instructor Dashboard or a        course About video. Always capitalize “Open edX” with a capital O to begin, a space between “Open” and “edX,” and a capital “X” to end. Do not use spellings such as “OPEN EDX”, “OpenedX,” or “openedx”            (unless referring specifically to terms used in code). Further, “Open edX” must always be used as an adjective per trademark rules.
   * - Contractions
     - Do not use.
   * - Cross-references
     - Introduce standalone cross-references to other Open edX topics with the phrase, ``For more information, see :ref:`{topic name}```. To include more specific information about the material you are   referencing, use the expanded phrase, ``For more information about {task or concept}, see :ref:`{topic name}```. Exception: In the glossary, cross-references to other glossary entries begin with, ``See :ref:`{topic name}``` if the current entry consists only of the cross-reference. To refer to a related entry, use ``See also :ref:`{topic name}```. To include a cross-reference inline, extend the cross-reference to include a phrase that makes sense in context. In this example, the “course launch checklist” is added to the cross-reference markup to create a sentence with the correct capitalization. ``To verify that the course is ready for release, you can use the :ref:`course launch checklist<Course Launch Checklist>```. For a cross-reference to an external resource, provide the title of the destination, not just a URL. This style promotes a better experience for those using screen readers. In addition, avoid repeating links to the same destination multiple times on a single HTML page.
   * - Dates
     - Format dates as ``DD Mon YYYY`` or ``DD Month YYYY``. For example, 11 Jan 2015. Do not use both date formats within the same .rst file.
   * - First-person
     - Do not use “I” or “me” unless you follow the text of a user interface label or message. Avoid using “we”. If there is an established Open edX best practice, identify the entity that recommends that               practice by name.
   * - Hyphenation
     - Minimize the use of hyphenated compounds. Present compound words as either two separate words or a single word. Use hyphens only when the meaning is unclear without them. For exceptions to this rule, see the word list.
   * - Pronouns
     - Avoid ambiguous pronouns such as all, each, many, several, some, that, them, these, those.
   * - Punctuation
     - Avoid slashes, particularly “and/or.” They introduce ambiguity. Avoid em dashes. Putting non-restrictive relative clauses into separate sentences leads to simpler, clearer writing. Do not use smart quotes        or smart apostrophes. Use the straight versions of these marks.
   * - Redundancy
     - Avoid including unnecessary words. For example, instead of “Create a new {noun},” use “Create a {noun},” and instead of “Delete or edit an existing {noun},” use “Delete or edit a {noun}.”
   * - Word choice
     - See the Glossary section for our preferred terminology. Avoid jargon, colloquialisms, and humor. 
       Do not use non-technical words that are not commonly used, such as “and so forth,” albeit, heretofore, thus, or whilst. Be careful of commonly used phrases that introduce ambiguity. For example, instead of “When the process completes…” use “After the process completes…”

.. seealso::

   :ref:`About Open edX Documentation Standards` (concept)

   :ref:`Documentor Guidelines` (reference)

   :ref:`Documentation Maintenance Process` (reference)

   :ref:`Open edX Documentation Writing Style Guide` (reference)

   :ref:`Documentation Templates` (reference)
   
   :ref:`Writing RST` (reference)

   :ref:`Documentation Audiences` (concept)

   :ref:`Update An Existing Doc via GitHub` (how-to)

   :ref:`Add New Documentation via GitHub` (how-to)

   :ref:`Report a problem with the docs` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
