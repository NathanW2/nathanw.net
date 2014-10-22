title: Waiting for QGIS 2.2: Highlighting current Atlas feature
description: ""
category: 
tags: []

A new feature coming up in QGIS 2.2 will be the ability to style the current active atlas feature with a different symbol.  This also extends to styling other layers based on the current feature geometry. 
This post is a quick preview of the upcoming 2.2 feature. 

When a layer has been enabled for Atlas in the composer two new variables will be created ``$atlasfeatureid`` and ``$atlasgeometry``.  This are static expression variables so once set they are available anywhere in QGIS.  These two new static variables will now be set for each feature when printing using the Atlas feature.   This also means we can access them in the rule and label expressions to do some pretty cool styled maps.

Once defined we can then create a rule using the rule based renderer to highlight the active layer.  We do this by using the expression ``$id = $atlasfeatureid``.  Simply put "Does this feature ID match the current atlas one"

![Alt Text](/images/atlasrule.png)

![Alt Text](/images/atlasruleresult.png)

That's pretty cool. The current feature (ID 0) in this case is green and the rest is gray.  You will also note another new feature in 2.2 which is the ``ELSE`` rule.  This rule will run when none of the other rules on it's level have passed or evaluated to true.  We can use this ``ELSE`` rule to just style everything else as gray.

Why don't we one up this a little and just label the current active one.

![Alt Text](/images/atlaslabelexpression.png)

![Alt Text](/images/atlaslabelexpressionresult.png)

You could also use a CASE expression do the same thing ``CASE WHEN $id = $atlasfeatureid THEN "name" END``.  Take your pick on which one you like the most. 

What if we wanted to just show other layers features that are within the area, maybe we want to style them different if they are within an area, or outside of that area.  Lets take a look at styling a tree layer that is only within the current atlas geometry.

We have geometry functions in the expression engine so lets use those here on our street trees layer:

![Alt Text](/images/atlastrees.png)

![Alt Text](/images/atlastreesresult.png)

I have nested the rule so that we can style the trees differently based on status but only if they are within the active atlas feature.

Remember this is dynamic so there is going to be a performance hit if you try and run this type of expression on many features. The expressions will run once per feature per map redraw so just be aware of how expensive this can become.

When we render the output to files we get what was expected.

![Alt Text](/images/atlasoutput.png)
