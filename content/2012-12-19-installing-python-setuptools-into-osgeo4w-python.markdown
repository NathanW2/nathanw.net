slug: installing-python-setuptools-into-osgeo4w-python
title: Installing Python setuptools into OSGeo4W Python
categories:
- Open Source
tags:
- FOSSGIS
- osgeo
- python
- qgis
- Quantum GIS



The easiest way install Python libraries is to use `easy_install` and `pip`.  `easy_install` and `pip` are package managers for Python. From the easy_install page:



> Easy Install is a python module (easy_install) bundled with setuptools that lets you automatically download, build, install, and manage Python packages.


and from the [pip](http://pypi.python.org/pypi/pip) page:


> pip is a tool for installing and managing Python packages, such as those found in the [Python Package Index](http://pypi.python.org/pypi). It's a replacement for [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall).

To get easy_install you need to install Python [setuptools](http://pypi.python.org/pypi/setuptools) and you are good to go. Sounds easy!  However the setuptools installer assumes that you have the normal standalone Python installed which writes it's install location to the registry, and when you run the installer it will say that it can't find Python on the system. What the!?

If you have installed QGIS, or any other tool from the OSGeo4W install, you will see that OSGeo4W bundles its own version of Python in: `C:\OSGeo4W\apps\python27.` This is the Python that is used when calling python in the OSGeo4W shell.  It seems someone on the OSGeo wiki has made a bootstrapped installer for setuptools that will install setuptools and easy_install into the  C:\OSGeo4W\apps\python27 folder for you.


## Steps to take

  * Download [ez_setup.py](http://peak.telecommunity.com/dist/ez_setup.py)	
  * Run `python ez_setup.py` in your OSGeo4W shell
  * Done!


To install a package with easy_install just use:

	easy_install {packagename}

I wanted to have [bottle](http://bottlepy.org/docs/dev/) and [flask](http://flask.pocoo.org/) installed:

	easy_install bottle

which gives you something like:

	Searching for bottle
	Reading http://pypi.python.org/simple/bottle/
	Reading http://bottle.paws.de/
	Reading http://github.com/defnull/bottle
	Reading http://bottlepy.org/
	Best match: bottle 0.11.4
	Downloading http://pypi.python.org/packages/source/b/bottle/bottle-0.11.4.tar.gz#md5=f767c340de0b7c9581917c48e609479b
	Processing bottle-0.11.4.tar.gz
	Running bottle-0.11.4\setup.py -q bdist_egg --dist-dir c:\users\woo\appdata\local\temp\easy_install-5b4qq6\bottle-0.11.4\egg-dist-tmp-q2yd68
	zip_safe flag not set; analyzing archive contents...
	bottle: module references __file__
	bottle: module references __path__
	Adding bottle 0.11.4 to easy-install.pth file
	Installing bottle.py script to C:\OSGeo4W\apps\Python27\Scripts
	Installed c:\osgeo4w\apps\python27\lib\site-packages\bottle-0.11.4-py2.7.egg
	Processing dependencies for bottle
	Finished processing dependencies for bottle



## Install pip

  * You should also install pip as it is a [better package manager](http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install) then easy_install

  * Just run `easy_install pip`

## Note

Most of the time any Python packages that are needed by your OSGeo4W tools are bundled in the installer and can be downloaded using the OSGeo4W installer, however there have been cases when I wanted to install a non OSGeo4W package into my setup by using easy_install or pip. Like bottle and flask in the example above.
