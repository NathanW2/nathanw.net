---
layout: index
title: Nathan's QGIS Blog
tagline: My adventures with QGIS and other GIS.
---
<div class="posts">
  {% for post in site.posts limit:5 %}
    <div class="post">
      <div class="title"><a href="{{ post.url }}">{{post.title }}</a></div>
      <small>Published: <b> {{ post.date | date_to_long_string }}</b></small>
      {% if post.excerpt %}
	  <blockquote>
	  	  <p>{{ post.excerpt | markdownify }}</p>
	  </blockquote>
      {% endif %}
    </div>
    <hr />
  {% endfor %}
</div>

