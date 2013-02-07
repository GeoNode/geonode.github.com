.. _setup:

Setting up your GeoNode Project
===============================

This section will walk you through the steps necessary to setup your own GeoNode project. It assumes that you have installed GeoNode from the ubuntu packages and that you have a working GeoNode site.

Setup Steps
-----------

If you are working remotely, You should first connect to the machine that has your GeoNode installed on it. You will need to perform the following steps in a directory where you intend to keep your newly created project.

#. Activate GeoNode's Virtual Environment::

    $ source /var/lib/geonode/bin/activate

#. Create your GeoNode project from the Template::

    $ django-admin.py startproject --template=https://github.com/GeoNode/geonode-project/zipball/master my_geonode
    $ cd my_geonode

#. Update your local_settings.py:

   You will need to check the local_settings.py that is included with the template project and be sure that it reflects your own local environment. You should pay particular attention to the Database settings especially if you intend to reuse the database that was setup with your base GeoNode installation.

#. Synchronize your Database::

    $ python manage.py syncdb --all

#. Run the test server::

    $ python manage.py runserver

#. Visit your new GeoNode Site.
  
    http://localhost:8000

Source Code Revision Control
----------------------------

It is recommended that you immediately put your new project under source code revision control. The GeoNode development team uses Git and GitHub purpose and recommends that you do the same. If you do not already have a GitHub account, it is recommended that you set one up. A full review of Git and distributed Source Code Revision Control systems is beyond the scope of this tutorial, but you may find the `Git Book`_ useful if you are not already familiar with these concepts.

.. _Git Book: http://git-scm.com/book

#. Create a new Repository in GitHub:

   You should use the GitHub user interface to create a new repository for your new project.

   .. figure:: img/github_home.jpg

   *Creating a new GitHub Repository From GitHub's Homepage*

   .. figure:: img/create_repo.jpg

   *Specifying new GitHub Repository Parameters*

   .. figure:: img/new_repo.jpg

   *Your new Empty GitHub Repository*

#. Initialize your own repository::

    $ git init

#. Add the remote repository reference to your local git configuration::

    $ git remote add 

#. Add your project files to the repository::

    $ git add .

#. Commit your changes::

   $ git commit -am "Initial commit"

#. Push to the remote repository::

   $ git push origin master

Your GeoNode Project's Struture
-------------------------------

Your GeoNode project will now be structured as depicted below::

    ├── README.rst
    ├── manage.py
    ├── my_geonode
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── static
    │   │   ├── README
    │   │   ├── css
    │   │   │   └── site_base.css
    │   │   ├── img
    │   │   │   └── README
    │   │   └── js
    │   │       └── README
    │   ├── templates
    │   │   ├── site_base.html
    │   │   └── site_index.html
    │   ├── urls.py
    │   └── wsgi.py
    └── setup.py

You can also view your project on github.

   .. figure:: img/github_project.png


Each of the key files in your project are described below.

manage.py
~~~~~~~~~

settings.py
~~~~~~~~~~~

urls.py
~~~~~~~

wsgi.py
~~~~~~~

setup.py
~~~~~~~~

static
~~~~~~

templates
~~~~~~~~~

Deploying your GeoNode Project
------------------------------

Now that your own project is setup, you will need to replace the existing default configuration with configuration for your own project in order to visit your new project site.

#. Update Apache Configuration

#. Check GeoServer Configuration

#. Check Database Configuration

Staying in Sync with Mainline GeoNode
-------------------------------------

One of the primary reasons that we setup your own GeoNode project using this method is so that you can stay in sync with mainline geonode as the core GeoNode development team makes new releases. Your own project should not be adversely affected by these upstream changes, but you will receive bug fixes and other improvements by staying in sync.

#. Upgrade GeoNode::

    $ apt-get update
    $ apt-get install geonode

#. Verify that your new project works with the upgraded GeoNode::

    $ python manage.py runserver

   Visit http://localhost:8000/
