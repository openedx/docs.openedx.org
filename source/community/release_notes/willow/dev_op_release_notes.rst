.. _Willow Dev Notes:

Open edX Willow Developer & Operator Release Notes
#####################################################

*Releasing December, 2026!*

These are the developer & operator release notes for the Willow release, the 23rd
community release of the Open edX Platform, spanning changes from April 10,
2025 to December 9, 2026. You can also review details about :ref:`Open edX Release Notes` or
learn more about the `Open edX Platform`_.

To view the end-user facing docs, see the :ref:`Willow Product Notes`.

.. _Open edX Platform: https://openedx.org

.. contents::
 :depth: 1
 :local:

Breaking Changes
****************

Deprecations & Removals
***********************

Aspects Analytics
*****************************

Administrators & Operators
**************************

Settings and Toggles
********************

- **+REDACT_CERTIFICATES_HISTORICAL_PII**: `lms/djangoapps/certificates/config.py <https://github.com/openedx/openedx-platform/blob/93dc65b9ae10ed72e56743459a944db68d5e7229/lms/djangoapps/certificates/config.py#L25>`_
  - Default value = ``False``
  - Description: Clears the ``name`` field in the `django-simple-history` audit table for retiring users\' certificate records.


Developer Experience
********************

Known Issues
************

See the `Build Test Release project board <https://github.com/orgs/openedx/projects/28>`_ for known open issues.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
