Configuring Google Analytics
############################

As of May 2023 edx-platform supports Google Analytics 4 and the deprecated Google Universal Analytics.
Google Universal Analytics is being turned off for all customer who don't have the paid service "Google
Analytics 360" on July 1, 2023.

More information on Universal Analytics deprecation can be found in this `Google help posting`_.

Details on migrating to Google Analytics 4 can be found in `another help posting`_.

This document pertains to configuring Google Analytics 4.

As of May 2023 Google Analytics 4 is supported in most edx-platform LMS templates and the following
micro-frontends (MFEs) in the upcoming Olive.4 and Palm named releases:

* Learning
* Profile
* Authentication
* Account
* Discussions

.. _Google help posting: https://support.google.com/analytics/answer/11583528?hl=en
.. _another help posting: https://support.google.com/analytics/answer/10759417


Adding Google Analytics 4
*************************

#. Create a Google Analytics 4 property:

   * Go to the Google Analytics website and create a new account if you don't have one already.
   * Create a new property by selecting "Create Property" and following the instructions.


#. Creating the 'MEASUREMENT ID':

   * In the Admin section of your Google Analytics 4 property, select "Data Streams" and create a new stream.
   * Choose "Web" as the stream type and provide your website URL.
   * Copy the 'MEASUREMENT ID'.

   .. image:: /_images/site_ops_how_tos/ga4_web_stream_details.png
      :alt: A screenshot of the Google Analytics interface showing the location of the MEASUREMENT ID.


#. Add 'MEASUREMENT ID' to your Open edX installation:

   Enabling or disabling Google Analytics 4 in the platform and all supported MFEs is done by the presence
   of the measumerment id in edx-platform configuration. Simply adding the id to your site will turn the
   feature on. This can be accomplished by either adding it directly into the your settings file:

   .. code::

       GOOGLE_ANALYTICS_4_ID = "G-123AV45",
       MFE_CONFIG = {
           "GOOGLE_ANALYTICS_4_ID": "G-123AV45"
       }

   Or via the admin interface via site configuration (ex: http://localhost:18000/admin/site_configuration ),
   making sure that the configuration is marked ``enabled``.

   .. code::

        {
            "GOOGLE_ANALYTICS_4_ID": "G-ZMXV6TSV3M",
            "MFE_CONFIG": {
                "GOOGLE_ANALYTICS_4_ID": "G-ZMXV6TSV3M"
            }
        }

   .. image:: /_images/site_ops_how_tos/ga4_site_configuration.png
      :alt: A screenshot of the LMS Django Admin interface showing where to place the configuration snippet.


Confirming the Configuration
****************************

After the above steps are complete, the Google Analytics javascript and tracking code should be added to
edx-platform templated pages and MFEs where it is configured:

edx-platform templates
----------------------

.. image:: /_images/site_ops_how_tos/ga4_edx_platform_snippet_1.png
  :alt: A screenshot of the course dashboard.

.. image:: /_images/site_ops_how_tos/ga4_edx_platform_snippet_2.png
  :alt: A screenshot of the course dashboard source code showing where to locate the GA4 snippet.

MFE pages
---------

.. image:: /_images/site_ops_how_tos/ga4_mfe_snippet_1.png
  :alt: A screenshot of the Learning MFE.

.. image:: /_images/site_ops_how_tos/ga4_mfe_snippet_2.png
  :alt: A screenshot of the source code showing where to locate the GA4 snippet.
