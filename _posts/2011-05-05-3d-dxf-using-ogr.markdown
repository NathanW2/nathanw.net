---
comments: true

layout: post
slug: 3d-dxf-using-ogr
title: '3D DXF from MapInfo Tab or ESRI Shape (or anything) using OGR '
wordpress_id: 596
categories:
- MapInfo
- Open Source
tags:
- 3D
- ESRI
- gdal
- gis
- mapinfo
- mapping
- ogr
- Open Source
- OSS
---

**Note:The following post requires gdal 1.8**

A lot of times we need to send/use 3D dxf files, we used to use [FME](http://www.safe.com/) however FME is not free or cheap.  So I went looking for a free solution.

If you have gdal 1.8 it's just one simple command line run using, what is becoming my favorite GIS tool, ogr2ogr.

All you have to do is run:

{% highlight bash %}
ogr2ogr -f "DXF" {outFile} {inFile} -zfield {ColumnWithZValue}
{% endhighlight %}

So in my case I ran:
{% highlight bash %}
ogr2ogr -f "DXF" C:\Temp\contourswarwick.dxf C:\Temp\Contours.TAB -zfield Height
{% endhighlight %}

I haven't fully tested it but {outfile} can be any file ogr supports. 

and the output:

[![Top view of contours](http://woostuff.files.wordpress.com/2011/05/before.png)](http://woostuff.files.wordpress.com/2011/05/before.png)

[![Contours side view](http://woostuff.files.wordpress.com/2011/05/after.png)](http://woostuff.files.wordpress.com/2011/05/after.png)

In the words of, the not so great, Charlie Sheen. WINNING!

Happy mapping :D
 
