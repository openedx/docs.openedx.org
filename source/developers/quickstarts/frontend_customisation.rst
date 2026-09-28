.. _Frontend Customisation:

############################################
Quickstart: Customise Your Open edX Frontend
############################################

.. tags:: developer, quickstart

Setup, and customise a frontend site with multiple MFEs using the
frontend-template-site and Tutor. You will create a custom app that
adds a new route, with a custom new page, adds a new widget to the 
header slot, modifies an existing slot's layout and adds a new route
to an existing app. 

.. contents:: Contents
   :local:
   :depth: 1


Setup Your Custom Site on Tutor
-------------------------------

Clone the ``frontend-template-site``
repo `https://github.com/openedx/frontend-template-site>`_ locally.
Normally you’d treat this as a template and modify things as needed, but
for this example we’ll use most of it as-is.

To keep things simple we will use tutor to handle this. Rename this
folder to ``frontend-site`` and mount it in tutor using
``tutor mounts add /path/to/frontend-site``. After this you need to run
``tutor dev launch -I`` to get everything set up.

To see if everything is working well, check the logs using:

.. code-block:: bash

   tutor dev logs --follow --tail=100 mfe-dev

This will show the build logs of the MFE site. If you edit
``site.config.dev.tsx`` you should see activity here.

What we will do to begin with, is create a new app inside this
``frontend-site`` folder itself. In ``src/myapp`` create an ``app.ts``
file. For now all this needs to have is the following code:

.. code-block:: tsx

   import { App } from '@openedx/frontend-base';

   const app: App = {
     appId: 'org.openedx.frontend.myapp',
   };

   export default app;

Let’s import this in ``site.config.dev.tsx`` as follows:

.. code-block:: TypeScript

   import myApp from './src/myapp/app';

And then add it to the list of apps.

Currently it does nothing, but with this in place we can now begin
working on ``myapp`` and with hot reloading everything will just work!

Adding a new Route
------------------

Let’s start with something that was previously quite difficult, adding a
new route to our site.

We will add a ``/myapp`` path that will just show some dummy content.
Let’s first write this component in ``src/myapp/MyApp.tsx``, just the
following to begin with:

.. code-block:: TSX

   import { Slot } from '@openedx/frontend-base';

   const MyApp = () => (
     <Slot id="org.openedx.frontend.slot.myapp.v1">
       <div className="container-xl">
         <h1>Welcome to MyApp!</h1>
       </div>
     </Slot>
   );

   export default MyApp;

Here we’re adding a simple demo page with just some text, and we’re
wrapping it in a slot so we can modify it later.

Next, let’s attach this to a route with the following content in
``src/myapp/routes.ts``:

.. code-block:: TypeScript

   const routes = [
     {
       path: '/myapp',
       handle: {
         roles: ['org.openedx.frontend.role.myapp'],
       },
       lazy: async () => {
         const { default: Component } = await import('./MyApp');
         return { Component };
       },
     },
   ];
   export default routes;

As you can see, we are adding a route with a path of ``/myapp``. We are
having this path handle the specified role, will look into this later.
Next we’re providing an async function called ``lazy`` that loads our
new component and returns it for this path.

Now let’s add this routes to our app by importing it and adding to the
app config. Your ``app.ts`` file should now look like:

.. code-block:: TypeScript

   import { App } from '@openedx/frontend-base';
   import routes from './routes';

   const app: App = {
     appId: 'org.openedx.frontend.myapp',
     routes,
   };

   export default app;

Now if you visit http://apps.local.openedx.io:8080/myapp you will see
this new component. Notice that we automatically get the header and
footer.

A Quick Test of Provides
------------------------

Let’s now quickly see how we can use provides to customise this app. We
will use a provides config from the shell app to tell it that our app
doesn’t need a header and footer. We can do this by adding our role to
``org.openedx.frontend.provides.chromelessRoles.v1``. Here is that that
looks like:

