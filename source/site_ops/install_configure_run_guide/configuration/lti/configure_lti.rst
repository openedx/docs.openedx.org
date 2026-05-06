.. _Configuring Credentials for a Tool Consumer:

###############################################################
Configuring LTI Consumers
###############################################################

.. tags:: site operator, how-to

For each external LMS that will consume content from your Open edX
instance, you must create a Learning Tools Interoperability (LTI) consumer record in the Django admin.
Each external LMS must have its own separate record.

.. contents::
   :local:
   :depth: 1

*****************************
Create a Consumer Record
*****************************

#. Sign in to the Django administration console at
   ``https://{your_lms_domain}/admin``.

#. Under `LTI Provider`, select :guilabel:`Add` next to `LTI Consumers`.

#. Fill in the fields:

   - `Consumer Name`: A label identifying this external LMS (for
     example, ``Canvas - Example University``).

   - `Consumer Key`: A unique identifier for this consumer. Generated
     automatically but you can also supply your own.

   - `Consumer Secret`: A secret used to sign LTI requests.
     Generated automatically but you can also supply your own.

   .. important::

      Leave `Instance GUID` blank. The external LMS generates and
      supplies this value on its first LTI launch.

   - `Require User Account` and `Use LTI PII`: These checkboxes
     control how Open edX associates learners with accounts. See
     :ref:`Authentication Modes` below before deciding which to enable.

#. Select :guilabel:`Save`.

#. Share the `Consumer Key` and `Consumer Secret` with the educator
   or administrator who will configure the external LMS.

.. _Authentication Modes:

*****************************
Authentication Modes
*****************************

When a learner launches LTI content for the first time, Open edX must
associate them with a user account. The two checkboxes on the consumer
record control how this happens.

Anonymous (default)
===================

Both `Require User Account` and `Use LTI PII` are unchecked.

Open edX automatically creates an account with a randomly generated
username and email address. The learner sees no login prompt and the
content loads immediately. This account is linked to the learner's
identity in the external LMS for grade passback.

Use this mode when learner identity on Open edX is not important and
you want the most seamless experience.

Auto-Create with Personal Information
======================================

Check `Use LTI PII`.

Open edX uses the learner's email address and full name from the LTI
launch request (``lis_person_contact_email_primary``,
``lis_person_name_full``) to create their account. If an account with
that email already exists, it is linked automatically instead of
creating a new one.

Use this mode when you need to associate LTI activity with real learner
identities or with accounts that already exist on your Open edX instance.

The external LMS must be configured to send ``lis_person_contact_email_primary``
in the launch request. This has been tested with Canvas LMS with the
privacy setting set to "Email Only" or "Public".

Require Existing Account
========================

Check `Require User Account`.

On the learner's first LTI launch, Open edX checks two conditions:

- The learner is already signed into Open edX in the same browser.
- Their Open edX account email matches ``lis_person_contact_email_primary``
  sent by the external LMS.

If either condition is not met, the learner sees an error page with a
link to the Open edX sign-in page. After signing in with the matching
account, they can return to the content.

.. important::

   The external LMS must be configured to send
   ``lis_person_contact_email_primary``. Without it, this check always
   fails, regardless of whether the learner is signed in.

This check runs only on the first launch per learner. Once Open edX
has linked their identities, subsequent launches proceed without the
check.

Use this mode when learners must have pre-existing accounts on your
Open edX instance and you want activity tied to those accounts.

If both `Require User Account` and `Use LTI PII` are checked,
`Require User Account` takes precedence.

Delivering Content in an iframe with Require User Account
---------------------------------------------------------

When this mode is used and content is embedded in an iframe, browsers
may block the session cookie. Add the following settings to your Tutor
plugin under ``openedx-lms-common-settings``:

.. code-block:: python

    SESSION_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE_FORCE_ALL = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'
    X_FRAME_OPTIONS = "ALLOW-FROM <your-lti-consumer-domain>"

After adding these settings, run:

.. code-block:: bash

    tutor config save
    tutor local restart lms

*****************************
Caveats
*****************************

- Enabling `Require User Account` only affects future LTI launches.
  Existing anonymous account data is not migrated.
- Disabling `Require User Account` after it has been enabled does not
  unlink accounts. If a rollback is needed, create a new consumer record
  with the flag disabled and use the new credentials in the external LMS.

*****************************
Grade Aggregation Delay
*****************************

When the external LMS links to a unit or subsection (rather than a
single problem), Open edX aggregates grades across all problems before
passing them back. Individual problem components return grades
immediately. The delay applies only to unit and subsection level links.

The default aggregation interval is 15 minutes. To change it, add the
following to your Tutor plugin under ``openedx-lms-common-settings``:

.. code-block:: python

    LTI_AGGREGATE_SCORE_PASSBACK_DELAY = 15 * 60  # seconds

Replace ``15 * 60`` with your desired interval in seconds. Then apply
the change:

.. code-block:: bash

    tutor config save
    tutor local restart lms


.. seealso::

   :ref:`Using Open edX as an LTI Tool Provider` (educator)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-06   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+

.. include:: /links.txt
