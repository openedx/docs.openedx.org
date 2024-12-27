.. _Problem with Adaptive Hint XML:

Problem with Adaptive Hint XML
###############################

.. tags:: educator, reference

Template
*********

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
	  print 'hint_fn called, ans=', ans
	  hint = ''
	  if 'incorrect answer 1' in ans:
	     hint = 'hint for incorrect answer 1'
	  elif 'incorrect answer 2' in ans:
	     hint = 'hint for incorrect answer 2'

	  if hint:
	    hint = "&lt;font color='blue'&gt;Hint: {0}&lt;/font&gt;".format(hint)
	    new_cmap.set_hint_and_mode(aid,hint,'always')
	</script>
	    <p>TEXT OF PROBLEM</p>
	    <p>
	      <customresponse cfn="test_str" expect="ANSWER">
	        <textline correct_answer="answer" label="LABEL TEXT"/>
	        <hintgroup hintfn="hint_fn"/>
	      </customresponse>
	    </p>
	  </text>
	</problem>

.. note:: If the hints that you supply include characters, the letters must be
 lowercase.


Tags
******

* ``<text>``: Surrounds the script and text in the problem.
* ``<customresponse>``: Indicates that this problem has a custom response.
* ``<textline>``: Creates a response field in the LMS where the student enters
  a response.
* ``<hintgroup>``: Specifies that the problem contains at least one hint.

**Tag:** ``<customresponse>``

  **Attributes**

  (none)

  **Children**

     * ``<textline>``
     * ``<hintgroup>``

**Tag:** ``<textline>``

  **Attributes**

  .. list-table::
     :widths: 20 80
     :header-rows: 1

     * - Attribute
       - Description
     * - label (required)
       - Contains the text of the problem.
     * - size (optional)
       - Specifies the size, in characters, of the response field in the LMS.
     * - hidden (optional)
       - If set to "true", students cannot see the response field.
     * - correct_answer (optional)
       - The answer to the problem. To supply a correct_answer value that
         includes letters, all letters **must be lowercase**. (Students'
         responses to the problem are not case sensitive. They can contain both
         uppercase and lowercase letters.)

  **Children**

  (none)

**Tag:** ``<hintgroup>``

  **Attributes**

  .. list-table::
     :widths: 20 80
     :header-rows: 1

     * - Attribute
       - Description
     * - hintfn
       - Must be set to **hint_fn** (that is, the tag must appear as
         ``<hintgroup hintfn="hint_fn"/>``).

.. seealso::
 :class: dropdown

 :ref:`Problem with Adaptive Hint` (how to)