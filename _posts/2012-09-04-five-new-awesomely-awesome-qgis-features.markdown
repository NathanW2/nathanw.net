---
comments: true
date: 2012-09-04 11:08:32
layout: post
slug: five-new-awesomely-awesome-qgis-features
title: Five new awesomely awesome QGIS features
wordpress_id: 1128
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- Open Source
- qgis
- Quantum GIS
---

Recently there have been some great new additions to the QGIS project. Being part of such a fast moving project is a great feeling, and it's only going to get better.

This post is going to be a quick over view of some of the newer features that I really like.


## HTML Annotations


Well of course I like this one, I [just](https://github.com/qgis/Quantum-GIS/compare/cbdafbc398...5a0d2f5863) added it. The reason I added this feature was because I really wanted to way to have popup images on the map canvas for flood damage reports on roads. I also wanted it dynamic so I could use template like syntax to replace values at run time.

The HTML annotations use QtWebKit and as a result support full HTML, CSS, and Javascript. The HTML can contain a QgsExpression - the same expression used in the expression labels and layer actions - inside [% %] which is replaced at run time with the data from the underlying feature e.g. [% "roadname" %]

[![](http://woostuff.files.wordpress.com/2012/09/roads.png)](http://woostuff.files.wordpress.com/2012/09/roads.png)

I'll let you think of some nice use cases for this new addition.


## Project macros and non blocking notifications


This new feature comes from Giuseppe Sucameli of [faunalia](http://www.faunalia.it/) with the work done for ARPA Piemonte.

The task was to add Python macros that run when a project is open, saved, closed. As a side effect of the task the issue of security was raise and how to notify the user that macros are going to run.  For me this was less about security and more about how to present that information to the user without annoying the crap out of them. Most of the time popup dialogs in software are a anti-pattern and are often abused for tasks like this. So knowing I would throw my computer out the window if I had to dismiss yet another dialog I suggested a less intrusive method being used a lot these days. The handy slide out notification bar. Giuseppe  was very welcoming to the idea and implemented it nicely.

[![](http://woostuff.files.wordpress.com/2012/09/marcos.png)](http://woostuff.files.wordpress.com/2012/09/marcos.png) Of course this addition can also expanded into other areas of the program. My first plan is to use it for notifying the user of plugins to failed to load.  There is nothing in QGIS that annoys more then starting and seeing this:

[![](http://woostuff.files.wordpress.com/2012/09/error.png)](http://woostuff.files.wordpress.com/2012/09/error.png) Dear dialog, why are you in my face!

To make matters worse if more then one plugin fails to load then I have to dismiss each dialog. So we can now use the notification bar to present it to the user in a nice non-blocking way. Something like "BTW four plugins failed to load at startup. What would you like me to do?"

Remember each time you use a blocking popup dialog it's pretty much yelling at the user "OMG GIVE ME ATTENTION!! NO YOU CAN'T KEEP WORKING! GIVE ME ATTENTION!"

I'm working on a patch  to move this stuff into the notification bar just no ETA at the moment as I'm a bit busy.


## Labeling improvements


[Larry Shaffer](https://github.com/dakcarto) has been working on some great improvements to the new labeling engine in order to make our maps look a lot more professional. Larry has been doing a lot of work in this area and is still going so I'm not going to go into all the details. However one new labeling feature that I really like is the ability to to set the  spacing between letters and words.

[![](http://woostuff.files.wordpress.com/2012/09/before_spacing.png)](http://woostuff.files.wordpress.com/2012/09/before_spacing.png) Before spacing

[![](http://woostuff.files.wordpress.com/2012/09/spacing.png)](http://woostuff.files.wordpress.com/2012/09/spacing.png) With a little bit of spacing

There is also the new ability to set the transparency of the label and the buffer.  The buffer transparency is something that I really like as sometimes you need a buffer but a solid buffer can then block out your map features; by adding a 45% transparent buffer I still have the labels pop off the map but not in your face or blocking features.  It's hard to make a picture to explain it well so you'll just have to experiment.


## Project Templates


This one could be quite handy for people that make a lot of maps with the same base data. Thanks to [Etienne Tourigny](https://github.com/etiennesky) QGIS can now load projects as a template. This means you can create a project with all your base layers, styles, labels, etc, configured and then load it by default, or from the file menu, and you will have everything setup. All you have to do is save the a normal .qgs project file in

`~/.qgis/project_templates` folder and the project will be shown in the file menu.

[![](http://woostuff.files.wordpress.com/2012/09/tempalte.png)](http://woostuff.files.wordpress.com/2012/09/tempalte.png) Template list

You can also set the current project as the default template:

[![](http://woostuff.files.wordpress.com/2012/09/options.png)](http://woostuff.files.wordpress.com/2012/09/options.png)

Handy!


## Symbol Manager


And last but not least. This years GSoC student [Arunmozhi](https://github.com/tecoholic) got the improvements he had (has) been working on included into the master build. Arun was very welcoming to any feedback that Martin and I gave him about how we would like symbol stuff to work.  Anita Graser has already covered a lot of the new features over on her [blog](http://underdark.wordpress.com/2012/08/15/introducing-the-latest-style-user-interface-improvements/) so I'm not going to go over everything again, although one thing she didn't really touch on was the smart groups and tagging.

The tagging and smart groups are one of my favorite additions to the new symbol manager.

[![](http://woostuff.files.wordpress.com/2012/09/tagging.png)](http://woostuff.files.wordpress.com/2012/09/tagging.png) Symbol tagging

I love this new feature as not all the symbols I create belong to a single group so the tagging and smart groups fit this bill well.  I can now tag all the council symbols with 'SDRC' and include them a SDRC smart group but at the same time tag the sewer ones with 'sewer' and they can live in the sewer style smart group; or how about all sewer symbols that are also SDRC ones:

[![](http://woostuff.files.wordpress.com/2012/09/smart.png)](http://woostuff.files.wordpress.com/2012/09/smart.png) Smart group with sewer and sdrc symbols

You can then filter by this group in the symbol selector:

[![](http://woostuff.files.wordpress.com/2012/09/search.png)](http://woostuff.files.wordpress.com/2012/09/search.png) Filter based on smart group


## Conclusion


I really love how fast QGIS is moving forward.  There almost isn't a week that goes by that something isn't getting done or someone is adding something new. Of course the great people on the project make this process a hell of a lot of fun and enjoyable.

Have fun experimenting! _(remember that these features are in the master development build and may or may not have bugs)_
