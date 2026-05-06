.. _Enable LTI Provider Functionality:

#################################################
Enable LTI Provider Functionality
#################################################

.. tags:: site operator, how-to

The Learning Tools Interoperability (LTI) provider feature is included in Open edX but is disabled by
default. The recommended way to enable it on a Tutor-based installation
is to install a Tutor plugin.

*****************************
Create the Tutor Plugin
*****************************

Create a file named ``enable_lti_provider.py`` (for example,
``~/.local/share/tutor-plugins/enable_lti_provider.py``) with the
following content:

.. code-block:: python

    """
    Tutor plugin: enable-lti-provider
    Sets ENABLE_LTI_PROVIDER = True in the edx-platform LMS and CMS settings.
    """
    import textwrap

    from tutor import hooks

    __version__ = "1.0.0"
    name = "enable-lti-provider"

    hooks.Filters.ENV_PATCHES.add_item(
        (
            "openedx-lms-common-settings",
            textwrap.dedent("""
            # Enable LTI Provider feature
            FEATURES['ENABLE_LTI_PROVIDER'] = True
            ENABLE_LTI_PROVIDER = True
            INSTALLED_APPS.append('lms.djangoapps.lti_provider.apps.LtiProviderConfig')
            AUTHENTICATION_BACKENDS.append('lms.djangoapps.lti_provider.users.LtiBackend')
            """),
        )
    )

    hooks.Filters.ENV_PATCHES.add_item(
        (
            "openedx-cms-common-settings",
            """
            # Enable LTI Provider feature
            FEATURES['ENABLE_LTI_PROVIDER'] = True
            ENABLE_LTI_PROVIDER = True
            """,
        )
    )

.. note::

   The plugin patches both LMS and CMS settings. The CMS patch keeps
   both services in sync but does not affect LTI provider functionality,
   which runs entirely in the LMS.

*****************************
Enable and Apply the Plugin
*****************************

After saving the file, run:

.. code-block:: bash

    tutor plugins enable enable-lti-provider
    tutor config save
    tutor local do init --limit lms

*****************************
Run Database Migrations
*****************************

.. code-block:: bash

    tutor local run lms python manage.py lms migrate

*****************************
Verify the Installation
*****************************

Confirm the LTI provider is active by checking that these database
tables exist:

.. code-block:: text

    lti_provider_gradedassignment
    lti_provider_lticonsumer
    lti_provider_ltiuser
    lti_provider_outcomeservice

If any tables are missing, check that the migration step completed
without errors.


.. seealso::

   :ref:`Configuring Credentials for a Tool Consumer`


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-06   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
