.. _Problem with Adaptive Hint:

Problem with Adaptive Hint
##########################

.. tags:: educator, how-to

A problem with an adaptive hint evaluates a student's response, then gives the
student feedback or a hint based on that response so that the student is more
likely to answer correctly on the next attempt. These problems can be text
input problems or single select problems.

.. image:: /_images/educator_how_tos/ProblemWithAdaptiveHintExample.png
 :alt: Image of a problem with an adaptive hint

Create a Problem with an Adaptive Hint
**************************************

To create the problem illustrated above, follow these steps.

#. In the unit where you want to create the problem, click **Problem**
   under **Add New Component**.
#. In the problem editor, select **Advanced problem types**. Then select
   **Problem with Adaptive Hint**.
#. In the advanced problem editor, replace the example code with the code below.
#. Click **Save**.

.. code-block:: xml

	<problem>
		<text>
			<script type="text/python" system_path="python_lib">
	def test_str(expect, ans):
	  print(expect, ans)
	  ans = ans.strip("'")
	  ans = ans.strip('"')
	  return expect == ans.lower()

	def hint_fn(answer_ids, student_answers, new_cmap, old_cmap):
	  aid = answer_ids[0]
	  ans = str(student_answers[aid]).lower()
	  print('hint_fn called, ans=', ans)
	  hint = ''
	  if '0.05' in ans:
	     hint = 'Make sure you enter your answer in cents'

	  if hint:
	    hint = "&lt;font color='blue'&gt;Hint: {0}&lt;/font&gt;".format(hint)
	    new_cmap.set_hint_and_mode(aid,hint,'always')
			</script>
			<p>If a bat and a ball cost $1.10 together, and the bat costs $1.00 more than the
			ball, how much does the ball cost? Enter your answer in cents, and include only
			the number (that is, do not include a $ or a ¢ sign).</p>
			<p>
				<customresponse cfn="test_str" expect="5">
					<textline correct_answer="5" label="How much does the ball cost?"/>
					<hintgroup hintfn="hint_fn"/>
				</customresponse>
			</p>
		</text>
	</problem>

.. seealso::
 :class: dropdown

 :ref:`Problem with Adaptive Hint XML` (reference)
