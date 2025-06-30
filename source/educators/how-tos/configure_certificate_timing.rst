.. _Configure Certificate Availability and Timing:

###############################################
Configure Certificate Availability and Timing
###############################################

.. tags:: educator, how-to

.. note::
 Before you can issue certificates, the administrator for your instance of
 Open edX must configure the platform to allow course teams to generate and
 issue certificates. For more information, see
 :ref:`Enable Automatic Certificate Generation` and
 :ref:`Enable Certificates` in *Installing, Configuring, and
 Running the Open edX Platform*.

The platform can automatically generate certificates for both self-paced courses and
instructor-paced courses. When certificates become available, options for
learners to view their certificates are available on the learner dashboard,
the learner **Profile** page, and the course **Progress** page.

Earlier Open edX versions had an **Enable Student-Generated
Certificates** option in the LMS instructor dashboard; this option has
been removed.

********************************************
Configure Certificate Display Behavior
********************************************

You can specify when you want to make certificates available.

#. In Studio, on the **Settings** menu, select **Schedule & Details**.

#. From the drop-down menu, select one of the following options:

   * **Immediately upon passing**: Learners can access their certificate as soon as they achieve a passing grade above the course grade threshold. Note: learners can achieve a passing grade before encountering all assignments in some course configurations.

   * **On course end date**: Learners with passing grades can access their certificate once the end date of the course has elapsed.
   
   * **A date after the course end date**: Learners with passing grades can access their certificate after the date that you set has elapsed. For more information about how to specify a day to issue certificates, see :ref:`Specify an Alternative Certificates Available Date`.

#. Select **Save Changes**.

.. seealso::

  :ref:`About Certificates` (concept)

  :ref:`Manage Course Certificates` (how-to)

  :ref:`View Certificate Data` (how-to)

  :ref:`Manage Course Badges` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+-------------------------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                                     |
+--------------+-------------------------------+----------------+-------------------------------------------------------------------+
| 06/10/2025   | Leira (Curricu.me)            |  Sumac         | `Fail <https://github.com/openedx/docs.openedx.org/issues/1116>`_ |
+--------------+-------------------------------+----------------+-------------------------------------------------------------------+
