.. _theme:

Theming your GeoNode Project
============================

There are a range of options available to you if you want to change the default look and feel or theme of GeoNode. Since GeoNode's style is based on bootstrap you will be able to make use of all that bootstrap has to offer as you customize the theme of your GeoNode. You should consult bootstrap's documentation as your primary guide once you are familiar with how Geonode implements bootstrap and how you can override GeoNode's theme in your own project.

Logos and Graphics
------------------

GeoNode intentionally does not include a large number of graphics files to drive its interface. this keeps browser loading times to a minimum and makes for a more responsive interface. That said, you are free to customize your GeoNode's interface by simply changing the default logo, or by adding your own images and graphics to deliver a GeoNode experience the way you envision int.

Your GeoNode project has a directory already setup for you to store your own images at my_geonode/static/img You should place any image files that you intend to use for your project in this directory.

Lets walk through an example of the steps necessary to change the default logo. 

#. Change directories into the img directory::

    $ cd my_geonode/static/img

#. Grab your logo image from the web using wget. This is just an example, you will need to Change this URL to match the location of your file or copy it to this location from somewhere else on disk or your network::

    $ wget http://www2.sta.uwi.edu/~anikov/UWI-logo.JPG 
    $ cd ../../..

#. Override the css that displays the logo by editing my_geonode/static/css/site_base.css with your favorite editor and adding the following lines::

    .nav-logo {
        width: 373px;
        height: 79px;
        background: url(../img/UWI-logo.JPG) no-repeat;
    }

You will need to update the width, height and url to match the specifications of your own image.

#. Restart your GeoNode project and look at the page in your browser::

    $ python manage.py runserver

Visit your site at http://localhost:8000/ or the remote URL for your site.

    .. figure:: img/logo_override.png

You can see that the header has been expanded to fit you graphic. In the following sections you will learn how to customize this header to make it look and work the way you want.


.. note:: You should commit these changes to your git repository as you progress through this section, and get in the habit of committing early and often so that you and others can track your project on github. Making many atomic commits and staying in sync with a remote repository (i.e. on GitHub) makes it easier to collaborate with others on your project.

Cascading Style Sheets
----------------------

In the last section you already learned how to override GeoNode's default css rules to include your own logo. You are able to customize any aspect of GeoNode's appearance this way. In the last screenshot, you saw that the main Hero are in the homepage is now covered up by the expanded header. 

First, Lets walk through the steps necessary to displace it downward so it is no longer hidden. 

#. Reopen my_geonode/static/css/site_base.css in your editor and add the following rule after the one we added in the previous step::

    .content-wrap {
        margin: 75px 75px;
    }

#. Restart the development server and reload the page::

    .. figure:: img/content_wrap_fixed.png


Templates and Static Pages
--------------------------

Other Theming Options
---------------------

Bootswatch
~~~~~~~~~~

