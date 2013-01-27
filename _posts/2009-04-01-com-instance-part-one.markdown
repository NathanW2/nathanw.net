---
comments: true
date: 2009-04-01 16:56:55
layout: post
slug: com-instance-part-one
title: Creating an instance of a Mapinfo COM object in .NET - Part One
wordpress_id: 61
categories:
- Mapinfo Programming
tags:
- .NET
- Mapbasic
- mapinfo
- mapinfo interop
- mapinfo ole
- mapping
---

This the first blog post in the series [Creating a instance of a Mapinfo COM object in .NET.](/2009/04/01/com-instance-mapinfo-main/)

In this post I am going to talk about **creating an instance of using Interop.Mapinfo.dll. **So lets get into it.


## Step 1: Adding a referance to Mapinfo.


First we need to add a reference to Mapinfo's COM object, this can be done in a few different ways, for now I will just focus on the main method.

You will need to open the add reference dialog in Visual Studio and select the COM tab, this should give you a list of all the COM objects that have been registered on your machine.  You will need to select the one marked "Mapinfo x.x OLE Automation" where x.x is the version of the currently installed Mapinfo.  For example:

![COM Dialog](http://woostuff.files.wordpress.com/2009/03/ref.jpg)

Once you have found and selected the Mapinfo COM object, you can then click OK.  When you return to Visual Studio you will notice that a referance to Mapinfo has been added to your project. 

![referance added](http://woostuff.files.wordpress.com/2009/03/mapref.jpg)


By checking the object browser, you will notice that by adding a reference to Mapinfo's COM object, we now have strong typed access to its members.

![objects1](http://woostuff.files.wordpress.com/2009/03/objects1.jpg)


(Note: Picture may differ slightly to other versions of Mapinfo).


We now have strongly typed access to Mapinfo's COM methods. When we add a reference to a COM object using Visual Studio it will create a dll in the form of a [RCW(Runtime Callable Wrapper).](http://msdn.microsoft.com/en-us/library/8bwh56xe.aspx) This then wraps all the exposed COM members into .NET objects which are responsible for marshaling all the calls between your .NET application and the COM object, including any type conversion that needs to be preformed. 


Now that we have got all of that out of the way lets move on to step 2.

## Step 2: Creating the instance


When you are using the Interop.Mapinfo.dll, creating an instance of the currently installed Mapinfo is very easy.
In the picture above you can see a class called _MapInfoApplicationClass, _this is the object we will be using to create an instance of Mapinfo.  Having said that, all we need to do is create a new _MapinfoApplicationClass _like this:

{% highlight csharp %}
MapInfo.MapInfoApplicationClass mapinfo = new MapInfo.MapInfoApplicationClass();
{% endhighlight %}

When this line is executed in your program  a new instance of  Mapinfo will be created and you will then be able to send commands to it by using the _Do_ and _Eval _command. Like so:

{% highlight csharp %}
MapInfo.MapInfoApplicationClass mapinfo = new MapInfo.MapInfoApplicationClass();
mapinfo.Do("Do somthing here");
string value = mapinfo.Eval("Eval something here");
{% endhighlight %}


Nice and easy!

So you compile your application and it runs and does what it has to do. Then a few months down the track you upgrade your version of Mapinfo and BOOM!, your application suddenly doesn't work any more.  Why does it not work anymore?

## Step 3: Finding the reason for not working with different versions.

If you go to the defintion of _MapInfoApplicationClass_ in Visual Studio you will notice something like this:

![def](http://woostuff.files.wordpress.com/2009/03/def.jpg)

Whats with that GUID?  Turns out that is the ID for the registered Mapinfo COM object, and each version of Mapinfo has a different GUID.
	
  * v9.5 GUID = {D66B3D9C-D465-46B8-BFB4-F63F04FB203C}
  * v8.5 GUID = {BA2638EB-CB99-4908-9915-771E04BBB7D3}

So why does your application blow up when you upgrade the version of Mapinfo or run it on different machine with a different version of Mapinfo?  Well lets have a look at the Mapinfo RCW.  

When you create a Mapinfo RCW (Interop.Mapinfo.dll) using Visual Studio it will create a _MapInfoApplicationClass _with the GUID attribute which matches the COM objects and when you call the constructor of _MapInfoApplicationClass_ it will look at all the registered COM objects on the computer to see if there is one with that GUID and if it finds one it will create an instance of it. 

## Summing up: Pros and Cons


In summng up, lets have a look at some of the pros and cons of this approch, most of which I'm sure you have already picked up on.

**_Pros_**

  * Allows strong typed access to members	
  * Allows early binding to take place which will let the compiler check for errors.
  * Fast runtime access to methods due to early binding.

**_Cons_**
  * Tied to the version of Mapinfo that was used when creating the RCW.


There maybe only one con but I believe that it is a pretty big one.  

On the plus side, if you are just creating a once off quick and dirty app, that will only be run once, then the above method will most likely be fine.
