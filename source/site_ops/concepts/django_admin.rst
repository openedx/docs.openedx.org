.. _About the Django Admin:

The LMS and Studio Django Admin Interfaces
##########################################

.. tags:: site operator, concept

Both major Open edX services — the LMS and Studio (CMS) — are built on the
`Django web framework <https://www.djangoproject.com/>`_. Django provides a
built-in, automatically generated administrative interface, commonly called the
**Django admin**, that lets authorized users view and edit application data
directly. Because the LMS and Studio are separate Django applications, each one
exposes its own, independent Django admin:

* The **LMS Django admin**, served from your LMS domain at ``/admin/``.
* The **Studio (CMS) Django admin**, served from your Studio domain at
  ``/admin/``.

Each admin only exposes the applications installed in that service, so the set of
available tools differs between the two. An app that appears in one admin is not
necessarily present in the other. For example, the **Course Creators** app used
to grant course creation access exists only in the Studio admin, not the LMS
admin. When following a how-to that references the Django admin, be sure to use
the correct service's admin.

What the Django Admin Is For
****************************

The Django admin is intended for administrative tasks that require elevated
privileges and are not exposed through the normal LMS or Studio user interfaces.
Site operators and other trusted administrators use it to inspect and adjust
platform data and configuration — for example, managing feature toggles and
waffle flags, reviewing or editing user records, and changing settings that are
deliberately kept out of the day-to-day authoring and learning experiences.

Access to the Django admin is restricted to users with **staff**
(``is_staff``) or **superuser** permissions. Because these interfaces can read
and modify sensitive data across the platform, admin accounts should be granted
sparingly and treated as high-security credentials.

Security Considerations
***********************

The Django admin is a powerful, high-privilege interface. To reduce risk, when
possible you should protect the LMS and Studio admin interfaces from open access
over the public internet — for example, by restricting them to trusted networks
or a VPN, placing them behind additional authentication, or otherwise limiting
who can reach them. Combined with granting admin privileges only to the users
who genuinely need them, this helps limit the impact of compromised credentials.

For more detail on how the admin works and how it can be configured and secured,
see the official Django documentation:

* `The Django admin site <https://docs.djangoproject.com/en/stable/ref/contrib/admin/>`_
* `Django admin tutorial <https://docs.djangoproject.com/en/stable/intro/tutorial07/>`_

.. seealso::

  :ref:`Grant Course Creation Access in Studio` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-08-14   |  Ty Hob                       | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
