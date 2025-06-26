.. _Enable the Google Drive Files Tool:

Enable the Google Drive Files Tool
##############################################

.. tags:: educator, how-to

Before you can add Google Drive files to your course, you must enable the
Google Drive tool in Studio or OLX (open learning XML).

Enable the Google Drive Files Tool in Studio
*************************************************
.. note::

    This tool is enabled by default in Teak. For earlier releases, follow the steps below to enable it manually.

To enable the Google Drive tool in Studio, you add the ``"google-document"``
key to the **Advanced Module List** on the **Advanced Settings** page. For
more information, see :ref:`Enable Additional Exercises and Tools`.

Alternatively, you can use OLX to enable the Google Drive tool.

.. _Enable Google Drive Files in OLX:

Enable Google Drive Files in OLX
********************************

To enable Google Drive files in your course, you edit the XML file that
defines the course structure. You locate the ``course`` element's
``advanced-modules`` attribute, and add the string ``google-document``
to it.

For example, the following XML code enables Google Drive files in a course. It
also enables Google calendars.

.. code-block:: xml

  <course advanced_modules="[&quot;google-document&quot;,
      &quot;google-calendar&quot;]" display_name="Sample Course"
      start="2014-01-01T00:00:00Z">
      ...
  </course>


.. seealso::
 

 :ref:`Google Drive Files Tool` (concept)

 :ref:`Add a Google Drive File to Your Course` (how to)



**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
