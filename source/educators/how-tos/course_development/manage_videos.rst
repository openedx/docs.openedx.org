.. _Manage Video Components:

###############################
Manage Video Components
###############################

.. tags:: educator, how-to

.. contents::
  :local:
  :depth: 2

.. _Add a Video:

****************
Add a Video
****************

This is how you can add a video to a course:

.. youtube:: 9C8YTP75HpA

To add a video, follow these steps.

.. START ADD A VIDEO

#. From Studio, in the unit where you want to place the video, under **Add New Component** select :guilabel:`Video`.

   .. image:: /_images/Educators_add_video.png

   A video with default settings is added to the unit.

#. The video component opens in the visual editor.

#. In the **Component Display Name** field, click the pencil icon and enter the name that you want learners to see for this video.

   This name appears as a heading above the video in the LMS, and it identifies the video for you in reports and analytics. If you do not enter a display name, the platform specifies “video” for you.

#. Paste the video URL in the default Video URL field, and then enter the location of your video. This is the URL that was created when you uploaded the video to the hosting site.

   .. image:: /_images/Educators_video_edit.png

   .. note::
      Youtube videos can be added by pasting the Youtube URL into the Video URL field.

   .. note::
      If you have created multiple versions that use different encodings or hosting
      services, add the URL for each video by selecting **Add a vido URL** below the
      **Fallback Videos** field and enter the URL in the **Video URL** field. The first
      listed video that is compatible with the learner's device plays.

      For the best experience for mobile users, make sure that the URL for the 360p
      version of the video is the first URL in the list.

#. Optionally, you can set more options for the video. For a description of each option,
   see :ref:`Video Settings`.

#. Click :guilabel:`Save` to save the video in the unit.

.. END ADD A VIDEO

.. _Additional Video Options:

**********************************
Specify Additional Video Options
**********************************

When you create a video component, you can customize additonal settings such as
specifying download options for the video and transcript, video license options,
and a start and stop time for the video.

.. contents::
  :local:
  :depth: 2

.. _Enable Video and Transcript Downloads:

============================================
Enable Video and Transcript Downloads
============================================

You can allow learners to download videos and transcript files you have
provided so that they can view them offline.

To enable video and transcript downloads, follow these steps.

#. To allow learners to download the video, select **Allow video downloads**
   in the **Video Source** section.
#. To allow learners to download an .srt and .txt video transcript, select
   **Allow transcript downloads** in the **Transcript** section.
#. Select **Save**.

To test transcript downloads for the video, select **Download transcript** in
the video player’s control bar. You can download either the SubRip (.srt)
format or text (.txt) format.

.. _Video Settings:

============================================
Set Video Settings
============================================

.. contents::
  :local:
  :depth: 1

The following options appear on the **Edit** page of the video component.

.. list-table::
    :widths: 30 70

    * - **Component Display Name**
      - The name you want your learners to see. To edit the display name,
        select the pencil icon in the top left hand corner.

.. _Video Source:


----------------------
Video Source
----------------------

.. list-table::
    :widths: 30 70

    * - **Video ID**
      - The Video ID is the source for your video. Video IDs are the
        identifiers that the video process assigns to the video.

        .. note::
           The Video ID is an Edx.org-specific identifier, and typically not used for Open edX deployments.

    * - **Video URL**
      - The Video URL is the source for your video. Video URLS are for externally
        hosted video.

    * - **Allow Video Downloads**
      - Specifies whether learners can download the video. If you select **Allow
        video downloads**, you must add at least one URL in the **Fallback
        Videos** field.

    * - **Fallback Videos**
      - The URL or URLs where you posted different versions of the video. If you
        added URLs by selecting **Add a video URL**, the URLs are listed in the
        fields below to **Fallback Videos**.

        Every URL must end in .mp4, .mpeg, .webm, or .ogg. Learners will view
        the first listed video that is compatible with their computer or mobile
        device.

        For the best experience for mobile users, make sure that the URL for
        the 360p version of the video is the first URL in the list.

        To help make sure all standard browsers can play your video, we
        **strongly** recommend you use the .mp4 format.

.. _Thumbnail:

----------------------
Thumbnail
----------------------

