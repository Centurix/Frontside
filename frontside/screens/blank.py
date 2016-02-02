# -*- coding: utf-8 -*-
from screen import Screen


class Blank(Screen):
    """
    A basic blank screen for interstitial overlays
    """
    def __init__(self, config):
        super(self.__class__, self).__init__(config)
