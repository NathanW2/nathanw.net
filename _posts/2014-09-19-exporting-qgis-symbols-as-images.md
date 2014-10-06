---
layout: post
title: "Exporting QGIS symbols as images"
tagline: "Why? Because we can"
description: ""
category: 
tags: [qgis, pyqgis]
---

Ever wanted to export your QGIS symbols as images? Yes. Well here is some Python code that will let you do just that:

{% highlight python %}
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QImage, QPainter

style = QgsStyleV2.defaultStyle()
names = style.symbolNames()
size = QSize(64, 64)

for name in names:
    symbol = style.symbol(name)
    if not symbol.type() == QgsSymbolV2.Marker:
        continue
    
    image = QImage(size, QImage.Format_ARGB32_Premultiplied)
    image.fill(0) 
    painter = QPainter(image)
    symbol.drawPreviewIcon(painter, size)
    painter.end()
    image.save(r"C:\temp\{}.png".format(name), "PNG")
{% endhighlight %}

Or in 2.6 it's even easier:

{% highlight python %}
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QImage, QPainter

style = QgsStyleV2.defaultStyle()
names = style.symbolNames()
size = QSize(64, 64)

for name in names:
    symbol = style.symbol(name)
    if not symbol.type() == QgsSymbolV2.Marker:
        continue
        
    image = symbol.asImage(size)
    image.save(r"C:\temp\{}.png".format(name), "PNG")
{% endhighlight %}

Bam! 

{% image symbols.png %}
{% endimage %}

Why?  Because we can.