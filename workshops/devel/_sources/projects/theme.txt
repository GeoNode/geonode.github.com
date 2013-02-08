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

   .. note: You will need to update the width, height and url to match the specifications of your own image.

#. Restart your GeoNode project and look at the page in your browser::

    $ python manage.py runserver

Visit your site at http://localhost:8000/ or the remote URL for your site.

    .. figure:: img/logo_override.png

You can see that the header has been expanded to fit you graphic. In the following sections you will learn how to customize this header to make it look and work the way you want.


.. note:: You should commit these changes to your git repository as you progress through this section, and get in the habit of committing early and often so that you and others can track your project on github. Making many atomic commits and staying in sync with a remote repository (i.e. on GitHub) makes it easier to collaborate with others on your project.

Cascading Style Sheets
----------------------

In the last section you already learned how to override GeoNode's default css rules to include your own logo. You are able to customize any aspect of GeoNode's appearance this way. In the last screenshot, you saw that the main Hero are in the homepage is now covered up by the expanded header. 

First, Lets walk through the steps necessary to displace it downward so it is no longer hidden, then lets change the background color of the header to match the color in our logo graphic.

#. Reopen my_geonode/static/css/site_base.css in your editor and add the following rule after the one we added in the previous step::

    .content-wrap {
        margin: 75px 75px;
    }

#. Add a rule to change the background color of the header to match the logo graphic we used::

    .navbar .navbar-inner {
        background: #0e60c3;
    }

#. Your projects css file should now look like this::

    .nav-logo {
        width: 373px;
        height: 79px;
        background: url(../img/UWI-logo.JPG) no-repeat;
    }

    .content-wrap {
        margin: 75px 75px;
    }

    .navbar .navbar-inner {
        background: #0e60c3;
    }

#. Restart the development server and reload the page::

    $ python manage.py runserver

   .. figure:: img/css_overrides.png

   Your GeoNode projects homepage should now look like this

.. note:: You can continue adding rules to this file to override the styles that are in geonodes base css file which is built from base.less. https://github.com/GeoNode/geonode/blob/master/geonode/static/geonode/less/base.less You may find it helpful to use your browsers development tools to inspect elements of your site that you want to override to determine which rules are already applied. You can see an example of that in the screenshot below. Another section of this workshop covers this topic in much more detail.


   .. figure:: img/inspect_element.png

   Screenshot of using Chrome's debugger to inspect the css overrides added in the previous steps.


Templates and Static Pages
--------------------------

Now that we have changed the default logo and adjusted our main content area to fit the expanded header, its time to update the content of the homepage itself. Your GeoNode project includes 2 basic templates that you will use to change the content of your pages. 

site_base.html is the basic template that all other templates inherit from and you will use it to update things like the header and navbar, site wide announcement, the footer and also to include your own javascript or other static things that are included in every page in your site. Its worth taking a look at GeoNode's base file for this on the GitHub site here. https://github.com/GeoNode/geonode/blob/master/geonode/templates/base.html You have several blocks available to you to for overriding, but since we will be revisiting this file in future sections of this workshop lets just look at it for now and leave it unmodified.

Open my_geonode/templates/site_base.html in your editor::

    {% extends "base.html" %}
    {% block extra_head %}
        <link href="{{ STATIC_URL }}css/site_base.css" rel="stylesheet"/>
    {% endblock %}

You will see that it extends from base.html which is the GeoNode template referenced above and it currently only overrides the extra_head block to include our projects site_base.css which we modified in the previous section. You can see on line 14 of GeoNodes base.html (https://github.com/GeoNode/geonode/blob/master/geonode/templates/base.html#L14) template that this block is included in an empty state and is setup specifically for you to include extra css files as your project is already setup to do.  

Now that we have looked at site_base.html, lets actually override a different template.

site_index.html is the template used to define for your GeoNode projects homepage. It extends GeoNode's default index.html template and gives you the option to override specific areas of the homepage like the hero area, but also allows you leave things like the Latest Layers and Maps and the Contribute section as they are if you want to keep them. You are of course free to override these sections if you choose and this section shows you the steps necessaryto do that below.

#. Open my_geonode/templates/site_index.html in your editor

#. Edit the h1 element on line 13 to say something other than "Welcome"::

    <h1>{% trans "UWI GeoNode" %}</h1>

#. Edit the intro paragraph to include something specific about your GeoNode project::

    <p>
        {% blocktrans %}
        UWI's GeoNode is setup for students and faculty to collaboratively
        create and share maps for their class projects. It is maintained by the
        UWI Geographical Society.
        {% endblocktrans %}
    </p>

#. Change the Getting Started link to point to another website:::

    <span>
        For more information about the UWI Geographical society, 
        <a href="http://uwigsmona.weebly.com/">visit our website</a>
    </span>

#. Add a Graphic to the hero area above the paragraph we replaced in step 3::

    <img src = 'http://uwigsmona.weebly.com/uploads/1/3/2/4/13241997/1345164334.png'>

#. Your edited site_index.html file should now look like this::

    {% extends 'index.html' %}
    {% load i18n %}
    {% load maps_tags %}
    {% load layers_tags %}
    {% load pagination_tags %}
    {% load staticfiles %}
    {% load url from future %}
    {% comment %}
    This is where you can override the hero area block. You can simply modify the content below or replace it wholesale to meet your own needs. 
    {% endcomment %}
    {% block hero %}
        <div class="hero-unit">
            <h1>{% trans "UWI GeoNode" %}</h1>
            <div class="hero-unit-content">
            <div class="intro">
                <img src = 'http://uwigsmona.weebly.com/uploads/1/3/2/4/13241997/1345164334.png'>
            <p>
                {% blocktrans %}
                UWI's GeoNode is setup for students and faculty to collaboratively
                create and share maps for their class projects. It is maintained by the
                UWI Geographical Society.
                {% endblocktrans %}
            </p>
            <span>
                For more information about the UWI Geographical society,
                <a href="http://uwigsmona.weebly.com/">visit our website</a>
            </span>
        </div>
        <div class="btns">
            <a class="btn btn-large" href="{% url "layer_browse" %}">
            {% trans "Explore Layers" %}
            </a>
            <a class="btn btn-large" href="{% url "maps_browse" %}">
            {% trans "Explore Maps" %}
            </a>
        </div>
        </div>
    </div>
    {% endblock %}

#. Restart your GeoNode project and look at the page in your browser::

    $ python manage.py runserver

Visit your site at http://localhost:8000/ or the remote URL for your site.

    .. figure:: img/homepage.png

    You can see that the homepage now includes our changes.

From here you can continue to customize your site_index.html template to suit your needs.

Other Theming Options
---------------------

Bootswatch
~~~~~~~~~~

