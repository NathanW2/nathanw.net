---
comments: true

layout: post
slug: wpfmapinfo
title: Showing a WPF form in Mapinfo 9.5.
wordpress_id: 5
categories:
- Mapinfo Programming
tags:
- .NET
- Mapbasic
- mapinfo
- mapping
- WPF
---

Being able to call methods inside of an dll or exe that has a CLR header is one of MapInfo 9.5 newest features. MapInfo 9.5 was released a couple of weeks ago now and since then I have been playing around with this new ability which I must say has some really good advantages with .net being a type safe and managed.

Then first thing I tried was to call a shared method in a dll that presented very basic win32 form with a couple of buttons on it, this works like a charm and was very easy to do (I'll make my next post about this). Anyway yesterday I was sitting there looking at the create a new project dialog in Visual Studio and thought "I wonder if I can show a WPF form in MapInfo".

It turns out that you can show a WPF form in MapInfo 9.5 but I requires some different code then that of the Win32 way. I created a basic WPF form with some text "This is a test MapInfo WPF form" and a button. Now for the code in order to show a WPF form in Mapinfo you need to use a class called Windows.Interop.WindowInteropHelper which will allow you to use a window handle as the owner of the of a WPF form becuase the WPF form ShowDialog function dosn't take any arguments like the Win32  

The resulting code looks like this:

{% highlight csharp %}
using System.Windows.Interop;
//...
public static void ShowForm(int handle)
        {
            Window1 window = new Window1();
            WindowInteropHelper helper = new WindowInteropHelper(window);
            helper.Owner = new IntPtr(handle);
            window.ShowDialog();
        }
{% endhighlight %}


Now when you run the mbx calling the ShowFrom method it will set the owner of the WPF form to the MapInfo window with that handle. Which will result in something like this:




![wpfform](http://woostuff.files.wordpress.com/2009/01/wpfform.jpg)
