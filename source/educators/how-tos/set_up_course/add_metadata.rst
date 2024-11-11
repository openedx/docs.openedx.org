.. _Add Course Metadata:

*******************
Add Course Metadata
*******************

   .. tags:: educator, how-to

  To make certain information about your course available to entities such as
  customer relationship management (CRM) software, a marketing site, or other
  external systems, follow these steps.

  #. Create a JSON dictionary that contains the metadata that you want to add.
  #. In Studio, open your course, and then select **Advanced Settings** on the
     **Settings** menu.
  #. In the **Other Course Settings** field, paste your JSON dictionary.

  In case you can't find the **Other Course Settings** field in
  the **Advanced Settings**, set ``ENABLE_OTHER_COURSE_SETTINGS`` to ``true``
  under ``FEATURES`` in ``/edx/etc/studio.yml`` and restart Studio...