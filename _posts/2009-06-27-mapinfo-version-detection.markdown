---
comments: true
date: 2009-06-27 14:50:21
layout: post
slug: mapinfo-version-detection
title: MapInfo version detection.
wordpress_id: 220
categories:
- Mapinfo Programming
tags:
- .NET
- Mapbasic
- mapinfo
- mapinfo ole
- mapping
---

I thought I would just write a follow up post for my creating an instance of MapInfo COM object series about being able to detect which version of MapInfo the user has installed.

 

In this blog post I'm going to show some sample code that you can use to find which version/s of MapInfo the user has installed, to allow you to notify which version of MapInfo your application is compatible with.

 

When you install MapInfo, it creates a key in the registry which stores information for MapInfo like MI version,COM GUID, Access code etc. The key that contains this information is located in:

 

HKEY_LOCAL_MACHINE\SOFTWARE\MapInfo\MapInfo\Professional

 

if we open up the registry and have a look at that key we should be able to see something that looks like this:

 

[![image](http://woostuff.files.wordpress.com/2009/06/image_thumb.png)](http://woostuff.files.wordpress.com/2009/06/image.png)

 

 

 

 

 

 

In the above picture you can see that professional subkey shows a folder for each version of MapInfo that you have installed, as you can see on my PC I have version 9.5 and 10 installed. Each one of these keys holds the information for that installed version of MapInfo, if we have a look at the information of version 10 it looks something like this:

 

[![image](http://woostuff.files.wordpress.com/2009/06/image_thumb1.png)](http://woostuff.files.wordpress.com/2009/06/image1.png)

 

 

 

 

 

 

 

 

 

 

 

As you can see the key has all the information about the installed version 10 of MapInfo including Access Code(000000 for demo version),the COM GUID for MapInfo and install path.

 

Enough talk lets see some code:

 

This is a little bit of C#3.0 sample code that you can use to detect and display which version of MapInfo the version has installed.

 

  

    
    
    <span style="color:#606060;">   1:</span> <span style="color:#0000ff;">string</span> registryKey = <span style="color:#006080;">@"SOFTWARE\MapInfo\MapInfo\Professional"</span>;



    
    
    <span style="color:#606060;">   2:</span>  



    
    
    <span style="color:#606060;">   3:</span> <span style="color:#0000ff;">using</span> (Microsoft.Win32.RegistryKey prokey = Registry.LocalMachine.OpenSubKey(registryKey))



    
    
    <span style="color:#606060;">   4:</span> {



    
    
    <span style="color:#606060;">   5:</span>     var versions = from a <span style="color:#0000ff;">in</span> prokey.GetSubKeyNames()



    
    
    <span style="color:#606060;">   6:</span>                    let r = prokey.OpenSubKey(a)



    
    
    <span style="color:#606060;">   7:</span>                    let name = r.Name



    
    
    <span style="color:#606060;">   8:</span>                    let slashindex = name.LastIndexOf(<span style="color:#006080;">@"\")



    
    
    <span style="color:#606060;">   9:</span>                    select new



    
    
    <span style="color:#606060;">  10:</span>                    {



    
    
    <span style="color:#606060;">  11:</span>                       MapinfoVersion = Convert.ToInt32(name.Substring(slashindex + 1,



    
    
    <span style="color:#606060;">  12:</span>                                                                        name.Length - slashindex -1))



    
    
    <span style="color:#606060;">  13:</span>                    };



    
    
    <span style="color:#606060;">  14:</span>  



    
    
    <span style="color:#606060;">  15:</span>     Console.WriteLine("</span>Installed Mapinfo Version<span style="color:#006080;">");



    
    
    <span style="color:#606060;">  16:</span>     foreach (var item in versions)



    
    
    <span style="color:#606060;">  17:</span>     {



    
    
    <span style="color:#606060;">  18:</span>         Console.WriteLine("</span>Mapinfo Version: {0}", item.MapinfoVersion);



    
    
    <span style="color:#606060;">  19:</span>     }



    
    
    <span style="color:#606060;">  20:</span> }


  








If you don’t want to use LINQ you could use something like this:






  


    
    
    <span style="color:#606060;">   1:</span> <span style="color:#0000ff;">string</span> registryKey = <span style="color:#006080;">@"SOFTWARE\MapInfo\MapInfo\Professional"</span>;



    
    
    <span style="color:#606060;">   2:</span>  



    
    
    <span style="color:#606060;">   3:</span> <span style="color:#0000ff;">using</span> (Microsoft.Win32.RegistryKey prokey = Registry.LocalMachine.OpenSubKey(registryKey))



    
    
    <span style="color:#606060;">   4:</span> {



    
    
    <span style="color:#606060;">   5:</span>     List<<span style="color:#0000ff;">int</span>> versions = <span style="color:#0000ff;">new</span> List<<span style="color:#0000ff;">int</span>>();



    
    
    <span style="color:#606060;">   6:</span>     <span style="color:#0000ff;">foreach</span> (<span style="color:#0000ff;">string</span> key <span style="color:#0000ff;">in</span> prokey.GetSubKeyNames())



    
    
    <span style="color:#606060;">   7:</span>     {



    
    
    <span style="color:#606060;">   8:</span>         RegistryKey subkey = prokey.OpenSubKey(key);



    
    
    <span style="color:#606060;">   9:</span>         <span style="color:#0000ff;">string</span> name = subkey.Name;



    
    
    <span style="color:#606060;">  10:</span>         <span style="color:#0000ff;">int</span> slashindex = name.LastIndexOf(<span style="color:#006080;">@"\");



    
    
    <span style="color:#606060;">  11:</span>         int version = Convert.ToInt32(name.Substring(slashindex + 1,



    
    
    <span style="color:#606060;">  12:</span>                                                      name.Length - slashindex - 1));



    
    
    <span style="color:#606060;">  13:</span>         versions.Add(version);



    
    
    <span style="color:#606060;">  14:</span>     }



    
    
    <span style="color:#606060;">  15:</span>  



    
    
    <span style="color:#606060;">  16:</span>     Console.WriteLine("</span>Installed Mapinfo Version<span style="color:#006080;">");



    
    
    <span style="color:#606060;">  17:</span>     foreach (int mapinfoversion in versions)



    
    
    <span style="color:#606060;">  18:</span>     {



    
    
    <span style="color:#606060;">  19:</span>         Console.WriteLine("</span>Mapinfo Version: {0}", mapinfoversion);



    
    
    <p><span style="color:#606060;">  20:</span>     }</p>


  








Both will output the installed versions to the console:





[![image](http://woostuff.files.wordpress.com/2009/06/image_thumb2.png)](http://woostuff.files.wordpress.com/2009/06/image2.png)





Now detecting the version is all well and good but you really need to tell the user if they won’t be able to use your application if they are running a version lower then your application was built with.





Something like this would do it: 
    







  


    
    
    <span style="color:#606060;">   1:</span> <span style="color:#0000ff;">const</span> <span style="color:#0000ff;">int</span> NeededMapinfoVersion = 1000;



    
    
    <span style="color:#606060;">   2:</span>  



    
    
    <span style="color:#606060;">   3:</span> Console.WriteLine(<span style="color:#006080;">"Checking Mapinfo Version"</span>);



    
    
    <span style="color:#606060;">   4:</span> <span style="color:#0000ff;">foreach</span> (var item <span style="color:#0000ff;">in</span> versions)



    
    
    <span style="color:#606060;">   5:</span> {



    
    
    <span style="color:#606060;">   6:</span>     <span style="color:#0000ff;">if</span> (item.MapinfoVersion < NeededMapinfoVersion)



    
    
    <span style="color:#606060;">   7:</span>     {



    
    
    <span style="color:#606060;">   8:</span>         Console.WriteLine(<span style="color:#006080;">"Sorry I need Mapinfo Version {0} but you have {1}"</span>,



    
    
    <span style="color:#606060;">   9:</span>                           NeededMapinfoVersion,item.MapinfoVersion);



    
    
    <span style="color:#606060;">  10:</span>        <span style="color:#008000;">// Exit the app.</span>



    
    
    <span style="color:#606060;">  11:</span>     }



    
    
    <span style="color:#606060;">  12:</span>     <span style="color:#0000ff;">else</span>



    
    
    <span style="color:#606060;">  13:</span>     {



    
    
    <span style="color:#606060;">  14:</span>         Console.WriteLine(<span style="color:#006080;">"Your good to go"</span>);



    
    
    <span style="color:#606060;">  15:</span>         <span style="color:#0000ff;">break</span>;



    
    
    <span style="color:#606060;">  16:</span>     }



    
    
    <span style="color:#606060;">  17:</span> }


  












Of course the above code is pretty rough but it should do the trick.





Hope this helps.
