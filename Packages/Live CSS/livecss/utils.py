# -*- coding: utf-8 -*-

"""
    livecss.colorizer
    ~~~~~~~~~

    This module implements some useful utilities.

"""
import sublime

# local imports

from .config import Config
from .state import state_for
from .theme import theme, uncolorized_path
from .colorizer import colorize_file
from .menu import create_menu


def colorize_on_select_new_theme(view):
    state = state_for(view)
    if not state.theme_path:
        return
    if uncolorized_path(state.theme_path) != uncolorized_path(theme.abspath):
        # here is small hack to colorize after we change the theme
        # TODO: find out better solution
        sublime.set_timeout(lambda: colorize_file(view, state, True), 200)


def generate_menu(view):
    config = Config(view)
    global_opt = config.global_on
    local_opt = config.local_on
    create_menu(local_opt, global_opt)


def file_id(view):
    return view.file_name() or view.buffer_id()


def is_colorizable(view):
    point = view.sel()[0].begin()
    file_scope = view.scope_name(point).split()[0]
    if file_scope in ['source.scss', 'source.css', 'source.css.less']:
        return True


def need_colorization(view):
    if not is_colorizable(view):
        return

    config = Config(view)
    global_on = config.global_on
    local_on = config.local_on
    if not local_on:
        return False
    if global_on:
        return True


def need_uncolorization(view):
    if not is_colorizable(view):
        return

    config = Config(view)
    global_on = config.global_on
    if not global_on:
        return True
