.. _Symbolic Response:

#################
Symbolic Response
#################

.. tags:: educator, reference

.. warning::

  Symbolic response is not a problem type exposed in Open edX Studio.

  Studio and LMS support of symbolic response is not guaranteed to work.

This topic is planned to document features that the current symbolic response
supports. In general, it allows the input and validation of math expressions,
up to commutativity and some identities.

********
Features
********

This is a partial list of features, to be revised over time.

* sub and superscripts: an expression following the ``^`` character
  indicates exponentiation. To use superscripts in variables, the syntax
  is ``b_x__d`` for the variable ``b`` with subscript ``x`` and super
  ``d``.

  An example of a problem.

  ::

    <symbolicresponse expect="a_b^c + b_x__d" size="30">
      <textline math="1"
        preprocessorClassName="SymbolicMathjaxPreprocessor"
        preprocessorSrc="/static/js/capa/symbolic_mathjax_preprocessor.js"/>
    </symbolicresponse>

  It's a bit of a pain to enter that.

* The script-style math variant. What would be outputted in LaTeX if
  ``\mathcal{N}`` was entered. This is used in some variables.

  An example::

      <symbolicresponse expect="scriptN_B + x" size="30">
        <textline math="1"/>
      </symbolicresponse>

  There is no fancy preprocessing needed, but if superscripts or
  complicated typesetting is used, that part would need to be included.


.. seealso::

  :ref:`Math Expression Input` (reference)
  
  :ref:`Math Expression Input Problem XML` (reference)

  :ref:`What is Open Learning XML?` (concept)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
