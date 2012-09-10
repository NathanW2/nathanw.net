---
comments: true
date: 2009-02-24 23:55:36
layout: post
slug: commands-to-a-mbx-program
title: Sending commands to a Mapbasic(.MBX) program from .NET
wordpress_id: 21
categories:
- Mapinfo Programming
tags:
- .NET
- Mapbasic
- mapinfo
- mapping
---

A couple of days ago on the Mapinfo-L Google group there was a question asked regrading passing arguments to specified Mapbasic program from a .Net application using OLE.
I'm going to tackle this in two posts, the first post will just be getting the basics down, the second post I plan on doing some more useful stuff.

The first thing you can do is launch an MBX from inside a .Net application by running the following command.

[sourcecode language="csharp"]
    MapinfoOLEInstance.Do(@"Run Application " + "\"" + @"{myapp.MBX}" + "\"");
[/sourcecode]

Now while this will launch the specified MBX in the current Mapinfo instance, Mapbasic programs do not allow arguments to be passed in at startup via another
program.  

So what is the next best solution, well Mapbasic has a reserved **RemoteMsgHandler** method which when declared in a Mapbasic program will leave the Mapbasic program in memory to listen for commands sent from an OLE object or until the End Program command is called.  

Lets go ahead and create a basic Mapbasic file which will just load in Mapinfo and listen for commands, like so:

_Note:  I will add comments to the source code to explain each section, and will be refered to as RemoteTest.mb/.mbx_

[sourcecode language="vb"]

Include "MAPBASIC.DEF" 
Include "MENU.DEF" 

Declare Sub RemoteMsgHandler 
Declare Sub Main 

Sub Main
    ' We don't need to doing anything here.
End Sub  

Sub RemoteMsgHandler 
    Dim command as String 

    'Call commandinfo to get the string that was sent to us. 
    command = CommandInfo(CMD_INFO_MSG) 
    Note command 
End Sub 
[/sourcecode]

Notice how Sub Main above doesn't contain any code, now normally if you where to run this program in Mapinfo
it would run and then just exit because it reached the end of Sub Main 
but in the _RemoteTest.mb_ program above we have declared the reserved method called **RemoteMsgHandler **which will cause the program to stay in memory and not exit once it has finished in Sub Main. 

Now once the **RemoteMsgHandler **mehtod is called we can call CommandInfo(CMD_INFO_MSG) to get the command that was sent from our .Net application and display it in a message box.

The .Net side of things it is pretty simple basically you have to:



	
  1. Create an instance of Mapinfo.

	
  2. Run the _RemoteTest.MBX._ (remember that sub main dosn't do anything so it will just sit there)

	
  3. Get all the running Mapbasic programs inside our instance of Mapinfo.

	
  4. Find our program using its name.

	
  5. Pass a command to our _RemoteTest.MBX _application.


Enough talk lets see some code:

First we will start with step 1 and 2 from the list above.


#### Step 1: Create an instance of Mapinfo.
Step 2: Run the RemoteTest.MBX.


[sourcecode language="csharp"]
        //... normal using statements
        using Mapinfo;
        static void Main(string[] args) 
        { 
            //Create a instance of Mapinfo
            MapInfoApplicationClass mapinfoinstance = new MapInfoApplicationClass();
            //Make this instance visible, this is just so we can see the note statement. 
            mapinfoinstance.Visible = true; 
            //Create a command string that contains the path to our mbx to be run.
            string appcommand = "Run Application " + "\"" + @"RemoteTest.MBX" + "\""; 

            //Run the command in Mapinfo.
            mapinfoinstance.Do(appcommand);
        }
[/sourcecode]

Now save and run the above code, if everything went ok the code should run, load Mapinfo and run the MBX file and just sit there.
If it did, great! That's what we wanted it to do.

Now stop your .Net program and close the running instance of Mapinfo.
On to the next step:


#### Step 3: Get all the running Mapbasic programs inside our instance of Mapinfo.


We can get all the running Mapbasic programs inside Mapinfo by using the following command:

[sourcecode language="csharp"]
     DMBApplications MBApps = (DMBApplications)mapinfoinstance.MBApplications; 
[/sourcecode]

MBApplications contains a collection of the currenly running Mapbasic programs running inside your instance of
Mapinfo.  Because MBApplications is just an object type we have to cast it to the DMBApplications interface which can be found in the Mapinfo namespace.


![DMBApplications](http://woostuff.files.wordpress.com/2009/02/objects.png)



 Now onto the last two steps.


#### Step 4: Find our program using its name.


Step four can be done two ways, one way is if you have LINQ and the other is just using a for loop.  I will show the LINQ method first.

[sourcecode language="csharp"]
             //If you can use LINQ you can do this:
             DMapBasicApplication  myapp = (from DMapBasicApplication app in MBApps
                                            where app.Name == "RemoteTest.MBX"
                                            select app).Single();
 [/sourcecode]

and now the for loop

[sourcecode language="csharp"]
            //If you don't have LINQ you can do this.
            DMapBasicApplication  myapp;
            foreach (DMapBasicApplication app in MBApps) 
            { 
                if (app.Name == "RemoteTest.MBX") 
                { 
                    myapp  = app; 
                    break; 
                } 
            }  
 [/sourcecode]

MBApps(which was declared in step three) should have had a collection of Mapbasic programs that are running in Mapinfo.  We can cast each one of these programs the inteface DMapBasicApplication found in the Mapinfo namespace. 

Both the above methods should preform around the same,   I prefer the LINQ method as it feels a little bit cleaner.


#### Step 5: Pass a command to our RemoteTest.MBX application.


The last thing we have to do is pass the command into the Mapbasic program,  which can be done like this.

[sourcecode language="csharp"]
myapp.Do("Hello World");
[/sourcecode]

When _myapp.Do is called, _it will call the **RemoteMsgHandler **in our Mapbasic file and pass in the "Hello World" string, which we then read and print to a messsage box.

That is pretty much it.  You should be able to complie and run.  Mapinfo should show you a message box with "Hello World" printed in it.

The final .Net code should look like this, using LINQ of course :).

[sourcecode language="csharp"]
        //... normal using statements
        using Mapinfo;
        static void Main(string[] args) 
        { 
            //Create a instance of Mapinfo
            MapInfoApplicationClass mapinfoinstance = new MapInfoApplicationClass();
            //Make this instace visible, this is just so we can see the note statement. 
            mapinfoinstance.Visible = true; 
            //Create a command string that contains the path to our mbx to be run.
            string appcommand = "Run Application " + "\"" + @"RemoteTest.MBX" + "\""; 

            //Run the command in Mapinfo.
            mapinfoinstance.Do(appcommand);
            DMBApplications MBApps = (DMBApplications)mapinfoinstance.MBApplications; 
            DMapBasicApplication  myapp = (from DMapBasicApplication app in MBApps
                                            where app.Name == "Test.MBX"
                                            select app).Single();
            myapp.Do("Hello World");
        }
[/sourcecode]

In my next post I will create a simple method name parser in the **RemoteMsgHandler **method** **to handle calling methods inside of a our Mapbasic program.
