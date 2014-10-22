slug: mapinfo-and-qgis-an-overview
title: MapInfo and QGIS - An overview
categories:
- MapInfo
- Open Source
- qgis
- QGIS for MapInfo Users
tags:
- mapinfo
- Open Source
- qgis
- qgis-vs-mapinfo

_Disclaimer: Like all my blog posts, this post is a reflection of my opinions and my opinions only. They do not reflect the opinions of my employer._

Recently I have got more into the open source movement, with my coding and my choice of software.  I tend to try to pick open source software for a couple of reasons, one of the main things is being free but apart from that I try to pick software that I can use to improve my development skills.  Being able to view the code is a big plus for me, being able to change and improve the software myself is an even bigger plus.

My most recent pick has been rediscovering [QGIS](www.qgis.org) (Quantum GIS), a free and open source GIS system written [mostly] in C++ using the [Qt](http://qt.nokia.com/products/) framework, and extensible by both Python and C++. I first discovered QGIS a couple of years ago, I was impressed but not impressed enough to really get into it. Maybe it was that I was so used to MapInfo I didn't give it a proper look; or I didn't really have the data in the right format, as I mainly used MapInfo, and if it couldn't open and edit MapInfo TAB files I didn't want to use it; or just lack of time; or whatever the reason. I used it for a day thought "Yep cool" and went back to using MapInfo.

Recently, however, they released [QGIS 1.5](http://www.qgis.org/en/component/content/article/108.html) [and now [QGIS 1.6](http://linfiniti.com/2010/11/qgis-1-6-copiapo-is-released/)] which changed the way I looked at the software.

The first thing I noticed was it was a lot faster in regards to map rendering then it used to be, not as fast as MapInfo but still very usable and efforts are being made to improve it even more so.

Styling of the layers has also improved a lot since I first tried it, it now has stack styling for points, lines and regions. Stack styles is something that was introduced in MapInfo 10.5, but unlike MapInfo, QGIS allows you to create a stacked style for each feature class rather than a style override like in MapInfo.  So you have a lot more control with styling in QGIS then you do in MapInfo.

[![](http://woostuff.files.wordpress.com/2010/12/styling.png)](http://woostuff.files.wordpress.com/2010/12/styling.png)

and styles applied:

[![](http://woostuff.files.wordpress.com/2010/12/styles.png)](http://woostuff.files.wordpress.com/2010/12/styles.png)

Styling in QGIS is also only based on the underlying data of the object, think thematic maps in MapInfo.  I kind of like this, rather than just being able to just style an object you need to think about the data that is stored with an object.  This also stops the style and data getting out of sync.  At times I have seen maps made in MapInfo with no information on the object but  just styled to show different classes.

QGIS supports a large number of formats. It can open and write tab files but just not at the same time, no big deal as you can always use shape or a postgis database then just convert back if needed.

QGIS also has an interesting plugin system, while being able to use C++ and Python, the main app has a plugin installer [a plugin itself] which lets you install plugins from "hosted repositories".  This makes finding new tools with work with very easy.

[![](http://woostuff.files.wordpress.com/2010/12/plugins.png)](http://woostuff.files.wordpress.com/2010/12/plugins.png)

Composers are basically MapInfo layout windows, they allow you to add maps, legends, text labels, dynamic scale bar. attribute tables.  Composers can be exported to svg, pdf or printed just like layouts and you can have as many composers as you need.

[![](http://woostuff.files.wordpress.com/2010/12/plugins1.png)](http://woostuff.files.wordpress.com/2010/12/plugins1.png)

Labeling options in QGIS are pretty much the same as MapInfo, if not more. You have the ability to use columns from a table that defines information about labels eg colour, X and Y etc if needed.

But one big feature that I really like about QGIS is the info tool. Unlike MapInfos info tool, you can define per table how and what information is displayed for each column and there is no stupid Ctrl+C copy bug.  It's a bit hard to explain so a picture saves a thousand words:

[![](http://woostuff.files.wordpress.com/2010/12/attribute.png)](http://woostuff.files.wordpress.com/2010/12/attribute.png)

and editing or adding a new feature:

[![](http://woostuff.files.wordpress.com/2010/12/editing.png)](http://woostuff.files.wordpress.com/2010/12/editing.png)

For me as a developer the one thing that I find great with QGIS is it has a very kind and active developer community, though both IRC and email, and the code is relatively well organized .   I was able to pull down the source code for the latest trunk and have a build running in Ubuntu in under a hour [this mainly being due to my lack of Linux experience].   Being able to see something you don't like, change it and submit it back to the project is a very good feeling.


## Some downsides:


While QGIS is very good, and is always improving, it doesn't always win over MapInfo in everything.  One major thing that MapInfo has going is its SQL, being able to run the same SQL syntax over any kind of table in MapInfo is a great feature.   QGIS, in this regard, tends to leave those things up to the underlying provider.  You are able to run simple [or complex] queries on an open table but being able to do something like "Select Col1, Col2, Col3 From Table Where Col1 = "SomeCondition" Group By Col2"  isn't really there, although if you are running PostGIS it is quite easy.

[![Query](http://woostuff.files.wordpress.com/2010/12/q.png)](http://woostuff.files.wordpress.com/2010/12/q.png)

The next big thing MapInfo has, is MAPBASIC.  While QGIS has a built-in Python shell and has a relatively good API, MAPBASIC is very easy language to get up to speed with especially for beginners.

MapInfo also has multiple map windows, this is something that isn't currently implemented in QGIS.  However I did bring it up on the #qgis IRC channel and the developers seemed happy with the idea but just needed time and someone to implement it.


## Summary:


I could talk all day about all the cool things that QGIS can do but to save boring you I'll leave it at this for now, more posts to come in the future I'm sure.

At the moment for my current day-to-day map work, I have gone from using MapInfo to using QGIS almost full time.  Like mentioned above, there are still some things that MapInfo does well and I tend to use MapInfo for those kind of jobs.  Also as my employer uses MapInfo and runs pretty much a full MapInfo system, I still use it for maintaining things like Exponare.  Using and developing for QGIS also means I have fallen behind on my MapInfo .Net tools, I still have a couple on the go and plan to get them out just before Christmas [or maybe a little bit after]

So my overall impressions with QGIS, if you couldn't tell already, are: very very impressed with a very strong feeling it's only going to get better.

So if you're interested in trying something new, give QGIS a go.


## Some handy links:





	
  * [http://linfiniti.com/](http://linfiniti.com/) Not only about QGIS but some other handy open source GIS tricks.

	
  * [http://linfiniti.com/2010/11/python-qgis-cookbook/](http://linfiniti.com/2010/11/python-qgis-cookbook/) Link to the QGIS python cookbook, handy for getting up to speed on the QGIS python API.

	
  * [http://underdark.wordpress.com/](http://underdark.wordpress.com/) Very handy blog to keep up with the latest happenings with QGIS

	
  * [http://qgis.org/](http://qgis.org/) The main QGIS page.

	
  * #qgis on irc.freenode.net The Irc channel for QGIS developers.


