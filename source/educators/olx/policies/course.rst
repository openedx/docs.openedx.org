.. _Course Policies:

#################################
Create OLX Course Policies
#################################

.. tags:: educator, how-to

You create a course policy file to specify metadata about your course.

.. contents::
  :local:
  :depth: 1

*******************************
Create the Course Policy File
*******************************

You define policies for your course in the ``policy.json`` file.

Save the ``policy.json`` file in the ``policy/<course-name>`` directory.

The ``<course-name>`` directory  must match the value of the ``url_name``
attribute in the ``course.xml`` file.

************************************
Course Policy JSON Objects
************************************

.. note::

  This is a partial list of supported fields in the ``policy.json`` file.
  Many more are available; these can be variously found on the Open edX Studio's "Advanced
  Settings" page, the Pages & Resources view, and the Course Settings page.



.. list-table::
    :widths: 10 80
    :header-rows: 0

    * - ``start``
      - The start date for the course, in UTC. For example: ``"2025-06-01T00:00:00Z"``.
    * - ``advertised_start``
      - The start date, in UTC, displayed in the course listing and course about pages.
        For example: ``"2025-06-15T00:00:00Z``.
    * - ``advanced_modules``
      - A list of non-standard XBlocks to use in the course, eg ``["lti", "scorm"]``
    * - ``enrollment_start``, ``enrollment_end``
      - The dates (in UTC) in which students can enroll in the course. For example,
        ``"2025-05-01T00:00:00Z"``. If not specified, students can enroll any
        time.
    * - ``end``
      - The end date for the course, in UTC. For example: ``"2027-06-01T12:00:00Z"``.
    * - ``graceperiod``
      - The amount of time learners have after a deadline to provide their answers,
        for example, ``"7200 seconds"``.
    * - ``tabs``
      - Custom pages, or tabs, in the courseware.  See below for details.
    * - ``discussion_blackouts``
      - An array of time intervals during which students cannot create or edit
        discussion posts. For example, you could specify blackout dates during
        exams. For example:

        ``[[""2017-10-29T04:00", "2017-11-03T04:00"], ["2017-12-30T04:00", "2018-01-02T04:00"]]``

        Course team members with the Discussion Moderator, Community TAs, or
        Administrator role are not restricted during blackout periods.

    * - ``show_calculator``
      - Whether the calculator is shown in the course (``true``) or not
        (``false``).
    * - ``days_early_for_beta``
      - The number of days early that students in the beta-testers group can
        access the course.
    * - ``cohort_config``
      -
        * ``cohorted`` : Boolean.  Set to ``true`` if this course uses
          student cohorts.  If so, all inline discussions are automatically
          cohorted, and top-level discussion topics are configurable via the
          ``cohorted_discussions`` list. Default is ``false``, not cohorted).
        * ``cohorted_discussions``: list of discussion topics that should be
          cohorted.  Any not specified in this list are not cohorted.
        * ``auto_cohort_groups``: ``["group name 1", "group name 2", ...]``
          If ``cohorted`` is ``true``, each student is automatically assigned
          to a random group from this list, creating the group if needed.
    * - ``pdf_textbooks``
      - Have pdf-based textbooks on tabs in the courseware.  See below for
        details.
    * - ``html_textbooks``
      - The addition of HTML-based textbooks on tabs in the courseware has
        been deprecated.


*******************************
Example Course Policy File
*******************************

An example with a few of the settings defined in the course policy file
follows.

.. code-block:: json

  

  {
      "course/2025": {
          "advanced_modules": [
              "edx_sga",
              "lti",
              "scorm",
              "poll",
              "survey"
          ],
          "cert_html_view_enabled": true,
          "certificates_display_behavior": "CertificatesDisplayBehaviors.END",
          "course_image": "Intro_to_OLX_course_card.png",
          "discussion_topics": {
              "General": {
                  "id": "course"
              }
          },
          "discussions_settings": {
              "enable_graded_units": false,
              "enable_in_context": true,
              "provider_type": "openedx",
              "unit_level_visibility": true
          },
          "display_name": "OLX Example Course",
          "end": "2027-06-01T00:00:00Z",
          "enrollment_end": "2026-01-31T00:00:00Z",
          "enrollment_start": "2025-05-01T00:00:00Z",
          "graceperiod": "7200 seconds",
          "instructor_info": {
              "instructors": []
          },
          "language": "en",
          "learning_info": [],
          "lti_passports": [
              "codeboard:codeboard_key_1:codeboard_secret_1234",
              "jupyter:811a447706c152588c436ee13addeeb889e7f256033679408737bd5bc4118225:869e9639af7de74929b13ae17ad22e4efb60d9d112143e287589289102e1de00"
          ],
          "minimum_grade_credit": 0.8,
          "pdf_textbooks": [
              {
                  "chapters": [
                      {
                          "title": "Full Book",
                          "url": "/asset-v1:OpenedX+OLXex+2025+type@asset+block@Education_for_a_Digital_World.pdf"
                      }
                  ],
                  "id": "6Education_for_a_Digital_World",
                  "tab_title": "Education for a Digital World: Advice, Guidelines and Effective Practice from Around Globe"
              }
          ],
          "start": "2025-06-01T00:00:00Z",
          "tabs": [
              {
                  "course_staff_only": false,
                  "name": "Course",
                  "type": "courseware"
              },
              {
                  "course_staff_only": false,
                  "name": "Progress",
                  "type": "progress"
              },
              {
                  "course_staff_only": false,
                  "name": "Dates",
                  "type": "dates"
              },
              {
                  "course_staff_only": false,
                  "name": "Discussion",
                  "type": "discussion"
              },
              {
                  "course_staff_only": false,
                  "is_hidden": true,
                  "name": "Wiki",
                  "type": "wiki"
              },
              {
                  "course_staff_only": false,
                  "name": "Textbooks",
                  "type": "textbooks"
              },
              {
                  "course_staff_only": false,
                  "name": "Textbooks",
                  "type": "pdf_textbooks"
              },
              {
                  "course_staff_only": false,
                  "name": "HTML Custom Tab",
                  "type": "static_tab",
                  "url_slug": "html_custom_tab"
              }
          ]
      }
  }

.. seealso::

  :ref:`Course Asset Policy` (reference) 

  :ref:`What is Open Learning XML?` (concept)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-11-06   | sarina                        |  Ulmo          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
