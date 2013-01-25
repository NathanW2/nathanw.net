---
comments: true
date: 2012-06-23 01:08:24
layout: post
slug: styling-temporal-time-data-in-qgis
title: Styling temporal (time) data in QGIS
wordpress_id: 1024
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- Open Source
- osgeo
- qgis
- Quantum GIS
- styling
---

So this years first uni semester is done and dusted, now I have some free time.  Blog all the things!

This is a follow up post for [discussion](http://www.linkedin.com/groupAnswers?viewQuestionAndAnswers=&discussionID=124557348&gid=2290177&commentID=84854003&trk=view_disc&ut=0yI5KvRgSoTRg1) that was started on LinkedIn about showing features older, or newer, then a certain date different colours   The main post was about using free, or low cost, solutions in order to aid in mapping water networks. I recommend that everyone watch it. A very good presentation.

I recommended that you could use the rule based rendering engine but the expression engine in QGIS doesn't have any date functions yet.  All good we can add them if we need and once I get my head around the expression engine I plan on doing exactly that. But for now we can do it a different way.

We are going to use Spatialite, but any database will do (_syntax and process will vary_).

Lets have a look an inspection layer we have in our Spatialite database viewed in QGIS:

![](http://woostuff.files.wordpress.com/2012/06/quantum-gis-1-8.png)

Pretty boring and hard to see what has been done in the last 30 days.  Now with the lack of support for dates in the expression engine we have to use another methods.  For this example we will use the really handy DBManger plugin that now ships with QGIS from 1.8.  Load it, connect to your database, and run the following query:

{% highlight sql %}
SELECT id,
              CASE WHEN DATE("date_checked") > DATE('now', '-30 days') THEN
                         'Within 30 Days'
              ELSE
                         'older'
              END as age, date_checked, geom
FROM  "inspections"
{% endhighlight %}



[![](http://woostuff.files.wordpress.com/2012/06/sql-window-inspections.png)](http://woostuff.files.wordpress.com/2012/06/sql-window-inspections.png)
As you can see anything that is within the 30 days now has the "Within 30 Days" string in the age column, or else it has "older".  CASE statements can be very powerful things in SQL sometimes.

Now load it into QGIS, style, and label it using the new **age** column


[![](http://woostuff.files.wordpress.com/2012/06/styled.png)](http://woostuff.files.wordpress.com/2012/06/styled.png)


and [Bob's your uncle](http://en.wikipedia.org/wiki/Bob's_your_uncle)


[![](http://woostuff.files.wordpress.com/2012/06/inspections-by-age.png)](http://woostuff.files.wordpress.com/2012/06/inspections-by-age.png)


You now have a layer that is style based on age but is also dynamic.  Adding a new inspection point will now will be styled according to those rules. _(Although you will have to edit the normal inspection layer with it turned off as views/queries are not editable - without some setup anyway)_

It might be a simple thing to some but sometimes it's hard to find the right words to describe what you want when you are looking for this kind of thing. So hopefully this has helped a few people get started with visualizing their time/date based data in QGIS.

Happy mapping!
