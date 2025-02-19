.. _Create a Poll via OLX:

Create a Poll (via OLX)
########################

.. tags:: educator, how-to

.. note:: If you choose to edit polls via OLX, we
 recommend that you create a backup copy of your course before you create the
 poll. We also recommend that you only edit the files that will contain polls
 in the text editor if you are very familiar with editing XML.

To work with polls without OLX, see :ref:`Enable the Poll Tool` and :ref:`Add Poll`.

**********************************
Enable the Poll Tool (via OLX)
**********************************

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


*******************************************
Add the Poll Component to a Unit (via OLX)
*******************************************

#. In Studio, navigate to the unit where you want to create the poll.

#. Click the **Edit** button.

#. In the unit where you want to create the poll, create components that
   contain all the content that you want *except* for the poll. Make a note of
   the 32-digit unit ID that appears in the **Unit Identifier** field under
   **Unit Location**.

#. Export your course. For information about how to do this, see
   :ref:`Export a Course`. Save the .tar.gz file that contains
   your course in a memorable location so that you can find it easily.

#. Locate the .tar.gz file that contains your course, and then unpack the
   .tar.gz file so that you can see its contents in a list of folders and
   files.

   - To do this on a Windows computer, you need to download a third-party
     program. For more information, see `How to Unpack a tar File in Windows
     <https://www.haskell.org/haskellwiki/How_to_unpack_a_tar_file_in_Windows>`_,
     `How to Extract a Gz File <https://www.wikihow.com/Extract-a-Gz-File>`_,
     `The gzip Home Page <http://www.gzip.org/>`_, or the `Windows
     <http://www.ofzenandcomputing.com/how-to-open-tar-gz-files/#windows>`_
     section of the `How to Open .tar.gz Files
     <http://www.ofzenandcomputing.com/how-to-open-tar-gz-files/>`_ page.

   - For information about how to do this on a Mac, see the `Mac OS X <http://www.ofzenandcomputing.com/how-to-open-tar-gz-files/#mac-os-x>`_ section of the `How to Open .tar.gz Files <http://www.ofzenandcomputing.com/how-to-open-tar-gz-files/>`_ page.

#. In the list of folders and files, open the **Vertical** folder.

   .. note:: If your unit is not published, open the **Drafts** folder, and then open the **Vertical** folder in the **Drafts** folder.

#. In the **Vertical** folder, locate the .xml file that has the same name as
   the unit ID that you noted in step 1, and then open the file in a text
   editor such as Sublime 2. For example, if the unit ID is
   e461de7fe2b84ebeabe1a97683360d31, you open the
   e461de7fe2b84ebeabe1a97683360d31.xml file.

   The file contains a list of all the components in the unit, together with
   the URL names of the components. For example, the following file contains an
   Text component followed by a discussion component.

   .. code-block:: xml

       <vertical display_name="Test Unit">
        <html url_name="b59c54e2f6fc4cf69ba3a43c49097d0b"/>
        <discussion url_name="8320c3d511484f3b96bdedfd4a44ac8b"/>
       </vertical>

#. Add the following poll code in the location where you want the poll. Change
   the text of the prompt to the text that you want.

   .. code-block:: xml

    <poll_question display_name="Poll Question">
      <p>Text of the prompt</p>
      <answer id="yes">Yes</answer>
      <answer id="no">No</answer>
    </poll_question>

   In the example above, if you wanted your poll to appear between the HTML
   component and the discussion component in the unit, your code would resemble
   the following.

   .. code-block:: xml

     <vertical display_name="Test Unit">
      <html url_name="b59c54e2f6fc4cf69ba3a43c49097d0b"/>
      <poll_question display_name="Poll Question">
        <p>Text of the prompt</p>
        <answer id="yes">Yes</answer>
        <answer id="no">No</answer>
      </poll_question>
      <discussion url_name="8320c3d511484f3b96bdedfd4a44ac8b"/>
     </vertical>

#. After you add the poll code, save and close the .xml file.

#. Re-package your course as a .tar.gz file.

#. In Studio, re-import your course. You can now review the poll question and
   answers that you added in Studio.

.. note::

  * Although polls render correctly in Studio, you cannot edit them in Studio.
    You will need to follow the export/import process outlined above to make
    any edits to your polls.

  * A .csv file that contains student responses to the problem is not currently
    available for polls. However, you can obtain the aggregate data directly in
    the problem.

******************************
OLX Poll Element Attributes
******************************

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

**************************************
Example Poll OLX with Four Questions
**************************************

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



.. seealso::
 

 :ref:`Guide to the Poll Tool via OLX` (reference)
 
 :ref:`Enable the Poll Tool` (how-to)

 :ref:`Add Poll` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
