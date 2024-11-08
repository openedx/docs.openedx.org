.. :diataxis-type: concept

.. _drag_and_drop_problem:

#####################
Drag and Drop Problem
#####################

In drag and drop problems, learners respond to a question by dragging text or
images to a specific location on a background image. This section explains how
to use drag and drop problems in your course.

.. contents::
  :local:
  :depth: 1

.. note::
    This drag and drop problem type is intended as a replacement for an older
    drag and drop problem type. This drag and drop problem type includes
    significant improvements and you should use it for any new course
    development. For more information about the previous, deprecated drag and
    drop problem type, see :ref:`Drag and Drop`.

.. _overview_of_drag_and_drop_problems:

**********************************
Overview of Drag and Drop Problems
**********************************

A drag and drop problem includes a background image and one or more items that
learners can drag into target zones on the background image. You can include as
many draggable items and as many target zones as you need. You can include
decoy items that do not have a target, and you can include decoy targets that
do not correspond to draggable items.

When learners view a drag and drop problem in the LMS, the problem includes a
top section and a bottom section. Learners drag items from the top section on
to the background image in the section below it.

The way that a learner selects, or grabs, an item depends on the type of
browser that the learner uses. For example, a learner might click and hold on
a draggable item with a mouse pointer to select it, drag the item to a target,
and release the mouse pointer to drop the item on the target. A learner who
accesses the problem on a mobile device with a touch screen might swipe an item
from the top section into a target zone. A learner who uses a keyboard
interface might use the navigation keys to select an item and then match it to
a target zone.

You can configure a drag and drop problem to give learners unlimited attempts
to match items to target zones or you can configure it to behave restrictively,
like a test.

* In standard mode, the problem gives learners unlimited attempts to match
  items and it provides immediate feedback to indicate whether an item is
  matched correctly.

* In assessment mode, learners must match all of the draggable items to target
  zones and then submit the problem. The problem does not reveal
  whether items are matched correctly until the learner submits the problem.

For more information about assessment mode and standard mode, see
:ref:`choosing_a_dnd_mode`.

The following image shows an example drag and drop problem.

.. image:: /_images/educator_concepts/dnd-initial.png
  :width: 600
  :alt: An example of a simple drag and drop problem. The components of the
      problem, such as its title, text, and introductory feedback are labeled.

The following image shows the success feedback message that learners see when
they match a draggable item with its target zone. Each draggable item has its
own success feedback message.

.. image:: /_images/educator_concepts/dnd-correct-feedback.png
  :width: 400
  :alt: An example of a simple drag and drop problem. The success feedback
      message appears above the background image.

The following image shows the error feedback message that learners see when
they match a draggable item with an incorrect target zone. Each draggable item
has its own error feedback message.

.. image:: /_images/educator_concepts/dnd-incorrect-feedback.png
  :width: 400
  :alt: An example of a simple drag and drop problem. The error feedback
      message appears over the background image.

The following image shows a completed drag and drop problem. The final feedback
message informs the learner that the problem is complete.

.. image:: /_images/educator_concepts/dnd-complete.png
  :width: 400
  :alt: An example of a simple drag and drop problem. The problem is complete
      and the final feedback message appears below the background image.


.. seealso::
 :class: dropdown

 :ref:`Creating a Drag and Drop Problem` (how to)

 :ref:`Drag and Drop` (reference)
