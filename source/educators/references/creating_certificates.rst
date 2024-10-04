.. :diataxis-type: reference

.. _Setting Up Certificates:

#################################
Setting Up Certificates in Studio
#################################

This section describes how to create and manage certificates for your course.


  .. note::
   Before you can issue certificates, the administrator for your instance of
   Open edX must configure the platform to allow course teams to generate and
   issue certificates. For more information, see
   :ref:`Enable Certificates <Enable Certificates>` in *Installing, Configuring, and
   Running the Open edX Platform*.

For more information about certificates, see these additional topics.

* :ref:`Obtaining Certificate Data<Reporting Certificate Data>`
* :ref:`Ending a Course<Checking Student Progress and Issuing Certificates>`


For information about awarding badges for your course, see :ref:`Enable or
Disable Badges for Your Course<Enable Badges in Course>`.

.. _Overview:

********
Overview
********

Using Studio, you create and manage the certificates that learners can earn in
your course.

The platform can automatically generate certificates as each learner
passes the course for both self-paced and instructor-paced courses.

* For self-paced courses, certificates are available immediately after they
  are generated.
* For instructor-paced courses, certificates become available 48 hours after
  your course end date by default. You can also specify a different date to
  make certificates available. For more information, see :ref:`Specify an
  Alternative Certificates Available Date <Specify an
  Alternative Certificates Available Date>`.

When certificates become available, options for learners to view their
certificates are available on the learner dashboard,
the learner **Profile** page, and the course **Progress** page.

For more information about issuing certificates, see :ref:`Issuing
Certificates <Checking Student Progress and Issuing Certificates>`.

The design of certificates for your course, including your institution's
logo, are configured on your instance of Open edX. For more information, see
:ref:`Enable Certificates <Enable Certificates>` in *Installing, Configuring, and
Running the Open edX Platform*.


.. The course start date limitation is not published for partners at this time.
.. Confirmed March 9, 2017 that there's no hard requirement for having
.. activated certs before edX course starts. Although there is a procedural
.. requirement for announcing activated certs, courses are able to start if
.. they have deactivated certs.



   .. note:: If your course is configured to issue certificates, you cannot
    start the course until the required certificates are
      :ref:`activated<Activate a Certificate>`.

       For information about starting the course, see :ref:`Guidelines for
       Start and End Dates <Guidelines for
       Start and End Dates>`.

