.. _Add Custom CSS or JavaScript Code to a Course:

Add Custom CSS or JavaScript Code to a Course
#############################################

.. tags:: educator, how-to

#. In Studio, from the **Settings** menu, select **Advanced Settings**.

#. Locate the policy keys for **Course-wide custom css** and **Course-wide custom js**.
   The default values will be an empty list ``[]``.

#. You can add URLs to any CSS or JavaScript files in their respective fields. You can use
   absolute or relative URLs, as you can see in the following example:

   .. code:: json

      [
         "https://some.cdn.com/library.js",
         "/asset-v1:OpenedX+DemoX+DemoCourse+type@asset+block@some-script.js"
      ]

#. You can upload scripts and CSS files to a course though the **Files** page accessible
   under the **Content** menu in Studio.

.. note::

   Custom CSS or JavaScript added to a course in this manner will only be
   available in the course content and will not apply to the rest of the
   site's UI.

.. seealso::

   :ref:`Add Course Files` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
