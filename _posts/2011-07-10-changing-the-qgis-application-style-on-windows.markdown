---
comments: true
date: 2011-07-10 11:26:55
layout: post
slug: changing-the-qgis-application-style-on-windows
title: Changing the QGIS application style on Windows
wordpress_id: 756
categories:
- Open Source
- qgis
tags:
- gis
- Open Source
- qgis
- Quantum GIS
---

By default QGIS uses the Qt QPlastiqueStyle for all its windows which makes QGIS render all controls like this:

[caption id="attachment_757" align="aligncenter" width="630" caption="Default style for QGIS on windows."][![](http://woostuff.files.wordpress.com/2011/07/qplastiquestyle.png)](http://woostuff.files.wordpress.com/2011/07/qplastiquestyle.png)[/caption]

However it can be changed in order to make it fit in with system style, as in use Windows style. Running the following commands in the python console:

[sourcecode language="python"]
from PyQt4.QtGui import QApplication
QApplication.setStyle("windowsvista")
[/sourcecode]

will change QGIS to render controls in windows style:

[caption id="attachment_758" align="aligncenter" width="630" caption="QGIS using windows style."][![](http://woostuff.files.wordpress.com/2011/07/qwindowsstyle.png)](http://woostuff.files.wordpress.com/2011/07/qwindowsstyle.png)[/caption]

_It's quite hard to notice many of the differences but just try it you will see them_

However there is one limitation. QGIS will not remember that setting as the compiled binary forces QGIS running on Windows into QPlastiqueStyle.

I have started working on a patch to give the user a choice in the options which control rendering style they would like to use. I think choice in these situations is good because I have grown to like the QPlastiqueStyle, mainly because I have used it so much , but other people I know prefer the Windows Vista style controls.
