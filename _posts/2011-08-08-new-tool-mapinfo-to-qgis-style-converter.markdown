---
comments: true
date: 2011-08-08 16:39:06
layout: post
slug: new-tool-mapinfo-to-qgis-style-converter
title: 'New Tool: MapInfo to QGIS style converter'
wordpress_id: 707
categories:
- MapInfo
- Open Source
- qgis
- QGIS for MapInfo Users
tags:
- gis
- mapinfo
- MapInfo Professional
- mapping
- Open Source
- qgis
- qgis-vs-mapinfo
- Quantum GIS
- styling
---

Hopefully this tool can be of some use to people, as I know it has been very helpful to me since I made it.

As I'm a pretty heavy QGIS user now, and my work place still stores most, if not all, of our data MapInfo TAB format, one  friction point for me using QGIS was having to restyle all the MapInfo layers.  If we only had a handful of layer this wouldn't be such a pain but we have a lot of tables and it would take me months to go though each one manually and style them.

I thought "there has to be some way I can automate this..." and so the MapInfo To QGIS Style Generator (or mapinfoToQgis.py) was born. Knowing that QGIS uses QML (a XML file format) to store it style information, and that MapInfo was able to export a style string for each object, I compared what QGIS generated for its QML using the same symbol I picked in QGIS as I had in MapInfo.  Almost a 1 to 1 conversion! Once I worked out how to convert MapInfo point size to QGIS symbol size, and MapInfo colour value to RGB it was just a matter of generating a QML with the correct values.

Long story short, after a bit of clean up and writing a user guide I would like release version 0.1 of the MapInfo To QGIS Style Generator for wider testing.

Here is a quick example of the output.

Step 1: Take One MapInfo table.

![](http://woostuff.files.wordpress.com/2011/08/mapinfo.png)

Step 2: Run it though mapinfoToQgis.py

{% highlight python %}
python mapinfoToQgis.py WaterFittings.Tab WatterFittings.qml -c FittingType --UseMapInfo
{% endhighlight %}

Step 3: Load QML file in QGIS

[![](http://woostuff.files.wordpress.com/2011/08/qgis.png)](http://woostuff.files.wordpress.com/2011/08/qgis.png)

Step 4: Get a beer?

If you are using MapInfo Font symbols or normal MapInfo 3.0 everything should come across almost exactly. mapinfoToQgis.py will use the same fonts in QGIS as you did in MapInfo and select to the correct symbol size. Although if you are using custom MapInfo 3.0 symbols you will get the default QGIS black square symbol,you can just change it to something better after loading the QML.

Currently the program only support converting symbols but I plan on adding line and region support sometime in the future.

The program can be found at [https://github.com/NathanW2/MapInfo-to-QGIS-style-generator](https://github.com/NathanW2/MapInfo-to-QGIS-style-generator) and more detailed instructions and download link can be found at [https://github.com/NathanW2/MapInfo-to-QGIS-style-generator/wiki/Using-MapInfo-to-QGIS-style-generator.](https://github.com/NathanW2/MapInfo-to-QGIS-style-generator/wiki/Using-MapInfo-to-QGIS-style-generator.)

Like I said at the start, hopefully other people will find this tool handy as I know I have.  If you do find it handy let me know, I would love to hear peoples feedback.  Also if you find any bugs let me know in the comments or log a issue on [https://github.com/NathanW2/MapInfo-to-QGIS-style-generator/issues](https://github.com/NathanW2/MapInfo-to-QGIS-style-generator/issues)

Enjoy :)


