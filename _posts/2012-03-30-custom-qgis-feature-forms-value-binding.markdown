---
comments: true
date: 2012-03-30 10:08:31
layout: post
slug: custom-qgis-feature-forms-value-binding
title: Custom QGIS feature forms - Value Binding
wordpress_id: 957
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- Open Source
- osgeo
- qgis-editing
- Quantum GIS
---

One thing I didn't explain very well  in my [other](http://woostuff.wordpress.com/2011/09/05/qgis-tips-custom-feature-forms-with-python-logic/) post was how to correctly set up value binding between your custom form and QGIS.  I didn't explain it because at the time I didn't know how.

The other day I was building a custom form QGIS for a project I am working on. I had named all the fields right, set the ui as the edit form for the layer, but only the line edits were getting bound to the correct values.


[![](http://woostuff.files.wordpress.com/2012/03/y-u-no.jpg)](http://woostuff.files.wordpress.com/2012/03/y-u-no.jpg)


 So having a dig around in the code I noticed that QGIS uses the same methods to bind the built-in edit forms as it does for the custom forms, meaning that you must set what kind of control you want to use in **Layer Properties -> Fields **


## Correctly binding values


First create the form with the controls you need, remember to name them the same as your fields.

[![](http://woostuff.files.wordpress.com/2012/03/customform.png)](http://woostuff.files.wordpress.com/2012/03/customform.png)

Note that here I have a QComboBox with the FeatureCla name, this will bind the combo box to the FeatureCla field in my dataset in QGIS.

Now set the custom form as the **Edit UI **for the layer

[![](http://woostuff.files.wordpress.com/2012/03/properties.png)](http://woostuff.files.wordpress.com/2012/03/properties.png)


> _Tip: You can use relative paths if you store the form along side your project file_


_ _Flick to the Fields tab and set up the **Edit Widget **type for each field that you have used on the custom feature form.

[![](http://woostuff.files.wordpress.com/2012/03/fields.png)](http://woostuff.files.wordpress.com/2012/03/fields.png)

I have set the **FeatueCla** field to use Unique values widget, this tells QGIS to collect all the unique values from that column and add them to the QComboBox.  There are a range of different edit widgets you can set

[![](http://woostuff.files.wordpress.com/2012/03/options.png)](http://woostuff.files.wordpress.com/2012/03/options.png)Each will map to a different set of control types (Widgets) e.g. If you want to have a checkbox on your form you must select Checkbox in the Edit Widget list to get it to bind correctly.

Save the properties and head back to you map.  Use the Identify Tool to select a feature.

[![](http://woostuff.files.wordpress.com/2012/03/form.png)](http://woostuff.files.wordpress.com/2012/03/form.png)

[![](http://woostuff.files.wordpress.com/2012/03/values.png)](http://woostuff.files.wordpress.com/2012/03/values.png)

And that is it. Pretty cool hey!


## Final thoughts


This is one feature I really like in QGIS.  The ability to create custom forms for people to do data entry without the need to build a plugin is very cool.  Couple this the built-in GPS module for QGIS and you have yourself a nice simple field data collection program.

I have some ideas to make this feature even more powerful, but more on that later once I get some time to add it in.
