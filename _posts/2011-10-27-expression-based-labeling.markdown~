---
comments: true
date: 2011-10-27 08:59:31
layout: post
slug: expression-based-labeling
title: Expression based labeling now in QGIS.
wordpress_id: 869
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- Open Source
- osgeo
- qgis
- Quantum GIS
---

QGIS finally has expression based labels! _(Although you must be running latest dev build)_

What does that mean? Well QGIS used to be only able to label with a field from the layer, very limiting if you need to make a nice looking label string. Now you can use expressions (eg 'Up ' || US_Invert || 'some more text' ) to label the feature, just like this.

[caption id="attachment_870" align="aligncenter" width="525" caption="Example of expression based labels"][![](http://woostuff.files.wordpress.com/2011/10/expression-labels.png)](http://woostuff.files.wordpress.com/2011/10/expression-labels.png)[/caption]

This is something that I missed a lot when moving from MapInfo to QGIS.  After opening a ticket on the QGIS bug list and nothing happening with it for a couple of months (not that I expected anything to, everyone is busy enough as is.  I don't expect the devs to just jump at all my requests) so I decided I should at least attempt adding it myself.  The joys of open source!

Turns out adding the expression labeling was the easy part, however there was no good generic expression string builder that I could use to build the expression string.  QGIS already had the expression builder for the query window and the field calculator, however the code was very tied down to only work for those implementations, plus they didn't scale with the increasing function list.  I'm not going to go and make yet another dialog just for the labeling.  Uniformity is the key to good user experience.

After searching around to see what other GIS systems did to get some inspiration it seemed that every example that I came across was, in my opinion, poor.    Although there was one ArcGIS idea ticket that gave me a few ideas [http://ideas.arcgis.com/ideaView?id=087300000008IbHAAU](http://ideas.arcgis.com/ideaView?id=087300000008IbHAAU)

So with that I started working on a generic expression builder that could be used to build an expression string anywhere, replacing the query window and field calculator in due time. One ring widget to rule them all, one ring widget to bind the, etc.


## The result


[caption id="attachment_871" align="aligncenter" width="630" caption="Generic expression builder"][![](http://woostuff.files.wordpress.com/2011/10/expression-based-dialog.png)](http://woostuff.files.wordpress.com/2011/10/expression-based-dialog.png)[/caption]

Key features of the new expression builder:



	
  * Live validation of expression

	
  * Real time searching

	
  * Live output preview

	
  * Help on selected item.

	
  * Easier to add new functions without changing the UI.  Function list is read right from the expression parser.  No more hidden functions.

	
  * Reusable widget


If the expression hits an error while you type you will be shown an "Expression is invalid" warning _(yes I know it's wrong in the screen shot). C_licking (more info) or hovering over the expression area will show you the error.

[caption id="attachment_872" align="aligncenter" width="512" caption="Expression has error"][![](http://woostuff.files.wordpress.com/2011/10/expression-based-dialog-error.png)](http://woostuff.files.wordpress.com/2011/10/expression-based-dialog-error.png)[/caption]

Searching can done by using the search box at the top. The function list will reduce to show only functions or fields containing that string _(Note: it is case sensitive at the current time) ._

[caption id="attachment_873" align="aligncenter" width="321" caption="Searching for a function or field name."][![](http://woostuff.files.wordpress.com/2011/10/expression-based-dialog-serach.png)](http://woostuff.files.wordpress.com/2011/10/expression-based-dialog-serach.png)[/caption]


## Still to do


As with all programming it is never bug free so I expect, now that it is open to wider testing, that there might be a few that need to be addressed .   There is also very limited function help written for the functions, although if anyone is willing to have a go at it I'm more than happy.

If you do find any bugs will the widget/dialog you can open a ticket at [http://hub.qgis.org/projects/quantum-gis/issues](http://hub.qgis.org/projects/quantum-gis/issues) , assign it to me and I'll see what I can do.


## In the works





	
  * Simple Syntax highlighting

	
  * Recent expression used list

	
  * Saved expressions

	
  * Auto bracketing _(maybe)_

	
  * __UI tweaking


I would like to thank Martin from the QGIS team for reviewing my code all though the project and helping me improve the code and idea.  Also thanks to all the other people who gave ideas for the widget/dialog.

**Enjoy!**
