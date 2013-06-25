---
layout: post
title: "Adding __geo_interface__ to QGIS geometry and feature"
description: ""
category: 
tags: []
---

What is `__geo_interface__` anyway? If you have never seen `__geo_interface__` it was defined by [Sean Gillies](http://sgillies.net/) at [https://gist.github.com/sgillies/2217756](https://gist.github.com/sgillies/2217756). A cool lightweight interface that describes a single spatial object using a GeoJSON like structure, in fact parts of it are just normal GeoJSON.	

Since QGIS in feature freeze at the moment I can't add this to the main code base just yet. Awwww sad face :(

### but wait!

Thanks to good ol' Python we can just monkey patch it right on.

{% highlight python %}
def mapping_feature(feature):
    geom = feature.geometry()
    properties = {}
    fields = feature.fields()
    for index, attr in enumerate(feature.attributes()):
        name = fields[index].name()
        properties[name] = attr
        
    return { 'type' : 'Feature',
             'properties' : properties,
             'geometry' : geom.__geo_interface__()}

def mapping_geometry(geometry):
    geo = feature.geometry().exportToGeoJSON()
    # We have to use eval because exportToGeoJSON() gives us
    # back a string that looks like a dictionary. 
    return eval(geo)

from types import MethodType
QgsGeometry.__geo_interface__ = MethodType(mapping_geometry, None, QgsGeometry)
QgsFeature.__geo_interface__ = MethodType(mapping_feature, None, QgsFeature)
{% endhighlight %}

And that's that. Easy hey. Really got to love dynamic languages. 

The `__geo_interface__` method will now exists on any instance of `QgsGeometry` or `QgsFeature`.  Lets test that theory.

{% highlight python %}
>>> layer = iface.activeLayer()
>>> feature = layer.selectedFeatures()[0]
>>> feature.__geo_interface__()
{'geometry': {'type': 'Point', 'coordinates': [388197.74503284, 6450504.16670842]}, 'type': 'Feature', 'properties': {u'court_acti': None, u'autoid': 0, u'userid': None, u'number': 0.0, u'datetime': None, u'building_l': None, u'totally_is': None, u'issue_date': u'1998-12-23', u'property_n': u'1103182', u'water_qual': None, u'pool_posit': u'CENTRE REAR', u'next_insp_': None, u'string': None, u'insp_form_': None, u'fence_type': None, u'dogs_on_pr': None, u'suburb': None, u'skimmer_bo': None, u'date': None, u'picklist': None, u'multitext': None, u'last_insp_': None, u'pool_licen': u'98167', u'pool_type': u'FIBREGLASS', u'map_key': 324548, u'boolean': u'F'}}
>>> feature.geometry().__geo_interface__()
{'type': 'Point', 'coordinates': [388197.74503284, 6450504.16670842]}
{% endhighlight %}

Excellent!


## Some extra info

If you have never seen this kind of voodoo `MethodType` magic before:

{% highlight python %}
def mapping_geometry(geometry):
	...

def mapping_feature(feature):
	...

from types import MethodType
QgsGeometry.__geo_interface__ = MethodType(mapping_geometry, None, QgsGeometry)
QgsFeature.__geo_interface__ = MethodType(mapping_feature, None, QgsFeature)
{% endhighlight %}

This is adding the `__geo_interface__` method onto the class `QgsGeomtry` and `QgsFeature` and mapping it to the `mapping_geometry` and `mapping_feature` methods respectively.  Each `mapping` function is passed the instance of the class they are bound to when called.  In the end it would be the same as if we had defined `QgsGeomtry` in Python like so:

{% highlight python %}
class QgsGeometry():
	def mapping_geometry(self):
		...
{% endhighlight %}

Again, <3 Python




