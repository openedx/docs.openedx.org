How To Enable Javascript Upgrade Automation
###########################################

This How-to will walk you through the process of getting Renovate enabled for a
repository.

Assumptions
***********

* You know how to use Git.

* You know your way around GitHub issues and pull requests.

* You are familiar with the JSON format.

Steps
*****

#. Commit a ``renovate.json`` file to the root of your repository as a copy of
   `the one in frontend-template-application`_.

#. File `a new [GH Request] issue`_ in the Open edX GitHub organization asking
   for Renovate and Renovate Approve to be enabled for your repository.  Fill
   out the relevant information, making sure to include your repository name in
   the "Problem/Request" section.

#. Once Renovate is enabled, you should notice auto-generated PRs getting
   issued to your repository.

   .. warning::

      The PRs that pass tests will be auto-merged by default even if the
      repository requires manual approval.

.. _the one in frontend-template-application: https://github.com/openedx/frontend-template-application/blob/master/renovate.json
.. _a new [GH Request] issue: https://github.com/openedx/axim-engineering/issues/new?assignees=&labels=github-request&template=04-systems-request---uncategorized.yml&title=[GH+Request]+Enable+Renovate+for+my+repo
