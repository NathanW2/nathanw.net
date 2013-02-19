---
comments: true

layout: post
slug: embedding-the-whole-mapinfo-application-in-a-net-form
title: 'Embedding the whole Mapinfo application in a .Net form. '
wordpress_id: 244
categories:
- Mapinfo Programming
tags:
- .NET
- Mapbasic
- mapinfo
- mapinfo interop
- mapinfo ole
---

Not sure if I'll ever have a need for this, but someone else may so I thought I would throw this up here, just in case.

A couple of days ago there was a question on MapInfo-l about embedding MapInfo into a .Net application([http://groups.google.com/group/mapinfo-l/browse_thread/thread/15dfc23ceff8ceef](http://groups.google.com/group/mapinfo-l/browse_thread/thread/15dfc23ceff8ceef)).
Embedding a map window into .Net is something that is covered in the Mapbasic manual however this is not what was needed, what was interesting was the person wanted to be able to embed the whole Mapinfo application menus and all into a .Net contol.

As I had not done this before or seen anyone else do it I thought it might be interesting to have a look into it, knowing also that by using Win32 libraries from .Net(_eg User32.dll_) you could do some cool stuff I figured why not?

The following code is what I managed to write that lets me embed the whole application into a .Net control(I let the code comments explain what is going on):

_For this code to work you will need to create a .Net form with a picture box somewhere on it and a button that calls button1_click for it's click handler, you will also need to reference Mapinfow.exe/Mapinfo COM server see _[_2009/04/01/com-instance-mapinfo-main/_](/2009/04/01/com-instance-mapinfo-main/)_ for details._


{% highlight csharp %}
    public partial class Form1 : Form
    {
        // Sets the parent of a window.
        [DllImport("User32", CharSet = CharSet.Auto, ExactSpelling = true)]
        internal static extern IntPtr SetParent(IntPtr hWndChild, IntPtr hWndParent);

        //Sets window attributes
        [DllImport("USER32.DLL")]
        public static extern int SetWindowLong(IntPtr hWnd, int nIndex, int dwNewLong);

        //Gets window attributes
        [DllImport("USER32.DLL")]
        public static extern int GetWindowLong(IntPtr hWnd, int nIndex);

        //assorted constants needed
        public static int GWL_STYLE = -16;
        public static int WS_CHILD = 0x40000000; //child window
        public static int WS_BORDER = 0x00800000; //window with border
        public static int WS_DLGFRAME = 0x00400000; //window with double border but no title
        public static int WS_CAPTION= WS_BORDER | WS_DLGFRAME; //window with a title bar
        public static int WS_MAXIMIZE = 0x1000000;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Create a new instance of MapInfo.
            MapInfoApplication mapinfo = new MapInfoApplication();

            // Get the handle to the whole MapInfo application.
            // 9 = SYS_INFO_MAPINFOWND.
            string handle = mapinfo.Eval("SystemInfo(9)");

            // Convert the handle to an IntPtr type.
            IntPtr oldhandle = new IntPtr(Convert.ToInt32(handle));

            //Make mapinfo visible otherwise it won't show up in our control.
            mapinfo.Visible = true;

            //Set the parent of MapInfo to a picture box on the form.
            SetParent(oldhandle, this.pictureBox1.Handle);

            //Get current window style of MapInfo window
            int style = GetWindowLong(oldhandle, GWL_STYLE);

            //Take current window style and remove WS_CAPTION(title bar) from it
            SetWindowLong(oldhandle, GWL_STYLE, (style & ~WS_CAPTION));

            //Maximize MapInfo so that it fits into our control.
            mapinfo.Do("Set Window 1011 Max");
        }
    }
{% endhighlight %}

After the code is complied and run you should end up with a screen like this:
_(Once the whole MapInfo application is embedded into our C# application, we can still do all the Do and Eval methods that we normally would when doing integrated Mapping) _

    
    <a href="http://woostuff.files.wordpress.com/2010/02/re-parented-whole-mapinfo-pro-application2.jpg"><img src="http://woostuff.files.wordpress.com/2010/02/re-parented-whole-mapinfo-pro-application2.jpg" title="Re-parented whole MapInfo Pro application" height="707" width="949" alt="" class="alignleft size-full wp-image-253"></img></a>



