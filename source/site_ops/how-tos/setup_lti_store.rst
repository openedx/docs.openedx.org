.. _Set up a Reusable LTI Store:

Set Up a Reusable LTI Store
###########################

.. tags:: site operator, how-to

LTI Store is an optional plugin that lets site operators define an LTI tool
configuration once and make it available for reuse. Course teams reference the
stored configuration from an LTI Consumer XBlock by entering its *Filter key*,
instead of entering the tool's connection values in every component.

Reusable configurations can be created for LTI 1.1/1.2 and LTI 1.3 tools. In
LTI Store, the older version option may appear as LTI 1.1. LTI Advantage
services, such as Deep Linking, Assignment and Grade Services, and Names and
Role Provisioning Services, are available only for LTI 1.3 configurations.

.. contents::
   :local:
   :depth: 1

Setting up LTI Store requires an operational Open edX deployment, permission
to install the plugin or Django app, and staff access to Django Admin with
permission to manage LTI Store models. You also need the connection and
registration values for the external tool.

For LTI 1.1/1.2 tools, collect the tool launch URL, consumer key, and shared
secret. For LTI 1.3 tools, collect the login and
launch URLs, tool keyset URL or public key, any required redirect URIs, and the
list of LTI Advantage services that the tool supports.

Install the LTI Store Plugin
****************************

#. Install the plugin from the `LTI Store repository`_.
#. Follow the plugin README to enable it for your environment.
#. Rebuild and restart the platform as required by your deployment.

For non-Tutor installations, follow the `non-Tutor installation instructions`_.

Grant Staff Access for LTI Store Administration
***********************************************

To create and manage reusable configurations, grant the administrator account
the minimum Django Admin access required for LTI Store.

* Enable ``is_staff`` for the account.
* Assign permissions for the LTI Store models.
* Avoid granting superuser access when model-level permissions are sufficient.

.. _Enable Reusable Configurations:

Enable Reusable Configurations
******************************

The LTI Consumer XBlock loads configurations provided by LTI Store only when
the ``lti_consumer.enable_external_config_filter`` CourseWaffleFlag is enabled.
This flag defaults to ``False``.

To enable reusable configurations for all courses, create or update the
standard Waffle flag named ``lti_consumer.enable_external_config_filter`` and
enable it for everyone. To enable reusable configurations for an organization
or an individual course instead, follow these steps.

#. In the LMS Django Admin, open *Waffle flag org overrides* or *Waffle flag
   course overrides* under *Waffle Utils*.
#. Add an override with the following values.

   * Set *Waffle flag* to ``lti_consumer.enable_external_config_filter``.
   * Enter the organization name or course ID.
   * Set *Override choice* to *Force On*.
   * Select *Enabled*.

#. Save the override.

A course-level override takes precedence over an organization-level override.
An organization-level override takes precedence over the standard Waffle flag
and its default value.

.. _Create a Reusable LTI Configuration:

Create a Reusable LTI Configuration
***********************************

#. Open Django Admin.
#. Navigate to ``/admin/lti_store/externallticonfiguration/``.
#. Select :guilabel:`Add External LTI Configuration`.

   .. image:: /_images/site_ops_how_tos/add_lti_store_configuration.png
      :alt: Django Admin page showing the Add External LTI Configuration
         button.

#. Enter a clear *Name* for the configuration.
#. Enter a *Slug*, or leave the field blank to generate a slug from the name.
#. Select the LTI *Version* used by the tool.
#. Enter the values required for the selected LTI version.

   * For LTI 1.1/1.2, enter:

     * *Launch URL*
     * *Client Key*
     * *Client Secret*

   * For LTI 1.3, enter:

     * *Client ID*
     * *Deployment ID*
     * *OIDC URL*
     * *Launch URL*
     * *Private Key* in PEM format (generate according to your organization's
       security policy paste in this field)
     * *Tool Public Key* OR *Tool Keyset URL*
     * *Redirect URIs*, if required by the tool
     * (Optional) Enable *Names and Role Provisioning Services*
     * (Optional) Enable *Deep Linking*
     * (Optional) *Deep Linking Launch URL*. If Deep Linking is enabled,
       enter the URL provided by the tool. If the tool does not provide
       a separate URL, use the tool's launch URL.
     * (Optional) Set *Assignment and Grade Services* mode

   .. figure:: /_images/site_ops_how_tos/create_ltistore_config.png
      :alt: Django Admin form showing the LTI 1.1, LTI 1.3, and LTI Advantage
         fields for an external LTI configuration.

      Select the tool's LTI version and enter the corresponding values to
      create a reusable LTI configuration.

