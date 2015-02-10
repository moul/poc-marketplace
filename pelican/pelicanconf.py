#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os.path

AUTHOR = u'Online Labs'
SITENAME = u'Online Labs Marketplace'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins')
]
PLUGINS = ['gravatar']

DEFAULT_METADATA = {
    'icon': 'https://cloud.online.net/images/69f046ad.image_default.jpg',
    'author': 'Online Labs',
    'email': 'opensource@ocs.online.net',
    'version': 'latest',
    'date': '2015-01-01 23:42',
    'category': 'Community',
}
