---
layout: post
title: "The QGIS Field calculator is dead. Long live the Field calculator bar"
description: ""
category: 
tags: [qgis]
---

Ahhh the good old field calculator, it's in a better place now. OK not really, it's still there if you need it, but we can do a little better in 2.4. Introducing the field calculator bar:

{% image fieldcalc1.png %}
{% endimage %}

oooo fancy.

The field calculator has always bugged me, I think it was just the combination of a few things:

- It's modal so it blocks you from doing anything else - this alone is motivation enough in my mind.
- You have to do the Open - Run - Close - Open - Run - Close dance which isn't great - annoying to say the least.
- Did I mention it's modal - AAAAAAAHHHHHHHHHHH
- Defaults to creating a new field - which is the edge case
- You only have All or Selection, which is a bit limiting

Anyway, enough with that. Last night I was having a chat to [Nyall](nyalldawson.net) about something unrelated, and while looking at Excel I thought about that little bar at the top and how handy that is.  You don't see a field calculator dialog in Excel - well there is one but not for the common case - you just wack in your expression and it does its thing. Why couldn't we have this for QGIS? I think I said to Nyall "you know this would be pretty cool, I might give it a go". Couple of hours later and this is it.

{% image fieldcalc.png %}
{% endimage %}

I have expressed in the past, and above, my hate for modal dialogs, so that was the main motivation and the results are much nicer then before.

What do we gain:

- Not modal - WIN!
- Don't have to close anything to see your results
- See the results as soon as you run Update (All|Filtered)
- Works on the features in table (All|Filtered)
- Does one job

The other improvment to the old dialog is what features the bar works on.  The bar will update what it sees in the dialog. If you need to update just the selection, simply select Show Selected and run the update. Need to search for something to update? Run a filter and press update.  The method has changed from All and Selected to All and Filtered.  Just remember if you see it in the attribute table it will be updated.

{% image fieldcalc-filter.png %}
{% endimage %}

The last point is important too, if you need a new field you use the New Field button, then run the update, there is no need to mix the two function into one tool. SRP.

This feature will be in 2.4. If you find any bugs assign them to me at hub.qgis.org and I will try to address them before 2.4 is out.

RIP Field calculator dialog
