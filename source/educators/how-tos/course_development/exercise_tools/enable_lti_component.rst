.. :diataxis-type: how-to
.. _enable_lti_components:

******************************************
Enabling LTI Components for a Course
******************************************

Before you can add LTI components to your course, you must enable the LTI tool
in Studio.

To enable the LTI tool in Studio, add ``"lti_consumer"`` to the
**Advanced Module List** on the **Advanced Settings** page. For more
information, see :ref:`Enable Additional Exercises and Tools`.

.. note::
  The ``lti_consumer`` module replaces a previous version of the LTI component.
  The name of the module for the previous LTI component is ``lti`` and it may
  appear in the **Advanced Module List** for older courses.

  The ``lti_consumer`` module includes all of the functionality of the previous
  LTI component and it should be used for all new courses. Courses that include
  the previous LTI component will continue to work correctly, even if the
  ``lti`` module is no longer present in the **Advanced Module List**.


.. _Setting up a LTI 1.1 component: 

*******************************
Setting up an LTI 1.1 component
*******************************

Some LTI 1.1 tools require users to provide authentication credentials. If the LTI
tool you are including in your course requires authentication, you must add an
LTI passport for that tool to your course configuration.

An LTI passport is a string of text that contains the authentication key and
shared secret for one LTI tool. A passport also contains the LTI ID for the
tool. When you add an LTI component to your course, assign it a matching LTI ID
so that it can use the LTI passport that it requires.

For more information about creating and registering LTI passports, see the
following sections.

.. contents::
   :local:
   :depth: 1

=========================================
Creating an LTI Passport String
=========================================

Each LTI passport includes three component text strings that are separated by
colon characters. The component strings are: the LTI ID, the client key, and
the client secret.

-  The **LTI ID** is a value that you create to refer to the remote LTI tool
   provider. You should create an LTI ID that you can remember easily.

   The LTI ID can contain uppercase and lowercase alphanumeric characters, as
   well as underscore characters (_). It can be any length. For example, you
   can create an LTI ID that is as simple as ``test_lti_id``, or your LTI ID
   can be a string of numbers and letters such as  ``id_21441`` or
   ``book_lti_provider_from_new_york``.

-  The **client key** is a sequence of characters that you obtain from the LTI
   tool provider. The client key is used for authentication and can contain any
   number of characters. For example, your client key might be
   ``b289378-f88d-2929-ctools.school.edu``.

-  The **client secret** is a sequence of characters that you obtain from the
   LTI tool provider. The client secret is used for authentication and can
   contain any number of characters. For example, your client secret can be
   something as simple as ``secret``, or it might be a string of numbers and
   letters such as ``23746387264`` or ``yt4984yr8``.

To create an LTI passport, combine the LTI ID, client key,
and client secret in the following format (be sure to include the colons).

``{your_lti_id}:{client_key}:{client_secret}``

The following example LTI passports show the format of the
passport string.

``test_lti_id:b289378-f88d-2929-ctools.school.edu:secret``

``id_21441:b289378-f88d-2929-ctools.school.edu:23746387264``

``book_lti_provider_from_new_york:b289378-f88d-2929-ctools.company.com:yt4984yr8``

.. _adding_an_lti_passport:

==================================================
Adding an LTI Passport to the Course Configuration
==================================================

To add an LTI passport for an LTI tool to the configuration for your course, follow these steps.

#. From the Studio **Settings** menu, select **Advanced Settings**.

#. In the **LTI Passports** field, place your cursor between the
   brackets.

#. Enter the LTI passport string surrounded by quotation marks.

   The following example shows an LTI passport string.

   ``"test_lti_id:b289378-f88d-2929-ctools.umich.edu:secret"``

   For more information about creating your key, see :ref:`Setting up a LTI 1.1 component`.

#. If you use more than one LTI provider in your course, separate each LTI
   passport string with commas. Make sure to surround each entry with quotation
   marks. The following example shows multiple LTI passports in the **LTI
   Passports** field.

   .. code-block:: json

      [
        "test_lti_id:b289378-f88d-2929-ctools.umich.edu:secret",
        "id_21441:b289378-f88d-2929-ctools.school.edu:23746387264",
        "book_lti_provider_from_new_york:b289378-f88d-2929-ctools.company.com:yt4984yr8"
      ]

#. Select **Save Changes**.

The page refreshes automatically, reformats your entry in the **LTI Passports**
field, and displays a notification that your changes have been saved.


=========================================
Adding an LTI Component to a Course Unit
=========================================

To add an LTI 1.1 component to a course unit, follow these steps.

#. If the LTI tool requires authentication, register the key and shared secret
   for the LTI tool in the configuration for your course. For more information
   about registering authentication credentials, see
   :ref:`Setting up a LTI 1.1 component`.

#. Edit the unit in which you want to add the remote LTI tool and select
   **Advanced** from the **Add New Component** section. Select **LTI
   Consumer**.

   If the **Advanced** component type is not available, make sure you have
   enabled LTI components. To do this, see :ref:`enable_lti_components`.

#. Select **Edit** in the component that appears.

#. In the **LTI Version** field, select **LTI 1.1/1.2**.

#. Configure the LTI component in the component editor. For more information
   about each setting, see :ref:`LTI Component settings`.

#. Select **Save**.

To test an LTI component, use the **Preview** feature or view the live version
in the LMS. For more information, see :ref:`Testing Your Course Content`.

.. _Setting up a LTI 1.3 component:

*******************************
Setting up an LTI 1.3 component
*******************************

