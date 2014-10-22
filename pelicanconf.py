#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nathan Woodrow'
SITENAME = u"Nathan's QGIS Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Brisbane'

DEFAULT_LANG = u'en'

THEME = 'themes/pelican-svbhack'

USER_LOGO_URL = SITEURL + '/images/bio.jpg'

TAGLINE = 'QGIS Developer, Python (Monty and code) fan'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'md5'

DISQUS_SITENAME = 'nathansqgisblog'
GOOGLE_ANALYTICS = 'UA-5231515-7'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('GitHub', 'https://github.com/NathanW2'),
          ('Twitter', 'https://twitter.com/madmanwoo'),
          ('Google+', 'https://plus.google.com/u/0/109990125267312011029/posts'))

DEFAULT_PAGINATION = 10

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
