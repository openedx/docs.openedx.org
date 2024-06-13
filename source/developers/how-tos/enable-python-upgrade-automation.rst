How To Enable Python Upgrade Automation
#######################################

This How-to will walk you through the process of getting the automated Python
requirements upgrade jobs setup on a repository.

Assumptions
***********

* You know how to use Git and GitHub PR Workflows.

* You have ``admin`` access to the repository.

Steps
*****

1. Replace ``<repo_name>`` with the name of your repository in the following URL
   and go to it:

   .. code::

      https://github.com/openedx/<repo_name>/actions/new?category=owner

2. Click :guilabel:`Configure` on the ``Python Requirements Upgrade Workflow``
   card.

   .. image:: /_images/developer_how_tos/python-requirements-upgrade-workflow.png
      :alt: An image of the Python Requirements Upgrade Workflow Card in GitHub's UI.

3. Review the contents of the GitHub action, make any changes that you might want
   to make.  If you're not sure, the defaults work fine for most use cases.

   * If you are applying changes to a newer repo, you may have ``main`` as your
     default branch instead of ``master``.  In which case you should update the
     workflow.

4. Commit the changes to a branch and get the PR reviewed and merged.

   .. image:: /_images/developer_how_tos/python-requirements-upgrade-make-pr.png
      :alt: An image of the UI formaking a branche for your changes.

5. Next, add the `edx-requirements-bot` team to your repository with ``write``
   permissions.  It will be at the following url with ``<repo_name>`` replaced
   with your actual repository name.

   .. code::

      https://github.com/openedx/<repo_name>/settings/access

   .. image:: /_images/developer_how_tos/edx-requirements-bot-write.png
      :alt: What the edx-requirements-bot team looks like once you've added it.
