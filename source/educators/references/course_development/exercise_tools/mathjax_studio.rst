.. :diataxis-type: reference
.. _MathJax in Studio:

##############################
MathJax for Mathematics
##############################

To produce clear and professional-looking symbols and equations in web browser,
edX uses `MathJax <https://www.mathjax.org/>`_. MathJax automatically formats
the mathematical symbols and equations that you enter in Text and problem
components using LaTeX notation into beautiful math.

This topic provides some pointers to get you started. Many resources for
learning and using MathJax are available online, including the official
:ref:`MathJax Documentation`. A tutorial is available on the :ref:`Mathematics meta`
stack exchange. Additional documentation, with a testing tool, is available on
the :ref:`Tree of Math` site.

A MathJax equation can appear with other text in the paragraph (inline format)
or on its own dedicated line (display format).

For inline equations, you can do either of the following.

* Surround your MathJax expression with backslash and parentheses characters.

    ``\( equation \)``

* Surround your MathJax expression with ``[mathjaxinline]`` tags. Note that
  these tags use brackets (``[ ]``).

    ``[mathjaxinline] equation [/mathjaxinline]``

For display equations, you can do either of the following.

* Surround your MathJax expression with backslash and bracket characters.

    ``\[ equation \]``

* Surround your MathJax expression with ``[mathjax]`` tags. Note that these
  tags use brackets(``[ ]``)

    ``[mathjax] equation [/mathjax]``

.. seealso::
 :class: dropdown

  :ref:`Adding MathJax` (reference)