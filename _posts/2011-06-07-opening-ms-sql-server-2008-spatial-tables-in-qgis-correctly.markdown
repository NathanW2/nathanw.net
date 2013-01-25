---
comments: true
date: 2011-06-07 15:47:36
layout: post
slug: opening-ms-sql-server-2008-spatial-tables-in-qgis-correctly
title: Opening MS SQL Server 2008 Spatial tables in QGIS - Correctly
wordpress_id: 662
categories:
- Open Source
- qgis
tags:
- gis
- map-rendering
- mapping
- MS SQL Server 2008
- MS SQL Spatial
- ogr
- Open Source
- OSS
- qgis
- Quantum GIS
---

**EDIT (22-07-12): QGIS 1.8 and above now ships with a native MS SQL data provider.  Look for Add MSSQL Spatial Layer in the Layer menu.**

Turns out the [last blog post](http://woostuff.wordpress.com/2011/03/13/opening-ms-sql-spatial-in-qgis/) I did on this subject contained a few errors, mainly that QGIS wouldn't render the layer when you opened it.

The answer is so obvious it's almost embarrassing :)

In order to open and display a SQL Server 2008 layer in QGIS correctly, via OGR, you must have a geometry_columns table in your database with the name, geometry type and srid of the layer. That's it! Oh look, it was even right in front of me in the OGR code for the mssqlspatial driver.

{% highlight cpp %}
int OGRMSSQLSpatialTableLayer::FetchSRSId()
{
    CPLODBCStatement oStatement = CPLODBCStatement( poDS->GetSession() );
    oStatement.Appendf( "select srid from geometry_columns "
                    "where f_table_schema = '%s' and f_table_name = '%s'",
                    pszSchemaName, pszTableName );

    if( oStatement.ExecuteSQL() && oStatement.Fetch() )
    {
        if ( oStatement.GetColData( 0 ) )
            nSRSId = atoi( oStatement.GetColData( 0 ) );
    }

    return nSRSId;
}
{% endhighlight %}

**So the process to open a MS SQL 2008 spatial layer in OGR is as follows.**

There are two main tables which tell OGR how to read a layers projection:



	
  * geometry_columns

	
  * spatial_ref_sys


_**geometry_columns**_ contains the table name and the key for the table _**spatial_ref_sys**_ which contains the projection string. The projection string is the info that QGIS needs in order to correctly render a layer.

The easiest way to get the correct tables is to let OGR handle it for you via ogr2ogr, then just adding any other tables you may have already in your database to the geometry_columns table.

So to get ogr2ogr to create the right tables for you it's as simple as running the following command from inside the OSGeo4W shell, changing the connection string part of course:

{% highlight bash %}
ogr2ogr -overwrite -f MSSQLSpatial "MSSQL:server=.\MSSQLSERVER2008;database=geodb;trusted_connection=yes" "rivers.tab"
{% endhighlight %}

_(sample taken from [http://www.gdal.org/ogr/drv_mssqlspatial.html](http://www.gdal.org/ogr/drv_mssqlspatial.html))_

Uploading even just one table this way will create both tables and fill in the needed info.
The **geometry_columns **table:

f_table_catalogf_table_schemaf_table_namef_geometry_column








geodb


dbo


rivers


ogr_geometry




coord_dimensionsridgeometry_type








2


32768


POLYGON




The **spatial_ref_sys **table:

sridauth_nameauth_sridsrtextproj4text








32768


NULL


NULL


PROJCS["UTM_Zone_56_Southern_Hemisph....


+proj=utm +zone=56 +south +ellps=GRS80 +units=m +no_defs




So if you have already existing tables in your MS SQL 2008 database that were loaded, via say MapInfo's EasyLoader, you would just upload one table via ogr2ogr to create the two tables needed by QGIS(using OGR) and then add the other tables to the geometry_columns table. If they are all in the same projection than you are in luck as you will only need to upload one in order to get the right strings in the spatial_ref_sys table, if not just upload a small sample for each projection.

Then you can open the table in QGIS using:

{% highlight python %}
uri = "MSSQL:server={serverName};database={databaseName};tables={tableName};trusted_connection=yes"
qgis.utils.iface.addVectorLayer(uri,'{yourLayerNameHere}','ogr')
{% endhighlight %}

**Tip:** In order to test you have correctly set the table in geometry_columns you can run another ogr tool ogrinfo:

{% highlight bash %}
ogrinfo -al "MSSQL:server=localhost;database={your database};tables={your table}" -fid 1
{% endhighlight %}

If you see a value in Layer SRS WKT: then chances are it's set right and QGIS should be able to render it, however if you see: Layer SRS WKT:(unknown) Than chances are QGIS will not render it correctly.

Hopefully this help people use MS SQL 2008 Spatial with QGIS, a important step I think in the world of using QGIS on Windows (especially when you don't have the freedom to run PostGIS:) ).

I might even do a video tutorial when I get some free time after my exams and my wedding.
