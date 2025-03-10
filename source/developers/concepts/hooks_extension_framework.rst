Hooks Extension Framework
#########################

.. tags:: developer, concept

What is the Hooks Extension Framework?
**************************************

Based on the :doc:`edx-platform:concepts/extension_points`, this framework aims to extend the Open edX platform in a maintainable way without modifying its core. The main goal is to leverage the existing extension capabilities provided by the :doc:`edx-django-utils:plugins/readme` architecture, allowing developers to implement new features while reducing the need for core modifications and minimizing maintenance efforts.

Hooks are places in the Open edX platform where externally defined functions can take place. These functions may alter what the user sees or experiences on the platform, while in other cases, they are informative only. All hooks are designed to be used along with :doc:`edx-django-utils:plugins/readme`.

Hooks can be of two types: events and filters. Events are signals sent in specific places whose receivers can extend functionality, while filters are functions that can modify the application's behavior. To allow extension developers to use these definitions in their implementations, both kinds of hooks are defined in lightweight external libraries:

* `openedx-filters`_
* `openedx-events`_

The framework's main goal is to empower developers to change the platform's functionality as needed while allowing them to migrate to newer Open edX releases with little to no development effort. The framework is designed with stability in mind, meaning it is versioned and backward compatible as much as possible.

A longer description of the framework and its history can be found in :doc:`openedx-proposals:architectural-decisions/oep-0050-hooks-extension-framework`.

Why Adopt the Hooks Extension Framework?
****************************************

Stable and Maintainable Extensions
==================================

The Hooks Extension Framework allows developers to extend the platform's functionality in a stable, maintainable, and decoupled way ensuring easier upgrades and long-term stability by removing the need to modify the core in a significant way.

Contained Solution Implementation
=================================

By avoiding core modifications, the framework promotes self-contained solutions, eliminating the need for custom code to coexist with core logic which lowers maintenance costs for extension developers. As most extensions can now be implementing using the framework, forks are closer to the core and easier to manage.

Leveraging the Open edX Plugin Extension Mechanism
==================================================

The framework allows developers to implement custom business logic and integrations directly in plugins. This keeps core modifications minimal, focusing maintenance and development efforts on plugins, where solutions can be built and maintained independently of the core platform.

Standardization
===============

Filters and events provide developers with a standard for adding new features to the platform through extension mechanisms. Events primarily handle communication or synchronization between different parts of the application, while filters modify application behavior. If a problem can be addressed through one of these two options, the implementation becomes pretty straightforward.

Community Compatibility
=======================

The framework allows for shorter and more agile contribution cycles. By adding standardized extension points, contributors avoid creating customer-specific logic, making development more community-friendly.

Backward Compatibility
======================

Hooks are designed to be backwards compatible, guaranteeing stability across releases and making it easier to upgrade without breaking existing functionality. This ensures that extensions built on the framework will continue to work as expected across different Open edX versions. See the Architectural Decision Records (ADRs) about versioning for Open edX Events and Filters for more information:

* :doc:`openedx-events:decisions/0002-events-naming-and-versioning`
* :doc:`openedx-filters:decisions/0004-filters-naming-and-versioning`

Open edX Events and Filters
***************************

Open edX Events
===============

Events are Open edX-specific Django signals sent in specific places on the Open edX platform. Developers write code that listens to these signals and performs additional processing based on the event data.

To start using Open edX Events in your project, see the :doc:`Open edX Events <openedx-events:index>` documentation.

Open edX Filters
================

Filters are functions that can modify the application's behavior by altering input data or halting execution based on specific conditions. They allow developers to implement application flow control based on their business logic or requirements without directly modifying the application code.

To start using Open edX Filters in your project, see the :doc:`Open edX Filters <openedx-filters:index>` documentation.

Differences Between Events and Filters
=======================================

Here are some key differences between Open edX Events and Filters:

