.. _apps:

Adding Additional Django apps to your GeoNode Project
========================================================

Since GeoNode is based on Django, your GeoNode project can be augmented and enhanced by adding additional third-party pluggable Django apps or by writing an app of your own. 

This section of the workshop will introduce you to the Django pluggable app ecosystem, and walk you through the process of writing your own app and adding a blog app to your project. 

Intro to Django Pluggable Apps
------------------------------

The Django app ecosystem provides a large number of apps that can be added to your project. Many are mature and used in many existing projects and sites, while others are under active early-stage development. Websites such as Django Packages provide an interface for discovering and comparing all the apps that can plugged in to your Django project. You will find that some can be used with very little effort on your part, and some will take more effort to integrate.

http://www.djangopackages.com/

Adding your own Django App
--------------------------

Lets walk through the an example of the set of steps necessary to create a very basic django polling app to and add it to your GeoNode project. This section is an abridged version of the Django tutorial itself and it is strongly recommended that you go through this external tutorial along with this section as it provides much more background material and a signficantly higher level of detail. You should become familiar with all of the information in the Django Tutorial as it is critical to your success as a GeoNode project developer.

Throughout this section, we will walk  through the creation of a basic poll application.

It’ll consist of two parts:

- A public site that lets people view polls and vote in them.
- An admin site that lets you add, change and delete polls.

Since we have already created our GeoNode project from a template project, we will start by creating our app structure and then adding models::

    $ python manage.py startapp polls

That'll create a directory polls, which is laid out like this::

    polls/
        __init__.py
        models.py
        tests.py
        views.py

This directory structure will house the poll application.

The first step in writing a database Web app in Django is to define your models -- essentially, your database layout, with additional metadata.

In our simple poll app, we'll create two models: polls and choices. A poll has a question and a publication date. A choice has two fields: the text of the choice and a vote tally. Each choice is associated with a poll.

These concepts are represented by simple Python classes. 

Edit the polls/models.py file so it looks like this::

    from django.db import models

    class Poll(models.Model):
        question = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
        def __unicode__(self):
            return self.question

    class Choice(models.Model):
        poll = models.ForeignKey(Poll)
        choice = models.CharField(max_length=200)
        votes = models.IntegerField()
        def __unicode__(self):
            return self.choice

That small bit of model code gives Django a lot of information. With it, Django is able to:

- Create a database schema (CREATE TABLE statements) for this app.
- Create a Python database-access API for accessing Poll and Choice objects.
- But first we need to tell our project that the polls app is installed.

Edit the my_geonode/settings.py file, and update the INSTALLED_APPS setting to include the string 'polls'. So it'll look like this::

    INSTALLED_APPS = (

        # Apps bundled with Django
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.admin',
        'django.contrib.sitemaps',
        'django.contrib.staticfiles',
        'django.contrib.messages',
        'django.contrib.humanize',

        #Third party apps

        # <snip>
 
        # GeoNode internal apps
        'geonode.maps',
        'geonode.upload',
        'geonode.layers',
        'geonode.people',
        'geonode.proxy',
        'geonode.security',
        'geonode.search',
        'geonode.catalogue',
        'geonode.documents',

        # My GeoNode apps
        'polls',
    )   

Now Django knows to include the polls app. Let's run another command::

    $ python manage.py syncdb


The syncdb command runs the SQL from sqlall on your database for all apps in INSTALLED_APPS that don't already exist in your database. This creates all the tables, initial data and indexes for any apps you've added to your project since the last time you ran syncdb. syncdb can be called as often as you like, and it will only ever create the tables that don't exist.

GeoNode uses south for migrations ...

Next, lets add the Django admin configuration for our polls app so that we can use the Django Admin to manage the records in our database. Edit a new file called polls/admin.py and make it look like the this::

    from polls.models import Poll
    from django.contrib import admin

    admin.site.register(Poll)

Run the development server and explore the polls app in the Django Admin by pointing your browser to http://localhost:8000/admin/ and logging in with the credentials you specified when you first ran syncdb.

.. figure:: img/admin_top.png

You can see all of the other apps that are installed as part of your GeoNode project, but we are specifically interested in our Polls app for now.

.. figure:: img/admin_polls.png

Next we will add a new poll via automatically generated admin form.

.. figure:: img/add_new_poll.png

You can enter any sort of question you want for initial testing and select today and now for the publication date.

.. figure:: img/add_poll.png

