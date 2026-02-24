.. _Configure Learner Unenroll Survey:

Configure Learner Unenroll Survey
###################################

.. tags:: site operator, how-to

Overview
********

When learners unenroll from a course in the Learner Dashboard, they can optionally be shown a survey asking them for their reason for unenrolling. This survey helps course teams and site operators understand why learners are leaving courses and can inform improvements to course content and platform features.

As of the Verawood release, the unenroll survey can be configured to be either shown or skipped entirely. This allows site operators to customize the unenrollment experience based on their institutional needs.

This document explains how to configure the ``SHOW_UNENROLL_SURVEY`` setting for the **frontend-app-learner-dashboard** micro-frontend (MFE).

Configuration Options
*********************

The unenroll survey behavior is controlled by the ``SHOW_UNENROLL_SURVEY`` environment variable, which accepts a boolean value:

* ``true (default)``: Shows the unenroll survey modal after the learner confirms they want to unenroll. The survey presents multiple-choice reasons and an optional custom text field.
* ``false``: Skips the survey entirely and unenrolls the learner immediately after they confirm the unenrollment action.

Unenrollment Flow
=================

**When** ``SHOW_UNENROLL_SURVEY`` **is true:**

#. Learner clicks "Unenroll" from the course actions menu
#. Confirmation modal appears asking "Are you sure you want to unenroll?"
#. Learner clicks "Unenroll" button in the confirmation modal
#. Survey modal appears asking "Why are you unenrolling?"
#. Learner selects a reason (or skips the survey)
#. Learner is unenrolled and sees a success message

**When** ``SHOW_UNENROLL_SURVEY`` **is false:**

#. Learner clicks "Unenroll" from the course actions menu
#. Confirmation modal appears asking "Are you sure you want to unenroll?"
#. Learner clicks "Unenroll" button in the confirmation modal
#. Learner is unenrolled immediately and sees a success message

Survey Reasons
==============

When the survey is enabled (``SHOW_UNENROLL_SURVEY=true``), learners can choose from the following predefined reasons:

* I don't have the academic or language prerequisites
* The course material was too hard
* The course material was too easy
* This won't help me reach my goals
* Something was broken
* I don't have the time
* I just wanted to browse the material
* I don't have enough support
* I am not happy with the quality of the content
* Other (custom text input)
* I prefer not to say

Configuring the Setting
************************

The configuration method depends on your deployment approach:

For Tutor Deployments
======================

If you're using Tutor to manage your Open edX installation, you can configure this setting using a Tutor plugin:

1. Create or edit a Tutor plugin file (e.g., ``myplugin.py``)

2. Add the following configuration using the appropriate settings hook:

   .. code-block:: python

       from tutor import hooks

       hooks.Filters.ENV_PATCHES.add_item(
           (
               "openedx-lms-production-settings",
               """
       MFE_CONFIG["SHOW_UNENROLL_SURVEY"] = {{ SHOW_UNENROLL_SURVEY|tojson }}
       """
           )
       )

       hooks.Filters.ENV_PATCHES.add_item(
           (
               "openedx-lms-development-settings",
               """
       MFE_CONFIG["SHOW_UNENROLL_SURVEY"] = {{ SHOW_UNENROLL_SURVEY|tojson }}
       """
           )
       )

       hooks.Filters.CONFIG_DEFAULTS.add_item(
           ("SHOW_UNENROLL_SURVEY", True)
       )

3. Enable the plugin:

   .. code-block:: bash

       tutor plugins enable myplugin

4. Save the new configuration:

   .. code-block:: bash

       tutor config save

5. If you want to disable the survey, you can set the value when saving the configuration:

   .. code-block:: bash

       tutor config save --set SHOW_UNENROLL_SURVEY=false

6. Rebuild and restart the MFE:

   .. code-block:: bash

       tutor images build mfe
       tutor local start -d

For Direct MFE Deployment
==========================

If you're deploying the frontend-app-learner-dashboard MFE directly (without Tutor):

1. Locate your MFE's ``.env`` file or environment configuration

2. Add or modify the following line:

   .. code-block:: bash

       SHOW_UNENROLL_SURVEY=true

   Or to disable the survey:

   .. code-block:: bash

       SHOW_UNENROLL_SURVEY=false

3. Rebuild the MFE:

   .. code-block:: bash

       npm run build

4. Restart your web server to apply the changes

Verifying the Configuration
****************************

To verify that the configuration has been applied correctly:

1. Log in to your Open edX site as a learner

2. Enroll in a test course

3. Navigate to your learner dashboard

4. Click on the course actions menu (three dots) for the test course

5. Click **Unenroll**

6. Observe the unenrollment flow:

   * If ``SHOW_UNENROLL_SURVEY`` is **true**: You should see a survey modal after confirming unenrollment
   * If ``SHOW_UNENROLL_SURVEY`` is **false**: You should be unenrolled immediately after confirming, without seeing the survey


Related Information
*******************

* **Product Proposal**: `Configurable Un-enrollment Survey`_
* **GitHub Issue**: `#765 - Make course unenrollment survey configurable`_
* **Pull Request**: `#738 - Make unenroll survey configurable`_
* **Frontend App Repository**: `frontend-app-learner-dashboard`_

.. _Configurable Un-enrollment Survey: https://openedx.atlassian.net/wiki/spaces/OEPM/pages/5395841025/Proposal+Configurable+Un-enrollment+Survey
.. _#765 - Make course unenrollment survey configurable: https://github.com/openedx/frontend-app-learner-dashboard/issues/765
.. _#738 - Make unenroll survey configurable: https://github.com/openedx/frontend-app-learner-dashboard/pull/738
.. _frontend-app-learner-dashboard: https://github.com/openedx/frontend-app-learner-dashboard

Troubleshooting
***************

Survey not showing when expected
=================================

If you've set ``SHOW_UNENROLL_SURVEY=true`` but the survey isn't appearing:

1. Verify that the environment variable is correctly set in your deployment
2. Clear your browser cache and MFE cache
3. Check the browser console for any JavaScript errors
4. Ensure you've rebuilt the MFE after changing the configuration
5. Verify that the MFE is loading the correct configuration using the browser console method above

Survey still showing when disabled
===================================

If you've set ``SHOW_UNENROLL_SURVEY=false`` but the survey still appears:

1. Verify that the configuration has been properly saved
2. Restart the MFE service
3. Clear any CDN or proxy caches that might be serving old versions of the MFE
4. Check if there are multiple configuration sources (e.g., site configuration overriding the default)

Institutional Considerations
*****************************

Benefits of Enabling the Survey
================================

* **Data-driven insights**: Collect valuable feedback about why learners are leaving courses
* **Course improvement**: Help instructors identify problem areas in their courses
* **Platform improvement**: Identify systemic issues that affect multiple courses
* **Research opportunities**: Generate data for educational research

Benefits of Disabling the Survey
=================================

* **Streamlined experience**: Reduce friction in the unenrollment process
* **Learner autonomy**: Respect learners who want to leave quickly without providing feedback
* **Lower abandonment rates**: Some learners might abandon unenrollment if required to complete a survey
* **Compliance**: Meet institutional policies that prohibit mandatory or suggested feedback collection

**Maintenance chart**

+--------------+-------------------------------+--------------------+--------------------------------+
| Review Date  | Working Group Reviewer        | Release            | Test situation                 |
+--------------+-------------------------------+--------------------+--------------------------------+
| 2026-02-23   | Muhammad Arslan Abdul Rauf    | master (>Ulmo)     | Verified on local deployment   |
+--------------+-------------------------------+--------------------+--------------------------------+
