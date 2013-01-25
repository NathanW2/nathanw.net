---
comments: true
date: 2013-01-18 22:38:30
layout: post
slug: quick-tip-using-coalesce-to-check-for-null-or-zero
title: 'Quick Tip: Using coalesce to check for NULL or zero'
wordpress_id: 1321
categories:
- qgis
tags:
- qgis
- sql
---

Here is a quick tip that you can use in QGIS expressions, T-SQL, or even PostgresSQL.

Normally if you have a column that you need query on to find all the NULL or zeros you have to do something like this:

{% highlight sql %}
COLA IS NULL OR COLA = 0
{% endhighlight %}

Well that isn't too bad. Sure yeah it's fine for one column but what if you have three and you need to check them all together

{% highlight sql %}
(COLA IS NULL OR COLA = 0) AND (COLB IS NULL OR COLB = 0) AND (COLC IS NULL OR COLC = 0)
{% endhighlight %}

That is pretty long and gets hard to read pretty quick.

To cut this down we can use the coalesce function - [T-SQL](http://msdn.microsoft.com/en-us/library/ms190349.aspx), [PostgresSQL](http://www.postgresql.org/docs/8.1/static/functions-conditional.html), [QGIS Expression](https://raw.github.com/qgis/Quantum-GIS/master/resources/function_help/coalesce-en_US). The coalesce function returns the first non-NULL value out of an expression, or list of values. So if you do something like this:

{% highlight sql %}
coalesce(NULL, "A", 0)
{% endhighlight %}

You will get "A" because the first value is NULL. The function will just evaluate each value/expression until something turns up that isn't NULL.

Using that logic we can replace the above function with the following:

{% highlight sql %}
coalesce(COLA, 0) = 0 AND coalesce(COLB, 0) = 0 AND coalesce(COLC, 0) = 0
{% endhighlight %}

To me that is a lot clearer and readable.
