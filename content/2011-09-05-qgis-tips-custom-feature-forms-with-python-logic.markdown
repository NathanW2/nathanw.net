slug: qgis-tips-custom-feature-forms-with-python-logic
title: QGIS Tips - Custom feature forms with Python logic
categories:
- Open Source
- qgis
tags:
- FOSSGIS
- gis
- Open Source
- qgis
- qgis-editing
- Quantum GIS

Last week I found a nice little undocumented feature of QGIS. I plan on writing documentation, so it won't stay that way for long but I thought I would post about it first and run though it step by step.

_This post is going to be a follow up post based on what Tim Sutton did for the same subject back in 2009 at [http://linfiniti.com/2009/11/creating-dynamic-forms-a-new-feature-headed-for-qgis-1-4/ ](http://linfiniti.com/2009/11/creating-dynamic-forms-a-new-feature-headed-for-qgis-1-4/)_

For data entry one feature I really like in QGIS is the automatic feature edit forms with support for textboxs, dropdowns and all sorts of other cool Qt controls to make data entry a breeze.

However one thing that people might not be aware of is that you can have a custom forms for data entry. QGIS will take care of setting all the fields and then saving the values back to your layer.

This could be handy if you want to have say a logo, some validation and maybe some text to help the user fill in the form correctly. Or just a custom form layout because you can.

One thing Tim didn't follow up on was a post about how to add custom Python logic to the form, which I think is the coolest feature of having these custom forms.

So lets get started.


## Creating the custom form


This process is pretty much the same as what Tim outlined in his [blog post](http://linfiniti.com/2009/11/creating-dynamic-forms-a-new-feature-headed-for-qgis-1-4/) however I'm going to go over it again for completeness.

In order to create the custom form you will need to install Qt Desinger. For windows I haven't found a way to just install the desinger although if you have QGIS installed it is normally installed with the Qt framework and can be found at C:\OSGeo4w\bin\designer.exe. If you're on Linux you can run something like

```bash
sudo apt-get install qt4-designer
```

_Ohh how I wish windows had a package management system :( _

Fire up Qt Desinger and select "Dialog with Buttons Bottom".

Lets throw on a couple of Labels and a few Line Edits for the data. Now set the form to use a Grid Layout (Right Click on empty space on form->Layout->Layout in Grid).

Now the trick in making a custom form for QGIS is naming the object the same as the field. So I my case I have a road layer with the following fields.

- Segment_ID
- Parcel_ID
- Name
- Alias_Name
- Locality
- Parcel_type

For my custom form I only care about Segment_ID and Name, so my form looks like:

[![](http://woostuff.files.wordpress.com/2011/09/designer.png)](http://woostuff.files.wordpress.com/2011/09/designer.png)

_Note that I have set the read only property of the Segment ID line edit to True so that it can't be edited. I don't want people messing around with the ID._

As I said above the tick is in the naming so right click on each line edit and select Change objectName, naming each line edit using the same name as the field. For me the first control is called Segment_ID and the other is called Name.

[![](http://woostuff.files.wordpress.com/2011/09/objectnaming.png)](http://woostuff.files.wordpress.com/2011/09/objectnaming.png)

Save the form into a new folder, I have put mine in C:\Temp\Roads. Jump back into QGIS, load the properties dialog for the layer. Select the General tab and set Edit UI to the new form .ui file.

[![](http://woostuff.files.wordpress.com/2011/09/properties.png)](http://woostuff.files.wordpress.com/2011/09/properties.png)

Save and exit the properties window. Enable the layer for editing (or not) and select an object with the Identify Feature tool.

[![](http://woostuff.files.wordpress.com/2011/09/mapwithform.png)](http://woostuff.files.wordpress.com/2011/09/mapwithform.png)

Magic! As I'm in edit mode any changes I make to the Name line edit will be reflected back on the layer (but not the Segment ID as it's read only). If you are in non-edit mode then you are given the custom form with everything disabled and a cancel button.


## With Python validation and custom logic.


Now creating a custom form like above is pretty cool although having some custom Python validation behind it would be even cooler.

What I want to do is add some validation to the Name field so the user can't enter null road names.

First save your QGIS project (as the Python code runner will look where the project is saved for the Python module). Again I have saved mine in C:\Temp\Roads as Roads.qgs. Now lets make a new python file in your favourite text editor and add the following code.

```python
from PyQt4.QtCore import *
from PyQt4.QtGui import *

nameField = None
myDialog = None

def formOpen(dialog,layerid,featureid):
	global myDialog
	myDialog = dialog
	global nameField
	nameField = dialog.findChild(QLineEdit,"Name")
	buttonBox = dialog.findChild(QDialogButtonBox,"buttonBox")

	# Disconnect the signal that QGIS has wired up for the dialog to the button box.
	buttonBox.accepted.disconnect(myDialog.accept)

	# Wire up our own signals.
	buttonBox.accepted.connect(validate)
	buttonBox.rejected.connect(myDialog.reject)

def validate():
  # Make sure that the name field isn't empty.
	if not nameField.text().length() > 0:
		msgBox = QMessageBox()
		msgBox.setText("Name field can not be null.")
		msgBox.exec_()
	else:
		# Return the form as accpeted to QGIS.
		myDialog.accept()
```

Wow! What the hell is all that! I'll step though the code to explain each bit.


### Code break down.


First import the modules from Qt and set up a few global variables to hold the dialog and name field.

```python
from PyQt4.QtCore import *
from PyQt4.QtGui import *

nameField = None
myDialog = None
```

Now we create a method that QGIS will call when it loads the form. This method takes an instance of our custom dialog, the Layer ID, and the Feature ID.

```python
def formOpen(dialog,layerid,featureid):
```

Then using the findChild method we want to grab the reference to the Name field and the button box. We are also calling buttonBox.accepted.disconnect() to disconnect the slots that QGIS has auto wired up to our button box, we do this so we can hook up our own accepted logic.

After we have disconnected the accepted signal we can wire up our own call to the validate method using buttonBox.accepted.connect(validate).

```python
global myDialog
myDialog = dialog
global nameField
nameField = dialog.findChild(QLineEdit,"Name")
buttonBox = dialog.findChild(QDialogButtonBox,"buttonBox")

# Disconnect the signal that QGIS has wired up for the dialog to the button box.
buttonBox.accepted.disconnect(myDialog.accept)
# Wire up our own signals.
buttonBox.accepted.connect(validate)
buttonBox.rejected.connect(myDialog.reject)
```

We need a method to validate the logic. This will be called when the signal buttonBox.accepted() is called. The logic in this method should be pretty streight forward. If the Name line edit has a length > 0 then we accept the dialog, if not then we give the user a message and let them fix the mistake.

```python
def validate():
  # Make sure that the name field isn't empty.
	if not nameField.text().length() > 0:
		msgBox = QMessageBox()
		msgBox.setText("Name field can not be null.")
		msgBox.exec_()
	else:
		# Return the form as accpeted to QGIS.
		myDialog.accept()
```


## Almost done!


Now that you have a Python file with the custom validation logic we need to tell QGIS to use this logic for the form. First save the Python file in the same directory as your project. I have called mine C:\Temp\Roads\RoadForm.py.

Back on the General tab in the layer properties we can set the Init function field. We set this to call the module and function we just made. The syntax is {module name}.{function name}. In my case my module (the Python file we made before) is called RoadForm and the function is called formOpen, so it will be RoadForm.formOpen.

[![](http://woostuff.files.wordpress.com/2011/09/propertiesupdated.png)](http://woostuff.files.wordpress.com/2011/09/propertiesupdated.png)

Save and use the Identify Feature tool to select a feature. You shouldn't get any errors if everything worked ok. Now delete everything in the Name field and hit Ok.

[![](http://woostuff.files.wordpress.com/2011/09/validate.png)](http://woostuff.files.wordpress.com/2011/09/validate.png)

Sweet! The form can now not be accepted if the name field is null.

And that's that. Pretty simple but powerful feature once you know how to set it up.

Enjoy!

_If you do end up using this custom form with python logic stuff in the real world, leave a comment and maybe a picture. It would be good to see use cases for this cool QGIS feature._

**Bonus**

Why not add a red highlight to the textbox if something is not valid.

```python
from PyQt4.QtCore import *
from PyQt4.QtGui import *

nameField = None
myDialog = None

def formOpen(dialog,layerid,featureid):
  global myDialog
  myDialog = dialog
  global nameField
  nameField = dialog.findChild(QLineEdit,"Name")
  buttonBox = dialog.findChild(QDialogButtonBox,"buttonBox")

  nameField.textChanged.connect(Name_onTextChanged)
  # Disconnect the signal that QGIS has wired up for the dialog to the button box.
  buttonBox.accepted.disconnect(myDialog.accept)
  # Wire up our own signals.
  buttonBox.accepted.connect(validate)
  buttonBox.rejected.connect(myDialog.reject)

def validate():
  # Make sure that the name field isn't empty.
  if not nameField.text().length() > 0:
    nameField.setStyleSheet("background-color: rgba(255, 107, 107, 150);")
    msgBox = QMessageBox()
    msgBox.setText("Name field can not be null.")
    msgBox.exec_()
  else:
  # Return the form as accpeted to QGIS.
    myDialog.accept()

def Name_onTextChanged(text):
  if not nameField.text().length() > 0:
    nameField.setStyleSheet("background-color: rgba(255, 107, 107, 150);")
  else:
    nameField.setStyleSheet("")
```

The key part of of this is nameField.textChanged.connect(Name_onTextChanged) and the Name_onTextChanged(text) method. Give it a try, I think it looks quite nice.

[![](http://woostuff.files.wordpress.com/2011/09/form.png)](http://woostuff.files.wordpress.com/2011/09/form.png)
