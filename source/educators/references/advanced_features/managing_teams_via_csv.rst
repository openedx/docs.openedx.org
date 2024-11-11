.. _Managing Teams via CSV Upload:

##########################################
Managing Teams via CSV Upload
##########################################

.. tags:: educator, reference
    
Initial Setup
-------------
There are cases where an instructor may want to manage team membership within a course
(e.g. assigning groups for team assignments). To do this, an instructor must configure
a team-set as ``public_managed`` or ``private_managed`` by following the Teams Configuration guide.

When this condition is met, an instructor can navigate to the **Teams** tab where the **Manage**
sub-tab will now be available alongside the **My Team** and **Browse** sub-tabs. Clicking the **Manage**
tab opens the **Manage** page where team membership can be viewed and modified.

.. image:: /_images/educator_references/Teams_ManageTab.png
   :width: 600
   :alt: The Manage Teams tab on the teams Page, which lets you download and upload a csv
     describing the team memberships for a course

Membership CSV File Schema
--------------------------

Team membership assignments are done through a CSV file upload. The membership CSV is formatted as follows:

.. code::

    user,              mode,              <team-set>,           <team-set>,           <...>
    <user-identifier>, <enrollment-mode>, <team-name-or-empty>, <team-name-or-empty>, <...>
    <user-identifier>, <enrollment-mode>, <team-name-or-empty>, <team-name-or-empty>, <...>
    <...>

The **header row** contains the headers “``user``”, “``mode``”, and an entry for each team-set within a course.
For example, a course with 2 team-sets (``discussion-teams`` and ``case-studies``) would start like this:

.. code::

    user, mode, discussion-teams, case-studies

Each additional row is a **user row** and has a ``user-identifier``
(which, in priority order, is the ``student-key``, ``edx-username``, or ``edx-email``),
``enrollment mode`` (one of ``audit``, ``verified``, or ``masters``), and the ``team`` assignment for the matchin
team-set in the header row. For example, here are 8 students assigned across different teams in the 2 team-sets:

.. code::

    user,            mode,     discussion-teams, case-studies
    alice,           verified, Team 1,           Team A
    bob@example.com, verified, Team 1,           Team B
    mitx_39181873,   verified, Team 1,           Team C
    derek,           verified, Team 2,           Team A
    edith,           verified, Team 2,           Team B
    felicia,         verified, Team 2,           Team C
    garrett,         verified, ,                 Team C
    hannah,          masters,  Team A,           Team 1

**Note** that since teams are only unique within a team-set, the “Team A” that hannah is a member of for the
“discussion-teams” team-set is different from the “Team A” in “case-studies” that alice and derek are assigned to.


Managing Teams
---------------

.. note:: Prerequisites: at least one managed team-set configured for course

From the **Teams > Manage** page, an instructor can use a CSV file, formatted per the schema above, to manage team memberships.

An instructor should first get current memberships by going to the **View Current Team Memberships** section and
clicking the *Download Memberships* button. This downloads a membership CSV file showing all enrolled students
and configured team-sets for the course.

Staff can then modify this document (as below) before browsing to the file and uploading it in the
**Assign Team Memberships** section.


Actions
~~~~~~~~

A **user can be added or moved** to a ``team`` by adding the ``team-name`` in the appropriate ``team-set`` column.
If the team does not already exist within the team-set a **new team will be created**.

.. note:: ``team-name`` and ``team-set`` * **are case sensitive.** *

A **user can be removed** from a team by removing the ``team-name`` from the appropriate ``team-set`` column,
leaving the entry empty.

.. note:: team-sets cannot be created from within the Manage tab. They must be created by following the
   Teams Configuration instructions.

Users and team-sets that are **not included** in the uploaded CSV are **not altered**.

Examples
---------
Initial Setup
~~~~~~~~~~~~~~

Remus Lupin is setting up his course, Defense Against the Dark Arts and wants to assign groups for his students
to write about different dark creatures and curses. Following the Teams Configuration instructions, he sets up
two managed team-sets, ``dark-creatures`` and ``curses``.

Next, he goes to the **Teams > Manage** page and clicks *Download Memberships* to get the following membership CSV:

.. code::

    user,      mode,       dark-creatures,  curses
    harry,     verified,                 ,
    ron,       audit,                    ,
    luna,      verified,                 ,
    draco,     verified,                 ,
    hermione,  masters,                  ,
    cho,       masters,                  ,

Lupin splits his students into several teams, making sure to not put ``masters`` and non-masters students on the same team,
and edits the CSV accordingly:

