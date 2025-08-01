
.. _Manage Course Certificates:

##########################
Manage Course Certificates
##########################

.. tags:: educator, how-to

.. contents::
 :local:
 :depth: 1

.. youtube:: 5Ys-E5K0_NY

Before you can create certificates, you must ensure web certificates are enabled
for your course. Web certificates are enabled by default for new courses, however
older courses may need to have them enabled.

#. From the **Settings** menu, select **Advanced Settings**.

#. Click **Show Deprecated Settings**.

#. In the **Certificate Web/HTML View Enabled** field, enter ``true``.

#. At the bottom of the page, select **Save Changes**.

In addition to enabling web certificates for your course, you have to add
a course mode for the course you wish to create a certificate for.

#. Access the LMS Django Administration website for your instance of
   Open edX. To do this, go to
   ``https://<host name of your Open edX instance>/admin``. For example,
   this might be ``https://courses.YourOrganization.com/admin``.

#. Under **Course Modes** > **Course modes**, add a new course mode for
   course you want to create a certificate for.

   - e.g. Add course mode 'honor' to the course you want to enable certificates for
   - .. image:: /_images/educator_how_tos/change_course_mode.png
        :alt: The change course mode selection screen, highlighting the dropdown menu for "Mode:"


.. note:: Different certificate types are available with the different
   course modes.

   See :term:`Enrollment Track` for more information
   about different course modes or certificate types.


.. _Create a Certificate:

********************
Create a Certificate
********************

To create a certificate for your course, follow these steps.

#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the **Certificates** page, select **Add your first certificate** or **Add
   a new certificate**.

#. Add a signatory for each person associated with the course or organization
   whose name and title you want to appear on the certificate. You must specify
   at least one signatory. You can add as many signatories as needed.


#. Optionally, upload an image file showing the signature of each signatory.

      The image file must be a transparent .png file, 450px by 150px.

#. When you have finished creating your certificate, select **Create**.

   You can :ref:`preview the certificate<Preview a Certificate>` to see how it
   will appear to a learner taking the course in the selected mode.

   Your course certificate is not available for issuing to learners until it is
   :ref:`activated<Activate a Certificate>`.


.. _Preview a Certificate:

********************
Preview Certificates
********************

After you have finished editing your certificate, you can preview a certificate
for verification purposes. You select from the available course modes (such as
"verified") to see how a certificate will appear to a learner taking the course
in the selected mode.

#. In Studio, from the **Settings** menu, select **Certificates**.

#. On the **Certificates** page, select the course mode of the certificate you
   want to preview, then click **Preview Certificate**.

   You see the web view for the certificate, as a learner in the selected
   course mode would see it.

After previewing the certificate, you can :ref:`edit the certificate<Edit Course
Certificates>` further or :ref:`activate your certificate<Activate a
Certificate>`.


.. _Activate a Certificate:

**********************
Activate a Certificate
**********************

When you have verified your certificate, a course team member with the Admin or
Staff role can activate the certificate.

.. note::
  Course team members without the Admin or Staff role cannot activate a
  certificate.

To activate a certificate, follow these steps.

#. Make sure that you have the Admin or Staff role for the course. For more
   information, see :ref:`Guide to Course Team Roles`.

#. In Studio, on the **Settings** menu, select **Certificates**.

#. On the **Certificates** page, select **Activate**.

After certificates are activated, learners in your course who attain a passing
grade or otherwise qualify receive certificates.


.. _Deactivate a Certificate:

************************
Deactivate a Certificate
************************

In some situations, after you have activated a certificate, you might need to
deactivate the certificate to make changes.

As a best practice, do not make changes to certificates in a running course if
the course has already issued certificates to learners.

To deactivate a certificate, follow these steps.

.. note::
  Only course team members that have the Admin or Staff role can deactivate a
  certificate.

#. Make sure that you have the Admin or Staff role for the course. For more
   information, see :ref:`Guide to Course Team Roles`.

#. In Studio, on the **Settings** menu, select **Certificates**.

#. On the **Certificates** page, select **Deactivate**.

The certificate is no longer active and the course team can edit it. No new
certificates can be issued to learners while it is deactivated. Learners who
have already been issued certificates can continue to access them.


.. _Manage Certificate Images:

*************************
Manage Certificate Images
*************************

When you add signatory image files to a certificate, the uploaded files are
listed in Studio on the **Files & Uploads** page.

When you delete a certificate, images that you uploaded for use with that
certificate are also deleted. However, if you edit a certificate and replace
images, the unused image files remain on the **Files & Uploads** page. You can
manually remove unused images. For information, see
:ref:`Delete a File <Delete a File>`.


.. seealso::

  :ref:`About Certificates` (concept)

  :ref:`Edit Course Certificates` (how-to)

  :ref:`Configure Certificate Availability and Timing` (how-to)

  :ref:`Manage Course Badges` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 06/26/2025   | Leira (Curricu.me)            | Leira          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