#. Save the configuration.
#. After saving, note the *Filter key* displayed on the External LTI
   Configurations screen.

   The Filter key usually has the form ``lti_store:slug``. For example,
   ``lti_store:reference_tool``.

   .. figure:: /_images/site_ops_how_tos/lti_filter_key.png
      :alt: Django Admin External LTI Configurations list with the Filter key
         column highlighted for an LTI 1.3 configuration.

      Copy the value in the *Filter key* column to share with the course team.

For LTI 1.3, coordinate with the course team to register the Open edX platform
with the external tool. This registration is shared by the XBlocks that use the
same reusable configuration and needs to be completed only once. For the
educator workflow, see :ref:`Register an LTI 1_3 reusable configuration with
the tool`.

.. _Allow per-XBlock launch URLs for reusable LTI tools:

Allow Per-XBlock Launch URLs
****************************

By default, every LTI Consumer XBlock that references a reusable configuration
uses the launch URL stored in that configuration. For LTI 1.3 tools, you can
allow course teams to enter a different launch URL in each XBlock while sharing
the other registration and connection values.

This feature requires xblock-lti-consumer 9.14.1 or later. It also requires
``lti_consumer.enable_external_config_filter`` and applies only to LTI 1.3
XBlocks that use an *Existing* reusable configuration.

Enable ``lti_consumer.enable_external_multiple_launch_urls`` by using the same
global, organization, or course-level method described in :ref:`Enable Reusable
Configurations`. This CourseWaffleFlag defaults to ``False`` and is part of the
LTI Consumer XBlock, not LTI Store.

When the flag is enabled, Studio displays the *Launch URL* field for affected
XBlocks. A nonempty value in this field overrides the launch URL from the
reusable configuration. If the field is empty, the XBlock uses the launch URL
from the reusable configuration. The flag does not affect LTI 1.1/1.2 tools,
configurations stored directly on the XBlock, or database-stored
configurations.

Share Configuration Details with Course Teams
*********************************************

Course teams need the Filter key to reference the reusable configuration in
Studio. They also need enough context to configure learner-facing options and
test the tool.

Share these details with course teams:

* Filter key
* LTI version
* Tool name or recommended display name
* Whether the tool is expected to return grades
* Any LTI Advantage services enabled for the configuration
* Whether LTI 1.3 registration with the tool is complete
* Whether the course needs LTI PII sharing enabled
* Any required Review Options settings in Studio
* Any tool-specific launch, Deep Linking, or testing instructions
* Whether per-XBlock launch URLs are enabled and, if so, which launch URL each
  XBlock should use

If you change a reusable configuration, the change can affect every LTI Consumer
XBlock that uses the same Filter key. Communicate changes to affected course
teams before updating shared configurations.

Best Practices
**************

* Use clear, consistent names and slugs for configurations.
* Create separate configurations for production, staging, and sandbox tools
  because registration values often differ by environment.
* Prefer using the tool keyset URL instead of a static public key when the tool
  supports a keyset URL.
* Keep a registry of tool names, environments, Filter keys, owners, and course
  teams that use each configuration.

Notes on Current Limitations and Improvements
*********************************************

* **Dynamic registration**: The LTI community is adopting dynamic registration,
  which allows configuring an LTI integration from a single URL. This may
  simplify setup in future releases. Dynamic registration is not currently
  supported by the Open edX platform.
* **Alternative reuse path**: Reusable Library Components may allow LTI reuse
  without LTI Store. Investigation is ongoing. Migration guidance will be
  provided if this path becomes preferred.

Next Steps
**********

After you create the reusable configuration and share the Filter key, course
teams can add the LTI Consumer XBlock in Studio and configure it to use the
stored configuration. For more information, see :ref:`Set up an LTI tool using
a reusable configuration`.

.. seealso::

 :ref:`Set up an LTI tool using a reusable configuration` (how-to)

 :ref:`Set up an LTI 1_1 tool` (how-to)

 :ref:`Set up an LTI 1_3 tool` (how-to)

 :ref:`LTI Advantage Services` (reference)

 :ref:`Manage LTI PII Sharing for a Course` (how-to)

 :ref:`Using your Open edX instance as an LTI Tool Provider` (concept)


.. _LTI Store repository: https://github.com/openedx/openedx-tutor-plugins/tree/main/plugins/tutor-contrib-ltistore
.. _non-Tutor installation instructions: https://github.com/openedx/openedx-tutor-plugins/tree/main/plugins/tutor-contrib-ltistore#non-tutor-install-instructions


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        | Release        | Test situation                 |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-12-05   | LTI WG                        | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
