---
comments: true
date: 2011-03-08 14:23:31
layout: post
slug: getting-ecw-and-mrsid-support-working-in-qgis-dev-osgeo4w-install
title: Getting ECW and MrSID support working in QGIS dev OSGeo4W install
wordpress_id: 491
categories:
- Open Source
- qgis
tags:
- ecw
- gis
- mapping
- mrsid
- Open Source
- qgis
- Quantum GIS
- raster
---

_Note:  This post is about getting ecw and mrsid support working in the trunk (qgis-dev) version of QGIS which is installed with the OSGeo4W installer.  Non-dev versions seem to work fine following this method: [http://www.qgis.org/wiki/OSGeo4wSetup#Installing_support_for_raster__.2A.ECW_.28ERMapper.29_and_.2A.sid_.28MrSid.29_formats](http://www.qgis.org/wiki/OSGeo4wSetup#Installing_support_for_raster__.2A.ECW_.28ERMapper.29_and_.2A.sid_.28MrSid.29_formats) _

Getting ECW and MrSID support into QGIS can be a real pain in the butt when you first try; but once you know how it's easy.

If you try to open a ecw file in QGIS you will get this nice little error message:

[](http://woostuff.files.wordpress.com/2011/03/error.png)[![](http://woostuff.files.wordpress.com/2011/03/error3.png)](http://woostuff.files.wordpress.com/2011/03/error2.png)

What?  I thought QGIS supported ECW files!

Turns out it does, but the team are not able to ship the required libs with the program due to licensing restrictions by ERDAS.   Luckily adding support is not "too" hard.



	
  1. First head over to [http://www.erdas.com/products/ERDASECWJPEG2000SDK/Downloads.aspx](http://www.erdas.com/products/ERDASECWJPEG2000SDK/Downloads.aspx)

	
  2. Click **Download Now** for the ERDAS ECW/JP2 SDK Desktop Read-Only, Version 4.1 libs,

	
  3. Fill out a bit of registration details and click though all the pages (_this is the most painful process I have ever had to go though to get some libs for a program, ERDAS should be ashamed that it is such an effort._)

	
  4. Once you have download **_ECWJP2SDKSetup_RO_20100920.exe_**; install it.

	
  5. Copy all the files from **C:\Program Files\ERDAS\ERDAS ECW JPEG2000 Read SDK\bin\vc90\win32** into the bin folder of your **OSGeo4W install **(default is C:\OSGeo4W\bin)
You can open the OSgeo4W shell and run: _**copy "C:\Program Files\ERDAS\ERDAS ECW JPEG2000 Read SDK\bin\vc90\win32\*.dll" %OSGEO4W_ROOT%\bin **_to do the same thing.

	
  6. Launch **osgeo4w-setup.exe**, the installer that you used to install qgis-dev,  and select  **gdal-ecw, gdal17-ecw** and **gdal-mrsid, gdal17-sid **under the libs section. Let it install the needed libs and any dependencies.

	
  7. Open _**%OSGEO4W_ROOT%\bin **_and search for **qgis-dev.bat; **open it with a text editor and add the following line:
**set GDAL_DRIVER_PATH="%OSGEO4W_ROOT%"\bin\gdalplugins\1.8
**I always insert it just after  SET OSGEO4W_ROOT=

	
  8. Launch qgis-dev.bat

	
  9. Open a ecw


[![](http://woostuff.files.wordpress.com/2011/03/ecw.png)](http://woostuff.files.wordpress.com/2011/03/ecw.png)

I have tested this on a couple of machines now but as always


![](http://woostuff.files.wordpress.com/2011/03/works-on-my-machine-starburst.jpg)


with no guarantee that it will work on yours :)  (_Although it should_)
