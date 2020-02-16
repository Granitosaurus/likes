#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# modify theses
AUTHOR = 'Bernard'
SITENAME = 'Stuff Bernard Likes'
SITEURL = ''
LINKS = (  # footer links
    ('made with WIL', 'http://github.com/granitosaurus/wil'),
    ('pelican', 'https://github.com/getpelican/pelican/'),
    ('blog', 'http://granitosaurus.rocks'),
)

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
THEME = 'wil'
USE_FOLDER_AS_CATEGORY = False  # wil doesn't care about categories
DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = ['img', 'thumb']
