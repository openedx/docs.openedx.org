.. _Configure an LTI Discussion Provider:

####################################
Configure an LTI Discussion Provider
####################################

.. tags:: educator, how-to

You can use a third-party discussion tool as the **Discussion** page in a
course. Open edX supports these discussion providers through LTI 1.1:

* Ed Discussion
* InScribe
* Piazza
* Yellowdig

.. note::

   Only an Open edX global administrator can select, configure, or change a
   third-party discussion provider.

********************************
Configure a discussion provider
********************************

.. warning::

   A discussion provider might require the usernames or email addresses of
   learners and course staff. Review your organization's privacy and data
   policies before enabling PII sharing.

#. Enable LTI PII sharing for the course. See :ref:`Manage LTI PII Sharing for
   a Course`.

#. In the Studio header, select **Content**, then **Pages & Resources**.

#. On the **Discussion** card, select the settings icon.

   .. image:: /_images/educator_how_tos/Discussion_tile_in_pages_and_resources.png
      :width: 600
      :alt: The Discussion card on the Pages & Resources page.

#. Select the third-party discussion provider.

#. Select **Next**.

#. Enter the **Consumer Key**, **Consumer Secret**, and **Launch URL** supplied
   by the provider.

#. Select **Save**.

The **Discussion** page in the course navigation now shows the third-party tool
in place of the platform's built-in discussions.


**Maintenance chart**

+--------------+-------------------------------+----------------+----------------+
| Review Date  | Working Group Reviewer        | Release        | Test situation |
+--------------+-------------------------------+----------------+----------------+
| 2026-07-31   | Aamir Ayub                    | Verawood       | Pass           |
+--------------+-------------------------------+----------------+----------------+
