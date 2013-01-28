---
layout: index
title: Nathan's QGIS Blog
tagline: My adventures with QGIS and other GIS.
---

<div class="posts">
  {% for post in site.posts limit:5 %}
    {% unless post.draft %}
    <div class="post">
      <h4><a href="{{ post.url }}">{{post.title }}</a></h4>
      <small>Published: {{ post.date | date_to_long_string }}</small>
      {% if post.excerpt %}
	    <div class="excerpt">
	  	  <p>{{ post.excerpt | markdownify }}</p>
	     </div>
      {% endif %}
    </div>
    <hr />
    {% endunless %}
  {% endfor %}
    <h4><a href="/archive.html" title="Rocky Horror">View more in the vault</a></h4>
</div>

