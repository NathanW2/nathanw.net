slug: qgis-now-with-100-more-ms-sql-2008-support
title: QGIS now with 100% more MS SQL Server 2008 support
categories:
- Open Source
- qgis
tags:
- MS SQL Server 2008
- MS SQL Spatial
- Open Source
- osgeo
- qgis
- Quantum GIS

_Ok the title is a bit of a lie. QGIS did support MS SQL Server 2008 before by using OGR but this is a native provider so it's a lot more integrated.._

Good news everyone!

QGIS now has a native MS SQL 2008 provider. The provider can found using the new toolbar button (purple icon) or in the MS SQL node in the QBrowser tree. The provider also supports drag and drop import.

The work was sponsored by [Digital Mapping Solutions](http://www.mapsolutions.com.au/) (Australia) and completed by [Tamas Szekeres](http://szekerest.blogspot.com.au/)

Any bugs can be assigned to "tamas" on hub.qgis.org.

A big thanks to both [Digital Mapping Solutions](http://www.mapsolutions.com.au/) and Tamas.

This addition will open QGIS up to a whole new set of users who have to use MS SQL but love QGIS.

Currently this is only in master but I will be in the 1.8 release when it comes out.

_Note: At the moment you have to have a geometry_columns table in the database in order to connect, this table is the same format used by PostGIS and can be made by importing a layer using the [ogr2ogr method](/2011/06/07/opening-ms-sql-server-2008-spatial-tables-in-qgis-correctly/). There will be a fix coming for this at some stage._
