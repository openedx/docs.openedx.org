Verifiable Credentials on the Open edX Platform (Palm)
######################################################

Verifiable digital credentials allow learners to control and share records of
their accomplishments in a way that is privacy-preserving, independently
verifiable, and tamper-evident. For learners, their credentials are ultimately
more valuable because they are easier to manage, present, and verify on terms
set by the learner themselves.

The basic idea is that learners can present proof of their accomplishments
instantly to potential employers, admissions offices, government agencies, or
whatever recipient they choose. The receiver of the credential can verify its
validity, and be confident that it hasn't been tampered with, ensuring it
belongs to the person presenting it. The entire process can be completed in
seconds!

   .. image:: /_images/release_notes/palm/vc1.png


Recently we shipped the first increment of support for verifiable credentials on
the Open edX platform. The first increment allows learners to share program
credentials to wallets that support two data models, `Verifiable Credentials Data
Model v1.1`_ and the `Open Badges Specification v3.0`_. Our testing and development
targeted sharing credential via the `Learner Credentials Wallet`_, an application
for iOS and Android phones, created by the `Digital Credentials Consortium`_. The
Learner Credentials Wallet supports storing credentials using both data models.

.. _Verifiable Credentials Data Model v1.1: https://www.w3.org/TR/vc-data-model-1.1/
.. _Open Badges Specification v3.0: https://1edtech.github.io/openbadges-specification/ob_v3p0.html
.. _Learner Credentials Wallet: https://github.com/digitalcredentials/learner-credential-wallet
.. _Digital Credentials Consortium: https://digitalcredentials.mit.edu/


Learners can choose a program credential to share and scan a QR code to import
it into their wallet on their mobile device.

   .. image:: /_images/release_notes/palm/vc2.png
      :scale: 50%


With the first increment, only program credentials are supported and it's
required that the `Credentials Service`_ is deployed along with
`frontend-app-learner-record`_. The feature is for anyone using the latest version
of the Palm release, or running off the latest version of the Open edX main
branch.

We are currently planning the next increments of support for verifiable digital
credentials on the Open edX platform. We expect to invest in supporting
additional data models, expanding to support course certificates, expanding to
support badges, and mapping credentials to content taxonomies to communicate
clearly what skills learners have acquired.

If you are interested in helping to test or refine the credentials roadmap, join
the conversation in the #learner-credentials channel in the `Open edX Slack`_!

If you're interested in setting up Verifiable Credentials support in your Open
edX instance, `start here`_.

.. _Credentials Service: https://github.com/openedx/credentials
.. _frontend-app-learner-record: https://github.com/openedx/frontend-app-learner-record
.. _Open edX Slack: https://openedx.slack.com/
.. _start here: https://edx-credentials.readthedocs.io/en/latest/verifiable_credentials/overview.html

**Maintenance chart**

+--------------+-------------------------------+----------------+---------------------------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                                     |
+--------------+-------------------------------+----------------+---------------------------------------------------+
|2025-04-28    | Docs WG                       | Teak           | Deprecated: This is no longer the current release |
+--------------+-------------------------------+----------------+---------------------------------------------------+

