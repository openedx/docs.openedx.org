Working With Placeholders
#########################

Strings in programs sometimes need to have data inserted into them before being
displayed to the user. Data placeholders label the places in the string where
the data will go.

Placeholders come in a few different forms. Often, they are named so that data
will be placed into the proper placeholder. Please familiarize yourself with all
the different forms to make your translation successful.

.. list-table::
   :header-rows: 1

   * - Placeholder Forms
   * - ``{student_name}``

   * - ``%(student_name)s``

   * - ``<%= student_name %>``

The placeholder string inside of the braces will give you clues as to what type
of data will be presented in the final string. For example, {student_name} is
replaced with the name of a student, whereas {contact_email} is replaced with an
email address that users can use to contact us. This will give you some context
when you are translating sentences with placeholders.

When dealing with placeholders, you must follow these rules.

* Do not translate the placeholder (for example, changing ``{day}`` to ``{día}``).

* Do not alter or remove the punctuation of the placeholder string (for example,
  changing a ``_`` to a ``-``).

* Do not alter the capitalization of the placeholder string (for example,
  changing ``{day}`` to ``{Day}``).

* Do not alter the spacing of the placeholder string (for example, changing
  ``{day}`` to ``{ day }``).

* You may rearrange the order of these strings, depending on the requirements of
  the target language.

   * For example, in English the name of the month precedes the day (January
     23), while in Spanish, the day precedes the month (23 de enero).

Examples may help you better understand what to do in these situations, so we
recommend checking out the :ref:`Placeholders Section of the Translators
Reference <translators reference placeholders>`

.. seealso::

   * :ref:`Placeholders Reference <translators reference placeholders>`

   * :doc:`working-with-html`
