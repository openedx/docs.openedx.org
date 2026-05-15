.. _Configuring an Open edX Instance as an LTI Tool Provider:

###########################################################
Configuring your Open edX instance as an LTI Tool Provider
###########################################################

.. tags:: site operator, concept

You can configure your Open edX instance to act as a Learning Tools
Interoperability (LTI) 1.1 tool provider, serving course content inside external learning management
systems such as Canvas or Blackboard.

Setting this up involves two tasks:

#. :ref:`Enable the LTI provider feature<Enable LTI Provider Functionality>`
   on your Open edX instance.
#. :ref:`Create LTI consumer credentials<Configuring Credentials for a Tool Consumer>`
   for each external LMS that will consume your content.

Once configured, course teams can construct LTI URLs for specific pieces
of content and add them to the external LMS. See
:ref:`Using your Open edX instance as an LTI Tool Provider` for the educator-facing steps.

.. seealso::

   :ref:`Using your Open edX instance as an LTI Tool Provider` (concept)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-05-06   | Aamir Ayub                    | Verawood       |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-06-04   | MITx                          | Teak           |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+

.. include:: /links.txt
