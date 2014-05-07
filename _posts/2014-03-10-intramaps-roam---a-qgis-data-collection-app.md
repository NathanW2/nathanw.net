---
layout: post
title: "IntraMaps Roam - A Python QGIS data collection app"
description: ""
category: 
tags: [roam, qgis]
---

For the last couple of months I, though [Digital Mapping Solutions](http://www.mapsolutions.com.au), have been working on a tablet friendly data collection application that has been built on Python and QGIS. For those of you who have seen my QMap project I started a year or so ago you can consider this a reincarnation of that project, and that project retired. Most of the code has been reworked and using the QGIS libs gave me full flexibility in layout and workflow.

IntraMaps Roam (or Roam for short) is a standalone, fully bundled, Python application that was created to do data collection with a QGIS backend. The primary use of Roam is in a disconnected setup were one might not have internet connection, however Roam is using QGIS so will support any data format QGIS does. You can can use Roam in a connected environment, if your internet premits, by having WFS and WMS layers, or direct database connections; it's up to you.  Roam forms also allow for custom logic to be added to each form using Python so you can add your own workflow if needed.

![Roam Map Window](http://i.imgur.com/F4TZScJ.png "Map Window") 
![Roam Data Capture](https://github.com/DMS-Aus/Roam/wiki/images/capture.png "Data capture")

The binary package comes with a config manager application that can be used to create and manage Roam projects

![Config Manager](https://github.com/DMS-Aus/Roam/wiki/images/config_form.png "Config Manager")
![Config Manager](https://github.com/DMS-Aus/Roam/wiki/images/config_preview.png "Form preview")

The [release page](https://github.com/DMS-Aus/Roam/releases/tag/v2.0) contains links to the 2.0 installers. The [wiki](https://github.com/DMS-Aus/Roam/wiki) contains all the information to get started.  You can also take a look at the [FAQ](https://github.com/DMS-Aus/Roam/wiki/FAQ) for the common questions.

Roam has been a great exercise in using and bundling QGIS libs with a Python application, which I have never done before but turned out to be pretty easy.  Being a fully bundled application means you don't need to install QGIS, or Python, on the client in order to run the application. Everything is in a nice bundled exe.

As Roam is based on PyQt and QGIS it is under the GPL2 license. Pull requests are welcome.

Currently Roam is only being packaged for Windows, because that was our first priority, however there isn't a lot of Windows only stuff in the code itself so creating a version for OS X and Linux shouldn't be too hard for someone with the know how.

Links

- [https://github.com/DMS-Aus/Roam/releases/tag/v2.0](https://github.com/DMS-Aus/Roam/releases/tag/v2.)
- [https://github.com/DMS-Aus/Roam/wiki](https://github.com/DMS-Aus/Roam/wiki)
- [https://github.com/DMS-Aus/Roam/wiki/FAQ](https://github.com/DMS-Aus/Roam/wiki/FAQ)

Happy mapping!?
