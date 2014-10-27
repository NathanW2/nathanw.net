title: My toolset

Last Updated: 2014

I am a big fan Scott Hanselman and this page was inspired by his [2011 Ultimate Developer and Power Users Tool List for Windows](http://www.hanselman.com/blog/ScottHanselmans2011UltimateDeveloperAndPowerUsersToolListForWindows.aspx) with some extra stuff thrown in.  I have nowhere close to the amount of tools that Scott does but I thought it would be cool to share my setup anyway.

#### Editors\IDEs

[Sublime]: http://www.sublimetext.com/2
[Notepad]: http://notepad-plus-plus.org/
[VS]: http://msdn.microsoft.com/en-au/library/dd831853(v=vs.100).aspx
[QT]: http://qt-project.org/downloads
[AP]: http://www.aptana.com/products/
[PyCharm]: https://www.jetbrains.com/pycharm/

- [Sublime Text 2][Sublime]\\[Notepad++][Notepad] : These two text editors are the best of the bunch.  Sublime Text 2 has a nice simple interface, good text editing features, and simple to configure. Sublime doesn't fill every need so Notepad++ fills any gaps.

- [Visual Studio 2010][VS] : I'm mostly a C++ and Python guy now due to QGIS but every now and then I need to do some C#.

- [Qt Creator][QT] : If you are working with Qt and C++ this is the IDE for it.  Built in Qt help files, form designer, good editor with a vim mode (*good for someone who can't use normal vim*).  Qt Creator is like Visual Studio for Qt C++ but less...bloated.

- [Aptanta Studio 3][AP] : I now much perfer PyCharm however this is still not a bad option if you would like a Python IDE.

- [PyCharm][PyCharm] : While it can be a little memory heavy being build in good ol' Java I haven't found a Python IDE as good as this. Even better there is now a community edition which is free.  You can add the IdeaVim plugin for that bit if vim(ness) and it's a really nice IDE to use. It is almost never closed these days as 90% of my dev work is now Python based.

#### Dev Tools

[git]: http://git-scm.com/
[svn]: http://subversion.tigris.org/
[Con]: https://code.google.com/p/conemu-maximus5/
[python]: https://www.python.org/
[Cygwin]:https://www.cygwin.com/

- [git][git] : Everyone uses git and if you don't you should.

- [ConEmu][Con] : I bloody love this program.  If you are still using cmd.exe to do anything just stop now! Go and download this. Tabs, better copy and paste, resize-able window, predefined tasks, and heaps more. Trust me you will be more productive. I found it though one of Scott's [posts](http://www.hanselman.com/blog/ConEmuTheWindowsTerminalConsolePromptWeveBeenWaitingFor.aspx) and haven't stopped using it since. Really don't even bother with cmd any more.

- [Cygwin][Cygwin] : For all your linux like tools in Windows.

- [Python][python] : Of course. You also have this if you have installed QGIS. On Windows you can still have the QGIS Python install and other Python installs without issues.  I run 3.4, 2.7, with no issues.

#### GIS

[QGIS]: http://www.qgis.org/
[MS]: http://mapserver.org/
[GRASS]: http://grass.osgeo.org/
[SAGA]: http://www.saga-gis.org/
[IL]: http://52north.org/communities/ilwis
[PG]: http://postgis.net/
[2008]: http://www.microsoft.com/en-au/download/details.aspx?id=1695
[intramaps]: http://www.mapsolutions.com.au/intramaps.aspx
[ogr]: http://www.gdal.org/

- [QGIS][QGIS] : Obviously

- [MapServer][MS] : The company I now work for uses MapServer as the base for their [product][intramaps], although that isn't the only reason that I like it of course.

- [GRASS][GRASS]\\[SAGA GIS][SAGA] : Great powerful tools for vector and raster progressing.

- [ILWIS][IL] : I first used this when I did a bushfire project ( the second round was done in QGIS ) however while I don't use it much anymore it still has some cool ideas.

- [PostGIS][PG] : Great relational spatial database

- [SQL Server 2008\\2012 Express][2008] : It's not that bad. 2012 has better spatial support. QGIS supports 2008/2012.

- [ogr/gdal][ogr] : The back bone of a lot of GIS processing. Great command line processing tools.  This one comes installed with QGIS so if you have QGIS you already have access to these tools, look for ogr2ogr, ogrinfo, gdalinfo, etc.

#### Handy tools

[Bins]: http://www.1upindustries.com/bins/
[Fences]: http://www.stardock.com/products/fences/
[Green]: http://getgreenshot.org/
[Drop]: https://www.dropbox.com/
[Paint]: http://getpaint.net/
[GIMP]: http://www.gimp.org/
[EE4]: http://www.microsoft.com/en-au/download/details.aspx?id=18974
[TC]: http://www.ghisler.com/
[Ultra]: http://www.realtimesoft.com/ultramon/
[Skype]: http://www.skype.com/en/
[IRC]: http://www.irssi.org/
[Sysinternals]: http://technet.microsoft.com/en-au/sysinternals/bb842062
[audioswitch]: https://code.google.com/p/audioswitch/

- [Bins][Bins] : This is a nifty little tool that I found tonight.  Lets you group icons into "Bins" in the Windows taskbar so you don't end up with mess of icons.  Handy!  Not free but only $5

- [Fences][Fences] : Another one from Scott's blog.  Handy for sorting out your mess of a desktop.

- [Greenshot][Green] : Great for taking screens shots. Export to Paint, Dropbox, Imgur, file, clipboard, printer. Built-in image editor for annotations. And it's free.

- [Dropbox][Drop] : It always pains me to hear people say "oh my computer crashed and I lost all my documents", and if it's your sister in law two days before an assignment is due then it's even worse. Use Dropbox, or SkyDrive, or something but keep more then one copy of important stuff. 

- [Paint.NET][Paint]\\[GIMP][GIMP] : Even as a developer one needs an editing program.  These are the two best free ones you can get.

- [Expression Encoder 4][EE4] : I have plans to do some screencasting in the future so I am giving this a run to see how things work out. This has a ten minute limit on the free version, but you don't really want to hear me talking for more then ten minutes anyway. 

- [Total Commander][TC] : This is one of the best tools you can get for working with your file system. No drag and drop here. Full keyboard control and speed. Can take a bit to getting used to however it will increase your productivity. 

- [UtlraMon][Ultra] : I can't even work with one screen anymore and this tool helps you get the most out of your monitors. Multi screen taskbar, shortcuts for predefined window locations and more. 

- [Sysinternals][Sysinternals] : If you are a Windows power user and you don't have these you are crazy. Get them now.

- [audioswitch][audioswitch] : A small tray utility to switch audio input and outout.  I have three different inputs connected and three outputs, depending on what I am doing I need to be able to easy swap between the three. The normal Windows method sucks but this makes life a lot easier. One click easy.  I really don't know why this isn't part of Windows, or least the ability to do what it does. 

#### Chat

- [Skype][Skype] : Being a remote worker I require good tools that work for video calls.  Internaly we use Lync however I run a potral video feed into the office most days of the week using Skype and it never fails me. It might be Microsoft but I have never found anything that is a good for video calls.  That have really got something right. 

- [Irssi][IRC] : Good ol' IRC. I have played around with a whole bunch of IRC clients on Windows and Linux but never found one that I liked apart from Irssi.  Sure it runs in a console window but IRC is just text anyway so who cares. I like to tweak things so Irssi scratches that itch for me. nathanW on #qgis.

#### Online

[Trello]: https://trello.com/
[github]: https://github.com/
[gis]: gis.stackexchange.com
[join.me]: https://join.me/
[toggl.com]: http://toggl.com/

- [Trello][Trello] : Another one in the bloody love list.  A simple to use but powerful, well I don't really know how to describe it so you can just check it out.  I use it for personal task management, work projects, software projects, event planning. 

- [GitHub][github] : I really like GitHub it really does add a nice social experience to development that most sites fail on. Even if you aren't in it for the socail side it's still a great site to use.

- [gis.stackexchange.com][gis] : Personally I really think they hit the nail on the head when building this Q&A site. I try to spend as much time as I can on here answering QGIS questions.

- [join.me][join.me] : If you have ever needed to screen share, or see someone elses screen you can know how much of a total pain in the butt it can be. But not anymore. Scott tweated this one day and I have loved it ever since.  It's as simple as telling someone to go to the site, click start meeting, and read you the join code.  No stuffing around. No email sign ups. Nothing.  It runs cross platform (at least Windows and OS X) so it's great for remote debugging famliy computers.  You even have the ability to control the other screen.

- [toggl.com][toggl.com] : A really simple time tracking app that I love to use. Lets you tags, group into project and client, reports for weekly/monthly/custom breakdowns. Great for the remote worker, or everyone really.  A nice feature is it can record the open applications over the day so if you forget what you might have been working on it might spark you memory, unless you were looking at Facebook which in that case, get back to work! 

If anyone has anything extra they can recommend feel free to leave a comment. 

