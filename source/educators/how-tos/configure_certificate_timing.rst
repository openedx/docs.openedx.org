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

You can specify when you want to make certificates available.

* For self-paced courses, by default, certificates are generated for
  learners when they have completed enough of the course, and with a high
  enough grade, to qualify for a certificate.

  If you want to generate certificates only after learners have
  completed the course, you can disable this feature. For more information,
  see :ref:`Allow Learners to Receive Early Certificates`.

* For instructor-paced courses, three options are available.

 * By default, certificates become available to learners 48
   hours after your course end date. If you change your course end date,
   Studio automatically adjusts the date for certificates as well.

 * You can specify a different date to make certificates available. For more
   information, see :ref:`Specify an Alternative Certificates Available
   Date`.

 * You can allow learners to receive their certificates when they have
   completed enough of the course, and with a high enough grade, to qualify
   for a certificate. For more information, see :ref:`Allow Learners to
   Receive Early Certificates`.

.. _Issue Certificates on a Specified Date:

**************************************
Issue Certificates on a Specified Date
**************************************

If you do not want to generate certificates 48 hours after the course
end date, you can specify the date when you want the platform to generate
certificates. You can change this date at any time.

For more information about how to specify a day to issue certificates, see
:ref:`Specify an Alternative Certificates Available Date`.

.. _Allow Learners to Receive Early Certificates:

********************************************
Allow Learners to Receive Early Certificates
********************************************

If the administrator has configured the site correctly (see
:ref:`Enable Automatic Certificate Generation` in
*Installing, Configuring, and Running the Open edX Platform*),
self-paced courses issue certificates to learners as soon as learners
have completed enough of the course, with a high enough grade, to earn
a certificate. You do not have to change any settings.

Earlier Open edX versions had an **Enable Student-Generated
Certificates** option in the LMS instructor dashboard; this option has
been removed.

.. _Allow Learners to Download Certificates:

*********************************************
Allow Learners to Download Early Certificates
*********************************************

To allow learners to download early certificates, you modify the
**Certificates Display Behavior** advanced setting in Studio.

#. In Studio, on the **Settings** menu, select **Advanced Settings**.

#. On the **Advanced Settings** page, locate **Certificates Display Behavior**.

#. In the **Certificates Display Behavior** field, enter ``"early_no_info"``.
   Be sure that you include the double quotation marks.

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
