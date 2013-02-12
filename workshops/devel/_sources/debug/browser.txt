.. _browser:

Debugging GeoNode in the Browser
================================


Net Tab
-------

The net tab allows viewing all of the network traffic from the browser. The subtabs (like the selected "Images" tab) allow filtering by the type of traffic. In this screenshot, the mouse hover shows the image content and the full URL requested. One can right-click to copy-paste the URL or view in a separate tab. This is useful for obtaining test URLs. The grayed out entries show that the resource was cached via conditional-get (the 304 not modified). Other very useful advanced information includes the size of the response and the loading indicator graphics on the right. At the bottom, note the total size and timing information.

- Go to layers/maps/search pages and look at the various requests. Note
the AJAX tab. Look at the various request specific tabs: headers,
params, etc.
- Use the 'disable browser cache' option and see how it affects page
loads. Discuss advantages/challenges of caching.

.. figure:: img/firebug-net.png

Dom Tab
-------

The dom tab shows all of the top-level window objects. By drilling down, this can be a useful way to find out what's going on in a page. In this example, the mouse is hovering over the app. Note the high level view of objects and their fields. The console tab allows interacting with the objects.

- drill down in the dom tab.
- use the console to interactively exercise jquery.
- use the console to interact with the app/map or other page objects

.. figure:: img/firebug-dom.png

Script Tab
----------

The script tab allows viewing scripts and debugging. The screenshot shows a breakpoint set at line 3, the current code is stopped at line 8 and the mouse hover is showing the value of the variable 'class_list'. On the right, the 'Watch' tab shows the various variables and scopes and offers a drill down view similar to the dom view. The stack tab shows the execution stack context outside the current frame.

- step through some code, look at various features, answer questions ???
- TODO - can we build the client stuff in debug mode (aka - not minified, etc.)? How?

.. figure:: img/firebug-debug.png

HTML Tab
--------

The HTML tag allows viewing and drilling down into the DOM. The screenshot shows a search result 'article' element highlighted with padding and margin in yellow and purple. The DOM structure is shown on the left and the right panel shows the specific style rules while the computed tab shows the effective style rules. The layout tab displays rulers and property values while the DOM tab shows a debug/DOM-like view of the actual object's properties.


- identify elements, look at the various tabs, etc.
- change styles, add new rules and styles
- edit existing HTML elements via the raw and tree-view

.. figure:: img/firebug-html.png
