# geonode.org

Prerequisites
-------------
    sudo apt-get install ruby-full build-essential zlib1g-dev
    echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
    echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
    echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    gem install bundler
    bundle install

Workflow
--------

    # edit content
    bundle exec jekyll serve  # default port is 4000, set explicitly with -P 
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
    bundle exec jekyll build
    git commit -m 'publish article'
    git push origin master
