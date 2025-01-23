Documentation Maintenance Process
############################################

.. contents:: Contents
  :local:
  :depth: 2

Introduction
*************

This document aims to establish a maintenance process for the community to keep Open edX documents current and accurate.

Purpose
********

The purpose of this document is to provide a standardized process for contributors who maintain existing documentation. Maintenance involves reviewing and testing existing documents, fixing docs, or submitting issues when they are outdated or inaccurate.

This process will actively collaborate to have the same standards among users and improve documentation QA.

Maintenance Procedure
***********************

The maintenance process involves reviewing and, if applicable, following the steps in the document on a stable and current Open edX release and either:

A. Passing the document  
B. Fixing an error  
C. Submitting an issue for an error to be fixed  

During this process, the user should read the document carefully and pay attention to the following details:

- Images  
- Links  
- Diataxis type (how-to, quickstart, concept, reference)  
- Process  
- Information veracity  
- Open edX version  

The user must also consider the standards previously defined in the `Diataxis Guide <https://docs.openedx.org/en/latest/documentors/concepts/content_types.html>`_ and `Style Guide <https://docs.openedx.org/en/latest/documentors/references/doc_style_guide.html>`_.

Steps to follow to comply with the maintenance procedure
*********************************************************

1. Pick one document to be reviewed.  
2. Confirm that the document meets the standards in the `Documentation Checklist <https://docs.openedx.org/en/latest/documentors/references/doc_checklist.html>`_:  
   a. Audience is defined  
   b. The Diataxis type is defined  
   c. RST standards are followed  
   d. Images are working and current  
   e. External links are working and accurate  
   f. See Also table is included  
3. While reading the document take into account standards defined in the Style Guide (be focused on Grammar, details, etc).  
4. Based on the diataxis type, test or validate the document:  
   a. If the document is a **how-to** or **quickstart**, complete the steps as instructed and confirm that the outcome you get in your Open edX instance is the same as what is expected by the doc.  
   b. If the document is a **reference**, confirm that the reference is complete and matches what you observe in your current version of Open edX.  
   c. If the document is a **concept**, confirm that the information is accurate and up-to-date.  
5. Complete the maintenance chart (following the instructions below).

Maintenance Chart
*******************

This chart will be included in every Open edX document so that each user can perform their test.  
It should be completed once the user completes the review process. All fields are required except for the name of the user.

.. list-table::
   :header-rows: 1

   * - Review Date
     - Working Group Reviewer
     - Release
     - Test Situation
   * - 01/2024
     - Documentation WG - Ana Gomez
     - Sumac
     - Pass
   * - 06/2024
     - Documentation WG
     - Verawood
     - `Fail <https://github.com/openedx/docs.openedx.org/issues>`_
   * - 12/2024
     - BTR WG
     - Verawood
     - Pass

To apply the maintenance chart on a new document, you can use the following code:

.. code-block:: RST

   .. list-table::
   :header-rows: 1
   * - Review Date
     - Working Group Reviewer
     - Release
     - Test Situation
   * - 01/2024
     - Documentation WG - Collaborator's name
     - Sumac
     - Pass
   * - 06/2024
     - Documentation WG
     - Verawood
     - `Fail <https://github.com/openedx/docs.openedx.org/issues>`_
   * - 12/2024
     - BTR WG
     - Verawood
     - Pass

Review Date
===========

The user should add the month and year of the review using the following format: mm/yyyy.

Working Group Reviewer
======================

This field should contain the name of the Working Group to which the user belongs. It is not mandatory to include the name and surname of the user.

Release
========

This field indicates the version of Open edX on which the test was performed.

Test Situation
===============

In this column, the user should state if the review process (test) is passed or failed, writing “Pass” or “Fail”.

If the test passes, the document does not need any change, which means that every link works, there is no need to add any new information, the diataxis criteria are good, etc. However, if the test fails, the contributor can take either of two actions:

1. Submit a PR with a fix and link to the PR in the Failure flag.  
   `https://docs.openedx.org/en/latest/documentors/how-tos/update_a_doc_via_github.html <https://docs.openedx.org/en/latest/documentors/how-tos/update_a_doc_via_github.html>`_  
2. Create a GitHub issue so someone else is aware of the error and can fix it. Link to the issue in the Failure flag.  
   `Check this how-to doc for creating GitHub issues <https://docs.openedx.org/en/latest/documentors/how-tos/update_a_doc_via_github.html>`_

    
