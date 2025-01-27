.. _Award Partial Credit:

Award Partial Credit for a Custom Python-Evaluated Input Problem 
#################################################################

.. tags:: educator, how-to

You can configure a custom Python-evaluated input problem so that learners
who give a partially correct answer receive partial credit for the problem.
You can award 50% of the points for the problem, or you can award a different
percentage of points. For more information, see the following sections.

* :ref:`Award Half Credit`
* :ref:`Award a Percentage of Credit`

.. _Award Half Credit:

Award Half Credit
*****************

You can configure a problem to award 50% of the possible points. To provide a
learner with a more granular score, see `Award a Percentage of Credit`_.

The ``check`` function must return the value ``"Partial"`` in one of the
following ways.

* Return the value ``"Partial"`` directly.

* Return the value ``"Partial"`` in the dictionary that is returned, in the
  following form.

  ``{ 'ok': 'Partial', 'msg': 'Message' }``

* Return the value ``"Partial"`` as part of the input list for multi-part
  problems.

  .. code-block:: python

    { 'overall_message': 'Overall message',
        'input_list': [
            { 'ok': True, 'msg': 'Feedback for input 1'},
            { 'ok': False, 'msg': 'Feedback for input 2'},
            { 'ok': 'Partial', 'msg': 'Feedback for input 3'}
            ... ] }

With all of these options, ``True`` awards learners with 100% of the available
points for the problem, ``'Partial'`` with 50%, and ``False`` with 0%.

For more information about ``check`` function return values, see :ref:`The Check Function`.

.. _Award a Percentage of Credit:

Award a Percentage of Credit
****************************

You can configure a problem to return a percent value as a grade. This method
provides greater flexibility in assigning the learner a score than
:ref:`awarding half credit<Award Half Credit>`.

In the following example, the learner's score equals the answer divided by 100.

.. image:: /_images/educator_references/partial-credit-python-problem.png
 :alt: An image of a write-your-own-grader problem that provides partial
     credit.

The following code shows the configuration of this problem.

.. code-block:: xml

  <problem>
  <p>In the following problem, the learner receives a score that equals the
     answer / 100. If the learner's answer is greater than 100 or less than 0,
     the score equals 0.</p>

  <script type="loncapa/python">

  def give_partial_credit(expect, ans):
    ans = float(ans)
    if ans &gt; 100 or ans &lt; 0:
        # Assign a score of zero if the answer is less than zero or over 100.
        ans = 0
    grade = ans/100
    return {
        'input_list': [
           { 'ok': True, 'msg': 'Your grade is ' + str(ans) + '%', 'grade_decimal':grade},
        ]
    }
  </script>

  <p>Enter a number beween 0 and 100.</p>
  <customresponse cfn="give_partial_credit">
    <textline points="100" size="40" label="Ans1"/><br/>
  </customresponse>
  </problem>

This example illustrates the following points.

* The ``points`` attribute of the ``<customresponse>`` element specifies that
  the question is worth 100 points.

* The ``give_partial_credit`` function checks that the answer is between 0 and
  100, and if so divides the learner's answer by 100 to determine the grade.

* The ``input_list`` that is returned specifies that:

  * The answer is acceptable and can receive partial or full credit, with the
    item ``'ok': True``.

  * The learner receives the message ``Your grade is`` followed by the percent
    grade, with the item ``'msg': 'Your grade is ' + str(ans) + '%'``.

  * The grade assigned is the learner's answer divided by 100, with the item
    ``'grade_decimal':grade``.

You can enhance and apply this example for your own partial credit problems.

.. seealso::
 :class: dropdown

 :ref:`Write Your Own Grader` (reference)

 :ref:`Create a Custom Python Evaluated Input Problem in Studio` (how to)

 :ref:`Create a Custom Python Evaluated Input Problem in Script Tag Format` (how to)

 :ref:`Create a Randomized Custom Python Evaluated Input Problem` (how to)

 :ref:`Script Tag Format` (concept)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
