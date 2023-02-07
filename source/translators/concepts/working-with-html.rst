Working With HTML
#################

Translating strings for the Open edX project is more complicated than simply
translating sentences from one language to another. Sometimes, sentences (or
“strings”) will contain HTML markup tags. It is very important to understand how
to deal with HTML markup.

Often, strings in the platform will contain HTML Tags.  Tags are usually single
words that are surrounded by angle brackets and may contain a forward slash.
Below are some examples of tags you might see:

.. code::

   <b>

   <a>

   <h1>

   </div>

   <figure>

If there are tags in the strings you are translating, you should not translate
the content inside the tags.  This includes adding or removing spaces inside the
tags.  The spacing matters, if you change ``</a>`` to ``</ a>`` it will break
the website.

Examples may help you better understand what to do in these situations so we
recommend checking out
:ref:`the HTML Section of the Translators Reference <translators reference html>`

.. seealso::

   * :ref:`HTML Reference <translators reference html>`

   * :doc:`working-with-placeholders`
