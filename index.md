---
layout: page
title: Nathan's QGIS Blog
tagline: A blog about my adventures with QGIS and other GIS.
---
    
## Posts

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

