.. _Customize Registration Page:

##############################################
Adding Custom Fields to the Registration Page
##############################################

.. tags:: site operator

This topic describes how to add custom fields to the registration page for your
instance of Open edX.

.. contents::
   :local:
   :depth: 1

*************
Introduction
*************

This guide explains how to add custom fields to the registration page of your Open edX instance. To integrate custom fields with the new Authn MFE, additional configuration steps are required. Custom fields can be either required—added directly to the registration page—or optional, and will be added to the progressive profiling page (welcome page) that users can skip.

**********************************
Two Main Ways to Add Custom Fields
**********************************

The Open edX platform has default additional fields that can be used in Authn MFE. The fields that are in `EXTRA_FIELDS <https://github.com/openedx/edx-platform/blob/a9355852edede9662762847e0d168663083fc816/openedx/core/djangoapps/user_authn/api/helper.py#L20-L39>`_ are already exist as columns in the user profile model, but are disabled, so when adding other fields that do not exist, a step to do data migration is required.

To add fields that already exist in the user model, it is sufficient to redefine several constants. How to do this will be described in instructions **A**. If you need to add fields that are not in the user model by default, use instruction **B**.

A. Add Fields that Already Exist as Columns in the User Profile Model
======================================================================
You need to redefine several constants in the settings. You can use various methods for this:

Method 1: Redefine constants using Django admin and `Site configurations` API. (recommended)
---------------------------------------------------------------------------------------------
#. Go to `Site configurations` in admin: {{LMS}}/admin/site_configuration/siteconfiguration/
#. Add new settings to OrderedDict (create new `Site configurations` if it was not before)
   .. code-block:: json

        {
            "ENABLE_DYNAMIC_REGISTRATION_FIELDS": "true",
            "MFE_CONFIG": {
            "ENABLE_DYNAMIC_REGISTRATION_FIELDS": "true"
            },

            "REGISTRATION_EXTRA_FIELDS": {
            "country": "required",
            "gender": "optional"

            }
        }


#. All possible fields can be found in `EXTRA_FIELDS <https://github.com/openedx/edx-platform/blob/a9355852edede9662762847e0d168663083fc816/openedx/core/djangoapps/user_authn/api/helper.py#L20-L39>`_.
#. REST API gets cached. If you are in a hurry, you can do this command: `tutor local exec redis redis-cli flushall`. Also, you can wait a few minutes until the cache is invalidated.
#. The new fields should appear on the Auth page. Required fields will appear on the registration form, and optional fields will appear on the progressive profiling form.

Method 2: Redefine Settings Above by Using the Tutor Plugin
------------------------------------------------------------
#. There is a tutorial `how Tutor plugin can be created <https://docs.tutor.edly.io/tutorials/plugin.html#creating-a-tutor-plugin>`_.
#. Settings above should be overridden in the Tutor plugin.

Method 3: For the Local Development or Testing Settings, It Can Be Overridden in Configuration Files
-----------------------------------------------------------------------------------------------------
#. Constants can be added here: `env/apps/openedx/settings/lms/development.py`:
   .. code-block:: python

        ENABLE_DYNAMIC_REGISTRATION_FIELDS = "true"

        MFE_CONFIG["ENABLE_DYNAMIC_REGISTRATION_FIELDS"] = "true"

        REGISTRATION_EXTRA_FIELDS["country"] = "required"

        REGISTRATION_EXTRA_FIELDS["gender"] = "required"

In total, you must redefine 3 constants using the method that is most preferable for you:

    .. code-block:: python

        ENABLE_DYNAMIC_REGISTRATION_FIELD = True,

        MFE_CONFIG["ENABLE_DYNAMIC_REGISTRATION_FIELDS"] = True,

        REGISTRATION_EXTRA_FIELDS["field_name"] = "required/optionl/hidden"

B. Add Fields that Do Not Exist in the User Profile Model
==========================================================
Everything said above in instructions **A** also applies to adding fields that do not exist in the user profile model. This is a more complex task and requires a basic understanding of the Open EdX platform, the concept of plugins, as well as knowledge of the Django framework. However, there are additional actions that you need  to perform:
#. Extend user profile model with new fields. An external plugin can be used for this (recommended). Also user profile model can be expanded inside edx-platform code base (not recommended). `New fields must be migrated to the database.`
#. Create a form with additional user profile fields and pass the path to this form into `settings`. The form can also be created in the Open edX plugin. `Edx-cookiecutters <https://github.com/openedx/edx-cookiecutters>`_ can be used for the plugin creation.
#. Additional settings can be passed via `Site configurations` in the LMS admin. This is described in instructions **A**. 
Example:

   .. code-block:: json

         {
            "REGISTRATION_EXTENSION_FORM": "you_application.form.ExtendedUserProfileForm",

            "extended_profile_fields": [
                "your_new_field_id",
                "subscribe_to_emails",
                "confirm_age_consent",
                "something_else"
            ]
         }

#. In total, you must migrate to DB new user profile fields and redefine 3 constants using the method that is most preferable for you:
   .. code-block:: python

        ENABLE_DYNAMIC_REGISTRATION_FIELD = True,

        MFE_CONFIG["ENABLE_DYNAMIC_REGISTRATION_FIELDS"] = True,

        REGISTRATION_EXTENSION_FORM = "you_application.form.ExtendedUserProfileForm"

.. note:: Below, you can read in detail how to create a new Application and Form, what happens when you redefine each constant, and how they can be redefined.

*******************************************************
Configuring Custom Registration Fields on the Back-End
*******************************************************
To configure dynamic registration fields within Authn, perform the following steps in Open edX LMS settings or your custom form plugin:

#. Install your custom form app and configure it in LMS. Follow the steps outlined in the official Open edX documentation to configure custom registration fields for your instance:
`Customize the Registration Page <https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/customize_registration_page.html>`_.
#. Enable dynamic registration fields setting in the Open edX platform. Enable the `ENABLE_DYNAMIC_REGISTRATION_FIELDS` setting in the settings file. This setting should be added to the plugin where the extension form is placed.

.. note:: See the context view for the Logistration page: `user_authn API Context View <https://github.com/openedx/edx-platform/blob/master/openedx/core/djangoapps/user_authn/api/views.py#L61>`_.

#. Add fields to the extended profile fields list. Add your `custom field <https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/retrieve_extended_profile_metadata.html>`_ to the `extended_profile_fields` list to ensure it is checked correctly during registration.
.. warning:: If this step is missed, fields from the extension form will not be saved. For more information, please see the condition in: `helper.py <https://github.com/openedx/edx-platform/blob/master/openedx/core/djangoapps/user_authn/api/helper.py#L97>`_.
#. After adding all required settings, verify that the context has been properly extended with the new fields by inspecting the networks tab in your browser's developer tools.

************************************************
Configuring Dynamic Registration Fields in Authn
************************************************
Enable dynamic fields in the MFE. Ensure that `ENABLE_DYNAMIC_REGISTRATION_FIELDS` is enabled for the MFE. This can be configured via env tokens or through site configurations if MFE CONFIG API is enabled.

.. include:: /links.txt

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 15/04/2026   |  edunext                      |   Ulmo         |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
