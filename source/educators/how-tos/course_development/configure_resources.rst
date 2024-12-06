.. _Configure Resources:

####################################
Configuring Applications & Resources
####################################

.. tags:: educator, how-to

As a best practice, you should avoid changing the visibility of your course pages after the course starts.
For example, your course includes the Wiki page when it starts. A learner adds a page to the course wiki,
and adds a browser bookmark to that page. If you later hide the Wiki page, the learner’s browser bookmark will continue to provide access to the entire course wiki.

Included below are detailed instructions for the configuration of applications and resources that have additional settings and options.

.. _Discussion Configuration:

***************************************
Configuring the Discussions application
***************************************

There are several configuration options available to the Discussions application.
Many basic configuration options are provided within Studio’s Pages & Resources area, and moderation capabilities
are available to instructors, moderators, and community TAs directly from the Discussions application.
Included below are details about both the configuration options and management tools.

To change how the discussion experience is configured, follow these steps:

#. In **Studio**, from the Content menu select **Pages & Resources**.
#. Click the gear icon on the **Discussion** card shown on this page.
#. From the **Configure discussion** modal, adjust any of the configuration settings as described below to fit your course needs.
#. Select **Apply** to save your configuration changes.

The discussion configuration experience is comprised of two steps: provider selection and provider configuration.
By default, courses are created with the discussion experience and its default configuration.
Other providers and configuration options can be selected to fit the needs of courses.

**Step 1: Provider Selection**

In this step, educators can select to use the default discussion experience or LTI based integrations with other providers.
Below the grid of available providers is a table summarizing the features each integration provides.

**Step 2: Configuration Options**

Each provider supports its own set of features depending on the discussion features they support. The discussion application has various settings and controls that are described below.
All integrations use LTI 1.1 configuration, and may additionally support platform settings from the list below. Any special instructions or details specific to a given provider are described in this step as well.

**Anonymous Posting**

If this setting is enabled, learners can create posts that are anonymous to all users.

**Allow Anonymous Discussion Posts to Peers**

When enabled learners will be able to post anonymously to other peers but all posts will be visible to course staff.

**General Discussion Topics**

It is possible to include general topics not associated with the course content structure. All courses have an initial general topic by default to start that can be renamed.

**Discussion Blackout Dates**

Course teams can specify one or multiple times during which the discussion forums are not available for new content additions. This can be helpful during exam periods or other course time periods.


.. _Wiki Configuration:

********************************
Configuring the Wiki application
********************************

For instructions on how to enable the wiki application see :ref:`11.3.2.3 Enabling the Wiki Application<Enable Wiki>`.

You can control access to the wiki in various ways: by changing access to the wiki as a whole,
by changing the read/write permissions settings of articles within the wiki, or by locking articles.

To change access to the course wiki, follow these steps.

#. In Studio, from the **Content** menu select **Pages & Resources**.
#. Click the gear icon on the **Wiki** card shown on this page.
#. From the **Configure** wiki modal, check or uncheck the toggle of the **Enable public wiki access** setting.
#. Select **Apply** to save your configuration changes.

The **Enable public wiki** access wiki setting is disabled by default, meaning that only course team members and
enrolled learners can see the course wiki. If you enable this setting, then any registered user can access the
course wiki, even if they are not enrolled in your course. However, public users would have to explicitly navigate
to your wiki via the edX-wide wiki structure, or a link that has been provided to them.

.. _Teams Configuration:

**********************************
Configuring the Teams application
**********************************

Additional management and configuration of the teams application can be done through the main Team application tab
in the learner experience, and is detailed in :ref:`12.4.1 Using the Teams application<Teams Setup>`.

.. _ORA Coursewide Settings:

**********************************************************
Configuring Course-level Open Response Assessment Settings
**********************************************************

To simplify the management of Open Response Assessment (ORA) problems, a card on this page provides a way to enable
certain course-wide overrides. Rather than going through each ORA in a course individually, these overrides allow
course staff to enable certain new features course-wide.

**Flexible Peer Grading**

This setting enables Flexible Peer Grade Averaging for all peer-graded ORA assignments across the course, without needing
to manually edit each individual problem.

To learn about Flexible Peer Grading and the course override setting, see  :ref:`Flexible Peer Grade Averaging`

.. seealso::
 :class: dropdown

 :ref:`Adding Pages to a Course` (how to)

 :ref:`Discussions` (concept)

 :ref:`About Course Wiki` (reference)

 :ref:`Teams Overview <CA_Teams_Overview>` (concept)

 :ref:`Open Response Assessments` (concept)