.. note::
  The thumbnail is not available for videos hosted on Youtube. You can set your thumbnail for Youtube videos from Youtube if you are the owner of the video. 

.. note::
   **This feature is not available for Video components in Libraries.**

The thumbnail image is the image that learners see before the video begins to
play. For videos found on the **Video Uploads** page, the thumbnail image can be
specified. The thumbnail image should have an aspect ratio of 16:9.

To add a thumbnail to a video component, follow these steps:

#. Open the video component for the video.
#. Scroll down to the **Thumbnail** section, and then select **Upload
   Thumbnail**.
#. In the dialog box, browse to the image file, and then select **Open**.

To replace the current thumbnail, delete the thumbnail, and then follow the
steps above for adding a thumbnail

.. _Transcript:

----------------------
Transcript
----------------------

.. note::
   To test the transcript with the video, after you have saved the video, select
   **Show transcript** (”) icon in the video player's control bar. The transcript
   file scrolls while the file plays. You can also test the transcript by
   selecting the **CC** icon.

.. list-table::
    :widths: 30 70

    * - **Transcript Languages**
      - The transcript files for any additional languages. For more
        information, see :ref:`Transcripts in Additional Languages<Add a Transcript>`.

    * - **Allow Transcript Downloads**
      - Specifies whether you want to allow learners to download the .srt or
        .txt transcript. (By default, Studio creates a .txt transcript when you
        upload an .srt transcript.) If you select **Allow transcript
        downloads**, a link to download the file appears below the video.

        If you want to provide a downloadable transcript in a different format
        as well, such as .pdf, the recommendation is to upload a handout for learners by
        using the **Upload Handout** field. For more information, see
        :ref:`Additional Transcripts`.

    * - **Show Transcript in the video player by default**
      - Specifies whether the transcript appears next to the video by default.
        If this is set to **unchecked**, learners can still view transcripts by
        selecting the **Show Transcript** (”) icon.

.. _Duration:

----------------------
Duration
----------------------

.. note::
   To keep the full length of the video, both the start and stop time should be
   set to 00:00:00.

.. list-table::
    :widths: 30 70

    * - **Video Start Time**
      - The time you want the video to start if you do not want the entire
        video to play. Use HH:MM:SS format. The maximum value is 23:59:59.

        .. note::
           Learners who play video in the mobile app see the entire video file.
           Only videos that play in a browser start playing at the specified
           start time.

    * - **Video Stop Time**
      - The time you want the video to stop if you do not want the entire video
        to play. Use HH:MM:SS format. The default value is 00:00:00 if you do
        not specify an end time. 00:00:00 is equal to the end of the video. The
        maximum value is 23:59:59.

        .. note::
           Learners who play video in the mobile app see the entire video file.
           Only videos that play in a browser stop playing at the specified
           stop time.

.. _Handout:

----------------------
Handout
----------------------

.. note::
   **This feature is not available for Video components in Libraries.**

.. list-table::
    :widths: 30 70

    * - **Upload Handout**
      - Allows you to upload a handout to accompany the video, such as a PDF
        transcript or other handout. Learners can download the handout by
        selecting **Download Handout** under the video. The procedure for
        adding handouts is the same as the procedure for adding a supplemental
        transcript. For more information, see :ref:`Additional Transcripts`.

.. _License:

----------------------
License
----------------------

.. note::
   The license defaults to the license set at the course level

.. list-table::
    :widths: 30 70

    * - **License**
      - Optionally, you can set the license for the video, if you want to
        release the video with a license different from the overall course
        license.

        * Select **All Rights Reserved** to indicate to learners you own
          the copyright for the video.

        * Select **Creative Commons** to grant others the right to share and
          use the video. You must then select the Creative Commons license
          options you want.

          The license options you select control the copyright notice that
          learners see for the video. For more information, see :ref:`Guide to Course Licenses`.


.. seealso::

  :ref:`Guide to Course Video` (how-to)

  :ref:`Video Process Overview` (reference)

  :ref:`Troubleshoot Videos` (reference)

  :ref:`Video Technical Specifications` (how-to)

  :ref:`Add an In Video Quiz` (how-to)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 03/19/2025   | John (Curricu.me)             | Sumac          | Pass                           |
+--------------+-------------------------------+----------------+--------------------------------+
