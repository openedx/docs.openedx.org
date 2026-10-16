.. _Customize Registration Page:

#############################################
Adding Custom Fields to the Registration Page
#############################################

.. tags:: site operator, how-to

This topic describes how to add fields to the registration page of the
Authn micro-frontend (MFE) on your Open edX instance.

.. contents::
   :local:
   :depth: 1

*********
Overview
*********

You can add two kinds of fields to the registration page.

* **Built-in fields** already exist in the Open edX platform, such as
  ``city``, ``gender`` or ``level_of_education``. Adding them only takes
  configuration.
* **Your own fields** are fields that the Open edX platform does not have. You
  add them with a Django app plugin that defines a model to store the values
  and a form that describes the fields.

A **required** field appears on the registration form, and the learner cannot
create an account without it. An **optional** field appears on the welcome
page that the Authn MFE shows right after registration. The learner can skip
that page.

This topic describes the Verawood release and later. For earlier releases,
see :ref:`Reg Fields Earlier Releases`.

****************************
Where Each Setting Is Read
****************************

Some of the settings on this page are Django settings and some are Site
Configuration values. A value that the platform reads as a Django setting is
ignored if you put it in Site Configuration, and the other way around, so use
the location in the following table.

.. list-table::
   :header-rows: 1
   :widths: 40 25 35

   * - Setting
     - Where it is read
     - What it does
   * - ``ENABLE_DYNAMIC_REGISTRATION_FIELDS``
     - LMS Django setting
     - The LMS sends the configurable fields to the Authn MFE.
   * - ``MFE_CONFIG["ENABLE_DYNAMIC_REGISTRATION_FIELDS"]``
     - MFE runtime configuration
     - The Authn MFE shows the configurable fields on the registration form.
   * - ``MFE_CONFIG["ENABLE_PROGRESSIVE_PROFILING_ON_AUTHN"]``
     - MFE runtime configuration
     - The Authn MFE shows the welcome page, where optional fields appear.
   * - ``REGISTRATION_EXTRA_FIELDS``
     - LMS Django setting, or Site Configuration
     - Whether each built-in field is ``required``, ``optional`` or
       ``hidden``.
   * - ``PROFILE_EXTENSION_FORM``
     - LMS Django setting only
     - The form that describes your own fields.
   * - ``extended_profile_fields``
     - Site Configuration only
     - Which of your own fields the platform can save and return.

On a Tutor installation, set the Django settings and the MFE runtime
configuration with a Tutor plugin, as shown in the next section. Set
``extended_profile_fields`` in the Django admin, as described in
:ref:`Reg Fields Site Configuration`.

.. _Reg Fields Enable:

*****************************************
Enable Configurable Registration Fields
*****************************************

Both kinds of fields need the three flags in the first rows of the table
above. With Tutor, create a plugin, for example
``$(tutor plugins printroot)/registration_fields.yml``:

.. code-block:: yaml

   name: registration_fields
   version: 0.1.0
   patches:
     openedx-lms-common-settings: |
       ENABLE_DYNAMIC_REGISTRATION_FIELDS = True
     mfe-lms-common-settings: |
       MFE_CONFIG["ENABLE_DYNAMIC_REGISTRATION_FIELDS"] = True
       MFE_CONFIG["ENABLE_PROGRESSIVE_PROFILING_ON_AUTHN"] = True

Use the ``mfe-lms-common-settings`` patch for the ``MFE_CONFIG`` values. It is
applied after the ``tutor-mfe`` plugin defines ``MFE_CONFIG``, so the values
are not overwritten.

Then enable the plugin and restart the LMS:

.. code-block:: bash

   tutor plugins enable registration_fields
   tutor local restart lms

For more about Tutor plugins, see `Creating a Tutor plugin
<https://docs.tutor.edly.io/tutorials/plugin.html>`_. If you do not use Tutor,
set the same values in your LMS Django settings.

.. _Add Existing Reg Fields:

**********************
Add Built-in Fields
**********************

Built-in fields are switched on with ``REGISTRATION_EXTRA_FIELDS``. Each value
is ``required``, ``optional`` or ``hidden``. You can find the field names in
`EXTRA_FIELDS
<https://github.com/openedx/openedx-platform/blob/5dba87b25bfbbbc818582a7be41744fa4cac8177/openedx/core/djangoapps/user_authn/api/helper.py#L20-L40>`_.

Add the fields to the ``openedx-lms-common-settings`` patch of your plugin.
Change single keys rather than replacing the whole setting, so the defaults
for the other fields are kept:

.. code-block:: yaml

   openedx-lms-common-settings: |
     ENABLE_DYNAMIC_REGISTRATION_FIELDS = True
     REGISTRATION_EXTRA_FIELDS["city"] = "required"
     REGISTRATION_EXTRA_FIELDS["gender"] = "optional"

