How to Enable a Waffle Flag for a User
#######################################

Follow these steps to enable a waffle flag for a single user. This may be useful in certain situations, such as internal testing or limited releases:

#. Get the LMS User ID, via a database query or other methods if you have them.
#. Login to the appropriate Django Admin Portal.
#. Navigate to ``DJANGO-WAFFLE > Flags``.
#. Find and select the appropriate flag using the `Open edX Feature Toggles Guide <https://docs.openedx.org/projects/edx-platform/en/latest/references/featuretoggles.html.>`_
#. Set the ``Everyone`` dropdown to ``Unknown``. This will cause the criterion specified on the page to be evaluated. Setting ``Everyone`` to ``True`` or ``False`` applies the flag globally.
#. Add the LMS User ID from Step 1 to the ``Users`` textbox at the bottom of the page. To add multiple users, values should be comma-separated with no spaces.
#. Click the appropriate ``Save`` button.
#. Refresh the page and see that the entered LMS User ID(s) now correspond to their LMS Usernames.
