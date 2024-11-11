.. _Enable Survey OLX:

======================================
Enable the Survey Tool in OLX
======================================

.. tags:: educator, reference

To enable the survey tool, you edit the XML file that defines the course
structure.

Open the XML file for the course in the ``course`` directory. In the ``course``
element's ``advanced-modules`` attribute, add the string ``survey``.

For example, the following XML code enables the survey tool.

.. code-block:: xml

  <course advanced_modules="[&quot;survey&quot;,
      &quot;poll&quot;]" display_name="Sample Course"
      start="2015-01-01T00:00:00Z">
      ...
  </course>

***************************
Add a Survey in OLX
***************************

To add a survey XBlock in OLX, you create the ``survey`` element. You can embed
the ``survey`` element in the ``vertical`` element, or you can create the
``survey`` element as a stand-alone file that you reference in the vertical.

The following example shows the OLX definition for a survey with two questions.

.. code-block:: xml

  <survey
    url_name="unique identifier for the survey"
    xblock-family="xblock.v1"
    questions="[
                 [&quot;unique code for question 1&quot;,
                   {
                     &quot;img&quot;: &quot;Static URL to image&quot;,
                     &quot;img_alt&quot;: &quot;Alternative text for image&quot;,
                     &quot;label&quot;: &quot;Text of question 1&quot;
                   }
                 ],
                 [&quot;unique code for question 2&quot;,
                   {
                     &quot;img&quot;: &quot;Static URL to image&quot;,
                     &quot;img_alt&quot;: &quot;Alternative text for image&quot;,
                     &quot;label&quot;: &quot;Text of question 2&quot;
                    }
                  ]
                ]"
    feedback="Feedback displayed to learner after submission"
    private_results="false"
    block_name="Display name for survey"
    max_submissions="1"
    answers="[
              [
                &quot;Unique identifier for answer 1&quot;,
                &quot;Answer text&quot;
              ],
              [
                &quot;Unique identifier for answer 2&quot;,
                &quot;Answer text&quot;
              ]
            ]"
  />

==========================
survey Element Attributes
==========================

The following table describes the attribute of the ``survey`` element.

.. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - ``url_name``
       - The unique identifier of the survey.
     * - ``xblock-family``
       - The XBlock version used. Must be ``xblock.v1``.
     * - ``questions``
       - An array of questions in the survey. Each question has a unique
         identifier, and a dictionary that defines values for the following
         names.

         * ``img``, the static URL of the question image.
         * ``img_alt``, the alternative text for the image.
         * ``label``, the question text.

         Each question must have a value for ``img`` or ``label``, or both.
     * - ``answers``
       - An array of answers in the survey. Each answer has a unique
         identifier, and a dictionary that defines values for the following
         names.

         * ``img``, the static URL of the answer image.
         * ``img_alt``, the alternative text for the image.
         * ``label``, the answer text.

         Each answer must have a value for ``img`` or ``label``, or both.
     * - ``feedback``
       - The text shown to learners after they submit a response.
     * - ``private_results``
       - Whether the survey results are shown to learners (``true``) or not
         (``false``).
     * - ``block_name``
       - The display name for the survey.
     * - ``max_submissions``
       - The number of times a learner can submit survey answers.  Use ``0`` to
         allow unlimited submissions. If you use a value other than ``1``, set
         ``private_results`` to ``true``. Otherwise, learners will be able to
         change their responses after seeing others' responses.

.. seealso::
 :class: dropdown

 :ref:`Survey Tool` (how to)