Save the configuration and restart the LMS:

.. code-block:: bash

   tutor config save
   tutor local restart lms

.. warning::

   ``REGISTRATION_EXTRA_FIELDS`` can also be set in Site Configuration, but
   there it **replaces** the Django setting instead of being merged with it.
   Every built-in field that the Site Configuration value does not list is
   then hidden, including the ones that are optional by default. If you use
   Site Configuration, list every field you want to show.

To change the order of the fields, set ``REGISTRATION_FIELD_ORDER`` to a list
of field names, in the Django settings or in Site Configuration.

.. _Add New Reg Fields:

********************
Add Your Own Fields
********************

Your own fields need a model to store the values and a form that describes the
fields. Both live in a Django app plugin that you install in the LMS. This
part requires some knowledge of Django.

The steps below use an example plugin called ``custom_profile`` that adds a
required ``organization`` field and an optional ``job_role`` field.

Step 1: Create the plugin
=========================

The plugin needs a model, a form, an app configuration, and an entry point
that registers it with the LMS.

The model stores one row per user. It must have a ``OneToOneField`` to the user
model, named ``user``:

.. code-block:: python

   # custom_profile/models.py
   from django.conf import settings
   from django.db import models

   JOB_ROLE_CHOICES = [
       ("student", "Student"),
       ("teacher", "Teacher"),
       ("other", "Other"),
   ]


   class ExtendedProfile(models.Model):
       user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       organization = models.CharField(verbose_name="Organization", max_length=100)
       job_role = models.CharField(
           verbose_name="Job role", max_length=32, blank=True, choices=JOB_ROLE_CHOICES
       )

The form is a ``ModelForm`` for that model. A field that is required in the
form appears on the registration form, and a field that is not required
appears on the welcome page. ``REGISTRATION_EXTRA_FIELDS`` does not apply to
these fields.

.. code-block:: python

   # custom_profile/forms.py
   from django import forms

   from .models import JOB_ROLE_CHOICES, ExtendedProfile


   class ExtendedProfileForm(forms.ModelForm):
       # Declared explicitly so the choices reach the MFE as a list of pairs.
       job_role = forms.ChoiceField(label="Job role", choices=JOB_ROLE_CHOICES, required=False)

       class Meta:
           model = ExtendedProfile
           fields = ["organization", "job_role"]

       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           # The account API binds this form to only the fields in the request.
           # Keep the stored value of every field the request leaves out, so that
           # saving one field does not fail validation or blank the others.
           if self.is_bound and self.instance.pk:
               data = self.data.copy()
               for name in self.fields:
                   if name not in data:
                       data[name] = getattr(self.instance, name)
               self.data = data

Two parts of this form are needed for the fields to work after registration:

* **Select fields are declared explicitly**, with the choices as a list. A
  select field that the ``ModelForm`` builds from a model field reaches the
  Authn MFE in a format it cannot read, and the welcome page fails with "An
  unexpected error occurred".
* **The** ``__init__`` **method keeps stored values.** The welcome page and
  other clients of the account API send only some of the fields. Without this
  method, the form treats the missing fields as empty, so saving fails
  whenever the form has a required field. See
  :ref:`Reg Fields Partial Updates`.

The Authn MFE can show ``text``, ``select``, ``textarea`` and ``checkbox``
fields. The field label comes from the form field label.

The app configuration must set ``plugin_app``. Without it, the LMS does not add
the app to ``INSTALLED_APPS``, even if the entry point is installed:

.. code-block:: python

   # custom_profile/apps.py
   from django.apps import AppConfig


   class CustomProfileConfig(AppConfig):
       name = "custom_profile"
       default_auto_field = "django.db.models.BigAutoField"
       # Registers the app as an Open edX plugin, so it is added to INSTALLED_APPS.
       plugin_app = {}

The entry point registers the app with the LMS, for example in
``pyproject.toml``:

.. code-block:: toml

   [project.entry-points."lms.djangoapp"]
   custom_profile = "custom_profile.apps:CustomProfileConfig"

Generate the initial migration for the model with ``makemigrations`` and
include it in the plugin.

Step 2: Install the plugin
==========================

Install the plugin in the LMS like any other Python package. With Tutor, add it
to ``OPENEDX_EXTRA_PIP_REQUIREMENTS`` and rebuild the ``openedx`` image, as
described in `Installing extra xblocks and requirements
<https://docs.tutor.edly.io/configuration.html#installing-extra-xblocks-and-requirements>`_.

Step 3: Run the migrations
==========================

The model needs its table in the database. ``tutor local launch`` runs the
migrations of every installed app, including your plugin. To run only the
migrations of your plugin:

.. code-block:: bash

   tutor local exec lms ./manage.py lms migrate custom_profile

