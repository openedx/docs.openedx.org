.. _enable_lti_components:

Enable LTI Components for a Course
##################################

.. tags:: educator, how-to

Studio includes a default set of core problem types that can be added to
any course. You can expand the types of content you include by enabling
additional exercises and tools, such as the LTI tool, which allows integration
with external learning applications.

Enable the LTI Tool
====================

.. note::

    This tool is enabled by default in Teak. For earlier releases, follow the steps below to enable it manually.

#. In Studio, select **Settings**, and then **Advanced Settings**.
#. Locate the **Advanced Module List** field. This field lists any advanced exercises and tools added to your course.
#. Enter ``"lti_consumer"``, ensuring it is enclosed in double quotes. If adding multiple tools, separate them with commas.
#. Select **Save Changes**.


For more
information, see :ref:`Enable Additional Exercises and Tools`.

.. note::
  The ``lti_consumer`` module replaces a previous version of the LTI component.
  The name of the module for the previous LTI component is ``lti`` and it may
  appear in the **Advanced Module List** for older courses.

  The ``lti_consumer`` module includes all of the functionality of the previous
  LTI component and it should be used for all new courses. Courses that include
  the previous LTI component will continue to work correctly, even if the
  ``lti`` module is no longer present in the **Advanced Module List**.

  Additionally, ``lti_consumer`` supports `LTI 1.3`_ and `LTI Advantage`_,
  providing enhanced security and interoperability features for integrating
  external tools with Open edX.

.. seealso::
 
 :ref:`About the LTI Component` (concept)

 :ref:`LTI Component Settings` (reference)

 :ref:`Set up an LTI 1_1 component` (how-to)

 :ref:`Set up an LTI 1_3 component` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-03-19   |   Documentation WG            |     Sumac      |      Pass                      |
+--------------+-------------------------------+----------------+--------------------------------+