+--------------------+------------------------------------------------------------------------+-------------------------------------------------------------+
|                    | Events                                                                 | Filters                                                     |
+====================+========================================================================+=============================================================+
| **Purpose**        | Notify when an action occurs in a specific part of the                 | Alter the application flow control.                         |
|                    | application.                                                           |                                                             |
+--------------------+------------------------------------------------------------------------+-------------------------------------------------------------+
|  **Usage**         | Used to **extend** functionality via signal receivers when an event is |  Used to intercept and **modify** the data used within a    |
|                    | triggered.                                                             |  component without directly modifying the application       |
|                    |                                                                        |  itself.                                                    |
+--------------------+------------------------------------------------------------------------+-------------------------------------------------------------+
|  **Definition**    |  Defined using the ``OpenEdxPublicSignal`` class, which                |  Defined using the ``OpenEdxPublicFilter`` class,           |
|                    |  provides a structured way to define the data and                      |  which provides a way to define the filter function         |
|                    |  metadata associated with the event.                                   |  and the parameters it should receive.                      |
+--------------------+------------------------------------------------------------------------+-------------------------------------------------------------+
| **Implementation** |  Implemented using `Django signals`_, which allow                      |  Implemented using an accumulative pipeline mechanism which |
|                    |  developers to send and receive notifications that an action happened  |  takes a set of arguments and returns a modified set        |
|                    |  within a Django application.                                          |  to the caller or raises exceptions during                  |
|                    |  Events use `attrs`_ classes with simple data types.                   |  processing. The input arguments are in-memory platform     |
|                    |                                                                        |  objects that can be modified.                              |
+--------------------+------------------------------------------------------------------------+-------------------------------------------------------------+
| **Use cases**      |  Send an email notification when a user enrolls in a course.           |  Prevent the enrollment of non-authorized users.            |
+--------------------+------------------------------------------------------------------------+-------------------------------------------------------------+

In this diagram you can see the main differences in functionality between Open edX Events and Filters:

.. image:: /_images/hooks_events_and_filters_side_by_side.png
   :alt: Open edX Events and Filters Side by Side
   :align: center

How to Know When to Use an Event or a Filter?
=============================================

When to Use an Open edX Event?
------------------------------

A developer might use an Open edX Event in order to perform the following actions. Note that this is not an exhaustive list.

- Trigger custom logic or processing in response to specific actions within the platform, e.g., updating a search index after a course block is modified.
- Communicate, synchronize, or coordinate with other components or services based on specific events or actions, e.g., send certificate data from LMS to credentials service to keep models up to date.
- Integrate with external systems or services based on specific events or actions, e.g., send user data to third-party services upon registration for marketing purposes.

Fore more detailed use cases, please visit :doc:`openedx-events:reference/real-life-use-cases`.

In summary, events can be used to integrate application components with each other or with external services, allowing them to communicate, synchronize, and perform additional actions when specific triggers occur.

You can review the :doc:`Open edX Events <openedx-events:index>` documentation for more information on :doc:`creating events <openedx-events:how-tos/create-a-new-event>` and :doc:`consuming them <openedx-events:how-tos/consume-an-event>` in your project. This documentation includes a list of :doc:`openedx-events:reference/events` and much more.

When to Use an Open edX Filter?
-------------------------------

A developer might use an Open edX Filter in order to perform the following actions. Note that this is not an exhaustive list.

- Enrich the data or parameters used to a specific component, e.g., fetch reusable LTI configurations from external plugins.
- Enforce specific constraints or business rules of a specific component, e.g., don't allow registration for non-authorized email domains.
- Implement additional features or behavior in a specific component, e.g., add registration extra fields to the user registration form.

Fore more detailed use cases, please visit :doc:`openedx-filters:reference/real-life-use-cases`.

In summary, filters can be used when implementing application flow control that modifies the application's behavior, navigation, or user interaction flow during runtime.

You can review the :doc:`Open edX Filters <openedx-filters:index>` documentation for more information on :doc:`creating filters <openedx-filters:how-tos/create-a-new-filter>` and :doc:`implement pipeline steps to use them <openedx-filters:how-tos/create-a-pipeline-step>` in your project. This documentation includes a list of :doc:`openedx-filters:reference/filters` and much more.

Still Deciding Which to Use?
----------------------------

If you're still unsure whether to use an Open edX Event or Filter, ask yourself the following questions:

**Does it change the default platform behavior?**

- **Yes:** For example, the course enrollment process now depends on a third-party subscription service. This modifies the default enrollment process.
- **No:** For example, when generating certificates, you may need to create credentials in an external service, but the default process remains unchanged.

Filters are useful when you need an immediate response that directly modifies the caller process and impacts the rest of the flow. In contrast, events are more decoupled from the caller process. They do not return a response, leaving the caller process unchanged.

**If the answer yes, should it be a filter? Does the application behavior benefit from being altered?**

