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
failure - to any CSW implementation and a switch to default usage of pycsw which has shown significant benefits.
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

</pre>

We have also moved to more complete and consistent usage of the django signals framework / design pattern (layers, maps, catalogue). It is now possible to run a GeoNode without a CSW catalogue at all (the current default configuration in dev mode is enabled with pycsw), all data is stored in GeoNode’s internal database, synced with external systems (GeoServer, GeoNetwork, ElasticSearch etc) via the layers and catalogue modules with pre and post_save signals. 

Additionally, the Link Class and Manager were introduced in the layers module to store the links available for each layer in Django’s own database rather than accessing this via gsconfig.py calls each time the layer page was loaded. 

## Refactor of Setup/Build/Package/Deploy

## Testing

*****THIS NEEDS TO BE REWORDED FROM AN EMAIL TO THE GEONODE-DEV LIST*****

After some struggles getting the new csw tests to run, we've finally got jenkins back happily building and testing the dev branch. You can see that here. http://geonode-testing.dev.opengeo.org:8090/job/geonode-dev/ I realize that some of you cant get to that port at your place of employ (thinking of you Ariel).

So, a quick summary, in the dev branch we now have about 90 tests spread across the smoke, unit, integration and csw suites. We are at ~75% line coverage (combined), and unfortunately in _very_ bad shape on the pep8 and pylint violations. The unit tests results for the geoserver-geonode-ext module and the javascript tests are not included yet, this is strictly the python part of the codebase. You can see the newest set of javascript tests (not yet in dev) here http://opendri.dev.opengeo.org/static/script/test.html

Should note that the original work to merge the integration tests into the main repo was done originally as part of GNIP-3

Nathan Wang (who is interning at OpenGeo while working on his dissertation this fall) is going to be continuing his excellent work on adding tests in our core modules focusing on geonode.catalogue.backends.generic and geonode.layers.management.commands in the short term and on other places lacking coverage in the medium term. We should hope to get up over 85% in the next several weeks and towards essentially full coverage before we put out a 2.0 beta this fall (which starts today in fact).

For new devs, its a really useful and beneficial to you and the project to spend time on the pylint and pep8 violations and fix them while reading through the code. There are some violations that are more difficult to tackle than others, but many that are very easy. Seems like submitting a pull request for one file of improvements at a time might work best. You can run pep8 and pylint locally before you push and send a PR. The Jenkins interface makes it really easy to switch between a terminal and a browser while you are fixing things. 

We want to bend the curve downward in the violations graph and upward in the coverage graph.

For more experienced devs, we already recognize that some of the existing tests are not as optimal as they should be and may not test every corner or edge case. If any of you want to take the time to review an existing test, amend it in anyway or simply verify that it is indeed a quality and complete test and denote that somehow, that is also super useful. 

Maybe if we did a 1 week testing challenge in October, where we challenged new devs to take on doing a bit of pylint and pep8 cleanup each day and more experienced devs taking on one existing test each day for a week. We could probably dramatically improve the test suites, our coverage, and our code quality. If that sounds interesting to you. I setup a poll on doodle where you can indicate which 5 day week might work for you. http://doodle.com/zy25tsc7dvep4983 (fwiw, I would like to do these kind of challenge weeks through the fall, focusing on things like documentation [user, dev, admin] and of course bug fixing).

There has been discussion about submitting incoming commits and pull requests to automated testing to see if they reduce (or improve!) aggregate test coverage and if they introduce new violations. Before we setup a policy to reject those outright, lets at least get the infrastructure in place such that we can see readily see that. Travis-CI apparently has a really nice interface for doing this, there has been some discussion about setting up a secondary test server there which could also be another externally hosted community resource.

There has also been discussion about setting up continuous deployments from this jenkins such that we leave an instance running after a successful build and redeploy it nightly to wipe out any new data and reload the sample data from the gisdata repo. The current setup already does leave a geonode running, but its currently against master, and appears to be pretty broken (there is a todo list item for this, see below). The goal here would be to setup a deployment for both the dev and master branches, and leave the demo server for actual releases (looks like it needs to be updated with 1.2b2).

