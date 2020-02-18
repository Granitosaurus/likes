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
DEFAULT_PAGINATION = 20  # more pages will load longer

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
THEME = 'wil'
USE_FOLDER_AS_CATEGORY = False  # wil doesn't care about categories
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['img', 'thumb']

# plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['thumbnailer']
IMAGE_PATH = 'img'
THUMBNAIL_DIR = 'thumb'
THUMBNAIL_SIZES = {
    '': '300x?'  # set thumbnails to 300 width and scaled height
}
THUMBNAIL_KEEP_NAME = True
