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

Configuration
^^^^^^^^^^^^^

pycsw configuration in managed in ``geonode/settings.py``, in the ``PYCSW`` dictionary.

To adjust pycsw configuration settings, edit/update the ``PYCSW`` dictionary values as required.
GeoNode's integration of pycsw has made CSW configuration very lightweight and user-friendly,
and as a result there is minimal configuration of the pycsw endpoint in GeoNode.

pycsw also includes INSPIRE Discovery Services 3.0 support, which is enabled by default.
If you would like your GeoNode CSW INSPIRE support turned off, set the ``metadata:inspire/enabled`` key to ``false``.

.. note::

  Make sure that ``settings.SITEURL`` is correctly set and run ``python manage.py updatelayers`` whenever this value changes, as this affects pycsw's Capabilities XML and metadata download links

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
