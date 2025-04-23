Use A Frontend Plugin Framework Slot
####################################

.. tags:: site operator, how-to

Utilizing *frontend plugin framework slots*, site operators now have the ability
to customize various portions of Open edX MFEs. A “frontend plugin framework
slot” refers to an area of a web page - comprising one or more visual elements -
that can be “swapped out” with other visual elements using custom code defined
in an `env.config.jsx` file. Note: In some cases a slot may default to being
empty, existing solely to be a placeholder for optional elements.

The basic procedure for replacing a slot in a production Tutor deployment is as follows:

#. Find the slot(s) you wish to customize by visiting the relevant
   `/src/plugin-slots` page of the MFE you wish to customize (for example, see
   the `Learner Dashboard MFE slots documentation
   <https://github.com/openedx/frontend-app-learner-dashboard/tree/master/src/plugin-slots>`_)

#. Follow the `Tutor MFE instructions <https://github.com/overhangio/tutor-mfe/tree/v19.0.0?tab=readme-ov-file#using-frontend-plugin-slots>`_ to `create a Tutor plugin <https://docs.tutor.edly.io/tutorials/plugin.html>`_ that configures `env.config.jsx` to use the slot you selected above.

#. After enabling your Tutor plugin, rebuild the MFE image via the `tutor images build mfe` command.  Then restart the MFE container with `tutor local stop mfe && tutor local start -d mfe`. 

#. After restarting, navigate to the page where the plugin slot is exposed, where you should be able to see the custom content your plugin provides.

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

   See :doc:`../references/frontend-plugin-slots` for a list of available slots.

   :doc:`/community/release_notes/sumac/customizing_header`

   :doc:`/community/release_notes/sumac/customizing_learner_dashboard`

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
