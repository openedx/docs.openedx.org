.. _Set up an LTI 1_3 component:

Set Up an LTI 1.3 Component
###########################

.. tags:: educator, how-to

To add an LTI 1.3 component to a course unit, follow these steps.

#. Edit the unit in which you want to add the remote LTI tool and select
   **Advanced** from the **Add New Component** section. Select **LTI
   Consumer**.

    .. note::

       This tool is enabled by default in Teak. For earlier releases, follow the steps below to enable it manually.
    
    
   If the **Advanced** component type is not available, make sure you have
   enabled LTI components. To do this, see :ref:`enable_lti_components`.

#. Select **Edit** in the component that appears.

#. In the **LTI Version** field, select **LTI 1.3**.

#. Enter the LTI 1.3 settings provided from your tool. For basic LTI 1.3
   tools, without LTI Advantage, you need to set the following settings:

   * **LTI 1.3 Tool Launch URL** (can also be called redirect url)
   * **LTI 1.3 OIDC URL** (can also be called login url)

   To enable *LTI Advantage* features, such as grades pass back and Deep
   Linking, you also need to set **LTI 1.3 Tool Public Key** with a key
   provided by the LTI tool. The key will look similar to this example:

   .. code-block:: bash

        -----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApAbQVx8FLXOflwvmV4dE
        merOO/C+syqDG7MniysYzbMm+egZ8Z3Dq0e2YuggZlRSHVtT9TpTu6BrP7GyWrhH
        7nOgCx5Rz+9g/B+KsasZ9x35bPjMeqNAu5aP3b0xgaRtnWec0h0a6T1L2xaQLuPS
        bDTJhABs0d22OYmdlMNN0+fWPmqxxAz8t7DBmjMMAmPLG4tjyEOwKCBlYCx0WELP
        Izg9bYA7MhCpHyD6+kTB51dbOA6lBbrIszCO9PBV4RD96LQWPs3YQ+DTqvPfLeTQ
        Q9XwiOe7yzsG1Ml+dkUODpZbuBk5Z9X486l36WbRWGBDWIWlsNE7M9Nl3eS42oS4
        IQIDAQAB
        -----END PUBLIC KEY-----

   You should paste the key from the tool directly into the configuration
   field. For more information about each setting, see :ref:`LTI Component
   settings`.

#. Select **Save**.

#. The Studio page will refresh and display LTI configuration required by the
   tool. Copy each of those values and follow the instructions provided by the
   tool to set them up.

   For basic LTI 1.3 launches, the following configuration values are required
   (they are provided by the LTI tool being set up):

   * **Client**
   * **Deployment ID**
   * **Keyset URL**
   * **OIDC Callback URL** (some tools refer to this as launch or redirect
     urls).

   For LTI Advantage, you'll also need to set **OAuth Token URL** (token/login
   url) in the tool.

.. note:: LTI 1.3 launches only work with published blocks, make sure the block
     is published before doing a launch.

.. seealso::
 
 :ref:`About the LTI Component` (concept)

 :ref:`LTI Component Settings` (reference)

 :ref:`Enable_LTI_Components` (how-to)

 :ref:`Set up an LTI 1_1 component` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
