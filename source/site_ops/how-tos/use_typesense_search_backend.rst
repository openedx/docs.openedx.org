.. _Use Typesense search backend:

Use Typesense search backend
############################

.. tags:: site operator, how-to

.. warning::

    Typesense search support as discussed below has not been released yet; it is planned for the Verawood release.

`Typesense <https://typesense.org/>`_ is a high performance search engine,
supported on the Open edX platform in the following search areas:

* Course info (course search on the Discover New page)
* Courseware (course content search)
* Forum (threads and comments)

This is an alternative to the default search backend, Meilisearch.

**You may wish to select Typesense here if you require high availability (HA) for the search backend**.
Typesense supports high availability out of the box, while Meilisearch does not (at least for the self hosted version).

Please note that either way, Meilisearch will still be required for Studio course content search; that does not yet have support for Typesense.

Getting started
***************

See below for how to start using Typesense with your Open edX instance, depending on whether you use Tutor or not:

Tutor
=====

If you use Tutor, you can install the `tutor-contrib-typesense`_
plugin, which will automatically deploy a single node Typesense instance
and configure the platform to use it.

.. note::

   This plugin does not support deploying Typesense as a HA cluster. If you require a cluster, please follow the manual configuration section below.

#. Install the plugin:

   .. code-block:: shell

      pip install -e https://github.com/open-craft/tutor-contrib-typesense
      tutor plugins enable typesense

#. Configure if required. For most cases, the defaults will be fine. Available configuration is documented on `the plugin's readme <https://github.com/open-craft/tutor-contrib-typesense?tab=readme-ov-file#configuration>`_.

   If you require custom configuration, set them using Tutor, for example:

   .. code-block:: shell

      tutor config save --set TYPESENSE_COLLECTION_PREFIX=my_instance_

#. Initialise the plugin - some examples:

   .. code-block:: shell

      # if an existing k8s deployment
      tutor k8s do init --limit=typesense

      # if launching a devstack
      tutor dev launch

#. Reindex content - if this is an existing deployment with content already, you will need to manually run a reindex (the Typesense indexes are created automatically):

   .. code-block:: shell

      # reindex courseware content and course info
      tutor dev exec cms -- python manage.py cms reindex_course --active

      # reindex forum threads and comments
      tutor dev exec lms -- python manage.py lms rebuild_forum_indices

#. Finally, to enable course content search on the frontend, create and enable a waffle flag named ``courseware.mfe_courseware_search``. You can do this from the LMS Django admin page, waffle flags section.

Manual configuration
====================

If you aren't using Tutor, here are instructions for getting started manually.

#. Deploy an instance of Typesense. See the `Typesense installation guide <https://typesense.org/docs/guide/install-typesense.html>`_ for more information.

#. Create an API key. See the Typesense `API Keys doc <https://typesense.org/docs/latest/api/api-keys.html>`_ for more information.
   Optionally, for extra security, you can scope the API key permissions to a custom collection prefix. This prefix can be configured for the Open edX platform in the following step (the ``TYPESENSE_COLLECTION_PREFIX`` setting).
   For example:

   .. code-block:: shell

      curl -X POST 'http://localhost:8108/keys' \
        -H 'Content-Type: application/json' -H 'X-TYPESENSE-API-KEY: mysecretadminkey' \
        --data-binary '{
            "value": "mysecretapikeyvalue",
            "description": "API key for my Open edX instance",
            "actions": ["*"],
            "collections": ["^openedx_.*"]
        }'


#. Set the following Django settings for LMS and CMS:

   .. code-block:: python

      # Enable the Typesense backend.
      TYPESENSE_ENABLED = True

      # Set the API key for authenticating to Typesense.
      TYPESENSE_API_KEY = "your-secret-api-key-for-typesense"

      # Set the internal urls where the LMS/CMS can reach the Typesense API.
      # If Typesense is deployed as a cluster, provide the urls to all nodes here.
      TYPESENSE_URLS = ["https://typesense-1.example.com:8108", "https://typesense-2.example.com:8108"]

      # The prefix that the backend should use for all collections (you can scope the API key permissions to this prefix for security).
      # This is useful if the Typesense instance is shared with other software.
      TYPESENSE_COLLECTION_PREFIX = "openedx_"

      # Optional: if you need to override the forum search backend module for testing
      #FORUM_SEARCH_BACKEND = "forum.search.typesense.TypesenseBackend"

      # Optional: if you need to override the course search backend module for testing
      #SEARCH_ENGINE = "search.typesense.TypesenseEngine"


#. Reindex content - if this is an existing deployment with content already, you will need to manually run a reindex (the Typesense indexes are created automatically):

   .. code-block:: shell

      # In the CMS environment: reindex courseware content and course info
      python manage.py cms reindex_course --active

      # In the LMS environment: reindex forum threads and comments
      python manage.py lms rebuild_forum_indices

#. Finally, to enable course content search on the frontend, create and enable a waffle flag named ``courseware.mfe_courseware_search``. You can do this from the LMS Django admin page, waffle flags section.


Clustered Typesense
*******************

Some notes regarding running Typesense in a cluster, for a HA setup.

* For clustered Typesense, it's best to provide urls to all the nodes to ``TYPESENSE_URLS``, rather than putting it behind a load balancer.
  This allows the Typesense client to manage load balancing and fallbacks itself.
* Be careful when running a Typesense cluster on Kubernetes, as there can be issues related to how consensus is implemented and that Kubernetes pods don't necessarily have static IP addresses. See `typesense/typesense#465 <https://github.com/typesense/typesense/issues/465>`_ and `typesense/typesense#2049 <https://github.com/typesense/typesense/issues/2049>`_ for more information.


Typesense web dashboard
***********************

Typesense doesn't come with an official web dashboard,
but there is a community dashboard developed at https://github.com/bfritscher/typesense-dashboard.
You can visit it directly on the web without installing at https://bfritscher.github.io/typesense-dashboard/.

For example, to connect to a Typesense server from a local Tutor devstack using the Typesense plugin,
visit the web dashboard url, and enter the following details at the login screen:

* Api Key: (use the output from running ``tutor config printvalue TYPESENSE_API_KEY``)
* protocol: ``http``
* host: ``localhost``
* port: ``8108``
* path: (leave blank)


.. seealso::

    :ref:`Enable edX Search`


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        | Release        | Test situation                 |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-01-21   | Samuel Allan                  | master         | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+

.. _tutor-contrib-typesense: https://github.com/open-craft/tutor-contrib-typesense/
