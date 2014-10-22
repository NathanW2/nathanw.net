title: Alpha by Value choropleth in QGIS
description: ""
category: 
tags: []



This post was inspired by a post written by [Xaquín G.V](http://www.xocas.com/blog/en/ubersimple-tutorial-a-choropleth-in-qgis/), some extra credit must also go to Mathieu for helping me with the expression.

One of the new great features in the upcoming QGIS 2.0 is the ability to use data defined symbology and labelling.  It might look like nothing on the surface but it can really open up the possibility of some great looking maps.



Lets start with the example Xaquín has used by classifying by the unemployment rate. I have even created a pre-joined dataset for you if you want to follow along, grab it [here](https://www.dropbox.com/s/u4ps3chnpscbzz0/US%20Country%202000%202004.sqlite).

So first lets make a custom colour ramp just for this:

![Alt Text](/images/usaramp.png)

call it "usa" and classify the data

![Alt Text](/images/usaclass.png)

![Alt Text](/images/usaresult1.png)

Ok not bad. *But* you will always have those hard edges on the colours. What if we could get the exact colour ramp value for a given value? Well you can.

We need to make a new column for the colour value for each feature.  Open up the field calculator and add a new column with the following expression

```sql
ramp_color('usa', scale_linear( "unemployed_by_county_xgv_Rate",0,18,0,1 ))
```

What are the `ramp_colur` and `scale_linear` functions? `ramp_colur` is a new function that allows you to get a RGBA value for a position inside the ramp. So if you want the RGBA value at the 75% mark you can use `ramp_color('usa', 0.75`).  

Cool but to make it dynamic we need to bring in the value from the "Rate" column, however that goes up higher then 1. How do we get in a range from 0..1? Well we can scale it back down using `scale_linear`. 

```sql
scale_linear(<column>,<min in value>,<max in value>,<min out value>,<max out value>) 
```

Having said all that here is our result:

![Alt Text](/images/usaattribute.png)

To use this new colour column we need to use data defined symbols

![Alt Text](/images/usasymbol.png)

*Note*: I have selected Single Symbol

And the result

![Alt Text](/images/usaresult2.png)

This isn't going to suit every map but when something is scale based this method works well.

## Bumping it up a notch

Higher unemployment rates plus high lobor force really should get more weight. One way to handle this is by using Alpha-By-Value like Xaquín said in his post. Well to do that in QGIS we need to change the alpha value of what is returned from `color_ramp`. Time for a bit of regex (don't worry in 2.1 I will add a colour_ramp_rgb function with no aplha part)

First lets get just the aplha value part by scaling the lobor force coloum.  Add a new column using the following expression

```sql
toint(scale_linear("unemployed_by_county_xgv_Labor_Force", 0, 100000, 0, 255))
```

![Alt Text](/images/usaattributealhpa.png)

Now make a new column that replaces the alpha part of the colour column

```sql
regexp_replace( "colour", ',[^,]*$' , format(',%1',"alpha" ))
```

![Alt Text](/images/usaattributealphacolour.png)

Then we can use data defined symbols on that new column

![Alt Text](/images/usaresult3.png)

Nifty!

Now you will have to play with the min and max values for the scaling functions and also the colours in the ramp but you get the idea.

### Bonus

You can also use the same colour column on the labels to match the polygon and even increase the label size based on the rate column

![Alt Text](/images/usalabels.png)

So that is your Thursday lesson on how to create a Alpha by value map in the upcoming QGIS 2.0.

### Extra stuff

If you want to avoid creating all those extra columns or even do it on the fly you can use this single expression

```sql
regexp_replace( ramp_color('usa', scale_linear( "unemployed_by_county_xgv_Rate",0,15,0,1)),',[^,]*$',','|| toint(scale_linear("unemployed_by_county_xgv_Labor_Force",0,100000,0,255)))
```

Using the single expression block can be handy if you want to get your upper and lower limits right.





 











