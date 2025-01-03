
###############################################################
Use a Section from a Course independently of the Course Outline
###############################################################

.. tags:: educator, how-to

#. From the course outline in Studio, go to the visibility options of a Section.
   You will see the option “Hide in Course Outline, accessible via Link”:

     .. image:: /_images/educator_how_tos/hide_in_outline_access_link.png

#. When selected and saved, the interface indicates that this section has been
   hidden but can be accessed through its URL:

     .. image:: /_images/educator_how_tos/hide_in_outline_link_display.png

#. Clicking on the :guilabel:`Share` button enables you to copy the URL to the specific
   subsection for sharing. There are two sharing options, as the URL for a
   complete page, or as the URL to embed.

   #. The first option “Full Page” shows the content on the original page, that
      is, with the header and footer of the site:

        .. image:: /_images/educator_how_tos/hide_in_outline_share_link.png

   #. The second option “Embed Link” displays the content directly on a page
      without a header or footer. This is ideal for embedding in other places:

        .. image:: /_images/educator_how_tos/hide_in_outline_embed_link.png

#. To embed one of the hidden subsections on a page outside the course flow,
   copy the link to embed. In Studio, go to the option “Content” → “Pages &
   Resources” → “Custom pages”:

     .. image:: /_images/educator_how_tos/hide_in_outline_custom_pages.png

#. There the subsection is embedded using the URL copied previously. Keep in
   mind to adjust the height and width of the iframe using the style attribute
   with the height in pixels as required: ``style="height: 900px; width: 100%;"``:

     .. image:: /_images/educator_how_tos/hide_in_outline_embedding_the_page.png

#. In this way, the student will not see the hidden section in the course
   outline, but they will be able to access it from the page created in the
   previous step. You can test section visibility by using the masquerade
   feature in the LMS;

     .. image:: /_images/educator_how_tos/hide_in_outline_learner_view.png

.. seealso::
 :class: dropdown

 :ref: `Add Content Experiments to Your Course` (how-to)
