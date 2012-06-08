# -*- coding: utf-8 -*-

"""
    livecss.theme
    ~~~~~~~~~

    This module implements abstraction around ST theme.

"""

# std lib
from os.path import basename, normpath, relpath, exists
from random import randint
import os.path
import re

import sublime

PACKAGES_PATH = sublime.packages_path()
SUBLIME_PATH = os.path.dirname(PACKAGES_PATH)


class theme(object):
    """Global object represents ST color scheme """

    _settings_file = 'Base File.sublime-settings'
    _settings = sublime.load_settings(_settings_file)
    prefix = 'Colorized-'

    class __metaclass__(type):
        @property
        def abspath(cls):
            theme_path = cls._settings.get('color_scheme') or ""

            if theme_path.startswith('Packages'):
                theme_path = os.path.join(SUBLIME_PATH, theme_path)

            return normpath(theme_path)

        @property
        def dirname(cls):
            return os.path.dirname(cls.abspath)

        @property
        def name(cls):
            return basename(cls.abspath)

        def set(cls, theme_path):
            """Set current theme.
            :param theme: abs or relpath to SUBLIME_PATH
            """
            if exists(theme_path):
                cls._settings.set('color_scheme', relpath(theme_path, SUBLIME_PATH))

        def on_select_new_theme(cls, callback):
            cls._settings.add_on_change('color_scheme', callback)


def is_colorized(name):
    if name.startswith(theme.prefix):
        return True


def colorized_path(path):
    dirname = os.path.dirname(path)
    name = basename(path)
    return os.path.join(dirname, colorized_name(name))


def colorized_name(name):
    random = str(randint(1, 10 ** 15)) + '-'
    return theme.prefix + random + uncolorized_name(name)


def uncolorized_name(name):
    if is_colorized(name):
        s = re.search(theme.prefix + "(\d+-)?(?P<Name>.*)", name)
        self_name = s.group('Name')
        return self_name
    return name


def uncolorized_path(path):
    dirname = os.path.dirname(path)
    name = basename(path)
    return os.path.join(dirname, uncolorized_name(name))
