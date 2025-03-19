.. _Zooming Image:

Zooming Image (Dual Image) Tool
###############################

.. tags:: educator, how-to

This tool allows the instructor to overlay a subsection of one image over a
second image. These two files can be any two image files.

In the particular use case shown, the team presented two views of a biochemical
pathway. One shows the names of molecules, and the second shows their chemical
structure when the learner clicks on that original image. That is why the
feature originally had the name “Zooming Image Tool”.  You could imagine other
use cases such as a map of a region and a second image that shows data or names
from each subsection from the first map.


.. image:: /_images/educator_how_tos/Zooming_Image.png
  :alt: Example zooming image (dual image) tool showing a chemistry exercise.

Components of a Zooming Image (Dual Image) Tool
***********************************************

To create a zooming image (dual image) tool, you need the following files.

* The primary image that you want learners to see when they access the unit.

* Secondly, an image that appears in the selected area when a learner
  selects a point in the primary image.


Create a Zooming Image (Dual Image) Tool
****************************************

#. In Studio, select **Content** and then select **Files & Uploads** to upload
   your regular-sized image file and, optionally, your large image file. For
   more information about uploading files for your course, see :ref:`Add Course
   Files`.

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
 

 :ref:`Add Course Files` (how-to)

 :ref:`About Image Mapped Input Problem` (concept)




**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-03-19   | Docs WG                       | Sumac          | Pass. Propose changing name to |
|              |                               |                | "Dual Image Tool" to better    |
|              |                               |                | reflect its actual capabilities|
+--------------+-------------------------------+----------------+--------------------------------+
