Translators Reference
#####################

HTML
****

We will use this string as an example for the advice in this section.

**Source String**:

.. code::

   If you have a general question about {platform_name} please email
   <a href="mailto:{contact_email}">{contact_email}</a>."

**Good translation**:

.. code::

   {platform_name}에 대해 일반적인 질문이 있으면
   <a href="mailto:{contact_email}">{contact_email}</a>로 이메일 주십시요."


**Bad Translations**:

.. list-table::
   :header-rows: 1

   * - Translation
     - Reason it's Bad
   * - ``{platform_name}에 대해 일반적인 질문이 있으면 {contact_email}로 이메일 주십시요.``

     - Removing tags can break platform functionality.  In the Bad translation
       the ``<a>`` tag and its content were removed.

   * - ``{platform_name}에 대해 일반적인 질문이 있으면<a href="흔한:{contact_email}">{contact_email}</a>로 이메일 주십시요.``
     - Do not translate the HTML tags. Please use the given HTML tags.

   * - ``{platform_name}에 대해 일반적인 질문이 있으면 <b>{contact_email}</b>로 이메일 주십시요.``
     - Do not change the HTML tags to something new. Please use the given HTML
       tags. Changing the html tags can alter the behavior of the platform in
       unintended ways.

   * - ``{platform_name}에 대해 일반적인 질문이 있으면 < a href = " mailto : {contact_email} " > {contact_email} < / a >로 이메일 주십시요.``
     - Do not add additional spacing to the HTML tags. Please use the given HTML tags.
