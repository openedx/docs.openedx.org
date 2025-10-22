.. _In-Context Analytics:

View In-Context Analytics in Studio
######################################

.. tags:: educator, how-to

In-Context Analytics introduces a new frontend plugin slot that can be used with
Aspects, customized to display metrics from other systems. 

#.  After enabling, users will see a new Analytics button at the top of the page on
    Course Outline and Unit pages. 

    .. image:: /_images/release_notes/teak/in-context-analyticsbutton.png
        :alt: A screenshot of the course outline page in Studio, highlighting the "Analytics" button in the top context menu

#.  Click the Analytics button to open an easy-to-access, easy-to-collapse sidebar
    in Studio that displays content engagement and performance data alongside the
    course outline, problem, and video components.

    .. image:: /_images/release_notes/teak/in-context-highlevelengagementcharts.png
        :alt: A screenshot of the analytics sidebar, showing subsection, problem, and video engagement bar graphs

#.  Select the subsection or component of interest (scroll to the menu beneath the 
    engagement charts) to drill in to view more detailed data about a single graded 
    subsection, problem, or video.

    .. image:: /_images/release_notes/teak/in-context-subprobvid.png

#.  Select a graded subsection component to view the number of respondents in 
    each score range for the graded subsection as well as the average subsection 
    score for all learners who attempted at least one problem in the subsection. 
    The second chart shows the total number of correct and incorrect 
    responses for each problem in the subsection.
    
    .. image:: /_images/educator_how_tos/In_Context_Metrics_Graded_Subsection.png

#.  Navigate to a specific Unit. In comparison to the analytics provided on the 
    Course Outline page, the In-Context Analytics sidebar on the Unit page provides 
    more granular insight into how learners are engaging with a single course component 
    at a time. From the sidebar, users simply click on the component they want to 
    view more information about to see more detailed data for that component.

    .. image:: /_images/release_notes/teak/in-context-unitsidebar.png
        :alt: A screenshot of the analytics sidebar in the context of editing a specific unit

#.  Select a specific problem to scroll the window to that component. The sidebar
    will show the percentage of correct responses on the first problem attempt and on 
    all problem attempts, and a breakdown of initial responses for each individual
    problem in the second table.

    .. image:: /_images/release_notes/teak/in-context-problemcomponent.png
        :alt: A screenshot of the unit level analytics sidebar, showing the percentage of correct attempts and correct first attempts for a text input component

    .. note::
        The percentage of correct problem responses on the first attempt is a good indicator
        of how difficult the problem is for the learners that submitted a response for
        the problem, and whether or not a learner immediately
        understands the question being asked/can identify the correct answer to the
        question. The percentage correct on all problem attempts is an indicator of how
        well learners were able to recover from earlier incorrect responses. A higher
        percentage correct out of all problem attempts indicates that the learner is
        able to figure out the right answer with additional effort or hints. If this
        percentage is still low, the problem may be too difficult or confusing for
        learners.
        
        The second table gives course delivery teams a peak into learners' thought
        processes when they approached the problem for the first time. This breakdown
        can give course authors quick insights into exactly how learners are getting a
        problem wrong, especially for difficult problems. This data can point to course
        delivery teams to where learners are getting mixed up.

#.  Select a specific video to scroll the window to that component. The sidebar
    will show the number of unique and repeat views for a single video by 
    timestamp across the duration of the video. 

    .. image:: /_images/release_notes/teak/in-context-videocomponent.png
        :alt: A screenshot of the video editor with the in-context analytics sidebar, which shows a bar graph of unique vs repeat views in a bar graph by timestamp

    .. note::
        Timestamp ranges with a large number of repeat views should be
        reviewed as this might be an indicator that this particular section of video is
        unclear to learners.

.. seealso::
 
 :ref:`openedx-aspects:production_configuration` (how to)

 :ref:`openedx-aspects:In-Context Dashboards` (reference)

 :ref:`In-Context Analytics (Teak)` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-06-06   | Data WG                       |   Teak         |       Pass                     |
+--------------+-------------------------------+----------------+--------------------------------+
| 2025-10-21   | Data WG                       |   Ulmo         |       Pass                     |
+--------------+-------------------------------+----------------+--------------------------------+