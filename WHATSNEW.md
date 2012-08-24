# Whats New in GeoNode 2.0

Current GeoNode development has been focused on a series of upcoming releases. The 1.x series will continue with
GeoNode 1.2, which is currently in beta. As well as on-going work towards the GeoNode 2.0 release which is a
significant focuses on stability, user interface as well as additional features. The 2.0 release is tentatively planned
for the end of 2012. The World Bank via GFDRR and the Open Data For Resilience (OpenDRI) initiative has provided
significant funding towards core development of the GeoNode platform. The World Banks commitment has been
combined with other funding sources, (including MapStory, The Australian-New Zealand Spatial Data Marketplace,
The Army Geospatial Center and OpenGeo – through internally directed resources) to advance a comprehensive
approach towards the 2.0 release.

The World Bank has funded a series of on-going improvements to the GeoNode Platform. Including improvements in the areas of:
 * User Interface/User Experience through a comprehensive evaluation and re-design process,
 * Uploader re-write to include drag and drop upload, as well as CSV and KML upload,
 * Printing capability to allow users to have high quality print and PDF outputs of maps, including the use of
templates and a re-designed User Interface.
 * Map legends to provide better aesthetics and understanding of data displayed in the system,
 * The search process to implement a more flexible search backend to allow users a more comprehensive search capability,
 * Testing through Unit and Integration Test Suite which will significantly improve stability of the platform,
 * Portals which will allow for creation of individual pages that encompass subsets of the broader GeoNode’s collection of Data and Maps to facilitate the rapid establishment of focused pages for specific groups, events or other targeted activities.
 * Documentation and Training materials to facilitate and encourage user adoption and administration of
GeoNode deployments

Significant focus has been placed on re-working various internal and back-end components of the GeoNode
platform in order to ensure stability and ease of use. These include refactoring the code structure, reworking
the metadata catalogue to abstract the need for GeoNetwork – which has been identified as a common point of
failure - to any CSW implementation and a switch to default usage of PyCSW which has shown significant benefits.
These combined with the comprehensive unit and integration test suite, which is under ongoing development, will
ensure significant improvements to stability of the GeoNode platform with the 2.0 release.

The development described above that the OpenDRI project with OpenGeo has funded encompasses a very
significant portion of the development that will form the basis of the GeoNode 2.0 release. In addition to areas
discussed above, ANZSM has funded the development of social features for the platform – such as ratings,
comments, tagging, groups, notifications, activity stream, and other features – which will be included in the 1.2
release. OpenGeo has also committed significant internal resources towards the development of the GeoNode
platform during the past six months, totaling over 800 hours, and will continue to throughout the 2.0 development
cycle. This combined effort from various parties will be able to provide significant advancement of the GeoNode
platform in the coming months.

## Codebase Refactor

The GeoNode project repository was reorganized by moving the key modules (GeoNodePy, geoserver-genode-ext and geonode-client) to the top level of the repo per GNIP-29. The core maps app/module was refactored and reorganized per GNIP-30 by splitting it into geonode.layers which provides the core layer/dataset functionality that geonode provides, geonode.maps app/module which stores and manages the configuration of gxp/openlayers based maps consisting of multiple layers (both local and remote), and the geonode.people module with provides the functionality related to storing profiles and layer metadata roles. Additionally, the geonode.core module was renamed to geonode.security per GNIP-20. CSW/Metadata functionality was moved to the geonode.catalogue module and setup using the django backends design pattern allowing GeoNode to work with different CSW backends.

The repo is now organized as below:

<pre>

https://github.com/GeoNode/geonode/tree/dev
     geonode - top level django ‘project’ with several apps below.
          layers - core layer/dataset app
          maps - core maps app
          security - granular (row level based) auth backend.
          people - profiles app (also used for organizational entities)
          catalogue - layers interaction with internal or external CS-W.
          static - static media (css, javascript, images)
          templates - base project templates and includes (includes avatar, profiles and registration)
          tests - integration tests (should eventually include javascript/client tests too)
     geonode-client - custom GeoExplorer build (the GIS tool component of GeoNode)
     geoserver-geonode-ext - custom GeoServer build
     package - packaging scripts and config files (debian, centos and eventually windows)
     docs - existing docs and build/make config

We have also moved to more complete and consistent usage of the django signals framework / design pattern (layers, maps, catalogue). It is now possible to run a GeoNode without a CSW catalogue at all (this current default configuration in dev mode), all data is stored in GeoNode’s internal database, synced with external systems (GeoServer, GeoNetwork, ElasticSearch etc) via the layers and catalogue modules with pre and post_save signals. I will ask Ariel Nunez from GFDRR to follow up on this thread and explain this a bit more and the rationale behind it.

Additionally, the Link Class and Manager were introduced in the layers module to store the links available for each layer in Django’s own database rather than accessing this via gsconfig.py calls each time the layer page was loaded. I’ll also ask Ariel to follow up and explain this a bit more.

</pre>

## Refactor of Setup/Build/Package/Deploy

## Testing

## GeoServer Integration

## Importer/Uploader

## Catalogue (CS-W)

## Search

## UI/UX

## GeoExplorer (GeoNode Client)

## Workspaces/Portals/Virtual Services

## Social

## Printing

## Template Projects

## Localization

## Monitoring/Analytics
