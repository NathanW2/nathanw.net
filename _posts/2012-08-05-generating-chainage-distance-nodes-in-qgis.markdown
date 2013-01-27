---
comments: true
date: 2012-08-05 19:36:01
layout: post
slug: generating-chainage-distance-nodes-in-qgis
title: Generating chainage (distance) nodes in QGIS
wordpress_id: 1091
categories:
- Open Source
- qgis
tags:
- language python
- Open Source
- osgeo
- pyqgis
- python
- qgis
- qgis-tips
- Quantum GIS
- tips
---

Something that I need to do now and then is generate points along a line at supplied distance.  I had never really looked into doing it in QGIS until [this](http://gis.stackexchange.com/questions/27102/how-to-create-equidistant-points-in-qgis) question poped up on [gis.stackexchange.com](gis.stackexchange.com).  This is a quick blog post because I thought it was a pretty handy little thing to do.

In the development version there is a new method on `QgsGeometry` called `interpolate`. This method takes a distance and returns a point along a line at that distance. Perfect! We can then just wrap this in a loop and generate a point increasing the distance as we move along

{% highlight python %}
from qgis.core import (QgsFeature, QgsGeometry,
                       QgsVectorLayer, QgsMapLayerRegistry,
                       QgsField)
from PyQt4.QtCore import QVariant
from qgis.utils import iface

def createPointsAt(distance, geom):
    length = geom.length()
    currentdistance = distance
    feats = []

    while currentdistance < length:
        # Get a point along the line at the current distance
        point = geom.interpolate(currentdistance)
        # Create a new QgsFeature and assign it the new geometry
        fet = QgsFeature()
        fet.setAttributeMap( { 0 : currentdistance } )
        fet.setGeometry(point)
        feats.append(fet)
        # Increase the distance
        currentdistance = currentdistance + distance

    return feats

def pointsAlongLine(distance):
    # Create a new memory layer and add a distance attribute
    vl = QgsVectorLayer("Point", "distance nodes", "memory")
    pr = vl.dataProvider()
    pr.addAttributes( [ QgsField("distance", QVariant.Int) ] )
    layer = iface.mapCanvas().currentLayer()
    # Loop though all the selected features
    for feature in layer.selectedFeatures():
        geom = feature.geometry()
        features = createPointsAt(distance, geom)
        pr.addFeatures(features)
        vl.updateExtents()

    QgsMapLayerRegistry.instance().addMapLayer(vl)
{% endhighlight %}

The above code might look a bit scary at first if you have never done any Python/pyqgis but hopefully the comments will ease the pain a little. The main bit is the `createPointsAt` function.

Cool! If we want to use this we can just stick it in a file in the `.qgis/python` folder (lets call it pointtools.py) and then run `import pointtools` in the python console.

So lets have a go. First select some objects then run the following in the Python Console

{% highlight python %}
import pointtools
pointtools.pointsAlongLine(40)
{% endhighlight %}

That will generate a point every 40 meters along then selected lines

{% image http://woostuff.files.wordpress.com/2012/08/nodes.png %}
{% endimage %}

To generate nodes along different lines, select the new features, then call `pointtools.pointsAlongLine(40)` in the Python console.

Simple as that!

(Who knows, someone (maybe me) might even add this as a core object function in QGIS in the future)
