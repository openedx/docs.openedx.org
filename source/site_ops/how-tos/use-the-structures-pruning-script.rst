.. _Use the Structures Pruning Script:

How to Use the Structures Pruning Script
########################################

.. tags:: site operator, how-to

Background
**********

The Open edX platform stores XBlock component data as documents in the MongoDB ``modulestore.structures`` collection.
The documents are never updated: every time a component is edited and saved, a new document is inserted.
This is to support reverting updates back to previous versions, however there is no UI for this.

This also means that the ``modulestore.structures`` collection can grow unbounded over time as many edits are made.

It may be desirable to delete old revisions to reduce the size of the MongoDB database.

The structures pruning script
*****************************

There is a script called `structures_pruning <https://github.com/openedx/openedx-platform/blob/master/scripts/structures_pruning>`_ in openedx-platform that can be run on the database to safely remove these old revisions.

On long lived instances, where it's been determined that old revisions were not required, this script has been known to reduce the size of the ``modulestore.structures`` collection by over 99%.

How to use
**********

Here is a step-by-step guide for running this.

1. Set up an environment
========================

This needs to run from an environment that can access the MongoDB server, and ideally from the same region for best performance.

You will also need a decent size persistent volume to store database backups. Also to store the plan from the script, so this process can be resumed if interrupted.

2. Back up the MongoDB database
===============================

The script takes precautions to ensure this doesn't leave the database in a broken state.
However, it's recommended to run a backup of the database first.

For example:

.. code:: sh

    mongodump -d "$DATABASE_NAME" -o "$OUTPUT_DIRECTORY" --authenticationDatabase admin \
      --dumpDbUsersAndRoles --gzip "$CONNECTION_STRING"

It's also probably worth doing this through a maintenance window to avoid disruption.
If possible, avoid using Studio during this time to prevent lost work in case you need to restore the database from this backup.

3. Make note of the database size
=================================

To be able to see how much space this script saves,
make note of some database size stats first.
The most useful ones to note would be:

- main openedx database disk size

- main openedx database data size

- ``modulestore.structures`` collection data size

- ``modulestore.structures`` collection disk size

