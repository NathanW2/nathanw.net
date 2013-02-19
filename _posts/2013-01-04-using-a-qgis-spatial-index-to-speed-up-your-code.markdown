---
comments: true

layout: post
slug: using-a-qgis-spatial-index-to-speed-up-your-code
title: Using a QGIS spatial index to speed up your code
wordpress_id: 1251
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- qgis
- Quantum GIS
- spatial operations
---

{% excerpt %}

If you need to do any kind of spatial operations in QGIS using Python or C++ you really want them to be as fast a possible in order reduce the amount of time you make the user wait. Lets take the simple scenario of a recent question that was asked on gis.stackexchange; [Summing up values of neighboring polygons?](http://gis.stackexchange.com/questions/44832/how-to-sum-up-values-of-neighbouring-polygons).

{% endexcerpt %}

I went for the SQL approach as I like how quick SQL can express what you need to do, however SQL is not the only way to skin a cat as [spatialthoughts](http://gis.stackexchange.com/users/5160/spatialthoughts) has shown in his [blog post](http://qgistips.spatialthoughts.com/2012/12/find-neighbor-polygons-in-layer-in-qgis.html). Here Ujaval has used Python to find the neighboring polygons of each feature. Running the script on a small dataset yields results in reasonable time however running it on a larger dataset can take a long time.

In order to check if a feature touches another you need to have two features to compare against each other. The simple way to do this is to create two loops where you check each feature against every other feature. Here is a quick code example of just that.

{% highlight python %}
layer = qgis.utils.iface.activeLayer()
# Select all features along with their attributes
allAttrs = layer.pendingAllAttributesList()
layer.select(allAttrs)
# Get all the features to start
allfeatures = {feature.id(): feature for (feature) in layer}

def noindex():
    for feature in allfeatures.values():
        for f in allfeatures.values():
            touches = f.geometry().touches(feature.geometry())
            # It doesn't matter if we don't return anything it's just an example

import timeit
print "Without Index: %s seconds " % timeit.timeit(noindex,number=1)
{% endhighlight %}

So the above code is pretty simple, just loop each feature and check against every other feature. No worries. No worries at least until you run this on a large dataset then I think you can see the issue here. Running the above code on a layer with around 28000 features takes 1912.41 seconds - that's 31 minutes. Holy crap!

Note: We put all the features of the layer into a dictionary as it will make lookup quicker in the later index example.

How can we speed up the above code? Lets take a gander at [QgsSpatialIndex](http://www.qgis.org/api/classQgsSpatialIndex.html)

### QgsSpatialIndex to rule them all

QgsSpatialIndex is a wrapper around the open source [SpatailIndex lib](http://libspatialindex.github.com/) and uses a RTree for an index method. If you don't know what an index is you can think of it like the index in a book - a pointer to a location in the book rather then having to scan every page to find a word.

There isn't much to using QgsSpatialIndex just insert each QgsFeature and it handles the rest, when we need something out we just use the intersects method to return any features inside an area.

{% highlight python %}
  layer = qgis.utils.iface.activeLayer()
  # Select all features along with their attributes
  allAttrs = layer.pendingAllAttributesList()
  layer.select(allAttrs)
  # Get all the features to start
  allfeatures = {feature.id(): feature for (feature) in layer}

  def withindex():
      # Build the spatial index for faster lookup.
      index = QgsSpatialIndex()
      for f in allfeatures.values():
              index.insertFeature(f)

      # Loop each feature in the layer again and get only the features that are going to touch.
      for feature in allfeatures.values():
        # Get the ids of all the features in the index that are within
        # the bounding box of the current feature because these are the ones
        # that will be touching.
        ids = index.intersects(feature.geometry().boundingBox())
        for id in ids:
          f = allfeatures[id]
          if f == feature: continue
          touches = f.geometry().touches(feature.geometry())
          # It doesn't matter if we don't return anything it's just an example

  import timeit
  print "With Index: %s seconds " % timeit.timeit(withindex,number=1)
{% endhighlight %}

Running this code on our 28000 feature layer returns the results in 10 seconds. 31 minutes down to 10 seconds by just using a spatial index. Nice!

So the next time you need to do some spatial operations remember to use the handy QgsSpatialIndex in order to speed up your code. If you don't want to use QgsSpatialIndex, or need some more flexiblity, you could even use the [Python RTree](http://toblerity.github.com/rtree/index.html) module.

### Full code

{% highlight python %}
  layer = qgis.utils.iface.activeLayer()

  # Select all features along with their attributes
  allAttrs = layer.pendingAllAttributesList()
  layer.select(allAttrs)
  # Get all the features to start
  allfeatures = {feature.id(): feature for (feature) in layer}

  def noindex():
    	for feature in allfeatures.values():
    		for f in allfeatures.values():
    			touches = f.geometry().touches(feature.geometry())
    			# It doesn't matter if we don't return anything it's just an example

  def withindex():
    	# Build the spatial index for faster lookup.
    	index = QgsSpatialIndex()
    	map(index.insertFeature, allfeatures.values())

    	# Loop each feature in the layer again and get only the features that are going to touch.
    	for feature in allfeatures.values():
    	  ids = index.intersects(feature.geometry().boundingBox())
    	  for id in ids:
    	    f = allfeatures[id]
    	    touches = f.geometry().touches(feature.geometry())
    	    # It doesn't matter if we don't return anything it's just an example

  import timeit
  print "With Index: %s seconds " % timeit.timeit(withindex,number=1)
  print "Without Index: %s seconds " % timeit.timeit(noindex,number=1)
{% endhighlight %}


