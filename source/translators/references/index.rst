Translators: Reference
######################

.. contents:: Translation Reference Materials
   :local:
   :class: no-bullets

.. _translators reference html:

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

.. _translators reference placeholders:

Placeholders
************

Curly Brace Placeholders
========================

**Source String**:

.. code-block::

   Welcome back {student_name}! Today is {month} {day}.

**Good Translation**:

It's okay to re-arrange the placeholders as long as you don't change them.

.. code-block::

   ¡Bienvenido {student_name}! Hoy es {day} de {month}.

**Bad Translations**:

.. list-table::
   :header-rows: 1

   * - Translation
     - Reason it's Bad

   * - ``¡Bienvenido {nombre de estudiente}! Hoy es {dia} de {mes}.``
     - Do not translate the placeholder string. You must use ``{student_name}``,
       ``{day}`` and ``{month}`` exactly as they are in the source string.

   * - ``¡Bienvenido {student-name}! Hoy es {day} de {month}.``
     - Do not alter the placeholder string punctuation. You must use
       ``{student_name}`` exactly as is.

   * - ``¡Bienvenido {Student_Name}! Hoy es {Day} de {Month}.``
     - Do not alter the placeholder string capitalization. You must use
       ``{student_name}``, ``{day}`` and ``{month}`` exactly as they are in the
       source string.

   * - ``¡Bienvenido { student_name }! Hoy es { day } de { month }.``
     - Do not add additional spacing inside the {}. You must use
       ``{student_name}``, ``{day}`` and ``{month}`` exactly as they are in the
       source string.

Percent Parenthesis Placeholders
================================

**Source String**:

.. code-block::

   Welcome back %(student_name)s! Today is %(month)s %(day)d.

**Good Translation**:

It's okay to re-arrange the placeholders as long as you don't change them.

.. code-block::

   ¡Bienvenido %(student_name)s! Hoy es %(day)d de $(month)s.

**Bad Translations**:

.. list-table::
   :header-rows: 1

   * - Translation
     - Reason it's Bad

   * - ``¡Bienvenido %(nombre de estudiente)s! Hoy es %(dia)d de %(mes)s.``
     - Do not translate the placeholder string. You must use
       ``%(student_name)s``, ``%(day)d`` and ``%(month)s`` exactly as they are
       in the source string.

   * - ``¡Bienvenido %(student-name)s! Hoy es %(day)d de %(month)s.``
     - Do not alter the placeholder string punctuation. You must use
       ``%(student_name)s`` exactly as is.

   * - ``¡Bienvenido %(Student_Name)s! Hoy es %(Day)d de %(Month)s.``
     - Do not alter the placeholder string capitalization. You must use
       ``%(student_name)s``, ``%(day)d`` and ``%(month)s`` exactly as they are
       in the source string.

   * - ``¡Bienvenido %( student_name )s! Hoy es %( day )d de %( month )s.``
     - Do not add additional spacing inside the %()s. You must use
       ``%(student_name)s``, ``%(day)d`` and ``%(month)s`` exactly as they are
       in the source string.

   * - ``¡Bienvenido (student_name)! Hoy es %(day)d de %(month)s.``
     - Do not remove the ``%`` or ``s``. You must use ``%(student_name)``
       exactly as is.

   * - ``¡Bienvenido %(student_name)s! Hoy es %(day)s de $(month)s.``
     - Do not change the character following the parenthesis. You must use
       ``%(day)d`` as is.

Angle Bracket Placeholders
==========================

**Source String**:

.. code-block::

   Welcome back <%= student_name %>! Today is <%= month %> <%= day %>.

**Good Translation**:

It's okay to re-arrange the placeholders as long as you don't change them.

.. code-block::

   ¡Bienvenido <%= student_name %>! Hoy es <%= day %> de <%= month %>.

**Bad Translations**:

.. list-table::
   :header-rows: 1

   * - Translation
     - Reason it's Bad

   * - ``¡Bienvenido <%= nombre de estudiente %>! Hoy es <%= dia %> de <%= mes %>.``
     - Do not translate the placeholder string. You must use ``<%= student_name %>``,
       ``<%= day %>`` and ``<%= month %>`` exactly as they are in the source string.

   * - ``¡Bienvenido <%= student-name %>! Hoy es <%= day %> de <%= month %>.``
     - Do not alter the placeholder string punctuation. You must use
       ``<%= student_name %>`` exactly as is.

   * - ``¡Bienvenido <%= Student_Name %>! Hoy es <%= Day %> de <%= Month %>.``
     - Do not alter the placeholder string capitalization. You must use
       ``<%= student_name %>``, ``<%= day %>`` and ``<%= month %>`` exactly as they are in the
       source string.

   * - ``¡Bienvenido < % =  student_name  % >! Hoy es < % =  day  % > de < % =  month  % >.``
     - Do not add additional spacing inside the <%=  %>. You must use
       ``<%= student_name %>``, ``<%= day %>`` and ``<%= month %>`` exactly as they are in the
       source string.

   * - ``¡Bienvenido <student_name>! Hoy es <day> de <month>.``
     - Do note remove or change the ``<%=`` or ``%>``. You must use ``<%=
       student_name %>``, ``<%= day %>`` and ``<%= month %>`` exactly as they
       are in the source string.
