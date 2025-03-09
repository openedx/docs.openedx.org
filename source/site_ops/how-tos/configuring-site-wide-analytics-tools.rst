Configuring Site-Wide Analytics Tools
#####################################

In addition to Google Analytics, the Open edX platform is flexible enough to support different analytics tools.

To inject various analytics, there is a provision to add them to the head or body using head-extra.html, body-initial.html, or body-extra.html.

One needs to be using the comprehensive theme to use these templates. More information can be found in the `README.rst under themes in edx-platform <https://github.com/openedx/edx-platform/blob/master/themes/README.rst>`_.

Let us walk you through integrating Matamo into the platform:

Matamo needs to be included under the head tag of the page; hence, we will use head-extra.html to include the analytics script.

#. Create the head-extra.html file under {theme}/lms/templates/.
#. Add the script provided by the platform to the file.

   For example:

   .. code-block:: html

      <!-- Matomo -->
      <script>
        var _paq = (window._paq = window._paq || []);
        /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
        _paq.push(["trackPageView"]);
        _paq.push(["enableLinkTracking"]);
        (function () {
          var u = "//analytics.demo-instance.com/";
          _paq.push(["setTrackerUrl", u + "matomo.php"]);
          _paq.push(["setSiteId", "4"]);
          var d = document,
            g = d.createElement("script"),
            s = d.getElementsByTagName("script")[0];
          g.async = true;
          g.src = u + "matomo.js";
          s.parentNode.insertBefore(g, s);
        })();
      </script>
      <!-- End Matomo Code -->

   This should be the content of html page for head-extra.html.

#. Apply the theme, and we are good to go.

Just like how Matamo is integrated we can use other analytics tools as well.

.. note::

  This will only be applied to the pages served by LMS and would not be supported by different MFEs used by the platform. Hence, to introduce the same, you need to create a custom component and put it in a slot. You can have a look at the `frontend-footer-component <https://github.com/openedx/frontend-component-footer>`_.


Maintenance Chart

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
