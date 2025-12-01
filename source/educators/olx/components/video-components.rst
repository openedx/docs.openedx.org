.. _Video Components:

#################################
Video Components in OLX
#################################

.. tags:: educator, reference

Authors can add video components to a course unit via the ``video/<video_name>.xml`` file.

.. contents::
  :local:
  :depth: 1

**********************************************
Create the XML File for a Video Component
**********************************************

To add a video component to a course, add it to the course XML tree as
follows. This is ``video/purpose_power_reach.xml`` in the olx_example_course.

.. code-block:: xml

  <video
    youtube="1.00:lVPPPpyUOR4"
    url_name="purpose_power_reach"
    display_name="The Purpose, Power and Reach of the Open edX® Platform"
    edx_video_id=""
    end_time="00:00:00"
    html5_sources="[]"
    start_time="00:00:00"
    track=""
    youtube_id_1_0="lVPPPpyUOR4"/>


Place an XML file in the ``video`` directory for each video component in the course.

The name of the XML file must match the value of the @url_name attribute of the
``video`` element in the vertical XML file.

For example, the vertical XML file uses the following format.

.. code-block:: xml

  <vertical display_name="Unit 1: Video">
    <video url_name="purpose_power_reach"/>
  </vertical>


Create the file ``video/purpose_power_reach.xml`` to define the video component.

*************************************
Video Component XML File Elements
*************************************

The root element of the XML file for the HTML component is file is ``video``.

*************************************
``video`` Element Attributes
*************************************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``display_name``
     - Required. The value that is displayed to learners as the name of the
       video component. If a ``display_name`` is not supplied, "video" will appear to learners.
   * - ``youtube``
     - The speed and 1.0 pairings for the YouTube video source (see Note below)
   * - ``youtube_id_1_0``
     - The YouTube id for the video
   * - ``download_track``
     - Whether learners can download the video track. ``true`` or ``false``.
   * - ``download_video``
     - Whether learners can download the video. ``true`` or ``false``.
   * - ``html5_sources``
     - The file path for the HTML5 version of the video.
   * - ``show_captions``
     - Whether learners can view the video captions. ``true`` or ``false``.
   * - ``start_time``
     - The HH:MM:SS value of when within the video playback should begin. Defaults to ``00:00:00``
   * - ``end_time``
     - The HH:MM:SS value of when within the video playback should end. Defaults to ``00:00:00`` (will play whole video)
   * - ``track``
     - TBD
   * - ``edx_video_id``
     - Only used on ``edx.org`` courses. Will be deprecated.

.. note::

  For historical reasons, the ``youtube`` attribute requires a speed mapping. Since YouTube introduced the
  native ability to speed up/slow down video circa 2014, the speed mapping is no longer required. However, the ``youtube``
  attribute still maps the YouTube id to the 1.0 speed as follows:

  .. code-block:: xml

    youtube="1.00:lVPPPpyUOR4"

==============================
``source`` Element
==============================

The optional ``source`` element contains the following attribute.

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``src``
     - The file path for the video file.

*************************************
Example Video Component XML File
*************************************

The following example shows an XML file for a video component.

.. code-block:: xml

  <video
    youtube="1.00:lVPPPpyUOR4"
    url_name="purpose_power_reach"
    display_name="The Purpose, Power and Reach of the Open edX® Platform"
    edx_video_id=""
    end_time="00:00:00"
    html5_sources="[]"
    start_time="00:00:00"
    track=""
    youtube_id_1_0="lVPPPpyUOR4">

    <source src="https://s3.amazonaws.com/edx-course-videos/mit-6002x/6002-Tutorial-00010_100.mov"/>
  </video>


.. seealso::

  :ref:`What is Open Learning XML?` (concept)

  :ref:`Add Video Components` (reference)

  :ref:`Example of an OLX Course` (reference)

  :ref:`Getting Started with OLX` (quickstart)

  :ref:`OLX Directory Structure` (reference)


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
