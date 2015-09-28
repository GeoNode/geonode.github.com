# geonode.org

This is the setup for the [GeoNode website](http://geonode.org).

## Setting up website environment locally

    # setup virtualenv
    virtualenv geonode.org && cd $_
    . bin/activate
    # get the repo
    git clone git@github.com:GeoNode/geonode.github.com && cd geonode.github.com
    # set Ruby environment variables
    . setenv-ruby-gem.sh
    # install Jekyll
    gem install jekyll link-checker jekyll-feed jekyll-mentions jekyll-sitemap github-pages

Workflow
--------

    # edit content
    jekyll build
    jekyll serve  # default port is 4000, set explicitly with -P 
    # check links
    check-links _site
    # view at http://localhost:4000
    # adding blogposts
    cd _drafts
    vi newpost.md
    # make sure to set the following YAML front matter:
    # layout: base
    #
    # preview with `jekyll build --drafts` or `jekyll serve --drafts` and draft will show up as latest post
    # when you are ready to publish:
    # - rename the file as per the current YYYY-MM-DD
    git mv _drafts/newpost.md _posts/YYYY-MM-DD-newpost.md
    vi _posts/YYYY-MM-DD-newpost.md
    # commit and push
    git commit -m 'publish article'
    git push origin master
