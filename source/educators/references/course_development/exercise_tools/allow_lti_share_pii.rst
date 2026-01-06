.. _Allow sharing PII to LTI Components:

Allow sharing PII to LTI Components
###################################

.. tags:: site operator, how-to

The LTI component block has settings to share the user's email or username with the LTI application.
By default, these settings are disabled for privacy reasons.
The settings may be enabled per-course by an administrator, using the Django admin console:

#. With a system administrator account, navigate to the django admin console, and find the "Course allow pii sharing in lti flags" item.
   Click the text on the left for the item to navigate to the page with the list of these flags.
   From this page, you can add, modify, or delete flags.

   .. image:: /_images/site_ops_how_tos/lti_pii_sharing_admin_1.png
      :alt: A screenshot of the Django admin console showing the "Course allow pii sharing in lti flags" menu item.

#. Click the button to add a new flag:

   .. image:: /_images/site_ops_how_tos/lti_pii_sharing_admin_2.png
      :alt: A screenshot of the Django admin console showing the button to "add course allow pii sharing in lti flag".

#. In the new flag form, enter the ID for the course you wish to enable this for, and ensure the "Enabled" field is checked.

   .. image:: /_images/site_ops_how_tos/lti_pii_sharing_admin_3.png
      :alt: A screenshot of the Django admin console showing the form to add an enabled flag for a particular course id.

#. Finally, save the form.

.. seealso::

 :ref:`LTI Component settings` (reference)
