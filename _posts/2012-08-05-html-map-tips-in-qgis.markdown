---
comments: true
date: 2012-08-05 21:35:17
layout: post
slug: html-map-tips-in-qgis
title: HTML map tips in QGIS
wordpress_id: 1098
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- mapping
- Open Source
- qgis
- styling
- tips
---

New fresh QGIS feature! So fresh in fact you can still smell the wet paint :)

QGIS (development build) can [now](https://github.com/qgis/Quantum-GIS/commit/8aa160bcb3548a881248c7d46d92c4f2e12ffc02) display map tips using HTML (a [subset](http://doc.qt.nokia.com/4.7-snapshot/richtext-html-subset.html) anyway).

To enable the new map tips: Open the Layer Properties dialog for a layer and select the Display tab

[![](http://woostuff.files.wordpress.com/2012/08/html.png)](http://woostuff.files.wordpress.com/2012/08/html.png) Display tab to set HTML map tips


## In action


[![](http://woostuff.files.wordpress.com/2012/08/html-inaction.png)](http://woostuff.files.wordpress.com/2012/08/html-inaction.png) Layer properties for HTML map tip

Notice how we can also use a QGIS expression. Anything inside `[% %]` will be evaluated and replaced with the value in real-time. We can even use a CASE statement. Pretty cool!

And the result when hovering over a feature

[![](http://woostuff.files.wordpress.com/2012/08/html-inaction2.png)](http://woostuff.files.wordpress.com/2012/08/html-inaction2.png) HTML in QGIS map tip? Yes! WOOT!

Hold on. Pause the track! We can even use some CSS to make it more fancy.

<script src="https://gist.github.com/3651842.js"> </script>

[![](http://woostuff.files.wordpress.com/2012/08/css.png)](http://woostuff.files.wordpress.com/2012/08/css.png) CSS in a html map tip

Happy Mapping :)
