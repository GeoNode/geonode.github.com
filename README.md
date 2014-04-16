GeoNode's Website

Please do not edit files outside the 'pages' directory. This repo is using Cactus [1] to generate the static files based on Django templates and your changes may be lost.

To make and preview changes you need to do the following:

```

#install lessc
sudo npm install -g less

pip install cactus
cactus build
cactus serve
# navigate to http://localhost:8000/

#This will copy the files from the .build folder. 'cp: cannot overwrite directory ./static with non-directory .build/static' is an expected error and can be ignored.
cp -R .build/* .

#lessc recompiles the CSS.
lessc static/less/site.less > static/css/style.css
# commit and push
```

When you have made your changes to ensure they are part of the compiled HTML page, please check the index.html file in the document root. Also, when commiting and pushing observe which files have been changed through using Cactus and only commit those pages which are directly affected from your changes.

[1] https://github.com/koenbok/Cactus
