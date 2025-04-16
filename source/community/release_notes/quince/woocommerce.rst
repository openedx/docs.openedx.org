Integrating WooCommerce WordPress Plugin (Quince)
#################################################

Earlier this year, we began discovery work on the possibility of integrating the
Open edX platform directly with a 3rd party ecommerce platform that we would not
need to maintain. The big catalysts for this project were the `deprecation`_ of
the `ecommerce repo`_, and the need for a replacement that would be accessible
across technical capabilities. We wanted to find out if a simple implementation
could not only work for smaller deployments, but that would also complement
commerce-coordinator for larger deployments.

We're happy to announce that we just successfully completed a funded
contribution project with eduNEXT to integrate WooCommerce as an e-commerce
service, through which courses can be sold. The integration helps to streamline
workflows and provide capabilities such as:

* Ability to create Open edX course products
* Ability to buy an Open edX course, which will start an enrollment with a seat
  in a specific course run
* Refunding an Open edX course, which will cause a soft unenrollment
  (``is_active=False``)
* Checking the status of an enrollment
* If you are using the Quince release, you can also create enrollment allowed

See a demo of the plugin here:

.. youtube:: TuDT-qwQdyE

If you're interested in the WooCommerce integration, you can now activate `this
plugin`_ in your WordPress site and connect your Open edX instance with your
WordPress! Additional documentation can be found here: :doc:`wordpress-ecommerce-plugin:index`

This integration can serve as a model for integrating with other ecommerce
platforms in a standard and supportable way. For further details on the project
work itself, you can check out:

* Pull requests created to improve the enrollment APIs: `#33006`_ and `#33059`_
* `Project discovery documentation`_

.. _deprecation: https://github.com/openedx/public-engineering/issues/22
.. _ecommerce repo: http://github.com/openedx/ecommerce/
.. _this plugin: https://edunext-docs-openedx-woocommerce-plugin.readthedocs-hosted.com/en/latest/plugin_quickstart.html#add-the-plugin-settings
.. _#33006: https://github.com/openedx/edx-platform/pull/33006
.. _#33059: https://github.com/openedx/edx-platform/pull/33059
.. _Project discovery documentation: https://docs.google.com/document/d/1gImq4DFy3B_JSZlH3tCj5bmPQXji0OCnw1SbGB8bVxw/edit?usp=sharing


**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-04-28    | Docs WG                       | Teak           | Deprecated: This is no longer the current release |
+--------------+-------------------------------+----------------+---------------------------------------------------+

