---
comments: true
date: 2009-05-06 15:15:47
layout: post
slug: creating-a-instance-of-a-mapinfo-com-object-in-net-part-two
title: Creating an instance of a Mapinfo COM object in .NET - Part Two
wordpress_id: 120
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

In part two of the series [Creating a instance of a Mapinfo COM object in .NET](2009/04/01/com-instance-mapinfo-main/), I'm going to be talking about **creating an instance of Mapinfo's COM object using reflection and Activator.CreateInstace**.  This approach unlike the approach outlined in [part one](2009/04/01/com-instance-part-one/), will allow for your application to be Mapinfo version independent.


## Step 1: Creating a COM instance of Mapinfo.


Unlike part one where the first step was to create a reference to the Mapinfo COM object, we won't be needing to do that here as we are using reflection to create an instance straight away.

The first function that we need to call is called _Type.GetTypeFromProgID, _ this will return a type  using the program ID of an application.  Where do we get this program ID from?  A listing in HKEY_CLASSES_ROOT is created when a application registers itself as a COM server, this listing includes things like the GUID of the application, the applications program ID and the path to the application to use as the COM server.  Lets have a quick look at how mapinfo is registered in the registry.

![registry](http://woostuff.files.wordpress.com/2009/04/registry.jpg)

If you have read part one of this series you will notice that the GUID above is for Mapinfo 9.5, we don't need to use this GUID anywhere in this post so I have only marked it in the above picture just as a note.

You will notice two other things in the picture above, one is the key _ProgID _and the other is the key _VersionIndependentProgID ,_ these keys contain the program ID that can be used by _Type.GetTypeFromProgID_ to create an instance of Mapinfo.
Enough about the registry lets see some code.

First lets get the type associated to Mapinfo using the program ID that's in the registry, like so:

{% highlight csharp %}
Type mapinfotype = Type.GetTypeFromProgID(&quot;Mapinfo.Application&quot;);
{% endhighlight %}

The above code will now search the regisrty for a application with the program ID equaling _"Mapinfo.Application" _and return the type for that application or as the documentation in the .NET framework says.


> Gets the type associated with the specified program identifier (ProgID),
returning null if an error is encountered while loading the System.Type.


Moving on. Now that we have the type that is associated to Mapinfo's COM object we can now go and create an instance of Mapinfo from this type, for this we will need a static method in the _Activator _ class.  The code that we will need to call is like this:

{% highlight csharp %}
object instance = Activator.CreateInstance(mapinfotype);
{% endhighlight %}

Passing the type that we got returned from_ Type.GetTypeFromProgID_ into the _CreateInstance _method will create an instance of Mapinfo for us and return it as a object. If we join the above code together we should have something like this:

{% highlight csharp %}
Type mapinfotype = Type.GetTypeFromProgID(&quot;Mapinfo.Application&quot;);
object instance = Activator.CreateInstance(mapinfotype);
{% endhighlight %}

Now that we have created an instance of Mapinfo we can go ahead and start using it.


## Step 2: Using the object.


The biggest problem with doing things this way is that because we only have the instance of Mapinfo as a object type we have to use reflection to get access to the _Do_ and _Eval_ methods that Mapinfo provides.

So what we will do first is create a our own _Do_ method that wraps up the reflection process, so we don't have to see it every time we need to call _Do_
{% highlight csharp %}
public void Do(string command) {}
{% endhighlight %}

 Now lets go on and fill out the reflection bit.
{% highlight csharp %}
public void Do(string command)
{
      parameter[0] = command; 
      mapinfoType.InvokeMember(&quot;Do&quot;,
                    BindingFlags.InvokeMethod,
                    null, instance, parameter); 
} 
{% endhighlight %}

 The above code will invoke the _Do_ method in Mapinfo using reflection and pass in the command string that we supplied.


> A note about the above code because we are using a COM object we have very limited use of reflection and have to use the InvokeMember method, which is slow compared to the optimized reflection methods that we can use on .NET objects.  I won't go into details here but if you do a quick google search on InvokeMemeber vs Methodinfo.Invoke speed you will find what I'm talking about.  Moving on. See speed test section form notes.


Now that we have to _Do_ method out of the way lets move on to _eval_. Pretty much the same process but it will return a string insteed of a void type.  

{% highlight csharp %}
public string Eval(string command)
{
      parameter[0] = command; 
      return (string)mapinfoType.InvokeMember(&quot;Eval&quot;, BindingFlags.InvokeMethod,
                             null,instance,parameter); 
} 
{% endhighlight %}

 Done, now lets put that all together in a nice class with a static CreateInstance method. {% highlight csharp %}
public class Mapinfo
{
   private object mapinfoinstance;
   public Mapinfo(object mapinfo)
   {
     this. mapinfoinstance = mapinfo;
   }

   public static Mapinfo CreateInstance()
   {
        Type mapinfotype = Type.GetTypeFromProgID(&quot;Mapinfo.Application&quot;);
        object instance = Activator.CreateInstance(mapinfotype);
        return new Mapinfo(instance);
    }

    public void Do(string command)
    {
          parameter[0] = command;
          mapinfoType.InvokeMember(&quot;Do&quot;,
                    BindingFlags.InvokeMethod,
                    null, instance, parameter);
     }

     public string Eval(string command)
     {
         parameter[0] = command;
         return (string)mapinfoType.InvokeMember(&quot;Eval&quot;, BindingFlags.InvokeMethod,
                             null,instance,parameter);
      }
}
{% endhighlight %}

 Now that we have it wrapped up in a nice class we can go ahead and use it in our application, something like this:  {% highlight csharp %}
public static void Main()
{
    Mapinfo mymapinfo = Mapinfo.CreateInstance();
    mymapinfo.Do(//Run some command);
}
{% endhighlight %}




## Summing up: Pros and Cons


In summng up, lets have a look at some of the pros and cons of this approch.  **_Pros_**



	
  * Allows Mapinfo version independence.


**_Cons_**



	
  * Not strongly typed

	
  * Is late bound using reflection = no complier support + slower speed  See Speed test section

	
  * Using reflection has speed issues due to it having to get type information everytime Do or Eval methods are called. See Speed test section

	
  * You have to write wrapper methods around the reflection process.

	
  * Can't easily get to methods that Mapinfo provides, with out wrapping them up first.


This approach has a lot more cons then pros as you can see, some of them are pretty big ones, the real only advantage it gives you is the ability to work with any version Mapinfo.  My next post will outline a method that allows both version independence and strong typed access and no late binding.
