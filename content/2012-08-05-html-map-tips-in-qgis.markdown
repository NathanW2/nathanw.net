slug: html-map-tips-in-qgis
title: HTML map tips in QGIS
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

New fresh QGIS feature! So fresh in fact you can still smell the wet paint :)

QGIS (development build) can [now](https://github.com/qgis/Quantum-GIS/commit/8aa160bcb3548a881248c7d46d92c4f2e12ffc02) display map tips using HTML (a [subset](http://doc.qt.nokia.com/4.7-snapshot/richtext-html-subset.html) anyway).

To enable the new map tips: Open the Layer Properties dialog for a layer and select the Display tab

![Alt Text](/images/http://woostuff.files.wordpress.com/2012/08/html.png)

## In action

![Alt Text](/images/http://woostuff.files.wordpress.com/2012/08/html-inaction.png)

Notice how we can also use a QGIS expression. Anything inside `[% %]` will be evaluated and replaced with the value in real-time. We can even use a CASE statement. Pretty cool!

And the result when hovering over a feature

![Alt Text](/images/http://woostuff.files.wordpress.com/2012/08/html-inaction2.png)

Hold on. Pause the track! We can even use some CSS to make it more fancy.

```html
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
```

![Alt Text](/images/http://woostuff.files.wordpress.com/2012/08/css.png)

Happy Mapping :)