Step 4: Point the LMS to your form
==================================

Add ``PROFILE_EXTENSION_FORM`` to the ``openedx-lms-common-settings`` patch of
the plugin from :ref:`Reg Fields Enable`. It is the dotted path to the form:

.. code-block:: yaml

   openedx-lms-common-settings: |
     ENABLE_DYNAMIC_REGISTRATION_FIELDS = True
     PROFILE_EXTENSION_FORM = "custom_profile.forms.ExtendedProfileForm"

Then save the configuration and restart the LMS:

.. code-block:: bash

   tutor config save
   tutor local restart lms

.. _Reg Fields Site Configuration:

Step 5: List the fields in Site Configuration
=============================================

Add the names of your fields to ``extended_profile_fields`` in the Site
Configuration of your LMS site. For the steps in the Django admin, see
:ref:`Retrieve_Extended_Profile_Metadata`.

.. code-block:: json

   {
       "extended_profile_fields": ["organization", "job_role"]
   }

.. warning::

   A field of your form that is not listed in ``extended_profile_fields`` is
   left out of the registration form and the welcome page, and nothing reports
   it. The platform only sends fields that it can save, and it only saves your
   fields when they are in this list.

The LMS keeps each site in memory for up to five minutes, so a change to Site
Configuration can take that long to appear. Restart the LMS to apply it at
once.

Step 6: Check the result
========================

The Authn MFE gets its fields from the ``/api/mfe_context`` endpoint of the LMS.
Open it in your browser:

.. code-block:: text

   https://<LMS host>/api/mfe_context?is_register_page=true

Required fields are listed under ``registrationFields`` and optional fields
under ``optionalFields``. In the example, ``organization`` is under
``registrationFields`` and ``job_role`` is under ``optionalFields``. If a field
is missing, check ``extended_profile_fields`` first.

Then open the registration page and create an account. The values are saved
in your model.

.. _Reg Fields Partial Updates:

*******************************************
Editing the Fields After Registration
*******************************************

With ``PROFILE_EXTENSION_FORM``, the account API reads your fields from your
model and saves changes through your form. The account settings page and the
welcome page both use this API.

When it saves, the API fills your form with only the fields in the request.
The account settings page sends all of your fields, but the welcome page sends
only the optional fields that the learner filled in. With a plain
``ModelForm``, every field the request leaves out counts as empty. If the form
has a required field, the save fails with a 400 error and the learner stays on
the welcome page. If all the fields are optional, the save succeeds and blanks
the fields that were left out.

The ``__init__`` method in the example form avoids this by filling in the
stored value of each field the request leaves out.

.. _Reg Fields Earlier Releases:

**************************************************
Earlier Releases and REGISTRATION_EXTENSION_FORM
**************************************************

Before the Verawood release, the form was set with ``REGISTRATION_EXTENSION_FORM``
instead of ``PROFILE_EXTENSION_FORM``. The other steps on this page are the
same, but the account API reads and saves your fields in the ``meta`` field of
the user profile, not in your model, so a value changed on the account
settings page does not reach your model.

In Verawood, ``REGISTRATION_EXTENSION_FORM`` still works with that behavior,
but it is deprecated and will be removed. If you switch to
``PROFILE_EXTENSION_FORM``, learners who have a value in ``meta`` but no row in
your model see empty fields until they save them again. To avoid that, copy
the existing values from ``meta`` to your model before you switch. For more
information, see the :ref:`Verawood Dev Notes` and the `deprecation ticket
<https://github.com/openedx/openedx-platform/issues/38409>`_.

****************
Troubleshooting
****************

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Symptom
     - Cause
   * - One of your fields does not appear.
     - The field is not in ``extended_profile_fields``, or the Site
       Configuration change has not reached the LMS yet.
   * - No configurable field appears at all.
     - ``ENABLE_DYNAMIC_REGISTRATION_FIELDS`` is missing either in the LMS
       Django settings or in ``MFE_CONFIG``.
   * - Optional fields never appear after registration.
     - ``MFE_CONFIG["ENABLE_PROGRESSIVE_PROFILING_ON_AUTHN"]`` is not set.
   * - The welcome page shows "An unexpected error occurred".
     - A select field in your form was built from a model field. Declare it
       explicitly with a list of choices.
   * - The welcome page does not save, and the account API answers 400 for a
       required field.
     - The form does not keep stored values. See
       :ref:`Reg Fields Partial Updates`.
   * - Built-in fields disappeared after you edited Site Configuration.
     - ``REGISTRATION_EXTRA_FIELDS`` in Site Configuration replaces the Django
       setting. List every field you want to show.

.. seealso::

   :ref:`Retrieve_Extended_Profile_Metadata`

   :ref:`Verawood Dev Notes`

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-10-13   | eduNEXT                       | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
