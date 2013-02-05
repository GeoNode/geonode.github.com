.. _architecture:

GeoNode Architecture
====================

GeoNode and GeoServer
---------------------

- Configuration via the REST API

- Authentication and Authorization

GeoNode and PostgreSQL/PostGIS
------------------------------

- Configuration and Application Information

- Vector Data Layer Storage

GeoNode and pycsw
-----------------

GeoNode is built with pycsw embedded as the default CSW server component.

Publishing
^^^^^^^^^^

Since pycsw is embedded in GeoNode, layers published within GeoNode are automatically published
to pycsw and discoverable via CSW.  No additional configuration or actions are required to publish
layers, maps or documents to pycsw.

Discovery
^^^^^^^^^

GeoNode's CSW endpoint is deployed available at ``http://localhost:8000/catalogue/csw`` and is
available for clients to use for standards-based discovery.  See http://pycsw.org/docs/tools.html
for a list of CSW clients and tools.

Javascript in GeoNode
---------------------

- GeoExplorer

- jQuery Functionality
