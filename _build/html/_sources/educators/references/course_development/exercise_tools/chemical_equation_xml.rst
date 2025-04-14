.. _Guide to Chemical Equation Problem XML:

Guide to Chemical Equation Problem XML
#########################################

.. tags:: educator, reference


Template
********

.. code-block:: xml

  <problem>
    <startouttext/>
    <p>Problem text</p>

    <customresponse>
      <chemicalequationinput size="NUMBER" label="LABEL TEXT"/>
      <answer type="loncapa/python">

  if chemcalc.chemical_equations_equal(submission[0], 'TEXT REPRESENTING CHEMICAL EQUATION'):
      correct = ['correct']
  else:
      correct = ['incorrect']

      </answer>
    </customresponse>

    <endouttext/>

   <solution>
   <div class="detailed-solution">
   <p>Solution or Explanation Header</p>
   <p>Solution or explanation text</p>
   </div>
   </solution>
  </problem>


Tags
****

* ``<customresponse>``: Indicates that this problem has a custom response.
* ``<chemicalequationinput>``: Specifies that the answer to this problem is a
  chemical equation.
* ``<answer type=loncapa/python>``: Contains the Python script that grades the
  problem.

**Tag:** ``<customresponse>``

Indicates that this problem has a custom response. The ``<customresponse>``
tags must surround the ``<chemicalequation>`` tags.

  **Attributes**

  (none)

  **Children**

  * ``<chemicalequationinput>``
  * ``<answer>``

**Tag:** ``<chemicalequationinput>``

Indicates that the answer to this problem is a chemical equation and creates a
response field where the learner enters an answer.

  **Attributes**

  .. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - size
       - Specifies the size of the response field, in characters.
     * - label (required)
       - Contains the text of the principal question in the problem.

  **Children**

  (none)

**Tag:** ``<answer>``

Contains the Python script that grades the problem.

  **Attributes**

  .. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - type (required)
       - Must be "loncapa/python".

  **Children**

  (none)

.. seealso::
 

 :ref:`Chemical Equation` (how to) 


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
