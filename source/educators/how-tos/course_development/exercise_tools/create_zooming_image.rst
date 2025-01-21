.. _Zooming Image:

##################
Zooming Image Tool
##################

.. tags:: educator, how-to

If you present information to your learners using very large or very detailed
images, learners might not be able to clearly see all the information in the
image. Use the zooming image tool to provide learners with the ability to zoom
in to and enlarge selected areas of your image.


.. image:: /_images/educator_how_tos/Zooming_Image.png
  :alt: Example zooming image tool showing a chemistry exercise.

***********************************
Components of a Zooming Image Tool
***********************************

To create a zooming image tool, you need the following files.

* The image that you want learners to see when they access the unit.

* Optionally, an image that appears in the magnified area when a learner
  selects the regular image. This image should be larger than the regular
  image.


****************************
Create a Zooming Image Tool
****************************

#. In Studio, select **Content** and then select **Files & Uploads** to upload
   your regular-sized image file and, optionally, your large image file. For
   more information about uploading files for your course, see :ref:`Add Files
   to a Course`.

#. Add a zooming image tool to your course. In the course outline in Studio,
   select **Add New Component**, select **Text**, and then select **Zooming
   Image Tool**.

#. In the new component that appears, select **Edit**.

#. In the component editor, replace the default text with your own text.

#. Select **HTML** from the toolbar to edit the HTML source code.

#. Scroll down in the file.  Assuming your regular image was uploaded as
   ``/static/RegularImage.jpg`` and your optional magnified image as
   ``/static/MagnifiedImage.jpg``, replace the sample content (everything in
   ``<div class="zooming-image" />``) with the following, making sure not to
   remove the included ``<script />`` at the bottom::

      <div class="zooming-image">
        <a data-src="/static/MagnifiedImage.jpg">
          <img src="/static/RegularImage.jpg" />
        </a>
      </div>

   - (Optional) If you want the magnified area to be larger or smaller, change
     the ``width`` and ``height`` options of the loupe tool from the default of
     350 to larger or smaller numbers.  For example, you can change both
     numbers to 450. Or, if you want a horizontal oval instead of a circle, you
     can change the ``width`` value to a number such as 500 and the ``height``
     value to a number such as 150.  You should do this where the loupe tool is
     attached to your ``zooming-image`` div, at the very bottom of the script::

        $('.zooming-image').loupe({
            width: 500,
            height: 150,
        });


#. Select **Save**.

.. seealso::
 :class:dropdown

 :ref:`Add Files to a Course` (how-to)

 :ref:`Image Mapped Input` (reference)


