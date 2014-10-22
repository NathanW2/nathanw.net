title: Keeping QGIS settings in sync on different machines
description: ""
category: qgis
tags: [qgis, settings]

Here is a quick tip from a [GIS.SE](http://gis.stackexchange.com/questions/87393/how-can-i-centralize-qgis-connections-for-multiple-qgis-installations) post that I answered the other day.

The topic was keeping the WMS settings in sync over different operating systems and machines.  Normally QGIS will store it settings in the registry on Windows and in different locations on Linux and OS X.  So then comes the question of how do you keep them in sync if you are using different machines.

Well the answer is simple.  QGIS provides `--optionspath` and `--configpath` command line options in order to move the `.qgis2` and settings files.    Using these two options, or just the one depending on what you need, will allow you to store the QGIS settings in a different location.  Rather then storing the settings in the registry, or .config and .plist files, it will create a `.ini` file and save everything there. 

All in all this means you can redirect your QGIS settings to a folder on dropbox and tell your QGIS installs to load the settings from a single place keeping everything in sync.  When you change a setting it will sync with Dropbox and onto your other machines.

The simple way on Windows to add the `--optionspath` and `--configpath` options is to copy the shortcut to QGIS and append it to the end of the Target.

```
--optionspath "F:\mydropbox\qgis" --configpath "F:\mydropbox\qgis"
```

QGIS IN THE CLOUD!!11! _ok not really but still cool_
