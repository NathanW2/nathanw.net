---
comments: true

layout: post
slug: total-length-of-selected-objects-qgis-via-python
title: Getting total length of selected lines in QGIS via python
wordpress_id: 507
categories:
- Open Source
- qgis
tags:
- gis
- mapping
- Open Source
- python
- qgis
- Quantum GIS
- shapely
---

The other day I was trying to get the total length of the some selected lines in QGIS.  In MapInfo I would just do


> Select Sum(ObjectLen(obj,"m")) from Selection


however QGIS doesn't have the ability (yet..) to run SQL queries like this, but you can do it via python.

The following is a little python snippet that will get the total length of the selected objects. _(You will need to have shapely installed to use)_

{% highlight python %}
from shapely.wkb import loads
def getLength():
    layer = qgis.utils.iface.mapCanvas().currentLayer()
    total = 0
    for feature in layer.selectedFeatures():
        geom = feature.geometry()
        wkb = geom.asWkb()
        line = loads(wkb)
        total = total + line.length
    return total

print getLength()
{% endhighlight %}

_**EDIT:Or as Peter asked in the comments, yes you can just call length on the geometry:**_

{% highlight python %}
def getLength():
    layer = qgis.utils.iface.mapCanvas().currentLayer()
    total = 0
    for feature in layer.selectedFeatures():
        geom = feature.geometry()
        total = total + geom.length()
    return total

print getLength()
{% endhighlight %}

Just copy and past that into your QGIS python console and call _getLength()_ when ever you need the total length.

_Note: I have found the _QgsGeometry ._legnth() function to be unstable in the past and it has crashed my QGIS instance. Just test it first, if not you can always use the shapely method._
