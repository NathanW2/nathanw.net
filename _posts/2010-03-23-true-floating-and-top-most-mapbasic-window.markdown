---
comments: true

layout: post
slug: true-floating-and-top-most-mapbasic-window
title: True floating and top most Mapbasic window.
wordpress_id: 270
categories:
- Mapinfo Programming
- MapInfo Tools
tags:
- .NET
- Mapbasic
- mapinfo
- mapinfo interop
- mapinfo ole
- mapping
---

<Rant>One thing that has always annoyed me with MapInfo is the Mapbasic window.</Rant>

That last statement is a bit bold so let me break it down, functionality wise it is great and I couldn't use MapInfo without it, however it is part of the MDI Client (the gray bit in MapInfo  that the map windows belong to) this means that when you have a map or browser window and the Mapbasic window open they both have the same z-order in the MDI Client, meaning you can end up with this problem.

[![](http://woostuff.files.wordpress.com/2010/03/example.jpg)](http://woostuff.files.wordpress.com/2010/03/example.jpg)


### Not Cool


This is not cool, and I wonder how this even passed the user interface testing phase but I digress.

One of the problems that this can bring is that you can't have a maximized map/browser window and just have a small Mapbasic window in the corner.  This may not seem like a big deal however due to the z-ordering issue it forces you to micro manage your windows in the MDI client, move the map a little bit now you have to move the Mapbasic window so that it doesn't sit behind you map and so on, all in all wasting time you could be making your map.


### Get on with it


So what is the point of this post, well a little while ago I was sitting writing some unrelated C# code and it hit me.  If I can call and show a .Net form from Mapbasic, parent it to MapInfo and embed the normal Mapbasic window in my new .Net form I could make a true top most floating Mapbasic window that lives above any other window in MapInfo and remove that z-ordering issue.

After doing some playing around in test projects I discovered what I wanted to do was possible and without to much effort, there was a few little things that caused problems but what software adventure doesn't have those.

I complied all the code into a set of tools called the "[Floating Windows Tool](http://code.google.com/p/nathansmapinfoprojects/wiki/FloatingWindowTools)s", this set of tools also does a few other things but they will be covered in other blog posts.

The main thing the set of tools does is float the Mapbasic window above all the other window, here is an example of the result of using the tool.

[![](http://woostuff.files.wordpress.com/2010/03/mapbasicwindowtool.jpg)](http://woostuff.files.wordpress.com/2010/03/mapbasicwindowtool.jpg)

The above image shows a maximized map window and the Mapbasic window sitting on top of the map, it will always be on top and never move behind the map or any other window in MapInfo for that matter.


### More Information & Downloads


More information, downloads and examples can be found on my google code project page for the project:



	
  * [http://code.google.com/p/nathansmapinfoprojects/wiki/FloatingWindowTools](http://code.google.com/p/nathansmapinfoprojects/wiki/FloatingWindowTools)




### Demo Video


[youtube=http://www.youtube.com/watch?v=9KsBr4Eg_OM]

Sorry about the low quality.


### Contact me


I have spent a fair fews hours developing and testing this tool, however as with all software there are always things that could be improved or  bug to be squished.  So if you find anything or have a improvment idea don't hesitate to contact me via here or on the google code page for this project.


### Sneak Peek


And because software is never finished here is a sneak peek at the new version I am working on, this version will have syntax highlighting and code completion so that it will make it easier to type Mapbasic.

[![](http://woostuff.files.wordpress.com/2010/03/mapbasicwindow.png)](http://woostuff.files.wordpress.com/2010/03/mapbasicwindow.png)

Since making the first release my time to work on this project has decrease a lot, so I can't see me making a release of the new version anytime soon however I may have a  "all I do is code" weekend and may get it done faster then I think so stay tuned if your interested.
