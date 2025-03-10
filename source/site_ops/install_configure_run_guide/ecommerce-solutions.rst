.. _Adding ECommerce to Open edX:

Adding ECommerce to Open edX
#############################

.. tags:: site operator

This section is intended for those are who are building Open edX ecommerce
solutions and customizing an Open edX installation to support their use.

.. contents::
   :local:
   :depth: 1

Open edX Commerce (WordPress Plugin)
************************************

The Open edX WooCommerce Plugin is a free, open-source WordPress plugin that aims to integrate third-party e-commerce, WooCommerce, with your Open edX platform. See the following resources:

* :doc:`wordpress-ecommerce-plugin:plugin_quickstart`
* `Open edX Commerce (WordPress Plugin) Source <https://github.com/openedx/openedx-wordpress-ecommerce?tab=readme-ov-file#-open-edx-commerce-wordpress-plugin>`_

Open edX Webhook Receiver
*************************

The `Open edX Webhook Receiver <https://github.com/hastexo/webhook-receiver?tab=readme-ov-file#openedx-webhook-receiver>`_
extension  is a small Django app that listens for incoming webhooks, and then
translates those into calls against the Open edX REST APIs.

As of Sumac it supports WooCommerce and Shopify endpoints.

Maintenance Chart

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
