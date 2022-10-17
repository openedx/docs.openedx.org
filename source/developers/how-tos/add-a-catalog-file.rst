How To Add a Catalog File
#########################


This How-to will walk you through the process of adding a ``catalog-info.yaml``
file to your repository so that it is properly cataloged in the Open edX instance
of `Backstage`_.

To learn more about why we use ``catalog-info.yaml`` and backstage, see `OEP-55
Decision 1`_.

.. _OEP-55 Decision 1: https://open-edx-proposals.readthedocs.io/en/latest/processes/oep-0055/decisions/0001-use-backstage-to-support-maintainers.html

.. _Backstage: https://backstage.openedx.org

Assumptions
***********

This How-to assumes the following:

* You know how to use Git and GitHub PR Workflows.

* You know how to edit YAML files.

* You have a local clone of the repository you wish to add a catalog file to.

* You have access to `Backstage`_.

Steps
*****

1. Go to your local clone of the repository you want to update.

2. Create a ``catalog-info.yaml`` file at the root of the repository.

3. Add the content from sample file from `OEP-55 Decision 1`_

4. Update the content using the comments as a guide.

5. Make a pull request with the changes and get it merged into your project.

6. After the PR has merged, it can take up to 90 minutes for backstage to pick
   up the changes.  But after that time you should see a catalog entry in
   backstage for your repository.
