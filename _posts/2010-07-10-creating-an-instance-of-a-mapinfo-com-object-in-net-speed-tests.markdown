---
comments: true
date: 2010-07-10 22:24:27
layout: post
slug: creating-an-instance-of-a-mapinfo-com-object-in-net-speed-tests
title: Creating an instance of a MapInfo COM object in .NET – Speed Tests
wordpress_id: 344
categories:
- Mapinfo Programming
tags:
- .NET
- C#
- Mapbasic
- mapinfo
- mapinfo interop
- mapinfo ole
- MapInfo Professional
---

A while ago I posted about how to create an instance of MapInfo in .Net, If you missed those posts then they can be found [here](https://woostuff.wordpress.com/2009/04/01/com-instance-mapinfo-main/).  In these posts I outlined how you can create a instance using three different methods, in the reflection based post I said that one of the disadvantages of doing it this way was that it was slower.   I said this due to just my observations but I thought it would be a good idea to put it to the test and show the speed difference.

I created a simple project to test and show me the results of three different things: Speed of complied MBX, calling a MapBasic function though the Do and via the interface (see posts [1](https://woostuff.wordpress.com/2009/04/01/com-instance-part-one/) & [3](https://woostuff.wordpress.com/2009/06/01/creating-an-instance-of-a-mapinfo-com-object-in-net-part-three/)) and calling Do and Eval via reflection (see post [2](https://woostuff.wordpress.com/2009/05/06/creating-a-instance-of-a-mapinfo-com-object-in-net-part-two/))

The code is simple, and is posted at the bottom of this post, the command “Fetch Next From {Table}” is called a number of times: 100;200;300;500;1000;2000;5000 and each block is timed.

After running each iteration set 3 times, these are the results :

[![SpeedTests](http://woostuff.files.wordpress.com/2010/07/speedtests_thumb.png)](http://woostuff.files.wordpress.com/2010/07/speedtests.png)

Behold my fancy graph making skills….or lack there of.  The time is in seconds, so the 0.032 in the Interface pass 1 is 0.032 seconds for 200 iterations which is still pretty quick.  You’ll notice that using the reflection based method starts to really take its toll when you are doing 5000 iterations, mind you ~1 second is still pretty quick.

The Mapbasic code I used:

[sourcecode language="csharp"]
Declare Sub Main
Declare Function Time(count as Integer) as Float
Declare Function GetTickCount Lib "kernel32" () As Integer

Sub Main
   Dim pass as Integer
   pass = 0
	Dim a,b,c,d,e,f,g as Integer
   a = 100
   b = 200
   c = 300
   d = 500
   e = 1000
   f = 2000
   g = 5000

	Do While pass <= 2
       Print "====PASS " + pass + "========="
       Print Time(a)
       Print Time(b)
       Print Time(c)
       Print Time(d)
       Print Time(e)
       Print Time(f)
       Print Time(g)
		pass = pass + 1
   Loop
End Sub

Function Time(count as Integer) as Float
    Dim a as Integer
    Dim b as Integer
	Dim i as Integer
	a = GetTickCount()
	For i = 0 to count
       Fetch Next From Untitled
    Next
	b = GetTickCount()
	Time = (b - a) / 1000
End Function
[/sourcecode]

and the C# code:

[sourcecode language="csharp"]
class ReflectionMapInfo
    {
        private readonly object mapinfo;

        public ReflectionMapInfo(object mapinfo)
        {
            this.mapinfo = mapinfo;
        }

        public void Do(string commandstring)
        {
            this.mapinfo.GetType().InvokeMember("Do", BindingFlags.InvokeMethod,
                                                                null, this.mapinfo,
                                                                new[] {commandstring});
        }
    }

    class Program
    {
        [DllImport("kernel32.dll", CharSet = CharSet.Auto, ExactSpelling = true)]
        public static extern int GetTickCount();
        static MapInfoApplication mapinfo = new MapInfoApplication();
        static ReflectionMapInfo reflectionmapinfo = new ReflectionMapInfo(mapinfo);

        static void Main(string[] args)
        {
            mapinfo.Do(@"Open Table ""C:\Users\Woo\Documents\Untitled.TAB""");

            int pass = 0;
            while (pass <= 2)
            {
                Console.WriteLine("Interface Test, Pass " + pass + "Count 100 " + Time(100));
                Console.WriteLine("Interface Test, Pass " + pass + "Count 200 " + Time(200));
                Console.WriteLine("Interface Test, Pass " + pass + "Count 300 " + Time(300));
                Console.WriteLine("Interface Test, Pass " + pass + "Count 500 " + Time(500));
                Console.WriteLine("Interface Test, Pass " + pass + "Count 1000 " + Time(1000));
                Console.WriteLine("Interface Test, Pass " + pass + "Count 2000 " + Time(2000));
                Console.WriteLine("Interface Test, Pass " + pass + "Count 5000 " + Time(5000));
                pass++;
            }

            pass = 0;
            while (pass <= 4)
            {
                Console.WriteLine("Reflection Test, Pass " + pass + "Count 100 " + ReflectionTime(100));
                Console.WriteLine("Reflection Test, Pass " + pass + "Count 200 " + ReflectionTime(200));
                Console.WriteLine("Reflection Test, Pass " + pass + "Count 300 " + ReflectionTime(300));
                Console.WriteLine("Reflection Test, Pass " + pass + "Count 500 " + ReflectionTime(500));
                Console.WriteLine("Reflection Test, Pass " + pass + "Count 1000 " + ReflectionTime(1000));
                Console.WriteLine("Reflection Test, Pass " + pass + "Count 2000 " + ReflectionTime(2000));
                Console.WriteLine("Reflection Test, Pass " + pass + "Count 5000 " + ReflectionTime(5000));
                pass++;
            }
            Console.ReadLine();
        }

        public static double Time(int count)
        {
            int start = GetTickCount();
            for (int i = 0; i < count; i++)
            {
                mapinfo.Do("Fetch Next From Untitled");
            }
            int end = GetTickCount();
            mapinfo.Do("Fetch First From Untitled");
            return (end - start) / 1000d;
        }

        public static double ReflectionTime(int count)
        {
            int start = GetTickCount();
            for (int i = 0; i < count; i++)
            {
                reflectionmapinfo.Do("Fetch Next From Untitled");
            }
            int end = GetTickCount();
            reflectionmapinfo.Do("Fetch First From Untitled");
            return (end - start) / 1000d;
        }
    }
[/sourcecode]
