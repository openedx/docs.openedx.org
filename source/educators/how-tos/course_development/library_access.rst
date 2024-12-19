.. _Give Other Users Access to Your Library:

<<<<<<< Updated upstream
=======
##############################################
Give Other Users Access to Your Legacy Library
##############################################

>>>>>>> Stashed changes
.. tags:: educator, how-to

.. warning::

   The Legacy Libraries feature will be supported through Teak, moving to
   unsupported in Ulmo. Teak will include a one-click migration feature that
   will make it easy to convert a Legacy Library into the new Library interface.

   See :doc:`/community/release_notes/sumac/content_libraries_redesign_beta` for
   more information.

When you create a library, you are automatically assigned an Admin role in that
library.

You can give other Studio users access to your library. Depending on the level
of access  that you give them in the library, additional library users can view
and use library content in courses, edit library content, or add and manage
other library users. All users to whom you give library access must be
registered with Studio and have an active account.

These are the levels of access for libraries.

* **User** -- Users can view library content and can use library components in
  their courses, but they cannot edit the contents of a library.

* **Staff** -- Staff can use library components in their courses. In addition,
  as content co-authors, they have full editing privileges in a library.

* **Admin** -- Admins have full editing privileges for a library. In addition,
  they can add and remove other team members from library access. There must be
  at least one user with Admin privileges in a library.

.. note:: The levels of access for libraries are hierarchical. You can add new
   library members only with the **User** level of access, after which you can
   give them the **Staff** level of access. You can give the **Admin** level of
   access only to people who already have the **Staff** level of access.

<<<<<<< Updated upstream
=======

*************************
Add a User to the Library
*************************

>>>>>>> Stashed changes
To grant a user initial **User** access to a library, follow these steps.

.. note:: Only library users with the **Admin** level of access can add users
   to the library.

#. Ensure that the new library member has an active Studio account.

#. On the Studio home page, select the **Libraries** tab and locate the library
   to which you are adding this user.

#. From the **Settings** menu select **User Access**.

#. On the **User Access** page, select **Add a New User**.

#. Enter the new user's email address, then select **ADD USER**.

   The new user is added to the list of library members with the **User** level
   of access.

<<<<<<< Updated upstream
=======
******************************
Remove a User from the Library
******************************

>>>>>>> Stashed changes
You can remove users from the library at any time, regardless of the level of
access that they have.

To remove a user from the library, follow these steps.

#. In Studio, select the **Libraries** tab and locate your library.

#. From the **Settings** menu select **User Access**.

#. On the **User Access** page, locate the user that you want to remove.

#. Hover over the user's box and select the trash can icon.

   You are prompted to confirm the deletion.

#. Select **Delete**.

  The user is removed from the library.

<<<<<<< Updated upstream
=======

*************************
Add Staff or Admin Access
*************************

>>>>>>> Stashed changes
The levels of access for libraries are hierarchical. You can add new library
members only with the **User** level of access, after which you can give them
the **Staff** level of access. You can give the **Admin** level of access only
to people who already have the **Staff** level of access.

To give a library member a higher level of access to the library, follow these
steps.

#. In Studio, select the **Libraries** tab and locate your library.

#. From the **Settings** menu select **User Access**.

#. On the **User Access** page, locate the user to whom you are giving
   additional privileges.

  - If he currently has **User** access, select **Add Staff Access**.
  - If he currently has **Staff** access, select **Add Admin Access**.

  The user's display listing is updated to indicate the new level of access. In
  addition, their listing now includes a button to remove their current level
  of access and move them back to their previous level of access. For details
  about reducing a user's level of access to a library, see :ref:`Remove Staff
  or Admin Access`.
  

<<<<<<< Updated upstream
.. _Remove Staff or Admin Access:
=======
****************************
Remove Staff or Admin Access
****************************
>>>>>>> Stashed changes

After you have granted users **Staff** or **Admin** access, you (or other
**Admin** library users) can reduce their levels of access.

To remove **Staff** or **Admin** access from a library user, follow these
steps.

#. In Studio, select the **Libraries** tab and locate your library.

#. From the **Settings** menu select **User Access**.

#. On the **User Access** page, locate the user whose access level you are
   changing.

  - If she currently has **Staff** access, select **Remove Staff Access**.
  - If she currently has **Admin** access, select **Remove Admin Access**.

   The user's display listing is updated to indicate the new role.

.. note:: There must always be at least one Admin for a library. If there is
   only one user with the Admin role, you cannot remove him or her from the
   Admin role unless you first assign another user to the Admin role.


.. seealso::
 :class: dropdown

 :doc:`/community/release_notes/sumac/content_libraries_redesign_beta`

 :ref:`Content Libraries Overview` (concept)

 :ref:`Create a New Library` (how to)

 :ref:`Exporting and Importing a Library` (how to)