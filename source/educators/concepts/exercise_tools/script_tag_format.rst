.. _Script Tag Format:

Script Tag Format
#################

.. tags:: educator, concept

The script tag format encloses a Python script that contains a "check function"
in a ``<script>`` tag, and adds the ``cfn`` attribute of the
``<customresponse>`` tag to reference that function.

This section contains the following information about using the ``<script>``
tag.

.. contents::
   :local:
   :depth: 1

.. _The Check Function:

The ``check`` Function
**********************

The ``check`` function in a ``<script>`` tag accepts two arguments.

* ``expect`` is the value of the ``expect`` attribute of ``<customresponse>``.
  If ``expect`` is not provided as an argument, the function must have another
  way to determine if the answer is correct.

* ``answer`` is one of the following two options.

    * The value of the answer the learner provided, if the problem only has one
      response field.

    * An ordered list of answers the learner provided, if the problem has
      multiple response fields.

The ``check`` function can return any of the following values to indicate
whether the learner's answer is correct.

* ``True``: Indicates that the learner answered correctly for all response
  fields.

* ``False``: Indicates that the learner answered incorrectly. All response
  fields are marked as incorrect.

* ``"Partial"``: Indicates that the learner's answer was partially correct. By
  default, the learner receives 50% of the points for the problem. For more
  information, see :ref:`Award Half Credit`.

* A dictionary of the form ``{ 'ok': True, 'msg': 'Message' }``. If the
  dictionary's value for ``ok`` is set to ``True``, all response fields are
  marked correct. If it is set to ``False``, all response fields are marked
  incorrect. If it is set to ``"Partial"``, the learner receives 50% of the
  problem points. The ``msg`` is displayed below all response fields, and it
  can contain XHTML markup.

* A dictionary of the form:

  .. code-block:: python

    { 'overall_message': 'Overall message',
        'input_list': [
            { 'ok': True, 'msg': 'Feedback for input 1'},
            { 'ok': False, 'msg': 'Feedback for input 2'},
            { 'ok': 'Partial', 'msg': 'Feedback for input 3'}
            ... ] }

The last form is useful for responses that contain multiple response fields. It
allows you to provide feedback for each response field individually, as well as
a message that applies to the entire response.

Example with the Script Tag
***************************

In the following example, ``<customresponse>`` tags reference the
``test_add_to_ten`` and ``test_add`` functions that are in the ``<script>``
tag.

.. Important::
 Python honors indentation. Within the ``<script>`` tag, the ``def
 check_func(expect, ans):`` line must have no indentation.


.. code-block:: xml

  <problem>

  <script type="loncapa/python">

  def test_add(expect, ans):
      try:
          a1=int(ans[0])
          a2=int(ans[1])
          return (a1+a2) == int(expect)
      except ValueError:
          return False

  def test_add_to_ten(expect, ans):
      return test_add(10, ans)

  </script>

  <p>Enter two integers that sum to 10. </p>
  <customresponse cfn="test_add_to_ten">
    <textline size="10"/><br/>
    <textline size="10"/>
  </customresponse>

  <p>Enter two integers that sum to 20: </p>
  <customresponse cfn="test_add" expect="20">
    <textline size="40" correct_answer="11" label="Integer #1"/><br/>
    <textline size="40" correct_answer="9" label="Integer #2"/>
  </customresponse>

  <solution>
    <div class="detailed-solution">
      <p>Explanation</p>
      <p>Any set of integers on the line \(y = 10 - x\) and \(y = 20 - x\)
         satisfies these constraints.</p>
      <p>You can also add images within the solution clause, like so:</p>
      <img src="/static/images/placeholder-image.png"/>
    </div>
  </solution>

  </problem>


Example of the ``check`` Function Returning a Dictionary
********************************************************

 The following example shows a ``check`` function that returns a dictionary.

.. code-block:: python

    def check(expect, answer_given):
        check1 = (int(answer_given[0]) == 1)
        check2 = (int(answer_given[1]) == 2)
        check3 = (int(answer_given[2]) == 3)
        return {'overall_message': 'Overall message',
                    'input_list': [
                        { 'ok': check1, 'msg': 'Feedback 1'},
                        { 'ok': check2, 'msg': 'Feedback 2'},
                        { 'ok': check3, 'msg': 'Feedback 3'} ] }

The function checks that the user entered ``1`` for the first input, ``2`` for
the  second input, and ``3`` for the third input. It provides feedback messages
for each individual input, as well as a message displayed below the entire
problem.

Script Tag Attributes
*********************

The following table explains the important attributes and values in the
preceding example.

.. list-table::
   :widths: 20 80

   * - ``<script type="loncapa/python">``
     - Indicates that the problem contains a Python script.
   * - ``<customresponse cfn="test_add_to_ten">``
     - Indicates that the function ``test_add_to_ten`` is called when the
       learner checks the answers for this problem.
   * - ``<customresponse cfn="test_add" expect="20">``
     - Indicates that the function ``test_add`` is called when the learner
       checks the answers for this problem and that the expected answer is
       ``20``.
   * - <textline size="10" correct_answer="3"/>
     - This tag includes the ``size``, ``correct_answer``, and ``label``
       attributes. The ``correct_answer`` attribute is optional.

.. seealso::
 :class: dropdown

 :ref:`Write Your Own Grader` (reference)

 :ref:`Create a Custom Python Evaluated Input Problem in Studio` (how to)

 :ref:`Create a Custom Python Evaluated Input Problem in Script Tag Format` (how to)

 :ref:`Create a Randomized Custom Python Evaluated Input Problem` (how to)

 :ref:`Award Partial Credit` (concept)

