---
layout: index
title: Nathan's QGIS Blog
tagline: My adventures with QGIS and other GIS.
---
<h1> Recent posts </h1>
<div class="posts">
  {% for post in site.posts limit:10 %}
    {% unless post.draft %}
    <div class="post">
      <h2><a href="{{ post.url }}">{{post.title }}</a></h2>
      <small>Published: {{ post.date | date_to_long_string }}</small>
    </div>
    <hr />
    {% endunless %}
  {% endfor %}
    <h4><a href="/archive.html" title="Rocky Horror">View more in the vault</a></h4>
</div>

