---
layout: post
title: "My QGIS git workflow"
description: ""
category: git
tags: [git qgis]
---


I thought it might be handy to post the git workflow that I use when working on QGIS, or any project for that matter.

In the following examples `upstream = https://github.com/qgis/Quantum-GIS.git`.  If you have cloned from your github fork of QGIS you can add `upstream` using:

{% highlight bash %}
$ git remote add upstream https://github.com/qgis/Quantum-GIS.git
{% endhighlight %}

The first thing we need to do is pull down the latest changes from the main QGIS repo aka `upstream` 


{% highlight bash %}
$ git fetch upstream
remote: Counting objects: 13, done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 7 (delta 6), reused 7 (delta 6)
Unpacking objects: 100% (7/7), done.
From github.com:qgis/Quantum-GIS
   18cd145..89bdb10  master     -> upstream/master
{% endhighlight %}

Now that we have the changes in our local repo we need to bring our master branch up to date with the latest changes from upstream.  I use `rebase` here because I don't want to see `merge master into master etc etc` each time I want to bring my master branch up to date. In the end I want my local `master` branch to reflect `upstream/master` exactly  

{% highlight bash %}
$ git rebase upstream/master
First, rewinding head to replay your work on top of it...
Fast-forwarded master to upstream/master.
{% endhighlight %}

*Note: You can combine the two into one call using: `git pull upstream master --rebase`*

In order to do any work in git you should really be using branches.  We can check a new one out using:

{% highlight bash %}
$ git checkout -b working
Switched to a new branch 'working'
{% endhighlight %}

This will checkout a new `working` branch off my local master branch and switch to it.

Lets do some work.

{% highlight bash %}
$ git commit -a -m "Add some feature"
[working 8cd2f4b] Add some feature

$ git commit -a -m "More feature stuff"
[working 72d30ad] More feature stuff

$ git commit -a -m "bug fix"
[working 25b10e5] bug fix

$ git commit -a -m "bug fix"
[working 211e387] bug fix
{% endhighlight %}

*Note: The `-a` means add any changed files to the commit. You can also use `git add`. I'm trusting you already understand how to add files to a commit.*

Now at this point I could merge my changes into the `master` branch and push it up, or if you don't have commit rights you can issue a pull request. However having heaps of "fix this", "fix that" commits is pretty ugly.  This is where git rebase can come in handy.

We can check which commits we have added that are not in master by doing:

{% highlight bash %}
$ git log --oneline master..
211e387 bug fix
25b10e5 bug fix
72d30ad More feature stuff
8cd2f4b Add some feature
{% endhighlight %}

{% image git2.png %}
{% endimage %}

There we can see we have four commits that differ and that `8cd2f4b` is the first commit we made.  I really want to merge all the commits into one to make this a little cleaner.

{% highlight bash %}
$ git rebase -i 8cd2f4b^
{% endhighlight %}

*Note: `^` means go back one commit from the one listed.  git rebase doesn't include the commit that you list so you have to go back one before it.*

{% highlight bash %}
pick 8cd2f4b Add some feature
f 72d30ad More feature stuff
f 25b10e5 bug fix
f 211e387 bug fix

# Rebase 89bdb10..7d02daf onto 89bdb10
#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# If you remove a line here THAT COMMIT WILL BE LOST.
# However, if you remove everything, the rebase will be aborted.
{% endhighlight %}

I have changed all but the first commit to `f` this will merge all the commits into the first one. The latest commit is at the bottom so you should read the rebase screen from bottom up.

{% highlight bash %}
[detached HEAD d5620a5] Add some feature
 1 file changed, 3 insertions(+)
 create mode 100644 test.txt
Successfully rebased and updated refs/heads/working.
{% endhighlight %}

{% image git1.png %}
{% endimage %}

At this point I normally merge it into master and push it upstream, but if you don't have commit rights then you can push it up to your github repo and open a pull request.

{% highlight bash %}
# Push them up for review
$ git push myrepo working
{% endhighlight %}

<div class="alert alert-block"><h4>Important Note:</h4> git rebase -i will change the commit hash for anything that is included in the range of commits. Make sure you only rebase commits that are not public yet. Only rebase commits that in your local repo.</div>
