.. _Verawood Copyright Acceptance:

Gating Studio Uploads Behind User Agreement Acceptance
#######################################################

Administrators can now configure user agreements that must be accepted before a
user can access the file or video upload pages for a course in Studio. This
can be used to gate access to these features behind acceptance of terms and
conditions, such as a copyright agreement or fair use policy.

When configured, users see an alert on the upload page, and the file or video
management UI is blurred and disabled. Once users accept the agreement, the
alert disappears and the UI becomes fully available.

You can use the same agreement or different agreements for both pages, and you
can require multiple agreements for either or both pages. No agreements are
configured in the default platform unless explicitly set up by an operator.

The system tracks user acceptance. If an agreement is updated, it prompts users
to re-accept.

Site operators should see :ref:`Configure copyright acceptance` to set up this feature on the backend.


.. seealso::

   :ref:`Verawood Product Notes` (reference)

   :ref:`Verawood Dev Notes` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-07-30   | OpenCraft                     | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
