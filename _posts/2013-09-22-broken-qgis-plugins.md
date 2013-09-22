---
layout: post
title: "Oh God my plugins! My precious QGIS plugins"
tagline: "or Why did updating to QGIS 2.0 break my plugins?"
description: "Missing plugins when updating to QGIS. Don't stress.  We needed to update the API to make things better."
category: qgis
tags: [qgis, plugins, python, api]
---

### tl;dr 

The API had to change. We don't like breaking plugins. It makes us sad. We did it now to save pain in the future. You will like the new version better. Trust me.

### What happened to my cheese?

When updating to QGIS 2.0 you might have noticed two things. (Apart from all the new awesome stuff!) 

1. All your settings have been set back to defaults
2. Some of your plugins are gone, or missing in the installer.

Resetting of settings is caused by QGIS now storing its 2.0 settings in a different folder then we used for 1.8.  In 1.8, all your plugins, etc, were stored in the ``./qgis`` folder in your home directory, in 2.0 these are now stored in ``./qgis2``. The reason will become evident later.  All user settings, the UI layout, database connections, etc, are now stored in a ``QGIS`` location. In windows this in the registry key ``HKEY_CURRENT_USER\Software\QGIS\QGIS2``.  So this explains why your settings are missing when you first load QGIS 2.0.

### Why did we have to move the settings location? 

Good question.

2.0 is very different from 1.8.  There has been a lot of work to make this the best version we have ever made, new features, more bug fixes, a bigger dev team, and a even bigger community.  Being the next major release we had to make some calls to remove some of the old code and features that were weighing us down.  Features such as the old labelling engine, old symbol engine, the old vector API.  Carrying old code and old out dated features into the future can sometimes really hurt a project and they have to be cut loose.  Because of the massive amount of changes in 2.0 people needed to be able to run 2.0 and 1.8 on the same machine without causing any issues.  If they both store settings in the same location this would have had bad results.

### Why move the settings. Part 2

Moving the settings was also a result of having non backwards compatible plugins between 1.x and 2.x.  If we kept both plugins in the same folder it just wouldn't work.  You would install a 1.8 version of a plugin, I would update my plugin to 2.0, you then install the same plugin in 2.0, and now you 1.8 version is broken. Fun!. To avoid this we moved all QGIS 2.0 stuff into ``./qgis2``.

### Why did my plugins break anyway.  Why not just leave them be.

In 1.x we were using SIP v1. This meant the framework we used, PyQt, felt more like C++ then it did Python.  If you are a Python developer then this isn't a very fun thing to deal with.  In SIP v1 you need to tell PyQt, and our QGIS API, what to convert the type to.  ``feature['mycolumn'].toInt()`` that is pretty gross.  In V2 you can just do ``feature['mycolumn']`` and SIP will auto convert the type for you.  This makes our API feel more like Python and less like C++.  There are other changes when using SIP V2 but you get the idea.  Unfortunately SIP v1 and v2 do not work together so we couldn't make the code backwards compatible.  This was also a forced change for us.  Once we switch to Python 3 at some stage in the future V2 would be the default and we have to change then.  The bright side of this change is most of the time you are removing code.  Consider it a good time to go though your code, give it a bit of a polish, and remove anything that is no longer needed. 

There was another major API change that needed to happen.  Vector API update.  In order to allow for multithreading in the future, and we all know everyone is looking forward to that, we needed to change how code can ask for features from a layer.  The old method would never work in a multithreaded structure and had to go.

### What can I do if I need a plugin?

Having a plugin missing from the plugin installer when you really need it can be a bit of a pain.  Plugin authors are working hard to update there plugins.  I approve about two a day into the plugin repository.  While most plugins might be updated at some stage. There are some things that you can do if you need a plugin update to work with 2.0.

1. Email the author of the plugin to see where they are at with the update

2. Email the author and offer your help to update the plugin. Remember a lot of plugins are written by volunteers who just need the plugin to get their work done and wanted to share it with everyone.

3. If the author has no intention of updating the plugin, or can't be contacted.  You are free to update you local copy and offer it back to the community as the updated copy.  If you are going to upload it back to the plugin repository please try to contact the author and seek permission first. I will be watching for copies of plugins to make sure we don't end up with 10 versions of the same plugin. The GPL allows for you to modify and share your updated version but it's nice to keep the original author in the loop.  If the author no longer wants to maintain the plugin and you are able to then contact me and I will make you the owner of the plugin. Overall be nice not evil, we are all friends here. 

4. If you don't have, or know someone with, the skills to update the plugin.  You can contact a developer to help update the plugin for you. Companies like [mine](http://mapsolutions.com.au/services.aspx), or [Faunalia](http://www.faunalia.eu/), or a whole range of other open source devs, can normally be contracted to update a plugin if needed.

### Moving forward

We like the new API. It makes the Python side of QGIS much cleaner.  There is still more work to do, it's never ending, but this is a good step. We don't like breaking plugins, but breaking a few now is better then breaking heaps as the popularity of QGIS continues to grow. 
