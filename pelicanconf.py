#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#SITEURL = u'http://mozz.kapsi.fi/blog'
AUTHOR = 'Tatu Seppä-Lassila'
FIRSTNAME = 'Tatu'
LASTNAME = 'Seppä-Lassila'
SITENAME = 'Tatu Seppä-Lassila'
SITESUBTITLE = 'Blog'
PROFILE_IMAGE = 'profile.jpg'
BIO = 'Some cool description here. And also something. And this fact, and that. More placeholder text..'

THEME = "themes/hyde"

STATIC_PATHS = ['images']

SOCIAL = (('linkedin', 'https://fi.linkedin.com/in/tatuseppalassila'),
          ('github', 'https://github.com/tatusl'),
          ('instagram', 'https://www.instagram.com/tssela/'),
          ('twitter', 'https://twitter.com/tatusl'))

# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATIVE_URLS = True

DEFAULT_PAGINATION = 5

ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

TIMEZONE = 'Europe/Helsinki'

#DISQUS_SITENAME = ""
