---
layout: post
title: "Installing QGIS using apt on windows (OSGeo4W)"
description: ""
category:  
tags: [OSGeo4W]
---



Here is a handy tip to be able to install and update OSGeo4W packages, things like QGIS, GRASS, etc, using the apt utility from OSGeo4W.  apt is a command line utility that you can install using OSGeo4W and then run using the OSGeo4W Shell.



First install apt via OSGeo4W

{% image osgeo.png %}
{% endimage %}

Now open the OSGeo4W Shell 

{% image shell.png %}
{% endimage %}

from here you can run the `apt` utility. 

The basic commands are `apt update`, `apt install {package}`, `apt upgrade`

## Installing nightly QGIS

For a quick example we will install qgis-dev. 

From the shell we can just run:

{% highlight bash %}
apt setup
apt update
apt install qgis-dev
{% endhighlight %} 

{% image qgis-dev-install.png %}
{% endimage %}

`apt` will install all the needed dependencies

Done!

## Script for updating nightly QGIS

So the good thing about using `apt` is if you wanted to make a quick batch file that you can run to update to the nightly build it's as simple as

{% highlight bash %}
@echo off
set OSGEO4W_ROOT=C:\OSGeo4W
set PATH=%OSGEO4W_ROOT%\bin;%PATH%

apt update
apt install qgis-dev
pause
{% endhighlight %}

Now you can just run the batch file to update your QGIS to the nightly build.

### Extra tip

If you just want to upgrade all the packages you have installed you can do: 

{% highlight bash %}
apt setup
apt upgrade
{% endhighlight %} 

Simple

{% include JB/setup %}
