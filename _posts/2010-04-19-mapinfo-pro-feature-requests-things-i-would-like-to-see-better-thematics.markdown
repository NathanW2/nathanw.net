---
comments: true

layout: post
slug: mapinfo-pro-feature-requests-things-i-would-like-to-see-better-thematics
title: MapInfo Pro Feature Requests - Things I would like to see - Better thematics
wordpress_id: 296
categories:
- Mapinfo Professional Feature Requests
tags:
- Feature Requests
- Mapbasic
- mapinfo
- MapInfo Professional
- mapping
- thematics
---

I have been working on a rather large mapping project over the last couple of months, and that thought I would write a blog post about some features that I would like to see implemented in MapInfo Pro to make map making a little bit easier.  This could get long so I might break in down into different posts.

Let us begin.


## Linked thematic map templates:


Thematic maps are great, I use them all the time but unfortunately they are a big pain in the butt when it comes to using and applying them across a large range of maps and workspaces and using them to keep map updated.

I will elaborate a bit on that last point with a scenario.  Lets say you have a table with a series of maintenance points each with one of the following values:



	
  * Complete

	
  * Started

	
  * Failed


Now we can create a thematic map to show these values:

![](http://woostuff.files.wordpress.com/2010/04/thematicexample.png)

Sweet, now we can use the Save As... template option so we can save it as something like **"Maintenance - Status - Standard"**, we do this so that we can apply it to other maps later on.

Now I want to save a workspace because I have all sorts of maps open that need to keep their formating, so I do a Save Workspace.... as something like "**Jobs.wor"** , a couple of weeks later I would like to make a new set of maps, (say for a gridded map book for the field) using the same template so that I am using the same standard colors across all my maps.   I open the table, make my grid and apply the template to the maintenance layer, everything looks good, now I save the workspace... **"Jobs Map book.wor"**.  So by this time we have two workspaces: "**Jobs.wor";**"Jobs Map book.wor".****

After a couple of weeks I realize that I have to change one of the colors that we use to show the job status.  So we open up the Maintenance.tab and apply the **"Maintenance - Status - Standard"** template that we have already set up, then we change the color of the Completed job status to yellow, and do a template Save As... and save it as the same name as the old template, overwriting the old one.

Now I want to generate my map book again to bring it up to the new standard colors, I open up the** "Jobs Map book.wor" **workspace, and what! my colors in the thematic for the maintenance job status are still the same as they were before I updated my template.  Opening up the **"Jobs.wor" **workspace I find the same thing, there is a disconnection between the template and where it is used.

The reason this happens is because when you save the workspace it hard codes the thematic values right into the workspace with the map. something like this:


_shade 1 with Values values_




_"Complete" Symbol (34,16711680,12) ,_




_"Failed" Symbol (34,65280,12) ,_




_"Started" Symbol (34,255,12)_




_default Symbol (40,0,12)   # color 1 #_




_
_




meaning that each map in the workspace now has its' own independent thematic map regardless of the template changes.  If I would like my two workspaces to have the template  new colors I must open both of them and remove the thematic on each map that uses it and reapply it and save.  The problem with this is that it requires the user of the workspace to be aware of the changes in the template and reapply them.  In a multi user environment this becomes difficult.  I also becomes a problem when you have a large workspace 20+ maps all using the same thematic, that is 20+ changes every time you need to make a style change.




## What I think would work


My idea is just like something Peter Horsboll Moller and Gentreau in [this Mapinfo-l](http://groups.google.com/group/mapinfo-l/browse_thread/thread/ffca3f14def5c68a/065a8e679fa9621d?lnk=gst&q=shade#065a8e679fa9621d) thread suggested beck in 2008, a syntax and command addition to MapBasic.
Something like the following:


Shade <tablename> Layer <layername> Using Template <full path to template> Column <column name>


This means you would be able to store templates in one place and any time somebody opens the workspace, the theme file is read and applied to the map, meaning you will always have the latest style changes.  By using the full path or just the theme name you could store theme files on a network drive or just with the workspaces if it is only going to be used for a selected job with lots of workspaces.

You could also store something like this in the tab file meta data, to use a theme file as the default shading:


\defaulttheme\path = "<full path to template>"





## Why I think this word be good.


As it's pretty obvious from the scenario that I outlined, if you are working on a large mapping project with a table and thematic being used in all the workspaces.  The ability to update just the template and not have to worry about updating each  independent  thematic stored for map in each workspace would greatly improve map making speed.  This feature become even more needed when projects become old and not knowing which workspace and maps need to be changed.


## Notes.


Just saving the path to a theme template file would not always be needed(sometimes templates aren't even needed, for one-off jobs), so hard coding the thematic into the workspace still needs to be an option, but by default it should save a template and the path to the template first rather than hard coding.


## Please let me know what you think.


I am writing this as a public blog rather than just sending it straight to MapInfo because I would like to see what other people also think.  Maybe this idea can be expanded? Maybe you would like to say why it shouldn't be done? Doesn't matter the reason, let me know.  All comments are welcome, the more people behind an idea the better.


[polldaddy poll=3075850]
