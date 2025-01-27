.. _Columns in the Student Profile Report:

===========================================
Columns in the Student Profile Report
===========================================

.. tags:: educator, reference

The student profile report includes a row for each enrolled learner or course
team member and the following columns. The fields fields that are available for 
students to fill out in **Account Settings** (and therefore will be populated
in this report) are configurable in the Open edX site configuration. 


.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - Column
     - Required?
     - Description
   * - id
     - Yes
     - The user account ID number that the system assigns to each registrant.
   * - username
     - Yes
     - The public username entered by the learner. Usernames cannot be changed
       except by requesting account deletion.
   * - name
     - Yes
     - The full name entered by the learner. Learners can update this value on
       the **Account Settings** page.
   * - email
     - Yes
     - The email address entered by the learner. Learners can update this
       value on the **Account Settings** page.
   * - language
     - No
     - This column is included for backward compatibility only. This data is
       no longer collected during account creation. The selection that a
       learner makes for language on the **Account Settings** page is not
       included in this report.
   * - location
     - No
     - This column is included for backward compatibility only. The selection
       that a learner makes for **Country** during registration or for
       **Country or Region** on the **Account Settings** page is displayed in
       the "country" column of this report.
   * - year_of_birth
     - No
     - This column is included for backward compatibility only. The selection
       that a learner makes for **Year of birth** on the **Account Settings**
       page is explicitly excluded from this report now.
   * - gender
     - No
     - This value can be updated on the **Account Settings** page.
   * - level_of_education
     - No
     - This value can be updated on the **Account Settings** page. For a list
       of the possible values, see the description of the `auth_userprofile`_
       table's level_of_education column in the *EdX Research Guide*.
   * - mailing_address
     - No
     - This column is included for backward compatibility only. It is no
       longer collected during registration. Previously, this value was
       optional and was supplied only at registration.
   * - goals
     - No
     - This column is included for backward compatibility only. It is no
       longer collected during registration. Previously, this value was
       optional and was supplied only at registration. This is not related
       to the course goals feature.
   * - enrollment_mode
     - Yes
     - Indicates the enrollment track that the learner is enrolled in, such as
       "audit" or "verified".
   * - verification_status
     - No
     - This column is only included if the ID verification feature is enabled
       and ``verification_status`` is included in the site's
       ``student_profile_download_fields`` setting.

       Indicates whether learners who are enrolled in course tracks that require
       ID verification have successfully verified their identities to edX by
       submitting an official photo ID via webcam. The value in this column is
       "N/A" for learners enrolled in course tracks that do not require ID
       verification.

       A value of "Not ID Verified" in this column indicates that the learner is
       enrolled in a course track that requires ID verification (such as
       "verified") but she has not attempted ID verification, or the ID
       verification has failed or expired.

       A value of "ID Verified" indicates that the learner is enrolled in a
       course track that requires ID verification, and her ID verification is
       current and valid.

   * - cohort
     - No
     - This column is included only if the course has cohorts enabled. For
       courses that include learner cohorts, shows the name of the cohort group
       that is assigned to the learner. If a learner is not assigned to a
       cohort, the value is ``[unassigned]``.
   * - team
     - No
     - This column is included only if the course has teams enabled. For courses
       that include teams, shows the name of the team that the learner belongs
       to. If a learner has not joined a team, the value is ``[unavailable]``.
   * - city
     - No
     - This column is included for backward compatibility only. Data for this
       column is not currently collected.
   * - country
     - No
     - On some sites, such as edx.org, learners are required to specify
       **Country** during registration. By default this is not required. This
       value can be updated or set on the **Account Settings** page.

.. seealso::
 :class: dropdown

 :ref:`Learner Data` (concept)

 :ref:`View and download student data` (how-to)

 :ref:`Access Anonymized Learner IDs <Access_anonymized>` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
