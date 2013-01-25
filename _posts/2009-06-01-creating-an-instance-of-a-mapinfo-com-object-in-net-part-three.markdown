---
comments: true
date: 2009-06-01 16:30:15
layout: post
slug: creating-an-instance-of-a-mapinfo-com-object-in-net-part-three
title: Creating an instance of a Mapinfo COM object in .NET - Part Three
wordpress_id: 192
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

In part three of the series [Creating a instance of a Mapinfo COM object in .NET](http://woostuff.wordpress.com/2009/04/01/com-instance-mapinfo-main/), I'm going to be talking about **creating an instance of Mapinfo's COM object using Activator.CreateInstace but also allowing you to have strong typed access to Mapinfo's members**.  This approach unlike the approach outlined in [part two](http://woostuff.wordpress.com/2009/05/06/creating-a-instance-of-a-mapinfo-com-object-in-net-part-two/), will allow for your application to be Mapinfo version independent without having to use reflection to get access to _Do_ and _Eval_

_If you haven't read part [one ](http://woostuff.wordpress.com/2009/04/01/com-instance-part-one/)and [two ](http://woostuff.wordpress.com/2009/05/06/creating-a-instance-of-a-mapinfo-com-object-in-net-part-two/) I would recommend reading them first as it will give you an understanding of where this post is heading._


## Step 1: Adding a referance to Mapinfo.


As this method requires us to get access to some of the interfaces that Mapinfo provides, we will need to add a reference to Mapinfo like we did in first step  in part one.

To save on re-explaining the whole process here again, I will wait while you head over to part [one](http://woostuff.wordpress.com/2009/04/01/com-instance-part-one/) and follow the process outlined in step 1.  Make sure that you come back here after you have completed step 1.


## Step 2: Creating the instance


Now that you are back, we can continue.

The process in this step is similar to the process outlined in Part two step 1, however things will differ a little bit.

If you have a look at the Interop.Mapinfo.dll in the object browser of visual studio you will notice that the class called _MapinfoApplicationClass_, implments a interface called _DMapinfo_.
![DMapinfo](http://woostuff.files.wordpress.com/2009/06/dmapinfo1.jpg)

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Does that _MapinfoApplicationClass_ class look familiar?  It should as it is what we used to create the Mapinfo instance in part one of this series, but we don't need that class here so we will just forget about it.  What we do need is that interface called _DMapinfo_ as it provides all the methods that we need to interact with Mapinfo.

If we have the code that we used in part two step 1 for creating the instance of Mapinfo.

{% highlight csharp %}
Type mapinfotype = Type.GetTypeFromProgID("Mapinfo.Application");
object instance = Activator.CreateInstance(mapinfotype);
{% endhighlight %}

now this code is great and all but we run into the problem that we had in part two where C# doesn't support late binding so we have to use reflection which just feels dirty. There has to be a better way.

What object is Activator.CreateInstace returning in the above code anyway?

Turns out that the object that it returns also implements the interface _DMapinfo_, this is good for us as it allows us to cast the object returned from Activator.CreateInstance() to the type _DMapinfo_.  If we go and add the right casting to the code it should now look like the following.

{% highlight csharp %}
Type mapinfotype = Type.GetTypeFromProgID("Mapinfo.Application");
DMapInfo instance = (DMapInfo)Activator.CreateInstance(mapinfotype);
{% endhighlight %}

Cool, so we have created a instance of Mapinfo and casted it to the type _DMapinfo_ now we should be able to do something useful with it.



## Step 3: Using the object.


Because we have casted our object to the interface called _DMapinfo_, we can now get strongly typed access to Mapinfo's Do and Eval method. No more reflection needed :).

Some sample code:
{% highlight csharp %}
Type mapinfotype = Type.GetTypeFromProgID("Mapinfo.Application");
DMapInfo instance = (DMapInfo)Activator.CreateInstance(mapinfotype);

instance.Do("Print 1234567");
string value = instance.Eval("NumTables()");
{% endhighlight %}



## More information on DMapinfo.


If we have a look at the GUID on the top of the _DMapinfo_ interface you will notice that it looks something like this:

{% highlight csharp %}
[Guid("1D42EC63-7B28-11CE-B83D-00AA002C4F58")]
public interface DMapInfo
{% endhighlight %}

This GUID for DMapinfo, which unlike the GUID for the MapinfoApplicationClass is the same for every Mapinfo version.  
Because it is the same we can create Mapinfo using Activator.CreateInstance() which will return a COM object, cast it DMapinfo and by making calls against the interface we don't have to worry about what version of Mapinfo the client is running.



## Summing up: Pros and Cons


In this post I have outlined how you can create an instance of Mapinfo using Activator.CreateInstance() and cast the return object to the interface called DMapinfo. This technique allows us to have Mapinfo version independence while still maintaining our type safety and compiler support.

**_Pros_**



	
  * Allows Mapinfo version independence.

        
  * Strong Typed

        
  * Cleaner then having to use reflection.

        
  * Faster method calling then using reflection.


**_Cons_**



       
  * No real cons




