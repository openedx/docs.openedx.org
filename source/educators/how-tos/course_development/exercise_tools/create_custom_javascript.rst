.. :diataxis-type: how-to
.. _Create Custom Javascript: 

******************************************************
Create a Custom JavaScript Display and Grading Problem
******************************************************

#. Create your JavaScript application, and then upload all files associated
   with that application to the **Files & Uploads** page.
#. In the unit where you want to create the problem, under **Add New
   Component** select **Problem**.
#. In the problem editor, select **Advanced problem types**. Then select
   **Custom JavaScript Display and Grading**.
#. In the advanced problem editor, modify the example code according to your problem.
   Be sure to specify a ``title`` attribute on the ``jsinput`` tag. This title
   is used for the title attribute on the generated inline frame.
#. (Optional) To add a **Save** button to your problem, in the settings panels on
   the right side of the editor, set **Attempts** to a number larger than zero.
#. Select **Save**.


.. note::  All problems include more than one resource. If all the resources in
   a problem have the same protocol, host, and port, then the problem conforms
   to the same-origin policy (SOP). For example, the resources
   ``http://store.company.com:81/subdirectory_1/JSInputElement.html`` and
   ``http://store.company.com:81/subdirectory_2/JSInputElement.js`` have the
   same protocol (``http``), host (``store.company.com``), and port (``81``).

   If any resources in your problem use a different protocol, host, or port,
   you need to bypass the SOP. For example,
   ``https://info.company.com/JSInputElement2.html`` uses a different
   protocol, host, and port from
   ``http://store.company.com:81/subdirectory_1/JSInputElement.html``.

   To bypass the SOP, change ``sop="true"`` to ``sop="false"``. In the example
   problem code, this attribute is just before the closing ``customresponse``
   tag.

   If you bypass the same-origin policy, you require an additional file.
   The example problem uses the file ``jschannel.js`` to bypass the SOP.

   For more information, see the same-origin policy page on the `Mozilla
   Developer Network site <https://developer.mozilla.org/en-US/docs/Web/Security/>`_
   or on `Wikipedia <https://en.wikipedia.org/wiki/Same_origin_policy>`_.


.. seealso::
 :class: dropdown

  :ref:`Custom JavaScript` (reference)

