---
comments: true
date: 2011-02-24 17:00:21
layout: post
slug: generating-contour-lines-in-qgis
title: Generating contour lines in QGIS
wordpress_id: 514
categories:
- MapInfo
- Open Source
- qgis
tags:
- gis
- mapping
- Open Source
- python
- qgis
- shapely
---

One of the cool things I love about QGIS is finding stuff that you didn't know it could do, well not just itself but plugins that you didn't know about.

Today my discovery was in how to generate contour lines from a point layer.



	
  1. First install the **contour **plugin for qgis via the plugin installer.  Just search for "contour"

	
  2. Once installed open a vector point layer in QGIS.  Make sure the point layer has a field that you can use for elevation.

[caption id="attachment_515" align="aligncenter" width="630" caption="One I prepared earlier"][![](http://woostuff.files.wordpress.com/2011/02/points.png)](http://woostuff.files.wordpress.com/2011/02/points.png)[/caption]

	
  3. Then select from the menu: Plugins->Contour->Contour

	
  4. Fill in the information

[caption id="attachment_517" align="aligncenter" width="514" caption="Details form (The above setting will generate 0.5m contours)"][![](http://woostuff.files.wordpress.com/2011/02/form.png)](http://woostuff.files.wordpress.com/2011/02/form.png)[/caption]

	
  5. Press OK

	
  6. Results

[caption id="attachment_518" align="aligncenter" width="630" caption="Results from plugin "][![](http://woostuff.files.wordpress.com/2011/02/results.png)](http://woostuff.files.wordpress.com/2011/02/results.png)[/caption]

	
  7. Profit??


The resulting contours will have a field that contains the label and z value for each contour line, you can then just label or color them how you wish.

**Note:  There is a bug with QGIS memory layers where the fields don't  show up in dropdown or attribute browsers, a simple fix is just to make the layer editable and then non editable then the fields will be there.**

The contour layer is a QGIS memory layer so remember to save it to disk eg a shapefile before you close you will loose your new fancy contour layer.

Happy mapping :)
