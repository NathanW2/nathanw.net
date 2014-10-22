title: Adding __geo_interface__ to QGIS geometry and feature
description: ""
category: 
tags: []

What is `__geo_interface__` anyway? If you have never seen `__geo_interface__` it was defined by [Sean Gillies](http://sgillies.net/) at [https://gist.github.com/sgillies/2217756](https://gist.github.com/sgillies/2217756). A cool lightweight interface that describes a single spatial object using a GeoJSON like structure, in fact parts of it are just normal GeoJSON.	

Since QGIS in feature freeze at the moment I can't add this to the main code base just yet. Awwww sad face :(

### but wait!

Thanks to good ol' Python we can just monkey patch it right on.

```python
def mapping_feature(feature):
    geom = feature.geometry()
    properties = {}
    fields = [field.name() for field in feature.fields()]
    properties = dict(zip(fields, feature.attributes()))
    return { 'type' : 'Feature',
             'properties' : properties,
             'geometry' : geom.__geo_interface__}

def mapping_geometry(geometry):
    geo = geometry.exportToGeoJSON()
    # We have to use eval because exportToGeoJSON() gives us
    # back a string that looks like a dictionary. 
    return eval(geo)

QgsFeature.__geo_interface__ = property(lambda self: mapping_feature(self))
QgsGeometry.__geo_interface__ = property(lambda self: mapping_geometry(self))
```

And that's that. Easy hey. Really got to love dynamic languages. 

The `__geo_interface__` property now exists on any instance of `QgsGeometry` or `QgsFeature`.  Lets test that theory.

```python
>>> import pprint
>>> layer = iface.activeLayer()
>>> feature = layer.selectedFeatures()[0]
>>> feature.__geo_interface__
>>> pprint.pprint(f.__geo_interface__)
{'geometry': {'coordinates': [[[385039.90567724, 6449154.61878853],
                               [385059.01135993, 6449154.80874077],
                               [385059.41538719, 6449114.58680192],
                               [385040.30145863, 6449114.38685169],
                               [385040.16953133, 6449127.46423076],
                               [385039.90567724, 6449154.61878853]]],
              'type': 'Polygon'},
 'properties': {u'address': u'HYNES WY',
                u'assessment': u'2204315',
                u'bool': u'F',
                u'dola_pin': 283678,
                u'field18': 2920,
                u'field19': 0.0,
                u'house_numb': u'3',
                u'location': None,
                u'lot': u'LOT 107',
                u'new': None,
                u'old': u'http://www.seabreeze.com.au|mylink',
                u'paid_in_fu': u'F',
                u'pin_string': u'283678',
                u'postcode': u'6163',
                u'reserve': None,
                u'sample_dat': u'2003-05-15',
                u'subdivided': None,
                u'suburb': u'HAMILTON HILL',
                u'suburb_wit': u'HAMILTON HILL',
                u'type': u'H',
                u'v_auto_dat': None,
                u'v_auto_use': None,
                u'v_boolean': None,
                u'v_datetime': None,
                u'v_decimal': None,
                u'v_int': None,
                u'v_numeric': None,
                u'v_varcha_1': None,
                u'v_varchar': None,
                u'v_varchar_': None},
 'type': 'Feature'}
>>> feature.geometry().__geo_interface__
{'type': 'Point', 'coordinates': [388197.74503284, 6450504.16670842]}
```

Excellent!
