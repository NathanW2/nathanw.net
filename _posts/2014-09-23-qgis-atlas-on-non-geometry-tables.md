---
layout: post
title: "QGIS atlas on non geometry tables"
description: ""
category: 
tags: [atlas, qgis]
---

This is proof that no matter how close you are to a project you can still miss some really cool stuff that you never knew or considered was possible.  

The problem to solve:

> You have a CSV with a row of colours. Each row should be a new map and each column is the colour for that feature.

This is example of that kind of input

```
A	    B
#93b2f3	#FF0000	
#dfbdbb	#FF0000
#f9d230	#FF0000
``` 

This questhion was asked on [GIS.SE](http://gis.stackexchange.com/q/114746/97) this morning.  When I first saw it I had no idea it was even possible, I was thinking along the same lines as the person asking, that it would have to be done with Python. Not hard, but a lot harder then something built in and I put it in the too hard basket.  I thought the atlas can almost do that, almost but not really.

Well *almost* was wrong. It can.

**Note: You will need QGIS 2.5 (2.6 when released) for this to work**

### Lets make some cool maps! (and go to [GIS.SE](http://gis.stackexchange.com/q/114746/97) and upvote [Nyalls](nyalldawson.net) answer)

First open your vector layer and the CSV. Don't worry about style just yet, we will do it later.

Create a composer and add your map.

Here comes the first part of the trick.

Enable Atlas and set the coverage layer to the **CSV layer**. Wait? What? That doesn't make any sense. If you think about it for a while it does. We need a map for each row (or "feature") in the CSV and atlas does just that. 

{% image atlas_colours.png %}
{% endimage %}

How do we style the features? Well here is the other part of the trick. In 2.6 there is a magic expression function that returns a field value from another feature. And it's as simple as `attribute(  $atlasfeature , 'A' )` - give me the attribute from the current atlas feature for field 'A'. Simple.

First we categorize our features so we have a symbol for each feature. I'm using a sample layer I have but you can understand how this works. The first feature is A and the other is B, etc, etc

{% image render.png %}
{% endimage %}

Now to use another awesome feature of QGIS. The data defined symbol properties (and labels too).  Change each symbol and define the colour data defined property. Using `attribute(  $atlasfeature , 'A' )` for the first one and `attribute(  $atlasfeature , 'B' )` for the second.

{% image atlas_feature.png %}
{% endimage %}

That is it.  Now jump back over to your composer and enable Atlas preview.

{% image atlas1.png %}
{% endimage %}

{% image atlas2.png %}
{% endimage %}

Bam! Magic!  How awesome is that!

Now my other thought was. "Ok cool, but the legend won't update". I should learn by now not to assume anything. The legend will also update based on the colours from the feature.

{% image atlas1_legend.png %}
{% endimage %}

{% image atlas2_legend.png %}
{% endimage %}

How far can we take this.  What if you need the label to match the colour. Simple just make the label text look like this:

```
<h1 style='color:[% "A" %]'>This is the colour of A</h1>
```

{% image atlas1_label.png %}
{% endimage %}

Heaps of credit to Nyall and the others who have added all this great stuff to the composer, atlas, and the data defined properties.  It's not something that you will do every day but it's great to see the flexibility of QGIS in these situations.

You can even make the background colour of the page match the atlas feature

{% image atlas1_back.png %}
{% endimage %}

but don't do that because people might think you are mad ;)

