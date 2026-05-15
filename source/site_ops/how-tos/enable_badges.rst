.. _Enable Badges:

Enable Badges
#################

.. tags:: site operator, how-to

.. note::

    This section includes brief information about the feature - what to start with; where to set up credentials, etc.

Currently Open edX supports two badge services: Credly and Accredible.

Prerequisites - service account
*********************************

To start using this feature a Credly or Accredible account is necessary.

For Credly:

#. Register on Credly and create your account.
#. Create Organization in Credly.
#. Create at least 1 badge template and activate it.


For Accredible:

#. Register on Accredible and create your account.
#. Create at least 1 group.

Enable feature
*********************************

Badges feature is optional and it is disabled by default. So, it must be enabled to be accessible.

.. code-block::

    # LMS service:
    FEATURES["BADGES_ENABLED"] = True

    # Credentials service:
    BADGES_ENABLED = True

Configure integration
*********************************

See :ref:`credentials:badges-quickstart` for more details on configuring the Credly and Accredible integrations.

See :ref:`credentials:Configuration examples for Badging` for some example configurations.

.. seealso::

    :ref:`About Badges`

    :ref:`Configuring Badges`

    :ref:`credentials:badges-quickstart`

    :ref:`credentials:Configuration examples for Badging`

    :ref:`credentials:badges-configuration`


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-05-20   | Sarina                        | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