- If so, a filter may suit your needs.
- If not, maybe because your use case should be the default offering of the platform, contribute changes if they benefit the community, but consider submitting a `Product Proposal`_ to begin discussing changes to the default offering.
- If the latter is not the case, then implementing your feature in a plugin using filters is the way to go.
- Next, review existing :doc:`openedx-filters:reference/real-life-use-cases` to find similar implementations.

**If the answer is no, should it be an event?**

- Consider if your use case involves communication, synchronization, or integration between services or components.
- Next, review existing :doc:`openedx-events:reference/real-life-use-cases` to find similar implementations.

We encourage you to review the list of use cases for events and filters to draw inspiration from real-life scenarios and see if your use case aligns with any of them. Also, maybe your feature can be implementing using the framework but there's not an available event or filter for it yet. In that case, consider proposing a new event or filter to the community!

The Framework vs Forking the Open edX Platform
**********************************************

The Hooks Extension Framework is designed to provide a stable and maintainable way to extend the Open edX platform without modifying its core. This approach stands in opposition to the practice of forking, which involves creating a separate version that diverges from the core codebase. Here is a comparison table of the two approaches:

+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                                                                    | **Open edX Events and Filters**                                                                               | **Forking**                                                                                                                        |
+====================================================================+===============================================================================================================+====================================================================================================================================+
| **Purpose**                                                        | Allow extending functionality of the Open edX platform without modifying the                                  | Modify the code directly to meet specific needs.                                                                                   |
|                                                                    | core codebase by leveraging plugins and configurations.                                                       |                                                                                                                                    |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| **Advantages**                                                     | - More decoupled implementations.                                                                             | - Full control of the platform behavior.                                                                                           |
|                                                                    | - Decreased maintenance burden of the platform, maintenance efforts are centered on plugins.                  | - No restrictions from what can be changed.                                                                                        |
|                                                                    | - Enables reusable behavior across the ecosystem and community.                                               | - Suitable for extremely customized use cases.                                                                                     |
|                                                                    | - Enables configurable behavior across the platform.                                                          |                                                                                                                                    |
|                                                                    | - Easier to maintain long-term due to backward compatibility and versioning policies.                         |                                                                                                                                    |
|                                                                    | - Easier to test due to more contained implementations.                                                       |                                                                                                                                    |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| **Disadvantages**                                                  | - Can increase complexity in debugging and maintenance because it adds more processing layers.                | - Separation from the separation from the upstream project makes long-term maintenance challenging.                                |
|                                                                    | - Limited by existing events and filters available in the Open edX ecosystem, although new events and         | - High maintenance burden for upgrades and compatibility.                                                                          |
|                                                                    |   filters can be proposed and added to the framework.                                                         | - Requires manual integration with the Open edX platform for each new release.                                                     |
|                                                                    | - Might increase complexity in plugins for highly customized features.                                        | - Not being able to be reused by the community.                                                                                    |
|                                                                    | - Although it is not recommended to do so, a plugin developer might introduce an edx-platform dependency,     | - Difficult to test in isolation due to highly coupled implementations.                                                            |
|                                                                    |   mainly when using filters, when there is no alternative for getting certain types of data.                  |                                                                                                                                    |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| **Community Compatibility**                                        | High, as the community encourages reusable implementations and the contribution of new extension points.      | Low, as changes in forks are usually extremely customized not designed for others to reuse. Also,                                  |
|                                                                    |                                                                                                               | community discoverability is low when changes are kept in a fork, making it harder to share and collaborate.                       |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| **Implementation Effort**                                          | Low to medium, depending on the complexity of the receiver logic and filter pipelines.                        | High, as modifications require expertise in the platform and increases technical debt. Also, changes may require additional testing|
|                                                                    |                                                                                                               | and monitoring to ensure integration compatibility with the Open edX platform.                                                     |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| **Upgrade Compatibility**                                          | High, due to backward compatibility policies.                                                                 | Low, as forks must manually integrate their changes with the Open edX platform for each new release.                               |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

When implementing a new feature, look into how the Hooks Extension Framework can help you extend the platform before considering forking the Open edX platform. You should consider the advantages and disadvantages of each approach to determine the best fit for your use case and long-term goals.

.. note:: If you think your feature should be part of the core instead of an extension, consider making a `Product Proposal`_.

Contribute to the Hooks Extension Framework
*******************************************

