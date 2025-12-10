.. _Set up a Reusable LTI Store:


Set up a Reusable LTI Store
###########################

.. tags:: site operator, how-to

The Reusable LTI Store centralizes LTI configuration in Django Admin.  
Course authors then reference a single reusable configuration in Studio (via the LTI Consumer component).  
A single configuration can be referenced multiple times, eliminating repeated copy/paste of tool credentials.

.. contents::
   :local:
   :depth: 1

Overview
********

The Reusable LTI Store allows operators and course authors to simplify setup by:

* Defining LTI configurations once in Django Admin.
* Allowing course authors to reference those configurations in Studio.
* Reducing errors and duplication of tool credentials.

This feature supports LTI 1.3 integrations and is particularly useful for institutions running multiple courses with the same tool.



Before you start
****************

To use the Reusable LTI Store, ensure the following:

* You have an operational Open edX deployment.
* You have staff access to Django Admin (model-level access to ``lti_store``).
* You have access to an LTI 1.3 tool with:

  - Client ID
  - Deployment ID
  - OIDC/Authorization URL
  - Launch URL
  - JWKS (key set) URL or a tool public key

* For Tutor-based deployments: You can install Tutor plugins.
* For non-Tutor deployments: You can install and configure Django apps.



Install the LTI Store Tutor Plugin
**********************************

1. Install the plugin from the `LTI Store Repository <https://github.com/openedx/openedx-tutor-plugins/tree/main/plugins/tutor-contrib-ltistore>`_ and follow the plugin’s README to enable it for your environment.
2. Rebuild and restart your platform. Apply the plugin’s documented Tutor config, images rebuild, and services restart steps.

.. note::
   For non-Tutor installations, follow `Non-Tutor Install Instructions <https://github.com/openedx/openedx-tutor-plugins/tree/main/plugins/tutor-contrib-ltistore#non-tutor-install-instructions>`_. Most community operators use Tutor, but some large operators do not.



Grant staff access for LTI Store administration
***********************************************

To create and manage reusable configurations:

* Ensure the user has ``is_staff`` enabled.
* Assign permissions for the LTI Store models only (no superuser needed).
* This limits access to just the LTI Store configuration screens.


.. _Create a Reusable LTI 1.3 Configuration:

Create a reusable LTI configuration
***********************************

.. note::
   The following steps correspond to an **LTI 1.3 configuration**.

#. Open Django Admin.
#. Navigate to: ``/admin/lti_store/externallticonfiguration/``  
   (You must be logged in as a staff user with LTI Store model access.)


#. Add a new **External LTI Configuration**.

  .. image:: /_images/educator_how_tos/add_lti_store_configuration.png
    :alt: 'Add External LTI Configuration' button on Django Admin

#. Enter the required fields:

   * **Name**
   * **Slug** (will be automatically generated from the name if left blank)
   * **Version**: LTI 1.3
   * **LTI 1.3 Client ID**: Provided by the tool.
   * **LTI 1.3 Deployment ID**: Provided by the tool.
   * **LTI 1.3 OIDC URL**: Provided by the tool (sometimes called “OIDC auth URL”).
   * **LTI 1.3 Launch URL**: The tool’s launch URL for LTI 1.3.
   * **LTI 1.3 Private key**: Platform private key for this registration. Must be supplied manually.  
     You can generate these using the `IMS LTI Reference Implementation <https://lti-ri.imsglobal.org/keygen/index>`_.
   * **LTI 1.3 Tool Keyset URL** (recommended), or **LTI 1.3 Tool Public Key**
   * **LTI 1.3 Redirect URIs**: Required by some tools. For many tools this matches the launch URL.  
     If not specified otherwise, use your launch URL in a JSON list. For example:

     ``["https://example.com/launch"]``

  .. image:: /_images/educator_how_tos/create_ltistore_config.png
    :alt: LTI store configuration fields in Django Admin

#. Save the configuration.
#. After saving, note the **Filter key** displayed on the External LTI Configurations screen (``/admin/lti_store/externallticonfiguration/``). The Filter Key usually has the form ``lti_store:slug`` (e.g. ``lti_store:reference_tool``). You will use this value later in Studio when referencing this configuration from the LTI Consumer component.



Recommended: Use the IMS LTI Reference Tool
===========================================

* For testing purposes, use the `Reference Tool <https://lti-ri.imsglobal.org/lti/tools/5621>`_ 
* This page shows typical LTI 1.3 values (Client ID, Deployment ID, JWKS URL, OIDC URL, Launch URL).
* Prefer using the **JWKS (key set) URL** instead of a static public key to reduce manual steps and key rotation issues.
* You can also create your own tool for testing here.



Best practices
==============

* Use clear, consistent names for configurations and slugs (for example: ``tool-environment-purpose``).
* Keep a registry of created configurations (tool name, environment, slug, owner) to assist course teams.
* Create separate configurations per environment (production, staging, sandboxes) since Client ID and Deployment ID typically differ.



Notes on current limitations and improvements
*********************************************

* **Dynamic registration**: The LTI community is adopting dynamic registration, which allows configuring an LTI integration from a single URL.  
  This may simplify setup in future releases. The Open edX platform does not currently support dynamic registration.
* **Alternative reuse path**: Reusable Library Components may allow LTI reuse without the LTI Store. Investigation is ongoing; migration guidance will be provided if this path becomes preferred.



Next steps
**********

* Share the Filter key with course authors.
* Authors configure the LTI Consumer component in Studio to use this reusable configuration (documented separately).


.. seealso::

 :ref:`Create a Reusable LTI 1.3 Configuration` (how-to)

 :ref:`Set up an LTI Consumer with Reusable LTI Configuration` (how-to) 

 :ref:`LTI Component Settings` (reference)

 :ref:`Enable_LTI_Components` (how-to)

 :ref:`Set up an LTI 1_1 component` (how-to)

 :ref:`Set up an LTI 1_3 component` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)

 :ref:`Using Open edX as an LTI Tool Provider` (concept)




**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        | Release        | Test situation                 |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-12-05   | LTI WG                        | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+