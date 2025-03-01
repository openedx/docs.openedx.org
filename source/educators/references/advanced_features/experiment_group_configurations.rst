.. _Experiment Group Configurations:

Experiment Group Configurations
###############################

.. tags:: educator, reference

Your Open edX instance assigns learners to each experiment groups within a group
configuration.

Experiment group assignments have the following characteristics.

* Dynamic

  Your instance assigns a learner to an experiment group the first time they
  view a content experiment that uses the group configuration.

* Random

  You cannot control which learners are assigned to which experiment group.

* Evenly distributed

  Your instance keeps track of the size of experiment groups, and assigns
  new learners to groups evenly. For example, if you have two experiment groups
  in a configuration, each group includes 50% of the learners in the course; if
  you have four experiment groups, each group includes 25% of the learners.

* Permanent

  Learners remain in their assigned experiment groups regardless of how many
  content experiments you set up that use the same group configuration.

.. seealso::

 :ref:`About Content Experiments` (concept)

 :ref:`Guidelines for Modifying Group Configurations` (reference)

 :ref:`Manage Content Experiments` (how-to)

 :ref:`Add a Content Experiment in OLX` (how-to)

 :ref:`Test Content Experiments` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
