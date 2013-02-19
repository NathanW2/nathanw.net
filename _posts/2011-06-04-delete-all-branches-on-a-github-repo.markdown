---
comments: true

layout: post
slug: delete-all-branches-on-a-github-repo
title: Delete all branches on a github repo
wordpress_id: 636
categories:
- Open Source
- qgis
tags:
- git
- Open Source
- OSS
- qgis
- Quantum GIS
---

I forked the QGIS repo on GitHub a little while ago although one thing that bothered me was that it gave me copies of all the branches that the main QGIS git repo had.  This is understandable as it's the way it works however I don't really need all these branches in my forked copy of the repo as I don't care about them.   I only care the ones I am working on, and I don't want to see a big list of branches in my git fork that have nothing to do with me.

So the next question was how do I delete all the branches on the remote repo at GitHub. Well you would normally do:

    
    
    git push origin :branch_name


although doing that by hand for each branch is, well, a pain in the butt! After a chat with a guy (strk) on the #qgis IRC channel who is more skilled at bash then me (I'm still a Linux noob) he came up with this:

    
    git branch -r | grep origin/ | grep -v master | grep -v HEAD| cut -d/ -f2 | while read line; do git push origin :$line; done;


Very handy.