In this vein, we have also long discussed setting up a set of black-box api tests that can test a site _only_ using HTTP (the current integration tests partially do this, but also use the internal methods). Ivan Willig has started on this, and there is certainly more work to be done as we eventually work to formalize what is now the ad-hoc API. The goal would be to be able to deploy a geonode site from packages (onto amazon or other virtual infrastructure) then run these kinds of black-box tests against that to be sure that its working well. People who deploy geonode sites would be able to use this same suite of tests to test their own deployments in a systematic way. I know this is near and dear to Ariel's heart since he has deployed more geonode sites than anyone else.

So, to that end, I've setup a trello board with a whole bunch of new tasks on this front. You can see it here.https://trello.com/board/geonode-ci/505cdc32557d2c4f49517d88  It's open for public read, but let me know if you want to comment or add/modify items and I can add you with your email address.

One quick semi-related note, I have my own opendri-branch deployed to http://opendri.dev.opengeo.org that is an integration branch that includes _all_ the current work that is going on in geonode land, including recent work that Eldarion is doing on the UI/UX, work on the new uploader/importer, work on portals, work on search and various other tidbits. I will be keeping it up to date over the next weeks and months as we continue all this work, and its _the_ place to go if you want to see whats 'next' in geonode. There are certainly many things that are broken here, some due to the integration of branches, some are still broken and being worked on in their own branches that are not ready yet for pull requests. But its a basically functional site you can check out. Let me know privately if you want credentials so you can play with it.

## GeoServer Integration

## Importer/Uploader

## Catalogue (CS-W)

## Search

## UI/UX

Significant effort has gone into completely reworking GeoNode’s User Interface and the User experience and interactions around it. Based on feedback from the initial GeoNode User Survey and input from key stakeholders, an initial set of wireframes developed by our colleagues at SpatialDev. These were circulated on the geonode-dev list a few months back, and based on feedback received on them and from interim reviews of the designs developed, further work was done to produce a set of designs that reflects the current functionality and some functionality that is intended to be merged in before the 2.0 release. 

After implementing this set of designs, both in person and remote user tests are planned to evaluate how they work for our various sets of users. There were a large number of people to asked to be included in user testing when we originally circulated the GeoNode User Survey, and anyone else who is interested is welcome to participate in this process.

Some initial refactoring of the organization and structure templates was done per GNIP-2. The repository now has a set of top level templates, a set of includes. The templates for layers & maps are located in their own app directories so as to make these apps more reusable in the normal django project structure of reusable apps. Additional renaming of templates and inclusion and use of template tags/snippets is being currently worked on in the design branch (layers and maps) These changes will be merged from the design branch into the dev branch in the next few weeks.

A critical part of the UI refactoring process has been the switch to using twitter’s Bootstrap css library per GNIP-28, and the use of Jquery for most javascript functionality in the template pages. Ext and GeoExt are now used primarily in the Map Composer although there are a few pages still using Ext as the switch to jquery is complete. More about the Map Composer, geonode-client and GeoExplorer in a subsequent mail.

A Design Review Site has been setup that is to be used for implementers of geonode and other stakeholders to review the design and user interaction of the site. The site is broken down granularly per page of functionality and each page will be annotated with information about the expected interactions on each page and how these work in different browsers or in different states on the site. You can request access to collaborate (comment, edit, update) with the development team on this site by posting to the geonode-dev list initially.

The design branch is where current is where current work is being done in the implementation of the designs. It is partially useable now, and anyone is certainly welcome to pull it and give it a spin. It may make sense to start filing tickets against this implementation in the issue tracker, but it may be better to just discuss on the list for now.

OpenGeo has a UI development site setup that will be used for both remote and in person User Testing in the coming months. It will keep up to date with changes with the design branch, but the data will be reset on a regular basis.

A user testing group has been setup which will be used as a mailing list designed to coordinate with participants in the user testing process. You welcome to join. For now it is setup as broadcast only, it may be a good idea to setup a separate list for discussion, but geonode-dev can also be used for that purpose.

The longer term goal is to build this into a collaborative community process that is iterative:
  * review designs on design site, discuss there with other implementers and stakeholders
  * rework designs based on consensus among comments in the review site
  * update the design review site with modified wireframes, mockups, design, annotation and screenshots
  * implement the revised designs in a branch
  * send pull requests with revised implementation
  * test with user participants (remote and in person)
  * collect user participant feedback and summarize on design review site
  * rinse and repeat

## GeoExplorer (GeoNode Client)

## Workspaces/Portals/Virtual Services

## Social

## Printing

## Template Projects

## Localization

## Monitoring/Analytics
