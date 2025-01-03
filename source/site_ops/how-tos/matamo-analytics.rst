Configuring Matamo Analytics
#############################

In addition to Google Analytics the Open edX platform is flexible enough to support different analytics
tool.

In order to inject various analytics there is a provision to add them to head or body using `head-extra.html`, `body-initial.html` or
`body-extra.html`.

One needs to be using comprehensive theme in order to use these templates. More information can be found at `README.rst under themes
in edx-platform <https://github.com/openedx/edx-platform/blob/master/themes/README.rst>`_.

Let us walk you through integrating Matamo to the platform:

Matamo demands to be included under the head tag of the page hence we will be using `head-extra.html` to include the analytics
script.

1. Create `head-extra.html` file under {theme}/lms/templates/.
2. Add the script given by the platform in the file.
3. Apply the theme and we are good to go.

Note::

This will only be applied to the pages served by LMS and would not be supported by different MFEs used by the platform.
Hence, for introducing the same you need to create a custom component and put it in a slot. You can have a look at `frontend-footer-component <https://github.com/openedx/frontend-component-footer>`_.



