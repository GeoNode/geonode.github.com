.. _projectsintro:

Introduction to GeoNode Projects
================================

GeoNode enables you to setup a complete site by simply by installing the packages and adding your data. If instead you want to create your own project based on GeoNode, there are a several options available to you that enable you to customize the look and feel of your GeoNode site, to add additional modules that are necessary for your own use case and to integrate your GeoNode project with other external sites and services.

This module assumes that you have installed a GeoNode site with the Ubuntu Packages and that you have a working GeoNode based on that setup. If you want to follow this same methodology on a different platform or setup, you should follow this module and adapt as necessary for your desired deployment environment.

Overview
--------

GeoNode by itself is an out of the box, full featured Spatial Data Infrastructure Solution, but many GeoNode implementations require either customization of the default site, or the use of additional modules whether they be third-party Django Pluggables or modules developed by a GeoNode implementor himself. There are quite a few existing Downstream GeoNode projects some of which follow the methology described in this module. You should familiarize yourself with these projects and how and why they extend GeoNode. You should also carefully think about what customization and additional modules you need for your own GeoNode based project and research the options that are available to you. The `Django Packages`_ site is a great place to start looking for existing modules that may meet your needs.

.. _Django Packages: http://www.djangopackages.com/

Existing Downstream GeoNode Projects
------------------------------------

- Harvard Worldmap

- MapStory

- Risiko/SAFE

Django Template Projects
------------------------

GeoNode follows the django template projects paradigm introduced in Django 1.4. At a minimum, a django project consists of a settings.py file and a urls.py file and django apps are used to add specific pieces of functionality. The GeoNode development team has created a template project which contains these required files with all the GeoNode configuration you need to get up and running with your own GeoNode project. If you would like learn more about Django projects and Apps, you should consult the `Django Documentation`_

.. _Django Documentation: https://docs.djangoproject.com/en/1.4/
