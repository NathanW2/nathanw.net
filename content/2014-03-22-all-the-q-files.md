title: What are all these QGIS file types? Why do I need them
tagline: "or: Lions and tigers and bears! Oh my!"
description: "QML, QLR, QGS. What are all these different files?"
category: 
tags: []

After I added the new QGIS Layer Definition feature in QGIS I have noticed some indirect feedback regarding its use. I thought I would do this post in order to clear things up regarding the new feature so that we are all on the same page.

Some of this feedback, or I could say confusion, was mainly "Why not use the qml format?" or "How is it different from a project file".  I can understand this confusion because they do kind of look and act the same however they are a little different.

I'm going to work my way up from the bottom up in terms of file levels and their use.

### The QML file (.qml)

**It contains:** Style information

The QML (.qml) file in QGIS is a style file.  It contains an export of the style information, including labels, from a layer.  The .qml file however has no reference to the layer. This means I can share a .qml file with you and you can apply it to your own data without needing the data I exported it from.    QML files are handy if you have one, or more, layers but have a collection of different style that you want to apply to them.

Style files can only be only be applied to a layer once it is opened. The recent [Ordance Survey](http://www.ordnancesurvey.co.uk/blog/2014/03/opening-up-to-qgis-qml-launched-for-os-opendata/) release of styles is a prefect QML use case.

### The Layer Definition file (.qlr)

**It contains:** Layer source pointer + Style information

This newest feature, also in [plugin](http://plugins.qgis.org/plugins/layerdefinitions/) form for 2.0 and 2.2, is a Layer Definition file.  This file contains the reference - or pointer - to the data source plus any style information.  This is like a the ArcGIS .lyr file, although maybe not as fully feature rich just yet.   The use case for this file is simple: To have a single file to can open a data source bringing in all the related style information.  These files also allow you to mask the underlying datasource in a easy to open file. 

One of my use cases is to open MS SQL layers.  Rather then having to go to the MS SQL connection dialog, connect, select and load, then style.  I can simply add a .qlr file that points to the correct MS SQL layer pre styled.

In the future a .qlr file may hold a reference to more then one layer. The Ordance Survey or Natural Earth stuff could also be done with a QLR in order too allow just opening a single file.

### The Project file (.qgs)

**It contains:** Layer source pointer + Style information + Composers + a whole heap of other stuff

The Project file is the highest level file that QGIS has.  This holds more then just a list of layers, it also holds order, groups, composers, marcos, etc.  I don't really need to explain any of this because you already know.


## Why not just extend QML (style file) or QGS (project file)?

In software development we have this thing called SRP (Single Responsibility Principle), and while it can be tricky to follow at times I think it can also apply in cases like this. Sometimes have a single file meaning many different things can be worse then having a many different files with one use case each.  

Could I have extended QML to support datasource too? Sure. Easy. However I don't think it made any sense. The use case of the QML is to store only the style and to be applied after the layer is loaded.  Who says I have the datasource you used in the first place?  In this case the QML is the most portable format because it doesn't point to a data source.  I could have just stored the layer reference and ignored it in the normal places we import QML, yes but now you start to muddy the water on what a QML is.  If your answer to "What is a QML file?" is "Well sometimes it opens a layer, and sometimes it's just the style" that to me is a smell.

The project file stores a lot of different things and I could have used that as a base, but again I think it starts to muddy the waters. The project file also contains a lot of other things that we just don't need, composers, etc.  I have started working on a Import from Project function, just like the plugin of the same function, however I don't think this process is a smooth as using something like a QLR file to bring in layers.  Giving someone a full project just so then can import a single layer from it feels like giving someone a full toolbox when all they want is a screwdriver. Just give me the screwdriver, I don't care for the other stuff.

