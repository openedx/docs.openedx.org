.. _LTI Component settings:

LTI Component Settings
######################

.. tags:: educator, reference

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Setting
     - Description

   * - Data Sharing Notice
     - The description of the remote LTI application. If the application
       requires a username or email address, use this field to inform learners
       that their information will be forwarded to the external application.

   * - LTI Version
     - Used to select the LTI version used for the current LTI component.

   * - LTI Passport ID (LTI 1.1 only)
     - Specifies the LTI ID for the remote LTI tool provider. This value must
       match the LTI ID that you entered as part of the LTI passport string for
       the LTI tool. For more information about LTI passports, see
       :ref:`enable_lti_components`.

   * - LTI URL (LTI 1.1 only)
     - Specifies the URL of the remote LTI tool that this component launches.

   * - Launch URL (LTI 1.3 only)
     - Specifies the URL of the remote LTI tool that this component launches.
       This is sometimes called *Redirect URL* in some tools.

   * - Tool Initiate Login URL (OIDC) (LTI 1.3 only)
     - Specifies the URL of the login URL for the remote LTI tool for the
       authentication flow. This can also be called *Login URL* on some tools.

   * - Registred Redirect URL (LTI 1.3 only)
     - Enter the redirect URIs this tool is allowed to use during login
       e.g. ["https://tool.com", "https://tool_deeplink.com"]. Leave this blank to
       use the launch URL and deep linking URL by default.

   * - Deep linking (LTI 1.3 only)
     - Toggle to enable or disable LTI Advantage Deep Linking. Select **Enabled** if
       the tool supports this feature and you want to use it in this component.

   * - LTI Deep Linking Launch URL (LTI 1.3 only)
     - Specifies the URL of the remote LTI tool that this component uses to perform
       deep linking launches. If not specified by the tool, use the same URL as
       in **LTI 1.3 Tool Launch URL**.

   * - LTI Assignment and Grades (LTI 1.3 only)
     - Toggle to enable LTI Advantage Assignment and Grades services and set the
       grading model.

       Options are:

       * **Disabled** - LTI AGS service will be disabled. Use this for tools that
         don't send any grades back to the platform.

       * **Declarative (Default)** - the platform will enable LTI AGS and prepare 
         a single grade container for problems to send grades back to. Use this 
         for simple LTI problems.

       * **Programmatic** - The tool will have full control over the grading process,
         enabling it to create and edit one or more grade containers and manage the
         learner scores that will be reported to the LMS.

   * - Names & Roles (NRPS) (LTI 1.3 only)
     - Enable this to allow the tool to access the names and roles of enrolled learners,
       if the tool supports NRPS.
   
   * - Tool Publick Key Mode (LTI 1.3 only)
     - Choose how Open edX will get the tool’s public key for validating signed messages.

       Options are:

       * **Public Key** - The tool will send the public key to the LMS.
       
       * **Keyset URL** - The tool will send the keyset URL to the LMS.

   * - LTI 1.3 Tool Public Key (LTI 1.3 only)
     - The LTI 1.3 tool's public key. This is a string that starts with
       '-----BEGIN PUBLIC KEY-----' and is required so that the LMS can check if
       the messages and launch requests received have the signature from the tool.
       This is not required when doing LTI 1.3 Launches without LTI Advantage.

       This is only required if **Tool Publick Key Mode** is set to **Public Key**.

   * - Tool Keyset URL (LTI 1.3 only)
     - The URL of the tool’s JWK keyset. Open edX uses this URL to retrieve the public
       keys needed to validate signed messages.
       
       This is only required if **Tool Publick Key Mode** is set to **Keyset URL**.

   * - Display Name
     - Specifies the name of the component. This name appears as a heading
       above the problem. Unique, descriptive display names help you
       identify problems quickly and accurately for analysis.

   * - Custom Parameters
     - Sends additional parameters that are required by the remote LTI tool.
       The parameters that you send depend on the specific LTI tool you are
       using.

       Supply a key and value for each custom parameter. The key is an
       identifier for the parameter. Use the following format.

       ``{key}={value}``

       For example, an LTI tool that displays an e-book might accept a ``page``
       parameter to control which page the e-book opens to by default. The
       following example sends a ``page`` parameter to an LTI tool.

       ::

          ["page=144"]

   * - This activity is graded
     - Indicates whether the LTI component receives a numerical score from the
       remote LTI tool provider. By default, this value is set to **Ungraded**.

   * - Grade Weight
     - Specifies the number of points possible for a problem. By default, if a
       remote LTI tool provider grades the problem, the problem is worth one
       point, and a learner's score can be any value between zero and one.

       This setting is only applied if **This activity is graded** is set to **Graded**.

       For more information about problem weights and computing point scores,
       see :ref:`Problem Weight`.

   * - Accept grades after due date
     - Specifies whether third-party systems are allowed to post grades after
       the deadline. By default, this value is set to **Enabled**.

       This setting is only applied if **This activity is graded** is set to **Graded**.

   * - Share Email
     - Sends the learner's email address to the remote LTI tool.

       An LTI component will only send learners' email addresses if the **Open
       Tool in** control is set to **New Window**. When the new window
       launches, the learners are warned that if they continue, their email
       address will be shared with the LTI provider.

       By default, this setting is not available in Studio.
       See :ref:`Allow sharing PII to LTI Components` for how to enable
       (requires system administrator privileges).

   * - Share Username
     - Sends the learner's username to the remote LTI tool. This is the
       username that the learner used to register for the course.

       An LTI component will only send learners' usernames if the **Open
       Tool in** control is set to **New Window**. When the new window
       launches, the learners are warned that if they continue, their username
       will be shared with the LTI provider.

       By default, this setting is not available in Studio.
       See :ref:`Allow sharing PII to LTI Components` for how to enable
       (requires system administrator privileges).

   * - Share Full name
     - Sends the learner's full name to the remote LTI tool. This is the
       full name that the learner used to register for the course.

       An LTI component will only send learners' full names if the **Open
       Tool in** control is set to **New Window**. When the new window
       launches, the learners are warned that if they continue, their full
       name will be shared with the LTI provider.

       By default, this setting is not available in Studio.
       See :ref:`Allow sharing PII to LTI Components` for how to enable
       (requires system administrator privileges).

   * - Hide External Tool
     - Controls whether the LTI component will display the remote LTI tool on
       the course page.

       Set the value to **True** to prevent the course page from displaying the
       remote LTI tool. For example, you might use an LTI component to
       synchronize with a remote grading system. In that situation, the LTI
       component should not appear on the course page.

       Set the value to **False** to display the remote LTI tool and allow
       learners to interact with it.

   * - Open Tool in
     - Controls the way that the course page will open and display the remote
       LTI tool.

       Options are:

       * **Inline** - the LTI tool will appear directly in the course page.

       * **Modal** - the LTI tool will appear in a separate display window in
         front of the course page. The modal display window prevents learners
         from interacting with the course page until they dismiss the LTI tool.

       * **New Window** - the LTI tool will appear in a new web browser window.
         Depending on the configuration of the web browser, it may appear in a
         new tab or in a separate browser window. Learners can interact with
         both the course page and the LTI tool.

   * - Inline Height (px)
     - Specifies the on-screen height of the LTI tool in pixels.

       This setting is only applied if the **Open Tool in** is set to
       **Inline**.

   * - Modal Height (%)
     - Specifies the on-screen height of the LTI content window as a percentage
       of the visible web browser window height. Enter the percentage in whole numbers.

       This setting is only applied if the **Open Tool in** control is set
       to **Modal**.

   * - Modal Width (%)
     - Specifies the on-screen width of the LTI content window as a percentage
       of the web browser window width. Enter the percentage in whole numbers.

       This setting is only applied if the **Open Tool in** control is set
       to **Modal**.

   * - Launch Button Text
     - Enter a custom label for the button that opens the external LTI tool.

     - The button text is only displayed if the **Open Tool in** control is set
       to **Modal** or **New Window**.

.. seealso::
 
 :ref:`About the LTI Component` (concept)

 :ref:`Enable_LTI_Components` (how-to)

 :ref:`Set up an LTI 1_1 component` (how-to)

 :ref:`Set up an LTI 1_3 component` (how-to)

 :ref:`Enabling and using LTI Advantage features` (how-to)

 :ref:`Allow sharing PII to LTI Components` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
