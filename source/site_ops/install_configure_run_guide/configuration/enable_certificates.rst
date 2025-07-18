.. _Enable Certificates:

############################
Enabling Course Certificates
############################

.. tags:: site operator

This topic describes how to enable and configure course certificates in your
instance of Open edX.

For information about configuring program certificates, refer to documentation
in the `edx/credentials`_ GitHub repository.

.. contents::
   :local:
   :depth: 1

****************************
Course Certificates Overview
****************************

Organizations and course teams can choose to generate certificates for learners
who pass a course. Learners can view, print, or share their certificates.

For additional information about certificates, see
:ref:`Manage Course Certificates` in the *Building and Running an
Open edX Course* guide or :ref:`Print a Web Certificate` in the
*Open edX Learner's Guide*.

To enable course certificates on your instance of Open edX, you must enable a
feature flag in both Studio and the Learning Management System and complete the
configuration tasks described in this topic.

.. Note::
  Before proceeding, review :ref:`Guidelines for Updating the Open edX
  Platform`.

************************************************
Enable Course Certificates in Studio and the LMS
************************************************

To enable certificates, modify the ``lms.yml`` and ``studio.yml``
files, which are located one level above the ``edx-platform`` directory.

#. In the ``lms.yml`` and ``studio.yml`` files, set the value of
   ``CERTIFICATES_HTML_VIEW`` within the ``FEATURES`` object  to ``true``.

   .. code-block:: none

     "FEATURES": {
         ...
         'CERTIFICATES_HTML_VIEW': true,
         ...
     }

#. Save the ``lms.yml`` and ``studio.yml`` files.

#. If it does not exist already, create the folder ``/tmp/certificates`` owned
   by the user and group ``www-data``. Depending on your configuration, this
   folder might not survive reboots, and so might need to be created by a
   script.

#. Run database migrations.


*****************************************
Configuring Course Certificates in Studio
*****************************************

Within Studio, course team members with the Admin role can create and edit a
certificate configuration that is used to generate certificates for their
course, including adding signatories and images for organization logo and
signature images for signatories. For details, :ref:`Manage Course
Certificates` in *Building and Running an Open edX Course*.


********************************************************
Configure Course Certificates for Your Open edX Instance
********************************************************

#. Access the LMS Django Administration website for your instance of Open edX.
   To do this, go to ``https://<host name of your Open edX instance>/admin``.
   For example, this might be ``https://courses.YourOrganization.com/admin``.

#. Under **Site Administration** > **Certificates**, add an HTML View
   Configuration, and select **Enabled**.

#. Set the following certificates-related parameters for your Open edX
   instance.

   * ``platform_name``
   * ``company_about_url``
   * ``company_privacy_url``
   * ``company_tos_url``
   * ``company_verified_certificate_url``
   * ``logo_src``
   * ``logo_url``

   For each course mode for which you want to offer certificates (such as
   "honor" or "verified"), define these parameters.

   * ``certificate_type``
   * ``certificate_title``
   * ``document_body_class_append``.

   Make sure the mode name matches your course mode name exactly. An example
   follows.

   For more information about course modes, also called enrollment modes
   or enrollment tracks, see :term:`Enrollment track`.

   .. code-block:: none

    {
        "default": {
            "accomplishment_class_append": "accomplishment-certificate",
            "platform_name": "YourPlatformName",
            "company_about_url":"https://www.YourOrganization.com/about-us",
            "company_privacy_url": "https://www.YourOrganization.com/our-privacy-policy",
            "company_tos_url": "https://www.YourOrganization.com/our-terms-service",
            "company_verified_certificate_url": "https://www.YourOrganization.com/about_verified_certificates",
            "logo_src": "/static/certificates/images/our_logo.svg",
            "logo_url": "www.YourOrganization.com"
        },
        "honor": {
            "certificate_type": "honor",
            "certificate_title": "Honor Certificate",
            "document_body_class_append": "is-honorcode"
        },
        "verified": {
            "certificate_type": "verified",
            "certificate_title": "Verified Certificate",
            "document_body_class_append": "is-idverified"
        },
        "base": {
            "certificate_type": "base",
            "certificate_title": "Certificate of Achievement",
            "document_body_class_append": "is-base"
        }
    }

