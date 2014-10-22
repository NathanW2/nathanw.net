title: QGIS 2.0: Dealing with Null values in pyqgis
tagline: "Hard decisions are hard. Lets go home!"
description: ""
category: 
tags: [pyqgis, python]
Nothing in life ever comes free. Each time you make a desision there can sometimes be long a lasting effect.  This is exectly the case with the new QGIS 2.0 pyqgis API. Changing to the new api was a big step in order make the API clear and more Pythonic. But there was a small detail to fix. 

In QGIS 2.0 we can now just do this to read the attribute value for a field:

```python
>>> feature['yourcolumn']
"Hello World"
```

What would you expect to get if the value was NULL (not empty string). Would you expect to see ``None``?  You would think so. Right? However lets just check that.

```python
>>> feature['yourcolumn']
NULL
```

``NULL``? What the heck? That isn't ``None``! What is ``NULL``?

```python
>>> type(NULL)
<class 'PyQt4.QtCore.QPyNullVariant'>
```

``QPyNullVariant`` WA! WHAAAT! Why didn't we get None? Turns out by removing ``QVariant`` from PyQt it had some impact on methods that expected a NULL QVariant  - A QVariant with no value. Passing None didn't work because those methods needed the type information that QVariant holds, even when NULL.  

When using SIP V2, which is what QGIS 2.0 is using, PyQt will auto convert any Null QVariants to ``QPyNullVariant``.

The ``NULL`` you see is a variable masking the QPyNullVariant so that the output is nicer and it's easier to work with. We have also added a bunch of methods to QPyNullVariant in order to make it act as much like None as we can.  

If you see a ``NULL`` this is how you can deal with it:

```python
>>> feature['yourcolumn']
NULL

>>> if not feature['nullcolumn']:
>>> 	print "Was null"
Was null

>>> if feature['nullcolumn'] == NULL:
>>>	print "Was null"
Was null 
```

``NULL`` will also return ``False`` if boolean checked:

```python
>>> value = NULL
>>> if value:
...	print "This value wasn't null"
... else:
... 	print 'This value was null' 
This value was null
```

It will also be equal to any other ``NULL`` aka ``QPyNullVariant`` variable

```python
>>> value = NULL
>>> value2 = NULL
>>> value == value2
True
>>> value = 100
>>> value2 = NULL
>>> value == value2
False 
```

## Does None is NULL work? No.
One way to check if something is Null in Python is to use ``value is None`` however this will not work with our ``NULL`` type. Overloading the ``is`` operator in Python is not supported and there is no way we can support this - trust me I have tried.  ``is`` is really doing ``id(object) == id(object)`` under the hood:

DO NOT do the following if you are checking for null values in pyqgis unless you know the return type is ``None``:

```python
>>> value = NULL
>>> value is None
false
```

