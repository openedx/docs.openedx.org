.. _Documentation Maintenance Process:

Documentation Maintenance Process
############################################

.. tags:: documentor, reference

.. contents:: Contents
  :local:
  :depth: 2

Introduction
*************

This document aims to establish a maintenance process for the community to keep Open edX documents current and accurate.

Purpose
********

The purpose of this document is to provide a standardized process for contributors who maintain existing documentation. Maintenance involves reviewing and testing existing documents, fixing issues, or submitting reports when they are outdated or inaccurate.

This process ensures consistent standards among contributors and improves documentation quality assurance (QA).

Roles and Responsibilities
****************************

User: Even without the official role of contributor, any user of the Open edX documentation may text and report errors in the documentation.

Contributors: Review and test documents, update the Maintenance Chart and submit pull requests or issues for fixes. 

Working Groups: Collaborate on unresolved issues, oversee compliance with standards, and ensure documentation QA.

Maintenance Procedure
***********************

The maintenance process involves reviewing and, if applicable, following the steps in the document on a stable and current Open edX release and either:

A. Mark the document as "passing" - that is, everything is accurate.  
B. Mark the document as "failing" and submit an issue to fix an error.  
C. Fixing an error and changing the document's status from "fail" to "pass". 

During this process, the user or contributor should read the document carefully and pay attention to the following details:

- Images  
- Links  
- Diataxis type (how-to, quickstart, concept, reference)  
- Process  
- Correctness of information  
- Open edX version  

The user must also consider the standards previously defined in the :ref:`About Open edX Documentation Standards` and :doc:`doc_style_guide`.

Steps to follow to comply with the maintenance procedure
*********************************************************

1. Pick one document to be reviewed.  
2. Confirm that the document meets the standards in the :doc:`doc_checklist`: 

   a. Audience is defined  
   b. The Diataxis type is defined  
   c. RST standards are followed  
   d. Images are working and current  
   e. External links are working and accurate  
   f. ``See Also table`` is included  

3. While reading the document, consider the standards defined in the :doc:`doc_style_guide` (be focused on Grammar, details, etc).  
4. Based on the diataxis type, test or validate the document:  

   a. If the document is a **how-to** or **quickstart**, complete the steps as instructed and confirm that the outcome in your Open edX instance is the same as what the doc expects.  
   b. If the document is a **reference**, confirm that the reference is complete and matches what you observe in your current Open edX version.  
   c. If the document is a **concept**, confirm that the information is accurate and up-to-date.  

5. Complete the maintenance chart (following the instructions below).

Maintenance Chart
*******************

This chart will be included in every Open edX document so that each user can perform their test.  
It should be completed once the user completes the review process. All fields are required except for the name of the user.

+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
| Review Date  | Reviewer                      |   Release      |    Test situation                                                                                                  | 
+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
| 2025-06-01   | Documentation WG              | Sumac          |     Pass                                                                                                           |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
| 2025-12-01   | Ana Gomez                     | Verawood       |`Fail <https://github.com/openedx/docs.openedx.org/issues/776>`_                                                    |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
| 2025-12-15   | BTR WG                        | Verawood       | Pass                                                                                                               |
+--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+



To apply the maintenance chart on a new document, you can use any of the following codes:

Table
=======
.. code-block:: RST

  +--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
  | Review Date  | Reviewer                      |   Release      |    Test situation                                                                                                  | 
  +--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
  | 2025-06-01   | Documentation WG              | Sumac          |     Pass                                                                                                           |
  +--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
  | 2025-12-01   | Ana Gomez                     | Verawood       |`Fail <https://github.com/openedx/docs.openedx.org/issues/XXXX>`_ (replace XXXX with the issue number)              |
  +--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+
  | 2025-12-15   | BTR WG                        | Verawood       | Pass                                                                                                               |
  +--------------+-------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------+

List Table
===========
.. code-block:: RST

   .. list-table::
   :header-rows: 1
   * - Review Date
     - Working Group Reviewer
     - Release
     - Test Situation
   * - 2025-06-01
     - Documentation WG - Collaborator's name
     - Sumac
     - Pass
   * - 2025-12-01
     - Documentation WG
     - Verawood
     - `Fail <<https://github.com/openedx/docs.openedx.org/issues/XXXX>`_ (replace XXXX with the issue number)
   * - 2025-12-15
     - BTR WG
     - Verawood
     - Pass

Review Date
===========

The user should add the month and year of the review using the following format: YYYY-MM-DD.

Reviewer
======================

This field should contain the name of the reviewer who can be a contributor or a working group.

Release
========

This field indicates the Open edX version on which the test was performed.

Test Situation
===============

In this column, the user should state if the review process (test) is passed or failed, writing “Pass” or “Fail”.

If the test passes, the document does not need any change, which means that every link works, there is no need to add any new information, the diataxis criteria are good, etc. However, if the test fails, the contributor can take either of two actions:

1. :doc:`Submit a PR with a fix <../how-tos/update_a_doc_via_github>` and link to the PR in the Failure flag.  
   
2. Create a GitHub issue and link it to the issue in the Failure flag so someone else is aware of the error and can fix it.  
   :ref:`Check this how-to doc for creating GitHub issues <Report a problem with the docs>`.

.. seealso::

   :ref:`About Open edX Documentation Standards` (concept)

   :ref:`Documentor Guidelines` (reference)

   :ref:`Guidelines for Writing Global English` (reference)

   :ref:`Open edX Documentation Writing Style Guide` (reference)

   :ref:`Documentation Templates` (reference)
   
   :ref:`Writing RST` (reference)

   :ref:`Documentation Audiences` (concept)

   :ref:`Update An Existing Doc via GitHub` (how-to)

   :ref:`Add New Documentation via GitHub` (how-to)

   :ref:`Report a problem with the docs` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
