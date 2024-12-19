.. _Add Unsupported Exercises Problems:

Adding Unsupported Problem Types and Exercises
###############################################

.. tags:: educator, how-to

 .. .. note: These instructions are applicable only if your Open edX site has configured...insert name of the config setting. 

In general, you should use only problem types and exercises that are either
fully or provisionally supported. By default, only supported problem
types and exercises are available in Studio for adding to courses.

However, in some situations, you might choose to use exercises and problem types
that the Open edX Platform does not support.

To add unsupported problem types, exercises, and tools to your course, follow
these steps.

#. In Studio, select **Settings**, then **Advanced Settings**.

#. Locate the **Add Unsupported Problems and Tools** field, and enter a value
   of ``true``.

#. Select **Save Changes**.

After you enable this setting, unsupported problem types, exercises, and tools
are available in the lists of new components that you can add to your course
in Studio.


.. seealso::
 :class: dropdown

 :ref:`Create Exercises` (concept)

 :ref:`Enable Additional Exercises and Tools` (how to)

 :ref:`Core Problem Types` (reference)