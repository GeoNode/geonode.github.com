GeoNode's Website

Please do not edit files outside the 'pages' directory. This repo is using Cactus [1] to generate the static files based on Django templates and your changes may be lost.

To make and preview changes you need to do the following:

```
pip install cactus
cactus build
cactus serve
# navigate to http://localhost:8000/
cp -R .build/* .
lessc static/less/site.less > static/css/style.css
# commit and push
```

[1] https://github.com/koenbok/Cactus
