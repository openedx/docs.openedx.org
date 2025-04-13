.. _Configure Open edX Discussions Legacy:

Configure Open edX Discussions - Legacy
########################################

.. tags:: educator, how-to

.. warning:: This is the legacy way to create a discussion component (for installations running the Palm or earlier releases; the new method was released in Quince, December 2023). View the latest way to create a discussion component in :ref:`Configure Open edX Discussions`.

You can add discussion components to a unit to pose questions about other
components, such as videos or text, in the unit. A discussion component gives
learners a chance to respond to and interact with each other about a specific
subject.

Discussion topics that you create by adding discussion components in your
course are known as content-specific discussion topics.

For more information about discussions, see these topics.

* :ref:`About Course Discussions`
* :ref:`Best Practices for Moderating Course Discussions`
* :ref:`Set up Discussions in Cohorted Courses`

.. _Create a Discussion Component:

*****************************
Create a Discussion Component
*****************************

.. note:: The recommendation is to add a Text component before each discussion
   component to introduce the topic you want learners to discuss. The
   discussion component itself does not contain any text and can be easy for
   learners to overlook.

#. Under **Add New Component**, select **Discussion**.

   .. warning:: You should always use these steps to create a discussion
     component. Do not create discussion components by using the **Duplicate**
     button in Studio. Duplicated discussion components result in
     discussion topics containing the same conversations, even if users post in
     different discussions.

#. In the discussion component that appears, select **Edit**.

#. Follow the guidelines in the editor to fill in the **Category**, the
   **Display Name**, and the **Subcategory** fields.

   .. note:: Each **Category**/**Subcategory** pair for the discussion topics
      in your course must be unique.

   The value in the **Display Name** field identifies the discussion in the
   course content. The default display name for new discussion components is
   "Discussion".  Changing the default to a unique, descriptive display name
   can help you and your learners identify different topics quickly and
   accurately. If you delete the default display name and do not enter your own
   identifying name, the platform supplies "discussion" for you.

   The values in the **Category** (1) and **Subcategory** (2) fields are
   visible to learners in the list of discussion topics on the **Discussion**
   page.

   .. image:: /_images/educator_how_tos/Discussion_category_subcategory.png
    :alt: A list of discussions with the "Answering More Than Once" topic
     indented under "Getting Graded".
    :width: 400

#. Select **Save**.

.. note:: On the **Discussion** page, you cannot see category and subcategory
   names of discussion components you created until after the course has
   started and the unit is released. For more details about when discussion
   topics are visible, see :ref:`Visibility of Discussion Topics`.

.. seealso::

  :ref:`About Course Discussions` (concept)

  :ref:`Best Practices for Configuring Course Discussions` (concept)

  :ref:`Configure Open edX Discussions` (how-to)

  :ref:`Best Practices for Moderating Course Discussions` (concept)

  :ref:`Assign discussion roles` (how-to)

  :ref:`Moderate Discussions` (how-to)

  :ref:`Toggle Anonymous Discussion Posts` (how-to)

  :ref:`Learner View of the Discussion` (reference)

  :ref:`About Divided Discussions` (concept)

  :ref:`Guide to Managing Divided Discussions` (reference)

  :ref:`Set Up Divided Discussions` (how-to)

  :ref:`Set up Discussions in Cohorted Courses` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                |
+--------------+-------------------------------+----------------+--------------------------------------------------------------+
| 2025-04-13   | sarina                        | Sumac          | Since these instructions are for pre-Quince instances, they  |
|              |                               |                | will always fail on Quince and later releases.               |
|              |                               |                | No further review of this page is needed moving forward.     |
+--------------+-------------------------------+----------------+--------------------------------------------------------------+
| 03/17/2025   | Leira (Curricu.me)            | Sumac          | Fail (https://github.com/openedx/docs.openedx.org/issues/907)|
+--------------+-------------------------------+----------------+--------------------------------------------------------------+
