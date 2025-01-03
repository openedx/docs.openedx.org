.. _enable_lti_components:

Enabling LTI Components for a Course
####################################

.. tags:: educator, how-to

Before you can add LTI components to your course, you must enable the LTI tool
in Studio.

To enable the LTI tool in Studio, add ``"lti_consumer"`` to the
**Advanced Module List** on the **Advanced Settings** page. For more
information, see :ref:`Enable Additional Exercises and Tools`.

.. note::
  The ``lti_consumer`` module replaces a previous version of the LTI component.
  The name of the module for the previous LTI component is ``lti`` and it may
  appear in the **Advanced Module List** for older courses.

  The ``lti_consumer`` module includes all of the functionality of the previous
  LTI component and it should be used for all new courses. Courses that include
  the previous LTI component will continue to work correctly, even if the
  ``lti`` module is no longer present in the **Advanced Module List**.

.. seealso::
 :class: dropdown

 :ref:`LTI Component` (reference)

 :ref:`LTI Component settings` (reference)

 :ref:`Setting up a LTI 1.1 component` (how-to)

 :ref:`Setting up a LTI 1.3 component` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)
