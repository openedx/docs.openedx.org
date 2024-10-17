.. :diataxis-type: reference
.. _Image Mapped Input Problem XML:

******************************
Image Mapped Input Problem XML
******************************

==========
Template
==========

.. code-block:: xml

  <problem>

    <p>Problem text</p>

        <imageresponse>

         <imageinput src="IMAGE FILE PATH" width="NUMBER" height="NUMBER"
         rectangle="(X-AXIS,Y-AXIS)-(X-AXIS,Y-AXIS)" alt="DESCRIPTION OF
         IMAGE" />

        </imageresponse>

  </problem>

=====
Tags
=====

* ``<imageresponse>``: Indicates that the problem is an image mapped input
  problem.
* ``<imageinput>``: Specifies the image file and the region in the file that
  the learner must click.

**Tag:** ``<imageresponse>``

Indicates that the problem is an image mapped input problem.

  **Attributes**

  (none)

  **Children**

  * ``<imageinput>``

**Tag:** ``<imageinput>``

Specifies the image file and the region in the file where learners must click.

  **Attributes**

   .. list-table::
      :widths: 20 80

      * - Attribute
        - Description
      * - ``src`` (required)
        - The URL of the image
      * - ``height`` (required)
        - The height of the image, in pixels
      * - ``width`` (required)
        - The width of the image, in pixels
      * - ``rectangle`` (required) (or, for irregular regions, ``region``)
        - An attribute with two or more coordinate pairs that define the region
          where learners should click
      * - ``alt`` (required)
        - A description of the image, used for accessibility

  **Children**

  (none)

.. seealso::
 :class: dropdown

  :ref:`Create Image Mapped Input Problem` (how to)
  :ref:`Image Mapped Input` (reference)