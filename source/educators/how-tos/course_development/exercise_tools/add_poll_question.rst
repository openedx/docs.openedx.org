.. :diataxis-type: how-to
.. _Add Poll: 

***************************
Add a Poll in edX Studio
***************************

You must :ref:`enable the poll <Enable Additional Exercises and Tools>` tool
before you add the component.

#. On the Course Outline page, open the unit where you want to add the poll.

#. Under **Add New Component** click **Advanced**, and then select **Poll**.

   The new component is added to the unit, with a default example poll that
   contains several answer fields.

   .. image:: /_images/educator_how_tos/poll_studio.png
    :alt: The poll component in Studio.
    :width: 400

#. In the new component, select **Edit**.

#. In the **Display Name** field, enter the name for the component.

#. In the **Question/Prompt** field, enter text that learners see above the
   poll. You can use Markdown in this field.

#. In the **Feedback** field, enter text that learners see after they submit a
   responses. You can use Markdown in this field.

#. In the **Private Results** field, to hide poll results from learners,
   select **True**. If you leave the default value, **False**, learners see
   poll results after they submit responses.

#. In the **Maximum Submissions** field, change the value to the number of
   times that you want to allow learners to submit responses. Enter **0** to
   allow unlimited responses.

   .. note::
    If you allow learners to submit responses more than once, you should set
    **Private Results** to **True**. Otherwise, learners will be able to change
    their responses after seeing others' responses.

#. Configure answers for the poll.

   #. In each **Answer** field, enter the answer text that learners see.

   #. You must enter either text or an image path, or both, for each answer.
      To enter an image, use the :ref:`Studio URL <File URLs>` for the image.

   #. If you use an image, you must enter useful alternative text in the
      **Image alternate text** field for non-sighted users.

   #. To add answers, select **Add answer** at the bottom of the editor. New
      answers are added at the bottom of the list.

   #. To change the order of answers, select the up and down buttons next to
      each answer.

   #. To remove an answer, select **Delete** next to the answer.

#. Select **Save**.


***************************
Editing Published Polls
***************************

Do not publish a poll until you have completed and tested it. You should
avoid changing a poll after learners have begun to use it.

If you must edit a poll after learners have submitted answers take into account
the following implications.

* If you edit the value of an answer, previous submissions are associated with
  the new answer value. This change can result in an inaccurate picture of the
  responses.

* If you change the poll so that previous submissions are invalid, by removing
  an answer, those submissions are deleted when learners next view the unit.
  Learners with invalid submissions can submit new responses.

***************************
View Poll Results
***************************

When you view the poll as a course staff member, you can view results of the
poll inside the course.

Select **View results** in the poll.

.. image:: /_images/educator_how_tos/poll_view_results.png
    :alt: A poll with the View Results button for course staff.
    :width: 400

The results of the poll are then displayed.

.. image:: /_images/educator_references/poll_with_results.png
    :alt: A poll showing results after the learner has submitted a response.
    :width: 400

.. seealso::
 :class: dropdown

  :ref:`Poll Tool` (reference)
  :ref:`Poll Tool for OLX` (reference)
  :ref:`Enable Poll in OLX` (reference)
