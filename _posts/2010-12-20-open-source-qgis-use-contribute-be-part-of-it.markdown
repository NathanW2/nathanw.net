---
comments: true
date: 2010-12-20 15:44:26
layout: post
slug: open-source-qgis-use-contribute-be-part-of-it
title: Open Source QGIS - Use, Contribute, Be part of it.
wordpress_id: 403
categories:
- Open Source
- qgis
---

Since using and writing code for the open source GIS project [QGIS](http://www.qgis.org/) I have come to see that the thing that really keeps open source projects alive is the community and documentation.  Without the community the project fails, and without documentation it makes it very hard for new users to find their feet and in the end loosing potential users and contributors.   Now what does have to do with QGIS?  Well, while the documentation is pretty good already there are always areas that could be improved, and new features are always slower to get help written as getting stable code is higher priority.

First. Why help in open source projects?



	
  1. Become part of the project rather then just a user.

	
  2. Help move the project forward faster.

	
  3. It helps tune your programming and non-programming skills.

	
  4. Get the girls!?


OK maybe not the last one, but the rest are valid.

If your not a developer, or even if you are, then this is where you come in.  If you are using QGIS and upon clicking a help button are presented with a help menu that doesn't exist (just a blank white help page) or even is missing help on a certain feature, maybe consider updating the help file with some info on said feature in order to help people in the future.   It doesn't have to be anything fancy, every little bit helps.


## Editing the help files.


The help files are probably the easiest things to edit as you don't need to be able to compile the source, or know anything about programming, to contribute.  First you will need to install QGIS. I would recommend using the  [OSGeo4W installer](http://www.qgis.org/wiki/Download#OSGeo4W_Installer) as it will get you everything you need in one easy installer.  Once you have installed QGIS, navigate to the following folder [depending where you installed it]: "C:\OSGeo4W\apps\qgis\resources\context_help" you will see something like the following:

﻿

[![](http://woostuff.files.wordpress.com/2010/12/help.png)](http://woostuff.files.wordpress.com/2010/12/help.png)

Don't be fooled by the file extensions, or lack thereof, they are just html files.  The funny stuff at the end is just the code for the language ie en_US is US English as QGIS supports different languages these codes are needed so the help knows which one to show to the user.

So that's really it, you don't need to do anything apart from edit some HTML files.


## Submitting Changes


This is the hardest part of the process. Currently there are two ways I can think of to commit your changes to the main QGIS project. (1) Download the full source from QGIS SVN server, create a diff patch for the changed file and submit it as a ticket to the QGIS bug list. (2) Send the new document  to me and I will do the first step for you, and submit it the team.  Also given that the first step involves knowing and understanding subversion, and accessing the source control [not a hard task just a topic for a different post/video] step 2 is easier for the non-developer.


## Example


I thought it would be good to give a quick example of editing a help document.

After finding the dialog with the help file needing work, let's go with the style manager dialog which happens to have no help written yet:

[![](http://woostuff.files.wordpress.com/2010/12/stylinghelp.png)](http://woostuff.files.wordpress.com/2010/12/stylinghelp.png)

We then need to navigate to the context help folder in C:\OSGeo4W\apps\qgis\resources\context_help and find the file that is linked to that dialogs help button [they tend to have the same name as the dialog]. So in this case it's called:  QgsStyleV2ManagerDialog-en_US.  As I don't know any other languages I will be working on the English one.

Opening the file in your favorite html editor [Notepad++] up gives us the following:

    
    <h3>Style Manager</h3>


Well that explains why there isn't any help.  The file is empty apart from the header.  So lets add something.

    
    <h3>Style Manager</h3>
    <br>The style manager allows for easy creation and management of QGIS styles that can be used when styling layers.</br>


Now save the file and reopen the help dialog in QGIS, no need to restart QGIS.  And there we go:

[![](http://woostuff.files.wordpress.com/2010/12/help1.png)](http://woostuff.files.wordpress.com/2010/12/help1.png)

﻿It's a simple as that.  I would advise reading though some of the already written help files to get a feel for style, and type of language used but apart from that feel free to send me any changes and I will submit them as a ticket once I have few collected.

Happy Mapping

P.S If are a non developer, or developer, and are interested in using Subversion to create patches for QGIS documentation I am more then happy to lend a hand if needed.


## Handy Links





	
  * [http://www.qgis.org/wiki/People](http://www.qgis.org/wiki/People) QGIS Community Team. These people are in charge of the community side of things for QGIS.  I would contact them if you need anymore info or help with documentation.

	
  * [http://linfiniti.com/2010/12/new-qgis-1-6-brochure-available/](http://linfiniti.com/2010/12/new-qgis-1-6-brochure-available/) Tims post talking about the [QGIS Brochure](http://www.qgis.org/en/documentation/brochures.html) and GIS Community Team.


