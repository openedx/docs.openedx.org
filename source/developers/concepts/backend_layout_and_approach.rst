Backend Layout and Approach
###########################

`OEP-49 <https://open-edx-proposals.readthedocs.io/en/latest/architectural-decisions/oep-0049-django-app-patterns.html>`_ defines the common conventions used for Django apps written for this project.

New apps, services, and libraries should be created using `edx-cookiecutters <https://github.com/openedx/edx-cookiecutters>`_, which will fill in a lot of the boilerplate pieces for you (e.g. license, translations, testing dependencies).

There are other OEPs that define accepted `best practices <https://open-edx-proposals.readthedocs.io/en/latest/index.html#best-practices>`_, including things like `data modeling conventions <https://open-edx-proposals.readthedocs.io/en/latest/best-practices/oep-0038-Data-Modeling.html>`_ and `caching <https://open-edx-proposals.readthedocs.io/en/latest/best-practices/oep-0022-bp-django-caches.html>`_. Some of these best practices are encoded into the `edx-django-utils <https://github.com/openedx/edx-django-utils>`_ package.

Many repositories and individual apps will contain `Architecture Decision Records (ADRs) <https://open-edx-proposals.readthedocs.io/en/latest/best-practices/oep-0019-bp-developer-documentation.html#adrs>`_ explaining the reasoning behind various decisions that were made there. It's a good idea to at least skim over the relevant ADRs in a repo before starting major work there.
