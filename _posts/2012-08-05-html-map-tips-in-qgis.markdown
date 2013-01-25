---
comments: true
date: 2012-08-05 21:35:17
layout: post
slug: html-map-tips-in-qgis
title: HTML map tips in QGIS
wordpress_id: 1098
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- mapping
- Open Source
- qgis
- styling
- tips
---

New fresh QGIS feature! So fresh in fact you can still smell the wet paint :)

QGIS (development build) can [now](https://github.com/qgis/Quantum-GIS/commit/8aa160bcb3548a881248c7d46d92c4f2e12ffc02) display map tips using HTML (a [subset](http://doc.qt.nokia.com/4.7-snapshot/richtext-html-subset.html) anyway).

To enable the new map tips: Open the Layer Properties dialog for a layer and select the Display tab

[caption id="attachment_1099" align="aligncenter" width="616"][![](http://woostuff.files.wordpress.com/2012/08/html.png)](http://woostuff.files.wordpress.com/2012/08/html.png) Display tab to set HTML map tips[/caption]


## In action


[caption id="attachment_1100" align="aligncenter" width="616"][![](http://woostuff.files.wordpress.com/2012/08/html-inaction.png)](http://woostuff.files.wordpress.com/2012/08/html-inaction.png) Layer properties for HTML map tip[/caption]

Notice how we can also use a QGIS expression. Anything inside `[% %]` will be evaluated and replaced with the value in real-time. We can even use a CASE statement. Pretty cool!

And the result when hovering over a feature

[caption id="attachment_1101" align="aligncenter" width="630"][![](http://woostuff.files.wordpress.com/2012/08/html-inaction2.png)](http://woostuff.files.wordpress.com/2012/08/html-inaction2.png) HTML in QGIS map tip? Yes! WOOT![/caption]

Hold on. Pause the track! We can even use some CSS to make it more fancy.

{% highlight html %}
<style>
h1 {color:red;}
p.question {color:blue;}
</style>
<h1> [% "NAME" %] </h1>
<br>
<img src="[% "image" %]" />
<br>
<p class="question">Is this place a country?</p>
<br>
[% CASE WHEN "TYPE" = 'Country' THEN 'Yes' ELSE 'No. It is a ' || "TYPE" END %]
{% endhighlight %}

[caption id="attachment_1105" align="aligncenter" width="576"][![](http://woostuff.files.wordpress.com/2012/08/css.png)](http://woostuff.files.wordpress.com/2012/08/css.png) CSS in a html map tip[/caption]

Happy Mapping :)
