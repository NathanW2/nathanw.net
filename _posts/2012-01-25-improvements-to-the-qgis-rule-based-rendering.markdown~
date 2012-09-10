---
comments: true
date: 2012-01-25 14:54:23
layout: post
slug: improvements-to-the-qgis-rule-based-rendering
title: 'Improvements to the QGIS rule based rendering  '
wordpress_id: 906
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- map-rendering
- mapping
- Open Source
- osgeo
- qgis
- Quantum GIS
- styling
---

The rule based rendering in QGIS has just got a make over to improve in some of the old usability issues it used to have.  Most of the improvements are UI related. If you would like to try them out you will need to grab a copy of the latest dev build (qgis-dev in OSGeo4W)

Main improvements include:



	
  * Nested rules.  If the parent rule evaluates to false none of the child rules are applied. This replaces the priority system in the old dialog.

	
  * Disable symbol for rules. Rules with no symbol only act as a check for the child rules e.g nothing is rendered for the rule but child rules still are (unless also disabled).

	
  * Drag and Drop rules _(multi-selection is supported)_.  Rules can be dragged onto other rules in order to nest them and set up a rendering hierarchy.

	
  * Inline editing of rule labels, expressions, scales

	
  * Overall tweaks to the dialog


[caption id="attachment_908" align="aligncenter" width="630" caption="The new rule dialog"][![](http://woostuff.files.wordpress.com/2012/01/rules-dialog.png)](http://woostuff.files.wordpress.com/2012/01/rules-dialog.png)[/caption]

As you can see in the screenshot, the rules are now organized in a tree which clearly expresses which rules should be applied and when.

In the example above, all the rules under the **Sealed **rule will only be applied if that rule is true. The old system would have you managing all rules in one big list and dealing with priorities in order to get the rules to apply right, the new dialog is a major improvement.

And the results! As you can see below, QGIS will only render the colored squares if the **Sealed **rule is true otherwise it just shows a green line.

[caption id="attachment_907" align="aligncenter" width="630" caption="The rules applied"][![](http://woostuff.files.wordpress.com/2012/01/rules.png)](http://woostuff.files.wordpress.com/2012/01/rules.png)[/caption]

The work was sponsored by Ville de Morges, Switzerland and developed by Martin Dobias.  Thanks to both of them for these improvements.

More info:



	
  * See Martin's notes for a more detailed breakdown, and maybe some future stuff to come, of the improvements  [http://lists.osgeo.org/pipermail/qgis-developer/2012-January/017909.html](http://lists.osgeo.org/pipermail/qgis-developer/2012-January/017909.html)


**Note:** As this is a brand new feature there might be some bugs, or things that don't quite work as expected. If you do find something don't hesitate to file a bug report at hub.qgis.org so it can be fixed, or at least known about.
