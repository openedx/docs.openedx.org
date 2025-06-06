.. _Configuring Badges:

Configuring Badges
####################

.. note::

    You can find technical details on how to set up proper configurations for badges to be active in this section.

Badges feature settings allow configuration:

1. feature availability;
2. event bus public signals subset for badges;
3. the Credly service integration details (URLs, sandbox usage, etc.);
4. the Accredible service integration details (URLs, sandbox usage, etc.);

You can use tutor plugin to setup all needed configurations:

https://github.com/raccoongang/tutor-contrib-badges


Feature switch
*********************************

The Badges feature is under a feature switch (disabled by default).

To enable the feature, update these settings as follows:

.. code-block:: python

    # Platform services settings:
    FEATURES["BADGES_ENABLED"] = True

    # Credentials service settings:
    BADGES_ENABLED = True


Default settings
*********************************

The feature has its configuration:

.. code-block:: python

    # Credentials settings:
    BADGES_CONFIG = {
        # these events become available in requirements/penalties setup:
        "events": [
            "org.openedx.learning.course.passing.status.updated.v1",
            "org.openedx.learning.ccx.course.passing.status.updated.v1",
        ],
        # Credly integration:
        "credly": {
            "CREDLY_BASE_URL": "https://credly.com/",
            "CREDLY_API_BASE_URL": "https://api.credly.com/v1/",
            "CREDLY_SANDBOX_BASE_URL": "https://sandbox.credly.com/",
            "CREDLY_SANDBOX_API_BASE_URL": "https://sandbox-api.credly.com/v1/",
            "USE_SANDBOX": False,
        },
        # Accredible integration:
        "accredible": {
            "ACCREDIBLE_BASE_URL": "https://dashboard.accredible.com/",
            "ACCREDIBLE_API_BASE_URL": "https://api.accredible.com/v1/",
            "ACCREDIBLE_SANDBOX_BASE_URL": "https://sandbox.dashboard.accredible.com/",
            "ACCREDIBLE_SANDBOX_API_BASE_URL": "https://sandbox.api.accredible.com/v1/",
            "USE_SANDBOX": False,
        },

        # requirements data rules:
        "rules": {
            "ignored_keypaths": [
                "user.id",
                "user.is_active",
                "user.pii.username",
                "user.pii.email",
                "user.pii.name",
            ],
        },
    }

- ``events`` - explicit event bus signals list (only events with PII user data in payload are applicable).
- ``credly`` - Credly integration details.
- ``accredible`` - Accredible integration details.
- ``rules.ignored_keypaths`` - event payload paths to exclude from data rule options (see: :doc:`credentials:badges/configuration/index`).

For more details on configuring badges, see :doc:`credentials:badges/quickstart`.


See :doc:`credentials:badges/examples` for some example configurations.


.. seealso::

    :ref:`Enable Badges`

    :doc:`credentials:badges/quickstart`

    :doc:`credentials:badges/examples`

    :doc:`credentials:badges/configuration/index`


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-05-20   | Sarina                        | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