#. Save the configuration parameters.

#. Restart the Studio and LMS processes to load the updated environment
   configurations.


.. _Discontinue Audit Certificates:

====================================
Discontinue Audit Track Certificates
====================================

Organizations that previously offered certificates to audit track learners will
no longer be able to grant certificates to these learners. Learners can
continue to audit courses, but they will not be able to earn a certificate.

For more information about course tracks, also called enrollment modes or
enrollment tracks, see :term:`Enrollment track`.


*****************************************************
Customize Certificate Templates For Your Organization
*****************************************************

Set up the templates for certificates that your organization will issue. Base
templates are included, but you must ensure that they are customized for your
organization. For example, you can change the images that appear on
certificates for each course mode that your organization supports, as well as
fonts and colors that are used on certificates.

To issue certificates in more than one language, see :ref:`Certificates in
Additional Languages`.

To display hours of effort on certificates, see :ref:`Display Hours of
Effort`.

Assets for HTML certificates exist in the following locations.

* ``lms/templates/certificates`` - this folder contains .html files for
  certificates. The file ``valid.html`` is an example of a certificate file.
  Files with names that start with an underscore, such as
  ``_certificate_footer.html``, are partial files that can be referenced in the
  main certificate .html files.

* ``lms/static/certificates`` - subfolders of this folder contain assets used
  in creating certificates, such as images, fonts, and sass/css files.

  .. note:: The organization logo on a certificate is uploaded in Studio. For
     details, see :ref:`Manage Course Certificates` in *Building
     and Running an Open edX Course*.



.. _Certificates in Additional Languages:

*******************************************
Enable Certificates in Additional Languages
*******************************************

You can configure course certificates to render in a specific language.

.. contents::
   :local:
   :depth: 1

=====================================================
Configure Course Certificates in Additional Languages
=====================================================

To enable generating course certificates in languages other than the
default language of your platform, follow these steps.

.. note:: Base certificate templates already exist for English and
      Spanish. If you want a course certificate that is different from the
      default certificate for the organization or language, create a new
      certificate template.

#. Add the language in which you want to generate certificates to
   ``EDXAPP_CERTIFICATE_TEMPLATE_LANGUAGES``
   (``edx/configuration/playbooks/roles/edxapp/defaults/main.yml``), where the
   key is the language code and the value is the name of the language.

   For example,    ``'fr':'français'``.

#. In the LMS Django Administration site for your instance of Open edX, under
   **Site Administration** > **Certificates** > **Certificate templates**, add
   a certificate template for each additional language in which you want to
   generate certificates.

#. In each certificate template, modify the configuration parameters as
   required to apply the template either to all course runs in an
   organization, or to a single course run.


   .. list-table::
      :widths: 10 35 35
      :header-rows: 1

      * - Parameter
        - To apply the template to all course runs
          in the organization
        - To apply the template to a specific course run
      * - ``Language``
        - Select the language that you want the certificate to be generated
          in.
        - Select the language that you want the certificate to be generated
          in.
      * - ``Organization ID``
        - Enter the ID for the organization whose courses should use this
          certificate template.
        - Select ``None``.
      * - ``Course Key``
        - Leave empty.
        - Enter the course key for the course run which should use this
          certificate template.
      * - ``Mode``
        - (Optional) Specify the course mode for which certificates will be
          generated using this template. If no mode is specified, this template
          is used for all course modes.
        - (Optional) Specify the course mode for which certificates will be
          generated using this template. If no mode is specified, this template
          is used for all course modes.
      * - ``Is Active``
        - Select this checkbox to make this template active.
        - Select this checkbox to make this template active.


   .. note:: If more than one certificate template would apply to a course
      run, the most specific (lowest level) template is used. For example, if
      you define a certificate template for all courses in an organization and
      another template for a specific course run, the template for the course
      run is used.

#. Save each certificate template.

#. ONLY if you are enabling additional language certificates for a specific
   course run, add a certificate generation course setting in LMS Django
   Administration, under **Site Administration** > **Certificates**.

