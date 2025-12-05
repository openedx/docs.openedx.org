.. _Create a Reusable LTI 1.3 Configuration:


Create a Reusable LTI 1.3 Configuration
######################################################

.. tags:: site operator, how-to


Overview
********

Reusable LTI configurations are created once by an administrator in Django Admin (LTI Store) and identified by a filter key.  
In Studio, you can point an LTI Consumer component to that reusable configuration, avoiding repeated copy/paste of credentials.

See :ref:`Set up an LTI Consumer with Reusable LTI Configuration` for
instructions on using the configuration in Studio once it has been set up.

Create Reusable Configuration in Django Admin
*********************************************

* Create a reusable LTI 1.3 configuration in Django Admin.
* Supply the reusable configuration's filter key to course authors. It may be shared as a value like ``lti_store:reference_tool``

.. seealso::

 :ref:`Set up a Reusable LTI Store` (how-to)

 :ref:`LTI Component Settings` (reference)

 :ref:`Set up an LTI 1_3 component` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        | Release        | Test situation                 |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-12-05   | LTI WG                        | Ulmo           | Draft                          |
+--------------+-------------------------------+----------------+--------------------------------+
