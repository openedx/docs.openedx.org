Additional Redwood Features
===========================

Redwood contains numerous features and feature enhancements that affect quality
of life for both authors and learners.

.. contents::
  :local:
  :depth: 1

Make Sections available independently of the course outline
***********************************************************

Redwood contains a feature enhancement that enables course authors to make a
Section of the course available independently of the course outline. This is
accomplished by hiding a section from the course outline and enabling sharing of
a URL to that section at any time.

This feature unlocks a number of use cases. Course authors can freely circulate
evergreen or supplemental course content, without needing to slot it
prescriptively into the course structure. It also enables authors to add
reference links to material that must be reviewed at different times of the
course, and gives learners an easy way to consistently reference parts of the
course that may need regular review.

For more details on how to use this feature, see
:doc:`/educators/how-tos/use_section_independently_of_course_outline`.

For more details on how to turn this feature on, see :doc:`dev_op_release_notes`.

Embed an iframe into the Text Editor
************************************

Course authors can now embed iframes into the Text Editor, making it easier to
enrich the course experience with third-party content, without having students
navigate away from the course.

For more details on how to use this feature, see
:doc:`/educators/how-tos/embed_iframe_text_editor`.

This feature is turned on by default in the Text Editor.

Connect Teams in a course to Content Groups
*******************************************

Previously, course authors were only able to connect subsets of learners to
custom content sets using the Cohorts and Content Groups features. Now, course
authors can also use the Teams feature to connect subsets of learners to custom
content sets. 

For more details on how to use this feature, see
:doc:`/educators/how-tos/connect_teams_content_groups`.

For more details on how to turn this feature on, see the :doc:`dev_op_release_notes`.


New User Role: Limited Staff
****************************

There is a new role for course staff, the Limited Staff role. Users in this role
have access to the LMS and the Instructor Dashboard, but do not have access to
Studio. This role enables course staff to have full sets of permission around
running/delivering a course, but restricts access to the course content itself. 

.. warning::

    There are known issues with this feature in the Redwood Release. When a user in
    this role lands on a page in Studio, they see a ``403 error`` message. UI
    improvements will be made in future releases.











