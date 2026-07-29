.. _Verawood Course Authoring Roles:

Course Authoring Roles and Permissions
############################################

   .. image:: /_images/educator_how_tos/console_course_team_members.png
      :alt: The Team Members tab of the Roles and Permissions console, showing course team members
      :width: 800

With Verawood, course authoring joins the Roles and Permissions console
already used for content libraries. Course team management now also
uses the same assignment and permission patterns as libraries,
available through the same console (see
:ref:`Verawood Roles and Permissions Console`).

Course Admin and Course Staff are the new system's equivalents of the
legacy Admin and Staff roles for a course: same responsibilities, new
assignment mechanism.

This feature is opt-in: the Course Authoring waffle flag is disabled by
default and can be enabled per platform, organization, or course. See
`Enabling the Feature`_ below for setup instructions.

.. _Verawood Authoring Roles Available:

Roles
*****

* **Course Admin** — the new-system equivalent of the legacy Admin
  role: course team management through the Roles and Permissions
  console and full authoring access in Studio.

* **Course Staff** — the new-system equivalent of the legacy Staff
  role: full course lifecycle management in Studio.

For a full breakdown of what each role can do, see
:ref:`Course Authoring Roles Under the New Roles and Permissions System <New System Course Authoring Roles>`.

Scope and Impact
****************

While this feature is enabled, the platform supports both the legacy
Instructor Dashboard roles (Admin, Staff, Limited Staff) and the new
Course Admin / Course Staff roles at the same time. New roles apply
according to the scope where the flag is enabled — platform,
organization, or course.

The Roles and Permissions console shows and lets you act on
course-authoring roles only for the specific courses and organizations
where the Course Authoring flag is actually enabled — not simply
because it's enabled somewhere else in your access. Turning the flag
on or off also triggers a migration of role assignments behind the
scenes: for a single course or organization this can happen
automatically, depending on your site's configuration, but a
platform-wide change always requires your site operator to run the
migration manually. Until that migration finishes, there can be a
brief window where a role assignment does not yet reflect the current
flag state. This is expected during a flag transition — if it doesn't
resolve on its own, check with your site operator.

Enabling the Feature
*********************

Disabled by default. Can be enabled at the platform, organization, or
course level. See the operator release notes:
https://openedx.atlassian.net/wiki/spaces/OEPM/pages/6331662350/RBAC+AuthZ+for+Course+Authoring+-+Operator+Release+Notes#Enabling-the-Feature-Flag

Migration of Existing Course Role Assignments
**********************************************

Verawood includes migration tools to synchronize existing Admin and
Staff course role assignments between the legacy system and Roles and
Permissions. Depending on how your site is configured, this can happen
automatically when the Course Authoring flag is turned on for a course
or organization — existing Admin and Staff assignments carry over to
the new system without manual steps. If automatic migration isn't
enabled on your site, your site operator can run the migration
separately. Either way, no role assignments are lost in the process.

Future Improvements
*******************

The Course Authoring waffle flag is expected to default to enabled at
the platform level in a future release (timeline not yet committed).

After Verawood, the Roles and Permissions work is expected to continue
in several directions:

New Studio roles are planned to separate authoring responsibilities
from managing an active course, and to introduce a read-only role for
reviewing course content in Studio without edit access.

Roles and Permissions will also expand to the LMS, bringing the same
model to learner-facing features and runtime course management.

Documentation with design patterns, guides, and extension points for
the community to build on top of the new system are also on the
roadmap.

.. seealso::

   :ref:`Verawood Roles and Permissions Console` (release notes)

   :ref:`Manage Course Authoring Roles` (how-to)

   :ref:`Guide to Course Team Roles` (reference)

   :ref:`Add Course Team Members` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| [DATE]       | [REVIEWER]                    |   Verawood     | [PASS/FAIL]                    |
+--------------+-------------------------------+----------------+--------------------------------+
