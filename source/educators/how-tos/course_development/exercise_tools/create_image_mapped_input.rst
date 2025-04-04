.. _Create Image Mapped Input Problem:

Create an Image Mapped Input Problem
####################################

.. tags:: educator, how-to

To create an image mapped input problem, follow these steps.

#. :ref:`Collect the information that you need for the image<Determine
   Coordinates>`.

#. :ref:`Create the problem in Studio<Create an IMI Problem in Studio>`.

.. _Determine Coordinates:

Collect Image Information
*************************

To create an image mapped input problem, you need the following elements.

   * The height and width of the image in pixels.
   * Coordinate pairs that define the region or regions where you want
     learners to click.

To collect the information you need about your image, use an image editing
tool such as Microsoft Paint.

.. note:: The coordinate pairs for all images start with (0,0) in the
 upper-left corner of the image and increase in value toward the lower-right
 corner, similar to the progression of reading English.

* To specify a rectangular region, you need two coordinate pairs: the
  upper-left corner and the lower-right corner.

* To specify more than one rectangle, you need the coordinate pairs for the
  upper-left and lower-right corners of each rectangle.

* To specify an irregular region, you need three or more coordinate pairs.
  Studio creates the simplest possible shape based on these coordinate
  pairs. You can enter the coordinate pairs in any order.

  For example, for a triangle, you need three coordinate pairs. For an
  octagon, you need eight coordinate pairs.

.. _Create an IMI Problem in Studio:

Create an Image Mapped Input Problem in Studio
**********************************************

#. In Studio, upload your image to the **Files & Uploads** page, and make a
   note of the file path for the image. For more information, see :ref:`Add
   Course Files`.
#. In the unit where you want to create the problem, click **Problem**
   under **Add New Component**.
#. In the problem editor, select **Advanced problem types**. Then select
   **Image Mapped Input**.
#. In the component editor, replace the example problem text with your own
   text.
#. In the ``<imageinput>`` element, follow these steps.

   #. Replace the example file path in the ``src`` attribute with the file
      path for your image.

   #. Include alt text for your image to make the image accessible. For more
      information about alt text, see :ref:`Best Practices for Describing
      Images`.

   #. Replace the example values for the ``width`` and ``height`` attributes
      with the dimensions for your image.

   #. Modify the example ``rectangle`` attribute to reflect the shape and size
      of the region that you want to specify. For more information, see
      :ref:`Specify a Rectangular Region`, :ref:`Specify Multiple Rectangular
      Regions`, or :ref:`Specify an Irregular Region`.

#. Click **Save**.

.. _Specify a Rectangular Region:

Specify a Rectangular Region
============================

To specify a rectangular region, edit the ``rectangle`` attribute in the
``<imageinput>`` element.

* Specify the coordinate pair for the upper-left and lower-right corners of
  the rectangle, separating the x and y values with a comma.
* Surround each coordinate pair with parentheses.
* Use a hyphen to separate the coordinate pairs.
* Surround the set of coordinate pairs with quotation marks (").


For example, the following ``rectangle`` attribute creates one rectangle from
two coordinate pairs:

``rectangle="(338,98)-(412,168)"``

**Problem Code**:

.. code-block:: xml

 <problem>

  <p>What country is home to the Pyramids as well as the cities of
  Cairo and Memphis? Click the country on the map below.</p>

  <imageresponse>
    <imageinput src="/static/Africa.png" width="600" height="638"
  rectangle="(338,98)-(412,168)" alt="Map of Africa" />
  </imageresponse>

  <solution>
    <div class="detailed-solution">

      <p>Explanation</p>

      <p>Egypt is home to not only the Pyramids, Cairo, and Memphis, but also the
  Sphinx and the ancient Royal Library of Alexandria.</p>

    </div>
  </solution>

 </problem>

.. _Specify Multiple Rectangular Regions:

Specify Multiple Rectangular Regions
====================================

You can specify more than one rectangular region in an image.

.. image:: /_images/educator_how_tos/ImgMapInput_Mult.png
 :width: 350
 :alt: Problem that asks learners to click inside one of three rectangles

To specify multiple rectangular regions, edit the ``rectangle`` attribute in
the ``<imageinput>`` element.

* Specify the coordinate pair for the upper-left and lower-right corners of
  each rectangle, separating the x and y values with a comma.
* Surround each coordinate pair with parentheses.
* Use a hyphen (-) to separate the coordinate pairs.
* Separate each rectangle with a semicolon (;).
* Surround the entire set of coordinates with quotation marks (").

For example, the following ``rectangle`` attribute creates three rectangles:

``rectangle="(62,94)-(262,137);(306,41)-(389,173);(89,211)-(187,410)"``

**Problem Code**:

.. code-block:: xml

 <problem>

  <p>In the following image, click inside any of the rectangles.</p>

    <imageresponse>

      <imageinput src="/static/imageresponse_multipleregions.png" width="450"
        height="450" rectangle="(62,94)-(262,137);(306,41)-(389,173);(89,211)-
        (187,410)" alt="Three rectangles on a white background" />

    </imageresponse>

 </problem>

.. _Specify an Irregular Region:

Specify an Irregular Region
===========================

You can specify one non-rectangular region.

.. image:: /_images/educator_how_tos/ImgMapInput_Irreg.png
  :width: 500
  :alt: Problem that asks learners to click inside a pentagon.

To specify an irregular region, edit the ``rectangle`` attribute in the
``<imageinput>`` element.

* Change ``rectangle`` to ``region``.
* Specify three or more coordinate points in any order.
* Enter each coordinate pair in brackets ([]). **Do not use parentheses**.
* Separate each set of points with a comma (,) and a space.
* Enclose the whole list of coordinate points in brackets ([]).
* Surround the outer brackets with quotation marks (").

For example, the following ``regions`` attribute creates a pentagon.

``regions="[[219,86], [305,192], [305,381], [139,381], [139,192]]"``

**Problem Code**:

.. code-block:: xml

 <problem>

  <p>In the following image, click inside the pentagon.</p>

  <imageresponse>

    <imageinput src="/static/imageresponse_irregularregions.jpg" width="600"
    height="204" regions="[[219,86], [305,192], [305,381], [139,381],
    [139,192]]" alt ="A series of 10 shapes including a circle, triangle,
    trapezoid, pentagon, star, and octagon" />

  </imageresponse>

 </problem>

.. seealso::
 

 :ref:`About Image Mapped Input Problem` (reference)

 :ref:`Image Mapped Input Problem XML` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
