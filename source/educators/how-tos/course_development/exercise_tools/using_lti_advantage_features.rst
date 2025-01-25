.. _Enabling and using LTI Advantage features:

Enable and Use LTI Advantage Features
#####################################

.. tags:: educator, how-to

LTI Advantage is an extension of the LTI 1.3 specification that enables
additional features in LTI components. See `LTI Advantage`_ for more
information.

Currently, the platform supports the following LTI Advantage extensions:

* `Assignments and Grades services`_
* `Deep Linking`_
* `Names and Roles Provisioning Service`_

.. _Enabling LTI Assignments and Grades services:

Enabling LTI Assignments and Grades services
********************************************

The LTI Assignments and Grades service (LTI-AGS) allows LTI tools to send and
manage learner grades back to the platform after an activity is completed.

To set up LTI-AGS services on a component, follow these steps.

#. Locate the unit and LTI component in which you want to enable LTI-AGS
   functionality.

#. Select **Edit** in the component that appears.

#. Locate the **LTI Assignment and Grades Service** setting.

#. Select the operation mode of the Assignments and Grades services. You can
   disable the LTI-AGS service by selecting **Disabled** or pick one of the
   operation modes available: *declarative* to allow only one grade per
   problem, or *programmatic* to let the tool create many grades. For more
   information about each mode, read the corresponding entry on :ref:`LTI
   Component settings`.

#. Select **Save**.

.. _Enabling and using LTI Deep Linking:

Enabling and using LTI Deep Linking
***********************************

The Deep Linking service (LTI-DL) allows course creators to select and
configure the content displayed to learners through Open edX Studio, removing
the need to use custom parameters and settings when setting up content,
improving the ease of use and content authoring experience.

To set up LTI-DL services on a component, follow these steps.

#. Locate the unit and LTI component in which you want to enable LTI-DL
   functionality.

#. Select **Edit** in the component that appears.

#. Locate the **Deep linking** setting and set it to **True** (enabled).

#. Locate the **LTI Advantage Deep Linking Launch URL** setting.

#. Retrieve the Deep Linking Launch url from the tool you're integrating with.
   If it's not provided, try using the same value as in the **LTI 1.3 Tool
   Launch URL**.

#. Select **Save**. The Studio page will refresh and show the updated details
   page.

To use LTI Deep Linking, follow these steps:

#. Ensure that LTI-DL is enabled by following the steps above.

#. Locate the unit and LTI component in Studio.

#. In the LTI component page in Studio, locate the **Deep Linking Launch -
   Configure tool** link and select it.

#. You'll be redirected to the Tool and presented with a page to select the
   options.

#. Once the configuration is complete, you'll be redirected back to the Studio
   and the Deep Linking setup will be complete.

#. The content you selected in the tool will be presented to your students in
   the LMS.

.. note:: LTI 1.3 launches only work with published blocks, make sure the block
     is published before doing a Deep Link Launch.

.. _Enabling LTI Names and Roles Provisioning Service:

Enabling LTI Names and Roles Provisioning Service
*************************************************

The Names and Roles Provisioning service (LTI-NRPS) allows tools to list and
retrieve information about the learners that have access to an LTI component.
The tools that support this service can retrieve a limited amount of personal
information (full name, email, username) and the membership status of all the
learners enrolled in the course.

To set up LTI-NRPS services on a component, follow these steps.

#. Locate the unit and LTI component in which you want to enable LTI-NRPS
   functionality.

#. Select **Edit** in the component that appears.

#. Locate the **Enable LTI NRPS** setting and set it to **True** (enabled).

#. Select **Save**. The LTI-NRPS will be enabled for all subsequent launches.

.. note:: Due to performance concerns, LTI-NRPS information is by default only
          available on courses with up to 1000 users. Site operators may adjust
          this limit using the `LTI_NRPS_ACTIVE_ENROLLMENT_LIMIT setting`_.

.. seealso::
 

 :ref:`LTI Component` (reference)

 :ref:`LTI Component settings` (reference)

 :ref:`Enable_LTI_Components` (how-to)

 :ref:`Setting up a LTI 1.1 component` (how-to)

 :ref:`Setting up a LTI 1.3 component` (how-to)
