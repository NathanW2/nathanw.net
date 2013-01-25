---
comments: true
date: 2012-09-10 07:50:52
layout: post
slug: announcing-qmap
title: 'Announcing QMap: A simple data collection application using QGIS   '
wordpress_id: 1152
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- qgis
- Quantum GIS
---

I would like to announce QMap: A simple data collection application built using QGIS and Python.


![](http://nathanw2.github.com/qmap/images/Screen2.png)


QMap is a QGIS based field data collection application that was built by myself and a work college at Southern Downs Regional Council.  QMap is now opened source under the same licence as QGIS, GPLv2.  The project homepage can be found at [http://nathanw2.github.com/qmap/](http://nathanw2.github.com/qmap/) and source at [https://github.com/NathanW2/qmap](https://github.com/NathanW2/qmap).

Before I go into to many more details I will preface with: The application is currently under active development and as such there might be bugs or little rough bits that I haven't cleaned up yet. However having said that, the program is functional and we are using it at work for the purpose it was built.


## Features





	
  * Simple to use

	
  * Simple to manage

	
  * Simple to install

	
  * Forms built using Qt Designer

	
  * Loads normal QGIS projects

	
  * Anything QGIS supports QMap does too (snapping, PostGIS, etc)

	
  * It's just QGIS with a tablet friendlier interface.

	
  * Syncing support _(MS SQL 2008 only at the moment)_




## The Story


The program was developed after we looked around and decided that nothing really fit our needs quite right and to our satisfaction. _(Within budget of course)_

We had a list of, I think simple, requirements:



	
  * Must be simple to use by field staff

	
  * Can deal with complex or simple forms

	
  * Fully offline but with a syncing option

	
  * GPS support

	
  * Easy maintenance


The first point for me is a big one.  I have a seen a lot of data collection applications and unfortunately this is where I feel a lot of them fall down.  Most seem to be designed with people like me in mind, people who understand computers, understand menu systems, etc. If you work in local government or with an older age group of outside workforce you will know that this assumption doesn't hold true.   Most of our field staff are not computer people, a few don't even have home computer, expecting them to navigate a menu just to enable the GPS, or click on a small 16x16 pixel icon, on a tablet PC is not a option.

I decided to take the same approach as QGIS and use Qt Designer to build the forms. Why invent another tool? Using Qt Designer can also give us the flexibly of creating simple or complex forms in our own layout.

We do have pretty good 3G connection coverage over our region however we only have limited bandwidth to play with and having a solution that is full connected doesn't really give the best user experience.  I would rather just store everything locally on the device and then sync when needed.  As all our layers are stored in MS SQL Server 2008 for the syncing we decided to use .NET Sync framework.  I would love to have sync support for PostGIS, Spatialite, or any other normal files, but it was out of scope for the project _(at the moment)_.

For me easy maintenance means two things: not having to deal with crap loads of configurations; and having the power to change what I don't like. For the first point I'm a big fan of convention over configuration.  I like to just drop stuff in a folder with a certain naming convention and it should just pick it up and work.  This also goes for the form bindings, just name the control the same as the field in the layer and QMap will bind it for you.  If I can follow a convention for things I have. Conventions make setup easier and consistent.

Once you have tasted the open source kool aid it can be quite hard to go back. Knowing that if there is a bug in QGIS I can fix it to make my project better is a comforting feeling.  There is also the lack of licence fees which makes open source very attractive for jobs with small budgets.


## How does it work?


At the moment the core of the application is built as a QGIS plugin, however there is one little trick here that is worth mentioning. QMap is really a script that loads QGIS and sets the --configpath in order to load all the QGIS settings from a supplied path, inside the supplied path is the plugin. Think of it as a sandboxed QGIS which only loads the QMap plugin.  I'm also using the new customization function to remove all unneeded interface items.


## Notes


Here are some notes worth bring up:

The application is still under development so things might change.
There is only point support at the moment, although adding line and region support wouldn't be hard.
Syncing only works using MS SQL 2008 and the code is a bit rough. Will be cleaned up over time.
The build script only works on Windows and there is some win32 stuff for power management in the code. This is not because I don't want to support the other platforms just that it was out of scope at work.
You need to be using the latest development build of QGIS _(qgis-dev for those using OSGeo4W) _this is because there have been a few bug [fixes](https://github.com/qgis/Quantum-GIS/commit/4a9a9f7dbb97d12f2b29237ec97fb7f93a9f2535) that make the application work as expected that aren't in 1.8.
