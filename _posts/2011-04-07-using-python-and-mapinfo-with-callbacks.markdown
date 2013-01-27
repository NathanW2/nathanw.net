---
comments: true
date: 2011-04-07 23:12:10
layout: post
slug: using-python-and-mapinfo-with-callbacks
title: Using Python and MapInfo with Callbacks
wordpress_id: 582
categories:
- MapInfo
- Mapinfo Programming
- Open Source
tags:
- gis
- Mapbasic
- mapinfo
- mapinfo interop
- mapinfo ole
- MapInfo Professional
- mapping
- Open Source
- python
---

The other day I posted an entry about using MapInfo with Python and Qt (see [2011/03/05/mapinfo-map-control-into-qt-python-form/](2011/03/05/mapinfo-map-control-into-qt-python-form/)), one big thing that I missed was support for callbacks, which if you want to do anything related to integrated mapping is a must for map tool support.

Turns out it is pretty easy, and today I worked out how.

You will need to create a class in python that looks something like this:

{% highlight python %}
class Callback():
    _public_methods_ = ['SetStatusText']
    _reg_progid_ = "MapInfo.PythonCallback"
    _reg_clsid_ = "{14EF8D30-8B00-4B14-8891-36B8EF6D51FD}"
    def SetStatusText(self,status):
        print status
{% endhighlight %}

This will be our callback object that we will need to create for MapInfo.

First I will explain what some of the funny stuff is:



	
  * **_public_methods_** is a Python array of all the methods that you would like to expose to COM eg MapInfo in this case. This attribute is a must for creating a COM object.

	
  * **_reg_progid_** is the name of your COM application or object.  This can be anything you would like.

	
  * **_reg_clsid_** is the GUID, or unique id, for the object or app.  Do not use the one I have, call the following in a Python shell to create your own.
{% highlight python %}
         import pythoncom
         pythoncom.CreateGuid()
         {% endhighlight %}

	
  * **SetStatusText** is the MapInfo callback method that is called when the status bar changes in MapInfo.


In order to use the class as a COM object we have two more steps to complete, one is registering the COM object and the other is creating it.

First, in oder to register the object we call the following code from our main Python method:

{% highlight python %}
if __name__ == "__main__":
    print "Registering COM server..."
    import win32com.server.register
    win32com.server.register.UseCommandLine(Callback)
    main()
{% endhighlight %}

This will register the COM object which will mean it can then be creating for use by MapInfo.

In order to create our callback in Python we call:

{% highlight python %}
callback = win32com.client.Dispatch("MapInfo.PythonCallback")
{% endhighlight %}

and set it as our callback object for MapInfo:

{% highlight python %}
mapinfo.SetCallback(callback)
{% endhighlight %}

So after all that the final code looks like this:

{% highlight python %}
def main():
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
    callback = win32com.client.Dispatch("MapInfo.PythonCallback")
    mapinfo.SetCallback(callback)
    mapinfo.do('Set Next Document Parent %s Style 1' % handle)
    mapinfo.do('Open Table "D:\GIS\MAPS\Property.TAB"')
    mapinfo.do('Map from Property')

    app.exec_()

class Callback():
    """ Callback class for MapInfo """
    _public_methods_ = ['SetStatusText']
    _reg_progid_ = "MapInfo.PythonCallback"
    _reg_clsid_ = "{14EF8D30-8B00-4B14-8891-36B8EF6D51FD}"
    def SetStatusText(self,status):
        print status

if __name__ == "__main__":
    print "Registering COM server..."
    import win32com.server.register
    win32com.server.register.UseCommandLine(Callback)
    main()
{% endhighlight %}

and the result is a map window and information printed to the console.

[caption id="attachment_591" align="aligncenter" width="630" caption="Information from MapInfo callback"][![](http://woostuff.files.wordpress.com/2011/04/image001.png)](http://woostuff.files.wordpress.com/2011/04/image001.png)[/caption]

I think Python could be a good language to prototype MapInfo based app, or even build a whole app itself.   If you do end up making something of it let me know I am quite interested with what people could come up with.
