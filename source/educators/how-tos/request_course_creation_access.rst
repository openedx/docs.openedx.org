.. _Request Access to Create Courses:

##########################################
Request Access to Create Courses in Studio
##########################################

.. tags:: educator, how-to

On many Open edX sites, the ability to create courses is not granted to every
user automatically. Instead, new authors request course creation access, and a
site administrator reviews and grants that access. If you sign in to Studio and
do not see an option to create a new course, you most likely need to request
course creation access first.

This how-to describes how to request that access as an author. The steps that a
site administrator takes to grant your request are described in
:ref:`Grant Course Creation Access in Studio`.

.. note::
  These steps apply to sites that have the course creator group enabled (the
  ``ENABLE_CREATOR_GROUP`` setting). If your site does not use this feature, any
  signed-in user can create courses and you do not need to request access. If
  you are not sure how your site is configured, contact your administrator.

***********************************
Request Course Creation Access
***********************************

#. Sign in to Studio at the URL provided by your administrator.

#. Open the Studio home page (your **Courses** dashboard).

   If you already have course creation access, you will see the option to create
   a new course, and no request is necessary.

   If you do not yet have access, Studio displays a message explaining that you
   do not have permission to create courses, along with an option to request it.

#. Select the option to request course creation rights.

   Simply visiting the Studio home page registers your account with the site. To
   submit a request for review, you must select the request option so that your
   status changes to **pending** and your site administrator is notified.

***********************************
After You Request Access
***********************************

After you submit your request, a site administrator with staff or superuser
permissions reviews it and either grants or denies course creation access. When
your administrator changes your status, the platform sends you an email
notification.

* If your request is **granted**, return to the Studio home page. You will now
  see the option to create a new course. See :ref:`Create a New Course` to get
  started.

* If your request is **denied**, or if you do not receive a response, contact
  your site administrator directly. They can explain the decision or, for
  example, tell you which organizations you are allowed to create courses under.

.. note::
  A site administrator can grant course creation access for **all
  organizations** on the site, or for one or more **specific organizations**. If
  you are granted access to specific organizations only, you will be able to
  create courses under those organizations but not others.

.. seealso::

  :ref:`Grant Course Creation Access in Studio` (how-to, for administrators)

  :ref:`Create a New Course` (how-to)

  :ref:`Re-Run a Course <Re Run a Course>` (how-to)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
