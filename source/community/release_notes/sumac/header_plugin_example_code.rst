.. include:: customizing_header.rst
    :start-after: simple-example-start
    :end-before: simple-example-end

.. _simple_header_plugin_code:

Sample ``env.config.jsx`` code
==============================

.. code-block:: jsx

    import { PLUGIN_OPERATIONS } from '@openedx/frontend-plugin-framework';

    const config = {
        pluginSlots: {
        learning_help_slot: {
            plugins: [
            {
                op: PLUGIN_OPERATIONS.Hide,
            },
            ]
        },
        },
    }

    export default config;

.. include:: customizing_header.rst
    :start-after: medium-example-start
    :end-before: medium-example-end

.. _medium_header_plugin_code:

Sample ``env.config.jsx`` code
==============================

.. code-block:: jsx

    import { DIRECT_PLUGIN, PLUGIN_OPERATIONS } from '@openedx/frontend-plugin-framework';
    import {Helmet} from "react-helmet";

    const config = {
    pluginSlots: {
        course_info_slot: {
        keepDefault: false,
        plugins: [
            {
            op: PLUGIN_OPERATIONS.Insert,
            widget: {
                id: 'custom_course_info_component',
                type: DIRECT_PLUGIN,
                RenderWidget: ({ courseTitle }) => (
                <>
                    <Helmet>
                    <style>
                    {/*
                        styles adapted from https://codepen.io/mina-mounir/pen/gOPppdv
                        by Mina Mounir https://codepen.io/mina-mounir under MIT as per
                        CodePen public pen licensing https://blog.codepen.io/documentation/licensing/
                    */}
                    {`
                        .book {
                        margin-left: 20px;
                        width: 80px;
                        height: 120px;
                        padding: 6px;
                        background: #f3efe1;
                        border-left: 6px solid #929292;
                        transform: rotate(-45deg) skewX(10deg) scale(.8);
                        box-shadow: -10px 10px 10px rgba(0, 0, 0, 0.5);
                        }
                        .bookHeader {
                        margin: 0 0 4px 0;
                        padding: 0;
                        text-align: center;
                        font-size: 18px !important;
                        color: #716f6f;
                        }
                        .book:before {
                        content: "";
                        width: 6px;
                        height: 100%;
                        background: #848484;
                        position: absolute;
                        top: 0;
                        left: 0;
                        transform: skewY(-45deg) translate(-11.4px, -8.6px);
                        }
                        .book:after {
                        content: "";
                        width: 106%;
                        height: 6px;
                        background: #CCC;
                        position: absolute;
                        bottom: 0;
                        left: 0;
                        transform: skewX(-45deg) translate(-2.2px, 6px)
                        }
                    `}
                    </style>
                    </Helmet>
                    <div class="book">
                    <div class="bookHeader">{courseTitle}</div>
                    </div>
                </>
                ),
            },
            },
        ]
        }
    },
    }

    export default config;
    
.. include:: customizing_header.rst
    :start-after: advanced-example-start
    :end-before: advanced-example-end


**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|  2025-04-15  | FWG                           | Sumac          |   Pass                         |
+--------------+-------------------------------+----------------+--------------------------------+
