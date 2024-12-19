Use A Frontend Plugin Framework Slot
####################################

Utilizing *frontend plugin framework slots*, site operators now have the ability
to customize various portions of Open edX MFEs. A “frontend plugin framework
slot” refers to an area of a web page - comprising one or more visual elements -
that can be “swapped out” with other visual elements using custom code defined
in an `env.config.jsx` file. Note: In some cases a slot may default to being
empty, existing solely to be a placeholder for optional elements.

The basic procedure for replacing a slot is as follows:

#. Find the slot(s) you wish to customize by visiting the relevant
   `/src/plugin-slots` page of the MFE you wish to customize (for example, see
   the `Learner Dashboard MFE slots documentation
   <https://github.com/openedx/frontend-app-learner-dashboard/tree/master/src/plugin-slots>`_)

#. Create or modify the `env.config.jsx` file as demonstrated in the documentation.

#. (How to test changes)

#. Rebuild the MFE (link to instructions - where?) to see your changes live on your site

Note that up to three actions may be available for a slot: “modify" (changing
the links in the existing component), "replace" (fully removing the existing
component and putting a custom one in instead), and  "add" (putting custom
components before/after the existing component). See `the MobileUserMenuSlot
<https://github.com/openedx/frontend-component-header/tree/master/src/plugin-slots/MobileUserMenuSlot>`_
for an example.

More on Frontend Plugin Slots
*****************************

See the `Frontend Plugin Slots section of the tutor-mfe README
<https://github.com/overhangio/tutor-mfe/?tab=readme-ov-file#using-frontend-plugin-slots>`_
for more about Frontend Plugin Slots and their usage.


.. seealso::

   See :ref:`../references/frontend-plugin-slots` for a list of available slots.