The next step is to configure the Choice model in the admin, but we will configure the choices to be editable inline with the Poll objects they are attached to. Edit the same polls/admin.py so it now looks like the following::

    from polls.models import Poll, Choice
    from django.contrib import admin

    class ChoiceInline(admin.StackedInline):
        model = Choice
        extra = 3

    class PollAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,               {'fields': ['question']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
        inlines = [ChoiceInline]

    admin.site.register(Poll, PollAdmin)

This tells Django: "Choice objects are edited on the Poll admin page. By default, provide enough fields for 3 choices."

You can now return to the Poll admin and either add a new poll or edit the one you already created and see that you can now specify the poll choices inline with the poll itself..

.. figure:: img/choice_admin.png

From here, we want to create views to display the polls inside our GeoNode project.A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template. In our poll application, we’ll have the following four views:

- Poll “index” page – displays the latest few polls.
- Poll “detail” page – displays a poll question, with no results but with a form to vote.
- Poll “results” page – displays results for a particular poll.
- Vote action – handles voting for a particular choice in a particular poll.

The first step of writing views is to design your URL structure. You do this by creating a Python module, called a URLconf. URLconfs are how Django associates a given URL with given Python code.

Lets start by adding our url configuration directly to the urls.py that already exists in your project my_geonode/urls.py. Edit this file and add the following lines after the rest of the existing imports around line 80::

    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

.. note:: Eventually we will want to move this set of url configurations inside the urls app itself, but for the sake of brevity in this workshop, we will put them in the main urls.py for now. You can consult the Django tutorial for more information on this topic.

Next lets write the views to drive the url patterns we configured above. Edit polls/views.py to that it looks like the following::

    from django.template import Context, loader
    from polls.models import Poll
    from django.http import HttpResponse
    from django.http import Http404
    from django.shortcuts import render_to_response

    def index(request):
        latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
        return render_to_response('polls/index.html',
            RequestContext(request, {'latest_poll_list': latest_poll_list}))

    def detail(request, poll_id):
        try:
            p = Poll.objects.get(pk=poll_id)
        except Poll.DoesNotExist:
            raise Http404
        return render_to_response('polls/detail.html', RequestContext(request, {'poll': p}))

    def results(request, poll_id):
        return HttpResponse("You're looking at the results of poll %s." % poll_id)

    def vote(request, poll_id):
        return HttpResponse("You're voting on poll %s." % poll_id)

.. note:: We have only stubbed in the views for the results and vote pages and they are not very useful as is. We will revisit these later. 

Now we have views in place, but we are referencing templates that do not yet exist. Lets add them by first creating a template directory in your polls app as polls/templates/polls and creating polls/templates/polls/index.html to look like the following::

    {% if latest_poll_list %}
        <ul>
        {% for poll in latest_poll_list %}
            <li><a href="/polls/{{ poll.id }}/">{{ poll.question }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No polls are available.</p>
    {% endif %}

Next we need to create the template for the poll detail page. Create a new file at polls/templates/polls/detail.html to look like the following::

    <h1>{{ poll.question }}</h1>
    <ul>
    {% for choice in poll.choice_set.all %}
        <li>{{ choice.choice }}</li>
    {% endfor %}
    </ul>

You can now visit http://localhost:8000/polls/ in your browser and you should see the the poll question you created in the admin presented like this.

.. figure:: img/polls_plain.png

We actually really want our polls app to display as part of our GeoNode project with the same theme, so lets update the 2 templates we created above to make them extend from the site_base.html template we looked at in the last section. You will need to add the following 2 lines to the top of each file::

    {% extends 'site_base.html' %}
    {% block body %}

And close the block at the bottom of each file with::

    {% endblock %}

This tells Django to extend from the site_base.html template so your polls app has the same style as the rest of your GeoNode, and it specifies that the content in these templates should be rendered to the body block defined in GeoNode's base.html template that your site_base.html extends from.

You can now visit the index page of your polls app and see that it is now wrapped in the same style as the rest of your geonode site. 

.. figure:: img/polls_geonode.png

If you click on a question from the list you will be taken to the poll detail page. 

.. figure:: img/poll_geonode_hidden.png

Looks like its empty, but in fact the text is there, but its been styled to white by the bootswatch theme we added in the last section. If you highlight the area where the text is, you will see that it is in fact there.

.. figure:: img/poll_geonode_highlight.png

Now that you have walked through the basic steps to create a very minimal (and currently mostly useless) Django app and integrate it with your GeoNode project, you should pick up the Django tutorial at part 4 and follow it to add the form for actually accepting responses to your poll questions. 

Again, its strongly recommended that you spend as much time as you need with the Django tutorial itself until you feel comfortable with all of the concepts it coveres. They are the essential building blocks you will need to extend your GeoNode project by adding your own apps. 

Adding a 3rd Party Blog App 
---------------------------

Adding Other Apps 
-----------------
