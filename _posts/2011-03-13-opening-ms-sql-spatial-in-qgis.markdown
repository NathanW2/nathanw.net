---
comments: true
date: 2011-03-13 22:44:45
layout: post
slug: opening-ms-sql-spatial-in-qgis
title: Opening MS SQL Server 2008 Spatial tables in QGIS
wordpress_id: 559
categories:
- Open Source
- qgis
tags:
- gis
- mapping
- MS SQL Server 2008
- MS SQL Spatial
- Open Source
- OSS
- python
- qgis
- Quantum GIS
---

**EDIT:  If you are having trouble opening MS SQL 2008 in QGIS I will have a blog post coming explaining how to correct it. Or you can read the comments between **TheGeoist and I below which will have the answer.****

Just a quick tip.

Thanks to GDAL/OGR 1.8 QGIS can now open MS SQL Server 2008 spatial tables via the OGR [MSSQLSpatial driver](http://www.gdal.org/ogr/drv_mssqlspatial.html).

First you must be running a version of QGIS that is using GDAL/OGR 1.8.  Opening the QGIS about page will tell you if it is supported.

[![](http://woostuff.files.wordpress.com/2011/03/version.png)](http://woostuff.files.wordpress.com/2011/03/version.png)

As I am writing this on my Ubuntu install I only have version 1.6.3 but the latest dev version of QGIS (upcoming 1.7 release) for Windows in the OSGeo4W installer is complied with version 1.8.

Now open the python console in QGIS and type the following:

{% highlight python %}
uri = "MSSQL:server={serverName};database={databaseName};tables={tableName};trusted_connection=yes"
qgis.utils.iface.addVectorLayer(uri,'{yourLayerNameHere}','ogr')
{% endhighlight %}

Replacing {serverName} with your server name, if installed on your local machine you can use localhost; {databaseName} with the name of the database with the tables;{tableName} with the table to open; {yourLayerNameHere} with the name you would like the layer to have in the map legend.

After that you should see your MS SQL Spatial table displayed in QGIS, with editing support.

At the moment there is no nice interface in QGIS to open MS SQL tables like there is for PostGIS, although that might be a good plugin project for someone to work on.