To add an LTI 1.3 component to a course unit, follow these steps.

#. Edit the unit in which you want to add the remote LTI tool and select
   **Advanced** from the **Add New Component** section. Select **LTI
   Consumer**.

   If the **Advanced** component type is not available, make sure you have
   enabled LTI components. To do this, see :ref:`enable_lti_components`.

#. Select **Edit** in the component that appears.

#. In the **LTI Version** field, select **LTI 1.3**.

#. Enter the LTI 1.3 settings provided from your tool. For basic LTI 1.3
   tools, without LTI Advantage, you need to set the following settings:

   * **LTI 1.3 Tool Launch URL** (can also be called redirect url)
   * **LTI 1.3 OIDC URL** (can also be called login url)

   To enable *LTI Advantage* features, such as grades pass back and Deep Linking,
   you also need to set **LTI 1.3 Tool Public Key** with a key provided by the
   LTI tool. The key will look similar to this example:

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

   You should paste the key from the tool directly into the configuration field.
   For more information about each setting, see :ref:`LTI Component settings`.

#. Select **Save**.

#. The Studio page will refresh and display LTI configuration required by the
   tool. Copy each of those values and follow the instructions provided by the
   tool to set them up.

   For basic LTI 1.3 launches, the following configuration values are required
   (they are provided by the LTI tool being set up):

   * **Client**
   * **Deployment ID**
   * **Keyset URL**
   * **OIDC Callback URL** (some tools refer to this as launch or redirect urls).

   For LTI Advantage, you'll also need to set **OAuth Token URL** (token/login url)
   in the tool.

.. note:: LTI 1.3 launches only work with published blocks, make sure the block is
          published before doing a launch.

.. _Enabling and using LTI Advantage features:

*****************************************
Enabling and using LTI Advantage features
*****************************************

LTI Advantage is an extension of the LTI 1.3 specification that enables additional
features in LTI components. See :ref:`LTI Advantage` for more information.

Currently, the platform supports the following LTI Advantage extensions:

* :ref:`Assignments and Grades services`
* :ref:`Deep Linking`
* :ref:`Names and Roles Provisioning Service`


.. _Enabling LTI Assignments and Grades services:

============================================
Enabling LTI Assignments and Grades services
============================================

The LTI Assignments and Grades service (LTI-AGS) allows LTI tools to send and manage
learner grades back to the platform after an activity is completed.

To set up LTI-AGS services on a component, follow these steps.

#. Locate the unit and LTI component in which you want to enable LTI-AGS functionality.

#. Select **Edit** in the component that appears.

#. Locate the **LTI Assignment and Grades Service** setting.

#. Select the operation mode of the Assignments and Grades services. You can disable
   the LTI-AGS service by selecting **Disabled** or pick one of the operation
   modes available: *declarative* to allow only one grade per problem, or *programmatic*
   to let the tool create many grades. For more information about each mode, read the
   corresponding entry on :ref:`LTI Component settings`.

#. Select **Save**.

.. _Enabling and using LTI Deep Linking:

===================================
Enabling and using LTI Deep Linking
===================================

The Deep Linking service (LTI-DL) allows course creators to select and configure
the content displayed to learners through Open edX Studio, removing the need to
use custom parameters and settings when setting up content, improving the ease of
use and content authoring experience.

To set up LTI-DL services on a component, follow these steps.

#. Locate the unit and LTI component in which you want to enable LTI-DL functionality.

#. Select **Edit** in the component that appears.

#. Locate the **Deep linking** setting and set it to **True** (enabled).

#. Locate the **LTI Advantage Deep Linking Launch URL** setting.

#. Retrieve the Deep Linking Launch url from the tool you're integrating with. If it's not
   provided, try using the same value as in the **LTI 1.3 Tool Launch URL**.

#. Select **Save**. The Studio page will refresh and show the updated details page.

To use LTI Deep Linking, follow these steps:

#. Ensure that LTI-DL is enabled by following the steps above.

#. Locate the unit and LTI component in Studio.

#. In the LTI component page in Studio, locate the **Deep Linking Launch - Configure tool**
   link and select it.

#. You'll be redirected to the Tool and presented with a page to select the options.

#. Once the configuration is complete, you'll be redirected back to the Studio and the
   Deep Linking setup will be complete.

#. The content you selected in the tool will be presented to your students in the LMS.

.. note:: LTI 1.3 launches only work with published blocks, make sure the block is
          published before doing a Deep Link Launch.


.. _Enabling LTI Names and Roles Provisioning Service:

=================================================
Enabling LTI Names and Roles Provisioning Service
=================================================

The Names and Roles Provisioning service (LTI-NRPS) allows tools to list and retrieve
information about the learners that have access to an LTI component.
The tools that support this service can retrieve a limited amount of personal
information (full name, email, username) and the membership status of all the learners
enrolled in the course.

To set up LTI-NRPS services on a component, follow these steps.

#. Locate the unit and LTI component in which you want to enable LTI-NRPS functionality.

#. Select **Edit** in the component that appears.

#. Locate the **Enable LTI NRPS** setting and set it to **True** (enabled).

#. Select **Save**. The LTI-NRPS will be enabled for all subsequent launches.

.. note:: Due to performance concerns, LTI-NRPS information is by default only
          available on courses with up to 1000 users. Site operators may adjust
          this limit using the `LTI_NRPS_ACTIVE_ENROLLMENT_LIMIT setting`_.

.. seealso::
 :class: dropdown

  :ref:`LTI Component` (reference)
  :ref:`LTI Component settings` (reference)
