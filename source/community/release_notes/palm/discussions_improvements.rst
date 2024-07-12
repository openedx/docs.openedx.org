Improvements to Discussions (Palm)
##################################

In the latest Open edX release, Palm, the default Discussions tool has had a
number of incremental improvements that provide a better discussions experience.
These improvements build on the many new moderating and authoring tools launched
in the Olive Release.

What has changed? We'll cover six smaller, but still significant, changes that
have been added to Palm.

#. Comments and responses can now be sorted in reverse order. A “Product tour”
   has been added to the Discussions experience that shows off this feature to a
   user until they click “Okay”:

      .. image:: /_images/release_notes/palm/discuss1.png

 The default is “Newest first”, but that can be switched to “Oldest first”:

      .. image:: /_images/release_notes/palm/discuss2.png

#. There is also a Product Tour for a new filtering option: you can now filter by discussions with no responses.

      .. image:: /_images/release_notes/palm/discuss3.png

#. The actions menu that appears on hover on post/comment:

      .. image:: /_images/release_notes/palm/discuss4.png

   has now been made keyboard accessible. `This video`_ displays the keyboard
   navigation of the Discussions page, including selecting this actions menu.

#. Previously, topic info was only shown on posts that belong to a
   content-specific discussion topic. Now, this info is shown for course-wide
   discussion topics as well, in a “Related to” note at the bottom of the post:

      .. image:: /_images/release_notes/palm/discuss5.png

#. The Posts page has been streamlined, allowing users to see more information
   at once. This was done by increasing the content density for posts,
   responses, and comments. Stylistic changes include decreasing the font size
   for various elements, moving elements around to be inline or hidden (such as
   putting post time next to author name and hiding Like and Follow icons if
   there are no likes or follows), and changing the height of various UI
   elements.

      .. image:: /_images/release_notes/palm/discuss6.png

   Note there are no “Likes” shown in this page. Using the top right context
   menu on a post, a Like can be added and will then show on the post.

      .. image:: /_images/release_notes/palm/discuss7.png


#. The loading time of posts has been improved significantly! Previously, when
   clicking on a post, there was a delay before the post was loaded. This has
   been fixed.

How can I get this?
===================

The Discussions improvements are available as of the Open edX Palm release.
`Upgrading your local installation to Palm
<https://docs.tutor.edly.io/install.html#upgrading>`_ will guarantee that your
system is up-to-date with the latest features, including the Discussions MFE
(Micro-Front End).

.. _This video: https://user-images.githubusercontent.com/73840786/222527569-2b7da65a-8e98-4358-92d7-63b571ebcbfe.webm