.. _MathJax in Studio:

MathJax for Mathematics
##############################

.. tags:: educator, reference

To produce clear and professional-looking symbols and equations in web browser,
the Open edX platform uses `MathJax <https://www.mathjax.org/>`_. MathJax automatically formats
the mathematical symbols and equations that you enter in Text and problem
components using LaTeX notation into beautiful math.

This topic provides some pointers to get you started. Many resources for
learning and using MathJax are available online, including the official
`MathJax Documentation`_. A tutorial is available on the `Mathematics meta`_
stack exchange. Additional documentation, with a testing tool, is available on
the `Tree of Math`_ site.

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
 

 :ref:`Adding MathJax` (reference)

 :ref:`Math Expression Input` (reference)

 :ref:`Math Expression Input Problem XML` (reference)

 :ref:`Adding MathJax` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
