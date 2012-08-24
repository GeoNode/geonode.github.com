# Current Status

  * geonode:master - built Aug 23, 2012 7:09:11 PM - [Test Results](http://geonode-testing.dev.opengeo.org:8090/job/geonode-server/)
  * geonode:dev - built Aug 23, 2012 7:16:28 PM [Test Results](http://geonode-testing.dev.opengeo.org:8090/job/geonode-dev/)
  * demo.geonode.org - [148 Layers](http://demo.geonode.org/data/search) [77 Maps](http://demo.geonode.org/maps/search)

# Overview

GeoNode is an open source web platform that facilitates the creation, sharing, and collaborative use of geospatial data. It is a powerful and flexible, user facing geospatial content management system that also provides a complete spatial data visualization and system. Built using the Django web framework and on top of GeoServer, GeoNode provides an easily installable, Open Geospatial Consortium (OGC) Compliant, Spatial Data Infrastructure (SDI). It has a simple yet highly extensible architecture that encourages diving in and working on the code and using it to develop sophisticated public facing geospatial website applications. GeoNode is GPL licensed and is supported by a diverse and active community.

Note about OGC Compliance (WMS/WFS/WCS/CSW/KML)


# Features

In addition to the general features provided by Django such as MVC architecture, ORM, templating, caching and an automatic admin interface, GeoNode provides the following functionality:

   * Spatial data import and management (Using GeoServer) [geonode.layers & geonode.import]
   * Metadata Editing and Management (pycsw or any OGC Compliant CSW Server) [geonode.catalogue]
   * Geospatial Visualization and Mapping (Using GeoExplorer GIS Tool) [geonode.maps]
   * Cartographic Styling and Product Creation (SLD) [geonode.print]
   * Full Text and Spatial Search Engine (Django Haystack and ElasticSearch) [geonode.search]
   * Social Functionality (Django Third Party modules & Pinax) [geonode.people, geonode.groups & geonode.social]
   * Geospatial Content Portals [geonode.portals]

## The GeoNode Homepage

![](https://raw.github.com/GeoNode/geonode.github.com/master/ui_design/gn-homepage.png)

## The GeoNode Admin Dashboard

![](https://raw.github.com/GeoNode/geonode.github.com/master/ui_design/gn-admin.png)

## GeoExplorer GIS Visualization and Cartography Tool

![](https://raw.github.com/GeoNode/geonode.github.com/master/ui_design/gn-geoexplorer.png)

# Community

GeoNode has active Mailing Lists for its Users and Developers. There is an IRC channel for real-time discussion and a GeoNode blog and twitter stream to provide updates about the project, interesting geonode sites and downstream projects and their users. The GeoNode development team holds regular 'hangouts' on the Google Plus network to discuss the project and its development. GeoNode 'Summits' are held on an approximately bi-annual basis as a forum for major GeoNode stakeholders to discuss their geonode implementations and collaborate on new features. These summits are supplemented by code-sprints where core developers work together in person or remotely for a set length of time, generally in order to accomplish a pre-defined set of goals.

# Dependencies

The core of GeoNode is built on top of GeoServer, several key python geospatial modules (gsconfig, owslib and pycsw) and  makes extensive use of third party django apps (modules) to provide further optional functionality. In many key modules (geonode.layers, geonode.catalogue, geonode.search), it is possible to choose from different backend engines to provide specific functionality similar to the way that django itself is able to use various database backends.

It is possible to deploy GeoNode on top of the OpenGeo suite which provides a complete, commercially supported, open source geospatial infrastructure stack built using open standards. GeoNode shares many core modules with the OpenGeo Suite, while adding a user facing website application.

GeoNode does not currently use GeoDjango, gdal, ogr, geos or shapely. Explain!

## Core Dependencies:

   * Python 2.7
   * Django 1.4
   * GeoServer 2.2
   * PostgreSQL & PostGIS
   * gsconfig (for interacting with GeoServer)
   * owslib (for interacting with OGC services)
   * pycsw 1.4.0 (for providing CSW metadata service)
   * PIL (for image processing)
   * lxml (for xml processing)
   * South (for database migrations)
   * requests (for internal and external HTTP interaction)
   * httplib (replaced in favor of requests?)

## Optional Dependencies

   * Markdown
   * beautifulsoup4
   * MultiPartPostHandler
   * Sphinx
   * gisdata
   * mock
   * pyelasticsearch
   * tastypie
   * agon-ratings
   * dialogos
   * idios
   * user_messages
   * django-registration
   * django-profiles
   * django-avatar
   * django-relationships
   * django-announcements
   * django-notification
   * django-activity-stream
   * django-taggit
   * django-extensions
   * django-forms-bootstrap
   * django-crispy-forms
   * django-hosts
   * django-nose
   * django-haystack

GeoNode is built on top of GeoServer which provides a complete OGC compliant GIS data management, editing, processing and cartographic rendering server which can interface with many different stores of geospatial (shape files and other vector file formats, geotiffs and other raster formats, postgis, oracle spatial, MSSQL server and other geospatial databases) using open standards.

GeoNode's front end is developed with django templates, bootstrap css and jQuery javascript. It is possible to use various bootstrap themes to customize GeoNode's interface, and/or to add jquery code or existing widgets to add additional javascript functionality.

GeoExplorer, the integrated GIS visualization and processing tool is developed using the OpenGeo Suite SDK which is built on top of GXP, GeoExt, ExtJS and OpenLayers.

GeoNode uses paver for setup, building, packaging and running the development server with paste and jetty and for running the tests with nose. jstools is used to assemble the compressed javascript, and fabric is used for deployment to external servers. The preferred deployment stack is apache with mod_wsgi, tomcat, postgres with postgis and celery, rabbitmq and supervisord, but it is possible to deploy in other configurations including on platforms like openshift.

Jenkins is used as a continuous integration, build and testing server.

GeoNode's documentation is developed with sphinx and is hosted by read the docs.

# Installation

If you simply want to try GeoNode, it is recommended to use Ubuntu 12.04 and install the latest stable release:
sudo add-apt-repository ppa:geonode/release
sudo apt-get update
sudo apt-get install geonode
geonode-startproject <template name>CentOS or Red Hat Enterprise Linux Installation Instructions
Windows Installation Instructions:
Installation on Other Platforms

   * Other Linux
   * Mac OSX
   * Solaris
   * BSD

# Template Projects

Geonode uses the Django concept of template projects to provide an easy way to deploy geonode sites with a common, pre-defined set of modules. The 4 template projects that GeoNode provides by default are the following:

  * minimal - provides a minimal GeoNode site (geonode.layers, geonode.security)
  * basic - minimal + import, maps, catalogue and search
  * social - basic + profiles, groups, notifications, activity stream

While these template projects account for the most common deployment situations, it is completely possible to configure and deploy a geonode site with a custom set of modules based on your specific requirements.


# Application Programming Interface (API)

GeoNode's API

GeoServer's REST Configuration API

GeoServer's GeoServices REST API

# Contributing

GeoNode is an open source software project, managed using the git distributed version control system. The source code repository, issue tracker and wiki are hosted on GitHub. Contributing is as easy as forking the project and contributing your enhancements as pull requests.

Please note the following guidelines for contributing:

   * Contributed code must be written in the existing style. This is as simple as following the Django coding style and (most importantly) PEP 8. You should also run your code through pylint to look for signs of bugs or poor code quality.
   * Contributions must be made available on a separately named branch based on the latest version of the master or dev branches.
   * You must run the existing unit and integration tests before submitting your changes. If your changes cause the tests to break, they won't be accepted.
   * If you are adding new functionality, you must include basic tests and documentation.
   * Patches that fix bugs should always be paired with an issue filed in the issue tracker, and ideally will provide a new test that demonstrates the existing problem while verifying that the patch fixes it.
   * If you intend to make changes which involve major refactoring of existing functionality or which are particularly large or far reaching improvements, you are encouraged to work through the GeoNode Improvement Proposal (GNIP) process.
You are also encouraged to file bug reports in GeoNode's issue tracker by providing as much information as you possibly can (error messages, stack trace, logfiles or excerpts) about how you encountered the problem and/or what steps can be taken to reproduce it. These details helps the developers as they try to replicate and solve the problem.

If you have a feature that you would like to request or functionality that you would like to see implemented or a change in how current functionality works, you can also file an issue for this in the issue tracker. It is advisable to provide as much information as you can about the proposed new feature or enhancement so the developers can consider it and act accordingly. If you, or your organization would like to make major contributions to the project, you are encouraged to get involved in the Roadmap and GNIP processes.

You can also contribute to the localization of GeoNode by contributing to an existing translation or starting a new one. See the section below for more information.

Contributors who regularly fix bugs or frequently make enhancements may be invited to become core committers of the GeoNode project. Core contributors are able to vote on GeoNode Improvement Proposals and have other rights and responsibilities as detailed in geonode's documentation.

# Setting up a Development Environment

Setting up a development environment generally involves the following 5 steps.

  1. Setup a virtual environment to sandbox GeoNode's python dependencies from the python packages installed systemwide. (mkvirtualenv my-geonode)
  2. Clone the git repository to your local machine. (git clone git://github.com/GeoNode/geonode.git)
  3. Run the paver command (paver setup) to install the dependencies and generally configure and setup the project.
  4. Run the unit and integration test suites to verify that everything is working correctly. (paver test and paver test_integration)
  5. Start the development server (paver start)
Full instructions on how to do this on various platforms can be found in geonode's documentation.

# GeoNode Improvement Proposals

GeoNode Improvement Proposals (GNIP) are a formal mechanism used to manage any sort of major change to GeoNode. While the definition of "major" is subject to interpretation, examples of changes which are managed by the GNIP process include:
   * Major redesign of existing features
   * Major new functionality
   * Code or build process re-architecture
   * Changes to GeoNode process or project policy
More information about the GNIP Process can be found in geonode's documentation.


# GeoNode's Roadmap Process

The GeoNode Roadmap Process is designed to complement the more technical GeoNode Improvement Proposals and strives to make it easier for the various organizations invested in GeoNode to collaborate on features of common interest. The GeoNode summits are an opportunity for major GeoNode stakeholders to discuss new features and to collaboratively lay out the projects roadmap for the coming months.

# Language Translations (Localization)

GeoNode makes full use of translation strings, which allow GeoNode to be translated into multiple languages using Django's internationalization methodology. Translations are managed on the Transifex website, but can also be submitted via GitHub. Consult Django's internationalization methodology for more information on creating translations or using them.

Currently Translations exist in the following languages. 

   * English
   * Spanish
   * German
   * French
   * Italian
   * Greek
   * Arabic
   * Indonesian
   * Chinese

# Third Party Modules

There are several external third party modules that can be used with GeoNode. 

  * geonode-documents
  * geonode-registry
  * geonode-import
  * geonode-export
  * geonode-cloud
  * geonode-themes

# Significant Projects Built on top of GeoNode

Several large downstream projects are built on top of GeoNode and provide additional functionality. Among the most significant of these are the following.

   * Harvard World map
   * MapStory
   * InaSAFE (Risiko)
   * GEM OpenQuake

#Commercial Support and Sponsored Development

OpenGeo offers Enterprise Commercial Support for GeoNode's deployed on top of the OpenGeo suite, either on premises or in the cloud. Consult their website for information and pricing.

Organizations wishing to sponsor the development of new features in GeoNode are encouraged to contact either OpenGeo or one of the following vendors to inquire about such services.

  * Your company listed here

# GPL License

GeoNode is Copyright 2010 OpenPlans.

GeoNode is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
GeoNode is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

http://www.gnu.org/licenses/
