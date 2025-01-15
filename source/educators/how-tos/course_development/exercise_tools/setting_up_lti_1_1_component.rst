.. _Setting up a LTI 1.1 component:

Set Up an LTI 1.1 Component
###########################

.. tags:: educator, how-to

Some LTI 1.1 tools require users to provide authentication credentials. If the
LTI tool you are including in your course requires authentication, you must add
an LTI passport for that tool to your course configuration.

An LTI passport is a string of text that contains the authentication key and
shared secret for one LTI tool. A passport also contains the LTI ID for the
tool. When you add an LTI component to your course, assign it a matching LTI ID
so that it can use the LTI passport that it requires.

For more information about creating and registering LTI passports, see the
following sections.

.. contents::
   :local:
   :depth: 1

Creating an LTI Passport String
*******************************

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

Adding an LTI Passport to the Course Configuration
**************************************************

To add an LTI passport for an LTI tool to the configuration for your course,
follow these steps.

#. From the Studio **Settings** menu, select **Advanced Settings**.

#. In the **LTI Passports** field, place your cursor between the
   brackets.

#. Enter the LTI passport string surrounded by quotation marks.

   The following example shows an LTI passport string.

   ``"test_lti_id:b289378-f88d-2929-ctools.umich.edu:secret"``

   For more information about creating your key, see :ref:`Setting up a LTI 1.1
   component`.

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

Adding an LTI Component to a Course Unit
****************************************

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

.. seealso::
 :class: dropdown

 :ref:`LTI Component` (reference)

 :ref:`LTI Component settings` (reference)

 :ref:`Enable_LTI_Components` (how-to)

 :ref:`Setting up a LTI 1.3 component` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)
