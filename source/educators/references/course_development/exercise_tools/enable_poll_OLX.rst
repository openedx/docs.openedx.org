.. _Enable Poll in OLX:

Enable the Poll Tool in OLX
############################

.. tags:: educator, reference

.. note:: Alternatively, you can use OLX to enable the poll tool.

To enable polls in your course, you edit the XML file that defines
the course structure.

Open the XML file for the course in the ``course`` directory. In the ``course``
element's ``advanced-modules`` attribute, add the string ``poll``.

For example, the following XML code enables polls in a course.

.. code-block:: xml

  <course advanced_modules="[&quot;survey&quot;,
      &quot;poll&quot;]" display_name="Sample Course"
      start="2015-01-01T00:00:00Z">
      ...
  </course>

.. _Add Poll in OLX:   

***************************
Add a Poll in OLX
***************************

To add a poll XBlock in OLX, you create the ``poll`` element. You can embed
the ``poll`` element in the ``vertical`` element, or you can create the
``poll`` element as a standalone file that you reference in the vertical.

The following example shows the OLX definition for a poll with four answers.

.. code-block:: xml

  <poll url_name="f4ae7de0006f426aa4eed4b0b8112da5" xblock-family="xblock.v1"
    feedback="Feedback"
    display_name="Poll"
    private_results="false"
    question="What is your favorite color?"
    max_submissions="1"
    answers="[
               [&quot;R&quot;,
                 {
                   &quot;img&quot;: &quot;/static/image.png&quot;,
                   &quot;img_alt&quot;: &quot;Alt 1&quot;,
                   &quot;label&quot;: &quot;Red&quot;
                 }
               ],
               [&quot;B&quot;,
                 {
                   &quot;img&quot;: &quot;/static/image.png&quot;,
                   &quot;img_alt&quot;: &quot;Alt 2&quot;,
                   &quot;label&quot;: &quot;Blue&quot;
                 }
               ],
               [&quot;G&quot;,
                 {
                   &quot;img&quot;: &quot;/static/image.png&quot;,
                   &quot;img_alt&quot;: &quot;Alt3&quot;,
                   &quot;label&quot;: &quot;Green&quot;
                 }
               ],
               [&quot;O&quot;,
                 {
                   &quot;img&quot;: &quot;/static/image.png&quot;,
                   &quot;img_alt&quot;: &quot;Alt 4&quot;,
                   &quot;label&quot;: &quot;Other&quot;
                 }
               ]
             ]
  "/>

==========================
poll Element Attributes
==========================

The following table describes the attributes of the ``poll`` element.

.. list-table::
     :widths: 20 80

     * - Attribute
       - Description
     * - ``url_name``
       - The unique identifier of the poll.
     * - ``xblock-family``
       - The XBlock version used. Must be ``xblock.v1``.
     * - ``private_results``
       - Whether the poll results are shown to learners (``true``) or not
         (``false``).
     * - ``display_name``
       - The display name for the poll.
     * - ``question``
       - The prompt for the poll.
     * - ``feedback``
       - The text shown to learners after they submit a response.
     * - ``max_submissions``
       - The number of times a learner can submit poll answers.  Use ``0`` to
         allow unlimited submissions. If you use a value other than ``1``, set
         ``private_results`` to ``true``. Otherwise, learners will be able to
         change their responses after seeing others' responses.
     * - ``answers``
       - An array of answers in the poll. Each answer has a unique
         identifier, and a dictionary that defines values for the following
         names.

         * ``img``, the static URL of the answer image.
         * ``img_alt``, the alternative text for the image.
         * ``label``, the answer text.

         Each answer must have a value for ``img`` or ``label``, or both.

.. seealso::
 :class: dropdown

 :ref:`Poll Tool` (reference)

 :ref:`Add Poll` (how to)

 :ref:`Poll Tool for OLX` (reference)