.. code-block:: TypeScript

   import { App } from '@openedx/frontend-base';
   import routes from './routes';

   const app: App = {
     appId: 'org.openedx.frontend.myapp',
     routes,
     provides: {
       'org.openedx.frontend.provides.chromelessRoles.v1': ['org.openedx.frontend.role.myapp'],
     }
   };

   export default app;

As soon as you make this change and save, you’ll notice that the header
and footer will disappear from our page! This is because the shell app
checks for all the roles that have been added to this provides ID and if
we’re on a path that has that role it will not render the header and
footer.

Let’s delete this for now, since we need the header for what’s coming
next.

Adding a Slot to the Header
---------------------------

Let’s now add a link to our app to the header. For this we need to first
create a component for this link. Let’s create
``src/myapp/MyAppLink.tsx`` with the following:

.. code-block:: TSX

   import { Hyperlink } from '@openedx/paragon';
   import { getLinkProps, resolveRouteByRole } from '@openedx/frontend-base';

   const MyAppLink = () => {
     const myAppRoute = resolveRouteByRole('org.openedx.frontend.role.myapp');
     return myAppRoute && <Hyperlink {...getLinkProps(myAppRoute.url)}>MyApp</Hyperlink>;
   };

   export default MyAppLink;

This is a very simple component but there is some interesting things 
going on here that are worth discussing. We could have just hardcoded 
the URL, but instead, since we tagged that route with a role, we can 
use tools provided by `frontend-base` to resolve the URL, similar to how
you'd use `reverse` in Django. 

In the above code, we're use `resolveRouteByRole` to get the URL of this
role dynamically. This function also return whether this is an internal 
link within the site, or one of the external routes so you can 
potentially alter the UX based on that. 

Another tool we're using is `getLinkProps`, which generates the 
appropriate props for the link based on whether it's an internal link 
that we can navigate to without a full page refresh, or an external 
link. These would work anywhere, even in another MFE to link between 
parts of different MFEs in the same site.

Let’s add this link to the header. We’ll add a slots config to
``app.ts`` which should look like the following:

.. code-block:: TypeScript

   import { App, WidgetOperationTypes } from '@openedx/frontend-base';
   import MyAppLink from './MyAppLink';
   import routes from './routes';

   const app: App = {
     appId: 'org.openedx.frontend.myapp',
     routes,
     slots: [
       {
         slotId: 'org.openedx.frontend.slot.header.primaryLinks.v1',
         id: 'org.openedx.frontend.widget.myapp.links',
         op: WidgetOperationTypes.APPEND,
         component: MyAppLink,
         condition: {
           inactive: ['org.openedx.frontend.role.myapp'],
         },
       }
     ]
   };

   export default app;

This will seem quite familiar to you. It’s adding our new app widget to
the header’s ``primaryLinks`` slot. What’s entirely new, is the
condition field. We don’t want this link to show up if we’re already on
``myapp`` so we’re going to add an ``inactive`` condition with this role
name so that when our role is active, this slot won’t show up.

Adding a Route to an Existing app
---------------------------------

Now let’s take a slightly more complex example of adding a route to an
existing app. We’ll add a ``myapp`` route to the catalog app so you can
access it at ``catalog/courses/courseId/myapp``.

Here I’m just going to give you the code to add to
``site.config.dev.tsx`` and explain it after:

.. code-block:: TypeScript

   catalogApp.routes![0].children!.push({
     path: 'courses/:courseId/myapp',
     async lazy() {
       const { default: Component } = await import('./src/myapp/MyApp');
       return { Component };
     }
   });

Here we’re adding a child path to the existing set of routes that the
catalog app has. We use the ``!`` after ``routes`` and ``children``
because technically they can be undefined, but in this case we know they
aren’t.

