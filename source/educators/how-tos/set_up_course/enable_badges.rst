.. _Enable Badges in Course:

****************************************
Enable or Disable Badges for Your Course
****************************************

.. tags:: educator, how-to

Badges provide a way for learners to share their course achievements. For
courses that have course completion badges enabled, learners receive a badge
at the same time as they receive a course certificate, and have the option of
sharing their badges to a badging site such as Mozilla Backpack.

The Open edX platform supports Open Badges, an open standard developed by the
Mozilla Foundation. For more information about Open Badges, see the `Open
Badges web site <http://openbadges.org/>`_.

If badging is enabled for your platform, course completion badges are enabled
by default for your course. If you are unsure whether badging is enabled for
your platform, or if you need help with configuring your course badges,
contact your platform administrator.

To stop issuing badges in your course, follow these steps.

#. In Studio, from the **Settings** menu, select **Advanced Settings**.

#. Locate the **Issue Open Badges** policy key. The default value is ``True``.

#. Change the setting to ``False`` and save your changes.

To enable badging for your course if it was previously disabled, change the
value of the key to ``True``.