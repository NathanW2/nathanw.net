---
comments: true

layout: post
slug: user-defined-expression-functions-for-qgis
title: 'User defined expression functions for QGIS '
wordpress_id: 1190
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- Open Source
- OSS
- qgis
- Quantum GIS
---

Ever since I added [expression based labels](/2011/10/27/expression-based-labeling/), including the new expression builder UI, something that I always wanted to add is the ability to define custom user defined functions in Python (or C++) and use them in an expression. The expression engine is used for [labels](/2011/10/27/expression-based-labeling/), [rule](/2012/01/25/improvements-to-the-qgis-rule-based-rendering/) [based rendering](/2011/06/06/one-of-my-favorite-features-of-qgis/), layer actions, field calculator, and atlas composer tags.  Thanks to the all the awesome work on the expression engine by Martin all this cool stuff is now possible.

Today I pushed a [commit](https://github.com/qgis/Quantum-GIS/commit/a7699e2696efcb471ab84871aae7af406ca2a375) into master that adds the ability to define a function in Python (or C++), register it in the expression engine, then use it anywhere expressions are used.


## The good stuff


Lets take a use case from [Ujaval Gandhi](http://qgistips.spatialthoughts.com/2012/11/tip-count-number-of-vertices-in-layer.html) and his example of counting vertices for each feature.

First we need to import the new [`qgsfunction`](https://github.com/qgis/Quantum-GIS/blob/a7699e2696efcb471ab84871aae7af406ca2a375/python/utils.py#L375) decorator function from `qgis.utils`. The `qgsfunction` decorator will take a normal Python function, wrap it up in the class used to define a function, and register it in the engine.

So what does an empty function look like:

{% highlight python %}
from qgis.utils import qgsfunction
from qgis.core import QGis

@qgsfunction(0, "Python")
def vertices(values, feature, parent):
	pass
{% endhighlight %}

`@qgsfunction(0, "Python")` means we are defining a new vertices function that takes 0 args and lives in the "python" group in the expression builder UI. Any custom function must take `(values, feature, parent)` as python args. `values` is a list of QVariants passed into the function, `feature` is the current `QgsFeature`, and `parent` is expression engine node (you use this to raise errors).

Lets stick some more logic in there:

{% highlight python %}
from qgis.utils import qgsfunction
from qgis.core import QGis

@qgsfunction(0, "Python")
def vertices(values, feature, parent):
	"""
		Returns the number of vertices for a features geometry
	"""
	count = None
	geom = feature.geometry()
	if geom is None: return None
	if geom.type() == QGis.Polygon:
		count = 0
		if geom.isMultipart():
		  polygons = geom.asMultiPolygon()
		else:
		  polygons = [ geom.asPolygon() ]
		for polygon in polygons:
		  for ring in polygon:
		    count += len(ring)
	return count
{% endhighlight %}

Pretty simple. Get the geometry from the feature, check if it's a polygon, if it is then count the number of vertices and return that number.

Now that we have that all done we can save it into a file in our `.qgis/python` folder, lets call it **userfunctions.py** (note you don't have to save it here, anywhere that QGIS can find it will do.  Anywhere on PATH)

Lets open QGIS and run import **userfunctions.py:**

{% image http://woostuff.files.wordpress.com/2012/11/import.png %}
{% endimage %}

Now open the label properties for the layer:

{% image http://woostuff.files.wordpress.com/2012/11/expression.png %}
{% endimage %}

Nice! Notice also that the function doc string is used as the function help. How cool is that.  You can also see the $ sign in front of the function, this is because any functions that take no args are considered special and use the $ sign as a convention, this is all automatic when the function is registered.

And the result is:

{% image http://woostuff.files.wordpress.com/2012/11/result.png %}
{% endimage %}

You can even use it in the rule based rendering:

{% image http://woostuff.files.wordpress.com/2012/11/rules.png %}
{% endimage %}

Enjoy!


## Notes

  * You must unregister a function once you are finished with it using QgsExpression.unregisterFunction(name). This mainly applies to plugins where the user might unload your plugin and the code is no longer available. In the above example we could import userfunctions and never unregister because we plan on using it for the whole session.
	
  * You can't override the built-in methods.