This is just like the route we added earlier, except it’s now adding our
component to a path that’s under the catalog MFE’s base path. If you now
navigate to
http://apps.local.openedx.io:8080/catalog/courses/course-v1:OpenedX+DemoX+DemoCourse/myapp
you will now see the existing component but under the catalog app.

You can take this a step further and add a link to this page via a slot
in the catalog MFE. We won’t discuss that here since that’s a
straightforward case of looking up where to add the slot and adding it.

**NOTE:** In this code we’re directly modifying the ``catalogApp``
config, which isn’t ideal. A better approach would be to do this by
creating a new object with the modifications. Even so it will be a bit
fragile and dependent on the route structure of the catalogApp and need
testing with each release.

Modifying Widget Layouts
------------------------

While it’s no longer possible to use the wrap operation, Slot layouts
and layout operations are a more powerful concept. A very simple way to
understand Slot layouts is that, all slots are automatically wrapped
with another component, which its layout and the `default
layout <https://github.com/openedx/frontend-base/blob/83a17527ad253c2c7ae07e452241c5c93d042edc/runtime/slots/layout/DefaultSlotLayout.tsx>`__
is simply an empty component that returns its contents as-is.

Let’s see how we can use layout operations to change the layout of a
slot and use that to do what we normally would with a wrap operation.

Let’s first create a new layout and understand how it works. Add the
following content to ``src/myapp/MyAppLayout.tsx``:

.. code-block:: TSX

   import { useWidgets } from '@openedx/frontend-base';

   const MyAppLayout = () => {
     const widgets = useWidgets();
     return (
       <div style={{ border: '3px solid red' }}>
         {widgets}
       </div>
     );
   };

   export default MyAppLayout;

This is a very simple demo wrap operation. This layout simply adds a
thick (3px) solid red border around the component. Frontend base is
providing a React hook ``useWidgets`` that lets you interact with the
widgets added to the slot using this layout.

To use this layout, let’s update ``app.ts`` file to add a new layout
update slot:

.. code-block:: TypeScript

   import { App, LayoutOperationTypes, WidgetOperationTypes } from '@openedx/frontend-base';
   import MyAppLayout from './MyAppLayout';
   import MyAppLink from './MyAppLink';
   import routes from './routes';

   const app: App = {
     appId: 'org.openedx.frontend.myapp',
     routes,
     slots: [
       {
         slotId: 'org.openedx.frontend.slot.header.primaryLinks.v1',
         id: 'org.openedx.frontend.slot.myapp.links',
         op: WidgetOperationTypes.APPEND,
         component: MyAppLink,
         condition: {
           inactive: ['org.openedx.frontend.role.myapp'],
         },
       },
       {
         slotId: 'org.openedx.frontend.slot.myapp.v1',
         op: LayoutOperationTypes.REPLACE,
         component: MyAppLayout,
         condition: {
           authenticated: true,
         }
       },
     ]
   };

   export default app;

This is a pretty straightforward slot config, we specify a slot ID, and
set the operation as a layout replacement, specify the component that
will be used as the new layout an specify the conditions in which this
layout should be used.

The end result of the above slot config is that we’ll see a thick red
border around our component if the user is logged in, and no border if
the user is logged out.

What makes this approach more powerful is that we have a lot of
flexibility in how we place widgets using a layout. Normally each append
will just add another widget in an empty react fragment, but what if you
could swap from a flex column layout to a flex row layout to a grid
layout? Even better you can query individual widgets to arrange them in
more complex ways.

For example, if you wanted to lay elements with some widgets vertically
in a stack and other horizontally in a row, you could use
``widget.byId`` or ``widget.byRole`` to query individual widgets by
their ID or role, and then put them in any arrangement you want.

Want even more flexibility? Your layouts can have slots of their own,
which can in turn have their own layouts!

.. _Getting started: https://docs.tutor.edly.io/quickstart.html

.. seealso::

   :ref:`Tutor for MFE QS` (how-to)
       A step-by-step recipe for adding an Aside to existing XBlocks.

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
