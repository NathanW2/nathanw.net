---
comments: true
date: 2011-03-05 21:59:40
layout: post
slug: mapinfo-map-control-into-qt-python-form
title: MapInfo map control into Qt Python form
wordpress_id: 527
categories:
- MapInfo
- Mapinfo Programming
- Open Source
tags:
- gis
- mapinfo
- mapinfo interop
- mapinfo ole
- MapInfo Professional
- mapping
- Open Source
- python
---

Tonight for a bit of fun, or shits and jiggles as we say here, I thought I would try and embed a MapInfo map control into a Qt python widget (although I should be studying, but it's Saturday night) .

Turns out it is pretty easy!

pls send me teh codez? OK here you go.

[sourcecode language="python"]
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from win32com.client import Dispatch
import sys

app = QApplication(sys.argv)
app.setAttribute(Qt.AA_NativeWindows,True)
wnd = QMainWindow()
wnd.resize(400, 400)
widget = QWidget()
wnd.setCentralWidget(widget)
wnd.show()

handle = int(widget.winId())
mapinfo = Dispatch("MapInfo.Application")
mapinfo.do('Set Next Document Parent %s Style 1' % handle)
mapinfo.do('Open Table "D:\GIS\MAPS\Property.TAB"')
mapinfo.do('Map from Property')

app.exec_()
[/sourcecode]

The above code will load MapInfo and open the property layer into the Qt Widget control, with the result below.

[![](http://woostuff.files.wordpress.com/2011/03/mapinfo.png)](http://woostuff.files.wordpress.com/2011/03/mapinfo.png)


So this means you don't "always" have to write your MapInfo based apps in C# or C++; of course I already knew this as anything that can use OLE and provide a native window handle to MapInfo will work, I just never tried it.
