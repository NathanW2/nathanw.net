---
layout: post
title: "Case of the Unexplained QGIS buzz sound"
description: "Yay computers"
category: 
tags: [qgis]
---

So picture this. Build up for the next release of QGIS. Make the release. Yay awesome! A day in and some users are reporting hearing a buzzing/clicking sound. What the heck!? 

Now QGIS doesn't use any sound code at all - A GIS program that can rick roll people, now that is an idea.  Hearing a sound and not using sound code was the first red flag that something stage was going on.  Only one user reported the issue and couldn't reproduce it on another machine so I closed the ticket as a local issue. Done. 

Or not..

Not soon after more users reported the issue. Then a client emailed me saying they had they same thing, then other person I knew.  Something really isn't right here, QGIS doesn't make sounds. Most users reported that this only happens when the file contains unicode or has a strange name like "test,test.shp".   Stuff like this bugs the living hell out of me so I just had to have a go at working out what was going on.


All users reported only seeing this issue in the 64bit build after installing I was also able to replicate the issue. Half the battle is just seeing if you can replicate. Now to the fun.  To track down why.  After I opened one of the files I noticed that a single buzz sound was made when panning, or zooming, and only with shape files. So it must be made when opening the file.

When trying to fetch the features using ``layer.getFeatures()`` in the Python console I could hear the sound. Before looking into the QGIS code to compare 2.2 and 2.4, I first wanted to confirm it was in QGIS and not outside.  Open up OSGeo4W shell ``ogrinfo -al -so "test,test.shp". BUZZZZZZ! So it's not QGIS, but OGR/GDAL.  At least now I have a reduced target to work with.
 
Enter ProcMon

The first thing I did was run ProcMon and saving two logs. One running while ogrinfo from my 32bit install, and the other from the 64bit install run. Now I could compare the two logs to see if anything strange was up:

[SIDE BY SIDE]

First thing I noticed was the 
