.. _Grant Course Creation Access in Studio:

Grant Course Creation Access in Studio
######################################

.. tags:: site operator, how-to

.. contents::
  :local:
  :depth: 1

When the course creator group is enabled on your site, new authors cannot create
courses in Studio until an administrator grants them access. This how-to
describes how to review a request and grant (or deny) course creation access
using the Studio Django admin.

The most common point of confusion is *where* this is done: course creation
access is managed in the **Studio (CMS)** Django admin, not the LMS Django admin.
The **Course Creators** admin app does not exist in the LMS, so looking for it
there is a dead end.

The author-facing side of this process is described in
:ref:`Request Access to Create Courses`.

Prerequisite
************

Course creation access is only requested and granted when the course creator
group is enabled with the ``ENABLE_CREATOR_GROUP`` setting (enabled by default
in Studio). When this setting is disabled, any signed-in user can create
courses, and there is nothing to grant.

You must sign in with an account that has **staff** (``is_staff``) or
**superuser** permissions to change records in the Course Creators admin app.

.. note::
  Users who are marked as global staff (``is_staff``) always have course
  creation access and are not added to the Course Creators table. You only need
  to grant access to non-staff authors.

Open the Course Creators Admin App
**********************************

#. Confirm that the author has requested access. When an author requests course
   creation rights from the Studio home page, their status changes to
   **pending** and, if email is configured, an email notification is sent to the
   address in the ``STUDIO_REQUEST_EMAIL`` setting.

#. Sign in to Studio with your staff or superuser account.

#. Go to the Studio Django admin **Course Creators** app. This is served by
   Studio (CMS), so use your Studio domain:

   .. code-block:: text

     https://<your-studio-domain>/admin/course_creators/coursecreator/

   .. important::
     This app lives in the **Studio** Django admin. It is not available in the
     LMS Django admin. If you browse the LMS admin (for example,
     ``https://<your-lms-domain>/admin/``) you will not find a Course Creators
     app.

#. The list page shows each author's username, email, current state, and whether
   they have access to all organizations. Select the user whose request you want
   to review.

Grant or Deny Access
********************

On the author's record, you control access with the **State** field and the
organization fields.

#. Set the **State** field:

   * **granted** - the author can create courses.
   * **denied** - the author is not allowed to create courses.
   * **pending** - the request is awaiting review (this is the state set when
     the author requests access).
   * **unrequested** - the author has not requested access.

#. When you set the state to **granted**, choose the scope of access:

   * To allow the author to create courses under **any** organization, leave
     **All organizations** selected and do not select any specific
     organizations.

   * To limit the author to **specific** organizations, clear the **All
     organizations** checkbox and select one or more organizations from the
     list.

   .. note::
     You must choose exactly one of these options. Selecting **All
     organizations** *and* specific organizations at the same time, or clearing
     **All organizations** without selecting any specific organization, produces
     a validation error when you save.

#. (Optional) Use the **Note** field to record context about the decision, such
   as why access was denied.

#. Select **Save**.

When you save, the platform updates the author's roles accordingly and, if email
is configured, notifies the author that their course creation access has changed.

Verify the Change
*****************

Ask the author to return to the Studio home page and reload it. If access was
granted, they will now see the option to create a new course. If you granted
access to specific organizations only, they will be able to create courses under
those organizations but not others.

.. seealso::

  :ref:`Request Access to Create Courses` (how-to, for authors)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-08-14   |  Ty Hob                       | Verawood       | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
