# -*- coding: utf-8 -*-
import pygame

class Theme(object):
    """
    Theme related stuff
    """
    def __init__(self, theme):
        self._theme = theme

    def __getitem__(self, screen):
        gg = {'pygame': pygame}
        execfile('themes/%s/%s.py' % (self._theme, screen), gg)
        return gg[screen]
