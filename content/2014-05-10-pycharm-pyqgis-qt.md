title: Setting up PyCharm for PyQGIS and Qt
description: ""
category: 
tags: [dev, pycharm, qt, pyqgis]

I have been asked a few times how to setup PyCharm so you are able to do PyQGIS development, or even PyQt because that is just as great.   Rather then tell each person one at a time I thought I would throw it out as a blog post so everyone gets the benift.

The first thing we need to do is create a batch file that will load PyCharm and setup all the paths correctly. We have to do this on Windows as Qt and QGIS are not on PATH.  QGIS also ships with it's own version of copy of Python so we need to tell PyCharm about it.

The batch file is as simple as this:

```python
SET OSGEO4W_ROOT=C:\OSGeo4W
SET QGISNAME=qgis
SET QGIS=%OSGEO4W_ROOT%\apps\%QGISNAME%
SET QGIS_PREFIX_PATH=%QGIS%
SET PYCHARM="C:\Program Files (x86)\JetBrains\PyCharm 3.0\bin\pycharm.exe"

CALL %OSGEO4W_ROOT%\bin\o4w_env.bat

SET PATH=%PATH%;%QGIS%\bin
SET PYTHONPATH=%QGIS%\python;%PYTHONPATH%

start "PyCharm aware of QGIS" /B %PYCHARM% %*
```

Save this somewhere called `pycharm-pyqgis.bat` and run it.

This is a pretty basic batch file.  It just sets the variables that we need for the QGIS and Qt libs, and also sets the PYTHONHOME to the QGIS version. The magic sause here is the `set PATH`, `set PYTHONHOM`, and `set PYTHONPATH` variables.  You can just update the `OSGeo4W_ROOT`, and `PYCHARM` variables for your setup. 

After running the batch we need to setup a Python interpreter in PyCharm.   Click Configure -> Settings on the load page (or settings in the File menu).  Search for Python Interpreters, and press the green add button and select local.  Here we need to add the Python interpreter that we setup in our batch file.  In the one I posted above it will be found at `C:\OSGeo4W\bin\python.exe`. Press Ok and PyCharm will find all the python paths it needs for the setup.

![Alt Text](/images/pycharm_python.png)

Leave the settings dialog and create a new project.

![Alt Text](/images/pycharm_newproject.png)

Remember to select the interpreter that we setup for the installed version of QGIS.

That is pretty much it.  We can now create a pyqgis and pyqt app in PyCharm.

Lets give it a go

```python
from qgis.core import QgsApplication
from PyQt4.QtGui import QDialog

GUIEnabled=True
app = QgsApplication([], GUIEnabled)

dlg = QDialog()
dlg.exec_()

app.exit(app.exec_())
```

Run it in PyCharm with Alt+Shift+F10.  Good to go!
