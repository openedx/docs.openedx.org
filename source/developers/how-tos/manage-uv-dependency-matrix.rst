How To Manage a uv Dependency Version Matrix
#############################################

.. tags:: developer, how-to

This how-to explains how to add, update, or retire a dependency that is tested
against multiple versions (e.g. Django 5.x *and* 6.x) in a repository that uses
``uv`` for dependency management.

Assumptions
***********

* Your repository uses ``uv``, ``tox-uv``, and ``uv-venv-lock-runner`` for
  dependency management and testing. If it does not, see the
  `uv ADR in openedx-proposals`_ for background on the expected setup.

* You understand
  `PEP 735 dependency groups`_ and how ``[tool.uv].conflicts`` lets ``uv``
  produce a single ``uv.lock`` with independent resolutions for mutually
  exclusive groups.

.. _uv ADR in openedx-proposals: https://docs.openedx.org/projects/openedx-proposals/en/latest/best-practices/oep-0067/decisions/backend/0001-uv.html
.. _PEP 735 dependency groups: https://peps.python.org/pep-0735/

Steps: Adding a new version
****************************

Use this process when you want to start testing against a new version while
still keeping the previous one in the matrix (e.g. add Django 6.0 while still
testing Django 5.2).

The ``test`` group always represents the **current default version** — the one
used by quality checks, docs builds, and the primary CI matrix entry. When
promoting a new version to default, the old version moves to its own named
group (e.g. ``django52``).

1. **Update the** ``test`` **group** in ``pyproject.toml`` to the new version:

   .. code-block:: toml

      # Before
      test = [
          {include-group = "test-base"},
          "Django>=5.0,<6.0",
      ]

      # After
      test = [
          {include-group = "test-base"},
          "Django>=6.0,<7.0",
      ]

2. **Add a legacy group** for the version being retained:

   .. code-block:: toml

      django52 = [
          {include-group = "test-base"},
          "Django>=5.0,<6.0",
      ]

3. **Register the conflict** so ``uv`` knows the groups are mutually exclusive:

   .. code-block:: toml

      [tool.uv]
      conflicts = [
          [
              {group = "test"},
              {group = "django52"},  # new
          ],
      ]

   Add the new group to the existing conflict entry — all version groups for
   the same dependency belong in a single list.

4. **Update** ``tox.ini`` — add the new legacy factor to ``envlist`` and a
   factor conditional to ``dependency_groups``:

   .. code-block:: ini

      # Before
      [tox]
      envlist = py312-django{52},quality,docs

      [testenv]
      runner = uv-venv-lock-runner
      dependency_groups =
          django52: test

      # After
      [tox]
      envlist = py312-django{52,60},quality,docs

      [testenv]
      runner = uv-venv-lock-runner
      dependency_groups =
          django52: django52
          django60: test

5. **If the new version requires overriding a global constraint** (for example,
   the global edx-lint constraint pins ``Django<6.0`` but you need ``Django<7.0``
   to allow 6.x to resolve), add an override to ``[tool.edx_lint].uv_constraints``
   in ``pyproject.toml``:

   .. code-block:: toml

      [tool.edx_lint]
      uv_constraints = [
          "Django<7.0",  # allows Django 6.x; overrides the global Django<6.0 pin
      ]

6. **Regenerate the lockfile**:

   .. code-block:: bash

      make upgrade

Steps: Retiring a version
**************************

Use this process when a version reaches end-of-life and you want to drop it
from the matrix entirely.

1. **Remove the legacy group** (e.g. ``django52``) from ``[dependency-groups]``
   in ``pyproject.toml``.

2. **Remove it from the** ``conflicts`` **list** in ``[tool.uv]``:

   .. code-block:: toml

      [tool.uv]
      conflicts = [
          [
              {group = "test"},
              {group = "django60"},
          ],
      ]

3. **Remove the factor conditional** from ``dependency_groups`` in ``tox.ini``
   and drop it from ``envlist``:

   .. code-block:: ini

      # Before
      [tox]
      envlist = py312-django{52,60},quality,docs

      [testenv]
      runner = uv-venv-lock-runner
      dependency_groups =
          django52: django52
          django60: test

      # After
      [tox]
      envlist = py312-django{60},quality,docs

      [testenv]
      runner = uv-venv-lock-runner
      dependency_groups =
          django60: test

4. **Regenerate the lockfile**:

   .. code-block:: bash

      make upgrade

**Maintenance chart**

.. list-table::
   :header-rows: 1

   * - Review Date
     - Working Group Reviewer
     - Release
     - Test situation
   * - 2026-04-27
     - @feanil
     - main
     - Pass