(Size on disk can be much larger than data size if free space is being reserved; we'll compact the database after running the pruning to realise the reduction in disk usage.)

These stats can be collected by getting a MongoDB shell:

.. code:: sh

    mongosh "$CONNECTION_STRING"

Then running these in the MongoDB shell:

.. code:: js

    use DATABASE_NAME

    // show the stats for the overall database, in GiB
    db.stats({ scale: 1073741824 })

    // show the stats for the structures collection, in GiB
    console.log({
      ...db["modulestore.structures"].stats({ scale: 1073741824 }),
      "wiredTiger": null
    })

4. Install the structures pruning script
========================================

Some quick steps for installing. A shallow clone of openedx-platform is recommended because the repository is very large.

.. code:: sh

    git clone --depth=1 https://github.com/openedx/openedx-platform.git
    virtualenv venv
    source venv/bin/activate
    pip install -r openedx-platform/scripts/structures_pruning/requirements/base.txt

5. Run the ``make_plan`` subcommand
===================================

The script operates in two subcommands, where the first does a read-only scan of the ``modulestore.structures`` collection and makes a plan for what to delete.
The second subcommand actually executes the plan.
This is to support resuming, and reduces the chance of a broken database state.

The ``make_plan`` subcommand can be run like this:

.. code:: sh

    python openedx-platform/scripts/structures_pruning/structures.py \
      --connection "$CONNECTION_STRING" --database-name "$DATABASE_NAME" \
      make_plan -v DEBUG --dump-structures --delay 1000 --batch-size 10000 \
      --retain 0 --details pruning-plan.txt pruning-plan.json 2>&1 | tee pruning-plan.log

Some important notes:

- ``--retain`` specifies how many old revisions to retain in addition to the current and original. Consider using ``0`` to clean up as much as possible, or set this to a small number (eg. ``2``) if there is a chance that recent revisions may be required. Note that there is no UI for restoring these revisions, and you are taking a backup, so in most cases, no revisions should need to be retained.

- This script can put a fair load on the MongoDB server, so to reduce noticeable slowdowns, consider tweaking the the following parameters:

  - ``--delay`` (time in ms to wait between batches)

  - ``--batch-size`` (number of structures to query at a time)

  - Consider checking the case studies at the end for examples of parameters and run time (in practice this can run pretty quickly).

- These are readonly operations and should be always safe to run. However, they may impact server load.

- Do check the plan output (both the human readable txt file and the json). The json file is the plan that will be executed in the next step.

6. Run the ``prune`` subcommand
===============================

Now the plan is generated, it can be executed with the prune subcommand.

WARNING: this subcommand is the one that writes and deletes data! It is designed to be as safe as possible: order of operations and resumability is to ensure the database cannot get into a broken state.

The ``prune`` subcommand can be run like this:

.. code:: sh

    python openedx-platform/scripts/structures_pruning/structures.py \
      --connection "$CONNECTION_STRING" --database-name "$DATABASE_NAME" \
      prune --delay 100 --batch-size 5000 -v DEBUG pruning-plan.json 2>&1 | tee prune.log

Some important notes:

- This can also put load on the MongoDB server, and the ``--delay`` and ``--batch-size`` options can be tweaked in the same way as for ``make_plan``.

  - Consider checking the case studies at the end for examples of parameters and run time (in practice this can run pretty quickly).

- This is safely resumable; if interrupted, simply run the same command again with the same ``pruning-plan.json``. Do not generate a new plan before this is complete, otherwise this may result in documents that can no longer be cleaned up by this script (the collection state will not be broken, but some older revisions may no longer be reachable).

7. Compact the database
=======================

You will not see an immediate disk size reduction in the database,
because the MongoDB engine will continue to reserve the disk for future operations.

To release this disk space and see a real disk usage reduction, you can run the MongoDB `compact <https://www.mongodb.com/docs/manual/reference/command/compact/>`_ command:

.. code:: sh

    mongosh "$CONNECTION_STRING"

Then in the MongoDB shell:

.. code:: js

    use DATABASE_NAME

    db.runCommand({ compact: "modulestore.structures" })

Note: if this is a MongoDB replicaset, see the `MongoDB reference for running compact on Replica Sets <https://www.mongodb.com/docs/manual/reference/command/compact/#replica-sets>`_
to compact each of the nodes (otherwise this may only compact a single node).

8. Check the instance
=====================

At this point, it's recommended to do some spot checks on the Open edX instance,
to check for any issues.
Navigate to some courses in Studio, make some test edits on components, check they display as expected.

If anything is really amiss, the database can be restored from the earlier backup.

9. Check the database size
==========================

Here we get to see the result of our efforts!

Repeat the queries from step `3. Make note of the database size`_,
and compare with the earlier stats. :)

Case studies
************

Some real world examples of running this.

Example 1
=========

- ``modulestore.structures`` collection

  - ~137,000 documents reduced to ~2000

  - 27GiB data size reduced to 0.1GiB

  - 9.3GiB disk storage reduced to 0.04GiB

  - more than 95% reduction in disk storage

- parameters used for the pruning subcommands:

  - ``make_plan``: 100ms delay, 10,000 batch size, 60s run time

  - ``prune``: 100ms delay, 5000 batch size, 1m 50s run time

Example 2
=========

- ``modulestore.structures`` collection

  - 258GB data size reduced 1.4GB

  - 80GB disk storage reduced to 0.55GB

  - more than 99% reduction

- parameters used for the pruning subcommands:

  - ``make_plan``: 200ms delay, 1000 batch size, ~10m run time

  - ``prune``: 200ms delay, 1000 batch size, 20m run time

Final notes
***********

If old revisions are not required for any reason, this could even be auto-run periodically to keep the database size in check.

If you ran this script on a particularly large database, or have any interesting observations, please let us know!
It will be interesting to add more real world examples to the case studies above.


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        | Release        | Test situation                 |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-07-20   | Samuel Allan                  | Ulmo           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
| 2026-07-26   | Samuel Allan                  | Teak           | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