#. In the **Course key** field of the certificate generation course setting,
   specify the course run for which you are enabling language specific
   certificate templates.

#. Select **Language specific templates enabled**, and save the configuration.


.. _Display Hours of Effort:

**********************************************
Display Hours of Effort on Course Certificates
**********************************************


To display hours of effort for a course run on a course certificate, follow
these steps.

#. Log in to the Discovery service Django Administration site for your instance
   of Open edX. To do this, go to ``https://<discovery.host name of your Open
   edX instance>/admin``. For example, this might be
   ``https://discovery.YourOrganization.com/admin``.

#. Under **Course Metadata** > **Course Runs**, locate the course run, and make
   sure there are values for the following attributes.

   * Max effort
   * Weeks to complete

#. Log in to the LMS Django Administration site for your instance of Open edX.
   To do this, go to ``https://<courses.host name of your Open edX
   instance>/admin``. For example, this might be
   ``https://courses.YourOrganization.com/admin``.

#. Under **Site Administration** > **Certificates**, add or edit a
   certificate generation course setting.

#. Select ``Yes`` for **Include hours of effort** and save the configuration.

#. Under **Site Administration** > **Certificates**, add or edit a certificate
   template.

#. In the certificate template, ensure that a ``div`` element exists that
   includes the context variable ``hours_of_effort``.

#. Save your edits to the certificate template.

.. _Enable Automatic Certificate Generation:

***************************************
Enable Automatic Certificate Generation
***************************************

It is suggested that automatic certificate generation
be enabled in order to provide the best experience for learners.
Particularly in self-paced courses (see :ref:`Enable Self Paced
Courses`), your learners might not want to wait until an instructor
initiates certificate generation; instead, they would typically expect
to be able to download their certificates as soon as they achieve a
passing grade. This can be achieved by enabling *auto_certificate_generation*
as described below.

To globally enable this functionality, you must set a `Waffle switch
<https://waffle.readthedocs.io/en/latest/types/switch.html>`_:

#. In the LMS Django Administration site for your instance of Open
   edX, under **Django-Waffle** > **Switches**, select **Add Switch**.

#. Name the switch ``certificates.auto_certificate_generation``.

#. Tick the **Active** checkbox.

#. Optionally, add a **Note** describing that the switch enables
   certificate auto-generation for self-paced courses, or any other
   information you consider necessary. The **Note** contents are never
   shown to learners.

#. Click **Save** to activate the switch.

Open edX caches the value of this Waffle switch, thus the changed
setting may take several minutes to propagate in a large installation.

In addition to this Waffle switch, automatic certificate generation
requires certain settings to be defined for the course, by a member of
the course staff. For more details, see :ref:`Configure Certificate Display Behavior` in *Building and Running an Open edX Course*.

.. _Manually Generate Certificates for a Course:

*******************************************
Manually Generate Certificates For a Course
*******************************************

To manually generate certificates for a course, run the ``manage.py`` script
with the following settings. When the script finishes running, course certificates
will have been generated for eligible learners.

#. Obtain the course ID for the course for which you are generating
   certificates. When you view course content in your browser, the course ID
   appears as part of the URL. For example, in the URL
   ``http://www.edx.org/course/course-v1:edX+demoX_Demo_2015``, the course ID
   is ``course-v1:edX+demoX_Demo_2015``. For some courses, the course ID
   contains slashes, however it will not contain beginning or trailing slashes.
   For example, a course id look like ``edX/Demox/Demo_2014``.

#. Obtain the user IDs for any learners for whom you'd like to generate course
   certificates. These can be found in the ``auth_user`` database table.

#. Run ``manage.py`` with the following settings, replacing {UserID} with a user id
   and ``{CourseID}`` with the course ID. Do not include beginning or trailing slashes.

   ``./manage.py lms --settings=production cert_generation -u {UserID} {UserID} -c {CourseID}``

   For example,

   ``./manage.py lms --settings=production cert_generation -u 123 456 -c course-v1:edX+DemoX+Demo_Course``

#. You can then view the certificates in the ``certificates_generatedcertificate`` database table.


.. include:: /links.txt

.. _edx/credentials: https://github.com/openedx/credentials


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
