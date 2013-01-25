---
comments: true
date: 2011-06-06 09:10:04
layout: post
slug: one-of-my-favorite-features-of-qgis
title: One of my favorite features of QGIS - Rule based styling.
wordpress_id: 630
categories:
- Open Source
- qgis
tags:
- gis
- map-rendering
- mapping
- Open Source
- OSS
- qgis
- Quantum GIS
- styling
- thematics
---

One of my favorite features of QGIS is the rule based rendering.

[caption id="attachment_631" align="aligncenter" width="630" caption="QGIS rule based rendering dialog"][![QGIS rule based rendering dialog](http://woostuff.files.wordpress.com/2011/06/rules.png)](http://woostuff.files.wordpress.com/2011/06/rules.png)[/caption]

If you're using MapInfo think of thematics + queries but on steroids. Rule based rendering allows you to you set, well, rules on what gets rendered and how.  The rules are based on a simple SQL style query language that's built into QGIS.

Take for example the above screen shot.   The screen shot is from a current project I am doing in QGIS to clean up our current stormwater/drainage layer.  The layer is a in a bit of a mess at the moment so I needed a way to visualize what I have cleaned up and what I haven't, so enter QGIS rule based styling.

For example: A pipe that has an upstream and downstream invert and is part of the trunk (main) network is then considered valid (for this situation anyway), so I created the following rule:

[sourcecode language="SQL"]
network_type = 'Trunk' AND Description != 'Drainage Imaginary Pipe' AND (US_Invert > 0 AND DS_Invert > 0)
[/sourcecode]

We also have little connecting pipes that I don't want to include in valid trunk  as they are only used to connect pits to pipes and are just cosmetic, I have excluded them by adding "**Description !='Drainage Imaginary Pipe'**" to the above filter.

Next I wanted to show invalid trunk network pipes (ones without an up or downstream invert), so we just invert the last condition and swap the last AND for a OR:

[sourcecode language="SQL"]
network_type = 'Trunk' AND Description != 'Drainage Imaginary Pipe' AND (NOT US_Invert > 0 OR NOT DS_Invert > 0)
[/sourcecode]

I also need to show but no highlight the non trunk pipes and the connecting pipes, so I made the next two rules and set their styles to a light gray:

[sourcecode language="SQL"]
NOT network_type = 'Trunk' AND NOT Description = 'Drainage Imaginary Pipe'
[/sourcecode]
[sourcecode language="SQL"]
Description = 'Drainage Imaginary Pipe'
[/sourcecode]

Finally I want to show pipe direction on all pipes but not the connecting pipes, again as they are just cosmetic:

[sourcecode language="SQL"]
Description != 'Drainage Imaginary Pipe'
[/sourcecode]

You will also note in the screenshot above that I have a max zoom scales set on the last three rules, this is because when I zoom out all that info becomes overwhelming at that scale and distracts from showing the invalid parts of the main trunk line.

So after all that, the results:

[caption id="attachment_650" align="aligncenter" width="630" caption="Map rendered using rules"][![Screenshot of rules applied](http://woostuff.files.wordpress.com/2011/06/rulesfinal.png)](http://woostuff.files.wordpress.com/2011/06/rulesfinal.png)[/caption]

and if I zoom out pass 5,000:

[caption id="attachment_651" align="aligncenter" width="630" caption="Map rendered when zoomed out pass 5,000"][![Screenshot of rules applied, zoomed past 5,000](http://woostuff.files.wordpress.com/2011/06/rulesfinal2.png)](http://woostuff.files.wordpress.com/2011/06/rulesfinal2.png)[/caption]

I think you can see how this rule based rendering could be very powerful, in fact I have about four different rule sets I use with the drainage layer to show different things to different people.

The rules I have shown above are pretty simple, you can go pretty crazy and use them to render OpenStreetMap data: [http://www.youtube.com/watch?v=NBBYtH2svw0](http://www.youtube.com/watch?v=NBBYtH2svw0)

The worst part about the rule based rendering is that I have gotten so used to their power that I feel crippled when I go back to MapInfo and try to do styling :)

Happy mapping.

**_What is your favorite QGIS feature?_**
