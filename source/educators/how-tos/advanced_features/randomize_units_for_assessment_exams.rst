.. _Randomize Units for Assessment (Exams):

Randomize Units for Assessment (Exams) or Variable Content Sharing
##################################################################

Common Instructor Use Cases
***************************

Often instructors want to randomize assessments in an online setting to deter
dishonest sharing or comparing of answers in a summative assessment. There is
also an interest in randomizing content or assessment units that keep multiple
problem or HTML components linked together when they share a logical flow,
concept, or narrative. The content experiment setup solves both of these
requests. 

In this example use case, different learners encounter different versions of the
same unit allowing multiple problem components or HTML components to stay
together after randomization via the content experiment or split test. Each
learner encounters a different version of each unit of the exam allowing
exponentially different versions of the same exam. For example, in one extensive
use case, a 25-unit exam using 4 different content experiment groups per unit
has :math:`4^{25}` different versions if you treat each unit as an independent
randomization from the previous unit. This scenario would have 25 content
experiments under the settings menu → group configurations in Studio. See
:ref:`Manage Content Experiments` (how-to). This allows for all learners to
receive similar summative assessments testing the same learning objectives but
not having the same exam questions and answers as any other learner.

Design Strategies to Randomize Units for Assessment (Exams)
***********************************************************

Keep the overall structure and number of problems nearly identical per content
group in one unit. Manipulate easy-to-change variables like a number in a
calculation. For example, in biology, these variables include DNA sequence,
amino acids, tables of data, etc. The following screenshots include group A, B,
and C versions of the first two related genetics questions for one unit of an
exam.

Group A:

.. image:: /_images/educator_how_tos/randomize_units_group_a.png
  :width: 600 px
  :align: center
  :alt: Two biology questions, one about F2 Progeny with a data set of four crossing options, three are filled in and one is a dropdown option. The second about crossing pairs dominance, four dropdown options related to recessive traits.

Group B:

.. image:: /_images/educator_how_tos/randomize_units_group_b.png
  :width: 600 px
  :align: center
  :alt: The same two biology questions, although in this iteration the F2 Progeny question uses a different data set. The second question is the same as Group A.

Group C:

.. image:: /_images/educator_how_tos/randomize_units_group_c.png
  :width: 600 px
  :align: center
  :alt: The same two biology questions, although in this iteration the F2 Progeny question uses a third data set. The second question asks about dominant, rather than recessive, traits.


This randomization strategy in combination with using the the Open edX features
of not showing problem correctness and timed exam has an evidence-based
reduction in cheating signals in an open online course setting. See `"The
effects of assessment design on academic dishonesty, learner engagement, and
certification rates in MOOCs"
<https://onlinelibrary.wiley.com/doi/full/10.1111/jcal.12733>`_.

.. seealso::
   
   :ref:`About Content Experiments` (concept)

   :ref:`About Group Configurations` (concept)

   :ref:`Guidelines for Modifying Group Configurations` (reference)

   :ref:`Manage Content Experiments` (how-to)

   :ref:`Add a Content Experiment in OLX` (how-to)

   :ref:`Set Up Group Configuration for OLX Courses` (how-to)

   :ref:`Test Content Experiments` (how-to)

   :ref:`Experiment Group Configurations` (reference)


+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-03-19   | Docs WG                       | Sumac          |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+