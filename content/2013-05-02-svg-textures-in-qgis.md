title: SVG textures + blend modes = Cool QGIS Maps
tagline: "Who doesn't love cool maps?"
description: ""
category: 
tags: []


Did you know you can use textures to fill a polyon in QGIS? No? Well you do now!

The cool thing is you can get results like this with a simple SVG and a texture.

![Alt Text](/images/texture.png)

So how do you do it? Lets give it a go.


First grab a texture you want from [http://texturelib.com/](http://texturelib.com/)

Install Inkscape, or any other tool that can create svgs with textures.

Drag and drop your texture into Inkscape and embed the texture into the SVG:

![Alt Text](/images/textureembed.png)

Twaek any settings you need in Inkscape and save it somewhere QGIS can find.

*Tip: You can configure extra search paths for svg in Options -> System -> SVG Paths*

![Alt Text](/images/inkscape.png)

Open QGIS and load a polygon layer

Change the symbol type for the style to SVG fill and selet your SVG

![Alt Text](/images/texturepicker.png)

Hit apply. 

Opps that's not right

![Alt Text](/images/textureresult1.png)

Enter the handy blend modes added by [Nyall](nyalldawson.net).

Change the blend mode to Soft Light and move the layer to the top of the drawing list

![Alt Text](/images/textureresult2.png)

SWEEEET!!!!

Now go and make some pirate maps.
