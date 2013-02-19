---
comments: true

layout: post
slug: browser-wars-qgis-vs-mapinfo-11
title: 'Browsers: QGIS vs MapInfo 11'
wordpress_id: 720
categories:
- MapInfo
- Open Source
- qgis
- QGIS for MapInfo Users
tags:
- .NET
- Feature Requests
- mapinfo
- MapInfo Professional
- mapinfo-11
- Open Source
- qgis
- qgis-vs-mapinfo
- Quantum GIS
---

_Warning: This post contains small rants! You have been warned._

PBBI have recently released MapInfo 11, the new version has brought one change that I think deserves some attention - even if for the wrong reasons.

MapInfo's browser window was in need of a very good make over; it didn't follow normal keyboard conventions, eg holding shift to select rather than ctrl; couldn't sort via the headers; keyboard navigation was poor; and it looked ugly. PBBI then announced that MapInfo 11 would have a new "improved" browser. I thought "Sweet! About time" and then we got a copy. _/sigh_


## So what's the problem?


First off it's slow to resize, this would be due to them using .NET WPF for the new browser (I have never seen a good fast .NET WPF datagrid).

Then we have sorting, which is meant to be the cool new feature. This is not the normal just click on the header to sort the column, no because that would be too easy, you have to right click in the browser, click sort and select the options which then opens a new browser window. um what?

[![](http://woostuff.files.wordpress.com/2011/07/mapinfosort.png)](http://woostuff.files.wordpress.com/2011/07/mapinfosort.png)

Yes this is a pretty handy feature but no it shouldn't be the only way to sort, you should have a click on the header kind of sort. This seems to be what people wanted.

Next. No visible scroll progress. When you move the little scroll box on the side the browser waits until you have finished to show you the data. I guess the old browser did this too so why change it!

And finally shift click to select a block of rows doesn't work, I mean come on this is not a hard thing to do.

Surly you can dock it? Nope!

In the end we have a browser that is pretty much the same as the old one but slower......oh and has alternating row colors.

Overall reaction: Disappointed


## Enter QGIS


Now if you are reading this blog you are well aware that I am a huge fan of QGIS, I don't really make that a secret. So I guess the overall point of this post is to compare the QGIS attribute table (browser) and the new MapInfo 11 one.

Lets run though the same list as MapInfo.

Slow to resize? Nope. Even with a large table open the resize speed doesn't change.

Header based sorting? Yep. Just click the header and it will sort that column. Multi column sorting is on the to-do list.

Live scrolling (results update as you scroll)? Yep + no lag.

Shift click to select blocks of rows? Sure why not. Or you can hold ctrl to select rows all over the grid.

Docking? Yep and floating so you can put it on a different monitor if you need.

**Bonus**

The QGIS attribute table has a built-in search/filter box, saves having to run a query and have a new window like in MapInfo if you just want to filter the browser.

[![](http://woostuff.files.wordpress.com/2011/07/qgisattribute.png)](http://woostuff.files.wordpress.com/2011/07/qgisattribute.png)

**Extra Bonus**
The QGIS browser can even have other UI objects inside the cells. Very bloody handy.

[![](http://woostuff.files.wordpress.com/2011/07/control.png)](http://woostuff.files.wordpress.com/2011/07/control.png)

You can even have a calendar date picker if you want.


## Lets review









Feature
MapInfo 11
QGIS





Good resize speed.


No


Yes






Header sorting.


Yes [See update]


Yes






Multi column sorting.


Yes [1]


No [2]






Live scrolling.


No


Yes






Shift click for blocks of rows


No


Yes






Docking.


No[3]


Yes




_[1] Why does it need to open a new browser window? At least make it an option.
[2] On the to-do list_
[3] Yes you can use http://www.pbinsight.com/support/product-downloads/item/windowhelper for this support. It's a good tool go and download it. I just think it should be built in.

Doesn't look too good for MapInfo at the moment. QGIS is even accessing the TAB data though ogr. Quick tip: if a free program can access and manage your data faster than you, you are failing.

My work place spends a good deal of money on our annual MapInfo "maintenance" licence, money I would happily send to the QGIS project if I had the choice. Or at least part of it,


### Data


Both programs opened a 27000 row .TAB file.

_Just for the record I'm not anti-MapInfo. It still has some features that I really like. I just wish they would pick up the game._


## Update for 11.03 patch


As promised in my comments this is an update to reflect the new header click sorting in MapInfo Professional 11.03.

The 11.03 patch has added header based sorting, and while the sorting works as expected which is good, there is something a little odd.

What is the typical sort pattern? Left click header, table sorts ascending click again and table sorts descending or vice versa.  Then you normally have any extra sorting stuff in the right-click menu e.g Sort Ascending, Sort Desending, Clear Sort etc.

Go into MapInfo 11.03 left click header, context menu appears 0_o...  I'm not aware of any program that  has ever done that.  A menu on left click is not normal, even crappy ol' Lotus Notes doesn't have a menu on left click and Lotus Notes is one really crappy program.

Nuff said.

P.S Don't talk about your new feature i.e the browser, following normal conventions for browser style windows then do something no one has ever done....and still no shift click block select.

P.P.S I know it may sound like a constant bashing but really something like this should never got passed review. I know UI is hard but come, on a context menu on left click...
