How To Maintain a Repository
############################

.. contents::
   :local:
   :class: no-bullets

.. note::

   Maintaining a repository requires more than just doing the tasks outlined
   here.  This page outlines the things that are easy to write down and follow.
   It does not include advice on other important aspects of being a good
   maintainer, such as being a good steward of the codebase, and being a
   supportive leader in the community. This and many other activities that a
   maintainer is expected to do involve critical thinking and an understanding
   of the specifics of the codebase you maintain.

Congratulations on becoming the maintainer of a repository in the Open edX
Platform! As outlined in `OEP-55`_ this is a big responsibility and we're
excited to help you fulfill it.

Your repository may be brand new or it may have been around for a while.  In
either case, this document will help you review the repository and help you make
the changes needed to meet the current standards of the platform.

GitHub Issues is Enabled
************************

GitHub Issues should be enabled on your repository.  This is how issues will be
reported against your repository.

**Test**

Go to your repository on GitHub.  If you see an issues tab, you don't need to do
anything else.  If you *don't see an issues tab* then see the ``Fix``
Section for what to do.

**Fix**

Go to the ``Settings`` Tab for the repository you maintain and check the
"Issues" box in the general settings.

A catalog-info.yaml File Exists
*******************************

We use `backstage`_ to help developers get a quick overview of all the things
they own and their status.

**Test**

* Check to see if there is a ``catalog-info.yaml`` file at the root of your repository.

* Ensure that the file is up-to-date.  Especially the name of the maintainer.

**Fix**

If the file exists, check to make sure the data is up-to-date and correct. If
you don't have a ``catalog-info.yaml`` file, see :doc:`add-a-catalog-file`

Python Dependency Update Automation is Enabled
**********************************************

**Test**

If your repository contains python code, ``.github/workflows/upgrade-python-requirements.yml``
should exist and be a copy of `the python upgrade workflow template`_.  You should
also see successful runs of the ``Upgrade Python Requirements`` workflow in the
``Actions`` tab of your repo.

For frontend repos, the XXX workflow(s) should exist.

.. _the python upgrade workflow template: https://github.com/openedx/.github/blob/master/workflow-templates/upgrade-python-requirements.yml

**Fix**

If the file doesn't exist, or the workflow runs are failing, go through
:doc:`enable-python-upgrade-automation`.

Javascript Dependency Update Automation is Enabled
**************************************************

**Test**

If your repository contains javascript code, ``renovate.json`` should exist and
be a copy of `the reference renovate.json in frontend-template-application`_.
You should also see auto-generated dependency update PRs show up in the
repository.

.. _the reference renovate.json in frontend-template-application: https://github.com/openedx/frontend-template-application/blob/master/renovate.json

**Fix**

If ``renovate.json`` doesn't exist or you don't see any PRs being generated,
follow :doc:`enable-javascript-upgrade-automation`.

A Well-Formed README Exists
***************************

**Test**

Check that your README.rst exists and has all the sections defined in the `README
specification`_.

**Fix**

Update your readme until it meets the above specification.

.. _OEP-55: https://open-edx-proposals.readthedocs.io/en/latest/processes/oep-0055-proc-project-maintainers.html

.. _backstage: https://backstage.openedx.org

.. _readme specification: https://open-edx-proposals.readthedocs.io/en/latest/processes/oep-0055/decisions/0003-readme-specification.html

Your CCs are Aligned With Your Expectations as Maintainer
*********************************************************

A repo that you take on may already
have other CCs that have merge rights on it.  You should review which CCs have
write access to your repo on the `CCs Wiki Page`_.  You should communicate with
your CCs and ensure that you are aligned with them on the architectural goals
of the repo, especially if there are particular kinds of changes that you as
the maintainer would like to have more input on.

.. warning::

   Sometimes github teams are used to group multiple repos together and the CCs
   wiki lists the team instead of each individual repo.  The teams that are
   used for access should be listed at the top of the wiki page.

   You can also make an `Axim Request`_ to get a snapshot of the what users and
   teams currently have access to your repo if you need more details or have
   questions.

.. _Axim Request: https://github.com/openedx/axim-engineering/issues/new/choose

For any new CCs that might get added to your repo, you will have the
opportunity to vote on their nomination and decide whether they should get
access.  See the :ref:`CC nomination process <openedx-proposals:new cc process>`
documentation for more details.

For any CCs that you believe are not fulfilling their role properly you may opt
to initiate :ref:`the CC removal process <openedx-proposals:removing ccs>` as
outlined in :doc:`OEP-54 <openedx-proposals:processes/oep-0054-core-contributors>`


.. _CCs Wiki Page: https://openedx.atlassian.net/wiki/spaces/COMM/pages/3156344833/Core+Contributors+to+the+Open+edX+Project

Congratulations!
****************

Your repository is now up to Maintainers standards! Now you're ready to begin your
journey as a maintainer of your repo. Visit the :doc:`ongoing-maintainers-tasks`
page to learn more about what's expected of you (and your team, if applicable).


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
