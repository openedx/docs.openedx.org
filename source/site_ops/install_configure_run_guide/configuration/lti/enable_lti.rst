.. _Enable LTI Provider Functionality:

#################################################
Enable LTI Provider Functionality
#################################################

.. tags:: site operator, how-to

The Learning Tools Interoperability (LTI) provider feature is included in Open edX but is disabled by
default. The recommended way to enable it on a Tutor-based installation
is to install a Tutor plugin. See `Creating a Tutor Plugin <https://docs.tutor.edly.io/developing/plugins/creating.html>`_.

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

    ########################################
    # Plugin metadata
    ########################################

    __version__ = "1.0.0"
    name = "enable-lti-provider"

    ########################################
    # LMS common settings patch
    ########################################

    hooks.Filters.ENV_PATCHES.add_item(
        (
            "openedx-lms-common-settings",
            textwrap.dedent("""
            # Enable LTI Provider feature
            FEATURES['ENABLE_LTI_PROVIDER'] = True
            ENABLE_LTI_PROVIDER = True
            INSTALLED_APPS.append('lms.djangoapps.lti_provider.apps.LtiProviderConfig')
            AUTHENTICATION_BACKENDS.append('lms.djangoapps.lti_provider.users.LtiBackend')
            SESSION_COOKIE_SAMESITE = 'None'
            SESSION_COOKIE_SECURE = True
            SESSION_COOKIE_SAMESITE_FORCE_ALL = True
            CSRF_COOKIE_SECURE = True
            CSRF_COOKIE_SAMESITE = 'None'
            X_FRAME_OPTIONS = "ALLOW-FROM <your-lti-consumer-domain>"
            """),

        )
    )

    ########################################
    # CMS common settings patch
    # (optional but keeps both services in sync)
    ########################################

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


You need to enable the plugin, restart your instance and run database migrations as described
in `Tutor documentation <https://docs.tutor.edly.io/developing/plugins/creating.html>`_.

.. important::

   If you plan to deliver content in an iframe, replace ``<your-lti-consumer-domain>``
   in the ``X_FRAME_OPTIONS`` setting with your actual LTI consumer domain. If you are
   not using iframe delivery, you can remove that line.



*****************************
Verify the Installation
*****************************

Confirm the LTI provider is active by looking for the `LTI Provider` section in Django admin panel.

.. figure:: /_images/site_ops_how_tos/lti_provider_section_django_panel.png
   :alt: Screenshot of LTI Provider section in the Django admin panel.
   :width: 100%

   LTI Provider section should appear in Django admin panel once the feature is active.

If its not visible, check that the migration step completed
without errors.


.. seealso::

   :ref:`Configuring an Open edX Instance as an LTI Tool Provider` (concept)

   :ref:`Configuring Credentials for a Tool Consumer` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-06   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-06-04   | MITx                          | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
