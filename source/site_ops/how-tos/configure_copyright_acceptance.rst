.. _Configure copyright acceptance:

Configure User Agreement Acceptance for Studio Uploads
*******************************************************

.. tags:: site operator, how-to

Setting this up requires two steps: creating the agreement record and then
configuring where it applies.

Step 1: Create a UserAgreement
==============================

In the Django admin, go to :guilabel:`/agreements/useragreement/` and create a
new ``UserAgreement``. Each agreement requires the following fields:

- **Type** — a unique identifier used to track where this agreement applies
  (for example, ``fair-use-terms`` or ``copyright-assignment``).
- **Name** and **Summary** — these appear in the alert banner shown to users.
- **URL** — required; displayed as a **Learn more** link in the alert banner.

Step 2: Configure Agreement Gating via SiteConfiguration
=========================================================

Configure where the agreement applies using the ``MFE_CONFIG_API`` in
``SiteConfiguration``. In the ``MFE_CONFIG`` section, add an
``AGREEMENT_GATING`` key. Under it, create a key for each gated feature with
one or more agreement types that must be accepted.

The supported feature keys are:

- ``upload`` — applies to both file and video upload pages
- ``upload.files`` — applies only to the file upload page
- ``upload.videos`` — applies only to the video upload page

For a single agreement, provide the agreement type as a string. For multiple
agreements, provide a list of type strings.

Example configuration:

.. code-block:: json

   {
       "MFE_CONFIG": {
           "AGREEMENT_GATING": {
               "upload": "fair-use-terms",
               "upload.files": "copyright-assignment",
               "upload.videos": [
                   "video-format-agreement"
               ]
           }
       }
   }

In this example:

- All users uploading files or videos see the ``fair-use-terms`` agreement.
- Users uploading files also see the ``copyright-assignment`` agreement.
- Users uploading videos also see the ``video-format-agreement`` agreement.

Acceptance is tracked by agreement type only, so a user who accepted
``fair-use-terms`` on the files page does not need to accept it again on the
videos page.

Prompt Users to Re-accept an Updated Agreement
***********************************************

If you update an agreement and need users to re-accept it, update the
agreement's **updated date** field. Any user who accepted the agreement before
that date will be prompted to re-accept.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-07-30   | OpenCraft                     | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+