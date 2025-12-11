.. _Ulmo Roles and Permissions:

Roles and Permissions in Libraries
#######################################

The Ulmo release introduces the first phase of the new roles and permissions
system for the Open edX platform. This MVP focuses on establishing a shared
authorization service and connecting it to the latest version of Libraries, so
the same model can be extended to other parts of the platform over time.

Any user who has a role in a library can open the library team manager in the
new Administrative Console from Studio. This view shows all members of the
library, the role each person holds, and the permissions associated with each
role. Library Admins and global admins can use this view to assign or revoke
roles for that library, so team membership and role information live in a single
place.

The goal of the Ulmo MVP is to introduce the new roles and permissions model to
Libraries with functional parity and a clearer model of roles, not to change how
authors create or reuse content. 

What's Available in Ulmo
************************

The Ulmo release includes:

* **Library scoped roles**: Library Admin, Library Author, Library Contributor
  and Library User, each mapped to a defined set of permissions that control who
  can view, edit, publish or reuse library content, and who can manage the
  library team.

* A new **Library Contributor** role that matches most of the Library Author
  capabilities for creating and editing content, managing tags and collections,
  and reusing content, but cannot publish content.

* Enforcement of these permissions when users view a library, edit draft
  content, publish content, manage tags and collections, reuse library content
  in courses, or manage the library team.

* A library team manager in the :ref:`Administrative Console <Ulmo console>`.
  Any user who has a role in a library can open this view to see all members,
  their roles and the available role definitions. Library Admins and global
  admins use the same view to assign or revoke roles for that library, so team
  membership and role information are managed from a single place.

* A migration tool that replicates existing library roles into the new system,
  so current configurations are preserved without manual changes.

Scope and Impact
****************

The new roles and permissions system applies only to Content Libraries, not
:ref:`Legacy Libraries <Legacy Content Libraries Overview>`. It replaces the
previous library specific authorization logic with library-scoped roles managed
by the shared authorization service and surfaced through the :ref:`Administrative
Console <Ulmo console>`.

The scope of this release is limited to:

* Libraries created and managed in Studio

* Library level roles and permissions managed through the Administrative Console

* Migration of existing library role assignments into the new roles & permissions system

The following areas are not affected in Ulmo:

* Courses, course roles and course level permissions

* Forums, cohorts and other runtime features

* Any legacy library implementations that have not yet been :ref:`migrated to Content Libraries <Migrating Legacy Libraries>`

Migration of Existing Library Access
************************************

Ulmo includes a migration path for existing library access configurations.

During the upgrade, current library role assignments are mapped into the new
roles & permissions system by the migration tool. The intent is to preserve who can
access each library and what they can do, without requiring manual configuration
from platform operators.

After the upgrade, operators can review library teams in the Administrative
Console to confirm that roles and access levels look correct. For most
deployments that already use Libraries, no additional action should be required
beyond this validation step.

Future improvements
*******************

After Ulmo, the Roles and Permissions work is expected to evolve in several
directions:

Extending the same Roles & Permissions model beyond Libraries. Course authoring is the
next candidate, and future phases will expand the roles and permissions pattern
to the LMS, forums, and other product areas.

Introducing more advanced administration features in the Administrative Console,
allowing for managing multiple scopes at once, listing users' roles across
scopes, and granting roles to multiple scopes in one action.

Exploring support for custom roles, based on feedback from operators who manage
large instances.

These improvements will be scoped and tracked in future releases once the
Libraries integration is validated in production.

.. seealso::

   :ref:`Ulmo console`

   :ref:`Add users to Libraries`

   :ref:`Migrating Legacy Libraries`


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-12-11   | Product WG                    | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+