Before considering contributing to the framework, we suggest you make a quick proposal with your use case and intended solution, and share it with the community to gather feedback and validate the approach. This can be done in the Open edX Discuss forum or in each repository's issue tracker.

If you're new to contributing to the Hooks Extension Framework, we recommend also reading the :doc:`openedx-events <openedx-events:index>` and :doc:`openedx-filters <openedx-filters:index>` documentation to understand each hook concepts and how to use them in your project.

After choosing between an event or filter based on your use case, you can start integrating the framework into your solution. You can find the list of available events and filters that work out-of-the-box in :doc:`openedx-events:reference/events` and :doc:`openedx-filters:reference/filters` corresponding documentation. If you have a use case that doesn't fit any existing hook, consider proposing a new one to the community.

.. note:: if your use case is too specific to your organization, consider making your definitions organization-scoped by implementing them in your project. However, if you believe your use case can benefit the community, consider proposing a new event or filter to the community.

Here's an overview of the steps that usually take place when contributing to the Hooks Extension Framework:

.. TODO: Reference new documentation for creating long-term Open edX Events and Filters contributions, but for the time being reference what's available in the openedx-events and openedx-filters repositories.

#. When contributing a hook, either an event or filter, you will need to interact with at least two repositories during the implementation: the hook repository (openedx-events or openedx-filters) and the service repository (edx-platform (LMS/CMS), credentials, etc.) where the hook will be used. This is done this way due to the design of the framework, implemented across two lightweight libraries that can be installed independently (see ADR: :doc:`openedx-events:decisions/0001-purpose-of-this-repo` for more details) in the service repositories where definitions are used.
#. For implementing the hook and integrate it into a service, follow the instructions in the guide specific to each repository for :doc:`creating events <openedx-events:how-tos/create-a-new-event>` and :doc:`filters <openedx-filters:how-tos/create-a-new-filter>`.
#. For using the hook and validate its functionality, follow the instructions in the relevant repository for :doc:`consuming events <openedx-events:how-tos/consume-an-event>` and :doc:`implement pipeline steps for filters <openedx-filters:how-tos/create-a-pipeline-step>`.
#. We recommend validating the previous steps simultaneously to ensure the implementations in both the hooks repository and the service align properly. The validation process might also include the implementation of an extension, e.g., a plugin, that uses the new hook to ensure it works as expected.
#. Once you've validated both implementations, you can open the Pull Requests for review. Typically, the Pull Request for the hook definition (in `openedx-events`_ or `openedx-filters`_) is opened first, along with a simultaneous PR in the service. While managing two Pull Requests at the same time might be challenging, it's recommended to avoid rework by validating definitions early, like ensuring the filter arguments are objects available during execution, verifying the event payload can be populated with the available information, that the hook name fits the context where it will be used, etc.
#. At this point you can actively involve the maintainers of the respective repositories. The framework maintainers would help you verify that the definitions are accurate and follow the repository guidelines, they should also take a look at the service repository Pull Request to ensure the hook is consistent with the service's context and the intended use case.
#. Once the review process is complete, the Pull Request will be merged, followed by a GitHub and Pypi release of either the `openedx-events`_ or `openedx-filters`_ library.
#. After the release, include the new version of the libraries in your Pull Request for the service repository. This ensures that the repository is using the latest version of the library, which includes the new hook definition.
#. Finally, the service repository Pull Request will be reviewed and merged by maintainers, completing the integration of the new hook.

By following these steps, you can start contributing to the Hooks Extension Framework and help extend the Open edX platform in a maintainable way.

For more specifics about Open edX Events and Filters, please visit the :doc:`openedx-events <openedx-events:index>` and :doc:`openedx-filters <openedx-filters:index>` documentation.

.. _openedx-filters: https://github.com/openedx/openedx-filters
.. _openedx-events: https://github.com/openedx/openedx-events
.. _Django signals: https://docs.djangoproject.com/en/4.2/topics/signals/
.. _Product Proposal: https://openedx.atlassian.net/wiki/spaces/COMM/pages/3875962884/How+to+submit+an+open+source+contribution+for+Product+Review
.. _attrs: https://www.attrs.org/en/stable/

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Reviewer                      |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|2025-02-10    | María Grimaldi                |   Sumac        |  Pass                          |
+--------------+-------------------------------+----------------+--------------------------------+
