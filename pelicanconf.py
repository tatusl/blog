#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITEURL = u'http://mozz.kapsi.fi/blog'
AUTHOR = 'Tatu Seppä-Lassila'
FIRSTNAME = 'Tatu'
LASTNAME = 'Seppä-Lassila'
SITENAME = 'Tatu Seppä-Lassila'
SITETITLE = 'Tatu Seppä-Lassila'
SITESUBTITLE = 'General IT enthusiast'
PROFILE_IMAGE = 'profile.jpg'
BIO = 'Some cool description here. And also something. And this fact, and that. More placeholder text..'

THEME = "themes/hyde"

STATIC_PATHS = ['images']

SOCIAL = (('linkedin', 'https://fi.linkedin.com/in/tatuseppalassila'),
          ('github', 'https://github.com/tatusl'),
          ('instagram', 'https://www.instagram.com/tssela/'),
          ('twitter', 'https://twitter.com/tatusl'))

FEED_ALL_RSS = SITEURL + '/feeds/all.atom.xml'

ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

TIMEZONE = 'Europe/Helsinki'
