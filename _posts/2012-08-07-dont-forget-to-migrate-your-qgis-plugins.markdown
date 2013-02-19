---
comments: true

layout: post
slug: dont-forget-to-migrate-your-qgis-plugins
title: Don't forget to migrate your QGIS plugins!
wordpress_id: 1116
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- Open Source
- python
- qgis
- Quantum GIS
---

From QGIS 1.8 and onwards the Plugin Installer plugin will no longer include the option to add the 3rd party repositories.  This was by design and intended to move people over to using the official plugin repository at [http://plugins.qgis.org/](http://plugins.qgis.org/) so we can provide a richer experience and keep everything in one place.

If you have plugins that are still not on the official repository then I would strongly recommend that you migrate them as a lot of new 1.8 users will be missing out on your great work.

{% image http://woostuff.files.wordpress.com/2012/08/migrate.jpg %}
{% endimage %}
