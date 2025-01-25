.. Section is shared in CA and OLX guides
.. _Guidelines for Modifying Group Configurations:


Guidelines for Modifying Group Configurations
#############################################

.. tags:: educator, concept

Review these guidelines if you must modify a group configuration after a course starts. These guidelines apply for courses built in Studio or using OLX (Open Learning XML).

Modifying a Group Configuration
*******************************

After the course starts, **do not**:

* Delete group configurations.

* Change the ``id`` value of a group configuration.


Modifying Experiment Groups
***************************

After the course starts, **do not** change the ``id`` value of an experiment group.

You can change experiment group names at any time.

Removing Experiment Groups from Group Configurations
****************************************************

After a course in which you are running a content experiment has started, learners in a specific experiment group might have difficulties with the content or the course experience. In this situation, you can remove the experiment group from the group configuration. The content specified for that experiment group is no longer visible to learners.

Learners in the removed experiment group are reassigned evenly to one of the other groups in the group configuration. Any problems that these learners completed in the removed experiment group content do not count toward their grades. The learners must begin the problem set again and complete all the problems in the experiment group content to which they are reassigned.

Removing an experiment group affects event data for the course. Ensure that researchers evaluating your course results are aware of the experiment group you removed and the date on which you removed it. 


.. seealso::
 

 :ref:`Offering Differentiated Content` (concept)

 :ref:`Overview of Content Experiments` (concept)

 :ref:`Configure Your Course for Content Experiments` (how-to)

 :ref:`Experiment Group Configurations` (reference)

 :ref:`Add a Content Experiment in OLX` (how-to)

 :ref:`Set Up Group Configuration for OLX Courses` (how-to)