.. code::

    user,      mode,       dark-creatures,  curses
    harry,     verified,   Dragons,         Mimble Wimble
    ron,       audit,      Dragons,         Morsmordre
    luna,      verified,   Werewolves,      Morsmordre
    draco,     verified,   Werewolves,      Mimble Wimble
    hermione,  masters,    Basiliks,        Expulso
    cho,       masters,    Basiliks,        Expulso

In the *Assign Team Memberships* section, Lupin browses to his updated membership CSV and clicks *Upload Memberships*.
The new teams are created and his students are assigned to the corresponding teams: Harry and Ron are assigned to the
“Dragons” team for the ``dark-creatures`` team-set. Harry is assigned to the “Mimble Wimble” team in the ``curses``
team-set, while Ron is on the “Morsmorde” team, and so on.

----

Later, Lupin goes back to the **Teams > Manage** page to download new memberships and finds that Fred and George joined
the class after the initial team assignments.

.. code::

    user,      mode,       dark-creatures,  curses
    harry,     verified,   Dragons,         Mimble Wimble
    ron,       audit,      Dragons,         Morsmordre
    luna,      verified,   Werewolves,      Morsmordre
    draco,     verified,   Werewolves,      Mimble Wimble
    hermione,  masters,    Basiliks,        Expulso
    cho,       masters,    Basiliks,        Expulso
    fred,      audit,      ,
    george,    audit,      ,

He decides he wants to add them to the “Werewolves” and “Dragons” teams for the ``dark-creatures`` team-set but wants them
on a new “Confringo” team for ``curses``.

.. code::

    user,      mode,       dark-creatures,  curses
    harry,     verified,   Dragons,         Mimble Wimble
    ron,       audit,      Dragons,         Morsmordre
    luna,      verified,   Werewolves,      Morsmordre
    draco,     verified,   Werewolves,      Mimble Wimble
    hermione,  masters,    Basiliks,        Expulso
    cho,       masters,    Basiliks,        Expulso
    fred,      audit,      Werewolves,      Confringo
    george,    audit,      Dragons,         Confringo

Uploading this updated CSV, the new “Confringo” team is created and Fred and George have been assigned to their respective teams.


Error Conditions
-----------------

**Header must contain column ‘user’ / Header must contain column ‘mode’**

The CSV is improperly formatted: the first row must contain the headers “user” and “mode”, in that order
(see Membership CSV File Schema).

**Teamset with id [ID] is duplicated**

A team-set cannot be listed more than once in the header of the CSV file. Remove the duplicated column and confirm
desired team mappings before re-uploading.

**Teamset with id [ID] does not exist**

Team-sets must be configured in Teams Configuration before teams can be assigned. Teams, however, can be created
directly from the Membership CSV.

**Team(s) [team] don’t have matching teamsets**

The team was entered in a column without a team-set, often caused by a column number mismatch or stray comma.
Correct the typo and re-upload.

**Username [name] listed more than once in file**

Users within a file should be unique. Remove the duplicate row and confirm desired team mappings before re-uploading.

**User name/email/external key: [ID] does not exist**

The ID in the “user” column (which could be a username, email, or external key) did not map to a user in our records.
Correct any typos and re-upload.

**User [username] is not enrolled in this course**

Users must be enrolled to be assigned to teams in a course. Remove or enroll the unenrolled user before re-uploading.

**User [username] enrollment mismatch**

The user “mode” specified in the CSV file does not match the user’s actual enrollment mode. Downloading memberships
should automatically populate the correct enrollment modes for each enrolled user. Alternatively, correct the user’s
enrollment mode making sure that team assignments do not mix masters and non-masters enrollment modes and re-upload.

**Team [team] cannot have Master’s track users mixed with users in other tracks.**

FERPA protections prohibit ``masters`` and non-masters (``audit`` and ``verified``) enrolled students from being on the same team.

If the team already exists, the enrollment mode of the first member assigned to that team sets the team’s protection level.
For example, if the first member assigned to a team is a non-master’s student, masters students cannot join.
If this team will be newly created through the CSV upload, the team makeup must be exclusively ``masters`` or non-masters
students to pass validation. Edit team mappings to create designated teams for ``masters`` and non-masters students and re-upload.

**New membership for team [team] would exceed max size of [max-size]**

Team-sets have a ``max-team-size`` configured in Teams Configuration.
The newly proposed team memberships would exceed the capacity of the given teams.
Increase the team-set size or redistribute users to different/more teams and re-upload.

.. seealso::
 :class: dropdown

 :ref:`Teams Overview <CA_Teams_Overview>` (concept)

 :ref:`Managing Team Discussions <Teams Discussions>` (concept)

 :ref:`Enable and Configure Teams` (how-to)

 :ref:`Teams Configuration Options` (reference)

 :ref:`The Learner's Experience of Teams <CA Learner Experience of Teams>` (concept)
