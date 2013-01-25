---
comments: true
date: 2011-09-27 16:35:31
layout: post
slug: generating-contours-using-gdal-via-shell-or-qgis
title: 'Generating contours using GDAL ( via shell or QGIS)   '
wordpress_id: 834
categories:
- Open Source
- qgis
tags:
- contours
- DEM
- FOSSGIS
- gdal
- gis
- grid
- ogr
- Open Source
- osgeo
- qgis
- Quantum GIS
- raster
---

I tell you. It always amazes me how much cool stuff you can do with great open source GIS software these days. GDAL is one of those great open source projects that I have just found a great use for (apart from just opening every raster type under the sun in QGIS).

GDAL has the ability to generate contours from a DEM, something that I have always wanted to try for my town but have never been able due to lack of a good DEMs.

Recently we purchased a set of DEMs that cover a large area as part of a study. Each DEM uses a grid size of 1mx1m. Prefect for generating contours.


## Using the GdalTools QGIS plugin.


First make sure that you have the latest version of the GdalTools plugin installed (GdalTools should be installed by default with QGIS. If it's not, search "Gdal" in the plugin installer). Enable the plugin once it's installed.

Load the DEM into QGIS using the Load Raster icon.

[caption id="attachment_846" align="aligncenter" width="630" caption="DEM loaded in QGIS"][![](http://woostuff.files.wordpress.com/2011/09/loaddem.png)](http://woostuff.files.wordpress.com/2011/09/loaddem.png)[/caption]

Now head up to the menu Raster->Extraction->Contour

[caption id="attachment_847" align="aligncenter" width="247" caption="Raster menu in QGIS"][![](http://woostuff.files.wordpress.com/2011/09/rastermenu.png)](http://woostuff.files.wordpress.com/2011/09/rastermenu.png)[/caption]

Select the settings that you need. For this DEM I am going to generate 250mm contours.

[caption id="attachment_848" align="aligncenter" width="605" caption="Contour dialog."][![](http://woostuff.files.wordpress.com/2011/09/contour.png)](http://woostuff.files.wordpress.com/2011/09/contour.png)[/caption]

Take note of the text area at the bottom of the dialog as that is the exact command sent to GDAL in order to generate the contours. If you take a copy of that you can run it on the command line for batch processing later.

Hit ok.

[caption id="attachment_849" align="aligncenter" width="630" caption="250mm contours from the DEM"][![](http://woostuff.files.wordpress.com/2011/09/250mm.png)](http://woostuff.files.wordpress.com/2011/09/250mm.png)[/caption]

[![](http://woostuff.files.wordpress.com/2011/09/zoomed.png)](http://woostuff.files.wordpress.com/2011/09/zoomed.png)

BAM! :)


## Using the command line/shell.


Using QGIS for a one off DEM is fine and dandy but what if you have 3000 DEMs that you need to process. To hell with doing that by hand!

Remember the contour tool in QGIS told us the exact command line args to use, so creating a shell script for automating the process is pretty easy.

{% highlight bash %}
for f in *.asc
do
  echo "Processing $f"
 gdal_contour -a ELEV -i 0.25 $f $f-250mm.shp
done
{% endhighlight %}

The above code will loop though the current directory and process all the DEMs generating 250mm contours for each one. It saves each new contour file as {filename}-250mm.shp. You will need to change *.asc to whatever format your DEM is in.

Copy the above code into a file somewhere and call it generate_contours.sh. This can then be called from the command line using

sh generate_contours.sh


### Running sh on Windows


If you're a windows user you will need to run OsGeo4W Shell in order to use sh.

[caption id="attachment_851" align="aligncenter" width="630" caption="Loading OsGeo4w shell."][![](http://woostuff.files.wordpress.com/2011/09/osgeoshell.png)](http://woostuff.files.wordpress.com/2011/09/osgeoshell.png)[/caption]

Once the shell is loaded you can just call:

sh generate_contours.sh

[caption id="attachment_852" align="aligncenter" width="630" caption="Output from running generate_contours.sh"][![](http://woostuff.files.wordpress.com/2011/09/osgeoshell2.png)](http://woostuff.files.wordpress.com/2011/09/osgeoshell2.png)[/caption]


## Final remarks


I ran the above sh script on a folder with about 2500 DEMs and it took around 4 hours to complete the whole folder. Of course performance will vary but it seems pretty quick considering.

Once again the possibly to use open source GIS tools to get my work done is amazing.  No expensive software here.

So far I'm not aware of any line smoothing/generalizing abilities using GDAL/OGR.  Although you can import the contours into GRASS and use that: [http://grass.osgeo.org/wiki/V.generalize_tutorial
](http://grass.osgeo.org/wiki/V.generalize_tutorial)

You can also generate the contours using GDAL via Python but that is a topic for another day.
