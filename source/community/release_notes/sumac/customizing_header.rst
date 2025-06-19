Customizing Site Header Using Frontend "Slots"
##############################################

Utilizing *frontend plugin slots*, site operators now have the ability to
customize various portions of the site header.

A “frontend plugin slot” refers to an area of a web page - comprising one or
more visual elements - that can be “swapped out” with other visual elements. For
example, one new plugin slot allows you to remove the "Help" button in the header.

Overhead and hassle is minimized using the plugin slot system. Site operators
can leverage a plugin slot using a configuration file; the codebase does not
need to be copied (“forked”) nor are extensive changes needed. A snippet of code
is all that is needed to use a plugin slot. A site operator places that code
within a configuration file. Site operators should refer to the ``src/plugin-slots``
directory within each MFE's codebase to view documentation for that MFE's plugin
slot(s).

In these release notes, we'll cover three example use cases for the header. Full
documentation is available `within the frontend-component-header codebase
<https://github.com/openedx/frontend-component-header/tree/master/src/plugin-slots>`_.

.. contents::
  :local:
  :depth: 1

.. simple-example-start

Simple example: Removing help button
************************************

In the default learner dashboard header, the content contains a "Help" button
to the left of the logged in user's username:

   .. image:: /_images/release_notes/sumac/sumac-header-easy-before.png

With frontend plugin slots, you can now hide the "Help" button:

   .. image:: /_images/release_notes/sumac/sumac-header-easy-after.png

.. simple-example-end

For site operators, see :ref:`simple_header_plugin_code` for this example.
    
.. medium-example-start

Medium-effort example: Replacing "Course Info" with a custom component
**********************************************************************

In the default learner dashboard header, the content contains information about
the current course's organization and title in the top left corner:

   .. image:: /_images/release_notes/sumac/sumac-header-medium-before.png

With frontend plugin slots, you can now create your own custom component (in
this case, an icon of a book) in place of the course info component:

   .. image:: /_images/release_notes/sumac/sumac-header-medium-after.png

.. medium-example-end

For site operators, see :ref:`medium_header_plugin_code` for this example.

.. advanced-example-start

Advanced example: Replacing the entire header
*********************************************

It is possible to replace the entire header using your own custom code. We
currently don't have an example of how to do that, but if you go this route on
your site, please feel free to make a pull request to add your example to this
release note!

.. advanced-example-end

.. seealso::

   * :doc:`/site_ops/how-tos/use-frontend-plugin-slots`

   * :doc:`customizing_learner_dashboard`

   * :doc:`/site_ops/references/frontend-plugin-slots`

**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-04-28    | BTR                           | Teak           | Deprecated: This is no longer the current release |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-04-15    |Frontend WG                    | Sumac          |  Pass                                             |
+--------------+-------------------------------+----------------+---------------------------------------------------+


