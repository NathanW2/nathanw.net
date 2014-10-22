title: Death to the message box! Use the QGIS messagebar
description: ""
category: 
tags: []

The good ol' message box. So easy to use. Yet such as stab in the users user experience metaphorical heart.  Nothing like working along and getting a nice dialog to tell you can't do something or that the operation has finished

![Alt Text](/images/dave.png)

![Alt Text](/images/info.png)

You might think. "Well there isn't really anything wrong with that. I needed to tell the user everything is done". Sure but what you didn't need to do was stop the user and make them acknowledge it. Consider if your car made you OK something you each time your speed changed.

![Alt Text](/images/speed.png)

![Alt Text](/images/speed2.png)

![Alt Text](/images/speed3.png)

Pretty annoying.

What is the alternative then? 

Introducing the QGIS message bar

![Alt Text](/images/errorbar.png)

![Alt Text](/images/infobar.png)

![Alt Text](/images/warningbar.png)

If you have been using QGIS 1.9 (the dev version for 2.0) you might have noticed it already.  It's a great new way for us to let the user know about something without blocking their work or getting in the way.  The best part is your can even access the message bar to post messages from your plugins.

```python
iface.messageBar().pushMessage("Error", "I'm sorry Dave, I'm afraid I can't do that", level=QgsMessageBar.CRITICAL)
``` 

![Alt Text](/images/errorbar.png)

It even has timer to show a message for a limited time.

```python
iface.messageBar().pushMessage("Error", "I'm sorry Dave, ..", level=QgsMessageBar.CRITICAL, duration=3)
``` 

![Alt Text](/images/errorbar-timed.png)

or showing a button for more info

```python
def showError():
    pass

widget = iface.messageBar().createMessage("Missing Layers", "Show Me")
button = QPushButton(widget)
button.setText("Show Me")
button.pressed.connect(showError)
widget.layout().addWidget(button)
iface.messageBar().pushWidget(widget, QgsMessageBar.WARNING)
``` 

![Alt Text](/images/bar-button.png)

### In your own widgets

You can even use a message bar in your own dialog so you don't have to show a message box or if it doesn't make sense to show it in the main QGIS window.

```python
class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.bar = QgsMessageBar()
        self.bar.setSizePolicy( QSizePolicy.Minimum, QSizePolicy.Fixed )
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.buttonbox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonbox.accepted.connect(self.run)
        self.layout().addWidget(self.buttonbox , 0,0,2,1)
        self.layout().addWidget(self.bar, 0,0,1,1)
        
    def run(self):
        self.bar.pushMessage("Hello", "World", level=QgsMessageBar.INFO)
```

![Alt Text](/images/dialog-with-bar.png)

### Don't abuse it

Like anything the message bar can be abused if not careful.  Avoid dumping debugging messages to it as this will annoy users rather then help.  Use ``QgsMessageLog.logMessage()`` if you need to write debugging information.  Also consider which messages you post there as posting too many messages will mean the user might just ignore it like they do with message boxes. 