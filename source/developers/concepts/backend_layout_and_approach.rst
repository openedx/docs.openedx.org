Backend Layout and Approach
###########################

.. tags:: developer, concept


:doc:`openedx-proposals:best-practices/oep-0049-django-app-patterns` defines the common conventions used for Django apps written for this project.

New apps, services, and libraries should be created using `edx-cookiecutters <https://github.com/openedx/edx-cookiecutters>`_, which will fill in a lot of the boilerplate pieces for you (e.g. license, translations, testing dependencies).

There are other OEPs that define accepted best practices (see :ref:`openedx-proposals:Best-Practices`), including things like :doc:`openedx-proposals:best-practices/oep-0038-Data-Modeling` and :doc:`openedx-proposals:best-practices/oep-0022-bp-django-caches`. Some of these best practices are encoded into the `edx-django-utils <https://github.com/openedx/edx-django-utils>`_ package.

Many repositories and individual apps will contain Architecture Decision Records (ADRs) :ref:`openedx-proposals:ADRs` explaining the reasoning behind various decisions that were made there. It's a good idea to at least skim over the relevant ADRs in a repo before starting major work there.


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
