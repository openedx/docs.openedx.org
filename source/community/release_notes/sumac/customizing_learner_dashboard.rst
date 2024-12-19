Customizing Learner Dashboard Using Frontend "Slots"
####################################################

Utilizing *frontend plugin slots*, site operators now have the ability to
customize various portions of the Learner Dashboard.

A “frontend plugin slot” refers to an area of a web page - comprising one or
more visual elements - that can be “swapped out” with other visual elements. For
example, one new plugin slot allows you to “swap out” the Upgrade button on the
Learner Dashboard course card with another button (or more than one, or remove
it entirely).

Overhead and hassle is minimized using the plugin slot system. Site operators
can leverage a plugin slot using a configuration file; the codebase does not
need to be copied (“forked”) nor are extensive changes needed. A snippet of code
is all that is needed to use a plugin slot. A site operator places that code
within a configuration file. Site operators should refer to the src/plugin-slots
directory within each MFE's codebase to view documentation for that MFE's plugin
slot(s).

.. contents::
  :local:
  :depth: 1

Course Card Action Slot
***********************

Capabilities
============

The “course card” is what represents a course on the learner dashboard - it
contains the course thumbnail, name, passing requirements, and other
information. In Redwood, it also contains an “Upgrade” button:

   .. image:: /_images/release_notes/sumac/sumac-ccaslot-current.png

In Sumac, this Upgrade button (or more generally, the “Action” button) is now a
plugin slot! This means that the button can easily be removed, changed, or even
added to. This example below shows how an instance might remove the Upgrade
button and instead add two custom action buttons:

   .. image:: /_images/release_notes/sumac/sumac-ccaslot-custom.png
 

Leveraging This Slot
====================

A commonly requested feature is to remove the Upgrade button. This slot can be
leveraged to achieve that styling.

This slot can be utilized via code-based configuration. Site operators should
consult the `Learner Dashboard plugin slot documentation`_ for examples of how to
use this slot.

Course List Slot
****************

Capabilities
============

The Course List appears on the learner dashboard; in Redwood, it consists of
horizontal course cards that represent the courses the learner is enrolled in.
The CourseListSlot appears for a given learner only when they are enrolled in at
least one course.

   .. image:: /_images/release_notes/sumac/sumac-course-list-slot-current.png

Sumac provides the option to entirely replace the list of course cards. This
involves writing code that provides for another way of displaying the entire
list of course cards, and using that code within this slot. For example, one
could create a CustomCourseList *component* that converts the horizontal course
cards into vertical cards:

   .. image:: /_images/release_notes/sumac/sumac-course-list-slot-custom.png

Leveraging This Slot
====================

This slot, which appears on the learner dashboard for learners enrolled in one
or more courses, allows instances to play around with the visual representation
of course cards. One use case would be to sort the CourseCards of completed
courses either to the bottom or hiding them in some way, without the user
needing to do so themselves. Another use case could be to embed a “call to
action” message in the top of the CourseList; since that's put at the top of
that CourseList and will be visible to the learner as soon as they enter their
dashboard, this could be an effective way to call attention to a message,
product, or service.

This slot can be utilized via code-based configuration. Site operators should
consult the `Learner Dashboard plugin slot documentation`_ for examples of how to
use this slot.

No Courses View Slot
********************

Capabilities
============

On the Learner Dashboard, when a learner is enrolled in zero courses, a special
message is displayed. Now, this special message lives within a slot that can be
customized. In Redwood, the message looks like this:

   .. image:: /_images/release_notes/sumac/sumac-nocourseslot-current.png

In Sumac, this message can be customized with any text, graphics, buttons, and
links that meets the needs of your instance:

   .. image:: /_images/release_notes/sumac/sumac-nocourseslot-custom.png

Leveraging This Slot
====================

Instances might use this slot to give a custom call to action for learners who
haven't enrolled in a course yet. For example, instance-specific
graphics/iconography and text (for example, a message from a site founder or
prominent course staff member, or learner testimonial) may provide a personal
touch for learners who, after making their account, land on the Learner
Dashboard unenrolled in any course.

This slot can be utilized via code-based configuration. Site operators should
consult the `Learner Dashboard plugin slot documentation`_ for examples of how to
use this slot.

Widget Sidebar Slot
*******************

Capabilities
============

On the right-hand sidebar of the Learner Dashboard there is a message in a
“card”. This card has now been wrapped in a slot. In Redwood, this sidebar
consists of the “Looking for a new challenge?” card which directs learners to
the course catalog:

   .. image:: /_images/release_notes/sumac/sumac-sidebar-widget-current.png

Now, in Sumac, the widget sidebar can be updated with zero or more custom cards,
each with its own images, text, and/or links:

   .. image:: /_images/release_notes/sumac/sumac-sidebar-widget-custom.png
 

Leveraging This Slot
====================

Customizing the cards in the right-hand sidebar of the Learner Dashboard gives
flexibility for instances to provide encouraging messages or calls to action.
For example, one could imagine a sidebar consisting of multiple cards, each with
a testimonial, a link to a resource, and/or a call to action specific to the
needs of the instance and its learners.

This slot can be utilized via code-based configuration. Site operators should
consult the `Learner Dashboard plugin slot documentation`_ for examples of how to
use this slot.

.. seealso::

   * :ref:`/site_ops/how-tos/use-frontend-plugin-slots`

   * :ref:`/site_ops/references/frontend-plugin-slots`

.. _Learner Dashboard plugin slot documentation: https://github.com/openedx/frontend-app-learner-dashboard/tree/master/src/plugin-slots