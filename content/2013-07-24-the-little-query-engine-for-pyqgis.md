title: The little pyqgis query engine
description: ""
category: 
tags: [python]



[Sean Gillies](http://sgillies.net/) has managed to get me addicted to using generators, itertools, map, filter, and a generally more [declarative](http://latentflip.com/imperative-vs-declarative/) style of programming. 

<blockquote class="twitter-tweet"><p><a href="https://twitter.com/madmanwoo">@madmanwoo</a> \o/</p>&mdash; Sean Gillies (@sgillies) <a href="https://twitter.com/sgillies/statuses/357318849407885313">July 17, 2013</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

What has this got to do with anything? Well let me explain. A little project I have recently started working on in my free time is a mini query engine for pyqgis to make fetching features easier. The goals are simple. 

- Use a query style syntax to say what I need, not how to get it.  The basics of declarative programming. 
- Use generators to save on memory unless the user asks.

Before we go any further, just note that this is just a hobby project of mine. Not feature complete nor bug free but it's evolving.

The code can be found on [github](https://github.com/NathanW2/little-pyqgis-query-engine) or its [homepage](http://nathanw2.github.io/little-pyqgis-query-engine/). 



What good is a mini query engine?  Lets try with some examples.

Get all the features that match the condition ``postcode > 6164 OR postcode < 6167'`. We will use QgsExpression because that provides a nice where clause type base for us to use.  

```python
exp = QgsExpression("postcode > 6164 OR postcode < 6167")
fields = layer.pendingFields()
exp.prepare(fields)
for feature in layer.getFeatures():
	if exp.evaluate(feature):
		print "Pass"
```

at best you can reduce it to this:

```python
exp = QgsExpression("postcode > 6164 OR postcode < 6167")
fields = layer.pendingFields()
exp.prepare(fields)
features = filter(exp.evaluate, layer.getFeatures())
```

Not too bad. But still. it's a bit of a pain because you have to care about QgsExpression and looping all the features to check.

How about something like this?

```python
q = query(layer).where("postcode > 6164 OR postcode < 6167")
for feature in q():
	print feature
```

Define a query on `layer` and return only the features that match the ``.where()`` condition. Sounds pretty descriptive to me.

Nothing is executed until you call the query object itself ``q()`` and the return result is a generator so it will only serve up records as we ask. The return type is a Python ``dict`` because they are simple, fast, and work well for a return type.

```python
>>> from query import query
>>> q = query(layer).where("postcode > 6164 OR postcode < 6167")
>>> type(q)
<class 'query.Query'>
>>> results = q()
>>> type(results)
<generator object <genexpr> at 0x1A8DDD78>
>>> results.next()
{
u'old': u'http://www.seabreeze.com.au|mylink', 
u'pin_string': u'286633', 
'qgs_geometry': <qgis.core.QgsGeometry object at 0x1A8DF588>, 
u'bool': u'F', 
u'location': None, 
u'lot': u'LOT 79', 
'qgs_feature': <qgis.core.QgsFeature object at 0x1A8DF0C0>
}
```

### Select support

What is the point of a query if you can't ask it to give you just what you need?

```python
>>> q = (query(layer).where("postcode > 6164 OR postcode < 6167")
                     .select('assessment','address', 'lot',
                              geom = lambda f: f.geometry().buffer(20,3),
                              mylot = lambda f: int(f['house_numb']) * 100))
>>> q().next()
{
'geom': <qgis.core.QgsGeometry object at 0x1A8E64B0>, 
'assessment': u'4309719', 
'mylot': 7900, 
'lot': u'LOT 79', 
'address': u'BIRCHLEY RD'
}
```
 
You can use ``"colname"`` or any Python callable in the select statement.  Using keyword arguments is the same as ``"Col" AS MyName`` in SQL.

### On the TODO list

I would really like to have some kind of index support in the future to make queries run faster. I had basic index support working using a ``dict`` however it was nothing smart and was hard coded. ``QgsExpression`` does provide support to walk the generated tree see what the expression includes.  In "theory" it would involve walking the expression tree and calculating what should be used for index lookup.

Join support would also be nice. Attribute and spatial.

### Helpers welcome

Like I said at the start, this is just a hobby project and it's still only in early days however I am always happy for help if you have ideas, or know how to improve something.  If you find it handy that would be cool to know too.

### Installing

- Just download the code from [here](https://github.com/NathanW2/little-pyqgis-query-engine/zipball/master). 
- Add the files to your Python project
- ``from query import query``



