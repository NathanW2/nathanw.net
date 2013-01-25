---
comments: true
date: 2011-08-08 08:48:26
layout: post
slug: slow-opening-of-rasters-in-qgis-1-7-here-is-a-fix
title: Slow opening of rasters in QGIS 1.7? Here is a fix.
wordpress_id: 790
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- Open Source
- OSS
- QGIS 1.7
- Quantum GIS
- rasters
---

**Note: The following post only applies to QGIS 1.7.  QGIS 1.7.1 (upcoming patch) will not have this issue as the default behavior has changed. **

One thing I noticed when running QGIS 1.7 was my rasters were really slow to open and sometimes froze QGIS.  I thought maybe it was some bad plugin that I had installed, nope; maybe opening the raster of the network drive was causing it to be slow, nope. I tried a bunch of stuff, still nothing.  After a while a few other people posted to the mailing list saying they were having the same issue, turns out the solution was very simple.

In QGIS contrast enhancement for rasters is turned on by default, so each time a raster is opened QGIS had to calculate the stats (max and min for example) for the raster and then scale the contrast.  For a large raster this is pretty heavy and this was the cause of all those problems.

**So what's the solution?**

****Turns out QGIS will remember the contrast setting for all rasters if you want it to.

To fix the slow opening raster problem:



	
  1. Open a small raster (just any old picture will do)

	
  2. Double click the layer in the layer list

	
  3. Change Contrast Enhancement to No Stretch

[caption id="attachment_791" align="aligncenter" width="580" caption="Change Contrast Enhancement to No Stretch"][![](http://woostuff.files.wordpress.com/2011/08/rasterfix.png)](http://woostuff.files.wordpress.com/2011/08/rasterfix.png)[/caption]

	
  4. Hit the little Save icon next to the drop down box

	
  5. Open your big raster.


That setting will now be remembered for each raster that is opened and improve the loading time.

On a similar note.  Tim over at [http://linfiniti.com](http://linfiniti.com/2011/08/improvements-to-raster-performance-in-qgis-master/) has done some work to improve the raster performance even more with [http://linfiniti.com/2011/08/improvements-to-raster-performance-in-qgis-master/](http://linfiniti.com/2011/08/improvements-to-raster-performance-in-qgis-master/) .  The improvements that  Tim has made are available in the nightly build of QGIS via qgis-dev in OSGeo4W, or by building the master line from github.com.


